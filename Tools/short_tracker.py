"""Short tracker: one table of how every recent Short is doing, for the "MetaSports Shorts Tracker" dashboard (owner, Nov 7).

  python Tools/short_tracker.py              # writes Research Notes/Tracker/*.json and appends public views to the log
  python Tools/short_tracker.py --no-public  # skip yt-dlp (offline); uses the last logged public counts

Sources, newest wins:
- YouTube Analytics API pulls the PC commits each morning: `Research Notes/Studio exports/api/daily <date>.csv` (NBA) and
  `api FC/daily <date>.csv` (views, engaged views, avg % viewed, avg view s, subs, likes, shares) and `retention <date>.csv`
  (100-point curves). They run 2-3 days behind, so a new Short has public views first and API numbers later.
- Studio exports (`Content .../Table data.csv`): the only source of "Stayed to watch (%)". The API has no such metric; the
  API's engaged views / views is the daily stand-in (r = 0.63 with stayed over 20 Shorts, see Tools/yt_analytics.py).
- Public view counts now (yt-dlp, both channels' Shorts tabs), appended to `Research Notes/Tracker/public_views_log.csv`.
- `Research Notes/Scheduled Uploads.csv` for go-live times and what is still to come.

Verdict (only at 72 h+, the channel's rule): views vs the median of that channel's other Shorts 72 h+ old in this table:
"hit" 2x+, "ok" 0.5-2x, "flop" under 0.5x; younger is "too new".
"""
import argparse, csv, datetime as dt, glob, json, os, re, statistics, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EXP = os.path.join(ROOT, "Research Notes", "Studio exports")
OUT = os.path.join(ROOT, "Research Notes", "Tracker")
CHANNELS = {
    "nba": {"api": os.path.join(EXP, "api"), "shorts": "https://www.youtube.com/@MetaSportsClips/shorts", "name": "MetaSports (NBA)"},
    "fc": {"api": os.path.join(EXP, "api FC"), "shorts": "https://www.youtube.com/channel/UCIYlW84gYcChQtdys5L9pOg/shorts", "name": "MetaSports FC"},
}
ET = dt.timezone(dt.timedelta(hours=-5))  # EST; the posting grid is written in ET (DST ended Nov 1, 2026)


def num(x):
    try:
        return None if x in (None, "") else float(x)
    except ValueError:
        return None


def file_date(path):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
    return m.group(1) if m else ""


def api_rows(ch):
    """Every daily API file for the channel, oldest first: [(date, {video_id: row})]."""
    out = []
    for p in sorted(glob.glob(os.path.join(CHANNELS[ch]["api"], "daily *.csv")), key=file_date):
        with open(p, encoding="utf-8") as f:
            out.append((file_date(p), {r["video_id"]: r for r in csv.DictReader(f)}))
    return out


def retention(ch):
    files = sorted(glob.glob(os.path.join(CHANNELS[ch]["api"], "retention *.csv")), key=file_date)
    if not files:
        return {}
    curves = {}
    with open(files[-1], encoding="utf-8") as f:
        for r in csv.DictReader(f):
            curves.setdefault(r["video_id"], []).append((float(r["elapsed_ratio"]), float(r["audience_watch_ratio"])))
    return curves


