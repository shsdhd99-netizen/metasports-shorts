"""Objective script checks that feed the Script Critic (Tools/script_critic.md). It does NOT judge whether a story is good.

  python Tools/script_lint.py "<Short folder>/script.txt" [more scripts...]

Reports: spoken words and estimated length at the house pace (225 wpm), the first sentence (words, the second it ends, and the
hook flags calibrated on the Oct 15 Studio export: number-led, list-like, no absolute claim, too long),
numbers per sentence (stacked numbers are hard to hear), jargon a casual fan may not know, names missing from
pronunciation.json, contractions, sentence-length spread, repeated content words, and endings that ask a question or a CTA.
Each finding is a RISK for the critic to weigh, not a verdict.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WPM = 225
JARGON = ["preseason", "g league", "two-way", "waived", "cash considerations", "luxury tax", "apron", "bird rights", "rookie scale",
          "restricted free agent", "sign-and-trade", "exhibit 10", "hardship", "per 36", "true shooting", "plus-minus", "lottery odds",
          "regular-season", "transition take", "flagrant", "technical foul", "eligib"]
CTA = ["subscribe", "follow for", "like and", "comment below", "let me know", "what do you think", "drop a"]
STOP = set("the a an and or but so of in on at to for with is was are were be been he she it they his her its their this that these those "
           "just than then from by as not no yes did does do has have had who what when where why how one two three four".split())
NW = "zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion"
NUMWORD = r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b"


def spoken(text):
    return re.sub(r"\{([^|{}]+)\|([^{}]+)\}", r"\2", text)


def shown(text):
    return re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", text)


ABSOLUTE = r"\b(only|every|never|nobody|no one|no other|first|last|just|until|ever|still|always|all-time|record|can't|cannot|isn't allowed|not allowed|banned|refused|secret|hidden|than anyone|in nba history|is not|isn't)\b"


def hook_flags(first):
    """Line 1 checks from the Studio export (audit §13): high 'stayed to watch' openings make one absolute, curious claim about a
    famous name in one sentence; low ones lead with a number, list details, or centre a player casual fans don't know.
    The last one needs a human: the critic's Hook score covers it."""
    f, low = [], first.lower()
    w = re.findall(r"[A-Za-z0-9'$%-]+", first)
    if w and (re.match(r"[$\d]", w[0]) or (re.fullmatch(r"(?:" + NW + r")(?:-(?:" + NW + r"))?", w[0].lower()) and w[0].lower() != "one")):
        f.append(f"opens with a number ('{w[0]}'): number-led openings stayed 48-59%")
    if first.count(",") >= 2 and re.search(r",\s*(and|or)\b", low):
        f.append("reads as a list (2+ commas and 'and'): the penalty-list opening stayed 50%")
    if not re.search(ABSOLUTE, low):
        f.append("no absolute or curious claim word (only, every, never... until, just, first, last...): 73%+ stayed openings all had one")
    if len(w) > 20:
        f.append(f"{len(w)} words: one short sentence lands faster")
    return f


def lint(path):
    raw = open(path, encoding="utf-8-sig").read().strip()
    disp, say = shown(raw), spoken(raw)
    sents = [s.strip() for s in re.split(r"(?<=[.?!])\s+", disp) if s.strip()]
    sw = len(re.findall(r"[A-Za-z0-9']+", say))
    out = {"file": path, "spoken_words": sw, "est_seconds": round(sw / WPM * 60, 1), "sentences": len(sents)}
    first = sents[0] if sents else ""
    raw_sents = [s for s in re.split(r"(?<=[.?!])\s+(?![^{]*\})", raw) if s.strip()]
    fw = len(re.findall(r"[A-Za-z0-9']+", spoken(raw_sents[0]))) if raw_sents else 0
    out["first_sentence"] = first
    out["first_sentence_ends_s"] = round(fw / WPM * 60, 1)
    risks = []
    if out["est_seconds"] > 35: risks.append(f"long: about {out['est_seconds']} s at {WPM} wpm (past the 22-33 s range our data covers; length itself showed no link to views inside it)")
    if out["est_seconds"] < 17: risks.append(f"short: about {out['est_seconds']} s; is there a payoff beat?")
    if out["first_sentence_ends_s"] > 3.5: risks.append(f"first sentence ends at about {out['first_sentence_ends_s']} s (aim for the premise by 3 s)")
    out["hook_flags"] = hook_flags(first)
    risks += ["hook: " + f for f in out["hook_flags"]]
    for i, s in enumerate(sents):
        run = r"\b(?:" + NW + r")(?:[\s-]+(?:and\s+)?(?:" + NW + r"))*\b"  # "six thousand and eighty-one" counts as one number
        n = len(re.findall(r"\d[\d,.%]*", s)) + len(re.findall(run, s.lower()))
        if n >= 3: risks.append(f"sentence {i + 1} stacks {n} numbers: '{s[:60]}'")
    low = disp.lower()
    jj = [j for j in JARGON if j in low]
    if jj: risks.append("jargon a casual fan may not know: " + ", ".join(jj))
    if sents and (sents[-1].endswith("?") or any(c in sents[-1].lower() for c in CTA)): risks.append("ends on a question or CTA")
    contr = len(re.findall(r"\b\w+(?:'s|n't|'re|'ve|'ll|'d|'m)\b", disp, re.I))
    out["contractions"] = contr
    lens = [len(s.split()) for s in sents]
    if lens:
        mean = sum(lens) / len(lens); sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        out["sentence_words"] = lens
        if sd < 3: risks.append(f"even cadence (sentence-length spread {sd:.1f} words): sounds read, not told")
        if mean < 8: risks.append(f"short choppy sentences (mean {mean:.1f} words): the fact-chain style our weak Shorts used")
    words = [w for w in re.findall(r"[a-z']+", low) if w not in STOP and len(w) > 3]
    rep = sorted({w for w in words if words.count(w) >= 3})
    if rep: risks.append("repeated words (3+): " + ", ".join(rep))
    try:
        dic = json.load(open(os.path.join(HERE, "pronunciation.json"), encoding="utf-8"))
        known = set(dic.get("default", {})) | set(dic.get("_notes", {}))
    except Exception:
        known = set()
    hard = re.findall(r"\b[A-Z][a-z]*(?:ic|ić|ovic|unas|un|ama|ounmpo)\b", disp)
    miss = sorted({h for h in hard if h not in known})
    if miss: risks.append("hard names not in pronunciation.json (test them on one line): " + ", ".join(miss))
    out["risks"] = risks
    return out


if __name__ == "__main__":
    for p in sys.argv[1:]:
        r = lint(p)
        print(f"\n== {p}\n{r['spoken_words']} spoken words, about {r['est_seconds']} s at {WPM} wpm; first sentence ends about {r['first_sentence_ends_s']} s")
        print("first sentence:", r["first_sentence"])
        for x in r["risks"]:
            print("  RISK", x)
