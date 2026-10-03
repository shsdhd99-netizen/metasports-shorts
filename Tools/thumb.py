"""Thumbnail maker (run with: py -3.14 thumb.py ...).

Commentary (16:9, the style that works in the COD-commentary scene):
  py -3.14 thumb.py --bg "gameplay.png" --text "SPECTATOR MODE" --cutout "character.png" --out "thumb.png"
  --variants 3  -> makes 3 versions (A/B/C) for YouTube's Test & Compare
MetaSports cover (9:16, optional custom Short thumbnail):
  py -3.14 thumb.py --shape short --bg "frame.png" --text "53 YEARS" --out "cover.png"

--cutout must be a PNG with a transparent background (a character/meme you made or own).
No --bg? A dark gradient is used so you can preview the text.
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

FONT = r"C:\Windows\Fonts\impact.ttf"
STYLES = {  # fill, stroke
    "yellow": ((255, 214, 0), (0, 0, 0)),
    "white": ((255, 255, 255), (0, 0, 0)),
    "orange": ((255, 107, 26), (11, 26, 51)),
}


def cover(img, size):
    return ImageOps.fit(img.convert("RGB"), size, Image.LANCZOS)


def fit_font(draw, text, max_w, max_h, start):
    size = start
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        b = draw.multiline_textbbox((0, 0), text, font=f, stroke_width=max(4, size // 12), spacing=4)
        if b[2] - b[0] <= max_w and b[3] - b[1] <= max_h:
            return f
        size -= 4
    return ImageFont.truetype(FONT, 20)


def sticker(cut, height):
    cut = cut.convert("RGBA")
    cut = cut.resize((max(1, int(cut.width * height / cut.height)), height), Image.LANCZOS)
    alpha = cut.split()[3]
    ring = alpha.filter(ImageFilter.MaxFilter(15))
    out = Image.new("RGBA", cut.size, (0, 0, 0, 0))
    white = Image.new("RGBA", cut.size, (255, 255, 255, 255))
    out.paste(white, (0, 0), ring)
    out.alpha_composite(cut)
    return out


def make(bg_path, text, cutout, shape, layout, style, out):
    W, H = (1280, 720) if shape == "long" else (1080, 1920)
    if bg_path and os.path.exists(bg_path):
        base = cover(Image.open(bg_path), (W, H)).convert("RGBA")
    else:
        base = Image.linear_gradient("L").resize((W, H)).point(lambda p: 30 + p // 5).convert("RGBA")
    # darken the text zone slightly so words pop
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(shade)
    band = (0, 0, W, int(H * 0.30)) if layout != "bottom" else (0, int(H * 0.70), W, H)
    d.rectangle(band, fill=(0, 0, 0, 70))
    base = Image.alpha_composite(base, shade.filter(ImageFilter.GaussianBlur(25)))
    if cutout and os.path.exists(cutout):
        st = sticker(Image.open(cutout), int(H * (0.78 if shape == "long" else 0.45)))
        x = 20 if layout != "right" else W - st.width - 20
        y = H - st.height if shape == "long" else int(H * 0.40)
        base.alpha_composite(st, (max(0, x), max(0, y)))
    draw = ImageDraw.Draw(base)
    fill, stroke = STYLES[style]
    text = text.upper()
    if shape == "long":
        box_w, box_h = int(W * 0.92), int(H * 0.26)
        f = fit_font(draw, text, box_w, box_h, 150)
        bb = draw.multiline_textbbox((0, 0), text, font=f, stroke_width=max(4, f.size // 12), spacing=4)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        x = (W - tw) // 2 if layout != "right" else W - tw - 30
        y = 18 if layout != "bottom" else H - th - 40
    else:
        box_w, box_h = int(W * 0.86), int(H * 0.22)
        f = fit_font(draw, text, box_w, box_h, 190)
        bb = draw.multiline_textbbox((0, 0), text, font=f, stroke_width=max(4, f.size // 12), spacing=4)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        x, y = (W - tw) // 2, int(H * 0.16)
    draw.multiline_text((x - bb[0], y - bb[1]), text, font=f, fill=fill, stroke_width=max(4, f.size // 12),
                        stroke_fill=stroke, spacing=4, align="center")
    base.convert("RGB").save(out, quality=95)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg")
    ap.add_argument("--text", required=True, help='2-3 words; use \\n for a line break')
    ap.add_argument("--cutout")
    ap.add_argument("--shape", choices=["long", "short"], default="long")
    ap.add_argument("--style", choices=list(STYLES), default="yellow")
    ap.add_argument("--variants", type=int, default=1)
    ap.add_argument("--out", default="thumbnail.png")
    a = ap.parse_args()
    text = a.text.replace("\\n", "\n")
    if a.variants <= 1:
        print(make(a.bg, text, a.cutout, a.shape, "top", a.style, a.out))
        return
    root, ext = os.path.splitext(a.out)
    combos = [("top", a.style, "A"), ("right", "white", "B"), ("bottom", "orange" if a.style != "orange" else "yellow", "C")]
    for layout, style, tag in combos[:a.variants]:
        print(make(a.bg, text, a.cutout, a.shape, layout, style, f"{root}_{tag}{ext}"))


if __name__ == "__main__":
    main()
