"""Evidence card: screenshot a web page, crop the headline and the one line that matters, put a red box on it, make the 9:16 clip.

  python card.py --url <page> --mark "text on the page to box" --out clips/c01.mp4 --len 2.4 [--mark "second box"] [--headline 190,470] [--byline 488,575]
  python card.py --png shot.png --crop 300,1405,1520,1500 --box 225,32,560,52 --out clips/c01.mp4 --len 2

How it works: webshot.mjs takes a full-page shot and reports where each --mark text is; this crops [headline][byline][the marked lines],
fixes washed-out ESPN pages (a dim overlay) with auto-contrast, and runs broll.py page with the red box timed 0.35 s in.
Cards sit at 14% from the top so the centred captions never cover them. Check the PNG next to the clip before using it.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def compose(src, parts, out, boxes_src, x0=300, x1=1520, gap=18):
    from PIL import Image, ImageOps
    e = ImageOps.autocontrast(Image.open(src).convert("RGB"), cutoff=0.5)
    crops = [e.crop((x0, a, x1, b)) for a, b in parts]
    c = Image.new("RGB", (x1 - x0, sum(p.height for p in crops) + gap * (len(crops) + 1)), (255, 255, 255))
    y, offs = gap, []
    for (a, b), cr in zip(parts, crops):
        c.paste(cr, (0, y)); offs.append((a, b, y)); y += cr.height + gap
    boxes = []
    for (x, yy, w, h) in boxes_src:
        for a, b, oy in offs:
            if a <= yy < b:
                boxes.append((max(0, x - x0 - 6), oy + yy - a - 4, w + 12, h + 8)); break
    c.save(out)
    return boxes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url"); ap.add_argument("--png"); ap.add_argument("--out", required=True)
    ap.add_argument("--mark", action="append", default=[], help="text on the page to box (repeatable)")
    ap.add_argument("--len", type=float, default=2.4)
    ap.add_argument("--headline", default="", help="y0,y1 of the headline in the full-page shot (omit for none)")
    ap.add_argument("--byline", default="")
    ap.add_argument("--x", default="300,1520", help="x0,x1 of the article column")
    ap.add_argument("--pad", type=int, default=45, help="rows above/below a marked line to keep")
    ap.add_argument("--zoom", default="1.0,1.22")
    a = ap.parse_args()
    png = a.png
    marks = []
    if a.url:
        png = os.path.splitext(a.out)[0] + "_page.png"
        cmd = ["node", os.path.join(HERE, "webshot.mjs"), "--url", a.url, "--full", "--wait", "5000", "--out", png]
        for m in a.mark:
            cmd += ["--mark", m]
        r = json.loads(subprocess.run(cmd, capture_output=True, text=True).stdout.strip().splitlines()[-1])
        marks = [(m["x"], m["y"], m["w"], m["h"]) for m in r["marks"] if not m.get("missing")]
        miss = [m["text"] for m in r["marks"] if m.get("missing")]
        if miss:
            print("not found on the page:", miss)
        if not marks:
            raise SystemExit("nothing to box")
    parts = []
    for v in (a.headline, a.byline):
        if v:
            parts.append(tuple(int(t) for t in v.split(",")))
    ys = sorted(m[1] for m in marks)
    parts.append((max(0, ys[0] - a.pad), ys[-1] + a.pad + 60))
    x0, x1 = (int(t) for t in a.x.split(","))
    card = os.path.splitext(a.out)[0] + ".png"
    boxes = compose(png, parts, card, marks, x0=x0, x1=x1)
    cmd = [sys.executable, os.path.join(HERE, "broll.py"), "page", card, "--len", str(a.len), "--out", a.out, "--y", "0.14",
           "--mark-at", "0.35", "--width", "1.0", "--zoom", a.zoom]
    for b in boxes:
        cmd += ["--box", ",".join(str(int(v)) for v in b)]
    print(subprocess.run(cmd, capture_output=True, text=True).stdout.strip())


if __name__ == "__main__":
    main()
