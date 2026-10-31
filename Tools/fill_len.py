"""Cut plan -> cut list: fill every shot's "len" from its anchor to the next anchor, plus a pad (Oct 24 2026; was a scratch helper).

  python Tools/fill_len.py "<Short folder>" [pad, default 0.3]

Reads <folder>/cuts_plan.json (cuts.json's format, shots without "len"), finds each anchor in words.json the same way
anchor_shots.py does, sets len = time to the next shot + pad (a shot that already has "len" keeps it), writes cuts.json and
prints a table: clip, start, duration, the words said over it (LONG over 3.5 s, short under 0.6 s). Then run cut_list.py.
A slowed clip (cuts.json "speed") needs len of footage at that speed; check the source has len x speed seconds before the next cut.
"""
import json, re, sys, os
F = sys.argv[1]; pad = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
plan = json.load(open(os.path.join(F, "cuts_plan.json")))
words = json.load(open(os.path.join(F, "words.json")))
norm = lambda w: re.sub(r"[^a-z0-9$%']", "", w.lower())
toks, own = [], []
for i, w in enumerate(words):
    for t in w["word"].split():
        if norm(t): toks.append(norm(t)); own.append(i)
pos, starts = 0, []
for i, s in enumerate(plan["shots"]):
    ph = s.get("anchor")
    if not ph:
        starts.append(0.0 if i == 0 else None); continue
    a = [norm(t) for t in ph.split() if norm(t)]
    for k in range(pos, len(toks) - len(a) + 1):
        if toks[k:k + len(a)] == a:
            starts.append(words[own[k]]["start"] - s.get("lead", 0.03)); pos = k + len(a); break
    else:
        raise SystemExit(f"anchor not found after token {pos}: {ph}")
total = words[-1]["end"] + 0.3
for i, s in enumerate(plan["shots"]):
    end = starts[i + 1] if i + 1 < len(starts) else total
    d = end - max(0, starts[i])
    s.setdefault("len", round(d + pad, 2))
    said = " ".join(w["word"] for w in words if starts[i] - 0.02 <= w["start"] < end - 0.02)
    flag = "  <-- LONG" if d > 3.5 else ("  <-- short" if d < 0.6 else "")
    print(f"{s['clip']:5} {max(0,starts[i]):6.2f} {d:5.2f}  {said[:80]}{flag}")
json.dump(plan, open(os.path.join(F, "cuts.json"), "w"), indent=1, ensure_ascii=False)
print(len(plan["shots"]), "shots;", round(len(plan["shots"]) / total * 60, 1), "per minute")
