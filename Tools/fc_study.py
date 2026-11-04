"""FC clip-repetition study (Nov 4, 2026): joins fc_reuse metrics to Studio outcomes + retention curves. Prints markdown tables.
  python Tools/fc_study.py"""
import csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fc_reuse as F
R = F.ROOT
VID = {"S01": "Wcaa80VvBmU", "S05": "DfDEyHM33is", "S17": "oeHLlOVX4ec", "S03": "9GJgflHx7pE", "S25": "LgP8hGayRiE", "S19": "BOsvemp6eTE",
       "S08": "M40gpi_afJo", "S16": "vwySCjDCmF8", "S18": "rjsig3vMYU4", "S07": "7KriW5jkFVc", "S06": "ORnkQcenDd8", "S04": "svDicOCeh7I",
       "S02": "y2aDVIc9rfg", "S15": "WCeenVoseEM", "S20": "ClFHN2NXXyU"}
daily = {r["video_id"]: r for r in csv.DictReader(open(os.path.join(R, "Research Notes/Studio exports/api FC/daily 2026-11-04.csv"), encoding="utf-8"))}
tab = {r["Content"]: r for r in csv.DictReader(open(os.path.join(R, "Research Notes/Studio exports/Content 2026-10-07 to 2026-11-04 FC/Table data.csv"), encoding="utf-8"))}
curves = {}
for r in csv.DictReader(open(os.path.join(R, "Research Notes/Studio exports/api FC/retention 2026-11-04.csv"), encoding="utf-8")):
    curves.setdefault(r["video_id"], []).append((float(r["elapsed_ratio"]), float(r["audience_watch_ratio"]), float(r["relative_retention"])))
rows = []
for d in F.folders():
    sid = os.path.basename(d).split()[1]
    if sid not in VID: continue
    v = VID[sid]; t = tab[v]; dl = daily.get(v, {})
    views = int(t["Views"]); dur = float(t["Duration"]); avd = float(t["Watch time (hours)"]) * 3600 / views
    pct = float(dl["averageViewPercentage"]) if dl.get("averageViewPercentage") else 100 * avd / dur
    shots = json.load(open(os.path.join(d, "cuts.json"), encoding="utf-8"))["shots"]; st = F.load_starts(d)
    r = F.reuse(shots, st, dur)
    mp4 = F.draft(d); vis = F.visual_repeats(mp4) if mp4 else (None, 0, None)
    rows.append(dict(sid=sid, v=v, views=views, pct=pct, subs=int(t["Subscribers"]), subs1k=1000 * int(t["Subscribers"]) / views, dur=dur, **r, vis=vis[0], vframes=vis[1], d=d, st=st, cshots=shots))
print("| Short | views | avg % viewed | subs | shots | mean shot s | overlapping pairs (unexcused) | min gap s | max one-source share | consecutive same-source | visual repeats (of frames) |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    print(f"| {r['sid']} | {r['views']:,} | {r['pct']:.0f}% | {r['subs']} | {r['shots']} | {r['mean_shot']:.2f} | {r['overlap_pairs']} ({r['n_unexcused']}) | {r['min_gap_s'] if r['min_gap_s'] is None else round(r['min_gap_s'],1)} | {r['max_src_share']:.2f} | {r['consec_same']} | {r['vis']} of {r['vframes']} |")

def spear(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y)); return float(np.corrcoef(rx, ry)[0, 1])
def boot(x, y, n=4000, seed=1):
    rng = np.random.default_rng(seed); x = np.array(x); y = np.array(y); out = []
    for _ in range(n):
        i = rng.integers(0, len(x), len(x))
        if len(set(x[i])) < 2 or len(set(y[i])) < 2: continue
        out.append(spear(x[i], y[i]))
    return np.percentile(out, [2.5, 97.5])
print(f"\nn = {len(rows)}")
for name in ("n_unexcused", "overlap_pairs", "max_src_share", "consec_same", "mean_shot", "vis"):
    x = [r[name] for r in rows]
    for yn in ("pct", "views", "subs1k"):
        y = [r[yn] for r in rows]; lo, hi = boot(x, y)
        print(f"spearman({name}, {yn}) = {spear(x, y):+.2f}  95% bootstrap CI [{lo:+.2f}, {hi:+.2f}]")
# retention curves: where do the drops fall, and is a repeated shot on screen there?
print("\n### Retention drops vs repeated shots (per Short, windows of 5% of runtime)")
print("| Short | biggest drop windows (second marks) | repeated-shot starts inside them | steepest 5% windows holding a repeated shot | share of all windows holding a repeat |")
print("|---|---|---|---|---|")
agg_rep, agg_non = [], []
for r in rows:
    c = curves.get(r["v"]);
    if not c: continue
    c = sorted(c); xs = np.array([a[0] for a in c]); w = np.array([a[1] for a in c]); dur = r["dur"]
    # per-5% drop in absolute watch ratio
    k = 5; drops = [(w[i - k] - w[i], xs[i - k] * dur, xs[i] * dur) for i in range(k, len(w), k)]
    tl, _ = F.timeline(r["cshots"], r["st"], dur)
    seen = {}; rep_times = []
    for i, a in enumerate(tl):
        for b in tl[:i]:
            if a["src"] and a["src"] == b["src"] and a["end"] > b["at"] + .05 and b["end"] > a["at"] + .05 and not a["replay"]:
                rep_times.append(a["t0"]); break
    def has_rep(t0, t1): return any(t0 - 0.0 <= x < t1 for x in rep_times)
    flags = [(dr, t0, t1, has_rep(t0, t1)) for dr, t0, t1 in drops]
    for dr, t0, t1, hr in flags: (agg_rep if hr else agg_non).append(dr)
    top = sorted(flags, reverse=True)[:3]
    holding = sum(1 for f in top if f[3])
    share = sum(1 for f in flags if f[3]) / len(flags)
    print(f"| {r['sid']} | {', '.join(f'{t0:.0f}-{t1:.0f}s (-{dr*100:.0f}pt)' for dr, t0, t1, _ in top)} | {len(rep_times)} | {holding} of 3 | {share:.0%} |")
print(f"\nmean 5%-window drop: windows with a repeated-shot start {np.mean(agg_rep)*100:.1f} pt (n={len(agg_rep)}), without {np.mean(agg_non)*100:.1f} pt (n={len(agg_non)})")
json.dump([{k: v for k, v in r.items() if k not in ("cshots", "st", "d", "unexcused")} for r in rows], open(os.path.join(R, "Research Notes", "_fc_study_rows.json"), "w"), default=str)
