"""Fit a Short's tags to YouTube's 500-character box, capped at 490 (owner, Oct 24 2026).

  python Tools/tags_fit.py "sga, sga streak, wilt chamberlain record, ..."      # most important first
  python Tools/tags_fit.py --file tags.txt                                       # one tag per line or comma-separated

YouTube's counter adds quotes around every tag that contains a space, and counts the commas, so "nba history" costs 13 + 1.
Keeps the tags in your order, drops duplicates, skips any tag that would push the total over the cap (a later, shorter one can
still fit), and prints the line to paste plus its count.
"""
import argparse, sys

CAP = 490


def cost(tag):
    return len(tag) + (2 if " " in tag else 0)


def fit(tags, cap=CAP):
    out, seen, total = [], set(), -1  # -1: n tags need n-1 commas
    for t in (x.strip().lower() for x in tags):
        if not t or t in seen:
            continue
        if total + 1 + cost(t) <= cap:
            out.append(t); seen.add(t); total += 1 + cost(t)
    return out, max(total, 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tags", nargs="?", help="comma-separated tags, most important first")
    ap.add_argument("--file")
    ap.add_argument("--cap", type=int, default=CAP)
    a = ap.parse_args()
    raw = open(a.file, encoding="utf-8").read() if a.file else (a.tags or sys.stdin.read())
    tags, n = fit(raw.replace("\n", ",").split(","), a.cap)
    dropped = len([t for t in raw.replace("\n", ",").split(",") if t.strip()]) - len(tags)
    print(", ".join(tags))
    print(f"{n} of {a.cap} characters (YouTube's count), {len(tags)} tags, {dropped} left out", file=sys.stderr)


if __name__ == "__main__":
    main()
