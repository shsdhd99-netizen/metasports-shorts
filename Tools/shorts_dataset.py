"""One table of every Short's features and results, so rules come from data (Oct 24 2026 audit).

  python Tools/shorts_dataset.py            # merge every Studio export (+ API daily files) into Research Notes/Shorts Dataset.csv
  python Tools/shorts_dataset.py --report   # also print medians by lane, star, freshness and the 74% line

Results come from the Studio exports in "Research Notes/Studio exports/" (folders ending in "FC" are the soccer channel) and,
when present, the API files in "api/" and "api FC/" (views to date, avg % viewed, engaged ratio). For each Short the export whose
date window contains the publish date wins (its first-week numbers). Hand-filled columns are never overwritten: lane, star,
fresh (same-day news / late news / evergreen), frame1, music, captions, folder, notes. The daily runs add the lane etc. for each
new Short; star and title_shape are guessed when blank.
"""
import argparse, csv, datetime as dt, glob, os, re, statistics as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(ROOT, "Research Notes", "Studio exports")
OUT = os.path.join(ROOT, "Research Notes", "Shorts Dataset.csv")
COLS = ["channel", "video_id", "published", "title", "length_s", "stayed_pct", "avg_pct_viewed", "views_first_window", "window",
        "subs", "views_api", "engaged_ratio", "api_date", "lane", "star", "fresh", "title_shape", "frame1", "music", "captions",
        "folder", "notes"]
MANUAL = ["lane", "star", "fresh", "frame1", "music", "captions", "folder", "notes"]
STARS = r"LeBron|Bronny|Wemby|Wembanyama|Curry|Steph|Flagg|Jokic|SGA|Shai|Giannis|Luka|Kawhi|Jordan|Clark|Messi|Ronaldo|Zidane|Maradona|Pickford|Lewandowski"


def studio_rows():
    for d in sorted(glob.glob(os.path.join(EXP, "Content *"))):
        m = re.search(r"(\d{4}-\d\d-\d\d) to (\d{4}-\d\d-\d\d)", d)
        if not m or not os.path.exists(os.path.join(d, "Table data.csv")):
            continue
        a, b = (dt.date.fromisoformat(x) for x in m.groups())
        ch = "fc" if d.rstrip().endswith("FC") else "nba"
        for r in csv.DictReader(open(os.path.join(d, "Table data.csv"), encoding="utf-8")):
            if r.get("Content") in ("Total", "") or not r.get("Video publish time"):
                continue
            pub = dt.datetime.strptime(r["Video publish time"], "%b %d, %Y").date()
            yield ch, r, pub, a, b


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def merge():
    old = {r["video_id"]: r for r in csv.DictReader(open(OUT, encoding="utf-8"))} if os.path.exists(OUT) else {}
    best = {}
    for ch, r, pub, a, b in studio_rows():
        vid = r["Content"]
        key = (a <= pub <= b, num(r.get("Views")) or 0)
        if vid not in best or key > best[vid][0]:
            best[vid] = (key, ch, r, pub, a, b)
    rows = {}
    for vid, (_, ch, r, pub, a, b) in best.items():
        row = dict(old.get(vid, {}))
        row.update(channel=ch, video_id=vid, published=pub.isoformat(), title=r["Video title"], length_s=r.get("Duration", ""),
                   stayed_pct=r.get("Stayed to watch (%)", ""), avg_pct_viewed=r.get("Average percentage viewed (%)", ""),
                   views_first_window=r.get("Views", ""), window=f"{a}..{b}", subs=r.get("Subscribers", ""))
        rows[vid] = row
    for ch, sub in (("nba", "api"), ("fc", "api FC")):  # newest API daily file: views to date
        files = sorted(glob.glob(os.path.join(EXP, sub, "daily *.csv")))
        if files:
            day = os.path.basename(files[-1])[6:16]
            for r in csv.DictReader(open(files[-1], encoding="utf-8")):
                row = rows.setdefault(r["video_id"], dict(old.get(r["video_id"], {}), channel=ch, video_id=r["video_id"],
                                                        published=r["published"][:10], title=r["title"], length_s=r["length_s"]))
                row.update(views_api=r.get("views", ""), engaged_ratio=r.get("engaged_ratio", ""), api_date=day)
    for row in rows.values():
        if not row.get("star"):
            m = re.search(STARS, row.get("title", ""))
            row["star"] = m.group(0) if m else ""
        row["title_shape"] = "question" if "?" in row.get("title", "") else "statement"
    for vid, r in old.items():  # keep hand-made rows the exports don't cover
        rows.setdefault(vid, r)
    out = sorted(rows.values(), key=lambda r: (r.get("channel", ""), r.get("published", "")))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print(f"{OUT}: {len(out)} Shorts ({sum(1 for r in out if r.get('stayed_pct'))} with stayed %)")
    return out


def report(rows, since="2026-10-03"):
    for ch in ("nba", "fc"):
        g = [r for r in rows if r.get("channel") == ch and r.get("published", "") >= since and num(r.get("stayed_pct")) is not None]
        if not g:
            continue
        views = lambda r: num(r.get("views_api")) or num(r.get("views_first_window")) or 0
        print(f"\n{ch.upper()}: {len(g)} Shorts since {since}")
        hi = [r for r in g if num(r["stayed_pct"]) >= 74]
        print(f"  stayed 74%+: {len(hi)}, median views {st.median([views(r) for r in hi]) if hi else 0:,.0f}; "
              f"below: {len(g) - len(hi)}, median {st.median([views(r) for r in g if r not in hi]) if len(g) > len(hi) else 0:,.0f}")
        for col in ("lane", "fresh", "title_shape", "music", "captions"):
            vals = sorted({r.get(col, "") for r in g if r.get(col)})
            for v in vals:
                s = [r for r in g if r.get(col) == v]
                print(f"  {col:11} {v[:28]:28} n={len(s):2}  stayed {st.median([num(r['stayed_pct']) for r in s]):5.1f}  views {st.median([views(r) for r in s]):>8,.0f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    rows = merge()
    if a.report:
        report(rows)
