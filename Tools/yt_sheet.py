"""Find the exact second of a moment in any YouTube video WITHOUT downloading it (works from the cloud, where YouTube blocks downloads).

  python yt_sheet.py <youtube id | url> --from 0 --to 120 --out sheet.jpg

Uses YouTube's own preview frames (160x90, about 1 per second): good enough to spot a scene and read its time,
not good enough to check a face. Confirm identities on the PC with `broll.py sheet` before cutting.
The sheet prints a timestamp on every frame. Put what you find in a clips_manifest.json (see pc_cut.py).
"""
import argparse, email, glob, io, math, os, re, shutil, subprocess, sys, tempfile
from email import policy

CLIENTS = "youtube:player_client=tv_embedded,web_embedded"


def vid_id(s):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", s)
    return m.group(1) if m else s


def frames(video):
    """-> (list of 160x90 PIL frames in time order, seconds per frame, duration)"""
    import json, urllib.request
    from PIL import Image
    r = subprocess.run(["yt-dlp", "-q", "--no-warnings", "--extractor-args", CLIENTS, "-f", "sb0", "-J",
                        "https://www.youtube.com/watch?v=" + video], capture_output=True, text=True)
    try:
        info = json.loads(r.stdout)
        fmt = [f for f in info["formats"] if f["format_id"] == "sb0"][0]
    except Exception:
        raise SystemExit("No preview frames: " + (r.stderr or "")[-300:])
    dur = float(info.get("duration") or 0)
    tiles = []
    for fr in fmt["fragments"]:  # each is a 5x5 sheet of 160x90 frames (WebP)
        data = urllib.request.urlopen(fr["url"], timeout=60).read()
        im = Image.open(io.BytesIO(data)).convert("RGB")
        for y in range(im.height // 90):
            for x in range(im.width // 160):
                tiles.append(im.crop((x * 160, y * 90, x * 160 + 160, y * 90 + 90)))
    while tiles and not tiles[-1].getbbox():
        tiles.pop()
    step = dur / len(tiles) if tiles and dur else 1.0
    return tiles, step, dur


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--from", dest="start", type=float, default=0)
    ap.add_argument("--to", dest="end", type=float, default=0)
    ap.add_argument("--every", type=float, default=0, help="seconds between tiles (default: every frame YouTube has)")
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--out", default="sheet.jpg")
    a = ap.parse_args()
    from PIL import Image, ImageDraw, ImageFont
    tiles, step, dur = frames(vid_id(a.video))
    end = a.end or dur
    pick = []
    t = a.start
    every = max(a.every, step)
    while t <= end:
        i = min(len(tiles) - 1, int(round(t / step)))
        pick.append((t, tiles[i]))
        t += every
    cols = a.cols
    rows = math.ceil(len(pick) / cols)
    font_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Montserrat-Bold.ttf")
    font = ImageFont.truetype(font_p, 15) if os.path.exists(font_p) else ImageFont.load_default()
    sheet = Image.new("RGB", (cols * 164, rows * 112), (16, 16, 16))
    d = ImageDraw.Draw(sheet)
    for n, (t, im) in enumerate(pick):
        x, y = (n % cols) * 164 + 2, (n // cols) * 112 + 2
        sheet.paste(im, (x, y))
        d.text((x + 2, y + 92), f"{int(t // 60)}:{t % 60:04.1f}", fill=(255, 255, 255), font=font)
    sheet = sheet.resize((sheet.width * 2, sheet.height * 2), Image.LANCZOS)
    sheet.save(a.out, quality=88)
    print(f"{a.out}: {len(pick)} frames, {step:.2f}s apart, video {dur:.0f}s")


if __name__ == "__main__":
    main()
