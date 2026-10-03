"""ASR-verified join search.
Cuts inside continuous speech cannot be placed reliably from forced-alignment times alone (CTC timings of short
fragments are off by up to 0.3 s). For each target join this tries the deepest dips/silences around the intended
boundaries, splices a short snippet for every (a, b) combination, transcribes it verbatim (um/uh/false starts kept)
and keeps the combination that reads exactly as intended: neighbouring words intact, no fragment left behind.
Among those, the deepest cut wins. Result -> edl/overrides_v4.json (read by build_v4.py).

usage: python join_search.py auto                      joins whose cut is not in real silence
       python join_search.py 12,40,55                  explicit join numbers (index in edl_v4.json)
       python join_search.py diff qa/asr_xxx_diff.json joins flagged by qa_asr_diff.py
"""
import os, sys, json, re, difflib, time
base = r"D:\OBS\ClaudeWork\commentary_v3"
for k, v in {"HF_HOME": r"cache\hf", "TORCH_HOME": r"cache\torch", "PIP_CACHE_DIR": r"cache\pip",
             "U2NET_HOME": r"cache\u2net", "XDG_CACHE_HOME": r"cache\xdg"}.items():
    os.environ[k] = os.path.join(base, v)
sys.path.insert(0, base + r"\tools")
import numpy as np, soundfile as sf, torch, gc
from scipy.signal import resample_poly
from splice import assemble, align_b, F, SR
from crisperwhisper import CrisperWhisperModel

HOP = 24
words = json.load(open(base + r"\asr\work\fa_LV60K.json"))
enh, _ = sf.read(base + r"\audio\enh_full_v2chain.wav", dtype="float32")
edl = json.load(open(base + r"\edl\edl_v4.json"))
joins = edl["joins"]
ovp = base + r"\edl\overrides_v4.json"
OVR = json.load(open(ovp)) if os.path.exists(ovp) else {}

