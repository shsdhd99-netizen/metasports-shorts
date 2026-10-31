"""Every shot as it is used: its first, middle and last frame, 3 tiles a shot, 6 shots a row (Oct 24 2026; was a scratch helper).

  python Tools/shot_strip.py "<Short folder>" out.jpg

Look at it after cut_list.py: the middle frame alone (cut_list's _check/sheet.jpg) misses a dark first frame, a dissolve at
the end of a shot or a player who walks out of the crop.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw
F, OUT = sys.argv[1], sys.argv[2]
shots = json.load(open(os.path.join(F, "shots.json"))); words = json.load(open(os.path.join(F, "words.json")))
total = words[-1]["end"] + 0.3; tmp = tempfile.mkdtemp(); tiles = []
for i, s in enumerate(shots):
    d = (shots[i + 1]["start"] if i + 1 < len(shots) else total) - s["start"]
    for k, t in enumerate((0.04, d / 2, max(0.04, d - 0.06))):
        p = os.path.join(tmp, f"{i}_{k}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", os.path.join(F, "clips", s["clip"]), "-frames:v", "1", "-vf", "scale=150:266", p])
        im = Image.open(p) if os.path.exists(p) else Image.new("RGB", (150, 266), "red")
        ImageDraw.Draw(im).text((3, 3), f"{i} {s['clip'][:-4]} {t:.2f}", fill="yellow"); tiles.append(im)
cols = 18; rows = (len(tiles) + cols - 1) // cols
sh = Image.new("RGB", (150 * cols, 266 * rows))
for k, im in enumerate(tiles): sh.paste(im, ((k % cols) * 150, (k // cols) * 266))
sh.save(OUT, quality=85); print(OUT, sh.size)
