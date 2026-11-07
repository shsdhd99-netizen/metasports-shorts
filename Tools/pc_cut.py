"""Cut every YouTube moment a cloud session found, in one go (run this on the PC, where YouTube downloads work).

  python pc_cut.py --folder "..\\Productions\\MetaSports\\<Short folder>"

Reads <folder>\\clips_manifest.json:  [{"file": "V01_jordan.mp4", "video": "dmFg6vJkSl8", "at": 123.4, "len": 2.5, "x": 0.5}, ...]
and makes clips\\<file> with broll.py cut (1080x1920, no audio). Skips files that already exist. Then run assemble.py.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument("--folder", required=True); a = ap.parse_args()
man = json.load(open(os.path.join(a.folder, "clips_manifest.json"), encoding="utf-8-sig"))
os.makedirs(os.path.join(a.folder, "clips"), exist_ok=True)
for m in man:
    out = os.path.join(a.folder, "clips", m["file"])
    if os.path.exists(out):
        continue
    cmd = [sys.executable, os.path.join(HERE, "broll.py"), "cut", m["video"], "--at", str(m["at"]), "--len", str(m.get("len", 3)),
           "--x", str(m.get("x", 0.5)), "--out", out, "--snap"]
    if m.get("zoom"):
        cmd += ["--zoom", str(m["zoom"])]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(("ok   " if os.path.exists(out) else "FAIL ") + m["file"], (r.stdout or r.stderr).strip()[-80:])
