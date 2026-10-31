"""MetaSports FC brand art, v2 (Oct 22, 2026): the sibling of the MetaSports Clips logo.
Clips (yt avatar, Oct 22): solid red #E51C24, a yellow #FFC100 running figure, a white slanted "MetaSports" wordmark and spaced
"C L I P S" under it. FC keeps all of that, swaps CLIPS for "F C" and gives the figure a football to kick.
  python make_brand.py            # profile 900x900, banner 2560x1440, watermark 150x150, previews
Fonts in fonts/ (Google Fonts, OFL): Poppins SemiBold/Bold, slanted 11 degrees like the Clips wordmark; Poppins Medium for the tagline.
The first, green version is kept in _v1_green/.
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
F = lambda n, s: ImageFont.truetype(os.path.join(D, "fonts", n), s)
RED, RED_DARK, YELLOW, WHITE, INK = (229, 28, 36), (200, 20, 28), (255, 193, 0), (255, 255, 255), (25, 25, 25)
TAGLINE = "Football stories that sound fake but are 100% real"


def slanted(text, font, size, fill=WHITE, spacing=0, slant=0.2):
    """Text sheared to the right, like the Clips wordmark (it is an oblique, not a true italic)."""
    f = F(font, size)
    w = int(sum(f.getlength(c) for c in text) + spacing * (len(text) - 1)) + 4
    h = int(size * 1.35)
    pad = int(h * slant) + 4
    im = Image.new("RGBA", (w + pad, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = pad
    for c in text:
        d.text((x, 0), c, font=f, fill=fill)
        x += f.getlength(c) + spacing
    im = im.transform(im.size, Image.AFFINE, (1, slant, 0, 0, 1, 0), Image.BICUBIC)
    return im.crop(im.getbbox())


def limb(d, pts, w0, w1, fill):
    """A tapered stroke through pts, round joints: the pictogram look of the Clips runner."""
    n = len(pts) - 1
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        a, b = w0 + (w1 - w0) * i / n, w0 + (w1 - w0) * (i + 1) / n
        ang = math.atan2(y1 - y0, x1 - x0) + math.pi / 2
        ca, sa = math.cos(ang), math.sin(ang)
        d.polygon([(x0 + ca * a / 2, y0 + sa * a / 2), (x1 + ca * b / 2, y1 + sa * b / 2),
                   (x1 - ca * b / 2, y1 - sa * b / 2), (x0 - ca * a / 2, y0 - sa * a / 2)], fill=fill)
        d.ellipse([x0 - a / 2, y0 - a / 2, x0 + a / 2, y0 + a / 2], fill=fill)
        d.ellipse([x1 - b / 2, y1 - b / 2, x1 + b / 2, y1 + b / 2], fill=fill)


def football(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
    pent = lambda x, y, s, rot: [(x + s * math.cos(rot + k * 2 * math.pi / 5), y + s * math.sin(rot + k * 2 * math.pi / 5)) for k in range(5)]
    d.polygon(pent(cx, cy, r * 0.36, -math.pi / 2), fill=INK)
    for k in range(5):  # the five half-hidden patches around the centre one
        a = -math.pi / 2 + k * 2 * math.pi / 5
        px, py = cx + math.cos(a) * r * 0.86, cy + math.sin(a) * r * 0.86
        d.polygon(pent(px, py, r * 0.26, a + math.pi), fill=INK)
    # clip anything outside the ball back to the background is done by the caller's mask; draw the seams
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        d.line([(cx + math.cos(a) * r * 0.36, cy + math.sin(a) * r * 0.36), (cx + math.cos(a) * r * 0.62, cy + math.sin(a) * r * 0.62)], fill=INK, width=max(2, int(r * 0.06)))


def figure(size, with_ball=True):
    """The yellow figure (1000-unit drawing, scaled), as chunky as the Clips runner: one arm up, right foot into a ball."""
    S = 1000
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    Y = YELLOW
    d.ellipse([235, 45, 425, 235], fill=Y)                                   # head
    limb(d, [(345, 275), (385, 400), (420, 530)], 160, 128, Y)               # torso
    limb(d, [(335, 315), (225, 290), (150, 175)], 100, 74, Y)                # back arm, fist up (like the Clips runner)
    limb(d, [(385, 335), (500, 395), (600, 350)], 94, 68, Y)                 # front arm
    limb(d, [(400, 545), (345, 735), (310, 930)], 128, 88, Y)                # standing leg
    limb(d, [(310, 930), (395, 945)], 86, 76, Y)                             # its foot
    limb(d, [(445, 555), (585, 650), (690, 720)], 128, 86, Y)                # striking leg
    limb(d, [(690, 720), (735, 700)], 80, 72, Y)                             # its foot
    if with_ball:
        ball = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        football(ImageDraw.Draw(ball), 835, 770, 85)
        m = Image.new("L", (S, S), 0)
        ImageDraw.Draw(m).ellipse([835 - 85, 770 - 85, 835 + 85, 770 + 85], fill=255)
        im.paste(ball, (0, 0), m)
    return im.resize((size, size), Image.LANCZOS)


def lockup(height):
    """Figure + 'MetaSports' + 'F C', proportioned like the Clips avatar: the figure is the full height, the two text lines are
    centred on it, the wordmark starts just past the figure's raised arm. Returns an RGBA image `height` px tall."""
    fig = figure(height)
    word = slanted("MetaSports", "Poppins-700.ttf", int(height * 0.34))
    fc = slanted("FC", "Poppins-700.ttf", int(height * 0.2), spacing=int(height * 0.13))
    gap = int(height * 0.06)
    block = word.height + gap + fc.height
    wx = int(fig.width * 0.62)
    wy = (height - block) // 2 - int(height * 0.07)
    im = Image.new("RGBA", (wx + word.width + 4, height), (0, 0, 0, 0))
    im.alpha_composite(fig, (0, 0))
    im.alpha_composite(word, (wx, wy))
    im.alpha_composite(fc, (wx + (word.width - fc.width) // 2 + int(height * 0.02), wy + word.height + gap))
    return im.crop(im.getbbox())


def profile(size=900):
    im = Image.new("RGBA", (size, size), RED + (255,))
    lk = lockup(size)
    lk = lk.resize((int(size * 0.84), int(lk.height * size * 0.84 / lk.width)), Image.LANCZOS)
    im.alpha_composite(lk, ((size - lk.width) // 2, (size - lk.height) // 2))
    return im.convert("RGB")


def banner():
    W, H = 2560, 1440
    im = Image.new("RGBA", (W, H), RED + (255,))
    d = ImageDraw.Draw(im)
    # pitch markings in a darker red, outside the text (TVs show the full banner; phones only the centre)
    lw = 10
    d.line([(W // 2, 0), (W // 2, H)], fill=RED_DARK, width=lw)
    d.ellipse([W // 2 - 360, H // 2 - 360, W // 2 + 360, H // 2 + 360], outline=RED_DARK, width=lw)
    for x0, x1 in ((-lw, 380), (W - 380, W + lw)):
        d.rectangle([x0, H // 2 - 540, x1, H // 2 + 540], outline=RED_DARK, width=lw)
        d.rectangle([x0 if x0 < 0 else W - 150, H // 2 - 240, 150 if x0 < 0 else x1, H // 2 + 240], outline=RED_DARK, width=lw)
    # the phone-safe centre: 1546 x 423
    sx0, sy0 = (W - 1546) // 2, (H - 423) // 2
    plate = Image.new("RGBA", (1546, 423), RED + (255,))
    im.alpha_composite(plate, (sx0, sy0))
    lk = lockup(380)
    lk = lk.resize((int(lk.width * 330 / lk.height), 330), Image.LANCZOS)
    lines = [slanted("Football stories that", "Poppins-600.ttf", 58, slant=0.0),
             slanted("sound fake but are", "Poppins-600.ttf", 58, slant=0.0),
             slanted("100% real", "Poppins-700.ttf", 58, fill=YELLOW, slant=0.0)]
    tag2 = slanted("NEW STORY EVERY DAY", "Poppins-700.ttf", 34, fill=WHITE, spacing=7, slant=0.2)
    gap = 60
    text_w = max(max(l.width for l in lines), tag2.width)
    total = lk.width + gap * 2 + 6 + text_w
    x = sx0 + (1546 - total) // 2
    im.alpha_composite(lk, (x, sy0 + (423 - lk.height) // 2))
    x += lk.width + gap
    d.rectangle([x, sy0 + 70, x + 5, sy0 + 353], fill=WHITE)  # divider
    x += 6 + gap
    y = sy0 + 62
    for l in lines:
        im.alpha_composite(l, (x, y))
        y += 78
    im.alpha_composite(tag2, (x, y + 18))
    return im.convert("RGB")


def watermark(size=150):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse([0, 0, S - 1, S - 1], fill=RED + (255,))
    fig = figure(int(S * 0.86))
    im.alpha_composite(fig, ((S - fig.width) // 2 - int(S * 0.02), (S - fig.height) // 2 + int(S * 0.02)))
    return im.resize((size, size), Image.LANCZOS)


p = profile(900)
p.save(os.path.join(D, "metasportsfc_profile_900.png"))
b = banner()
b.save(os.path.join(D, "metasportsfc_banner_2560x1440.jpg"), quality=93)
watermark().save(os.path.join(D, "metasportsfc_watermark_150.png"))
b.crop(((2560 - 1546) // 2, (1440 - 423) // 2, (2560 + 1546) // 2, (1440 + 423) // 2)).save(os.path.join(D, "preview_banner_phone.png"))
# side by side with the Clips avatar, as circles at 98 px and 48 px (how YouTube shows them)
clips = os.path.join(D, "_ref_metasportsclips_avatar.jpg")
m = Image.new("L", (900, 900), 0)
ImageDraw.Draw(m).ellipse([0, 0, 899, 899], fill=255)
sheet = Image.new("RGB", (460, 140), (255, 255, 255))
x = 20
for src in ([Image.open(clips).convert("RGB").resize((900, 900))] if os.path.exists(clips) else []) + [p]:
    for s in (98, 48):
        c = Image.new("RGBA", (900, 900), (0, 0, 0, 0))
        c.paste(src, (0, 0), m)
        c = c.resize((s, s), Image.LANCZOS)
        sheet.paste(c, (x, (140 - s) // 2), c)
        x += s + 20
sheet.save(os.path.join(D, "preview_profile_sizes.png"))
print("brand v2 ok")
