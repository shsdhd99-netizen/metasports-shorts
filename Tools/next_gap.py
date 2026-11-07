"""Find the next posting slot that has NOTHING ready, per channel (Nov 3, 2026; zero Claude credits).

  python Tools/next_gap.py nba|fc [--hours 54] [--min-lead 8]

A slot counts as covered when either (a) Research Notes/Scheduled Uploads.csv has an upload for that channel at that time, or
(b) a production folder has an UPLOAD.md whose slot is that time AND at least one DRAFT*.mp4 (built, even if on HOLD or waiting
for an arm choice: it only needs the owner, not a new build). Slot grid (UPLOAD SCHEDULE.md): NBA 7:15 AM and 3:30 PM ET, FC 12:00 PM ET.
Prints `GAP <channel> <YYYY-MM-DD HH:MM> ET` for the first uncovered slot between now+min-lead hours and now+hours, or `NO GAP`.
Exit code 0 = gap found, 3 = no gap. run_daily.ps1 uses it so the PC builds only what the cloud left open.
"""
import argparse, csv, datetime, glob, os, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import schedule_ready as sr  # slot parser and folder list (same rules as the scheduler)

ET = ZoneInfo("America/New_York")
GRID = {"nba": [(7, 15), (15, 30)], "fc": [(12, 0)]}
# Nov 5, 2026 posting TEST (Research Notes/Posting Plan (Nov 5, 2026).md): while Research Notes/POSTING_TEST.txt exists, days alternate so the
# ElevenLabs budget stays the same: EVEN dates NBA 2 + FC 1 (the old grid), ODD dates NBA 1 + FC 2 (FC at 12:00 and 18:00 ET). A slot is only
# filled when an idea passes Tools/build_gate.py; an unfilled slot is simply skipped (skipping beats a weak Short).
TEST_ODD = {"nba": [(7, 15)], "fc": [(12, 0), (18, 0)]}


def grid_for(ch, date):
    if os.path.exists(os.path.join(ROOT, "Research Notes", "POSTING_TEST.txt")) and date >= datetime.date(2026, 11, 9) and date.toordinal() % 2 == 1:
        return TEST_ODD[ch]
    return GRID[ch]


def covered(ch, now):
    out = set()
    log = os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv")
    if os.path.exists(log):
        for r in csv.DictReader(open(log, encoding="utf-8")):
            if r.get("channel") == ch and r.get("publish_et"):
                out.add(r["publish_et"].strip()[:16])
    for c, d in sr.candidates():
        if c != ch or not glob.glob(os.path.join(d, "DRAFT*.mp4")):
            continue
        slot = sr.slot_of(open(os.path.join(d, "UPLOAD.md"), encoding="utf-8-sig").read(), now.year)
        if slot:
            out.add(f"{slot:%Y-%m-%d %H:%M}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", choices=["nba", "fc"])
    ap.add_argument("--hours", type=float, default=54)
    ap.add_argument("--min-lead", type=float, default=8, help="a build takes 1-3 h and the owner needs time to look")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    have = covered(a.channel, now)
    day = now.date()
    for i in range(4):
        for h, m in grid_for(a.channel, day + datetime.timedelta(days=i)):
            t = datetime.datetime.combine(day + datetime.timedelta(days=i), datetime.time(h, m), tzinfo=ET)
            if now + datetime.timedelta(hours=a.min_lead) <= t <= now + datetime.timedelta(hours=a.hours):
                if f"{t:%Y-%m-%d %H:%M}" not in have:
                    print(f"GAP {a.channel} {t:%Y-%m-%d %H:%M} ET ({t:%a %b} {t.day}, {t:%I:%M %p} ET)")
                    return 0
    print(f"NO GAP {a.channel} in the next {a.hours:.0f} h")
    return 3


if __name__ == "__main__":
    sys.exit(main())
