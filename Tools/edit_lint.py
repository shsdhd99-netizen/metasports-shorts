"""Edit lint (Nov 1, 2026): checks the PICTURE side of an edit by reading cuts.json (and shots.json), the way a person scrubbing the
timeline would, before anything is rendered. It looks only at editing craft, not at views.

  python Tools/edit_lint.py --folder "<Short folder>"

Found by watching the frames of our #82 next to CoachClank, swishyhoopz and Ahmed's Goal Shorts (Research Notes/Editing Study (Nov 1, 2026).md):
  1. SAME ANGLE x3 IN THE HOOK. #82's first 8 s was the live wide, the rewind and a half-speed replay of ONE shot: three clips, one
     picture, so nothing "new" arrives for 8 s. `qa_short`'s "footage shown twice" check passes because the clip ranges differ.
     Rule: in the first 8 s, never 3 shots in a row from the same source within 4 s of each other, and at most 2 from one angle.
  2. 3:4 WINDOW CLIPS THE BROADCAST BUG. A blurfit shot with blurfit_aspect < 1 crops the sides of a 16:9 frame, so an ESPN/NBA score
     bug (full-width at the bottom) is cut in half ("105 S"). If a shot's `why` says scorebug/bug/clock, use plain --blurfit
     (blurfit_aspect 0) or a window of 1.0+, or drop the claim that the bug proves.
  3. LONG STATIC CLOSE-UP. A closing shot over 2.8 s with no new picture (a held face + stat card) is dead time for the eye.
  4. HOOK SUBJECT TOO SMALL. A shot in the first 3 s using zoom 1.0-1.2 on a wide source with blurfit shows the subject at under
     15% of the frame height; use `zoom` 1.5+ or a closer angle (the winners' first frame always has the subject big).
  5. CLIP REUSE (Nov 4, 2026, Research Notes/FC Clip Repetition Study (Nov 4, 2026).md; Tools/fc_reuse.py): the same source file AND
     overlapping time range twice in one Short (excused only by `"replay": true` on the later shot), one source file on screen for
     more than 35% of the runtime, and two back-to-back shots from the same source within 3 s of each other (a near-duplicate angle).
     Evidence tier [S]: across 15 FC Shorts reuse did NOT correlate with lower % viewed, so these are advice for variety, not a gate.
     `python Tools/edit_lint.py --selftest` proves the check flags a known repeating Short and passes a clean one.
Exit code 1 if anything was flagged; it is advice, not a gate.
"""
import argparse, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fc_reuse


def reuse_flags(shots, starts=None):
    """Clip-reuse flags for one Short (rule 5). Returns a list of strings."""
    out = []
    r = fc_reuse.reuse(shots, starts)
    if r["n_unexcused"]:
        pairs = ", ".join(f"{a}~{b}" for a, b, _ in r["unexcused"][:6])
        out.append(f"CLIP REUSE: {r['n_unexcused']} repeated source range(s) ({pairs}{' ...' if r['n_unexcused'] > 6 else ''}): the same footage shows twice. "
                   "Use another source/angle, or mark the one intentional replay with \"replay\": true.")
    if r["max_src_share"] > 0.35:
        out.append(f"ONE SOURCE: {r['max_src']} is on screen {r['max_src_share']*100:.0f}% of the runtime (limit 35%). Add footage from a second source.")
    tl, _ = fc_reuse.timeline(shots, starts)
    near = [(tl[i - 1]["clip"], tl[i]["clip"]) for i in range(1, len(tl))
            if tl[i]["src"] and tl[i]["src"] == tl[i - 1]["src"] and not tl[i]["still"] and abs(tl[i]["at"] - tl[i - 1]["at"]) < 3.0 and not tl[i]["replay"]]
    if near:
        out.append(f"SAME ANGLE BACK-TO-BACK: {len(near)} pair(s) of consecutive shots from one source within 3 s of each other ({near[0][0]}, {near[0][1]}...).")
    return out