def studio_stayed():
    """video_id -> (stayed %, export folder), newest export (by its end date) wins."""
    best = {}
    for p in glob.glob(os.path.join(EXP, "Content *", "Table data.csv")):
        folder = os.path.basename(os.path.dirname(p))
        end = (re.findall(r"\d{4}-\d{2}-\d{2}", folder) or [""])[-1]
        with open(p, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                s = num(r.get("Stayed to watch (%)"))
                vid = r.get("Content", "")
                if s is None or vid in ("", "Total"):
                    continue
                if vid not in best or end > best[vid][2]:
                    best[vid] = (s, folder, end)
    return {k: (v[0], v[1]) for k, v in best.items()}


def schedule():
    rows = {}
    p = os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows[r["video_id"]] = r
    return rows


def public_now(ch):
    r = subprocess.run(["yt-dlp", "--no-warnings", "--flat-playlist", "--print", "%(id)s\t%(view_count)s",
                        CHANNELS[ch]["shorts"]], capture_output=True, text=True, timeout=240)
    out = {}
    for line in r.stdout.splitlines():
        vid, _, v = line.partition("\t")
        if vid and v not in ("", "NA", "None"):
            out[vid] = int(float(v))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-public", action="store_true")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc)
    stamp = now.strftime("%Y-%m-%d %H:%M")
    log_path = os.path.join(OUT, "public_views_log.csv")
    log = []
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            log = list(csv.DictReader(f))
    pub = {}
    if not a.no_public:
        new = []
        for ch in CHANNELS:
            try:
                for vid, v in public_now(ch).items():
                    pub[vid] = v
                    new.append({"checked_utc": stamp, "channel": ch, "video_id": vid, "views": v})
            except Exception as e:  # yt-dlp blocked or slow: keep going on API data
                print(f"public counts for {ch} failed: {e}")
        if new:
            exists = os.path.exists(log_path)
            with open(log_path, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["checked_utc", "channel", "video_id", "views"])
                if not exists:
                    w.writeheader()
                w.writerows(new)
            log += [{k: str(v) for k, v in r.items()} for r in new]
    if not pub:  # last logged count per video
        for r in log:
            pub[r["video_id"]] = int(r["views"])

    sched, stayed = schedule(), studio_stayed()
    shorts, history, curves_out, upcoming = [], [], [], []
    for ch in CHANNELS:
        files = api_rows(ch)
        latest, meta = {}, {}
        for day, rows in files:
            for vid, r in rows.items():
                meta[vid] = r
                if num(r.get("views")) is not None:
                    latest[vid] = (day, r)
                    history.append({"video_id": vid, "channel": ch, "date": day, "views": int(num(r["views"])), "source": "api"})
        curves = retention(ch)
        for vid, r in meta.items():
            s = sched.get(vid)
            if s and s.get("publish_et"):
                live = dt.datetime.strptime(s["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET).astimezone(dt.timezone.utc)
            else:
                live = dt.datetime.strptime(r["published"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
            if live > now:
                continue  # scheduled, not live yet (listed under upcoming)
            age_h = (now - live).total_seconds() / 3600
            if pub and vid not in pub and r["title"].strip().lower() in ("", "unknown"):
                continue  # deleted or private upload
            day, lr = latest.get(vid, ("", {}))
            if lr and (not num(lr.get("views")) or (pub.get(vid) and num(lr["views"]) < 0.2 * pub[vid])):
                day, lr = "", {}  # the API hasn't caught up (it reports 0 for the newest Shorts)
            views_api, eng = num(lr.get("views")), num(lr.get("engagedViews"))
            st = stayed.get(vid)
            shorts.append({
                "video_id": vid, "channel": ch, "title": r["title"].strip(),
                "live_et": live.astimezone(ET).strftime("%Y-%m-%d %H:%M"), "age_hours": round(age_h, 1),
                "length_s": int(num(r.get("length_s")) or 0),
                "views": pub.get(vid, int(views_api) if views_api is not None else None),
                "api_views": int(views_api) if views_api is not None else None,
                "engaged_pct": round(100 * eng / views_api, 1) if eng is not None and views_api else None,
                "avg_viewed_pct": num(lr.get("averageViewPercentage")),
                "avg_view_s": num(lr.get("averageViewDuration")),
                "subs": int(num(lr.get("subscribersGained")) or 0) if lr else None,
                "likes": int(num(lr.get("likes")) or 0) if lr else None,
                "shares": int(num(lr.get("shares")) or 0) if lr else None,
                "stayed_pct": st[0] if st else None,
                "stayed_from": st[1] if st else "",
                "api_day": day,
                "url": f"https://youtube.com/shorts/{vid}",
            })
            for x, y in curves.get(vid, []):
                curves_out.append({"video_id": vid, "channel": ch, "elapsed_pct": round(100 * x), "watch_ratio": round(y, 3)})
    for r in log:
        history.append({"video_id": r["video_id"], "channel": r["channel"], "date": r["checked_utc"][:10],
                        "views": int(r["views"]), "source": "public"})
    keep = {s["video_id"] for s in shorts}
    history = [h for h in history if h["video_id"] in keep]
    # one point per video, day and source (the last of the day)
    hist = {}
    for h in history:
        hist[(h["video_id"], h["date"], h["source"])] = h
    history = sorted(hist.values(), key=lambda h: (h["video_id"], h["date"], h["source"]))

    for ch in CHANNELS:  # verdict at 72 h+
        mature = [s for s in shorts if s["channel"] == ch and s["age_hours"] >= 72 and s["views"] is not None]
        for s in (x for x in shorts if x["channel"] == ch):
            others = [m["views"] for m in mature if m["video_id"] != s["video_id"]]
            med = statistics.median(others) if others else None
            s["vs_median"] = round(s["views"] / med, 2) if med and s["views"] is not None else None
            if s["age_hours"] < 72 or s["vs_median"] is None:
                s["verdict"] = "too new" if s["age_hours"] < 72 else "no data"
            else:
                s["verdict"] = "hit" if s["vs_median"] >= 2 else ("flop" if s["vs_median"] < 0.5 else "ok")
    shorts.sort(key=lambda s: s["live_et"], reverse=True)

    for vid, s in sched.items():
        if not s.get("publish_et"):
            continue
        t = dt.datetime.strptime(s["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        if t.astimezone(dt.timezone.utc) > now:
            upcoming.append({"video_id": vid, "channel": s["channel"], "live_et": s["publish_et"], "title": s["title"].strip()})
    upcoming.sort(key=lambda u: u["live_et"])

    for name, rows in (("shorts", shorts), ("history", history), ("retention", curves_out), ("upcoming", upcoming)):
        with open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
    print(f"tracker {stamp} UTC: {len(shorts)} Shorts, {len(history)} history points, {len(curves_out)} curve points, "
          f"{len(upcoming)} upcoming, {sum(1 for s in shorts if s['stayed_pct'] is not None)} with Studio stayed %")


if __name__ == "__main__":
    main()
