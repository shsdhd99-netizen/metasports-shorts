"""v4 voice edit: no cold open, story runs from the first word; every um/uh, stutter, false start, restart and
stumble removed with cuts placed at real dips between words (crossfaded). Works on the v2-chain enhanced audio.
"""
import json, re, sys, os, numpy as np, soundfile as sf
sys.path.insert(0, "D:/OBS/ClaudeWork/commentary_v3/tools")
from splice import assemble, align_b, F as FX

W = r"D:\OBS\ClaudeWork\commentary_v3"
SR = 48000
words = json.load(open(W + r"\asr\work\fa_LV60K.json"))
for x in words:
    x["s"], x["e"] = x["fa_start"], x["fa_end"]
N = len(words)
nrm = lambda s: re.sub(r"[^a-z0-9'-]", "", s.lower())

enh, sr = sf.read(W + r"\audio\enh_full_v2chain.wav", dtype="float32")
assert sr == SR
HOP = 24          # 0.5 ms
WIN = 120         # 2.5 ms
env = np.sqrt(np.convolve(enh.astype(np.float64) ** 2, np.ones(WIN) / WIN, "same"))[::HOP]
edb = 20 * np.log10(env + 1e-9)
def E(t): return edb[min(len(edb) - 1, max(0, int(round(t * SR / HOP))))]
def peak(t0, t1):
    a, b = int(max(0, t0) * SR / HOP), int(t1 * SR / HOP) + 1
    return edb[a:b].max()

# --------------------------------------------------------------------------------------------
# removal list: (first_idx, last_idx, expected words (normalized, for safety), reason)
# --------------------------------------------------------------------------------------------
R = []
def rm(i, j, exp, reason):
    got = [nrm(words[k]["word"]) for k in range(i, j + 1)]
    want = [nrm(w) for w in exp.split()]
    if got != want:
        sys.exit(f"MISMATCH at {i}-{j}: got {got} expected {want}")
    R.append((i, j, reason))

rm(18, 18, "[um]", "um")
rm(38, 47, "well it's gonna be uploaded on that channel most likely", "meta aside about uploading")
rm(146, 150, "that shit goes by fast", "restart at the file join (same sentence said again right after)")
rm(307, 307, "[um]", "um")
rm(427, 427, "that's", "stray false start")
rm(438, 438, "[um]", "um")
rm(483, 484, "[um] like", "um + doubled like")
rm(550, 551, "i w-", "false start")
rm(561, 561, "[um]", "um")
rm(582, 582, "wh-", "false start")
rm(590, 590, "s-", "false start")
rm(592, 592, "like", "doubled 'like like'")
rm(670, 672, "is people like", "restart ('is people like is everyone')")
rm(819, 820, "see that", "restart ('see that see them')")
rm(828, 828, "whatever", "doubled 'whatever whatever'")
rm(884, 884, "i", "stutter 'I I'")
rm(1073, 1075, "then you're like", "restart before 'I feel like you're cooked'")
rm(1092, 1093, "like [um]", "um")
rm(1100, 1121, "like i'll i'll probably make a separate video about this i don't know if i'm gonna upload it it depends but [um]",
   "tangent about a future video / uploading")
rm(1147, 1149, "f- like f-", "false starts before 'fucking'")
rm(1169, 1169, "m-", "false start")
rm(1243, 1243, "ga-", "false start")
rm(1309, 1309, "[um]", "um (0.7 s)")
rm(1351, 1351, "[um]", "um")
rm(1365, 1365, "f-", "false start")
rm(1372, 1372, "i", "stutter 'I I'")
rm(1435, 1435, "they", "restart ('they their friends')")
rm(1451, 1473, "and i don't know if it's just like people don't understand like the like the i don't know the word but like and",
   "failed sentence: word-search stumble, restarted right after")
rm(1514, 1533, "like i know i got like way off topic i've been y- yapping about this for like five minutes bro",
   "'I got way off topic' aside")
rm(1625, 1625, "[um]", "um")
rm(1704, 1705, "your mo-", "false start ('your mo- your dad')")
rm(1753, 1753, "yourself", "doubled 'yourself yourself'")
rm(1776, 1776, "g-", "false start")
rm(1798, 1802, "you have to constantly like", "abandoned clause before 'to make yourself proud'")
rm(1809, 1809, "c-", "false start")
rm(1818, 1820, "i was [uh]", "restart ('I was uh I listened')")
rm(1854, 1856, "he always like", "restart before 'what I noticed'")
rm(1909, 1912, "like his goals basically", "restart ('his goals basically his goals are changing')")
rm(1959, 1959, "that", "doubled 'that that'")
rm(1987, 1989, "you're gonna like", "restart before 'your needs'")
rm(1991, 1991, "sh-", "false start")
rm(2051, 2052, "con- con-", "false starts")
rm(2097, 2098, "i barely", "restart ('I barely I haven't')")
rm(2124, 2124, "i", "stutter 'I I'")
rm(2142, 2143, "i don't", "doubled 'I don't I don't'")
rm(2289, 2289, "b-", "false start")
rm(2295, 2298, "fucking i don't know", "hesitation before 'fucking tricycle cars'")
rm(2383, 2383, "p-", "false start")
rm(2449, 2449, "d-", "false start")
rm(2472, 2472, "look", "doubled 'look look'")
rm(2479, 2479, "[um]", "um")
rm(2503, 2508, "do not have to worry another", "abandoned clause ('...worry another, their parents...')")
rm(2527, 2528, "go b-", "false start")
rm(2606, 2606, "[um]", "um")
rm(2688, 2688, "[um]", "um")
rm(2710, 2710, "[um]", "um")

