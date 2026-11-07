"""S02 evidence cards as full 9:16 frames (for broll.py still). Every card stays above y=890 so the captions (y=960) sit on the dark fill.
  bbc_headline.png  : BBC Sport, Oct 22 2011, "Mario Balotelli unhurt in firework blaze ahead of Man Utd - City derby" (webshot.mjs)
  mcfc_page.png     : mancity.com, Mon 24 Oct 2011 21:00, "Mario backs firework safety campaign" (webshot.mjs, scale 2)
  motd_record_graphic.png : BBC Match of the Day graphic at 18:45 of the archive.org highlights ("RECORD-BREAKING GAME")
"""
import os
from PIL import Image, ImageDraw, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))


def bg():
    b = Image.open(os.path.join(D, "bg_oldtrafford.jpg")).convert("RGB")
    b = b.resize((int(b.width * 1920 / b.height), 1920)).crop((0, 0, 1080, 1920)) if b.width * 1920 / b.height >= 1080 else b.resize((1080, 1920))
    return Image.eval(b.filter(ImageFilter.GaussianBlur(30)), lambda v: int(v * 0.5))


def place(card, width, top=80, pad=30, box=None):
    f = bg()
    c = card.resize((width - 2 * pad, int(card.height * (width - 2 * pad) / card.width)), Image.LANCZOS)
    plate = Image.new("RGB", (width, c.height + 2 * pad), (255, 255, 255))
    plate.paste(c, (pad, pad))
    x = (1080 - width) // 2
    f.paste(plate, (x, top))
    assert top + plate.height <= 890, f"card bottom {top + plate.height} would sit under the captions"
    if box:  # red box in card pixels
        s = (width - 2 * pad) / card.width
        d = ImageDraw.Draw(f)
        bx = [x + pad + box[0] * s - 8, top + pad + box[1] * s - 6, x + pad + box[2] * s + 8, top + pad + box[3] * s + 6]
        for k in range(6):
            d.rectangle([bx[0] - k, bx[1] - k, bx[2] + k, bx[3] + k], outline=(225, 30, 30))
    return f


bbc = Image.open(os.path.join(D, "bbc_headline.png")).convert("RGB").crop((0, 0, 1260, 384))
place(bbc, 1000, top=300).save(os.path.join(D, "card_bbc.jpg"), quality=92)
rb = Image.open(os.path.join(D, "motd_record_graphic.png")).convert("RGB").crop((262, 82, 1022, 640))
place(rb, 1040, top=80, pad=0, box=(18, 420, 540, 456)).save(os.path.join(D, "card_1955.jpg"), quality=92)
mc = Image.open(os.path.join(D, "mcfc_page.png")).convert("RGB").crop((280, 150, 1720, 1440))
place(mc, 920, top=40).save(os.path.join(D, "card_mcfc.jpg"), quality=92)
print("cards ok")
lu = Image.open(os.path.join(D, "motd_lineup.png")).convert("RGB").crop((270, 20, 1045, 670))
place(lu, 1000, top=40, pad=0, box=(120, 95, 245, 192)).save(os.path.join(D, "card_lineup.jpg"), quality=92)
print("lineup ok")