# smoothed envelope (5 ms) in dBFS at 0.5 ms hop
cs = np.concatenate([[0.0], np.cumsum(enh.astype(np.float64) ** 2)])
W5 = 240
mid = np.arange(0, len(enh), HOP)
lo_i = np.clip(mid - W5 // 2, 0, len(enh)); hi_i = np.clip(mid + W5 // 2, 0, len(enh))
env = 10 * np.log10((cs[hi_i] - cs[lo_i]) / np.maximum(hi_i - lo_i, 1) + 1e-18)
E = lambda t: float(env[min(len(env) - 1, max(0, int(round(t * SR / HOP))))])

nrm = lambda s: re.sub(r"[^a-z0-9'-]", "", s.lower())
def fz(x, y): return x == y or difflib.SequenceMatcher(None, x, y).ratio() >= 0.7

removed = set()
for j in joins:
    removed.update(range(j["pi"] + 1, j["qi"]))
def kept_left(p, n): return [k for k in range(p, max(-1, p - 12), -1) if k not in removed][:n][::-1]
def kept_right(q, n): return [k for k in range(q, min(len(words), q + 12)) if k not in removed][:n]

def candidates(t0, t1, n, near):
    """distinct dips in [t0,t1]: nested 'runs below threshold', strict thresholds first; returns [(time, level_dB)]"""
    i0, i1 = int(max(0, t0) * SR / HOP), int(t1 * SR / HOP)
    seg = env[i0:i1]; out = []
    for thr in (-70, -60, -52, -46, -40, -35, -30, -25, -20):
        m = seg <= thr; k = 0
        while k < len(m):
            if m[k]:
                s0 = k
                while k < len(m) and m[k]: k += 1
                if (k - s0) * HOP / SR >= 0.004:
                    c = (i0 + (s0 + k) // 2) * HOP / SR
                    if all(abs(c - o[0]) > 0.03 for o in out):
                        out.append((c, thr, (i0 + s0) * HOP / SR, (i0 + k) * HOP / SR))
            else: k += 1
    out.sort(key=lambda o: (o[1], abs(o[0] - near)))
    return out[:n]

def to16(x48): return resample_poly(x48, 1, 3).astype(np.float32)

model = None
def asr(x48):
    global model
    if model is None:
        model = CrisperWhisperModel("large", backend="transformers", compute_type="float16", device="cuda")
    r = model.transcribe(to16(x48), sr=16000, language="en", mode="verbatim", word_timestamps=False)
    return r.text

def snippet(k, a, b, W=1.4):
    """+-W s of context around join k with candidate (a, b); neighbouring cuts inside the window are applied too
    (their override if there is one, else the default), so the expected words stay contiguous across clusters of cuts."""
    js = []
    for m in range(max(0, k - 4), min(len(joins), k + 5)):
        if m == k: js.append((a, b)); continue
        o = OVR.get(f"{joins[m]['pi']}-{joins[m]['qi']}", {})
        if o.get("skip"): continue
        js.append((o.get("a", joins[m]["a"]), o.get("b", joins[m]["b"])))
    start, end = a - W, b + W
    for x, y_ in js:                                  # a cut straddling a window edge: move the edge out of the removed span
        if x <= start < y_: start = y_
        if x < end <= y_: end = x
    sel = [(x, y_) for x, y_ in js if x > start and y_ < end]
    pts = [start] + [t for xy in sel for t in xy] + [end]
    segs = [(pts[2 * i], pts[2 * i + 1]) for i in range(len(sel) + 1)]
    y, _ = assemble(enh, segs, sel, fade_in=0.01, fade_out=0.03)
    return y, start, end

FRAG = lambda t: t.endswith("-") or bool(re.fullmatch(r"\[.*\]", t)) or t in ("um", "uh", "umm", "uhh", "er", "erm", "hmm")

STOP = {"bro", "bruh", "like", "um", "uh", "yeah", "literally", "just"}     # interjections the ASR drops or rewrites at random
def rate(text, eL, eR):
    """Works on content words only (interjections in STOP are dropped from the transcript and from the expectation).
       2 = the words right of the cut were heard directly after the word left of it, nothing fragment-like between (join verified);
       1 = right-hand words heard cleanly, no fragment in the few tokens before them, left side not verifiable (the ASR often drops a short
           snippet's first sentence, so that is not evidence of a problem);
       0 = a fragment/filler heard at the join, or the right-hand words are damaged / missing."""
    raw = [t for t in (nrm(x) for x in text.split()) if t]
    pos = [i for i, t in enumerate(raw) if t not in STOP]
    cont = [raw[i] for i in pos]
    L = [t for t in eL if t not in STOP][-2:] or eL[-1:]
    R = [t for t in eR if t not in STOP][:2] or eR[:1]
    def find(seq):
        for i in range(len(cont) - len(seq) + 1):
            if all(fz(cont[i + j], seq[j]) for j in range(len(seq))): return i
        return None
    # anchors: try the two nearest content words first, then just the nearest one (a short snippet often lacks the outer word)
    iL = find(L) if L else None
    if iL is None and len(L) > 1:
        L = L[-1:]; iL = find(L)
    iR = find(R) if R else None
    if iR is None and len(R) > 1:
        R = R[:1]; iR = find(R)
    if iL is not None and iR is not None and iL + len(L) <= iR:
        if iL + len(L) != iR: return 0                # extra content words between the anchors: something is left over
        between = raw[pos[iL + len(L) - 1] + 1: pos[iR]]
        return 0 if any(FRAG(t) for t in between) else 2
    if iR is not None:                                # only the right-hand words could be located
        return 0 if any(FRAG(t) for t in raw[max(1, pos[iR] - 3):pos[iR]]) else 1
    if iL is not None:                                # only the left-hand words could be located
        e = pos[iL + len(L) - 1] + 1
        return 0 if any(FRAG(t) for t in raw[e:e + 3]) else 1
    return 0

def pick(results):
    ok = [r for r in results if r["level"] >= 1]
    return min(ok, key=lambda r: r["cost"] - (12 if r["level"] == 2 else 0)) if ok else None

def cost_of(j, ta, tb):
    """lower = better: deep silence at both cut points, and the pause left at the join close to a natural breath
    (<= 0.40 s after a sentence end, <= 0.20 s mid-sentence; over-long pauses are penalised hard, too-short ones after a full stop mildly)"""
    pw, qw = words[j["pi"]], words[j["qi"]]
    pause = max(0.0, ta - pw["fa_end"]) + max(0.0, qw["fa_start"] - tb)
    sent = bool(re.search(r"[.?!]$", j["prev"]))
    allowed = 0.40 if sent else 0.20
    c = max(E(ta), -80) + max(E(tb), -80) + 70 * max(0.0, pause - allowed)
    if sent: c += 40 * max(0.0, 0.15 - pause)
    return c

def decide(k, res, eL, eR, log):
    """choose among scored combinations, record override"""
    j = joins[k]; p, q = j["pi"], j["qi"]; key = f"{p}-{q}"
    best = pick(res)
    cur = next((r for r in res if r["la"] == "cur" and r["lb"] == "cur"), None)
    print(f"\n#{k} a={j['a']:.3f} b={j['b']:.3f} [{j['label'][:40]}]  expect {' '.join(eL)!r} | {' '.join(eR)!r}")
    for r in sorted(res, key=lambda r: (-r["level"], r["cost"]))[:4]:
        mark = "  <== chosen" if r is best else ""
        print(f"   lvl{r['level']} cost {r['cost']:6.1f} a={r['a']:.3f}({r['la']},{r['Ea']:.0f}dB) b={r['b']:.3f}({r['lb']},{r['Eb']:.0f}dB) -> {r['text'][:80]!r}{mark}")
    OVR.pop(key, None)
    if best is not None:
        if not (cur is not None and best is cur):
            OVR[key] = {"a": best["a"], "b": best["b"], "level": best["level"]}
    else:
        print(f"   !! no combination read cleanly for #{k}")
        if q - p - 1 <= 3:
            OVR[key] = {"skip": True}
            print("   -> small removal: marked skip (keep the original speech)")
    log[key] = dict(join=j, eL=eL, eR=eR, results=res, chosen=best)

def main():
    mode = sys.argv[1]
    if mode == "rescore":
        old = json.load(open(base + r"\qa\join_search_log.json")); log = {}
        OVR.clear()
        for k, v in old.items():
            eL, eR = v.get("eL"), v.get("eR")
            if eL is None:
                ex = v["expect"]; eL, eR = ex[:len(ex) // 2], ex[len(ex) // 2:]
            for r in v["results"]:
                r["level"] = rate(r["text"], eL, eR); r["cost"] = cost_of(joins[int(k)], r["a"], r["b"])
            decide(int(k), v["results"], eL, eR, log)
        json.dump(OVR, open(ovp, "w"), indent=1)
        json.dump(log, open(base + r"\qa\join_search_log_rescored.json", "w"), indent=1, default=float)
        print("\nwrote", ovp, "with", len(OVR), "overrides"); return
    if mode == "auto":
        T = [k for k, j in enumerate(joins) if not j["label"].startswith("(pause") and max(E(j["a"]), E(j["b"])) > -45]
    elif mode == "diff":
        d = json.load(open(sys.argv[2])); T = sorted(int(k) for k in d["near_cut"])
    elif mode.startswith("keys:"):                    # keys:p-q,p-q  (word indices around the cut; stable across rebuilds)
        want = set(mode[5:].split(","))
        T = [k for k, j in enumerate(joins) if f"{j['pi']}-{j['qi']}" in want]
    else:
        T = [int(x) for x in mode.split(",")]
    print("targets:", T, flush=True)
    lp = os.path.join(base, "qa", "join_search_log_keyed.json"); log = json.load(open(lp)) if os.path.exists(lp) else {}
    for k in T:
        j = joins[k]; p, q = j["pi"], j["qi"]
        pw, qw = words[p], words[q]
        first, last = words[p + 1], words[q - 1]
        A = candidates(pw["fa_end"] - 0.10, min(first["fa_start"] + 0.14, pw["fa_end"] + 0.60), 2, pw["fa_end"] + 0.03)
        B = candidates(max(last["fa_end"] - 0.14, qw["fa_start"] - 0.60), qw["fa_start"] + 0.10, 2, qw["fa_start"] - 0.03)
        ca = [(j["a"], "cur")] + [(c[0] if c[1] > -40 else max(c[2] + 0.012, min(c[0], c[3] - 0.012)), f"{c[1]}") for c in A]
        cb = [(j["b"], "cur")] + [(c[0] if c[1] > -40 else max(c[2] + 0.012, min(c[0], c[3] - 0.012)), f"{c[1]}") for c in B]
        L = [words[i] for i in kept_left(p, 5)]; Rr = [words[i] for i in kept_right(q, 5)]
        eL = [nrm(w["word"]) for w in L]; eR = [nrm(w["word"]) for w in Rr]
        res = []
        for ta, la in ca:
            for tb, lb in cb:
                if tb - ta < 0.03: continue
                bb = tb
                if max(E(ta), E(tb)) > -45:
                    bb, c = align_b(enh, ta, tb)
                y, s, e = snippet(k, ta, bb)
                txt = asr(y)
                lv = rate(txt, eL, eR)
                res.append(dict(a=ta, b=bb, la=la, lb=lb, level=lv, cost=cost_of(j, ta, bb), text=txt, Ea=E(ta), Eb=E(bb)))
        decide(k, res, eL, eR, log); gc.collect(); torch.cuda.empty_cache()
        json.dump(OVR, open(ovp, "w"), indent=1)
        json.dump(log, open(lp, "w"), indent=1, default=float)
    print("\nwrote", ovp, "with", len(OVR), "overrides")

if __name__ == "__main__":
    main()
