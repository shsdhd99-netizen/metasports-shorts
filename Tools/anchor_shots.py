"""Pin every shot to the words it illustrates, so a script rewrite never leaves pictures one slot late.

  python anchor_shots.py --folder "<Short folder>"            # fills shots.json "start" from "anchor" phrases and prints a check table
  python anchor_shots.py --folder "<folder>" --dry-run

shots.json entries may carry  "anchor": "the Knicks swept"  (the first words of the phrase the shot shows) and optional "lead": 0.03
(seconds before the first anchor word that the cut lands, default 0.03). The phrase is searched in words.json starting after the
previous anchor, case and punctuation ignored. The first shot is 0.0 unless it has an anchor. Shots without an anchor keep their
own "start". The check table lists, for each shot, the clip, the start and the words spoken during it, so you can eyeball that the
picture matches the words (and that a named person is on screen while the name is spoken).
"""
import argparse, json, os, re


def norm(w):
    return re.sub(r"[^a-z0-9$%']", "", w.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    F = a.folder
    shots = json.load(open(os.path.join(F, "shots.json"), encoding="utf-8"))
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8"))
    nw, owner = [], []  # one token per spoken token (a words.json entry like "GTA 6" or "$30 million" can hold several)
    for wi, w in enumerate(words):
        for t in w["word"].split():
            if norm(t):
                nw.append(norm(t))
                owner.append(wi)
    pos = 0
    for i, s in enumerate(shots):
        ph = s.get("anchor")
        if not ph:
            if i == 0:
                s["start"] = 0.0
            continue
        toks = [norm(t) for t in ph.split() if norm(t)]
        found = None
        for j in range(pos, len(nw) - len(toks) + 1):
            if nw[j:j + len(toks)] == toks:
                found = j
                break
        if found is None:
            raise SystemExit(f"shot {i} ({s.get('clip')}): anchor '{ph}' not found after word {pos}")
        s["start"] = 0.0 if i == 0 else round(max(0.0, words[owner[found]]["start"] - s.get("lead", 0.03)), 2)
        pos = found
    prev = -1
    for i, s in enumerate(shots):
        if s["start"] <= prev:
            raise SystemExit(f"shot {i} ({s.get('clip')}) starts at {s['start']} which is not after the previous shot ({prev}); fix the anchors")
        prev = s["start"]
    total = words[-1]["end"] + 0.3
    print(f"{'#':>2} {'start':>6} {'len':>5}  {'kind':6} clip  |  words spoken during the shot")
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        spoken = " ".join(w["word"] for w in words if s["start"] - 0.02 <= w["start"] < end - 0.02)
        print(f"{i:>2} {s['start']:>6.2f} {end - s['start']:>5.2f}  {s.get('kind', '?'):6} {s['clip']}  |  {spoken}")
    if not a.dry_run:
        json.dump(shots, open(os.path.join(F, "shots.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("shots.json updated")


main()