OVR_PATH = W + r"\edl\overrides_v4.json"
OVR = json.load(open(OVR_PATH)) if os.path.exists(OVR_PATH) else {}
_full = set()
for i, j, _ in R: _full.update(range(i, j + 1))
def _key(i, j):
    p = i - 1
    while p in _full: p -= 1
    q = j + 1
    while q in _full: q += 1
    return f"{p}-{q}"
R = [r for r in R if not OVR.get(_key(r[0], r[1]), {}).get("skip")]
removed_idx = set()
for i, j, _ in R:
    removed_idx.update(range(i, j + 1))

# --------------------------------------------------------------------------------------------
# cut-point placement
# --------------------------------------------------------------------------------------------
QUIET = -42.0    # dBFS of the enhanced signal: noise-gated silence sits far below this

def quiet_runs(t0, t1, thr=QUIET):
    """contiguous runs where the envelope is below thr inside [t0,t1] -> list of (start,end)"""
    a, b = int(max(0, t0) * SR / HOP), int(t1 * SR / HOP)
    seg = edb[a:b] <= thr
    runs, k = [], 0
    while k < len(seg):
        if seg[k]:
            s0 = k
            while k < len(seg) and seg[k]: k += 1
            runs.append(((a + s0) * HOP / SR, (a + k) * HOP / SR))
        else:
            k += 1
    return runs

