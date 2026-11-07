"""Red circle (and optional arrow) on the detail that makes the story, for an opening A/B test. Works on a finished video.

  python pointer.py IN.mp4 OUT.mp4 --x 540 --y 700 --r 150 [--t0 0] [--t1 2.5] [--arrow from-left|from-right|from-top|from-bottom|none] [--color red|yellow|white]

x, y, r are pixels on the 1080x1920 frame (centre and radius of the ring). The ring pops in over 0.15 s at t0 and is gone at t1.
Audio is copied untouched. Use it to make the 'pointer' twin of a Short (the plain one stays final.mp4).
Why (Oct 13 2026, Research Notes/Winning Formula v2): in the old era 7 of 27 Shorts with a red circle/arrow on the detail in frame 1
reached 40K+, vs 2 of 44 without (one coder; HYPOTHESIS). None of the Oct 2026 posts had one. Test it in pairs before adopting it.
"""
import argparse, math, os, subprocess, tempfile

from PIL import Image, ImageDraw

RED = (255, 42, 42, 255)
COLORS = {"red": RED, "yellow": (255, 214, 0, 255), "white": (255, 255, 255, 255)}  # Oct 13 critic v2: a red ring on a red banner reads as circling the logo


def ring_png(r, width, arrow, path, color=RED):
    pad = 140 if arrow != "none" else 12
    S = 2 * (r + width + pad)
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = S / 2
    for k in range(3):  # soft dark outline so the ring reads on bright floors and white jerseys
        d.ellipse([c - r - width / 2 - 3 + k, c - r - width / 2 - 3 + k, c + r + width / 2 + 3 - k, c + r + width / 2 + 3 - k], outline=(0, 0, 0, 70), width=2)
    d.ellipse([c - r - width / 2, c - r - width / 2, c + r + width / 2, c + r + width / 2], outline=color, width=width)
    if arrow != "none":
        ang = {"from-left": math.pi, "from-right": 0.0, "from-top": -math.pi / 2, "from-bottom": math.pi / 2}[arrow]
        tip = (c + math.cos(ang) * (r + width + 8), c + math.sin(ang) * (r + width + 8))
        tail = (c + math.cos(ang) * (r + width + pad - 10), c + math.sin(ang) * (r + width + pad - 10))
        d.line([tail, tip], fill=color, width=width + 2)
        for s in (-1, 1):
            a2 = ang + s * 0.5
            d.line([tip, (tip[0] + math.cos(a2) * 46, tip[1] + math.sin(a2) * 46)], fill=color, width=width + 2)
    im.save(path)
    return S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--x", type=float, required=True); ap.add_argument("--y", type=float, required=True)
    ap.add_argument("--r", type=float, default=140); ap.add_argument("--width", type=int, default=12)
    ap.add_argument("--t0", type=float, default=0.0); ap.add_argument("--t1", type=float, default=2.5)
    ap.add_argument("--arrow", default="none", choices=["none", "from-left", "from-right", "from-top", "from-bottom"])
    ap.add_argument("--color", default="red", choices=sorted(COLORS))
    a = ap.parse_args()
    png = tempfile.mktemp(suffix=".png")
    S = ring_png(int(a.r), a.width, a.arrow, png, COLORS[a.color])
    pop = 0.15
    # scale 1.25 -> 1.0 over 0.15 s (a 'pop'), then hold; enable only inside [t0, t1]
    sc = f"if(lt(t-{a.t0},{pop}),{S}*(1.25-0.25*(t-{a.t0})/{pop}),{S})"
    fc = (f"[1:v]format=rgba,scale=w='{sc}':h='{sc}':eval=frame[ring];"
          f"[0:v][ring]overlay=x='{a.x}-overlay_w/2':y='{a.y}-overlay_h/2':enable='between(t,{a.t0},{a.t1})':eval=frame,format=yuv420p[v]")
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-loop", "1", "-i", png, "-filter_complex", fc,
                        "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-c:a", "copy",
                        "-shortest", "-movflags", "+faststart", a.out], capture_output=True, text=True)
    os.remove(png)
    if r.returncode:
        raise SystemExit(r.stderr[-400:])
    print(f"Done: {a.out} (ring at {a.x:.0f},{a.y:.0f} r{a.r:.0f}, {a.t0}-{a.t1} s, arrow {a.arrow}, {a.color})")


if __name__ == "__main__":
    main()
