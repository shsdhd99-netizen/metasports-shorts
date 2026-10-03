"""Weekly MetaSports check (free). Compares your newest Shorts to your normal and logs it.

Usage: python channel_check.py [channel handle, default @MetaSportsClips]
Saves: Tools/data/channel_log.csv (one row per run) + prints a plain-English summary.
"""
import csv, datetime, json, os, statistics, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def info(video_id):
    """Full details for one Short -> (dict, error text). Age-restricted Shorts fail with an age error."""
    r = subprocess.run(["yt-dlp", "-j", "--skip-download", "--no-warnings", f"https://www.youtube.com/shorts/{video_id}"],
                       capture_output=True, text=True, encoding="utf-8")
    try:
        return json.loads(r.stdout), ""
    except json.JSONDecodeError:
        return {}, (r.stderr or "").lower()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    handle = sys.argv[1] if len(sys.argv) > 1 else "@MetaSportsClips"
    flat = json.loads(subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", f"https://www.youtube.com/{handle}/shorts"],
                                     capture_output=True, text=True, encoding="utf-8").stdout or "{}")
    ents = [e for e in flat.get("entries") or [] if e]
    if not ents:
        raise SystemExit("Couldn't read the channel (check the handle or your internet).")
    subs = flat.get("channel_follower_count") or 0
    views = [e.get("view_count") or 0 for e in ents]
    recent = ents[:7]
    med_old = statistics.median(views[7:37] or views)
    print(f"{flat.get('channel')} · {subs:,} subs · {len(ents)} Shorts\n")

    newest, _ = info(ents[0]["id"])
    days = None
    if newest.get("upload_date"):
        days = (datetime.date.today() - datetime.datetime.strptime(newest["upload_date"], "%Y%m%d").date()).days
        print(f"Last upload: {days} day(s) ago" + ("  -> post today; after a long break YouTube re-tests you from scratch" if days > 3 else ""))
    too_new = {ents[0]["id"]} if days is not None and days < 2 else set()
    med_new = statistics.median([e.get("view_count") or 0 for e in recent if e["id"] not in too_new] or [0])
    print(f"Last 7 Shorts median: {int(med_new):,} views  (your normal before that: {int(med_old):,})")
    trend = "UP" if med_new > med_old * 1.2 else ("DOWN" if med_new < med_old * 0.8 else "FLAT")
    print(f"Trend: {trend}\n")
    ranked = sorted(recent, key=lambda e: e.get("view_count") or 0, reverse=True)
    print("Your last 7 Shorts, best → worst:")
    for e in ranked:
        v = e.get("view_count") or 0
        if e["id"] in too_new:
            tag = "too new - judge it after 48h"
        elif v >= 2 * med_old:
            tag = "WINNER - make a follow-up"
        elif v < 0.1 * med_old:
            d, err = info(e["id"])
            if d.get("age_limit") or "confirm your age" in err or "age-restricted" in err or "inappropriate" in err:
                tag = "FLOP - age-restricted; YouTube barely shows these (skip fights/injuries)"
            else:
                tag = "FLOP - open it in YouTube Studio: look for a copyright claim or restriction"
        else:
            tag = "above normal" if v > med_old else ""
        print(f"  {v:>10,}  {(e.get('title') or '')[:60]}  {tag}")
    log = os.path.join(HERE, "data", "channel_log.csv")
    os.makedirs(os.path.dirname(log), exist_ok=True)
    new = not os.path.exists(log)
    with open(log, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "subs", "shorts", "last_upload_days", "median_last7", "median_before", "trend", "best_title", "best_views"])
        w.writerow([datetime.date.today(), subs, len(ents), days, int(med_new), int(med_old), trend,
                    ranked[0].get("title"), ranked[0].get("view_count")])
    print(f"\nLogged to {log}")


if __name__ == "__main__":
    main()
