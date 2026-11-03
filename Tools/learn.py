"""The learning loop as a script, not a mood (Nov 3, 2026; automation to-do items 2 and 8). Zero Claude credits.

  python Tools/learn.py ingest [--fetch]   # (re)build Research Notes/Experiments.csv from the repo's own records
  python Tools/learn.py report             # compare every feature value with its channel median -> Research Notes/Learned Weights.md
  python Tools/learn.py                    # both

Sources, in order (later ones fill blanks, never overwrite a hand-filled value in Experiments.csv):
  Posted Tracker (Oct 21)  lane, star, posted date, views            | Shorts Dataset.csv  stayed %, avg % viewed, engaged ratio, music
  MetaSportsClips - all 80 Shorts.csv  views, length, date           | Scheduled Uploads.csv  draft file name (music / no music), slot
  --fetch: public view counts with yt-dlp (no login, no credits) for @MetaSportsClips and @MetaSportsFC; stamps views_date.
Rules baked in (from the to-do list): never judge before 72 h (age_days < 3 is excluded); n is printed on every row and n < 5
is marked "guess"; a lane with 3 flops in a row (each under its channel median) is flagged PAUSE; about 70% of builds should come
from lanes above the median and 30% explicit experiments. Change one variable per test or the loop learns nothing.
"""
import argparse, csv, datetime as dt, json, os, re, statistics as st, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RN = os.path.join(ROOT, "Research Notes")
EXP = os.path.join(RN, "Experiments.csv")
OUT = os.path.join(RN, "Learned Weights.md")
COLS = ["channel", "video_id", "posted", "title", "lane", "star", "fresh", "title_shape", "length_s", "music", "stayed_pct",
        "avg_pct_viewed", "engaged_ratio", "views", "views_date", "source", "notes"]
HAND = ["lane", "star", "fresh", "title_shape", "music", "notes"]  # hand-filled values are kept on re-ingest
STARS = (r"LeBron|Bronny|Wemby|Wembanyama|Curry|Steph|Flagg|Jokic|Jokić|SGA|Shai|Giannis|Luka|Kawhi|Jordan|Kobe|Shaq|Durant|"
         r"Harden|Kidd|Draymond|Messi|Ronaldo|Zidane|Maradona|Pickford|Lewandowski|Mourinho|Fabregas|Fábregas|Klopp|Haaland")
HANDLES = {"nba": "@MetaSportsClips", "fc": "@MetaSportsFC"}
TODAY = dt.date.today()


def read(path):
    if not os.path.exists(path):
        return []
    return list(csv.DictReader(open(path, encoding="utf-8-sig")))


def num(x):
    try:
        return float(str(x).replace(",", ""))
    except (TypeError, ValueError):
        return None


def shape(title):
    t = re.sub(r"#\w+", "", title).strip()
    w = t.split()[0].lower() if t.split() else ""
    if "?" in t or w in {"why", "how", "who", "what", "did", "does", "is", "are", "can", "would"}:
        return "question"
    if re.search(r"\d", t):
        return "number"
    return "statement"


def fetch(rows):
    for ch, handle in HANDLES.items():
        try:
            r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", f"https://www.youtube.com/{handle}/shorts"],
                               capture_output=True, text=True, encoding="utf-8", timeout=240)
            entries = json.loads(r.stdout)["entries"]
        except Exception as e:  # network or yt-dlp trouble: keep old numbers
            print(f"fetch {ch}: skipped ({str(e)[:80]})")
            continue
        n = 0
        for e in entries:
            v = e.get("view_count")
            if e.get("id") and v is not None:
                row = rows.setdefault(e["id"], {c: "" for c in COLS} | {"video_id": e["id"], "channel": ch, "title": e.get("title", "")})
                row["views"], row["views_date"] = str(v), TODAY.isoformat()
                row["source"] = (row["source"] + "+yt-dlp").strip("+")
                n += 1
        print(f"fetch {ch}: {n} public view counts")


