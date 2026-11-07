"""The whole 'ARGENTINA PENALTY TAKER LIST' on Pickford's 2026 bottle, framed above the caption line (long cut)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(D, "x_4999_HNUlVdFXUAENRjq.jpg")).convert("RGB")   # 643x970 photo shared on X
bg = ImageEnhance.Brightness(src.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(30))).enhance(0.45)
crop = src.crop((92, 222, 472, 900))                      # title to the last name (Rulli)
H = 700; crop = crop.resize((int(crop.width * H / crop.height), H), Image.LANCZOS)
x0, y0 = (1080 - crop.width) // 2, 72
frame = Image.new("RGB", (crop.width + 24, H + 24), "white")
bg.paste(frame, (x0 - 12, y0 - 12)); bg.paste(crop, (x0, y0))
d = ImageDraw.Draw(bg)
f = ImageFont.truetype(os.path.join(D, "..", "..", "..", "..", "..", "Tools", "fonts", "DMSans-Bold.ttf"), 30)
cap = "Pickford's bottle, World Cup 2026 semi-final (photo shared on X)"
d.text(((1080 - d.textlength(cap, font=f)) / 2, y0 + H + 26), cap, font=f, fill=(200, 200, 205))
bg.save(os.path.join(D, "list_9x16.jpg"), quality=92)
print("card bottom", y0 + H + 60)
