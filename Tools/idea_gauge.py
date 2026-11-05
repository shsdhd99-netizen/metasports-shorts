"""Idea gauge (Nov 1, 2026): score a Short idea BEFORE any work is spent, and say GO, FIX (with the exact fix) or SKIP.

  python Tools/idea_gauge.py --title "Cooper Flagg vs LeBron: Rookie Years" --lane nba --answers "a2 b2 c1 d2 e1 f2 g2 h1 i0 j2"
  python Tools/idea_gauge.py --list                 # print the questions
  python Tools/idea_gauge.py --backtest             # score the sample in Research Notes/Idea Gauging (Nov 1, 2026).md

Answers are one letter + 0/1/2 each (2 = clearly yes, 1 = partly, 0 = no). The questions come from what separated our 15-80K Shorts
from our sub-3K ones (the channel's 132 NBA Shorts, our 12 FC Shorts, 4,885 competitor soccer Shorts); see the research note.
Weights are judgement calibrated on that sample, NOT a fitted model: treat the verdict as a filter that removes the worst ideas and
names the weakest part of a good one, not a prediction of views.
"""
import argparse, sys

Q = [  # key, text, weight, fix-if-low
    ("a", "Unknown-answer hook: the viewer does NOT already know the answer, and a specific question or contradiction is in the first line", 3,
     "Rewrite line 1 as a contradiction or a question the title raises and the clip answers; if everyone already knows it, SKIP"),
    ("b", "Lightning-rod subject: a person/club the audience already has strong opinions about (Bronny, Steph, Luka, LeBron, Wemby, Flagg)", 3,
     "Add the lightning-rod angle (who argues about this?) or pick the version of the story that features the famous name"),
    ("c", "One visible oddity: a single object/act you can SEE in frame 1 (a note in a sock, a ball that falls up), not a number or a rule", 3,
     "Find the one picture that shows the oddity and open on it; if only a number/rule exists, make it a counter on that picture"),
    ("d", "Footage exists that shows the claim (verified, sharp, 9:16-croppable)", 3,
     "SKIP until footage is found; never script first"),
    ("e", "Arguable: viewers will take a side in the comments (opinion, ranking, 'is he overrated')", 2,
     "End on a real either/or question the story sets up"),
    ("f", "Escalation: it gets stranger in the middle, and the last line reverses the opening device (irony)", 2,
     "Reorder so the strangest fact is second-to-last and the last line flips line 1"),
    ("g", "Fresh or live hook: tied to something people are talking about THIS week, or a classic told through today's name", 2,
     "Attach a current hook (a record chase, an anniversary, a player now in the news); otherwise it is evergreen: lower the expectation"),
    ("h", "No context needed: understandable in 3 seconds with no rules lesson, contract detail or backstory", 2,
     "Cut the explanation; if it needs a paragraph of rules or money, SKIP"),
    ("i", "Not a flop shape: NOT a rules/technicality, a hypothetical ('would it be called now'), a pure record number, or 'did X just...?' news", 3,
     "Convert to a show-it version (the play, the object) or SKIP"),
    ("j", "Classic-story test: if the story is old, the detail is unknown to most viewers AND there is real footage/photos AND a modern hook", 2,
     "Old + well-known + no new hook = SKIP; old + unknown detail + footage = GO"),
]
W = {k: w for k, _, w, _ in Q}
MAXS = sum(2 * w for k, _, w, _ in Q)


def score(ans):
    a = {s[0]: int(s[1]) for s in ans.split()}
    miss = [k for k in W if k not in a]
    if miss:
        sys.exit("missing answers for: " + ", ".join(miss))
    total = sum(a[k] * W[k] for k in W)
    pct = 100 * total / MAXS
    hard = []
    if a["d"] == 0:
        hard.append("no verified footage")
    if a["i"] == 0 and a["c"] == 0:
        hard.append("a flop shape with nothing visible")
    if a["a"] == 0 and a["b"] == 0:
        hard.append("no hook and no lightning rod")
    if hard:
        v = "SKIP"
    elif pct >= 68:
        v = "GO"
    elif pct >= 50:
        v = "FIX"
    else:
        v = "SKIP"
    fixes = sorted([(W[k] * (2 - a[k]), k) for k in W if a[k] < 2], reverse=True)
    return v, pct, total, hard, [(k, f) for _, k in fixes for kk, _, _, f in Q if kk == k][:3]


PAUSED_SHAPES = {"rule", "history", "news explainer", "news", "off-niche"}  # NBA test lanes (FC has none)  # Nov 5, 2026: Learned Weights + case study


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="")
    ap.add_argument("--lane", default="")
    ap.add_argument("--shape", default="", help="topic shape (family, moment, superlative, rule, history, news, goalkeeper trick, ...): paused shapes are reframed")
    ap.add_argument("--answers", default="")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--backtest", action="store_true")
    a = ap.parse_args()
    if a.list or not (a.answers or a.backtest):
        for k, t, w, _ in Q:
            print(f"{k} (x{w}): {t}")
        return
    if a.backtest:
        import re, os
        note = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Research Notes", "Idea Gauging (Nov 1, 2026).md")
        rows = [l for l in open(note, encoding="utf-8") if l.startswith("| ") and re.search(r"\| [a-j][012]( [a-j][012]){9} \|", l)]
        for l in rows:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            title, views, ans = cells[0], cells[1], cells[2]
            v, pct, *_ = score(ans)
            print(f"{v:5} {pct:3.0f}%  {views:>8}  {title[:70]}")
        return
    v, pct, total, hard, fixes = score(a.answers)
    paused = a.shape.strip().lower() in PAUSED_SHAPES
    if paused and v == "GO":
        v = "REFRAME"
    print(f"{a.title or '(idea)'} [{a.lane}]: {v}  ({pct:.0f}% of {MAXS} points)")
    if paused:
        print(f"  PAUSED SHAPE '{a.shape}' (Nov 4-5 data: median 0.5-0.6x the channel; Topic and Script Reset): reframe it as a family story, a watchable curiosity, a moment or a live star chase, or drop it. Only an explicit one-variable experiment may override.")
    for h in hard:
        print("  HARD STOP:", h)
    if v != "GO":
        for k, f in fixes:
            print(f"  FIX {k}: {f}")


if __name__ == "__main__":
    main()
