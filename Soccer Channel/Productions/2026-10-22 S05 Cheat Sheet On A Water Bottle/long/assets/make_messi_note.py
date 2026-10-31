"""Messi's line on Pickford's 2026 bottle ('FAKE LEFT - DIVE RIGHT'), boxed, in the same layout as feel_9x16.jpg (long cut)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(D, "x_4999_HNUlVdFXUAENRjq.jpg")).convert("RGB")   # 643x970 photo shared on X
bg = ImageEnhance.Brightness(src.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(30))).enhance(0.45)
crop = src.crop((92, 222, 472, 440))                       # the list's title, Messi and the next four names
W = 980; crop = crop.resize((W, int(crop.height * W / crop.width)), Image.LANCZOS)
x0, y0 = 50, 72
frame = Image.new("RGB", (W + 24, crop.height + 24), "white")
bg.paste(frame, (x0 - 12, y0 - 12)); bg.paste(crop, (x0, y0))
d = ImageDraw.Draw(bg)
s = W / 380                                                # source px -> card px
top, bot = y0 + int((295 - 222) * s), y0 + int((323.5 - 222) * s)   # the MESSI row
d.rectangle([x0 - 16, top, x0 + W + 16, bot], outline=(226, 30, 40), width=7)
f = ImageFont.truetype(os.path.join(D, "..", "..", "..", "..", "..", "Tools", "fonts", "DMSans-Bold.ttf"), 30)
cap = "Pickford's bottle, World Cup 2026 semi-final (photo shared on X)"
tw = d.textlength(cap, font=f)
d.text(((1080 - tw) / 2, y0 + crop.height + 26), cap, font=f, fill=(200, 200, 205))
bg.save(os.path.join(D, "messi_note_9x16.jpg"), quality=92)
print("card bottom", y0 + crop.height + 60)
