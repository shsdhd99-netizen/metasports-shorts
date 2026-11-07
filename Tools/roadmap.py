r"""Roadmap auto-update (Nov 7, 2026; owner: "always update roadmap, etc.").

  python Tools/roadmap.py            # refresh the LIVE STATUS block at the top of "Roadmap - Next 90 Days.md" (+ channel_daily files)
  python Tools/roadmap.py --no-api   # use the newest channel_daily files already in the repo (no YouTube keys)

The block (between <!-- AUTO:STATUS --> and <!-- /AUTO:STATUS -->) is rewritten every run; everything below it is history and stays.
It shows, per channel: subscribers now and per day (28 days), Shorts views per day (7-day and 28-day), the last-90-day total against the
money lines (3M lower tier, 10M Partner Program, 20M for new applicants from Feb 1, 2027) with the date each is reached at the current pace;
then this week's auto queue (Research Notes/Auto Queue.md), the live lab tests (Research Notes/Lab/Scoreboard.md), rules flagged by the
lab's Rule check, and the QA board. Read-only on YouTube (Analytics + Data API "mine" reads). Zero Claude credits.
Also writes `Research Notes/Studio exports/api[ FC]/channel_daily <date>.csv` so state.py and weekly_review.py have fresh numbers.
"""
import argparse, csv, datetime, glob, json, os, re, sys, urllib.parse
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RN = os.path.join(ROOT, "Research Notes")
ET = ZoneInfo("America/New_York")
ROAD = os.path.join(ROOT, "Roadmap - Next 90 Days.md")
SUB = {"nba": "api", "fc": "api FC"}
sys.path.insert(0, HERE)


def pull(ch, today):
    import yt_analytics as Y
    Y.REFRESH_ENV = "YT_REFRESH_TOKEN_FC" if ch == "fc" else "YT_REFRESH_TOKEN"
    if ch == "fc":
        Y.TOKEN = Y.TOKEN.replace("yt_token.json", "yt_token_fc.json")
    else:
        Y.TOKEN = Y.TOKEN.replace("yt_token_fc.json", "yt_token.json")
    at = Y.access_token()
    start = (today - datetime.timedelta(days=364)).isoformat()
    p = {"ids": "channel==MINE", "startDate": start, "endDate": today.isoformat(), "dimensions": "day", "sort": "day",
         "metrics": "views,estimatedMinutesWatched,subscribersGained,subscribersLost,averageViewPercentage"}
    res = Y.get("https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode(p), at)
    cols = [h["name"] for h in res.get("columnHeaders", [])]
    rows = [dict(zip(cols, r)) for r in res.get("rows", [])]
    out = os.path.join(RN, "Studio exports", SUB[ch], f"channel_daily {today.isoformat()}.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["day", "views", "estimatedMinutesWatched", "subscribersGained", "subscribersLost", "averageViewPercentage"])
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in w.fieldnames})
    stats = Y.get("https://www.googleapis.com/youtube/v3/channels?" + urllib.parse.urlencode({"part": "statistics", "mine": "true"}), at).get("items", [{}])[0].get("statistics", {})
    json.dump(dict(subs=int(stats.get("subscriberCount", 0) or 0), videos=int(stats.get("videoCount", 0) or 0), at=today.isoformat()),
              open(os.path.join(RN, "Lab", f"channel_{ch}.json"), "w"), indent=1)


def load(ch):
    files = sorted(glob.glob(os.path.join(RN, "Studio exports", SUB[ch], "channel_daily *.csv")))
    rows = list(csv.DictReader(open(files[-1], encoding="utf-8"))) if files else []
    for r in rows:
        r["views"] = float(r["views"] or 0)
        r["net"] = float(r["subscribersGained"] or 0) - float(r["subscribersLost"] or 0)
    sp = os.path.join(RN, "Lab", f"channel_{ch}.json")
    subs = json.load(open(sp)) if os.path.exists(sp) else {}
    return rows, subs, (os.path.basename(files[-1])[14:24] if files else "none")


def eta(have, need, per_day, today):
    if have >= need:
        return "reached"
    if per_day <= 0:
        return "not at this pace"
    d = (need - have) / per_day
    return f"{today + datetime.timedelta(days=round(d)):%b %d, %Y}" if d < 730 else "over 2 years at this pace"


def channel_block(ch, today):
    rows, subs, asof = load(ch)
    name = "MetaSports (NBA)" if ch == "nba" else "MetaSports FC"
    if not rows:
        return [f"### {name}", "", "- no channel_daily file yet (run `python Tools/roadmap.py` with the YouTube keys)", ""]
    # the API runs ~2 days behind: drop trailing zero days
    while rows and rows[-1]["views"] == 0:
        rows.pop()
    last = rows[-1]["day"]
    v7 = sum(r["views"] for r in rows[-7:]) / 7
    v28 = sum(r["views"] for r in rows[-28:]) / 28
    v90 = sum(r["views"] for r in rows[-90:])
    s28 = sum(r["net"] for r in rows[-28:]) / 28
    n_subs = subs.get("subs")
    L = [f"### {name} (data to {last})", "",
         "| Now | |", "|---|---|",
         f"| Subscribers | {n_subs if n_subs is not None else '-'} (+{s28:.1f} a day, 28-day average) |",
         f"| Views a day | {v7:,.0f} (7-day) vs {v28:,.0f} (28-day): {'up' if v7 >= v28 else 'down'} {abs(v7 / v28 - 1) * 100 if v28 else 0:.0f}% |",
         f"| Views, last 90 days | {v90:,.0f} |", "",
         "| Milestone | Needs | Now | Reached at today's pace (7-day) |", "|---|---|---|---|"]
    if n_subs is not None:
        for target in (500, 1000):
            L.append(f"| {target:,} subscribers | {target:,} | {n_subs:,} | {eta(n_subs, target, s28, today)} |")
    for label, need in (("Fan funding (3M Shorts views / 90 days)", 3e6), ("Partner Program today (10M / 90 days)", 10e6), ("New applicants from Feb 1, 2027 (20M / 90 days)", 20e6)):
        per = need / 90
        L.append(f"| {label} | {per:,.0f} a day | {v7:,.0f} a day ({v7 / per * 100:.0f}%) | {'on pace' if v7 >= per else f'needs {per / v7:.1f}x the current pace' if v7 else '-'} |")
    return L + [""]


