#!/usr/bin/env python
"""Full Review (Nov 1, 2026): measure every built Short's edit features and join them to results.

Reads each production folder (words.json, cuts.json, captions.ass, sfx.json, music.json, final mp4) and joins
YouTube Analytics API pulls (Research Notes/Studio exports/api, api FC: daily + retention CSVs) by title match.
Writes Research Notes/Full Review data (Nov 1, 2026)/features.csv + correlations.csv (Spearman, with n).
Read-only. Run: PYTHONUTF8=1 python Tools/review_measure.py [--no-media] [--out DIR]
"""
import csv, glob, json, os, re, statistics as st, subprocess, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUMW = set("one two three four five six seven eight nine ten eleven twelve twenty thirty forty fifty hundred thousand million billion".split())
STOP = set("the a an of to in on for and is was he his she her it at by with from as that this who how what why".split())


def toks(s):
    return [t for t in re.findall(r"[a-z0-9']+", s.lower()) if t not in STOP]


def load(p, d=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def ass_feats(p):
    out = dict(cap_screens=0, cap_words_per=None, cap_colored_screens=0, cap_colors="", cap_font="", cap_size="", cap_y="")
    try:
        t = open(p, encoding="utf-8").read()
    except Exception:
        return out
    m = re.search(r"^Style: Cap,([^,]*),(\d+)", t, re.M)
    if m:
        out["cap_font"], out["cap_size"] = m.group(1), m.group(2)
    n = []
    cols = {}
    ys = set()
    for ln in re.findall(r"^Dialogue:.*$", t, re.M):
        txt = ln.split(",", 9)[-1]
        y = re.search(r"\\pos\(\d+,(\d+)\)", txt)
        if y:
            ys.add(y.group(1))
        body = re.sub(r"\{[^}]*\}", "", txt).strip()
        if not body:
            continue
        n.append(len(body.split()))
        c = re.search(r"\\c&H([0-9A-F]{6})&", txt)
        if c:
            cols[c.group(1)] = cols.get(c.group(1), 0) + 1
    out["cap_screens"] = len(n)
    out["cap_words_per"] = round(sum(n) / len(n), 2) if n else None
    out["cap_colored_screens"] = sum(cols.values())
    out["cap_colors"] = "|".join(f"{k}:{v}" for k, v in cols.items())
    out["cap_y"] = ",".join(sorted(ys))
    return out


def word_feats(p):
    w = load(p, []) or []
    o = {}
    if not w:
        return o
    s0, e1 = w[0]["start"], w[-1]["end"]
    o["voice_s"] = round(e1 - s0, 1)
    o["n_words"] = len(w)
    o["wpm"] = round(len(w) / (e1 - s0) * 60) if e1 > s0 else None
    gaps = [w[i + 1]["start"] - w[i]["end"] for i in range(len(w) - 1)]
    o["pauses_gt_0.3"] = sum(g > 0.3 for g in gaps)
    o["median_gap"] = round(st.median(gaps), 3) if gaps else None
    o["max_gap"] = round(max(gaps), 2) if gaps else None
    n1 = 0
    for i, x in enumerate(w):
        if re.search(r"[.!?]$", x["word"]):
            n1 = i + 1
            break
    o["line1_words"] = n1 or None
    o["line1_end_s"] = round(w[n1 - 1]["end"], 2) if n1 else None
    for x in w:
        t = re.sub(r"[^\w]", "", x["word"].lower())
        if any(ch.isdigit() for ch in t) or t in NUMW:
            o["first_number_s"] = round(x["start"], 2)
            break
    for i, x in enumerate(w[1:], 1):
        if x["word"][:1].isupper() and not re.search(r"[.!?]$", w[i - 1]["word"]):
            o["first_name_s"] = round(x["start"], 2)
            break
    o["live_words"] = sum(1 for x in w if x.get("live"))
    return o


def shot_feats(folder):
    c = load(os.path.join(folder, "cuts.json"), {}) or {}
    sh = c.get("shots") if isinstance(c, dict) else None
    o = {}
    if not sh:
        return o
    lens = [s.get("len") or 0 for s in sh]
    starts = []
    t = 0
    for l in lens:
        starts.append(t)
        t += l
    o["n_shots"] = len(sh)
    o["shots_first3"] = sum(s < 3 for s in starts)
    o["shots_first5"] = sum(s < 5 for s in starts)
    o["shot1_len"] = round(lens[0], 2)
    o["median_shot"] = round(st.median(lens), 2)
    o["last_shot_len"] = round(lens[-1], 2)
    o["zooms"] = sum(1 for s in sh if s.get("zoom"))
    o["speed_ramps"] = sum(1 for s in sh if s.get("speed") and s["speed"] != 1)
    o["overlays"] = sum(len(s.get("overlay") or []) for s in sh)
    o["replays"] = sum(1 for s in sh if s.get("replay"))
    o["blurfit_share"] = round(sum(1 for s in sh if s.get("blurfit")) / len(sh), 2)
    o["n_sources"] = len(c.get("sources", {}))
    o["cut_total_s"] = round(t, 1)
    return o


def media_feats(folder):
    o = {}
    mp = sorted(glob.glob(os.path.join(folder, "*.mp4")))
    mp = [m for m in mp if "narrated spare" not in m] or mp
    if not mp:
        return o
    m = next((x for x in mp if "(music)" in x), mp[0])
    try:
        o["final_s"] = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", m], text=True).strip()), 1)
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", m, "-frames:v", "1", "-vf", "signalstats,metadata=print:file=-", "-f", "null", "-"], capture_output=True, text=True)
        y = re.search(r"YAVG=([\d.]+)", r.stdout)
        if y:
            o["frame1_luma"] = round(float(y.group(1)))
    except Exception:
        pass
    return o


def results():
    res = {}
    for ch, d in (("nba", "api"), ("fc", "api FC")):
        base = os.path.join(ROOT, "Research Notes", "Studio exports", d)
        dp = sorted(glob.glob(os.path.join(base, "daily *.csv")))[-1]
        rp = sorted(glob.glob(os.path.join(base, "retention *.csv")))[-1]
        ret = {}
        for r in csv.DictReader(open(rp, encoding="utf-8")):
            ret.setdefault(r["video_id"], {})[round(float(r["elapsed_ratio"]), 2)] = float(r["audience_watch_ratio"])
        for r in csv.DictReader(open(dp, encoding="utf-8")):
            if not r["views"]:
                continue
            cv = ret.get(r["video_id"], {})
            res[r["video_id"]] = dict(
                channel=ch, video_id=r["video_id"], title=r["title"], published=r["published"][:10],
                length_s=r["length_s"], age_days=r["age_days"], views=int(float(r["views"])),
                avg_pct_viewed=float(r["averageViewPercentage"] or "nan"), engaged_ratio=float(r["engaged_ratio"] or "nan"),
                subs=r["subscribersGained"], ret_at_3pct=cv.get(0.03), ret_at_10pct=cv.get(0.10), ret_at_50pct=cv.get(0.5),
                ret_end=cv.get(0.99) or cv.get(1.0),
                early_drop=(round(cv[0.01] - cv[0.1], 3) if 0.01 in cv and 0.1 in cv else None))
    return res


def match(folder_title, res, ch):
    ft = set(toks(folder_title))
    best = (0, None)
    for v in res.values():
        if v["channel"] != ch:
            continue
        vt = set(toks(v["title"]))
        if not vt or not ft:
            continue
        cov = len(ft & vt) / len(ft)  # folder names are truncated, so coverage of the folder's words matters most
        j = cov * 0.7 + 0.3 * len(ft & vt) / len(ft | vt)
        if j > best[0]:
            best = (j, v)
    return best[1] if best[0] >= 0.6 else None


def public(ch):
    """Public view counts (yt-dlp flat playlist saved by the review): id|views|title. Rounded by YouTube to 2 sig figs when large."""
    out = {}
    f = os.path.join(ROOT, "Research Notes", "Full Review data (Nov 1, 2026)", "public_" + ("MetaSportsClips" if ch == "nba" else "MetaSportsFC") + ".txt")
    try:
        for ln in open(f, encoding="utf-8"):
            i, v, t = ln.rstrip().split("|", 2)
            if v.isdigit():
                out[i] = dict(channel=ch, video_id=i, title=t, views=int(v))
    except Exception:
        pass
    return out


def rank(x):
    o = sorted(range(len(x)), key=lambda i: x[i])
    r = [0.0] * len(x)
    i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = rank(a), rank(b)
    ma, mb = st.mean(ra), st.mean(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** .5
    return num / den if den else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "Research Notes", "Full Review data (Nov 1, 2026)"))
    ap.add_argument("--no-media", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    res = results()
    pub = {"nba": public("nba"), "fc": public("fc")}
    rows = []
    for ch, pat in (("nba", "Productions/MetaSports/20*"), ("fc", "Soccer Channel/Productions/20*")):
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            if not os.path.isdir(f) or not os.path.exists(os.path.join(f, "words.json")):
                continue
            name = os.path.basename(f)
            title = re.sub(r"^\d{4}-\d\d-\d\d\s+(S?\d+\s+)?", "", name)
            r = dict(channel=ch, folder=name)
            m = match(title, res, ch)
            r.update(word_feats(os.path.join(f, "words.json")))
            r.update(shot_feats(f))
            r.update(ass_feats(os.path.join(f, "captions.ass")))
            sf = load(os.path.join(f, "sfx.json"), [])
            r["sfx"] = len(sf) if isinstance(sf, list) else None
            mj = load(os.path.join(f, "music.json"))
            r["music"] = bool(mj)
            r["music_lu"] = (mj or {}).get("bed_lu")
            r["real_audio"] = os.path.isdir(os.path.join(f, "_realaudio")) or bool(r.get("live_words"))
            if not a.no_media:
                r.update(media_feats(f))
            if m:
                r.update({k: v for k, v in m.items() if k != "channel"})
            pm = match(title, pub[ch], ch)
            if pm:
                r["views_pub"] = pm["views"]
                r["pub_id"] = pm["video_id"]
                if not m:
                    import datetime as _d
                    r["age_days"] = (_d.date(2026, 11, 1) - _d.date.fromisoformat(name[:10])).days
            rows.append(r)
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(os.path.join(a.out, "features.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, keys)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} folders, {sum(1 for r in rows if r.get('views'))} joined to results")
    skip = {"channel", "folder", "title", "published", "video_id", "cap_colors", "cap_font", "cap_y", "real_audio", "views", "views_pub", "pub_id", "avg_pct_viewed",
            "engaged_ratio", "subs", "ret_at_3pct", "ret_at_10pct", "ret_at_50pct", "ret_end", "early_drop", "age_days", "length_s"}
    num = [k for k in keys if k not in skip]
    lines = []
    for ch in ("nba", "fc"):
        for tgt in ("avg_pct_viewed", "engaged_ratio", "views_pub"):
            for k in num:
                pts = []
                for r in rows:
                    if r["channel"] != ch or r.get(k) in (None, "") or r.get(tgt) in (None, ""):
                        continue
                    try:
                        x, y = float(r[k]), float(r[tgt])
                    except ValueError:
                        continue
                    if y != y or float(r.get("age_days") or 0) < 3:
                        continue
                    pts.append((x, y))
                if len(pts) >= 8 and len(set(p[0] for p in pts)) > 1:
                    lines.append((ch, tgt, k, len(pts), round(spearman([p[0] for p in pts], [p[1] for p in pts]), 2)))
    with open(os.path.join(a.out, "correlations.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["channel", "target", "feature", "n", "spearman"])
        w.writerows(lines)
    for l in sorted(lines, key=lambda x: -abs(x[4]))[:45]:
        print(*l)


if __name__ == "__main__":
    main()
