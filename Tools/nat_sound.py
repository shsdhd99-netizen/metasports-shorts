"""Real-audio ("nat sound") mix for moment Shorts (Oct 28 2026; owner: "for all clips that are viral, experiment with using the
actual audio for the moment").

  python Tools/nat_sound.py --folder "<Short folder>" --video final_voiceonly.mp4 --out final_live.mp4 --burst 12.2-16.35
         [--burst A-B ...] [--bed-db -15] [--tail 0.06] [--clip-db P11=-40 ...] [--burst-lufs -15] [--target-lufs -14]

Builds a track from the source clips' own audio (crowd, commentator), lined up with every shot on the timeline, and mixes it
under the narration of an already-rendered video (render it first with assemble.py --no-music; its audio is voice + effects):
- each shot plays its source's audio from the clip's "at" (cuts.json), so the sound matches the picture;
- a slowed replay (cuts.json "speed" < 1) keeps the previous shot's audio running instead (no repeated or warped call);
- outside a burst the track is a bed, --bed-db below the burst level (default -15 dB: crowd and a murmur of the call);
- inside a burst (a window where the narration stops, e.g. the live "for the win!" call and the roar) it plays at full level.
  Make the window in the voice first: cut the narration words out and insert silence (see the #75 _realaudio folder).
  The same works for a real quote: play the speaker's own words in a window, with the quote shot cut from the same second
  of the source so the lips match (#76 _realaudio). Mark those words "live": true in words.json so captions show them.
Each burst is levelled on its own to --burst-lufs (clips can differ by 15 dB); the bed sits --bed-db under the bursts' overall
level; the whole mix is then set to --target-lufs with a limiter.
Broadcast audio raises the chance of a Content ID claim compared with footage alone: keep the original version as the fallback.
"""
import argparse, json, os, subprocess, sys
import numpy as np

SR = 48000


def pcm(path, start, dur):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(start, 0):.3f}", "-t", f"{dur:.3f}", "-i", path, "-vn", "-ac", "1",
                        "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True)
    a = np.frombuffer(r.stdout, dtype=np.float32).copy()
    n = int(round(dur * SR))
    return np.pad(a, (0, max(0, n - len(a))))[:n]


def lufs_of(a):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", "ebur128", "-f", "null", "-"], input=a.astype(np.float32).tobytes(), capture_output=True)
    import re
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", p.stderr.decode(errors="ignore"))
    return float(m[-1]) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--video", required=True, help="rendered video inside the folder (voice + effects, no music)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--burst", action="append", default=[], help="start-end seconds where the real audio plays at full level")
    ap.add_argument("--bed-db", type=float, default=-15.0)
    ap.add_argument("--tail", type=float, default=0.06, help="seconds each burst takes to fade down to the bed after its end "
                    "(e.g. 0.8 lets a roar die away under the first narrated words)")
    ap.add_argument("--burst-lufs", type=float, default=-15.0)
    ap.add_argument("--target-lufs", type=float, default=-14.0)
    ap.add_argument("--clip-db", action="append", default=[], help="CLIP=dB: a different bed level for one shot, e.g. P11=-40 to keep a\n"
                    "talking head's own voice from murmuring under the narration")
    a = ap.parse_args()
    F = a.folder
    cuts = json.load(open(os.path.join(F, "cuts.json")))
    shots = json.load(open(os.path.join(F, "shots.json")))
    video = os.path.join(F, a.video)
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                                 capture_output=True, text=True).stdout)
    by_clip = {c["clip"]: c for c in cuts["shots"]}
    nat = np.zeros(int(round(total * SR)), dtype=np.float32)
    fade = int(0.04 * SR)
    prev = None  # (source path, source time at the end of the previous shot)
    clip_db = {k: float(v) for k, v in (x.split("=") for x in a.clip_db)}
    bed_override = []  # (t0, t1, linear gain) for shots with their own bed level
    for i, s in enumerate(shots):
        t0 = s["start"]
        t1 = shots[i + 1]["start"] if i + 1 < len(shots) else total
        c = by_clip[os.path.splitext(s["clip"])[0]]
        src = os.path.join(F, cuts["sources"][c["src"]])
        if c.get("speed", 1.0) < 1.0 and prev:
            src, at = prev  # slowed replay: keep the live sound running
        else:
            at = c["at"]
        seg = pcm(src, at, t1 - t0)
        seg[:fade] *= np.linspace(0, 1, fade); seg[-fade:] *= np.linspace(1, 0, fade)
        i0 = int(round(t0 * SR)); nat[i0:i0 + len(seg)] += seg[:len(nat) - i0]
        prev = (src, at + (t1 - t0))
        name = os.path.splitext(s["clip"])[0]
        if name in clip_db:
            bed_override.append((t0, t1, 10 ** (clip_db[name] / 20)))
        print(f"  {s['clip']:<9} {t0:6.2f}-{t1:6.2f}  {os.path.basename(src)} from {at:.2f}" + (" (slowed: live sound continues)" if c.get("speed", 1.0) < 1.0 else ""))
    bursts = [tuple(float(x) for x in b.split("-")) for b in a.burst]
    t = np.arange(len(nat)) / SR
    env = np.full(len(nat), 10 ** (a.bed_db / 20), dtype=np.float32)
    for b0, b1, gl in bed_override:
        env[int(b0 * SR):int(b1 * SR)] = gl
    # the bed follows the bursts' overall level; each burst is levelled on its own (sources differ by 15 dB: the #76 ESPN clip)
    gain = lambda L: 10 ** (((a.burst_lufs - L) if L is not None and L > -70 else 0) / 20)
    g = gain(lufs_of(np.concatenate([nat[int(b0 * SR):int(b1 * SR)] for b0, b1 in bursts]) if bursts else nat))
    env *= g
    ramp = 0.06  # short: a burst starts on a cut or inside one continuous clip, so a long fade would leak the previous shot's sound
    gains = []
    for b0, b1 in bursts:
        gi = gain(lufs_of(nat[int(b0 * SR):int(b1 * SR)])); gains.append(round(20 * np.log10(gi), 1))
        up = (np.clip((t - b0) / ramp, 0, 1) * np.clip((b1 + a.tail - t) / a.tail, 0, 1)).astype(np.float32)
        env = env * (1 - up) + gi * up
    tail = int(0.3 * SR); env[-tail:] *= np.linspace(1, 0, tail)
    nat = nat * env
    vo = pcm(video, 0, total)
    mix = vo + nat
    L2 = lufs_of(mix)
    mix *= 10 ** (((a.target_lufs - L2) if L2 else 0) / 20)
    tmp = os.path.join(F, "_nat_mix.f32")
    mix.astype(np.float32).tofile(tmp)
    out = os.path.join(F, a.out)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", tmp,
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "alimiter=limit=0.89:level=disabled", "-ac", "2",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
    os.remove(tmp)
    print(f"Done: {out}  (bursts {bursts}, burst gains {gains} dB, bed {a.bed_db} dB under {20*np.log10(g):+.1f} dB, mix {L2:.1f} -> {a.target_lufs} LUFS)")


if __name__ == "__main__":
    main()
