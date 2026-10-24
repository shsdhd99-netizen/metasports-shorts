"""Find and download official NBA team-site clips (NBA.com) at 1280x720, no account, works from the cloud.

  python Tools/nba_videos.py search --player 201935 --q "step back"            # Harden clips on every team site
  python Tools/nba_videos.py search --team 1610612752 --q harden --grep block  # Knicks site: titles with 'block'
  python Tools/nba_videos.py search --team 1610612741 --game 0022401063        # Bulls site clips from one game
  python Tools/nba_videos.py get "<1280x720 mp4 url>" --out src/clip.mp4

How it works: NBA.com's public content index (content-api-prod.nba.com, the one the team sites read) lists each team
site's videos with direct cdn.nba.com MP4s (320/960/1280 wide). League videos (nba.com/watch) are not in it as files.
IDs: team ids 1610612737-1610612766 (e.g. Lakers 1610612747, Rockets 1610612745, Knicks 1610612752); player ids are
NBA.com person ids (LeBron 2544, Curry 201939, Harden 201935); game ids like 0022401063 (season 2024-25, game 1063).
Per-play clips ("Harden Step-Back", "Robinson denies Harden from three") are the gold: close replays, often the miss
or block that highlight packages skip. Always watch the frames before using a clip (player, jersey, date).
Found Oct 19, 2026 for #48 (Harden) when YouTube was blocked in the cloud.
"""
import argparse, json, re, subprocess, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://content-api-prod.nba.com/public/1"
TEAMS = range(1610612737, 1610612767)


def fetch(path, **params):
    q = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    req = urllib.request.Request(f"{API}/{path}?{q}", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("results", {})
    except Exception as e:  # one team site failing should not stop the search
        print(f"  ({path}: {e})", file=sys.stderr)
        return {}


def best_mp4(item):
    va = item.get("videoAssets") or {}
    for k in ("1280", "960", "320"):
        if isinstance(va.get(k), dict) and va[k].get("video"):
            return va[k]["video"]
    return None


def search(a):
    teams = [a.team] if a.team else list(TEAMS)

    def one(t):
        out = []
        for page in range(1, a.pages + 1):
            res = fetch(f"teams/{t}/content", types="video", count=100, page=page, players=a.player, games=a.game, q=a.q)
            items = res.get("items", [])
            out += [(t, i) for i in items]
            if len(items) < 100:
                break
        return out

    with ThreadPoolExecutor(8) as ex:
        rows = [r for chunk in ex.map(one, teams) for r in chunk]
    seen, hits = set(), []
    for t, i in rows:
        url = best_mp4(i)
        if not url or i["id"] in seen:
            continue
        if a.grep and not re.search(a.grep, i["title"], re.I):
            continue
        if a.max_len and i.get("videoDurationSeconds", 0) > a.max_len:
            continue
        seen.add(i["id"])
        hits.append({"team": t, "date": i["date"][:10], "secs": i.get("videoDurationSeconds"), "title": i["title"],
                     "page": i.get("permalink"), "mp4": url})
    hits.sort(key=lambda h: h["date"])
    if a.json:
        print(json.dumps(hits, indent=1))
    else:
        for h in hits:
            print(f"{h['date']}  {h['secs']:>4}s  {h['title'][:80]}\n      {h['mp4']}")
        print(f"{len(hits)} clip(s)")


def get(a):
    r = subprocess.run(["curl", "-s", "-f", "-o", a.out, a.url])
    if r.returncode:
        raise SystemExit(f"download failed: {a.url}")
    info = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height:format=duration", "-of", "csv=p=0", a.out],
                          capture_output=True, text=True).stdout.split()
    print(a.out, " ".join(info))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("--team", type=int, help="one team id (default: all 30 team sites)")
    s.add_argument("--player", help="NBA.com person id")
    s.add_argument("--game", help="game id, e.g. 0022401063")
    s.add_argument("--q", help="text search")
    s.add_argument("--grep", help="regex the title must match")
    s.add_argument("--max-len", dest="max_len", type=int, default=0, help="only clips up to this many seconds")
    s.add_argument("--pages", type=int, default=3, help="pages of 100 per team site")
    s.add_argument("--json", action="store_true")
    g = sub.add_parser("get")
    g.add_argument("url")
    g.add_argument("--out", required=True)
    a = ap.parse_args()
    {"search": search, "get": get}[a.cmd](a)


if __name__ == "__main__":
    main()
