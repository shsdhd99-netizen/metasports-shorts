"""Title audit (Nov 5, 2026): every video in Research Notes/Scheduled Uploads.csv must carry the title we scheduled.

  python Tools/title_audit.py            (load Tools/.env first so the read-only YouTube tokens are set)

Reads each channel's videos back through the read-only YouTube Data API (the analytics token has youtube.readonly) and flags: an empty/"unknown"/
"untitled" title, or a title different from the CSV. state.py runs it and lists problems under "Needs attention". Cause it guards against: two FC Shorts went
out titled "unknown" on Nov 1 because the soccer card format had no `**Title:**` line (parse_card now reads the H1, and yt_schedule refuses placeholder titles).
"""
import csv, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_analytics as Y
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD = {"", "unknown", "untitled", "none"}


def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv"), encoding="utf-8")))
    bad = []
    for ch in ("nba", "fc"):
        if ch == "fc":
            Y.REFRESH_ENV = "YT_REFRESH_TOKEN_FC"; Y.TOKEN = Y.TOKEN.replace("yt_token.json", "yt_token_fc.json")
        try:
            at = Y.access_token()
        except SystemExit as e:
            print(f"{ch}: no token ({e})"); continue
        mine = [r for r in rows if r["channel"] == ch]
        for i in range(0, len(mine), 40):
            chunk = mine[i:i + 40]
            url = "https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "snippet,status", "id": ",".join(r["video_id"] for r in chunk)})
            have = {v["id"]: v for v in Y.get(url, at).get("items", [])}
            for r in chunk:
                v = have.get(r["video_id"])
                if not v:
                    bad.append(f"{ch} {r['video_id']}: not found (deleted or not visible)"); continue
                t = v["snippet"]["title"].strip()
                if t.lower() in BAD or (r["title"].strip() and t != r["title"].strip()):
                    bad.append(f"{ch} {r['video_id']} ({v['status'].get('privacyStatus')}): title on YouTube {t!r}, scheduled as {r['title']!r}")
    print("\n".join(bad) if bad else "title_audit: all titles match")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
