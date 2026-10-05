"""Voice post-processing that raises pace WITHOUT time-stretching (stretching is what made the voice sound artificial).

tighten_gaps(in_audio, words, out_audio, keep=0.10, thresh=0.22):
    Where the silence between two words is longer than `thresh` seconds, cut it down to `keep` seconds (a jump-cut, like a human editor does).
    words = [(word, start, end), ...] on in_audio's timeline. Returns (new_words, seconds_removed). Pitch, tone and quality are untouched.
    Typical effect: expressive models (eleven_v3, ~120-140 wpm) gain 10-20% pace and still keep natural sentence pauses (0.10 s + the 0.12 s splice gap).
CLI test:  python voice_fx.py in.mp3 words.json out.mp3
"""
import json, subprocess, sys


def tighten_gaps(in_audio, words, out_audio, keep=0.10, thresh=0.22, extra_filter=""):
    keeps, removed, t0 = [], 0.0, 0.0
    shift = []  # (original time boundary, cumulative removed)
    for i in range(len(words) - 1):
        e, s = words[i][2], words[i + 1][1]
        if s - e > thresh:
            cut_a, cut_b = e + keep / 2, s - keep / 2
            keeps.append((t0, cut_a)); t0 = cut_b
            removed += cut_b - cut_a; shift.append((cut_b, removed))
    keeps.append((t0, None))
    parts = []
    for k, (a, b) in enumerate(keeps):
        trim = f"atrim=start={a:.4f}" + (f":end={b:.4f}" if b is not None else "")
        parts.append(f"[0:a]{trim},asetpts=PTS-STARTPTS[s{k}]")
    cc = "".join(f"[s{k}]" for k in range(len(keeps)))
    fc = ";".join(parts) + f";{cc}concat=n={len(keeps)}:v=0:a=1[out]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", in_audio, "-filter_complex", fc, "-map", "[out]"]
    if extra_filter:
        cmd += ["-af", extra_filter]
    subprocess.run(cmd + ["-c:a", "libmp3lame", "-q:a", "0", out_audio], check=True)

    def new_t(t):
        r = 0.0
        for boundary, cum in shift:
            if t >= boundary - 1e-6: r = cum
            else: break
        return t - r
    return [(w, new_t(s), new_t(e)) for w, s, e in words], removed


if __name__ == "__main__":
    ws = [(w["word"], w["start"], w["end"]) for w in json.load(open(sys.argv[2]))]
    nw, rem = tighten_gaps(sys.argv[1], ws, sys.argv[3])
    print(f"removed {rem:.2f} s of pauses; {len(nw)} words")