def selftest():
    bad = [{"clip": "A", "src": "X", "at": 10, "len": 2}, {"clip": "B", "src": "Y", "at": 5, "len": 2}, {"clip": "C", "src": "X", "at": 11, "len": 2}]
    good = [{"clip": "A", "src": "X", "at": 10, "len": 2}, {"clip": "B", "src": "Y", "at": 5, "len": 2}, {"clip": "C", "src": "Z", "at": 40, "len": 2},
            {"clip": "D", "src": "X", "at": 40, "len": 2}, {"clip": "E", "src": "W", "at": 1, "len": 2},
            {"clip": "F", "src": "V", "at": 1, "len": 2}]
    replay = [dict(bad[0]), dict(bad[1]), dict(bad[2], replay=True)]
    ok = bool(reuse_flags(bad)) and not reuse_flags(good) and not any("CLIP REUSE" in f for f in reuse_flags(replay))
    # a real Short known to repeat (S26, 36 unexcused overlaps) must flag
    d = [x for x in fc_reuse.folders() if " S26 " in x]
    if d:
        sh = json.load(open(os.path.join(d[0], "cuts.json"), encoding="utf-8"))["shots"]
        ok = ok and any("CLIP REUSE" in f for f in reuse_flags(sh, fc_reuse.load_starts(d[0])))
    print("edit_lint selftest:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
    if not a.folder:
        ap.error("--folder is required")
    cuts = json.load(open(os.path.join(a.folder, "cuts.json"), encoding="utf-8"))
    shots = cuts["shots"]
    flags = []
    t, timeline = 0.0, []
    for s in shots:
        ln = float(s.get("len") or 0)
        timeline.append((t, t + ln, s))
        t += ln

    # 1. same angle in the hook
    hook = [(a0, b0, s) for a0, b0, s in timeline if a0 < 8.0 and s.get("src")]
    run = 1
    for i in range(1, len(hook)):
        p, q = hook[i - 1][2], hook[i][2]
        same = p.get("src") == q.get("src") and abs(float(q.get("at", 0)) - float(p.get("at", 0))) < 4.0
        run = run + 1 if same else 1
        if run >= 3:
            flags.append(f"HOOK SAME ANGLE: {hook[i-2][2]['clip']}, {hook[i-1][2]['clip']}, {q['clip']} are one source within 4 s: "
                         "the first 8 s shows one picture three times. Use another angle, or a card/photo/other game between them.")
            break
    by_src = {}
    for a0, b0, s in hook:
        by_src.setdefault((s.get("src"), round(float(s.get("at", 0)) / 6)), []).append(s["clip"])
    for k, v in by_src.items():
        if len(v) >= 3 and not any("HOOK SAME ANGLE" in f for f in flags):
            flags.append(f"HOOK SAME ANGLE: {', '.join(v)} come from the same 6 s of one source.")

    # 2. 3:4 window vs broadcast bug
    for a0, b0, s in timeline:
        why = str(s.get("why", "")).lower()
        if s.get("blurfit") and s.get("blurfit_aspect") and float(s["blurfit_aspect"]) < 1.0 and any(k in why for k in ("scorebug", "score bug", "clock", " bug")):
            flags.append(f"BUG CLIPPED: {s['clip']} (at {a0:.1f} s) uses a {s['blurfit_aspect']} window but its note relies on the scorebug; "
                         "the window cuts the bug's sides. Re-cut it with blurfit_aspect 0 (whole frame) or stop citing the bug.")

    # 3. long static close
    if timeline:
        a0, b0, s = timeline[-1]
        if b0 - a0 > 2.8:
            flags.append(f"LONG CLOSE: last shot {s['clip']} holds {b0 - a0:.1f} s (over 2.8 s). Split it into two angles or trim it to 2.5 s "
                         "(let the last word land on the cut).")

    # 4. small subject in the first 3 s
    for a0, b0, s in timeline:
        if a0 < 3.0 and s.get("blurfit") and float(s.get("zoom", 1.0)) < 1.3 and not s.get("still") and not s.get("page")                 and not any(k in str(s.get("why", "")).lower() for k in ("close-up", "closeup", "tight", "face to face")):  # a close broadcast angle is already big (Nov 1 Full Review)
            flags.append(f"SMALL SUBJECT: {s['clip']} (hook, {a0:.1f} s) is a wide blurfit at zoom {s.get('zoom', 1.0)}; "
                         "players are tiny. Try zoom 1.5+ centred on the subject or a closer angle.")

    # 5. clip reuse (Nov 4)
    flags += reuse_flags(shots, fc_reuse.load_starts(a.folder))

    print(f"edit_lint: {os.path.basename(os.path.abspath(a.folder))}: {len(shots)} shots, {t:.1f} s")
    for f in flags:
        print("  FLAG ", f)
    if not flags:
        print("  clean")
    sys.exit(1 if flags else 0)


if __name__ == "__main__":
    main()
