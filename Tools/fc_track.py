"""Track MetaSports FC from public data (yt-dlp, no login, no cookies). Owner, Oct 22: "start tracking the channel now".
  python Tools/fc_track.py            # prints every Short with views/likes/comments and appends a row per Short to the log
Log: Soccer Channel/Data/fc_channel_log.csv (checked_utc, video_id, title, published_utc, hours_live, views, likes, comments, subs).
Read it with the Outcome Log rule: judge a Short at 3+ days, not day 1.
"""
import csv, datetime as dt, json, os, subprocess, sys

CH = "UCIYlW84gYcChQtdys5L9pOg"
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Soccer Channel", "Data", "fc_channel_log.csv")


def ytdlp(*args):
    r = subprocess.run(["yt-dlp", "--no-warnings", "-J", *args], capture_output=True, text=True, timeout=180)
    return json.loads(r.stdout) if r.stdout.strip() else {}


def main():
    now = dt.datetime.now(dt.timezone.utc)
    ch = ytdlp("--flat-playlist", f"https://www.youtube.com/channel/{CH}/shorts")
    subs = ch.get("channel_follower_count")
    rows = []
    for e in ch.get("entries", []):
        v = ytdlp("--skip-download", f"https://www.youtube.com/shorts/{e['id']}")
        ts = v.get("timestamp")
        pub = dt.datetime.fromtimestamp(ts, dt.timezone.utc) if ts else None
        rows.append({"checked_utc": now.strftime("%Y-%m-%d %H:%M"), "video_id": e["id"], "title": v.get("title") or e.get("title"),
                     "published_utc": pub.strftime("%Y-%m-%d %H:%M") if pub else "",
                     "hours_live": round((now - pub).total_seconds() / 3600, 1) if pub else "",
                     "views": v.get("view_count", e.get("view_count")), "likes": v.get("like_count"),
                     "comments": v.get("comment_count"), "subs": subs})
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["checked_utc"])
        if new: w.writeheader()
        for r in rows: w.writerow(r)
    print(f"MetaSports FC: {subs} subs, {len(rows)} Shorts ({now:%Y-%m-%d %H:%M} UTC)")
    for r in rows:
        print(f"  {r['views']:>8} views  {r['likes']} likes  {r['comments']} comments  {r['hours_live']} h live  | {r['title']}")


if __name__ == "__main__":
    sys.exit(main())
