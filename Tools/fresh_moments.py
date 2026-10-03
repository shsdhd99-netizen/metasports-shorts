"""Finds today's freshest NBA moments and storylines (free, no accounts).

Usage: python fresh_moments.py            -> prints + saves Tools/data/fresh_moments.md
Sources: newest Shorts from big NBA highlight channels (ranked by how hot they are vs. that
channel's normal; clips that aren't about the NBA are skipped) + Google News NBA headlines.
"""
import json, os, re, statistics, subprocess, sys, urllib.request, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CHANNELS = {"House of Highlights": "https://www.youtube.com/@HouseofHighlights/shorts",
            "NBA": "https://www.youtube.com/@NBA/shorts",
            "Bleacher Report": "https://www.youtube.com/@BleacherReport/shorts",
            "ClutchPoints": "https://www.youtube.com/@ClutchPoints/shorts"}
# Mixed-sport channels: keep a clip only if its title names the NBA, a team or a known player.
NBA_ANY_CASE = re.compile(
    r"\b(NBA|basketball|hoops?|dunk\w*|buzzer|triple.double|MVP|playoffs?|rookie|posteri[sz]ed|OKC|"
    r"Lakers|Celtics|Knicks|Warriors|Bucks|Nuggets|Mavs|Mavericks|Timberwolves|Cavs|Cavaliers|Clippers|"
    r"Pelicans|Grizzlies|Raptors|Spurs|Rockets|Hornets|Pistons|Pacers|Sixers|76ers|Blazers|Wizards|"
    r"LeBron|Bronny|Curry|Steph|Giannis|Luka|Doncic|Jokic|Embiid|Wemby|Wembanyama|SGA|Shai|Tatum|Jaylen|"
    r"Morant|Durant|Kyrie|Harden|Booker|Haliburton|Brunson|Lillard|Zion|Flagg|Banchero|Holmgren|Kawhi|"
    r"Westbrook|Draymond|Klay|Cade|Sabonis|Trae|LaMelo|Adebayo|Gobert|Porzingis|Siakam|Shaq|Kobe|Iverson)\b", re.I)
NBA_TEAM_CASED = re.compile(r"\b(Heat|Magic|Kings|Jazz|Suns|Nets|Thunder|Hawks|Bulls|Wolves|Finals)\b")


def is_nba(title):
    return bool(NBA_ANY_CASE.search(title) or NBA_TEAM_CASED.search(title))


def newest(url, n=20):
    r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", "--playlist-end", str(n), url],
                       capture_output=True, text=True, encoding="utf-8")
    try:
        return [e for e in (json.loads(r.stdout) or {}).get("entries") or [] if e]
    except json.JSONDecodeError:
        return []


def headlines(n=12):
    try:
        x = urllib.request.urlopen("https://news.google.com/rss/search?q=NBA&hl=en-US&gl=US&ceid=US:en", timeout=20).read().decode("utf-8", "ignore")
    except Exception:
        return []
    return [html.unescape(t) for t in re.findall(r"<item>.*?<title>(.*?)</title>", x, re.S)[:n]]


def main():
    rows = []
    for name, url in CHANNELS.items():
        ents = newest(url)
        views = [e.get("view_count") or 0 for e in ents if e.get("view_count")]
        if not views:
            continue
        med = statistics.median(views)
        for e in ents[:12]:
            title = e.get("title") or ""
            if name != "NBA" and not is_nba(title):
                continue
            v = e.get("view_count") or 0
            rows.append((v / med if med else 0, v, name, title, f"https://www.youtube.com/shorts/{e.get('id')}"))
    rows.sort(reverse=True)
    lines = [f"# Fresh NBA moments — {datetime.date.today()}\n",
             "## Hottest new NBA Shorts from big highlight channels (vs. their normal)\n",
             "| Heat | Views | Channel | Moment | Link |", "|---|---|---|---|---|"]
    for heat, v, name, title, link in rows[:15]:
        lines.append(f"| {heat:.1f}x | {v:,} | {name} | {title[:80].replace('|', '/')} | {link} |")
    lines += ["", "## Top NBA headlines right now (storyline ideas — verify before using)\n"]
    lines += [f"- {t.replace('|', '/')}" for t in headlines()]
    lines += ["", "**Next:** pick one → type `/nba-short the moment` in Claude (it runs the copy-check for you)."]
    out = "\n".join(lines)
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    open(os.path.join(HERE, "data", "fresh_moments.md"), "w", encoding="utf-8").write(out)
    sys.stdout.reconfigure(encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
