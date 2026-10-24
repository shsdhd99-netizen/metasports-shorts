"""Recreation of Lehmann's 2006 penalty note for S01 (not the real note: labelled 'recreation' on the page).
Names from FIFA.com and Football Shirt Culture/Reuters (see notes.md); directions only where the script says them.
  python make_note.py <out_dir> <handwriting.ttf>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out, hand = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sans = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Tools", "fonts", "TikTok-Sans-SemiBold.ttf")

W, H = 900, 1150
LINES = [("Riquelme", "left high"), ("Crespo", ""), ("Heinze", "left low"), ("Ayala", ""), ("Messi", ""), ("Aimar", ""), ("Rodriguez", "")]


def page():
    im = Image.new("RGB", (W, H), (246, 242, 230))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 120], fill=(232, 228, 216))  # blank letterhead strip
    for y in range(190, H - 40, 105):
        d.line([(40, y), (W - 40, y)], fill=(170, 195, 220), width=3)
    d.line([(120, 130), (120, H)], fill=(220, 120, 120), width=3)
    f = ImageFont.truetype(hand, 92)
    for i, (name, side) in enumerate(LINES):
        y = 190 + i * 105 - 88
        d.text((145, y), name, font=f, fill=(70, 70, 75))
        if side:
            d.text((500, y), "- " + side, font=f, fill=(70, 70, 75))
    d.text((W - 230, H - 52), "recreation", font=ImageFont.truetype(sans, 30), fill=(150, 145, 135))
    return im


def framed(im, angle=-3):
    pad = 40
    sh = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([pad + 8, pad + 12, pad + im.width + 8, pad + im.height + 12], fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    sh.paste(im, (pad, pad))
    return sh.rotate(angle, resample=Image.BICUBIC, expand=True)


base = page()
framed(base).save(os.path.join(out, "note_a.png"))
# price tag for the payoff line
tag = base.copy().convert("RGBA")
t = Image.new("RGBA", (640, 220), (0, 0, 0, 0))
td = ImageDraw.Draw(t)
td.rounded_rectangle([0, 0, 639, 219], 30, fill=(255, 255, 255, 255), outline=(30, 30, 30, 255), width=6)
td.ellipse([30, 90, 70, 130], fill=(246, 242, 230, 255), outline=(30, 30, 30, 255), width=5)
fs = ImageFont.truetype(sans, 84)
td.text((92, 48), "€1,000,000", font=fs, fill=(200, 30, 30))
t = t.rotate(8, resample=Image.BICUBIC, expand=True)
tag.alpha_composite(t, (W - t.width - 10, H - t.height - 120))
framed(tag.convert("RGB")).save(os.path.join(out, "note_tag.png"))
print("ok", out)


# Oct 21: full 9:16 frames (page over the blurred stadium) for broll.py still. The page stays ABOVE y=890 so the white
# captions (centred at y=960) never sit on the cream paper.
def frame(pg, width=690, top=50, crop_top=None, circle=None):
    bgp = os.path.join(out, "bg_stadium.jpg")
    bg = Image.open(bgp).convert("RGB") if os.path.exists(bgp) else Image.new("RGB", (1080, 1920), (30, 40, 30))
    bg = bg.resize((max(1080, int(bg.width * 1920 / bg.height)), 1920)).crop((0, 0, 1080, 1920))
    bg = Image.eval(bg.filter(ImageFilter.GaussianBlur(28)), lambda v: int(v * 0.55))
    if crop_top:  # close-up on the names: keep the top share of the page only
        pg = pg.crop((0, 0, pg.width, int(pg.height * crop_top)))
    p = pg.resize((width, int(pg.height * width / pg.width)), Image.LANCZOS)
    bg.paste(p, ((1080 - width) // 2, top), p if p.mode == "RGBA" else None)
    if circle:  # red ellipse in page-share coordinates (x0, y0, x1, y1)
        d = ImageDraw.Draw(bg)
        x0, y0 = (1080 - width) // 2, top
        box = [x0 + circle[0] * width, y0 + circle[1] * p.height, x0 + circle[2] * width, y0 + circle[3] * p.height]
        for k in range(6):
            d.ellipse([box[0] - k, box[1] - k, box[2] + k, box[3] + k], outline=(220, 30, 30))
    return bg


pa = Image.open(os.path.join(out, "note_a.png"))
pt = Image.open(os.path.join(out, "note_tag.png"))
frame(pa).save(os.path.join(out, "note_f1.jpg"), quality=92)
frame(pa, width=1000, top=40, crop_top=0.6).save(os.path.join(out, "note_f2.jpg"), quality=92)
frame(pa, circle=(0.18, 0.72, 0.84, 0.87)).save(os.path.join(out, "note_f3.jpg"), quality=92)
frame(pt).save(os.path.join(out, "note_f4.jpg"), quality=92)
print("frames ok")
