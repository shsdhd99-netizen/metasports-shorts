"""Wilt card: the public-domain 1962 photo, full width, low in a 9:16 frame over a blurred fill (room on top for the 126 overlay)."""
import os
from PIL import Image, ImageFilter, ImageEnhance
D = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(D, "wilt100.jpg")).convert("RGB")
bg = im.resize((1080, int(1080 * im.height / im.width))).resize((1080, 1920)).filter(ImageFilter.GaussianBlur(40))
bg = ImageEnhance.Brightness(bg).enhance(0.55)
fg = im.resize((1080, int(1080 * im.height / im.width)), Image.LANCZOS)
bg.paste(fg, (0, 1920 - fg.height - 30))
bg.save(os.path.join(D, "wilt_9x16.jpg"), quality=92)
