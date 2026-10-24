"""MetaSports FC brand art (Oct 22, 2026): profile picture, YouTube banner, video watermark, and a phone preview of the banner.
  python make_brand.py            # writes into this folder
Look: a mowed pitch (alternating stripes) with chalk markings, an "MS" crest with a gold "FC" bar.
Fonts in fonts/ (Google Fonts, OFL): Anton for the crest and wordmark, Barlow Condensed for the tagline.
YouTube sizes: profile 800x800 (shown as a circle, down to 48 px), banner 2560x1440 with everything that matters inside the
1546x423 centre (the part phones show), watermark 150x150 PNG.
"""
import math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))
F = lambda n, s: ImageFont.truetype(os.path.join(D, "fonts", n), s)
PITCH, PITCH2, DEEP = (16, 74, 52), (21, 87, 62), (9, 46, 33)
CHALK, GOLD, INK = (244, 246, 240), (242, 182, 50), (12, 40, 29)
TAGLINE = "Football stories that sound fake but are 100% real"


def pitch(w, h, stripe, vertical=True):
    im = Image.new("RGB", (w, h), PITCH)
    d = ImageDraw.Draw(im)
    n = (w if vertical else h) // stripe + 1
    for i in range(0, n, 2):
        box = [i * stripe, 0, (i + 1) * stripe, h] if vertical else [0, i * stripe, w, (i + 1) * stripe]
        d.rectangle(box, fill=PITCH2)
    # vignette so the edges sit back and the centre reads
    v = Image.new("L", (w, h), 0)
    ImageDraw.Draw(v).ellipse([-w * 0.25, -h * 0.35, w * 1.25, h * 1.35], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(min(w, h) // 6))
    return Image.composite(im, Image.new("RGB", (w, h), DEEP), v)


def text_center(d, xy, s, font, fill):
    b = d.textbbox((0, 0), s, font=font)
    d.text((xy[0] - (b[0] + b[2]) / 2, xy[1] - (b[1] + b[3]) / 2), s, font=font, fill=fill)


def crest(size, bg=True):
    """Circular crest: chalk centre circle + halfway line, 'MS' and a gold 'FC' bar."""
    S = size * 4  # draw large, then downsample for clean edges
    im = pitch(S, S, S // 8) if bg else Image.new("RGBA", (S, S), (0, 0, 0, 0))
    if not bg:
        ImageDraw.Draw(im).ellipse([0, 0, S - 1, S - 1], fill=PITCH + (255,))
    d = ImageDraw.Draw(im)
    lw = max(4, S // 70)
    r = int(S * 0.40)
    c = S // 2
    d.line([(0, c), (S, c)], fill=CHALK + ((90,) if not bg else ()), width=lw) if not bg else d.line([(0, c), (S, c)], fill=(150, 185, 160), width=lw)
    d.ellipse([c - r, c - r, c + r, c + r], outline=CHALK, width=lw * 2)
    d.ellipse([c - r + lw * 4, c - r + lw * 4, c + r - lw * 4, c + r - lw * 4], fill=DEEP)
    text_center(d, (c, c - S * 0.045), "MS", F("Anton-400.ttf", int(S * 0.34)), CHALK)
    bw, bh = int(S * 0.30), int(S * 0.115)
    by = int(c + S * 0.165)
    d.rounded_rectangle([c - bw // 2, by - bh // 2, c + bw // 2, by + bh // 2], radius=bh // 4, fill=GOLD)
    text_center(d, (c, by + S * 0.004), "FC", F("Anton-400.ttf", int(S * 0.09)), INK)
    return im.resize((size, size), Image.LANCZOS)


def banner():
    W, H = 2560, 1440
    im = pitch(W, H, 160)
    d = ImageDraw.Draw(im)
    lw = 8
    # chalk markings across the full banner (TV shows all of it): halfway line, centre circle, both penalty areas
    line = (205, 225, 210)
    d.line([(W // 2, 0), (W // 2, H)], fill=line, width=lw)
    d.ellipse([W // 2 - 330, H // 2 - 330, W // 2 + 330, H // 2 + 330], outline=line, width=lw)
    for x0, x1 in ((0, 360), (W - 360, W)):
        d.rectangle([x0 - (lw if x0 == 0 else 0), H // 2 - 520, x1 + (lw if x1 == W else 0), H // 2 + 520], outline=line, width=lw)
    # safe area (every device): 1546 x 423 in the centre
    sx0, sy0 = (W - 1546) // 2, (H - 423) // 2
    plate = Image.new("RGBA", (1546, 423), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle([0, 0, 1545, 422], radius=36, fill=DEEP + (232,))
    im.paste(plate, (sx0, sy0), plate)
    c = crest(330, bg=False)
    im.paste(c, (sx0 + 50, sy0 + 46), c)
    d = ImageDraw.Draw(im)
    tx = sx0 + 430
    d.text((tx, sy0 + 38), "METASPORTS", font=F("Anton-400.ttf", 150), fill=CHALK)
    w_ms = d.textlength("METASPORTS ", font=F("Anton-400.ttf", 150))
    d.text((tx + w_ms, sy0 + 38), "FC", font=F("Anton-400.ttf", 150), fill=GOLD)
    d.text((tx + 4, sy0 + 248), TAGLINE, font=F("BarlowCondensed-600.ttf", 58), fill=CHALK)
    d.text((tx + 4, sy0 + 330), "NEW STORY EVERY DAY", font=F("BarlowCondensed-800.ttf", 46), fill=GOLD)
    return im


pfp = crest(800)
pfp.save(os.path.join(D, "metasportsfc_profile_800.png"))
wm = crest(150, bg=False)
wm.save(os.path.join(D, "metasportsfc_watermark_150.png"))
b = banner()
b.save(os.path.join(D, "metasportsfc_banner_2560x1440.png"))
b.convert("RGB").save(os.path.join(D, "metasportsfc_banner_2560x1440.jpg"), quality=92)
# previews: the phone crop (safe area) and the profile as YouTube shows it (circle, 98 px and 48 px)
b.crop(((2560 - 1546) // 2, (1440 - 423) // 2, (2560 + 1546) // 2, (1440 + 423) // 2)).save(os.path.join(D, "preview_banner_phone.png"))
m = Image.new("L", (800, 800), 0)
ImageDraw.Draw(m).ellipse([0, 0, 799, 799], fill=255)
circ = Image.new("RGBA", (800, 800), (0, 0, 0, 0))
circ.paste(pfp, (0, 0), m)
sheet = Image.new("RGB", (420, 140), (255, 255, 255))
sheet.paste(circ.resize((98, 98), Image.LANCZOS), (20, 21), circ.resize((98, 98), Image.LANCZOS))
sheet.paste(circ.resize((48, 48), Image.LANCZOS), (150, 46), circ.resize((48, 48), Image.LANCZOS))
dark = Image.new("RGB", (190, 140), (15, 15, 15))
dark.paste(circ.resize((98, 98), Image.LANCZOS), (10, 21), circ.resize((98, 98), Image.LANCZOS))
dark.paste(circ.resize((48, 48), Image.LANCZOS), (125, 46), circ.resize((48, 48), Image.LANCZOS))
sheet.paste(dark, (230, 0))
sheet.save(os.path.join(D, "preview_profile_sizes.png"))
print("brand ok")
