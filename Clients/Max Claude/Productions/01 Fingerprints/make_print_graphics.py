"""Fingerprint illustration clips for the Fingerprints lesson (Nov 3, 2026).

Drawn from maths, so they are ours to use (no stock licence). Three 1080x1920 clips, 30 fps, marked "Illustration":
  gfx_ridges.mp4   ridges appear as if dusted with powder (4 s)
  gfx_minutiae.mp4 the same print, close-up, with three details circled and the word "minutiae" (4 s)
  gfx_match.mp4    a partial print beside a stored print, a scan bar, lines between matching points,
                   then "Possible match" and "Examiner confirms" (5 s)
Run: python make_print_graphics.py  (needs numpy, Pillow, ffmpeg)
"""
import subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = np.array([16, 24, 40], np.float32)       # deep navy
INK = np.array([236, 176, 92], np.float32)    # warm amber ridges
CYAN = (92, 200, 210)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(sz):
    try:
        return ImageFont.truetype(FONT, sz)
    except OSError:
        return ImageFont.load_default()


def ridge_field(w, h, scale=1.0, seed=3, spacing=22.0, minutiae=()):
    """A loop/whorl-like ridge pattern inside a fingertip-shaped mask; returns (ridges 0..1, mask 0..1).
    minutiae: (x, y, sign) points in pixels where a ridge splits or ends (a phase dislocation, the standard
    mathematical model of a minutia), so the circles in the close-up sit on real splits and endings."""
    rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    cx, cy = w / 2, h * 0.47
    sx, sy = w * 0.30 * scale, h * 0.25 * scale
    nx, ny = (x - cx) / sx, (y - cy) / sy
    r = np.sqrt(nx ** 2 + (ny * 0.9) ** 2)
    th = np.arctan2(ny, nx)
    warp = np.zeros_like(r)
    for k in range(1, 5):
        a, b, p = rng.normal(0, 0.05 / k), rng.normal(0, 0.05 / k), rng.uniform(0, 6.28)
        warp += a * np.sin(k * 2.3 * nx + p) + b * np.cos(k * 1.9 * ny + p)
    freq = 2 * np.pi * sx / spacing
    phase = (r + 0.22 * np.sin(2 * th) * r * np.exp(-1.5 * r) + warp) * freq
    for (mx, my, s) in minutiae:
        phase += s * np.arctan2(y - my, x - mx)
    ridges = 0.5 + 0.5 * np.cos(phase)
    ridges = np.clip((ridges - 0.32) * 2.4, 0, 1)
    tip = np.sqrt((nx / 1.05) ** 2 + (np.where(ny < 0, ny / 1.25, ny / 1.05)) ** 2)
    mask = np.clip((1.12 - tip) * 6.0, 0, 1)
    return ridges, mask


def compose(ridges, mask, alpha):
    a = (ridges * mask * alpha)[..., None]
    return (BG * (1 - a) + INK * a).astype(np.uint8)


def label(img, text, xy, size=54, fill=(240, 240, 240), anchor="mm"):
    d = ImageDraw.Draw(img)
    d.text(xy, text, font=font(size), fill=fill, anchor=anchor)


def tag(img):
    label(img, "Illustration", (W - 40, H - 60), size=30, fill=(150, 160, 180), anchor="rm")


def writer(path, n):
    return subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", path],
                            stdin=subprocess.PIPE)


def clip_ridges():
    ridges, mask = ridge_field(W, H)
    rng = np.random.default_rng(7)
    grain = rng.random((H, W)).astype(np.float32)
    n = 4 * FPS
    p = writer("src/gfx_ridges.mp4", n)
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    dist = np.sqrt((x - W * 0.3) ** 2 + (y - H * 0.35) ** 2) / np.hypot(W, H)
    for i in range(n):
        t = i / (n - 1)
        reveal = np.clip((t * 1.25 - dist * 1.1) * 4 + (grain - 0.5) * 0.6, 0, 1)   # powder sweeps across
        img = Image.fromarray(compose(ridges, mask, reveal))
        tag(img)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()


def clip_minutiae():
    pts = [(330, 760, 1), (720, 980, -1), (470, 1300, 1)]
    ridges, mask = ridge_field(W, H, scale=1.9, seed=3, spacing=40.0, minutiae=pts)
    base = Image.fromarray(compose(ridges, mask, 1.0))
    n = 4 * FPS
    p = writer("src/gfx_minutiae.mp4", n)
    for i in range(n):
        t = i / FPS
        img = base.copy(); d = ImageDraw.Draw(img)
        for k, (px, py, _) in enumerate(pts):
            start = 0.4 + 0.6 * k
            if t > start:
                grow = min(1.0, (t - start) / 0.35)
                r = int(70 * grow) + 6
                d.ellipse([px - r, py - r, px + r, py + r], outline=CYAN, width=8)
        if t > 2.4:
            d.rounded_rectangle([W // 2 - 260, 230, W // 2 + 260, 370], radius=28, fill=tuple(int(c) for c in BG))
            label(img, "minutiae", (W // 2, 300), size=92, fill=CYAN)
        tag(img)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()


def clip_match():
    pw, ph = 470, 820
    ridges, mask = ridge_field(pw, ph, scale=1.15, seed=11, spacing=16.0)
    stored = Image.fromarray(compose(ridges, mask, 1.0))
    rng = np.random.default_rng(5)
    low = Image.fromarray((rng.random((ph // 40 + 2, pw // 40 + 2)) * 255).astype(np.uint8)).resize((pw, ph), Image.BICUBIC)
    holes = np.clip((np.asarray(low, np.float32) / 255 - 0.35) * 4, 0, 1)
    yy = np.linspace(0, 1, ph)[:, None]
    partial_mask = mask * holes * np.clip((0.75 - yy) * 5, 0, 1)          # smudged, top part only
    partial = Image.fromarray(compose(ridges, partial_mask, 1.0))
    lx, rx, top = 50, W - 50 - pw, 520
    matches = [(150, 180), (300, 250), (220, 360), (340, 130), (120, 300)]
    n = 5 * FPS
    p = writer("src/gfx_match.mp4", n)
    for i in range(n):
        t = i / FPS
        img = Image.new("RGB", (W, H), tuple(int(c) for c in BG))
        img.paste(partial, (lx, top)); img.paste(stored, (rx, top))
        d = ImageDraw.Draw(img)
        label(img, "Crime scene print", (lx + pw // 2, top - 50), size=40, fill=(200, 205, 215))
        label(img, "Stored print", (rx + pw // 2, top - 50), size=40, fill=(200, 205, 215))
        if t < 2.0:   # scan bar sweeps the database side
            yb = top + int((t / 2.0) * ph)
            d.rectangle([rx, yb - 6, rx + pw, yb + 6], fill=CYAN)
        shown = int(min(len(matches), max(0, (t - 1.8) / 0.25)))
        for (mx, my) in matches[:shown]:
            a, b = (lx + mx, top + my), (rx + mx, top + my)
            d.line([a, b], fill=CYAN, width=4)
            for (cx, cy) in (a, b):
                d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline=CYAN, width=5)
        if t > 3.2:
            label(img, "Possible match", (W // 2, top + ph + 140), size=80, fill=(240, 240, 240))
        if t > 4.0:
            label(img, "Examiner confirms", (W // 2, top + ph + 250), size=60, fill=CYAN)
        tag(img)
        p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()


if __name__ == "__main__":
    clip_ridges(); clip_minutiae(); clip_match()
    print("wrote src/gfx_ridges.mp4, src/gfx_minutiae.mp4, src/gfx_match.mp4")
