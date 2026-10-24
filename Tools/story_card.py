"""Evidence cards for the story format, as full 9:16 frames for broll.py `still` shots (soccer channel, Oct 22, 2026).
Everything stays above y=890 so the centred captions (y=960) sit on the dark fill.

  # a stat card: title, subtitle, rows of "label|value" (the row marked with * is highlighted), footer
  python Tools/story_card.py --bg frame.jpg --out card.jpg --title "GOLDEN BALL 2006" --sub "Journalists' vote" \
      --row "*Zinedine Zidane|2,012" --row "Fabio Cannavaro|1,977" --foot "Source: BBC Sport, 10 July 2006"
  # a photo card: the photo on a white plate, an optional red box (photo pixels x0,y0,x1,y1) and a credit line
  python Tools/story_card.py --bg frame.jpg --out card.jpg --photo bottle.jpg --box 118,620,395,665 --credit "Photo: X / @FabrizioRomano"
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Soccer Channel", "Brand", "fonts")
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)
RED, WHITE, GREY, YELLOW, INK = (229, 28, 36), (255, 255, 255), (200, 200, 200), (255, 193, 0), (25, 25, 25)
LIMIT = 890


def background(path, dim=0.42):
    if not path:
        return Image.new("RGB", (1080, 1920), (18, 18, 22))
    b = Image.open(path).convert("RGB")
    b = b.resize((max(1080, int(b.width * 1920 / b.height)), 1920))
    x = (b.width - 1080) // 2
    b = b.crop((x, 0, x + 1080, 1920))
    return Image.eval(b.filter(ImageFilter.GaussianBlur(28)), lambda v: int(v * dim))


def centred(d, y, text, font, fill=WHITE):
    d.text(((1080 - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def fit(d, text, name, size, width):
    while size > 20 and d.textlength(text, font=F(name, size)) > width:
        size -= 2
    return F(name, size)


def stat_card(a):
    f = background(a.bg)
    d = ImageDraw.Draw(f)
    y = 80
    centred(d, y, a.title, fit(d, a.title, "Poppins-700.ttf", 74, 980)); y += 100
    if a.sub:
        centred(d, y, a.sub, fit(d, a.sub, "Poppins-600.ttf", 38, 980), GREY); y += 70
    y += 20
    for r in a.row:
        hi = r.startswith("*")
        label, value = r.lstrip("*").split("|", 1)
        if hi:
            d.rounded_rectangle([50, y - 8, 1030, y + 84], radius=14, fill=RED)
        lf = fit(d, label, "Poppins-600.ttf", 44, 640)
        d.text((80, y + 14), label, font=lf, fill=WHITE)
        vf = F("Poppins-700.ttf", 52)
        d.text((1000 - d.textlength(value, font=vf), y + 6), value, font=vf, fill=WHITE if hi else YELLOW)
        y += 112
    if a.big:
        y += 10
        centred(d, y, a.big, fit(d, a.big, "Poppins-700.ttf", 60, 980), YELLOW); y += 84
    if a.foot:
        centred(d, y + 6, a.foot, fit(d, a.foot, "Poppins-600.ttf", 26, 980), GREY); y += 46
    assert y <= LIMIT, f"card bottom {y} would sit under the captions; use fewer rows"
    return f


def photo_card(a):
    f = background(a.bg or a.photo)
    p = Image.open(a.photo).convert("RGB")
    box = [int(v) for v in a.box.split(",")] if a.box else None
    maxw, maxh = a.width, LIMIT - 60 - 24 - (44 if a.credit else 0) - (90 if a.title else 0)
    s = min(maxw / p.width, maxh / p.height)
    p = p.resize((int(p.width * s), int(p.height * s)), Image.LANCZOS)
    d = ImageDraw.Draw(f)
    top = 60
    if a.title:
        centred(d, top, a.title, fit(d, a.title, "Poppins-700.ttf", 62, 980)); top += 90
    plate = Image.new("RGB", (p.width + 24, p.height + 24), WHITE)
    plate.paste(p, (12, 12))
    x0 = (1080 - plate.width) // 2
    f.paste(plate, (x0, top))
    if box:
        bx = [x0 + 12 + box[0] * s - 10, top + 12 + box[1] * s - 8, x0 + 12 + box[2] * s + 10, top + 12 + box[3] * s + 8]
        for k in range(7):
            d.rectangle([bx[0] - k, bx[1] - k, bx[2] + k, bx[3] + k], outline=RED)
    y = top + plate.height + 12
    if a.credit:
        centred(d, y, a.credit, fit(d, a.credit, "Poppins-600.ttf", 22, 980), GREY); y += 32
    assert y <= LIMIT, f"photo card bottom {y} would sit under the captions"
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--bg")
    ap.add_argument("--title", default="")
    ap.add_argument("--sub", default="")
    ap.add_argument("--row", action="append", default=[])
    ap.add_argument("--big", default="")
    ap.add_argument("--foot", default="")
    ap.add_argument("--photo")
    ap.add_argument("--box")
    ap.add_argument("--width", type=int, default=980)
    ap.add_argument("--credit", default="")
    a = ap.parse_args()
    (photo_card(a) if a.photo else stat_card(a)).save(a.out, quality=92)
    print(a.out)


if __name__ == "__main__":
    main()
