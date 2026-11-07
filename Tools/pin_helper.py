r"""Pin helper (Nov 6, 2026): the one routine the YouTube API cannot do (pinning a comment) made as quick as possible.

  python Tools/pin_helper.py            # writes Desktop\PIN THESE TODAY.txt and prints it
  python Tools/pin_helper.py --open     # also opens it in Notepad

Lists every Short that goes live (or went live in the last 48 hours): channel, title, link, time, and the exact pinned-comment text from its UPLOAD.md,
ready to paste. Reads Research Notes/Scheduled Uploads.csv and each card; no network. In the YouTube app: open the Short > comments > paste > the 3 dots
next to your own comment > Pin. Runs from state.py so the file is always current.
"""
import csv, datetime, glob, os, re, subprocess, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ET = ZoneInfo("America/New_York")
OUT = os.path.join(os.path.expanduser("~"), "Desktop", "PIN THESE TODAY.txt")


def pinned(card):
    t = open(card, encoding="utf-8-sig").read()
    m = re.search(r"\*\*Pinned comment:?\*\*:?\s*(.+)", t, re.I) or re.search(r"##\s*Pinned comment[^\n]*\n+(.+)", t, re.I)
    return m.group(1).strip().strip("*").strip() if m else "(no pinned comment in the card)"


def main():
    now = datetime.datetime.now(ET)
    rows = list(csv.DictReader(open(os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv"), encoding="utf-8")))
    lines = [f"PIN THESE (written {now:%a %b %d %H:%M} ET). YouTube app > the Short > comments > paste > 3 dots on your comment > Pin.", ""]
    n = 0
    for r in sorted(rows, key=lambda r: r["publish_et"]):
        try:
            t = datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        except ValueError:
            continue
        if not (now - datetime.timedelta(hours=48) <= t <= now + datetime.timedelta(hours=14)):
            continue
        d = os.path.join(ROOT, os.path.dirname(r["file"]))
        card = os.path.join(d, "UPLOAD.md")
        txt = pinned(card) if os.path.exists(card) else "(no card found)"
        state = "LIVE" if t <= now else f"goes live {t:%a %I:%M %p}"
        title = r["title"] or "(title missing in the log: check the card)"
        lines += [f"[{r['channel'].upper()}] {title}", f"  {state} ({t:%a %b %d %H:%M} ET)   https://youtube.com/shorts/{r['video_id']}", f"  PASTE: {txt}", ""]
        n += 1
    if n == 0:
        lines.append("Nothing to pin right now.")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(lines))
    if "--open" in sys.argv:
        subprocess.Popen(["notepad.exe", OUT])


if __name__ == "__main__":
    main()
