r"""QA sweep (Nov 7, 2026; owner: "go more in depth with the tools, scoring, and the qa for everything").

  python Tools/qa_sweep.py            # QA every waiting draft (cached when nothing changed) + check every scheduled upload on YouTube
  python Tools/qa_sweep.py --fresh    # re-run qa_final on every waiting draft even if cached
  python Tools/qa_sweep.py --no-live  # skip the YouTube check (no API keys, e.g. a fresh cloud session)

1. DRAFTS: every production folder with a DRAFT*.mp4 that is not already on YouTube gets `qa_final.py` (cached in its qa_final.json unless the
   video, card, script or cuts changed since). Each gets its verdict (SHIP / FIX / HOLD), QA score (100 - 30 per FAIL - 4 per WARN), the lab's
   predicted score and the first problem to fix.
2. ON YOUTUBE: every upload in Scheduled Uploads.csv that goes live in the future (or went live in the last 48 h) is read back from the YouTube
   Data API (read-only, one call per channel) and checked: the video exists; the title is the card's title and not a placeholder ("unknown");
   it has tags; it is private with publishAt equal to the planned slot (scheduled) or public (live); and no second upload has the same title.
Writes Research Notes/QA Board.md. Read-only on YouTube: it never changes a video. Zero Claude credits.
"""
import argparse, csv, datetime, glob, json, os, re, subprocess, sys, urllib.parse
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RN = os.path.join(ROOT, "Research Notes")
sys.path.insert(0, HERE)
import schedule_ready as sr
import queue_rank as qr

ET = ZoneInfo("America/New_York")


def norm(t):
    return " ".join(re.findall(r"[a-z0-9']+", (t or "").lower()))


def newest_input(d):
    files = glob.glob(os.path.join(d, "DRAFT*.mp4")) + [os.path.join(d, x) for x in ("UPLOAD.md", "script.txt", "cuts.json", "shots.json", "sources.csv", "notes.md")]
    return max((os.path.getmtime(f) for f in files if os.path.exists(f)), default=0)


def drafts(fresh):
    posted = qr.posted_titles()
    out = []
    for ch, d in sr.candidates():
        if not glob.glob(os.path.join(d, "DRAFT*.mp4")):
            continue
        txt = open(os.path.join(d, "UPLOAD.md"), encoding="utf-8-sig").read()
        if re.search(r"LIVE ON YOUTUBE|^\s*#?\s*TRASH\b|\*\*Queue:\*\*\s*no", txt, re.I | re.M):
            continue
        try:
            title, _ = sr.ys.parse_card(os.path.join(d, "UPLOAD.md"))
        except Exception:
            title = ""
        if title and qr.already_posted([title], posted):
            continue
        cache = os.path.join(d, "qa_final.json")
        j = None
        if not fresh and os.path.exists(cache) and os.path.getmtime(cache) >= newest_input(d):
            try:
                j = json.load(open(cache, encoding="utf-8"))
            except Exception:
                j = None
        if j is None or "qa_score" not in j:
            subprocess.run([sys.executable, os.path.join(HERE, "qa_final.py"), d], capture_output=True, text=True, encoding="utf-8", errors="replace")
            try:
                j = json.load(open(cache, encoding="utf-8"))
            except Exception:
                j = {"verdict": "ERROR", "fails": 1, "warns": 0}
        first = (j.get("fail_list") or j.get("warn_list") or [""])[0]
        out.append(dict(ch=ch, dir=d, name=os.path.basename(d), title=title, **{k: j.get(k) for k in ("verdict", "qa_score", "predicted_score", "predicted_views", "fails", "warns")}, first=first))
    return out


