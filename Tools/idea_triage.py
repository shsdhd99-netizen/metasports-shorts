"""Idea triage (Nov 5, 2026; owner: "anything that gets skipped: the strongest ones stay as possible ideas, anything else is notes or trashed").

  python Tools/idea_triage.py add nba "idea in one line" --score 88 [--shape moment] [--source URL]
  python Tools/idea_triage.py list
  python Tools/idea_triage.py use nba "idea words"      # remove a candidate once it is built

Rules: score 80 or more -> CANDIDATE (at most 5 per channel, ranked; a stronger idea evicts the weakest, which becomes a note);
60-79 -> NOTE (one line, at most 15 per channel, oldest dropped); under 60 -> TRASH (not stored, only counted).
Candidates older than 14 days are demoted to notes (news goes stale). Renders Research Notes/Idea Candidates.md. Nothing else keeps an idea alive:
the old Idea Bank files are history; new ideas go through here.
"""
import argparse, datetime, json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = os.path.join(ROOT, "Research Notes", "_idea_triage.json")
MD = os.path.join(ROOT, "Research Notes", "Idea Candidates.md")


def load():
    return json.load(open(J, encoding="utf-8")) if os.path.exists(J) else {"cand": [], "notes": [], "trashed": 0}


def render(d):
    out = ["# Idea candidates and notes (auto-written by Tools/idea_triage.py)", "",
           "Candidates (score 80+, max 5 per channel) are the only ideas allowed to become builds; notes are one-liners; everything below 60 was trashed.",
           f"Trashed so far: {d['trashed']}.", ""]
    for ch in ("nba", "fc"):
        out.append(f"## {ch.upper()} candidates")
        for c in sorted([c for c in d["cand"] if c["ch"] == ch], key=lambda c: -c["score"]):
            out.append(f"- **{c['score']:.0f}%** {c['idea']} [{c.get('shape','')}] ({c['date']}) {c.get('source','')}")
        out.append(f"\n## {ch.upper()} notes")
        for n in [n for n in d["notes"] if n["ch"] == ch]:
            out.append(f"- {n['score']:.0f}% {n['idea']} ({n['date']})")
        out.append("")
    out += kept_sections()
    open(MD, "w", encoding="utf-8").write("\n".join(out))


GENERATED = {"## NBA candidates", "## NBA notes", "## FC candidates", "## FC notes"}


def kept_sections():
    """Hand-written '## ...' sections in the old file (not the four generated ones) are carried over unchanged (Nov 7 fix:
    a re-render used to delete them, e.g. the N1-N3 butterfly ideas)."""
    if not os.path.exists(MD):
        return []
    keep, on = [], False
    for line in open(MD, encoding="utf-8").read().split("\n"):
        if line.startswith("## "):
            on = line.strip() not in GENERATED
        if on:
            keep.append(line)
    return keep


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["add", "list", "use"]); ap.add_argument("ch", nargs="?"); ap.add_argument("idea", nargs="?")
    ap.add_argument("--score", type=float, default=0); ap.add_argument("--shape", default=""); ap.add_argument("--source", default="")
    a = ap.parse_args(); d = load(); today = datetime.date.today()
    for c in list(d["cand"]):  # staleness
        if (today - datetime.date.fromisoformat(c["date"])).days > 14:
            d["cand"].remove(c); d["notes"].append(c)
    if a.cmd == "add":
        item = dict(ch=a.ch, idea=a.idea, score=a.score, shape=a.shape, source=a.source, date=today.isoformat())
        if a.score >= 80:
            mine = [c for c in d["cand"] if c["ch"] == a.ch]
            if len(mine) >= 5:
                weakest = min(mine, key=lambda c: c["score"])
                if a.score <= weakest["score"]:
                    d["notes"].append(item); print("candidate list full of stronger ideas -> saved as a note")
                else:
                    d["cand"].remove(weakest); d["notes"].append(weakest); d["cand"].append(item); print(f"candidate (evicted weaker: {weakest['idea'][:50]})")
            else:
                d["cand"].append(item); print("candidate")
        elif a.score >= 60:
            d["notes"].append(item); print("note")
        else:
            d["trashed"] += 1; print("trashed (not stored)")
        for ch in ("nba", "fc"):
            ns = [n for n in d["notes"] if n["ch"] == ch]
            for n in ns[:-15]:
                d["notes"].remove(n)
    elif a.cmd == "use":
        d["cand"] = [c for c in d["cand"] if not (c["ch"] == a.ch and a.idea.lower() in c["idea"].lower())]
        print("removed")
    json.dump(d, open(J, "w", encoding="utf-8"), indent=1); render(d)
    if a.cmd == "list":
        print(open(MD, encoding="utf-8").read())


if __name__ == "__main__":
    main()
