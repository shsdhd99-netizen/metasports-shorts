"""Replaced on Nov 7, 2026 by the lab (owner: "auto run and log tests yourself with a score on them").
The old arms (control / length_30_35 / foreshadow / tension_first; FC action_first) were never logged, and length_30_35 was scrapped
(our 16 NBA Shorts over 25 s got 2.9K vs 6.4K). Live tests now live in Research Notes/Lab/tests.json.
  python Tools/next_arm.py nba|fc        -> same as: python Tools/lab.py assign nba|fc
"""
import os, subprocess, sys

if __name__ == "__main__":
    ch = sys.argv[1] if len(sys.argv) > 1 else "nba"
    print("next_arm.py is replaced by the lab; running: python Tools/lab.py assign " + ch)
    sys.exit(subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab.py"), "assign", ch]).returncode)
