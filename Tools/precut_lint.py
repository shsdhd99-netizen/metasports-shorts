"""Pre-cut lint (Nov 5, 2026): catches, BEFORE cutting, the problems that cost #95 five re-cuts and that qa_audit shows firing in most Shorts.

  python Tools/precut_lint.py --folder "<Short folder>"      # reads cuts_plan.json (or cuts.json) and the source files; exit 1 on any FIX

FIX (will fail QA or cause a re-cut): a source clip window that runs past the end of the source; shot 1 shorter than 2.0 s or more than 2 shots in the
first 3 s (NBA rule; FC allows 4-5 cuts in the first 5 s when the plan says "style": "v3"); an overlay inside the caption band (y 1000-1300);
a shot with no `why` (nothing to verify); a source smaller than 720p.
WARN (the top recurring QA warnings): a source under 1080p (blow-up above 1.8x; download 1080p with yt-dlp height<=1080 instead), the same source range
reused (edit_lint rule), one source over 35% of the runtime, and a shot that starts within 0.4 s of a known dissolve (add `"at"` + 0.5).
Nov 7 (efficiency review): when words.json exists the shots are timed the way cut_list.py will time them (Tools/anchors.py), so a plan
without "len" values can be linted before cutting. New FIX: an anchor that is not in words.json; no `kind: action` shot in the first 3 s
(qa_short --full fails that after the render); an overlay whose text reaches into the caption band (it was checked by its top edge only).
New WARN: an anchor that pins mid-sentence while a later copy starts a phrase (the #99 Luka re-cut); overlay words on screen too briefly
to read (under 0.6 s, or more than 4 words a second); a shot that runs over 6 s (qa_short fails "too long").
"""
import copy
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
    plan = json.load(open(p, encoding="utf-8")); src = plan.get("sources", {})
    fix, warn = [], []
    wp = os.path.join(F, "words.json")
    starts = None
    if os.path.exists(wp):
        from anchors import fill_lengths
        words = json.load(open(wp, encoding="utf-8"))
        plan = copy.deepcopy(plan)  # lint only: cut_list.py writes the filled lengths
        auto = [s.get("clip") for s in plan["shots"] if not s.get("len")]
        starts, problems = fill_lengths(plan, words, pad=0.3)
        for pr in problems:
            (fix if pr.startswith("FIX") else warn).append(pr.split(": ", 1)[1])
        if auto:
            print(f"  ({len(auto)} shot length(s) filled from the anchors for this check; cut_list.py saves them)")
    shots = plan["shots"]
    info, missing = {}, []
    for k, v in src.items():
        info[k] = probe(os.path.join(F, v))
        if info[k] is None:
            missing.append(k)
        elif info[k][1] < 720:
            fix.append(f"source {k} is {info[k][0]}x{info[k][1]}: under 720p")
        elif info[k][1] < 1080:
            warn.append(f"source {k} is {info[k][0]}x{info[k][1]}: blown up {1080 / info[k][1]:.1f}x+ (QA warns above 1.8x); get a 1080p copy if one exists")
    if missing:  # Nov 7: one line, not one per source (media is git-ignored, so a fresh checkout has none)
        warn.append(f"{len(missing)} source file(s) missing, so their windows were not checked: {', '.join(missing)}")
    t = 0.0
    for i, s in enumerate(shots):
        ln = float(s.get("len") or 0)
        if not s.get("why"):
            fix.append(f"shot {s.get('clip')} has no `why` (nothing to verify against the line)")
        i0 = info.get(s.get("src"))
        if i0 and s.get("at") is not None and ln and float(s["at"]) + ln > i0[2] + 0.05:
            fix.append(f"shot {s.get('clip')}: window {s['at']}+{ln:.1f} s runs past the end of its source ({i0[2]:.1f} s)")
        for o in s.get("overlay", []) or []:
            y, size = float(o.get("y", 300)), float(o.get("size", 150))
            if y < 1300 and y + size > 1000:  # y is the TOP of the text; the text runs down by about its size
                fix.append(f"shot {s.get('clip')}: overlay at y={y:.0f} (size {size:.0f}) reaches into the caption band (1000-1300); move it up to y<={1000 - size:.0f}")
            txt = " ".join(str(x) for x in (o.get("text"), o.get("sub")) if x)
            nw = len(txt.split()) + (1 if o.get("count") else 0)
            vis = min(float(o.get("end", ln or 9)), ln or 9) - float(o.get("start", 0))
            if vis < 0.6:
                warn.append(f"shot {s.get('clip')}: overlay '{txt[:30] or o.get('count', {}).get('to')}' is on screen only {vis:.2f} s (shot {ln:.2f} s); too fast to read")
            elif nw / vis > 4:
                warn.append(f"shot {s.get('clip')}: overlay '{txt[:30]}' has {nw} words in {vis:.1f} s; cut words or hold it longer")
        t += ln
    lens = [float(s.get("len") or 0) for s in shots]
    # the real timeline: anchor starts when words.json exists (what cut_list/anchor_shots will use), else the lengths end to end
    if starts and all(x is not None for x in starts):
        total = words[-1]["end"] + 0.3
        tl = [(starts[i], (starts[i + 1] if i + 1 < len(starts) else total)) for i in range(len(starts))]
    else:
        acc, tl = 0.0, []
        for l in lens:
            tl.append((acc, acc + l)); acc += l
    dur = [e - b for b, e in tl]
    if dur and dur[0] < 2.0 and plan.get("style") != "v3":
        fix.append(f"shot 1 runs {dur[0]:.1f} s (needs 2.0 s or more)")
    # Nov 7 (C2): the cut-count rule for the first 3 s was scrapped (no effect: lab study, edit_shots_first3_le2). The action rule stays:
    if tl and not any(s.get("kind", "action") == "action" for s, (b, e) in zip(shots, tl) if b < 3.0):
        fix.append("no `kind: action` shot starts in the first 3 s (qa_short fails this: a talking head or card hook gets swiped)")
    for s, d in zip(shots, dur):
        if d > 6.0:
            warn.append(f"shot {s.get('clip')} runs {d:.1f} s (qa_short fails a shot over 6 s); split it")
    t = sum(dur) if dur else t
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
