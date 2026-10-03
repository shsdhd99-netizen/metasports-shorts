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
    """-> (list of PNG paths in time order, seconds per frame, duration)"""
    tmp = tempfile.mkdtemp(prefix="ytsb-")
    r = subprocess.run(["yt-dlp", "-q", "--no-warnings", "--extractor-args", CLIENTS, "-f", "sb0", "--print", "duration", "--no-simulate",
                        "-o", os.path.join(tmp, "sb.%(ext)s"), "https://www.youtube.com/watch?v=" + video],
                       capture_output=True, text=True)
    dur = float((r.stdout.strip().splitlines() or ["0"])[-1] or 0)
    files = glob.glob(os.path.join(tmp, "sb.*"))
    if not files:
        raise SystemExit("No preview frames: " + (r.stderr or "")[-300:])
    msg = email.message_from_binary_file(open(files[0], "rb"), policy=policy.default)
    pngs, k = [], 0
    for part in msg.walk():
        if part.get_content_type().startswith("image"):
            src = os.path.join(tmp, f"s{k}.webp")
            open(src, "wb").write(part.get_payload(decode=True))
            out = os.path.join(tmp, f"s{k}.png")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, out])
            if os.path.exists(out):
                pngs.append(out)
            k += 1
    from PIL import Image
    tiles = []
    for p in pngs:  # each sheet is a 5x5 grid of 160x90 frames
        im = Image.open(p).convert("RGB")
        cols, rows = im.width // 160, im.height // 90
        for y in range(rows):
            for x in range(cols):
                tiles.append(im.crop((x * 160, y * 90, x * 160 + 160, y * 90 + 90)))
    # drop empty trailing tiles
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
