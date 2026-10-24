"""Fast contact sheet of a source video, and its scene cuts (Oct 24 2026; was a scratch helper in the #66 session).

  python Tools/frame_sheet.py src/den_hl.mp4 --from 100 --to 118 --every 0.5 --out _sheets/den_end.jpg [--width 200]
  python Tools/frame_sheet.py src/mvp_reel.mp4 --cuts            # prints the scene-change times (clean in/out points)

Grabs one frame per step in parallel (input seeking, so a 10-minute file takes seconds) and tiles them 6 wide with time
labels. Times accept seconds or m:ss. Use --cuts before choosing an in-point: highlight reels dissolve between shots, and a
shot that starts or ends inside a dissolve shows two pictures at once (#66: the MVP reel's close-ups last 0.5-1 s between
flash transitions; #60's Jordan zoom was a dissolve).
"""
import argparse, os, re, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont

FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "DMSans-Bold.ttf")


def secs(v):
    p = [float(x) for x in str(v).split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0]


def label(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


def cuts(src, thresh):
    err = subprocess.run(["ffmpeg", "-nostdin", "-i", src, "-vf", f"scale=320:-2,select='gt(scene,{thresh})',showinfo", "-an", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", err)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--from", dest="start", default="0")
    ap.add_argument("--to", dest="end")
    ap.add_argument("--every", type=float, default=2.0)
    ap.add_argument("--width", type=int, default=200)
    ap.add_argument("--out")
    ap.add_argument("--cuts", action="store_true", help="print scene-change times instead of drawing a sheet")
    ap.add_argument("--thresh", type=float, default=0.25)
    a = ap.parse_args()
    if a.cuts:
        print(" ".join(f"{t:.2f}" for t in cuts(a.src, a.thresh)))
        return
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.src],
                               capture_output=True, text=True).stdout)
    t0, t1 = secs(a.start), min(secs(a.end) if a.end else dur, dur - 0.05)
    ts, t = [], t0
    while t <= t1 + 1e-6:
        ts.append(round(t, 2)); t += a.every
    tmp = tempfile.mkdtemp()

    def grab(t):
        p = os.path.join(tmp, f"{t:.2f}.jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t}", "-i", a.src, "-frames:v", "1", "-vf", f"scale={a.width}:-2", "-q:v", "5", "-y", p])
        return t, p

    with ThreadPoolExecutor(8) as ex:
        ims = [(t, Image.open(p)) for t, p in ex.map(grab, ts) if os.path.exists(p)]
    w, h = ims[0][1].size
    cols = 6
    sheet = Image.new("RGB", (cols * (w + 4), ((len(ims) + cols - 1) // cols) * (h + 4)))
    d, f = ImageDraw.Draw(sheet), ImageFont.truetype(FONT, 18)
    for i, (t, im) in enumerate(ims):
        x, y = (i % cols) * (w + 4), (i // cols) * (h + 4)
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x + 110, y + 24], fill=(0, 0, 0)); d.text((x + 4, y + 2), label(t), font=f, fill=(255, 255, 0))
    out = a.out or os.path.splitext(a.src)[0] + "_sheet.jpg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    sheet.save(out, quality=80)
    print(out, len(ims), "frames")


if __name__ == "__main__":
    main()
