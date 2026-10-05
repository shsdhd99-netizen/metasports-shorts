"""WATCH a competitor Short for free (no vidIQ): download it, then report cut rate, loudness, words/min, hook, ending, and a contact sheet you can look at.

  python watch_short.py https://www.tiktok.com/@coachclank_/video/7615272838886378774 --out watch/clank1
  python watch_short.py some_local_video.mp4 --out watch/x            (any local mp4, e.g. from x_clip.py)

Why TikTok: YouTube blocks downloads and previews from this cloud IP (bot check), but TikTok pages play in the preinstalled Chromium
(watch_dl.mjs). Most creators cross-post, so search the title with site:tiktok.com. Writes <out>/video.mp4, sheet.jpg (0.5 s frames for
the first 4 s, then 1 per second, with timestamps), report.md. Open sheet.jpg with the Read tool to LOOK at captions, cards, zooms.
Limits: speech-to-text is faster-whisper (tiny/base), may misspell names; scene cuts are a frame-difference estimate.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def download(url, out):
    r = sh(["node", os.path.join(HERE, "watch_dl.mjs"), "--url", url, "--out", out])
    if r.returncode != 0:
        raise SystemExit("download failed: " + (r.stderr or r.stdout)[-300:])
    return json.loads(r.stdout.strip().splitlines()[-1])


def probe(path):
    r = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height", "-of", "json", path])
    d = json.loads(r.stdout)
    st = [s for s in d["streams"] if "width" in s][0]
    return float(d["format"]["duration"]), st["width"], st["height"]


def cuts(path, thr=0.28):
    r = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vf", f"select='gt(scene,{thr})',metadata=print:file=-", "-an", "-f", "null", "-"])
    return sorted(float(m) for m in re.findall(r"pts_time:([\d.]+)", r.stdout + r.stderr))


def lufs(path):
    r = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128", "-f", "null", "-"])
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else None


def sheet(path, dur, out_jpg):
    from PIL import Image, ImageDraw
    times = [i * 0.5 for i in range(0, 8)] + [float(t) for t in range(4, int(dur) + 1)]
    times = [t for t in times if t < dur]
    tmp = out_jpg + "_frames"; os.makedirs(tmp, exist_ok=True)
    thumbs = []
    for t in times:
        f = os.path.join(tmp, f"{t:05.1f}.jpg")
        sh(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", path, "-frames:v", "1", "-vf", "scale=216:-1", f])
        if os.path.exists(f):
            im = Image.open(f).convert("RGB"); ImageDraw.Draw(im).text((4, 4), f"{t:.1f}s", fill=(255, 255, 0)); thumbs.append(im)
    cols = 8; w, h = thumbs[0].size; rows = (len(thumbs) + cols - 1) // cols
    S = Image.new("RGB", (cols * w, rows * h), (0, 0, 0))
    for i, im in enumerate(thumbs):
        S.paste(im, ((i % cols) * w, (i // cols) * h))
    S.save(out_jpg, quality=80)
    for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)


def transcribe(path):
    try:
        from faster_whisper import WhisperModel
    except Exception:
        return None
    for size in ("base", "tiny"):
        try:
            m = WhisperModel(size, device="cpu", compute_type="int8")
            segs, _ = m.transcribe(path, word_timestamps=True, vad_filter=True)
            return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
        except Exception as e:
            err = e
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("--out", default="watch/short"); ap.add_argument("--no-stt", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    vid = os.path.join(a.out, "video.mp4"); meta = {}
    if re.match(r"https?://", a.src):
        meta = download(a.src, vid)
    else:
        vid = a.src
    dur, w, h = probe(vid)
    c = cuts(vid); first3 = [t for t in c if t < 3]
    shots = len(c) + 1; avg = dur / shots
    L = lufs(vid)
    sheet(vid, dur, os.path.join(a.out, "sheet.jpg"))
    words = None if a.no_stt else transcribe(vid)
    lines = [f"# WATCH REPORT: {meta.get('title', os.path.basename(vid))}", f"- source: {a.src}", f"- {dur:.1f} s, {w}x{h}, loudness {L} LUFS",
             f"- scene cuts (frame-diff estimate): {len(c)} -> about {shots} shots, avg {avg:.2f} s, cuts in first 3 s: {len(first3)}", f"- cut times: {', '.join(f'{t:.1f}' for t in c)}"]
    if words:
        n = len(words); span = words[-1][2] - words[0][1]; wpm = n / span * 60 if span > 0 else 0
        txt = " ".join(x[0] for x in words)
        lines += [f"- speech: {n} words, {wpm:.0f} wpm, voice starts {words[0][1]:.2f} s, ends {words[-1][2]:.1f} s of {dur:.1f} s",
                  f"- HOOK (first 10 words): {' '.join(x[0] for x in words[:10])}", f"- ENDING (last 12 words): {' '.join(x[0] for x in words[-12:])}",
                  f"- ends on a question: {txt.strip().endswith('?')}", "", "## Transcript (whisper, may misspell names)", txt]
    else:
        lines.append("- speech-to-text unavailable (no faster_whisper model) or no speech detected")
    lines += ["", "Open sheet.jpg to look at captions, cards, zooms; frames are 0.5 s apart for the first 4 s then 1 per second."]
    open(os.path.join(a.out, "report.md"), "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(lines[:9]))


if __name__ == "__main__":
    main()
