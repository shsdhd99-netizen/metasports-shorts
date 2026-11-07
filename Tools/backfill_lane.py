"""Backfill `shape` (and an empty `lane`) in Research Notes/Experiments.csv from the title (Nov 5, 2026; backlog item).

  python Tools/backfill_lane.py            # dry run: counts, a 12-row spot check, and the rows it would leave blank
  python Tools/backfill_lane.py --apply    # writes the CSV (only blank cells; a hand-filled value is never overwritten)

Keyword rules for the Nov 4 topic-shape taxonomy (Research Notes/Topic and Script Reset (Nov 2026).md). A title that matches no rule stays blank
(no guess). Rules are checked in order, first match wins; the shape is also copied to `lane` when `lane` is empty, so `learn.py` can rank them.
Tier [H]: keyword labels, spot-check them (the dry run prints 12 random rows to read).
"""
import argparse, csv, os, random, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "Research Notes", "Experiments.csv")

NBA = [
    ("off-niche", r"(#ai|#comedy|#funny|#storytime|#sora|yarn|snoop|squirrel|fishing|pov:)"),
    ("family", r"\b(bronny|boozer|his son|his dad|father|family|kid|son in the nba|brother)\b"),
    ("rule", r"\b(banned?|ban|illegal|allowed|rule|rules|bet|refuse|why (?:nba )?players? (?:refuse|stopped)|technical foul|count[s]?\b|doesn'?t count|line lying|measured)\b"),
    ("superlative", r"\b(most|ever|record|oldest|youngest|first|never|only|all-time|history|ranked|top \d|best|worst)\b"),
    ("news", r"\b(trade[sd]?|sign(?:ed|s)?|extension|contract|waive|cut|fired|hired|retire|injur|suspend|out indefinitely)\b"),
    ("moment", r"\b(hit|hits|threw|throw|blocked|dunk|buzzer|overtime|ejected|ejection|fan|bench|mascot|alley|scored|steal|swish|tech)\b"),
]
FC = [
    ("goalkeeper trick", r"\b(goalkeepers?|keepers?)\b"),
    ("manager", r"\b(manager|coach|boss)\b"),
    ("player record", r"\b(scored|goals?|record|most|first)\b"),
    ("club story", r"\b(barcelona|madrid|united|city|liverpool|club|signed|napkin|shirt|odds|derby|sent off)\b"),
]


def shape_of(ch, title):
    t = title.lower()
    for name, pat in (FC if ch == "fc" else NBA):
        if re.search(pat, t):
            return name
    return ""


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    cols = list(rows[0].keys())
    todo = [r for r in rows if not r["shape"].strip()]
    filled, left = [], []
    for r in todo:
        s = shape_of(r["channel"], r["title"])
        (filled if s else left).append((r, s))
    print(f"rows {len(rows)}; blank shape {len(todo)}; labelled by rule {len(filled)}; left blank {len(left)}; blank lane {sum(1 for r in rows if not r['lane'].strip())}")
    random.seed(5)
    print("spot check (12 random):")
    for r, s in random.sample(filled, min(12, len(filled))):
        print(f"  [{s}] {r['channel']} {r['posted']} {r['title'][:70]}")
    print("left blank (no rule matched), first 8:")
    for r, s in left[:8]:
        print(f"  {r['channel']} {r['posted']} {r['title'][:70]}")
    if a.apply:
        n = 0
        for r, s in filled:
            r["shape"] = s
            if not r["lane"].strip():
                r["lane"] = s
            n += 1
        with open(CSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
        print(f"wrote {n} labels to {CSV}")


if __name__ == "__main__":
    main()
