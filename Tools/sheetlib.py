"""Contact-sheet helpers drawn with PIL (Nov 1 2026). ffmpeg drawtext needs a fontconfig file, which this PC lacks
('Fontconfig error: Cannot load default config file'), so numbered tiles are labelled and tiled here instead.
  label(im, text)            -> yellow text on a black box, top-left of a PIL image
  grid(images, cols, out)    -> pastes equal-size tiles into one jpg (black background)
"""
import os
from PIL import Image, ImageDraw, ImageFont

_FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "DMSans-Bold.ttf")


def _font(size):
    for p in (_FONT, "C:/Windows/Fonts/arialbd.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()


def label(im, text, size=20):
    im = im.convert("RGB")
    d = ImageDraw.Draw(im)
    f = _font(size)
    x0, y0, x1, y1 = d.textbbox((4, 4), str(text), font=f)
    d.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], fill="black")
    d.text((4, 4), str(text), font=f, fill="yellow")
    return im


def grid(images, cols, out, tile=None):
    """Tiles are placed left to right, row by row; `tile` = (w, h), default the first image's size."""
    w, h = tile or images[0].size
    rows = (len(images) + cols - 1) // cols
    sh = Image.new("RGB", (w * cols, h * rows), "black")
    for k, im in enumerate(images):
        sh.paste(im.convert("RGB").resize((w, h)), ((k % cols) * w, (k // cols) * h))
    sh.save(out, quality=88)
    return out
