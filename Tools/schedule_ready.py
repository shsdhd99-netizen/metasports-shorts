"""Schedule ready DRAFTs by script (zero Claude credits), with yt_schedule.py's guard rails unchanged (Nov 3, 2026).

A folder qualifies only when ALL hold: exactly one `DRAFT*.mp4` in it; an `UPLOAD.md` with a parsable title, tags and a slot
(`Target:` / `Slot:` / `Post:` followed by e.g. "Wed Nov 4, 7:15 AM ET"); a passing QA line in the card ("QA PASS"/"QA: PASS"/...);
no `HOLD` marker in the card; slot at least --min-lead minutes away (default 120, so the owner can still look); file never scheduled
before (sha in Research Notes/Scheduled Uploads.csv). yt_schedule.py then re-applies its own refusals (20 min to 30 days, title and
tags present, 100-char title, never re-upload). Uploads are PRIVATE with publishAt; nothing goes public by itself before its slot,
and the owner can delete it in the YouTube app until then. It never opens Studio, pins, edits or deletes.

  python Tools/schedule_ready.py            -> dry run: lists what it would schedule and why others are skipped
  python Tools/schedule_ready.py --go       -> really schedules (this is what the Task Scheduler entry runs)
Writes one summary line to Research Notes/Schedule Ready Log.md each --go run, plus the reason for every skip (also on --go since Nov 5).
--require-approved (Nov 5): only schedules cards that carry `**Approved:** yes`.
Slots under 6 h from another Short on the same channel (already in Scheduled Uploads.csv, or picked earlier in this run) are skipped.

A/B pairs (Nov 3): a folder with a music and a no-music DRAFT is no longer always skipped. A card line `**Arm:** music`/`no-music`
picks that file. With no Arm line it is still skipped (the arm is the owner's call) unless the run passes
--default-arm no-music|music; then a card's `**Post:** MUSIC version`/`no-music version` line wins, else the default arm is used.
"""
import argparse, datetime, glob, os, re, subprocess, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import yt_schedule as ys

ET = ZoneInfo("America/New_York")
MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
SLOT = re.compile(r"(?:target(?: slot)?|slot|post)\W{0,6}(?:[^.\n]{0,25}?)\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*,?\s+"
                  r"([A-Z][a-z]{2})[a-z]*\s+(\d{1,2}),?\s+(?:about\s+)?(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\b", re.I)
QA = re.compile(r"QA[^\n]{0,40}\bPASS|qa_short[^\n]{0,30}PASS", re.I)
ARM = re.compile(r"\*{0,2}Arm:?\*{0,2}:?\s*(no[- ]?music|music)\b", re.I)
POSTARM = re.compile(r"\*{0,2}Post:?\*{0,2}:?\s*(no[- ]?music|music)\b", re.I)
NOMUSIC = re.compile(r"no[- _]?music", re.I)
FOLDERS = [("nba", os.path.join(ROOT, "Productions", "MetaSports")), ("fc", os.path.join(ROOT, "Soccer Channel", "Productions"))]


def slot_of(text, year):
    m = SLOT.search(text)
    if not m or m.group(1).title() not in MONTHS:
        return None
    h = int(m.group(3)) % 12 + (12 if m.group(5).upper() == "PM" else 0)
    return datetime.datetime(year, MONTHS[m.group(1).title()], int(m.group(2)), h, int(m.group(4) or 0), tzinfo=ET)


def pick_arm(drafts, text, default):
    """Return (file, arm, None) or (None, None, why) for a folder with 2+ DRAFTs."""
    m = ARM.search(text) or (default and POSTARM.search(text))  # Post: line only refines an opted-in default
    arm = (m.group(1).lower().replace(" ", "-") if m else default)
    if arm == "nomusic":
        arm = "no-music"
    if not arm:
        return None, None, f"{len(drafts)} DRAFT files and no **Arm:** line (owner's call)"
    nm = [f for f in drafts if NOMUSIC.search(os.path.basename(f))]
    mu = [f for f in drafts if f not in nm]
    pool = nm if arm == "no-music" else mu
    if len(pool) != 1:
        return None, None, f"{len(drafts)} DRAFT files; arm '{arm}' matches {len(pool)} of them"
    return pool[0], arm, None


GAP_H = 6  # rule: at most 2 posts a day per channel, 6+ hours apart


