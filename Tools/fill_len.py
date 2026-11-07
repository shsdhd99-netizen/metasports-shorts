"""Cut plan -> cut list: fill every shot's "len" from its anchor to the next anchor, plus a pad (Oct 24 2026; Nov 7: shared Tools/anchors.py).

  python Tools/fill_len.py "<Short folder>" [pad, default 0.3]

Reads <folder>/cuts_plan.json (or cuts.json when there is no plan), finds each anchor in words.json with Tools/anchors.py (the same
matching cut_list.py and precut_lint.py use), sets len = time to the next shot + pad (a shot that already has "len" keeps it), writes
cuts.json and prints a table: clip, start, duration, the words said over it (LONG over 3.5 s, short under 0.6 s).
Anchor problems print first: FIX (not found: exit 1, nothing written) and WARN (an anchor that appears more than once).
Nov 7: cut_list.py now does this by itself when a shot has no "len", so this is only needed to look at the table first.
A slowed clip (cuts.json "speed") needs len of footage at that speed; check the source has len x speed seconds before the next cut.
"""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anchors import fill_lengths, table

F = sys.argv[1]
pad = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
pp = os.path.join(F, "cuts_plan.json")
plan = json.load(open(pp if os.path.exists(pp) else os.path.join(F, "cuts.json"), encoding="utf-8"))
words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8"))
starts, problems = fill_lengths(plan, words, pad=pad)
for p in problems:
    print(" ", p)
if any(p.startswith("FIX") for p in problems):
    raise SystemExit("fill_len: fix the anchors above first (nothing written)")
for line in table(plan["shots"], starts, words):
    print(line)
json.dump(plan, open(os.path.join(F, "cuts.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
total = words[-1]["end"] + 0.3
print(len(plan["shots"]), "shots;", round(len(plan["shots"]) / total * 60, 1), "per minute")
