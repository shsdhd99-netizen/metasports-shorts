"""One cut list per Short, for the story format (40-50 pictures a minute): cuts every clip and writes shots.json.

  python Tools/cut_list.py --folder "<Short folder>"            # cuts what is missing, writes shots.json, runs anchor_shots
  python Tools/cut_list.py --folder "<Short folder>" --force    # re-cut every clip
  python Tools/cut_list.py --folder "<Short folder>" --verified # after you LOOKED at _check/sheet.jpg and the source sheets:
                                                                 # marks every clip verified in sources.csv (qa_short needs it)
Also fills sources.csv (what each clip shows, the line it is used for) and draws _check/sheet.jpg: one frame from the middle
of every shot, numbered, to check framing and that the named person is on screen.

<folder>/cuts.json:
  {"sources": {"C": "src/clean.mp4", ...},                 # short names for source files (relative to the folder)
   "shots": [
     {"clip": "A01", "src": "C", "at": 255.3, "len": 2.2, "x": 0.45, "kind": "face", "why": "...", "anchor": "Goalkeepers"},
     {"clip": "A06", "src": "C", "at": 32.0, "len": 2.6, "blurfit": true, ...},          # wide shot over a blurred fill
     {"clip": "A10", "still": "assets/kopke_9x16.jpg", "len": 1.9, ...},                 # photo, slow push-in
     {"clip": "A13", "page": "assets/note_a.png", "len": 1.9, "width": 0.86, "y": 0.4, "box": "x,y,w,h", ...},
     {"clip": "A16", "stock": 47015, "at": 1.0, "len": 1.6, ...}]}                       # Mixkit id: downloaded to src/ first
Any broll.py cut option works as a key: x, y, zoom, blurfit, blurfit_width, delogo, flip. "shot_zoom" becomes the shot's push-in
in shots.json. Every clip lands in clips/<clip>.mp4 and every cut is logged to sources.csv by broll.py.
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"failed: {' '.join(cmd)}\n{r.stdout}\n{r.stderr}")
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--verified", action="store_true", help="mark every clip verified in sources.csv (only after looking at the sheet)")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    plan = json.load(open(os.path.join(F, "cuts.json"), encoding="utf-8"))
    srcs = {k: os.path.join(F, v) for k, v in plan.get("sources", {}).items()}
    os.makedirs(os.path.join(F, "clips"), exist_ok=True)
    py = sys.executable
    shots = []
    for s in plan["shots"]:
        out = os.path.join(F, "clips", s["clip"] + ".mp4")
        if a.force or not os.path.exists(out):
            if "stock" in s:
                sp = os.path.join(F, "src", f"stock_{s['stock']}.mp4")
                if not os.path.exists(sp):
                    run([py, os.path.join(HERE, "stock.py"), "get", str(s["stock"]), "--out", sp, "--note", s.get("why", "")])
                srcs[f"stock_{s['stock']}"] = sp
                s = dict(s, src=f"stock_{s['stock']}", at=s.get("at", 0.5))
            if "still" in s:
                msg = run([py, os.path.join(HERE, "broll.py"), "still", os.path.join(F, s["still"]), "--len", str(s["len"]), "--out", out])
            elif "page" in s:
                cmd = [py, os.path.join(HERE, "broll.py"), "page", os.path.join(F, s["page"]), "--len", str(s["len"]), "--out", out]
                for k in ("width", "y", "zoom", "focus", "dim", "mark_at", "margin"):
                    if k in s:
                        cmd += [f"--{k.replace('_', '-')}", str(s[k])]
                if s.get("bg"):
                    cmd += ["--bg", os.path.join(F, s["bg"])]
                for b in ([s["box"]] if isinstance(s.get("box"), str) else s.get("box", [])):
                    cmd += ["--box", b]
                if s.get("circle"):
                    cmd.append("--circle")
                msg = run(cmd)
            else:
                cmd = [py, os.path.join(HERE, "broll.py"), "cut", srcs[s["src"]], "--at", str(s["at"]), "--len", str(s["len"]), "--out", out]
                for k in ("x", "y", "zoom", "delogo", "blurfit_width"):
                    if k in s:
                        cmd += [f"--{k.replace('_', '-')}", str(s[k])]
                for k in ("blurfit", "flip"):
                    if s.get(k):
                        cmd.append(f"--{k}")
                msg = run(cmd)
            print(f"  {s['clip']}: {msg}")
        shot = {"clip": s["clip"] + ".mp4", "kind": s.get("kind", "action"), "why": s.get("why", "")}
        for k in ("anchor", "lead"):
            if k in s:
                shot[k] = s[k]
        if "shot_zoom" in s:
            shot["zoom"] = s["shot_zoom"]
        shot["start"] = 0.0
        shots.append(shot)
    json.dump(shots, open(os.path.join(F, "shots.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    subprocess.run([py, os.path.join(HERE, "anchor_shots.py"), "--folder", F])
    # every clip must be at least as long as its shot (qa_short fails replays/freezes)
    shots = json.load(open(os.path.join(F, "shots.json"), encoding="utf-8"))
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8"))
    total = words[-1]["end"] + 0.3
    lens = {s["clip"] + ".mp4": s["len"] for s in plan["shots"]}
    for i, s in enumerate(shots):
        need = (shots[i + 1]["start"] if i + 1 < len(shots) else total) - s["start"]
        if lens[s["clip"]] < need - 0.02:
            print(f"  SHORT CLIP: {s['clip']} is {lens[s['clip']]:.2f}s but the shot runs {need:.2f}s")
    log_sources(F, plan, shots, words, total, a.verified)
    sheet(F, shots, total)


def log_sources(F, plan, shots, words, total, verified):
    import csv, datetime
    p = os.path.join(F, "sources.csv")
    cols = ["clip", "kind", "used_at_s", "used_for_line", "what_it_shows", "source_url", "source_account", "source_date", "source_in_s",
            "source_out_s", "crop", "match_score", "licence_risk", "verified", "verified_on", "notes"]
    rows = {r["clip"]: r for r in csv.DictReader(open(p, encoding="utf-8"))} if os.path.exists(p) else {}
    info = {s["clip"] + ".mp4": s for s in plan["shots"]}
    for i, sh in enumerate(shots):
        c, s = sh["clip"], info[sh["clip"]]
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        r = rows.setdefault(c, {"clip": c})
        if "still" in s or "page" in s:
            r.setdefault("source_url", s.get("still") or s.get("page"))
            r.setdefault("crop", "still, slow push-in")
        r.update(kind=sh.get("kind", ""), used_at_s=f"{sh['start']:.2f}", what_it_shows=s.get("why", ""),
                 used_for_line=" ".join(w["word"] for w in words if sh["start"] - 0.02 <= w["start"] < end - 0.02))
        if verified:
            r.update(verified="yes", verified_on=datetime.date.today().isoformat())
    w = csv.DictWriter(open(p, "w", encoding="utf-8", newline=""), fieldnames=cols)
    w.writeheader()
    w.writerows({k: r.get(k, "") for k in cols} for r in rows.values() if r["clip"] in info)


def sheet(F, shots, total):
    os.makedirs(os.path.join(F, "_check"), exist_ok=True)
    tiles = []
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        t = os.path.join(F, "_check", f"t{i:02d}.jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{(end - s['start']) / 2:.2f}", "-i", os.path.join(F, "clips", s["clip"]),
                        "-frames:v", "1", "-vf", f"scale=216:384,drawtext=text='{i} {s['clip'][:-4]}':x=4:y=4:fontsize=22:fontcolor=yellow:box=1:boxcolor=black", t])
        tiles.append(t)
    ins = sum((["-i", t] for t in tiles), [])
    lay = "|".join(f"{(k % 12) * 216}_{(k // 12) * 384}" for k in range(len(tiles)))
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", "".join(f"[{k}]" for k in range(len(tiles))) +
                    f"xstack=inputs={len(tiles)}:layout={lay}:fill=black", os.path.join(F, "_check", "sheet.jpg")])
    print(f"  contact sheet: {os.path.join(F, '_check', 'sheet.jpg')}")


if __name__ == "__main__":
    main()