def youtube_check():
    import yt_analytics as Y
    rows = list(csv.DictReader(open(os.path.join(RN, "Scheduled Uploads.csv"), encoding="utf-8")))
    now = datetime.datetime.now(ET)
    keep = []
    for r in rows:
        try:
            t = datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        except (KeyError, ValueError):
            continue
        if t >= now - datetime.timedelta(hours=48):
            keep.append((r, t))
    out = []
    for ch in ("nba", "fc"):
        mine = [(r, t) for r, t in keep if r["channel"] == ch]
        if not mine:
            continue
        if ch == "fc":
            Y.REFRESH_ENV = "YT_REFRESH_TOKEN_FC"; Y.TOKEN = Y.TOKEN.replace("yt_token.json", "yt_token_fc.json")
        else:
            Y.REFRESH_ENV = "YT_REFRESH_TOKEN"; Y.TOKEN = Y.TOKEN.replace("yt_token_fc.json", "yt_token.json")
        at = Y.access_token()
        ids = ",".join(r["video_id"] for r, _ in mine)
        items = {v["id"]: v for v in Y.get("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "snippet,status", "id": ids}), at).get("items", [])}
        titles = {}
        for v in items.values():
            titles.setdefault(norm(v["snippet"]["title"]), []).append(v["id"])
        for r, t in mine:
            v = items.get(r["video_id"])
            probs = []
            if not v and norm(r["title"]) in ("", "unknown"):
                probs.append("deleted placeholder upload (the Nov 5-6 duplicates): fine")
            elif not v:
                probs.append("FAIL video not found (deleted or wrong id)")
            else:
                yt_title = v["snippet"]["title"].strip()
                if norm(yt_title) in ("unknown", "untitled", "") or yt_title.lower().startswith("draft"):
                    probs.append(f"FAIL placeholder title {yt_title!r}")
                elif norm(yt_title) != norm(r["title"]):
                    probs.append(f"FAIL title on YouTube {yt_title[:50]!r} != planned {r['title'][:50]!r}")
                if len(v["snippet"].get("tags", [])) < 3:
                    probs.append(f"WARN only {len(v['snippet'].get('tags', []))} tags")
                stt = v["status"]
                pa = stt.get("publishAt")
                if t > now:
                    if stt.get("privacyStatus") != "private" or not pa:
                        probs.append(f"FAIL not scheduled: privacy {stt.get('privacyStatus')}, publishAt {pa}")
                    else:
                        pt = datetime.datetime.fromisoformat(pa.replace("Z", "+00:00")).astimezone(ET)
                        if abs((pt - t).total_seconds()) > 120:
                            probs.append(f"FAIL publishAt {pt:%a %b %d %H:%M} != planned {t:%a %b %d %H:%M}")
                elif stt.get("privacyStatus") != "public":
                    probs.append(f"WARN slot passed but privacy is {stt.get('privacyStatus')}")
                if len(titles.get(norm(yt_title), [])) > 1:
                    probs.append("FAIL two uploads with this title in the check window")
            out.append(dict(ch=ch, id=r["video_id"], when=t, title=r["title"], probs=probs))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--no-live", action="store_true")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    D = drafts(a.fresh)
    lines = [f"# QA board ({now:%a %b %d, %I:%M %p} ET)", "", "Auto-written by `python Tools/qa_sweep.py` (daily). SHIP = ready for its slot; FIX = 3+ warnings; HOLD = a FAIL (never scheduled).",
             "QA score = 100 - 30 per FAIL - 4 per WARN. Predicted = the lab's 0-100 premise score (50 = a typical Short for the channel).", "",
             "## Waiting drafts", "", "| Ch | Short | Verdict | QA | Predicted | Fix first |", "|---|---|---|---|---|---|"]
    for x in sorted(D, key=lambda x: ({"HOLD": 0, "ERROR": 0, "FIX": 1, "SHIP": 2}.get(x["verdict"], 3), x["ch"], -(x["predicted_score"] or 0))):
        lines.append(f"| {x['ch']} | {x['title'][:55] or x['name'][:55]} | **{x['verdict']}** | {x['qa_score'] if x['qa_score'] is not None else '-'} | "
                     f"{x['predicted_score'] if x['predicted_score'] is not None else '-'} | {(x['first'] or '-')[:110]} |")
    if not D:
        lines.append("| - | none waiting | | | | |")
    lines += ["", "## On YouTube (scheduled, or live in the last 48 h)", ""]
    if a.no_live:
        lines.append("- skipped (--no-live)")
    else:
        try:
            Y = youtube_check()
            lines += ["| Ch | When (ET) | Title | Check |", "|---|---|---|---|"]
            for y in sorted(Y, key=lambda y: y["when"]):
                lines.append(f"| {y['ch']} | {y['when']:%a %b %d %H:%M} | {y['title'][:55]} | {'; '.join(y['probs']) or 'OK'} |")
            bad = [y for y in Y if any(p.startswith('FAIL') for p in y['probs'])]
            print(f"qa_sweep: {len(Y)} uploads checked on YouTube, {len(bad)} with a FAIL")
        except Exception as e:
            lines.append(f"- not checked: {str(e)[:160]} (needs the YouTube keys: PC Tools/.env or this cloud session's environment)")
    open(os.path.join(RN, "QA Board.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"qa_sweep: {len(D)} waiting drafts ({sum(x['verdict']=='SHIP' for x in D)} SHIP, {sum(x['verdict']=='FIX' for x in D)} FIX, "
          f"{sum(x['verdict'] in ('HOLD','ERROR') for x in D)} HOLD) -> Research Notes/QA Board.md")


if __name__ == "__main__":
    main()
