"""Storyboard check: the picture on screen for every caption card, so you can see if words and footage match.

  python storyboard.py --folder "<build folder>"                  # uses shots.json + clips + words.json
  python storyboard.py --folder "..." --video final.mp4           # check a finished video instead
  python storyboard.py --folder "..." --cols 6 --out board.jpg

Each tile = the frame shown halfway through one caption card, with the card's words under it.
A coloured top bar marks where a new shot starts. Look for tiles where the picture doesn't show the words.
"""
import argparse, json, os, subprocess, sys, tempfile, shutil
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import captions  # noqa: E402

TW, TH, LAB = 240, 426, 64


def grab(path, t, out):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{max(0, t):.3f}", "-i", path, "-frames:v", "1",
                    "-vf", f"scale={TW}:{TH}:force_original_aspect_ratio=increase,crop={TW}:{TH}", out], check=False)
    return os.path.exists(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--video")
    ap.add_argument("--style", default="metasports")
    ap.add_argument("--cols", type=int, default=7)
    ap.add_argument("--out")
    a = ap.parse_args()
    folder = os.path.abspath(a.folder)
    words = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8-sig"))
    cards = captions.chunk(words, captions.STYLES[a.style])
    plan = None
    if not a.video:
        plan = json.load(open(os.path.join(folder, "shots.json"), encoding="utf-8-sig"))
    tmp = tempfile.mkdtemp()
    tiles = []
    try:
        last_clip = None
        for k, card in enumerate(cards):
            s, e = card[0]["start"], card[-1]["end"]
            mid = (s + e) / 2
            text = " ".join(w["word"] for w in card).upper()
            f = os.path.join(tmp, f"{k:03d}.png")
            new_shot = False
            if a.video:
                ok = grab(os.path.join(folder, a.video) if not os.path.isabs(a.video) else a.video, mid, f)
                label_clip = ""
            else:
                cur = max((p for p in plan if float(p["start"]) <= mid + 1e-6), key=lambda p: float(p["start"]))
                ok = grab(os.path.join(folder, "clips", cur["clip"]), mid - float(cur["start"]), f)
                label_clip = cur["clip"]
                new_shot = cur["clip"] != last_clip
                last_clip = cur["clip"]
            tiles.append((f if ok else None, text, s, label_clip, new_shot))
        cols = a.cols
        rows = (len(tiles) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (TW + 6) + 6, rows * (TH + LAB + 6) + 6), (18, 18, 18))
        try:
            font = ImageFont.truetype(os.path.join(HERE, "fonts", "Montserrat-Bold.ttf"), 17)
            small = ImageFont.truetype(os.path.join(HERE, "fonts", "Montserrat-Medium.ttf"), 13)
        except OSError:
            font = small = ImageFont.load_default()
        d = ImageDraw.Draw(sheet)
        for i, (f, text, s, clip, new) in enumerate(tiles):
            x, y = 6 + (i % cols) * (TW + 6), 6 + (i // cols) * (TH + LAB + 6)
            if f:
                sheet.paste(Image.open(f).convert("RGB"), (x, y))
            if new:
                d.rectangle([x, y, x + TW, y + 6], fill=(255, 196, 0))
            d.text((x + 4, y + TH + 4), text[:26], font=font, fill=(255, 255, 255))
            if len(text) > 26:
                d.text((x + 4, y + TH + 24), text[26:52], font=font, fill=(255, 255, 255))
            d.text((x + 4, y + TH + 46), f"{s:5.2f}s  {clip}", font=small, fill=(150, 150, 150))
        out = a.out or os.path.join(folder, "storyboard.jpg")
        sheet.save(out, quality=88)
        print(f"{out}  ({len(tiles)} cards)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
