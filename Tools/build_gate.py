"""Build gate (Nov 5, 2026, owner: "don't build any Shorts unless it is currently useful, the autopilot is working, or it gets a high rating").

  python Tools/build_gate.py nba --shape moment --score 88 [--owner-request] [--note "why"]
  python Tools/build_gate.py fc  --shape "goalkeeper trick" --score 92

Prints BUILD or DO NOT BUILD with every reason. BUILD needs ALL of:
  1. an uncovered slot: `next_gap.py <channel>` reports a GAP (the autopilot's 6:45/7:30 AM gap-fill runs first; do not double-build), or --owner-request;
  2. a shape that is not paused (rule, history, news explainer, manager, off-niche) unless --experiment names ONE variable;
  3. an idea_gauge score of 80% or more (`idea_gauge.py` percent), no HARD STOP, and a FRESH copy-check (you assert it with --fresh);
  4. nobody else holds the build (BUILDER.txt says cloud/pc matching --builder, or no CLAIM line for this slot in STATE.md).
--owner-request (the owner asked for this Short in chat) skips 1 only. The goal is channels that run themselves with high retention and millions of views,
so a weak or redundant Short costs a slot, the voice credits and the channel's signal; skipping is the default.
"""
import argparse, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAUSED = {"rule", "history", "news explainer", "news", "manager", "off-niche"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", choices=["nba", "fc"])
    ap.add_argument("--shape", required=True)
    ap.add_argument("--score", type=float, required=True, help="idea_gauge percent")
    ap.add_argument("--fresh", action="store_true", help="copy_check said FRESH")
    ap.add_argument("--owner-request", action="store_true")
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
    if a.shape.lower() in PAUSED and not a.experiment:
        why_not.append(f"shape '{a.shape}' is paused (0.5-0.6x the channel); name one variable with --experiment or pick another shape")
    else:
        why_ok.append(f"shape '{a.shape}' ok" + (f" (experiment: {a.experiment})" if a.experiment else ""))
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
