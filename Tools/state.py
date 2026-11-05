"""One-page STATE writer plus health check (Nov 5, 2026; backlog items "STATE.md writer" and "routine health check").

  python Tools/state.py            # rewrites the AUTO block at the top of Research Notes/STATE.md and prints the health flags
  python Tools/state.py --check    # health flags only, exit code 1 when anything needs attention

Reads only local files and runs Tools/next_gap.py (no network, no credits): builder, preflight result, newest analytics file, channel
numbers from channel_daily CSVs (Tools/channel_totals.py writes them), next uncovered slot for both channels, the last scheduler lines, the last
cloud STATUS lines from the Daily Log, disk space. Everything between <!-- AUTO:START --> and <!-- AUTO:END --> is replaced; the hand-written
STATE history below is never touched.
"""
import csv, datetime, glob, os, re, shutil, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RN = os.path.join(ROOT, "Research Notes")
START, END = "<!-- AUTO:START -->", "<!-- AUTO:END -->"


def read(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def gap(ch):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "Tools", "next_gap.py"), ch], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return (r.stdout.strip().splitlines() or ["?"])[-1]


def channel_line(label, folder):
    files = sorted(glob.glob(os.path.join(RN, "Studio exports", folder, "channel_daily *.csv")))
    if not files:
        return f"{label}: no channel_daily file (run `python Tools/channel_totals.py`)", None
    rows = list(csv.DictReader(open(files[-1], encoding="utf-8")))
    v7 = sum(int(r["views"]) for r in rows[-7:]) / 7
    v90 = sum(int(r["views"]) for r in rows[-90:])
    return f"{label}: {v7:,.0f} Shorts views/day (7-day), {v90:,} in the last 90 days ({v90/1e5:.1f}% of the 10M line), data to {rows[-1]['day']}", rows[-1]["day"]


def main():
    flags = []
    now = datetime.datetime.now()
    builder = read(os.path.join(RN, "BUILDER.txt")).strip().splitlines()[:1] or ["?"]
    pre = read(os.path.join(RN, "Preflight.md"))
    pre_ok = re.search(r"PREFLIGHT (OK|BLOCKED)[^\n]*", pre)
    if not pre_ok or "BLOCKED" in pre_ok.group(0):
        flags.append("preflight: " + (pre_ok.group(0) if pre_ok else "no result in Preflight.md"))
    daily = sorted(glob.glob(os.path.join(RN, "Studio exports", "api", "daily *.csv")))
    age = (now.date() - datetime.date.fromisoformat(os.path.basename(daily[-1])[6:16])).days if daily else 99
    if age > 2:
        flags.append(f"analytics: newest daily file is {age} days old")
    free_gb = shutil.disk_usage(ROOT).free / 2**30
    if free_gb < 8:
        flags.append(f"disk: only {free_gb:.1f} GB free (preflight blocks under 5 GB)")
    gaps = {ch: gap(ch) for ch in ("nba", "fc")}
    for ch, g in gaps.items():
        m = re.search(r"GAP \w+ (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})", g)
        if m and datetime.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}") - now < datetime.timedelta(hours=30):
            flags.append(f"{ch}: open slot within 30 h ({g})")
    log = read(os.path.join(RN, "Daily Log.md"))
    cloud = [l.strip() for l in log.splitlines() if "cloud" in l.lower() and "STATUS" in l][-3:]
    if any("blocked" in l.lower() for l in cloud[-2:]):
        flags.append("cloud routines: the last STATUS says blocked (keys missing in the cloud environment?)")
    sched = [l.strip() for l in read(os.path.join(RN, "Schedule Ready Log.md")).splitlines() if l.startswith("- 20")][-3:]
    nba_line, _ = channel_line("NBA", "api")
    fc_line, _ = channel_line("FC", "api FC")
    block = [START, f"## AUTO (written by `python Tools/state.py`, {now:%Y-%m-%d %H:%M} local; do not edit by hand)",
             f"- Builder: {builder[0]}", f"- Preflight: {pre_ok.group(0) if pre_ok else 'unknown'}", f"- Disk free: {free_gb:.1f} GB",
             f"- {nba_line}", f"- {fc_line}",
             f"- Next open slot: NBA {gaps['nba']}; FC {gaps['fc']}",
             "- Last scheduler lines: " + (" | ".join(s[:120] for s in sched) or "none"),
             "- Last cloud STATUS lines: " + (" | ".join(c[:100] for c in cloud) or "none"),
             "- **Needs attention:** " + ("; ".join(flags) if flags else "nothing"), END]
    print("\n".join(block[1:]))
    if "--check" in sys.argv:
        sys.exit(1 if flags else 0)
    p = os.path.join(RN, "STATE.md")
    s = read(p)
    if START in s and END in s:
        s = re.sub(re.escape(START) + r".*?" + re.escape(END), "\n".join(block).replace("\\", "\\\\"), s, flags=re.S)
    else:
        first, _, rest = s.partition("\n")
        s = first + "\n" + "\n".join(block) + "\n" + rest
    open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    main()