def section(path, start, stop=None, maxlines=40):
    if not os.path.exists(path):
        return []
    t = open(path, encoding="utf-8").read().splitlines()
    try:
        i = next(k for k, l in enumerate(t) if l.startswith(start))
    except StopIteration:
        return []
    out = []
    for l in t[i + 1:]:
        if stop and l.startswith(stop):
            break
        out.append(l)
    return out[:maxlines]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-api", action="store_true")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    today = now.date()
    if not a.no_api:
        for ch in ("nba", "fc"):
            try:
                pull(ch, today)
            except Exception as e:
                print(f"roadmap: {ch} API pull skipped ({str(e)[:120]}); using the newest file in the repo")
    B = ["<!-- AUTO:STATUS -->", f"## LIVE STATUS (auto, {now:%a %b %d, %I:%M %p} ET; `python Tools/roadmap.py` rewrites this block daily)", "",
         "The plan below it is history (Sep 2026). What runs the channels now: THE RULES (Nov 7) in `MetaSports - Playbook.md`, "
         "the auto queue (`Research Notes/Auto Queue.md`), the lab (`Research Notes/Lab/Scoreboard.md`) and the QA board (`Research Notes/QA Board.md`).", ""]
    for ch in ("nba", "fc"):
        B += channel_block(ch, today)
    # this week
    qp = os.path.join(RN, "Lab", "queue.json")
    if os.path.exists(qp):
        q = json.load(open(qp, encoding="utf-8"))
        B += ["### The next 7 days (auto queue)", "", "| Slot (ET) | Ch | What | Short | Score |", "|---|---|---|---|---|"]
        for s in q["slots"]:
            t = datetime.datetime.fromisoformat(s["slot"])
            B.append(f"| {t:%a %b %d %I:%M %p} | {s['ch']} | {s['kind']} | {(s.get('title') or '-')[:55]} | {s['score'] if s.get('score') is not None else '-'} |")
        if q.get("holds"):
            B += ["", "Held by QA: " + "; ".join(f"{h['title'][:40]} ({h['fix'][:60]})" for h in q["holds"][:5])]
        B.append("")
    # tests
    sb = section(os.path.join(RN, "Lab", "Scoreboard.md"), "| Test |", "## Shorts in each", 12)
    if sb:
        B += ["### Live tests (the lab scores them daily)", "", "| Test |" + sb[0].split("| Test |", 1)[-1] if sb[0].startswith("| Test") else "| Test | Question | A | B | Score | p | Avg % | Status | Next |"] + sb + [""]
    dec = os.path.join(RN, "Lab", "Decisions.md")
    if os.path.exists(dec):
        B += ["Decided: " + "; ".join(l.strip("- \n")[:120] for l in open(dec, encoding="utf-8").readlines()[-3:]), ""]
    # rule flags
    studies = sorted(glob.glob(os.path.join(RN, "Lab", "Study - all (*).md")))
    if studies:
        rc = [l for l in section(studies[-1], "## Rule check", "## How good", 60) if re.search(r"AGAINST|REVISIT", l)]
        B += ["### Rules the data questions (fixed or dropped on Sunday)", ""] + ([f"- {l.split('|')[1].strip()} ({l.split('|')[3].strip()}): {l.split('|')[-2].strip()}" for l in rc] or ["- none"]) + [""]
    qa = section(os.path.join(RN, "QA Board.md"), "## Waiting drafts", "## On YouTube", 20)
    holds = [l for l in qa if "HOLD" in l]
    yt = [l for l in section(os.path.join(RN, "QA Board.md"), "## On YouTube", None, 40) if "FAIL" in l]
    B += ["### QA", "", f"- Waiting drafts: {sum(1 for l in qa if l.startswith('| ') and 'SHIP' in l)} SHIP, {sum(1 for l in qa if 'FIX**' in l)} FIX, {len(holds)} HOLD (see `Research Notes/QA Board.md`).",
          f"- On YouTube: {len(yt)} upload(s) with a FAIL." + (" " + "; ".join(l.split('|')[3].strip()[:40] for l in yt[:3]) if yt else ""), "", "<!-- /AUTO:STATUS -->", ""]
    text = open(ROAD, encoding="utf-8").read() if os.path.exists(ROAD) else ""
    if "<!-- AUTO:STATUS -->" in text:
        text = re.sub(r"<!-- AUTO:STATUS -->.*?<!-- /AUTO:STATUS -->\n?", "\n".join(B), text, flags=re.S)
    else:
        text = re.sub(r"^> \*\*HISTORICAL \(Sep 2026\)\.\*\*[^\n]*\n", "", text)
        text = "\n".join(B) + "\n" + text
    open(ROAD, "w", encoding="utf-8").write(text)
    print(f"roadmap: LIVE STATUS block refreshed in {os.path.basename(ROAD)}")


if __name__ == "__main__":
    main()