def valley(t0, t1, prefer=None):
    """time of the deepest dip in [t0,t1]; ties (digital silence) broken toward `prefer`"""
    a, b = int(max(0, t0) * SR / HOP), int(t1 * SR / HOP) + 1
    if b <= a + 1: return (t0 + t1) / 2, 0.0
    seg = edb[a:b]
    mn = seg.min()
    cand = np.where(seg <= mn + 2.0)[0]
    if prefer is not None:
        k = cand[np.argmin(np.abs((a + cand) * HOP / SR - prefer))]
    else:
        k = cand[len(cand) // 2]
    t = (a + k) * HOP / SR
    depth = min(peak(t - 0.06, t - 0.01), peak(t + 0.01, t + 0.06)) - mn
    return t, float(depth)

def zero_cross(t):
    k = int(round(t * SR)); w = 96
    seg = enh[max(0, k - w): k + w]
    zc = np.where(np.diff(np.signbit(seg).astype(np.int8)) != 0)[0]
    if len(zc) == 0: return t
    kk = zc[np.argmin(np.abs(zc - min(w, k)))] + max(0, k - w)
    return kk / SR

def ends_sentence(w): return bool(re.search(r"[.?!]$", w))

joins = []   # dicts: a (end of kept audio), b (start of next kept audio), info
kept = [k for k in range(N) if k not in removed_idx]
notes = []
for p, q in zip(kept[:-1], kept[1:]):
    pw, qw = words[p], words[q]
    between = list(range(p + 1, q))
    gap = qw["s"] - pw["e"]
    if not between and gap < 0.9:
        continue
    sent_end = ends_sentence(pw["word"])
    if between:
        first, last = words[between[0]], words[between[-1]]
        pre = max(0.0, first["s"] - pw["e"])
        post = max(0.0, qw["s"] - last["e"])
        P = 0.40 if sent_end else (0.20 if pre + post >= 0.25 else 0.0)
        # if the removed stretch is long, a clear pause reads better
        if last["e"] - first["s"] > 3.0: P = max(P, 0.35)
        if pre + post <= P:
            kb, ka = pre, post
        else:
            kb = min(pre, P * 0.5); ka = min(post, P - kb)
            if ka < P * 0.5 and pre > kb: kb = min(pre, P - ka)
        # left cut point: inside the pre-silence if there is some, else at the dip at the word start
        if pre >= 0.06:
            a, da = valley(pw["e"] + max(0.0, kb - 0.03), pw["e"] + kb + 0.03, prefer=pw["e"] + kb)
        else:
            a, da = valley(first["s"] - 0.045, first["s"] + 0.025, prefer=first["s"] - 0.01)
        if post >= 0.06:
            b, db = valley(qw["s"] - ka - 0.03, qw["s"] - max(0.0, ka - 0.03), prefer=qw["s"] - ka)
        else:
            b, db = valley(qw["s"] - 0.045, qw["s"] + 0.025, prefer=qw["s"] - 0.01)
        label = " ".join(words[k]["word"] for k in between)
        why = "; ".join(sorted({next(r[2] for r in R if r[0] <= k <= r[1]) for k in between}))
    else:
        # plain long pause: shorten to ~0.35-0.45 s, cutting only inside real silence
        runs = [r for r in quiet_runs(pw["e"], qw["s"]) if r[1] - r[0] >= 0.75]
        if not runs: continue
        r0 = max(runs, key=lambda r: r[1] - r[0])
        P = 0.45 if sent_end else 0.35
        a, da = r0[0] + P * 0.55, 99.0
        b, db = r0[1] - P * 0.45, 99.0
        label = f"(pause {gap:.2f}s)"; why = "long pause shortened"
    ov = OVR.get(f"{p}-{q}")
    if ov and "a" in ov:
        a, b, da, db = ov["a"], ov["b"], 99.0, 99.0
    elif between and max(E(a), E(b)) > -45:
        b2, c = align_b(enh, a, b)
        if c > 0.3: b = b2
    if b - a < 0.03:
        continue
    joins.append(dict(a=a, b=b, da=da, db=db, prev=pw["word"], nxt=qw["word"], label=label, why=why, pi=p, qi=q))

# ---- segments of kept source audio (canonical source time) ----
MAIN_START = max(0.0, words[0]["s"] - 0.10)
MAIN_END = min(len(enh) / SR, words[-1]["e"] + 1.6)
F = FX                       # 10 ms crossfade centred on each cut point
pts = [MAIN_START] + [x for j in joins for x in (j["a"], j["b"])] + [MAIN_END]
segs = [(pts[2 * k], pts[2 * k + 1]) for k in range(len(joins) + 1)]
y, seg_map = assemble(enh, segs, [(j["a"], j["b"]) for j in joins])
TOTAL = len(y) / SR
np.save(W + r"\audio\voice_v4_pregain.npy", y.astype(np.float32))
sf.write(W + r"\audio\voice_v4_pregain.wav", y.astype(np.float32), SR, subtype="FLOAT")

def to_final(t, tol=0.04):
    for s0, e0, o0 in seg_map:
        if s0 - tol <= t <= e0 + tol: return o0 + (min(max(t, s0), e0) - s0)
    return None

fw = []
for k, w in enumerate(words):
    if k in removed_idx: continue
    fs, fe = to_final(w["s"]), to_final(w["e"])
    if fs is not None and fe is not None:
        fw.append({"i": k, "word": w["word"], "start": round(fs, 3), "end": round(fe, 3), "src_start": w["s"], "src_end": w["e"]})
json.dump(fw, open(W + r"\edl\final_words_v4.json", "w"), indent=0)
json.dump({"joins": joins, "segs": segs, "seg_map": seg_map, "total_seconds": TOTAL, "main_start": MAIN_START, "main_end": MAIN_END},
          open(W + r"\edl\edl_v4.json", "w"), indent=1, default=float)

removed_total = sum(j["b"] - j["a"] for j in joins)
def mmss(t): t = int(round(t)); return f"{t // 60}:{t % 60:02d}"
with open(W + r"\edl\cutlist_v4.txt", "w", encoding="utf-8") as f:
    f.write("CUTLIST v4 - everything taken out of your two recordings (joined 1.mkv then 2.mkv).\n")
    f.write(f"{len(joins)} cuts, {removed_total:.1f} s removed, final length {mmss(TOTAL)} ({TOTAL:.1f} s). No cold open; the story starts with your first word.\n")
    f.write("The time on each line = where the cut is heard in the finished video. [ASIDE] = a tangent / abandoned sentence: tell me if you want any of them back.\n\n")
    for k, j in enumerate(joins):
        at = seg_map[k + 1][2] - 0.005
        tag = " [ASIDE]" if ("tangent" in j["why"] or "aside" in j["why"] or "failed sentence" in j["why"] or "abandoned" in j["why"]) else ""
        f.write(f"{mmss(at)}  ({at:7.1f}s)  {j['why']}{tag}\n      removed {j['b']-j['a']:.2f}s of audio: {j['label']}\n      heard as: ...{j['prev']} | {j['nxt']}...\n")
print(f"cuts {len(joins)}  removed {removed_total:.1f}s  TOTAL {TOTAL:.2f}s  words kept {len(fw)}/{N}")
soft = [(round(j['a'],2), j['label'][:40], round(min(j['da'], j['db']),1)) for j in joins if min(j['da'], j['db']) < 10]
print("soft-dip cuts (depth<10 dB):", len(soft)); [print("  ", s) for s in soft]
