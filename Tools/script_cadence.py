"""Does this script read like a person talking, or like an AI narrator? (free, local; same rules as Everygen's check_voice_cadence)

  python Tools/script_cadence.py "<Short folder>/script.txt"
Errors: no long flowing line (>= 14 words) or no punchy line (<= 4 words). Warnings: few contractions (a real commentator says 'he's', 'it's', 'didn't'),
sentence lengths too even (stdev < 3.0), every sentence starting the same way, stock filler phrases. Fix errors before recording; warnings are advice.
"""
import re, sys
FILLER = ["in conclusion", "it is worth noting", "it's worth noting", "needless to say", "at the end of the day", "without further ado", "let's dive in", "buckle up", "game changer", "in today's video", "stay tuned"]


def analyse(text):
    text = re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", text)
    sents = [s.strip() for s in re.split(r"(?<=[.?!])\s+", text.strip()) if s.strip()]
    lens = [len(s.split()) for s in sents]
    contr = len(re.findall(r"\b\w+(?:'s|'t|'re|'ve|'ll|'d|'m)\b", text, re.I))
    mean = sum(lens) / len(lens)
    sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
    starters = [s.split()[0].lower() for s in sents]
    err, warn = [], []
    if max(lens) < 14: err.append(f"no long flowing line (>= 14 words); lengths {lens}")
    if min(lens) > 4: err.append(f"no punchy line (<= 4 words); lengths {lens}")
    if contr < max(1, len(sents) // 4): warn.append(f"only {contr} contraction(s) across {len(sents)} sentences: a person contracts more")
    if sd < 3.0: warn.append(f"cadence is even (stdev {sd:.1f}): vary the lengths")
    if len(set(starters)) < len(starters) * 0.6: warn.append("many sentences start with the same word")
    for f in FILLER:
        if f in text.lower(): warn.append(f"filler phrase: '{f}'")
    return dict(sentences=len(sents), lengths=lens, stdev=round(sd, 1), contractions=contr, errors=err, warnings=warn)


if __name__ == "__main__":
    r = analyse(open(sys.argv[1], encoding="utf-8-sig").read())
    print(("OK" if not r["errors"] else "FIX"), {k: r[k] for k in ("sentences", "stdev", "contractions")})
    for e in r["errors"]: print("  ERROR", e)
    for w in r["warnings"]: print("  warn ", w)
