"""Compare a verbatim re-transcription of the edited voice with the words that SHOULD be there.
Reports (a) every filler / false-start token that survived, (b) every mismatch within +-1.5 s of a cut,
(c) overall word error rate.   usage: python qa_asr_diff.py asr.json [edl.json final_words.json]"""
import json, re, sys, difflib
W = r"D:\OBS\ClaudeWork\commentary_v3"
asr = json.load(open(sys.argv[1]))
edl = json.load(open(sys.argv[2] if len(sys.argv) > 2 else W + r"\edl\edl_v4.json"))
fw = json.load(open(sys.argv[3] if len(sys.argv) > 3 else W + r"\edl\final_words_v4.json"))

def norm(w):
    w = w.lower().strip()
    if re.fullmatch(r"\[[a-z ]+\]", w): return w           # [um] / [uh]
    return re.sub(r"[^a-z0-9'-]", "", w)
FILL = lambda t: bool(re.fullmatch(r"\[[a-z ]+\]", t)) or (t.endswith("-") and len(t) <= 4) or t in ("um", "uh", "umm", "uhh", "uh-huh")

exp = [(norm(x["word"]), x["start"]) for x in fw if norm(x["word"])]
got = [(norm(x["word"]), x["start"]) for x in asr["words"] if norm(x["word"])]
# expected side must not contain fillers (they were cut); drop any that slipped through (none expected)
sm = difflib.SequenceMatcher(a=[t for t, _ in exp], b=[t for t, _ in got], autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != "equal"]

F = 0.005
segm = edl["seg_map"]
join_out = [segm[k + 1][2] - F for k in range(len(segm) - 1)]     # output time of each crossfade centre
def near_join(t):
    ds = [abs(t - j) for j in join_out]; k = min(range(len(ds)), key=ds.__getitem__)
    return k, ds[k]

print(f"expected {len(exp)} words, transcribed {len(got)}; word-level mismatches: {sum(max(i2-i1, j2-j1) for _, i1, i2, j1, j2 in ops)}")
fr = [(t, s) for t, s in got if FILL(t)]
print(f"\nfiller / false-start tokens in the edited audio: {len(fr)}")
for t, s in fr:
    k, d = near_join(s)
    print(f"  {s:8.2f}s  {t!r}   (nearest cut #{k} is {d:.2f}s away)")
print("\nmismatches near cuts (<=1.5 s) -- these need a look:")
bad = {}
for tag, i1, i2, j1, j2 in ops:
    e = [t for t, _ in exp[i1:i2]]; g = [t for t, _ in got[j1:j2]]
    tt = got[j1][1] if j1 < len(got) else exp[i1][1]
    if j1 >= len(got) or (i1 < len(exp) and j1 < len(got) and False): tt = exp[min(i1, len(exp)-1)][1]
    tt = exp[i1][1] if i1 < len(exp) and tag == "delete" else tt
    k, d = near_join(tt)
    if d <= 1.5:
        bad.setdefault(k, []).append((tag, e, g, tt))
for k, lst in sorted(bad.items()):
    for tag, e, g, tt in lst:
        print(f"  cut #{k:2d} @out {tt:7.2f}s  {tag:8s} expected={' '.join(e)!r}  heard={' '.join(g)!r}")
print(f"\n{len(bad)} cuts with nearby mismatches; all other cuts transcribed exactly as expected.")
json.dump({"filler": fr, "near_cut": {str(k): v for k, v in bad.items()}}, open(sys.argv[1].replace(".json", "_diff.json"), "w"), indent=0)
