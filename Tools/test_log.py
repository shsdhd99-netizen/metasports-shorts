"""Test-and-learn log (Nov 5, 2026; owner: "be willing to try new things, learn from errors; stick with what works, test what doesn't until it works").

  python Tools/test_log.py add nba "#98 title" --lane "rule" --variable "reframed as a watchable curiosity" [--post-date 2026-11-08]
  python Tools/test_log.py result "#98 title" --views 9500 --stayed 0.58 --lesson "the curiosity framing worked; keep"
  python Tools/test_log.py status [nba|fc]      # per lane: attempts, last variable, best/last result, verdict (PROVEN / TESTING / RETIRED)

A lane is PROVEN when its median is at least 1.5x the channel median with n >= 4. Otherwise it is TESTING: every new attempt must change ONE variable
compared with the previous attempt (hook, length, footage type, title opener, framing, posting slot) and the lesson is written down once the 72 h
result is in. A lane is RETIRED only after 5 attempts that changed 3 different variables and all stayed under the channel median. Nothing is paused
for ever: a retired lane can be reopened with a genuinely new idea. File: Research Notes/Test Log.csv.
"""
import argparse, csv, datetime, os, statistics, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "Research Notes", "Test Log.csv")
COLS = ["date", "channel", "short", "lane", "variable", "post_date", "views_72h", "stayed", "lesson"]


def rows():
    return list(csv.DictReader(open(LOG, encoding="utf-8"))) if os.path.exists(LOG) else []


def write(rs):
    with open(LOG, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(rs)


def channel_median(ch):
    try:
        import learn  # noqa
    except Exception:
        pass
    med = {"nba": 6800, "fc": 2500}  # Learned Weights Nov 4-5 (era medians); update when learn.py changes them
    return med[ch]


def lane_status(ch):
    rs = [r for r in rows() if r["channel"] == ch]
    out = {}
    for r in rs:
        out.setdefault(r["lane"], []).append(r)
    med = channel_median(ch)
    res = {}
    for lane, items in out.items():
        v = [float(i["views_72h"]) for i in items if i["views_72h"]]
        variables = {i["variable"] for i in items}
        verdict = "TESTING"
        if len(v) >= 4 and statistics.median(v) >= 1.5 * med:
            verdict = "PROVEN"
        elif len(v) >= 5 and len(variables) >= 3 and all(x < med for x in v):
            verdict = "RETIRED"
        res[lane] = (len(items), items[-1]["variable"], (statistics.median(v) if v else None), verdict)
    return res


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["add", "result", "status"]); ap.add_argument("a", nargs="?"); ap.add_argument("b", nargs="?")
    ap.add_argument("--lane", default=""); ap.add_argument("--variable", default=""); ap.add_argument("--post-date", default="")
    ap.add_argument("--views", default=""); ap.add_argument("--stayed", default=""); ap.add_argument("--lesson", default="")
    a = ap.parse_args()
    rs = rows()
    if a.cmd == "add":
        last = [r for r in rs if r["channel"] == a.a and r["lane"] == a.lane]
        if last and last[-1]["variable"].strip().lower() == a.variable.strip().lower():
            sys.exit(f"Same variable as the last attempt in lane '{a.lane}' ({a.variable!r}): change ONE different thing, then log it.")
        rs.append(dict(date=datetime.date.today().isoformat(), channel=a.a, short=a.b, lane=a.lane, variable=a.variable, post_date=a.post_date, views_72h="", stayed="", lesson=""))
        write(rs); print("logged test", a.b)
    elif a.cmd == "result":
        for r in rs:
            if r["short"] == a.a:
                r["views_72h"], r["stayed"], r["lesson"] = a.views, a.stayed, a.lesson
        write(rs); print("result saved for", a.a)
    else:
        for ch in ([a.a] if a.a else ["nba", "fc"]):
            print(f"== {ch} (channel median {channel_median(ch):,})")
            for lane, (n, lastvar, med, v) in sorted(lane_status(ch).items()):
                print(f"  {lane:22} attempts {n:2}  median {("-" if med is None else str(int(med))):>7}  {v:8}  last variable: {lastvar[:60]}")


if __name__ == "__main__":
    main()
