"""S05 v2 patch (Oct 26, owner: no cards): replace the card segments of the finished render with footage, burn the same captions on them,
and splice them back in frame-accurately. The voice, music and effects stay exactly as rendered."""
import json, os, subprocess, sys
D = sys.argv[1]; P = os.path.join(D, "_patch_v2"); T = os.path.abspath("Tools")
FPS = 30
W = "white"
def ov(text, sub, size=200, start=0.05, end=9, y=300):
    return [dict(text=text, size=size, color=W, y=y, start=start, end=end, sub=sub)]
# (name, first frame, end frame, kind, source spec, overlay)
segs = [
    ("p1990", 229, 266, "action", ("cut", "src/g90.mp4", 3.5, {"x": 0.45}), ov("1990", "LOST")),
    ("p1998", 266, 293, "action", ("cut", "src/g98.mp4", 2.5, {"x": 0.45}), ov("1998", "LOST")),
    ("p2006", 293, 327, "action", ("cut", "src/g06.mp4", 3.0, {"blurfit": True}), ov("2006", "LOST")),
    ("pmbs", 1328, 1409, "action", ("still", "_patch_v2/mbs_9x16.jpg"), ov("ENG v ARG", "WORLD CUP SEMI-FINAL", 190)),
    ("pbottle2", 1409, 1467, "action", ("still", "_patch_v2/bottle2_9x16.jpg"), None),
    ("pgoals", 1467, 1552, "action", ("cut", "src/stock_18781.mp4", 1.0, {}), ov("85' & 90+2'", "ARGENTINA SCORED", 170)),
    ("pbox", 1692, 1758, "action", ("still", "_patch_v2/bottle_box_9x16.jpg"), None),
]
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: raise SystemExit(" ".join(cmd) + "\n" + r.stderr[-1500:])
out = []
for name, f0, f1, kind, src, overlay in segs:
    n = f1 - f0; dur = n / FPS; raw = f"{P}/{name}_raw.mp4"
    if src[0] == "cut":
        cmd = [sys.executable, f"{T}/broll.py", "cut", f"{D}/{src[1]}", "--at", str(src[2]), "--len", f"{dur + 0.2:.2f}", "--out", raw]
        for k, v in src[3].items():
            cmd += [f"--{k}"] + ([] if v is True else [str(v)])
    else:
        cmd = [sys.executable, f"{T}/broll.py", "still", f"{D}/{src[1]}", "--len", f"{dur + 0.2:.2f}", "--out", raw]
    run(cmd)
    if overlay:
        spec = f"{P}/{name}_ov.json"; json.dump(overlay, open(spec, "w"))
        run([sys.executable, f"{T}/overlay.py", "--in", raw, "--out", f"{P}/{name}_ovl.mp4", "--spec", spec]); raw = f"{P}/{name}_ovl.mp4"
    t0 = f0 / FPS
    rel = lambda p: os.path.relpath(p).replace("\\", "/")
    vf = (f"fps={FPS},scale=1080:1920,setsar=1,setpts=PTS-STARTPTS+{t0}/TB,"
          f"subtitles='{rel(D + '/captions.ass')}':fontsdir='{rel(T + '/fonts')}',setpts=PTS-STARTPTS,format=yuv420p")
    run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-vf", vf, "-frames:v", str(n), "-an", "-c:v", "libx264", "-crf", "16", "-preset", "fast", f"{P}/{name}.mp4"])
    out.append((name, f0, f1)); print(name, n, "frames")
json.dump(out, open(f"{P}/segs.json", "w"))
