"""S03 cards as full 9:16 frames (broll.py still). Every card stays above y=890 so the centred captions (y=960) sit on the dark fill.
  reina.jpg      : Pepe Reina playing for Liverpool, 2007. Photo: Agnieszka Mieszczak / Wikimedia Commons, CC BY 2.0
                   (File:Pepe_Reina.JPG, via the thumbnail host). The credit is printed on the card.
  bg_dudek.jpg   : frame of Dudek with the trophy (archive.org, 2005 final celebration, 5:31) for the blurred backgrounds.
  card_games.jpg : Dudek's Liverpool games per season, all competitions, from LFChistory.net (lfchistory.net/players/292):
                   2004-05: 41, 2005-06: 6, 2006-07: 6. liverpoolfc.com: "restricted to just 12 appearances in the two years that followed".
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(D, "..", "..", "..", "Brand", "fonts")
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)
RED, WHITE, GREY = (229, 28, 36), (255, 255, 255), (200, 200, 200)


def bg(name="bg_dudek.jpg", dim=0.45):
    b = Image.open(os.path.join(D, name)).convert("RGB")
    b = b.resize((int(b.width * 1920 / b.height), 1920))
    x = (b.width - 1080) // 2
    b = b.crop((x, 0, x + 1080, 1920))
    return Image.eval(b.filter(ImageFilter.GaussianBlur(28)), lambda v: int(v * dim))


def centred(d, y, text, font, fill=WHITE):
    w = d.textlength(text, font=font)
    d.text(((1080 - w) / 2, y), text, font=font, fill=fill)


# Reina: the photo on a white plate, credit under it
f = bg()
p = Image.open(os.path.join(D, "reina.jpg")).convert("RGB")
w = 660
p = p.resize((w, int(p.height * w / p.width)), Image.LANCZOS)
top = 60
plate = Image.new("RGB", (w + 24, p.height + 24), WHITE)
plate.paste(p, (12, 12))
f.paste(plate, ((1080 - plate.width) // 2, top))
d = ImageDraw.Draw(f)
centred(d, top + plate.height + 14, "Photo: Agnieszka Mieszczak / Wikimedia Commons, CC BY 2.0", F("Poppins-600.ttf", 22), GREY)
assert top + plate.height + 14 + 30 <= 890, "Reina card would sit under the captions"
f.save(os.path.join(D, "card_reina.jpg"), quality=92)

# Dudek's Liverpool games per season
f = bg()
d = ImageDraw.Draw(f)
centred(d, 70, "JERZY DUDEK", F("Poppins-700.ttf", 78))
centred(d, 165, "Liverpool games, all competitions", F("Poppins-600.ttf", 40), GREY)
rows = [("2004-05", 41, "won the Champions League"), ("2005-06", 6, ""), ("2006-07", 6, "")]
y, x0, maxw = 270, 300, 620
for season, n, note in rows:
    d.text((60, y + 8), season, font=F("Poppins-600.ttf", 46), fill=WHITE)
    bw = max(24, int(maxw * n / 41))
    d.rounded_rectangle([x0, y, x0 + bw, y + 80], radius=12, fill=RED if n < 41 else WHITE)
    lbl = str(n)
    lf = F("Poppins-700.ttf", 54)
    if n == 41:
        d.text((x0 + bw - d.textlength(lbl, font=lf) - 20, y + 6), lbl, font=lf, fill=(25, 25, 25))
        d.text((x0, y + 92), note, font=F("Poppins-600.ttf", 30), fill=GREY)
    else:
        d.text((x0 + bw + 20, y + 6), lbl, font=lf, fill=WHITE)
    y += 150
centred(d, y + 10, "12 games in two seasons", F("Poppins-700.ttf", 52), (255, 193, 0))
centred(d, y + 82, "Source: LFChistory.net", F("Poppins-600.ttf", 24), GREY)
assert y + 82 + 34 <= 890, f"stats card bottom {y + 116} would sit under the captions"
f.save(os.path.join(D, "card_games.jpg"), quality=92)
print("S03 cards ok")
