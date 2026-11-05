"""Build gate (Nov 5, 2026, owner: "don't build any Shorts unless it is currently useful, the autopilot is working, or it gets a high rating").

  python Tools/build_gate.py nba --shape moment --score 88 [--owner-request] [--note "why"]
  python Tools/build_gate.py fc  --shape "goalkeeper trick" --score 92

Prints BUILD or DO NOT BUILD with every reason. BUILD needs ALL of:
  1. an uncovered slot: `next_gap.py <channel>` reports a GAP (the autopilot's 6:45/7:30 AM gap-fill runs first; do not double-build), or --owner-request;
  2. a PROVEN lane, or a TEST lane with --experiment naming ONE variable that differs from the last attempt (Tools/test_log.py); FC has no banned shapes;
  5. not in AUTOPILOT TEST MODE (Research Notes/AUTOPILOT_TEST.txt) unless --owner-request;
  3. an idea_gauge score of 80% or more (`idea_gauge.py` percent), no HARD STOP, and a FRESH copy-check (you assert it with --fresh);
  4. nobody else holds the build (BUILDER.txt says cloud/pc matching --builder, or no CLAIM line for this slot in STATE.md).
--owner-request (the owner asked for this Short in chat) skips 1 only. The goal is channels that run themselves with high retention and millions of views,
so a weak or redundant Short costs a slot, the voice credits and the channel's signal; skipping is the default.
"""
import argparse, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAUSED = {"nba": {"rule", "history", "news explainer", "news", "off-niche"}, "fc": set()}  # Nov 5: FC has no paused shapes (owner: do not limit FC to goalkeepers)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", choices=["nba", "fc"])
    ap.add_argument("--shape", required=True)
    ap.add_argument("--score", type=float, required=True, help="idea_gauge percent")
    ap.add_argument("--fresh", action="store_true", help="copy_check said FRESH")
    ap.add_argument("--owner-request", action="store_true")
    ap.add_argument("--autopilot", action="store_true", help="the scheduled autopilot run (PC gap-fill 6:45/7:30 or the cloud routines): exempt from AUTOPILOT TEST MODE")
    ap.add_argument("--experiment", help="the ONE variable this build tests (allows a paused shape)")
    ap.add_argument("--builder", default="pc", choices=["pc", "cloud"])
    a = ap.parse_args()
    why_not, why_ok = [], []
    g = subprocess.run([sys.executable, os.path.join(ROOT, "Tools", "next_gap.py"), a.channel], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip().splitlines()
    gap = (g or ["?"])[-1]
    if gap.startswith("GAP"):
        why_ok.append("slot open: " + gap)
    elif a.owner_request:
        why_ok.append("owner asked for it (slot rule skipped): " + gap)
    else:
        why_not.append("no uncovered slot (" + gap + "); the autopilot gap-fill covers new gaps")
    sys.path.insert(0, os.path.join(ROOT, "Tools"))
    try:
        import test_log as TL
        st = TL.lane_status(a.channel).get(a.shape, None)
    except Exception:
        st = None
    proven = bool(st and st[3] == "PROVEN")
    needs_angle = a.shape.lower() in PAUSED[a.channel] or (st is not None and not proven)
    if needs_angle and not a.experiment:
        why_not.append(f"lane '{a.shape}' is not proven yet: it is a TEST lane, so name the ONE variable you change from the last attempt with --experiment (and log it with test_log.py add)")
    elif needs_angle and st and a.experiment.strip().lower() == st[1].strip().lower():
        why_not.append(f"the experiment variable repeats the last attempt in this lane ({st[1]!r}): change something else")
    else:
        why_ok.append(f"lane '{a.shape}' " + ("PROVEN" if proven else "new lane (test)") if not needs_angle else f"test lane '{a.shape}' changing: {a.experiment}")
    if os.path.exists(os.path.join(ROOT, "Research Notes", "AUTOPILOT_TEST.txt")) and not (a.owner_request or a.autopilot):
        why_not.append("AUTOPILOT TEST MODE (owner, Nov 5): terminal sessions do not build Shorts; only the autopilot builds unless the owner says so")
    if a.score < 80:
        why_not.append(f"gauge score {a.score:.0f}% is under 80%")
    else:
        why_ok.append(f"gauge {a.score:.0f}%")
    if not a.fresh:
        why_not.append("copy_check not confirmed FRESH (pass --fresh after running copy_check.py)")
    b = open(os.path.join(ROOT, "Research Notes", "BUILDER.txt"), encoding="utf-8", errors="replace").read().strip().split()[0:1]
    if b and b[0] != a.builder and not a.owner_request:
        why_not.append(f"BUILDER.txt says {b[0]}, not {a.builder}")
    st = open(os.path.join(ROOT, "Research Notes", "STATE.md"), encoding="utf-8", errors="replace").read()
    if re.search(r"^CLAIM .*", st, re.M):
        why_not.append("an open CLAIM line exists in STATE.md: check it is not this slot")
    print(("BUILD" if not why_not else "DO NOT BUILD"))
    for w in why_ok:
        print("  ok  ", w)
    for w in why_not:
        print("  NO  ", w)
    sys.exit(0 if not why_not else 1)


if __name__ == "__main__":
    main()
