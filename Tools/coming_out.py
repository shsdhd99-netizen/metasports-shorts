"""What comes out when: one plain list on the Desktop, always current (Nov 7, 2026, owner request: "make sure i always know when videos are coming out").

Reads Research Notes/Scheduled Uploads.csv (every Short scheduled by script, private + publishAt) and the open slots in
Research Notes/Auto Queue.md, and writes:
  Desktop/MetaSports - COMING OUT.txt          (the list: today first, then the next 14 days, then open slots to fill)
  Research Notes/Coming Out.md                  (same list in the repo, so the cloud and every account see it)
Runs by itself after every `schedule_ready.py --go` and from the daily task; run it by hand any time:
  python Tools/coming_out.py            -> writes both files and prints the list
Read-only toward YouTube: it never calls the API.
"""
import csv, datetime, os, re, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ET = ZoneInfo("America/New_York")
CSV = os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv")
QUEUE = os.path.join(ROOT, "Research Notes", "Auto Queue.md")
CHAN = {"nba": "MetaSports (NBA)", "fc": "MetaSports FC (soccer)"}


def scheduled():
    out, seen = [], set()
    for r in csv.DictReader(open(CSV, encoding="utf-8")):
        try:
            t = datetime.datetime.strptime(r["publish_et"].strip(), "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        except Exception:
            continue
        if r["video_id"] in seen:
            continue
        seen.add(r["video_id"])
        out.append((t, r["channel"].strip(), r["title"].strip(), r["video_id"].strip()))
    return sorted(out)


def open_slots():
    if not os.path.exists(QUEUE):
        return []
    rows = []
    for line in open(QUEUE, encoding="utf-8"):
        m = re.match(r"\| (\w{3} \w{3} \d\d \d\d:\d\d [AP]M) \| \*\*(EMPTY|MOMENT|IDEA|BUILD[^*]*)\*\* \| ([^|]*)\|", line)
        if m:
            rows.append((m.group(1), m.group(2), m.group(3).strip()))
    return rows


def main():
    now = datetime.datetime.now(ET)
    items = scheduled()
    today = [x for x in items if x[0].date() == now.date()]
    nxt = [x for x in items if now.date() < x[0].date() <= (now + datetime.timedelta(days=14)).date()]
    fmt = lambda t: t.strftime("%a %b %d, %I:%M %p ET").replace(" 0", " ")

    def line(x):
        t, ch, title, vid = x
        state = "LIVE NOW" if t <= now else "goes live by itself"
        return f"  {fmt(t):<26} {CHAN.get(ch, ch):<24} {title}\n  {'':<26} https://youtu.be/{vid}  ({state})"

    L = [f"METASPORTS: WHAT COMES OUT WHEN   (updated {now.strftime('%a %b %d, %I:%M %p ET')})", "=" * 78, "",
         f"TODAY ({now.strftime('%a %b %d')}):"]
    L += [line(x) for x in today] or ["  nothing scheduled today"]
    L += ["", "NEXT 14 DAYS:"]
    L += [line(x) for x in nxt] or ["  nothing scheduled yet"]
    slots = open_slots()
    if slots:
        L += ["", "SLOTS STILL OPEN (from the Auto Queue; a builder fills these):"]
        L += [f"  {s:<22} {k:<10} {w}" for s, k, w in slots]
    L += ["", "Every Short above is uploaded PRIVATE with a publish time: it goes public by itself at that time.",
          "To stop one: delete it in the YouTube app before its time. Nothing is posted any other way."]
    text = "\n".join(L) + "\n"
    desk = os.path.join(os.path.expanduser("~"), "Desktop", "MetaSports - COMING OUT.txt")
    try:
        open(desk, "w", encoding="utf-8").write(text)
    except OSError:
        desk = None  # cloud / no Desktop
    open(os.path.join(ROOT, "Research Notes", "Coming Out.md"), "w", encoding="utf-8").write("```\n" + text + "```\n")
    print(text)
    if desk:
        print("written:", desk)


if __name__ == "__main__":
    main()
