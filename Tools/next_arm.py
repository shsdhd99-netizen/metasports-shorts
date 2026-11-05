"""Which one-variable test arm should the next NBA Short use? (Nov 5, 2026; backlog tests from the Growth Study and Case Study)

  python Tools/next_arm.py nba                  # prints the arm to use (the least-used arm below its target n)
  python Tools/next_arm.py nba --log "#98 title" length_30_35   # records that a Short used an arm

Arms (NBA): control (usual 18-25 s, no foreshadow), length_30_35 (a 30-35 s story, same lane), foreshadow (line 2 says what the ending is about),
tension_first (line 1 states a tension, not the result). Target n = 4 per arm, judged at 72 h on stayed % (API engaged ratio) and views against
the control. Only one variable per Short; a Short in a paused shape is never an arm. The log is Research Notes/Experiment Arms.csv.
FC arm: action_first (open on the action instead of the spoken title), target n = 4, goalkeeper lane only.
"""
import csv, os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "Research Notes", "Experiment Arms.csv")
ARMS = {"nba": ["control", "length_30_35", "foreshadow", "tension_first"], "fc": ["control", "action_first"]}
N = 4


def rows():
    if not os.path.exists(LOG):
        return []
    return list(csv.DictReader(open(LOG, encoding="utf-8")))


def main():
    ch = sys.argv[1] if len(sys.argv) > 1 else "nba"
    if "--log" in sys.argv:
        i = sys.argv.index("--log"); title, arm = sys.argv[i + 1], sys.argv[i + 2]
        new = not os.path.exists(LOG)
        with open(LOG, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["date", "channel", "short", "arm"])
            w.writerow([datetime.date.today().isoformat(), ch, title, arm])
        print("logged", title, arm); return
    used = {a: sum(1 for r in rows() if r["channel"] == ch and r["arm"] == a) for a in ARMS[ch]}
    # control only gets built after each test arm has at least one Short, so the first runs are the tests
    order = [a for a in ARMS[ch] if a != "control"] + ["control"]
    open_arms = [a for a in order if used[a] < N]
    print("arm counts:", used)
    print("NEXT ARM:", open_arms[0] if open_arms else "all arms full (n=4 each): judge them at 72 h and write the result in Learned Weights/Lessons")
    if open_arms and ch == "nba" and used["control"] < N and open_arms[0] != "control":
        print("(tests first; the control side is any usual 18-25 s Short in the same lane)")


if __name__ == "__main__":
    main()
