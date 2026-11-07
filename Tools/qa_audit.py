"""QA audit (Nov 5, 2026; owner: "make sure QA is always up to date and improved every single day").

  python Tools/qa_audit.py            # writes Research Notes/QA Audit.md and prints the top recurring findings

Reads every saved QA output (_qa*.txt in Short folders), normalises each warn/FIX/FAIL line (numbers, clip names and times removed) and ranks them by
how often they fire and in how many Shorts. A finding that fires in most Shorts is either noise (loosen it) or a process flaw (move the check EARLIER:
into the script, the cut plan or the clip cutter, see precut_lint.py). Every day: read this, change ONE check (add, tighten, loosen or move earlier),
and write one line in Research Notes/QA Changelog.md with the reason and the evidence.
"""
import collections, glob, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(line):
    t = re.sub(r"\b[A-Z]\d{1,3}(?:\.mp4)?\b", "<clip>", line)
    t = re.sub(r"\d+(?:\.\d+)?", "#", t)
    t = re.sub(r"'[^']{3,60}'", "'..'", t)
    return t.strip()[:150]


def main():
    files = glob.glob(os.path.join(ROOT, "Productions", "*", "*", "_qa*.txt")) + glob.glob(os.path.join(ROOT, "Soccer Channel", "Productions", "*", "_qa*.txt"))
    cnt, shorts, firsts = collections.Counter(), collections.defaultdict(set), collections.Counter()
    verdicts = collections.Counter()
    for f in files:
        folder = os.path.dirname(f)
        lines = open(f, encoding="utf-8", errors="replace").read().splitlines()
        if lines:
            verdicts[lines[0].strip()[:12]] += 1
        for l in lines:
            m = re.match(r"\s*(warn|FIX|FAIL)\s+(.*)", l)
            if m:
                k = (m.group(1), norm(m.group(2)))
                cnt[k] += 1; shorts[k].add(folder)
    out = ["# QA audit (auto-written by Tools/qa_audit.py)", "",
           f"{len(files)} saved QA outputs; verdict counts: {dict(verdicts)}.", "",
           "| Level | Finding (normalised) | Fired | In Shorts | Read |", "|---|---|---|---|---|"]
    for (lvl, txt), n in cnt.most_common(25):
        ns = len(shorts[(lvl, txt)])
        read = "noise or process flaw: fires in most Shorts" if ns >= 0.5 * max(1, len({os.path.dirname(f) for f in files})) else ("recurring" if ns >= 3 else "rare")
        out.append(f"| {lvl} | {txt.replace('|', '/')} | {n} | {ns} | {read} |")
    open(os.path.join(ROOT, "Research Notes", "QA Audit.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out[:22]))


if __name__ == "__main__":
    main()
