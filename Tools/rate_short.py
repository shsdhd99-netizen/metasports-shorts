"""Viral-formula rating for every queued Short (0-100) from the strict critics' 9-item scorecards, plus a post-priority that weighs topic power.

  python Tools/rate_short.py            # reads Research Notes/Critique Round 3 - Ratings.json, writes Research Notes/Ratings - <date>.md and ratings.json
Weights (sum 100): 1 hook 20, 2 turn by 6-8 s 12, 3 escalation 14, 4 payoff 18, 5 loop 4, 6 proof/footage 10, 7 pace/edit 8, 8 voice 6, 9 packaging/topic 8.
PASS = 1, WEAK = 0.5, FAIL = 0. Craft score = weighted sum. Topic power (0-1) comes from this channel's own results (Bronny, free throws, Wemby, Luka, Curry =
the audience's winners; contract lane = flop). Post priority = craft * (0.5 + 0.5 * topic). Predictions are HYPOTHESIS until real results come in:
log each posted Short's real stayed-to-watch / views in the Outcome Log and compare (calibration).
"""
import json, os, sys
W = {"1": 20, "2": 12, "3": 14, "4": 18, "5": 4, "6": 10, "7": 8, "8": 6, "9": 8}
V = {"PASS": 1.0, "WEAK": 0.5, "FAIL": 0.0}
TOPIC = {"01": 0.5, "11": 0.7, "13": 0.7, "14": 0.8, "15": 0.9, "16": 0.8, "17": 0.8, "19": 0.75, "20": 0.8, "21": 0.9, "23": 1.0, "24": 1.0, "25": 1.0,
         "26": 0.8, "27": 0.8, "28": 0.75, "29": 0.95, "30": 0.8, "32": 0.85, "33": 0.8, "34": 0.85, "35": 1.0}
NAME = {"01": "LeBron minimum (contract)", "11": "Jordan push-off", "13": "Kawhi picks", "14": "Four stars push-off", "15": "Adams GTA", "16": "Giannis Vice City",
        "17": "Flopping", "19": "Flagg height", "20": "Bad Boys defense", "21": "Jokic vs Westbrook", "23": "Father vs son (HOLD to Oct 21)", "24": "Bronny roster spot",
        "25": "Bronny better?", "26": "Screens", "27": "Lotteries", "28": "NBA Cup at Hinkle", "29": "Underhand free throws", "30": "Giannis steps", "32": "Spurs 29-pt lead",
        "33": "Runs out of players", "34": "2007 top four", "35": "Wemby rugby"}


def score(r):
    return round(sum(W[k] * V.get(r.get(k, "FAIL"), 0) for k in W), 1)


def main():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Research Notes")
    ratings = json.load(open(os.path.join(root, "Critique Round 3 - Ratings.json"), encoding="utf-8"))
    rows = []
    for k, r in ratings.items():
        c = score(r); t = TOPIC.get(k, 0.7); rows.append(dict(num=k, name=NAME.get(k, k), craft=c, topic=t, priority=round(c * (0.5 + 0.5 * t), 1), verdict=r.get("verdict"),
                                                       weak=[i for i in W if r.get(i) == "WEAK"], fail=[i for i in W if r.get(i) == "FAIL"]))
    rows.sort(key=lambda x: -x["priority"])
    out = ["# Ratings (strict critic Round 3, Oct 5 2026)", "", "Craft = viral-formula score 0-100 from the critics' 9-item scorecards (weights in Tools/rate_short.py). Priority = craft x (0.5 + 0.5 x topic power). Verdict is the critic's: no Short is SHIP yet; scores are BEFORE the fixes.", "",
           "| rank | # | Short | craft | topic | priority | verdict | FAIL items | WEAK items |", "|---|---|---|---|---|---|---|---|---|"]
    for i, x in enumerate(rows, 1):
        out.append(f"| {i} | {x['num']} | {x['name']} | {x['craft']} | {x['topic']} | {x['priority']} | {x['verdict']} | {','.join(x['fail']) or '-'} | {','.join(x['weak']) or '-'} |")
    open(os.path.join(root, "Ratings - Oct 5 2026.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    json.dump(rows, open(os.path.join(root, "ratings.json"), "w"), indent=1)
    print("\n".join(out))


if __name__ == "__main__":
    main()
