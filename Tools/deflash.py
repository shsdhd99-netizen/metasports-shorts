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


def _read_frames(cmd, nbytes):
    """Yield raw frames from an ffmpeg pipe one at a time (never the whole file in memory)."""
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        while True:
            buf = pr.stdout.read(nbytes)
            if len(buf) < nbytes:
                break
            yield buf
    finally:
        pr.stdout.close(); pr.wait()


def flashes(path, ratio=2.5, floor=12.0):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=96:170,format=gray", "-f", "rawvideo", "-"]
    bad, win = [], []  # sliding window of 3 small gray frames
    for n, buf in enumerate(_read_frames(cmd, 96 * 170)):
        win.append(np.frombuffer(buf, np.uint8).reshape(170, 96).astype(np.float32))
        if len(win) > 3:
            win.pop(0)
        if len(win) == 3:
            p, f, q = win
            a = np.abs(f - p).mean(); b = np.abs(q - f).mean(); c = np.abs(q - p).mean()
            if min(a, b) > floor and min(a, b) > ratio * max(c, 1.0):
                bad.append(n - 1)
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
    badset = set(bad)
    # Streamed: decode frame by frame, replace flashes with the previous frame, encode through a pipe. The audio is copied
    # straight from the source (stream copy), so nothing is lost and nothing big sits in memory.
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", f"{fps:.5f}", "-i", "-",
                            "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "15", "-preset", "veryfast",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", out], stdin=subprocess.PIPE)
    prev = None
    for i, buf in enumerate(_read_frames(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], w * h * 3)):
        if i in badset and prev is not None:
            buf = prev
        enc.stdin.write(buf)
        prev = buf
    enc.stdin.close()
    if enc.wait():
        raise SystemExit("ffmpeg could not write " + out)
    print(f"wrote {out} ({len(bad)} frame(s) replaced, audio kept)")


if __name__ == "__main__":
    main()
