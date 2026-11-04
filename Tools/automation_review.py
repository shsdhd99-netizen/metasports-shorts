"""Daily automation review for the two-week proving period (Nov 4-17, 2026; owner: "make sure automation is reviewed and tested
over the next 2 weeks"). Zero Claude credits.

  python Tools/automation_review.py          -> prints the checks, appends one dated block to Research Notes/Automation Check.md
  exit code: 0 all PASS/WARN, 2 at least one FAIL (Tools/automation_review.ps1 then starts a Claude session to fix it)

Checks: every "MetaSports*" Windows task ran in the last 26 h with result 0 (one-shot tasks only need result 0); both channels have
something scheduled or built for every slot in the next 24 h (next_gap.py); preflight is not BLOCKED; C: has 10 GB+ free; nothing
committed is left unpushed; the gap-fill logs end cleanly.
"""
import datetime, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Research Notes", "Automation Check.md")
DAILY = {"MetaSports analytics", "MetaSports schedule ready AM", "MetaSports schedule ready PM", "MetaSports gapfill nba",
         "MetaSports gapfill fc", "MetaSports automation review"}
results = []


def add(level, name, evidence):
    results.append((level, name, evidence))


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT, **kw)


def tasks():
    ps = ("Get-ScheduledTask -TaskName 'MetaSports*' | ForEach-Object { $i = $_ | Get-ScheduledTaskInfo; "
          "'{0}|{1}|{2}|{3}' -f $_.TaskName, $i.LastRunTime.ToString('s'), $i.LastTaskResult, $_.State }")
    r = sh(["powershell", "-NoProfile", "-Command", ps])
    now = datetime.datetime.now()
    seen = set()
    for line in r.stdout.splitlines():
        parts = line.strip().split("|")
        if len(parts) != 4:
            continue
        name, last, res, state = parts
        seen.add(name)
        try:
            t = datetime.datetime.fromisoformat(last)
        except ValueError:
            t = None
        never = t is None or t.year < 2000
        if name in DAILY:
            if never:
                add("WARN", f"task {name}", "has not run yet")
            elif now - t > datetime.timedelta(hours=26):
                add("FAIL", f"task {name}", f"last ran {t:%b %d %H:%M} (over 26 h ago), state {state}")
            elif res not in ("0", "267009"):  # 267009 = still running
                add("FAIL", f"task {name}", f"last result {res} at {t:%b %d %H:%M}")
            else:
                add("PASS", f"task {name}", f"ran {t:%b %d %H:%M}, result {res}")
        else:
            add("PASS" if never or res == "0" else "WARN", f"task {name}", f"one-shot; last {'never' if never else f'{t:%b %d %H:%M}'}, result {res}")
    for name in DAILY - seen:
        add("FAIL", f"task {name}", "not registered")


def coverage():
    for ch in ("nba", "fc"):
        r = sh([sys.executable, os.path.join(HERE, "next_gap.py"), ch, "--hours", "24", "--min-lead", "0"])
        line = (r.stdout.strip().splitlines() or ["?"])[-1]
        add("FAIL" if line.startswith("GAP") else "PASS", f"{ch} slots in the next 24 h", line)


def preflight():
    r = sh([sys.executable, os.path.join(HERE, "preflight.py"), "--quiet"])
    line = (r.stdout.strip().splitlines() or ["?"])[-1]
    add("FAIL" if "BLOCK" in line.upper() else "PASS", "preflight", line[:160])


def disk():
    free = shutil.disk_usage(ROOT).free / 1e9
    add("PASS" if free >= 10 else "WARN" if free >= 5 else "FAIL", "disk C:", f"{free:.1f} GB free")


def git():
    sh(["git", "fetch", "-q", "origin"])
    r = sh(["git", "rev-list", "--count", "origin/main-329h3w..HEAD"])
    n = r.stdout.strip() or "?"
    add("PASS" if n == "0" else "WARN", "git pushed", f"{n} local commit(s) not on origin")


def gapfill_logs():
    for ch in ("nba", "fc"):
        p = os.path.join(ROOT, "Research Notes", f"Daily Run {ch} Last.txt")
        if not os.path.exists(p):
            add("WARN", f"gapfill {ch} log", "no log yet")
            continue
        last = open(p, encoding="utf-8", errors="replace").read().strip().splitlines()[-1:] or ["?"]
        ok = re.search(r"nothing to build|claude ended, exit 0|another run is active", last[0])
        add("PASS" if ok else "WARN", f"gapfill {ch} log", last[0][:160])


def main():
    for f in (tasks, coverage, preflight, disk, git, gapfill_logs):
        try:
            f()
        except Exception as e:  # a broken check is itself a finding
            add("FAIL", f.__name__, f"check crashed: {e}")
    worst = "FAIL" if any(r[0] == "FAIL" for r in results) else "WARN" if any(r[0] == "WARN" for r in results) else "PASS"
    now = datetime.datetime.now()
    block = [f"\n## {now:%a %b %d, %Y %H:%M} ET: {worst}", "| Result | Check | Evidence |", "|---|---|---|"]
    block += [f"| {lvl} | {name} | {ev.replace('|', '/')} |" for lvl, name, ev in results]
    new = not os.path.exists(OUT)
    with open(OUT, "a", encoding="utf-8") as f:
        if new:
            f.write("# Automation Check (daily, Nov 4-17, 2026; `python Tools/automation_review.py`, PC task 9:00 AM)\n"
                    "A FAIL starts one Claude session to fix it (Tools/automation_review.ps1); its STATUS line goes in the Daily Log.\n")
        f.write("\n".join(block) + "\n")
    for lvl, name, ev in results:
        print(f"{lvl:4}  {name}: {ev}")
    print(f"OVERALL {worst}")
    return 2 if worst == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
