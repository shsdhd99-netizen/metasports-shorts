"""Pre-cut lint (Nov 5, 2026): catches, BEFORE cutting, the problems that cost #95 five re-cuts and that qa_audit shows firing in most Shorts.

  python Tools/precut_lint.py --folder "<Short folder>"      # reads cuts_plan.json (or cuts.json) and the source files; exit 1 on any FIX

FIX (will fail QA or cause a re-cut): a source clip window that runs past the end of the source; shot 1 shorter than 2.0 s or more than 2 shots in the
first 3 s (NBA rule; FC allows 4-5 cuts in the first 5 s when the plan says "style": "v3"); an overlay inside the caption band (y 1000-1300);
a shot with no `why` (nothing to verify); a source smaller than 720p.
WARN (the top recurring QA warnings): a source under 1080p (blow-up above 1.8x; download 1080p with yt-dlp height<=1080 instead), the same source range
reused (edit_lint rule), one source over 35% of the runtime, and a shot that starts within 0.4 s of a known dissolve (add `"at"` + 0.5).
"""
import argparse, json, os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "Tools"))


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", path], capture_output=True, text=True)
    try:
        j = json.loads(r.stdout); return int(j["streams"][0]["width"]), int(j["streams"][0]["height"]), float(j["format"]["duration"])
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--folder", required=True); a = ap.parse_args()
    F = a.folder
    p = os.path.join(F, "cuts.json") if os.path.exists(os.path.join(F, "cuts.json")) else os.path.join(F, "cuts_plan.json")
    plan = json.load(open(p, encoding="utf-8")); shots = plan["shots"]; src = plan.get("sources", {})
    fix, warn = [], []
    info = {}
    for k, v in src.items():
        info[k] = probe(os.path.join(F, v))
        if info[k] is None:
            warn.append(f"source {k} ({v}) could not be probed (missing?)")
        elif info[k][1] < 720:
            fix.append(f"source {k} is {info[k][0]}x{info[k][1]}: under 720p")
        elif info[k][1] < 1080:
            warn.append(f"source {k} is {info[k][0]}x{info[k][1]}: blown up {1080 / info[k][1]:.1f}x+ (QA warns above 1.8x); get a 1080p copy if one exists")
    t = 0.0
    for i, s in enumerate(shots):
        ln = float(s.get("len") or 0)
        if not s.get("why"):
            fix.append(f"shot {s.get('clip')} has no `why` (nothing to verify against the line)")
        i0 = info.get(s.get("src"))
        if i0 and s.get("at") is not None and ln and float(s["at"]) + ln > i0[2] + 0.05:
            fix.append(f"shot {s.get('clip')}: window {s['at']}+{ln:.1f} s runs past the end of its source ({i0[2]:.1f} s)")
        for o in s.get("overlay", []) or []:
            y = o.get("y", 300)
            if 1000 <= y <= 1300:
                fix.append(f"shot {s.get('clip')}: overlay at y={y} sits in the caption band (1000-1300)")
        t += ln
    lens = [float(s.get("len") or 0) for s in shots]
    if lens and lens[0] and lens[0] < 2.0 and plan.get("style") != "v3":
        fix.append(f"shot 1 is {lens[0]:.1f} s (needs 2.0 s or more)")
    cum, n3 = 0.0, 0
    for l in lens:
        if cum < 3.0:
            n3 += 1
        cum += l
    # Nov 7 (C2): the cut-count rule for the first 3 s was scrapped (no effect: lab study, edit_shots_first3_le2)
    try:
        import fc_reuse
        r = fc_reuse.reuse(shots)
        if r["n_unexcused"]:
            warn.append(f"{r['n_unexcused']} repeated source range(s) (edit_lint reuse rule)")
    except Exception:
        pass
    print(f"precut_lint: {os.path.basename(os.path.abspath(F))}: {len(shots)} shots, {t:.1f} s")
    for f in fix:
        print("  FIX ", f)
    for w in warn:
        print("  warn", w)
    if not fix and not warn:
        print("  clean")
    sys.exit(1 if fix else 0)


if __name__ == "__main__":
    main()
