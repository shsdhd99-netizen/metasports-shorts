"""Remove one-frame flashes from a clip: a frame that differs from BOTH neighbours while the neighbours match each other
(a washed-out frame, a stray frame from another shot) is replaced by the frame before it.

  python Tools/deflash.py clips/a1.mp4 clips/a1_df.mp4          # writes a new file; the original is kept
  python Tools/deflash.py clips/a1.mp4 --check                   # only lists the flashes (seconds), changes nothing
  add --ratio 1.5 for fast-motion clips (default 2.5 is strict); look at the listed frames before trusting a low ratio

Why (Oct 14, 2026): #21 and #36 renders showed single washed-out frames (b7L, c_xmas56, a1, c_34, k2bg). They come from the
source encodes and older cuts, not the edit. qa's frozen/black checks can't see them; this does. Real cuts are left alone:
at a cut, the frames on either side differ from each other, so they don't match the rule.
"""
import json, subprocess, sys
import numpy as np


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height,avg_frame_rate",
                          "-of", "json", path], capture_output=True, text=True).stdout
    s = json.loads(out)["streams"][0]
    n, d = s["avg_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d)


def flashes(path, ratio=2.5, floor=12.0):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=96:170,format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, 170, 96).astype(np.float32)
    bad = []
    for i in range(1, len(fr) - 1):
        a = np.abs(fr[i] - fr[i - 1]).mean(); b = np.abs(fr[i + 1] - fr[i]).mean(); c = np.abs(fr[i + 1] - fr[i - 1]).mean()
        if min(a, b) > floor and min(a, b) > ratio * max(c, 1.0):
            bad.append(i)
    return bad


def main():
    src = sys.argv[1]
    w, h, fps = probe(src)
    ratio = float(sys.argv[sys.argv.index("--ratio") + 1]) if "--ratio" in sys.argv else 2.5  # lower (1.5) for fast motion; check the frames
    bad = flashes(src, ratio=ratio)
    print(f"{src}: {len(bad)} flash frame(s) at " + ", ".join(f"{i / fps:.3f}s" for i in bad))
    if "--check" in sys.argv or len(sys.argv) < 3 or sys.argv[2].startswith("--"):
        return
    out = sys.argv[2]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    frames = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).copy()
    for i in bad:
        frames[i] = frames[i - 1]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", f"{fps:.5f}", "-i", "-",
                    "-c:v", "libx264", "-crf", "15", "-preset", "veryfast", "-pix_fmt", "yuv420p", out], input=frames.tobytes(), check=True)
    print(f"wrote {out} ({len(bad)} frame(s) replaced)")


if __name__ == "__main__":
    main()
