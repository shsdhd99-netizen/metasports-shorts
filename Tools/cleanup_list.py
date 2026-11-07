"""List (never delete) the heavy folders of Shorts that are already posted, so the owner can free disk by exact path (Nov 5, 2026; backlog item).

  python Tools/cleanup_list.py [--days 7] [--min-mb 50] [--write "Research Notes/Cleanup Candidates.txt"]

A Short counts as posted when Research Notes/Experiments.csv has a video_id and a `posted` date at least --days old AND its number or S-code
matches the Short's folder name. Only src/, clips/, _rawclips/, long/ and *.mp4 inside those folders are listed (the DRAFT and final files of
a posted Short are listed separately as "keep until the owner says"). Exact paths only: nothing here deletes anything, and a folder that
cannot be matched to a posted Short is never listed.
"""
import argparse, csv, datetime, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    return sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(path) for f in fs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--min-mb", type=float, default=50)
    ap.add_argument("--write")
    a = ap.parse_args()
    cut = datetime.date.today() - datetime.timedelta(days=a.days)
    posted = set()
    for r in csv.DictReader(open(os.path.join(ROOT, "Research Notes", "Experiments.csv"), encoding="utf-8")):
        if r["video_id"].strip() and r["posted"] and datetime.date.fromisoformat(r["posted"]) <= cut:
            m = re.match(r"\s*(?:#)?(S?\d+)\b", r["title"])
            posted.add((r["channel"], r["posted"], r["title"][:40]))
    rows, total = [], 0
    folders = [(p, "nba") for p in glob.glob(os.path.join(ROOT, "Productions", "MetaSports", "*"))] + \
              [(p, "fc") for p in glob.glob(os.path.join(ROOT, "Soccer Channel", "Productions", "*"))]
    for f, ch in sorted(folders):
        name = os.path.basename(f)
        m = re.match(r"(\d{4}-\d{2}-\d{2}) (?:A2 )?(S?\d+)\b", name)
        if not m or datetime.date.fromisoformat(m.group(1)) > cut:
            continue
        for sub in ("src", "clips", "_rawclips", "long"):
            p = os.path.join(f, sub)
            if os.path.isdir(p):
                mb = size(p) / 2**20
                if mb >= a.min_mb:
                    rows.append((mb, p)); total += mb
    rows.sort(reverse=True)
    out = [f"{mb:8.0f} MB  {p}" for mb, p in rows] + [f"TOTAL {total:,.0f} MB in {len(rows)} folders (posted/older than {a.days} days by folder date)"]
    print("\n".join(out))
    if a.write:
        open(os.path.join(ROOT, a.write), "w", encoding="utf-8").write(
            "Owner: delete only the exact folders you approve; each is regenerable source/cut footage of an older Short.\n" + "\n".join(out) + "\n")


if __name__ == "__main__":
    main()