def booked_slots():
    """(channel, publish datetime ET, title) of everything already scheduled, from Scheduled Uploads.csv."""
    import csv
    out = []
    if os.path.exists(ys.LOG):
        for r in csv.DictReader(open(ys.LOG, encoding="utf-8")):
            try:
                t = datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
            except (KeyError, ValueError):
                continue
            out.append((r.get("channel", ""), t, r.get("title", "")[:40]))
    return out


def clash(ch, slot, booked):
    for c, t, who in booked:
        if c == ch and abs((t - slot).total_seconds()) < GAP_H * 3600:
            return f"slot {slot:%a %b %d %H:%M} is under {GAP_H} h from {who} ({t:%a %b %d %H:%M})"
    return None


def candidates():
    for ch, base in FOLDERS:
        for d in sorted(glob.glob(os.path.join(base, "*"))):
            if os.path.isdir(d) and os.path.exists(os.path.join(d, "UPLOAD.md")):
                yield ch, d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true")
    ap.add_argument("--default-arm", choices=["music", "no-music"], help="arm for A/B pairs with no **Arm:** line")
    ap.add_argument("--require-approved", action="store_true",
                    help="strict mode (option B): only cards with a line `**Approved:** yes` (the owner's OK, mirrors Hub approved:true) are scheduled")
    ap.add_argument("--min-lead", type=int, default=120, help="minutes the slot must be away")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    done, report = [], []
    booked = booked_slots()
    for ch, d in candidates():
        name = os.path.basename(d)
        drafts = glob.glob(os.path.join(d, "DRAFT*.mp4"))
        if not drafts:
            continue
        card = os.path.join(d, "UPLOAD.md")
        text = open(card, encoding="utf-8-sig").read()
        slot = slot_of(text, now.year)
        title, tags = ys.parse_card(card)
        why, arm = None, None
        if len(drafts) > 1:
            pick, arm, why = pick_arm(drafts, text, a.default_arm)
            drafts = [pick] if pick else drafts
        if not slot or slot < now + datetime.timedelta(minutes=a.min_lead):
            continue  # old or unslotted folder: silent (not a candidate)
        if why:
            pass
        elif ys.already(ys.sha(drafts[0])):
            continue  # already scheduled: silent
        elif clash(ch, slot, booked):
            why = clash(ch, slot, booked)
        elif re.search(r"\bHOLD\b", text):
            why = "card says HOLD"
        elif a.require_approved and not re.search(r"\*\*Approved:\*\*\s*(yes|true)", text, re.I):
            why = "--require-approved: no `**Approved:** yes` line on the card"
        elif not QA.search(text):
            why = "no passing QA line in the card"
        elif not (title and tags):
            why = "title or tags missing"
        elif not slot:
            why = "no parsable slot"
        elif slot < now + datetime.timedelta(minutes=a.min_lead):
            why = f"slot {slot:%a %b %d %H:%M} is under {a.min_lead} min away or past"
        if why:
            report.append(f"skip {name}: {why}")
            continue
        cmd = [sys.executable, os.path.join(HERE, "yt_schedule.py"), "--channel", ch, "--file", drafts[0], "--card", card,
               "--at", f"{slot:%Y-%m-%d %H:%M}"] + (["--go"] if a.go else [])
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        out = (r.stdout + r.stderr).strip().splitlines()
        report.append(f"{'SCHEDULED' if a.go and r.returncode == 0 else 'would schedule' if r.returncode == 0 else 'REFUSED'} "
                      f"{name} -> {slot:%a %b %d %H:%M} ET" + (f" [arm {arm}]" if arm else "") + (f" ({out[-1][:160]})" if r.returncode else ""))
        if r.returncode == 0:
            booked.append((ch, slot, name[:40]))  # later folders in this run must keep the gap too
        if a.go and r.returncode == 0:
            done.append(name)
    print("\n".join(report) or "nothing to do")
    if a.go:
        log = os.path.join(ROOT, "Research Notes", "Schedule Ready Log.md")
        with open(log, "a", encoding="utf-8") as f:
            for r_ in report:  # Nov 5: every skip/refusal is logged with its reason, not only the count
                if r_.startswith(("skip", "REFUSED")):
                    f.write(f"  - {now:%Y-%m-%d %H:%M} {r_}\n")
            f.write(f"- {now:%Y-%m-%d %H:%M} ET: scheduled {len(done)}" + (": " + "; ".join(done) if done else "") +
                    f"; skipped/refused {len([r for r in report if r.startswith(('skip', 'REFUSED'))])}.\n")


if __name__ == "__main__":
    main()
