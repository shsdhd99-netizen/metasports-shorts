"""Recreation of the Messi napkin (NOT the real napkin; labelled 'recreation' on the picture).
Wording = the English translation quoted by NPR/90min (see notes.md). Graphics stay above y=890 (captions sit at y=960)."""
import os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
out = os.path.dirname(__file__)
hand = r"C:\Windows\Fonts\Inkfree.ttf"
sans = os.path.join(out, "..", "..", "..", "..", "Tools", "fonts", "TikTok-Sans-SemiBold.ttf")
random.seed(4)

def bg():
    im = Image.new("RGB", (1080, 1920))
    d = ImageDraw.Draw(im)
    for y in range(1920):
        c = int(28 + 22 * (1 - y / 1920))
        d.line([(0, y), (1080, y)], fill=(c + 8, c + 4, c))
    return im

def napkin(lines, w=760, h=640, circle=None):
    n = Image.new("RGBA", (w, h), (250, 248, 242, 255))
    d = ImageDraw.Draw(n)
    for _ in range(9000):  # paper grain
        x, y = random.randrange(w), random.randrange(h)
        v = random.randrange(222, 244)
        d.point((x, y), fill=(v, v, v - 4, 255))
    for x in range(30, w, 38):  # embossed dots
        for y in range(30, h, 38):
            d.ellipse([x, y, x + 3, y + 3], fill=(232, 230, 222, 255))
    d.line([(w // 2, 0), (w // 2, h)], fill=(226, 224, 216, 255), width=3)  # fold
    d.line([(0, h // 2), (w, h // 2)], fill=(226, 224, 216, 255), width=3)
    boxes = []
    for (txt, size, x, y) in lines:
        f = ImageFont.truetype(hand, size)
        d.text((x, y), txt, font=f, fill=(24, 40, 130, 255))
        boxes.append(d.textbbox((x, y), txt, font=f))
    d.text((w - 190, h - 44), "recreation", font=ImageFont.truetype(sans, 28), fill=(150, 145, 135, 255))
    if circle is not None:
        b = boxes[circle]
        for k in range(5):
            d.ellipse([b[0] - 14 - k, b[1] - 8 - k, b[2] + 14 + k, b[3] + 8 + k], outline=(210, 30, 30, 255))
    return n

def place(base, n, angle, cx, cy, scale=1.0):
    if scale != 1.0:
        n = n.resize((int(n.width * scale), int(n.height * scale)), Image.LANCZOS)
    pad = 50
    sh = Image.new("RGBA", (n.width + 2 * pad, n.height + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([pad + 10, pad + 14, pad + n.width + 10, pad + n.height + 14], fill=(0, 0, 0, 150))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    sh.alpha_composite(n, (pad, pad))
    sh = sh.rotate(angle, resample=Image.BICUBIC, expand=True)
    base.paste(sh, (cx - sh.width // 2, cy - sh.height // 2), sh)

L1 = [("In Barcelona, 14th of December 2000", 40, 40, 50),
      ("hereby agrees, under his responsibility and", 40, 40, 160),
      ("regardless of any", 62, 40, 250),
      ("dissenting opinions,", 62, 40, 335),
      ("to sign the player", 56, 40, 450),
      ("Lionel Messi", 78, 40, 520)]
# frame 1: whole napkin, tilted
b = bg(); place(b, napkin(L1, 760, 640), -5, 540, 470, 1.18)
d = ImageDraw.Draw(b)
b.convert("RGB").save(os.path.join(out, "napkin_f1.jpg"), quality=93)
# close-up with the key words circled
b2 = bg(); place(b2, napkin(L1, 760, 640, circle=3), 3, 540, 470, 1.3)
b2.convert("RGB").save(os.path.join(out, "napkin_f2.jpg"), quality=93)
print("ok")
# f3: sold-at-auction frame (price from NPR/Bonhams: 762,400 pounds, May 2024)
b3 = bg(); place(b3, napkin(L1, 760, 640), 4, 540, 310, 0.88)
st = Image.new("RGBA", (900, 220), (0, 0, 0, 0))
sd = ImageDraw.Draw(st)
sd.rounded_rectangle([0, 0, 899, 219], 24, outline=(210, 30, 30, 255), width=10)
sd.text((40, 20), "SOLD  \u00a3762,400", font=ImageFont.truetype(sans, 96), fill=(210, 30, 30, 255))
sd.text((44, 150), "Bonhams auction, May 2024", font=ImageFont.truetype(sans, 40), fill=(210, 30, 30, 255))
st = st.rotate(-9, resample=Image.BICUBIC, expand=True)
b3.paste(st, (80, 580), st)
b3.convert("RGB").save(os.path.join(out, "napkin_f3.jpg"), quality=93)
