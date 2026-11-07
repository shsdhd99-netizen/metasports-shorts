r"""ESPN highlight clips by game, in two commands (Nov 7, 2026; efficiency review: footage hunting was the biggest time sink).

  python Tools/espn_clip.py games  [--league nba] [--date 20261106] [--team LAL]      # games that day, with event ids
  python Tools/espn_clip.py clips  [--league nba] (--event 401909294 | --date D --team LAL) [--find luka]
                                                                                       # that game's ESPN clips: id, seconds, headline
  python Tools/espn_clip.py get    <clip id> [<clip id> ...] --folder "<Short folder>" [--name luka53]
                                                                                       # HD mp4 into <folder>/src/, plus a .url sidecar

`get` saves src/espn_<id>.mp4 (or src/<name>.mp4) and src/<file>.mp4.url with the clip's ESPN page link, so cut_list.py fills
sources.csv by itself (no hand patching: #99 had every row hand-set to one link). It prints the resolution and length to put in
cuts.json "sources". Leagues: nba, wnba, epl (eng.1), ucl (uefa.champions), laliga (esp.1), mls (usa.1), or any "sport/league" path.
Uses ESPN's public JSON (site.api.espn.com, api-app.espn.com) and the clip's own HD file. Read-only; never uploads anything.
Footage rule stays: every clip is watched (cut_list contact sheet) and verified against its line before QA.
"""
import argparse, datetime, json, os, subprocess, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
LEAGUES = {"nba": "basketball/nba", "wnba": "basketball/wnba", "epl": "soccer/eng.1", "ucl": "soccer/uefa.champions",
           "laliga": "soccer/esp.1", "seriea": "soccer/ita.1", "bundesliga": "soccer/ger.1", "mls": "soccer/usa.1",
           "worldcup": "soccer/fifa.world"}
UA = {"User-Agent": "Mozilla/5.0 (metasports-tools)"}


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.load(r)


def path(league):
    return LEAGUES.get(league, league)


def games(league, date, team=None):
    j = get_json(f"https://site.api.espn.com/apis/site/v2/sports/{path(league)}/scoreboard" + (f"?dates={date}" if date else ""))
    out = []
    for e in j.get("events", []):
        abbr = [c.get("team", {}).get("abbreviation", "") for c in e.get("competitions", [{}])[0].get("competitors", [])]
        if team and team.upper() not in [x.upper() for x in abbr] and team.lower() not in e.get("name", "").lower():
            continue
        out.append((e["id"], e.get("shortName", e.get("name", "")), e.get("status", {}).get("type", {}).get("description", "")))
    return out


def clips(league, event):
    j = get_json(f"https://site.api.espn.com/apis/site/v2/sports/{path(league)}/summary?event={event}")
    return [(v.get("id"), v.get("duration"), v.get("headline", "")) for v in j.get("videos", [])]


def clip_info(cid):
    v = (get_json(f"https://api-app.espn.com/v1/video/clips/{cid}").get("videos") or [{}])[0]
    src = v.get("links", {}).get("source", {})
    href = (src.get("HD") or {}).get("href") or src.get("href")
    return v.get("headline", ""), v.get("duration"), href, v.get("originalPublishDate", "")


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", p],
                       capture_output=True, text=True)
    try:
        j = json.loads(r.stdout)
        return f"{j['streams'][0]['width']}x{j['streams'][0]['height']}, {float(j['format']['duration']):.1f} s"
    except Exception:
        return "could not probe"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["games", "clips", "get"])
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--league", default="nba")
    ap.add_argument("--date", help="YYYYMMDD (ET game date); default today's scoreboard")
    ap.add_argument("--team")
    ap.add_argument("--event")
    ap.add_argument("--find", help="only clips whose headline contains this (case-insensitive)")
    ap.add_argument("--folder")
    ap.add_argument("--name", help="file name for a single clip (default espn_<id>)")
    a = ap.parse_args()
    if a.cmd == "games":
        for g in games(a.league, a.date, a.team):
            print(f"{g[0]}  {g[1]:16} {g[2]}")
        return
    if a.cmd == "clips":
        evs = [a.event] if a.event else [g[0] for g in games(a.league, a.date, a.team)]
        if not evs:
            raise SystemExit("no game found (try --date YYYYMMDD and --team ABC)")
        for ev in evs:
            print(f"== event {ev}")
            for cid, dur, head in clips(a.league, ev):
                if a.find and a.find.lower() not in head.lower():
                    continue
                print(f"  {cid}  {dur or '?':>3} s  {head}")
        return
    if not a.folder or not a.ids:
        raise SystemExit("get needs clip id(s) and --folder")
    os.makedirs(os.path.join(a.folder, "src"), exist_ok=True)
    for cid in a.ids:
        head, dur, href, when = clip_info(cid)
        if not href:
            print(f"  {cid}: no downloadable file in the ESPN feed")
            continue
        name = a.name if (a.name and len(a.ids) == 1) else f"espn_{cid}"
        out = os.path.join(a.folder, "src", name + ".mp4")
        if not os.path.exists(out):
            with urllib.request.urlopen(urllib.request.Request(href, headers=UA), timeout=120) as r, open(out, "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
        open(out + ".url", "w", encoding="utf-8").write(f"https://www.espn.com/video/clip/_/id/{cid}\n")
        print(f"  src/{name}.mp4  {probe(out)}  ({when[:10]}) {head}")


if __name__ == "__main__":
    main()