def ingest(do_fetch):
    rows = {r["video_id"]: r for r in read(EXP)}

    def put(vid, ch, **kw):
        row = rows.setdefault(vid, {c: "" for c in COLS} | {"video_id": vid, "channel": ch})
        for k, v in kw.items():
            if v not in ("", None) and (not row.get(k) or k in ("views", "views_date", "stayed_pct", "avg_pct_viewed", "engaged_ratio") and k not in HAND):
                row[k] = str(v)
        row["source"] = "+".join(dict.fromkeys(filter(None, row["source"].split("+") + [kw.get("source", "")])))
        return row

    for r in read(os.path.join(RN, "MetaSportsClips - all 80 Shorts.csv")):
        d = r["date"]
        put(r["id"], "nba", title=r["title"], posted=f"{d[:4]}-{d[4:6]}-{d[6:]}", length_s=r["dur"], views=r["views"],
            views_date="2026-10-14", source="all80")
    for r in read(os.path.join(RN, "Posted Tracker (Oct 21, 2026).csv")):
        put(r["video_id"], "nba", title=r["title"], posted=r["posted"], lane=r["lane"], star=r["star"], views=r["views_oct21_0010utc"],
            views_date="2026-10-21", source="tracker")
    for r in read(os.path.join(RN, "Shorts Dataset.csv")):
        put(r["video_id"], r["channel"], title=r["title"], posted=r["published"], length_s=r["length_s"], lane=r["lane"], star=r["star"],
            fresh=r["fresh"], title_shape=r["title_shape"], music=r["music"], stayed_pct=r["stayed_pct"],
            avg_pct_viewed=r["avg_pct_viewed"], engaged_ratio=r["engaged_ratio"], views=r["views_api"] or r["views_first_window"],
            views_date=r["api_date"] or r["window"][-10:], source="dataset")
    for r in read(os.path.join(RN, "Scheduled Uploads.csv")):
        f = r["file"]
        music = "no" if "no music" in f.lower() else "yes" if "(music" in f.lower() else ""
        put(r["video_id"], r["channel"], title=r["title"], posted=r["publish_et"][:10], music=music, source="scheduled")
    for f in sorted(os.listdir(os.path.join(RN, "Studio exports", "api"))) if os.path.isdir(os.path.join(RN, "Studio exports", "api")) else []:
        if f.startswith("daily"):
            for ch, sub in (("nba", "api"), ("fc", "api FC")):
                for r in read(os.path.join(RN, "Studio exports", sub, f)):
                    if num(r.get("views")) is not None:
                        put(r["video_id"], ch, title=r["title"], posted=r["published"][:10], length_s=r["length_s"], views=r["views"],
                            views_date=f[6:16], engaged_ratio=r["engaged_ratio"], avg_pct_viewed=r["averageViewPercentage"], source="api")
    if do_fetch:
        fetch(rows)
    for r in rows.values():  # derived features, only where blank
        r["title_shape"] = r["title_shape"] or shape(r["title"])
        r["star"] = r["star"] or ("star" if re.search(STARS, r["title"], re.I) else "no star")
    out = sorted(rows.values(), key=lambda r: (r["channel"], r["posted"]))
    with open(EXP, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print(f"Experiments.csv: {len(out)} rows ({sum(1 for r in out if r['views'])} with views, {sum(1 for r in out if r['lane'])} with a lane)")


def length_bucket(s):
    s = num(s)
    return "" if s is None else "under 20 s" if s < 20 else "20-30 s" if s < 30 else "30-45 s" if s < 45 else "45 s +"


def lane_clean(l):
    return re.split(r"[,:(]", l.lower())[0].strip() if l else ""


def report():
    rows = read(EXP)
    mature = []
    for r in rows:
        v, p = num(r["views"]), r["posted"]
        try:
            age = (TODAY - dt.date.fromisoformat(p[:10])).days
        except ValueError:
            continue
        if v is None or age < 3:
            continue
        r["_v"], r["_age"] = v, age
        r["lane_c"], r["len_b"] = lane_clean(r["lane"]), length_bucket(r["length_s"])
        r["star"] = "no star" if r["star"] in ("", "no star") else "star named in title"
        r["music"] = {"none": "no", "": ""}.get(r["music"], r["music"])
        mature.append(r)
    lines = [f"# Learned Weights (auto-written by Tools/learn.py, {TODAY})", "",
             "Views vs the channel's own median, Shorts 3+ days old only. **n is on every row. n under 5 = guess, do not build a rule on it.**",
             "Ratio 1.0 = typical for the channel. Views are public counts at the date in Experiments.csv, not stayed-to-watch.", ""]
    findings, flags, leads = [], [], []
    for ch, name in (("nba", "MetaSports (NBA)"), ("fc", "MetaSports FC (soccer)")):
        rs = [r for r in mature if r["channel"] == ch and r["posted"] >= "2026-10-14"]  # the era of our own Shorts
        if len(rs) < 5:
            lines += [f"## {name}", f"Only {len(rs)} mature Shorts with views: too few to weigh anything.", ""]
            continue
        med = st.median(r["_v"] for r in rs)
        lines += [f"## {name}: n={len(rs)}, median {med:,.0f} views", "", "| Feature | Value | n | Median views | vs channel median | Read |", "|---|---|---|---|---|---|"]
        for dim, key in (("lane", "lane_c"), ("star in title", "star"), ("title shape", "title_shape"), ("length", "len_b"),
                         ("music", "music"), ("freshness", "fresh")):
            groups = {}
            for r in rs:
                if r[key]:
                    groups.setdefault(r[key], []).append(r["_v"])
            for val, vs in sorted(groups.items(), key=lambda kv: -st.median(kv[1])):
                m, n = st.median(vs), len(vs)
                ratio = m / med if med else 0
                read_ = "guess (n<5)" if n < 5 else "ABOVE" if ratio >= 1.5 else "BELOW" if ratio <= 0.67 else "typical"
                lines.append(f"| {dim} | {val} | {n} | {m:,.0f} | {ratio:.2f}x | {read_} |")
                if n >= 3:
                    leads.append((abs(ratio - 1) * n, f"{name}: {dim} \"{val}\" runs {ratio:.1f}x the channel median (n={n})."))
                if n >= 5 and read_ in ("ABOVE", "BELOW"):
                    findings.append((abs(ratio - 1) * n, f"{name}: {dim} \"{val}\" runs {ratio:.1f}x the channel median (median {m:,.0f} vs {med:,.0f} views, n={n})."))
        # lane streaks: last 3 Shorts in a lane all below the channel median -> pause
        by_lane = {}
        for r in sorted(rs, key=lambda r: r["posted"]):
            if r["lane_c"]:
                by_lane.setdefault(r["lane_c"], []).append(r["_v"])
        for lane, vs in by_lane.items():
            if len(vs) >= 3 and all(v < med for v in vs[-3:]):
                flags.append(f"- **PAUSE** {name} lane \"{lane}\": last 3 were under the channel median ({', '.join(f'{v:,.0f}' for v in vs[-3:])}).")
        lines.append("")
    lines += ["## One finding in plain English", ""]
    if findings:
        findings.sort(reverse=True)
        lines += [f"- {t}" for _, t in findings[:3]]
        lines.append("- Correlation, small n, mixed topics: use it to choose experiments, not as proof.")
    else:
        lines.append("- No feature has n>=5 and a clear gap yet. Everything above is a guess; keep logging.")
        if leads:
            leads.sort(reverse=True)
            lines.append("- Best lead so far (n=3-4, a GUESS to test, not a rule): " + leads[0][1][:-1] + ".")
    lines += ["", "## For daily-run (item 15)", "- Lane picks: about 70% from lanes marked ABOVE (or typical with a hit in the last 5), about 30% explicit experiments, one variable at a time.",
              "- A lane flagged PAUSE below is skipped until the Sunday review."]
    lines += flags or ["- No lane has 3 flops in a row (lanes are only known for the Oct 21 tracker set; most Shorts have no lane yet, so fill `lane` in Experiments.csv)."]
    lines += ["", f"Rows with a lane: {sum(1 for r in mature if r['lane_c'])} of {len(mature)} mature. Fill `lane` for new Shorts at build time."]
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"wrote {OUT} ({len(mature)} mature Shorts)")
    print("\n".join(l for l in lines if l.startswith("- ") and "Correlation" not in l)[:900])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="all", choices=["all", "ingest", "report"])
    ap.add_argument("--fetch", action="store_true", help="refresh public view counts with yt-dlp")
    a = ap.parse_args()
    if a.cmd in ("all", "ingest"):
        ingest(a.fetch)
    if a.cmd in ("all", "report"):
        report()
