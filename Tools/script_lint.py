"""Objective script checks that feed the Script Critic (Tools/script_critic.md). It does NOT judge whether a story is good.

  python Tools/script_lint.py "<Short folder>/script.txt" [more scripts...]

Reports: spoken words and estimated length at the house pace (225 wpm), the first sentence (words, the second it ends, and the
hook flags calibrated on the Oct 15 Studio export: number-led, list-like, no absolute claim, too long),
numbers per sentence (stacked numbers are hard to hear), jargon a casual fan may not know, names missing from
pronunciation.json, contractions, sentence-length spread, repeated content words, and endings that ask a question or a CTA.
Each finding is a RISK for the critic to weigh, not a verdict.

Nov 7 (efficiency review): it is also the PRE-VOICE GATE. FIX lines mean "do not spend voice credits yet" and the exit code is 1:
  - length from the house pace measured on 45 built Shorts after tighten_voice (median 234 wpm, range 220-250, both channels):
    NBA FIX outside about 16-28 s, warn outside 20-25 s (rule S2); FC FIX over 240 or under 185 words, warn if it may pass 59.5 s or
    fall under 50 s (rule F2; qa_short fails a story outside 50-59.9 s);
  - line 1 over 11 words (rule S1); a filler first word (qa_short fails it); a last line that asks a question or a CTA (rules: end on
    the payoff); a score or range written "3-0" outside braces (the voice says "three minus zero": write {3-0|three-nil});
  - warn: time-bound words ("last night"; qa_final fails them 30 h after the voice), and the lab's predicted score (under 35 = filler).
  python Tools/script_lint.py "<folder>/script.txt"              # risks + gate, exit 1 on FIX
  python Tools/script_lint.py "<folder>/script.txt" --format42   # also the #42 FORMAT checklist (was always printed; noise otherwise)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WPM = 234  # Nov 7: measured on 45 built Shorts after tighten_voice (was 225)
WPM_FAST, WPM_SLOW = 250, 220
FILLER = {"so", "look", "that's", "thats", "mate", "um", "uh", "well", "okay", "hey", "today", "welcome"}  # = qa_short.FILLER
TIMEBOUND = r"\b(last night|tonight|yesterday|this morning|on (?:monday|tuesday|wednesday|thursday|friday|saturday|sunday) night)\b"
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
    if len(w) >= 12:  # Nov 3 hook study (n=21, [S]): line 1 of 12+ words engaged 0.490 (n=6) vs 0.557 under 12 words (n=15)
        f.append(f"{len(w)} words: line 1 of 12+ words engaged 0.490 vs 0.557 for under 12 (n=21 Shorts, Nov 3 hook study); cut to under 12")
    return f


def format42(disp):
    """Checks for THE #42 FORMAT (Library/THE 42 FORMAT.md): accusation superlative in line 1, the count as its own sentence,
    a paradox 'And he's...' line, a 'So is he ...? No.' turn, a flip that ends on a number, 65-85 spoken words."""
    sents = [s.strip() for s in re.split(r"(?<=[.?!:])\s+", disp) if s.strip()]
    low = [s.lower() for s in sents]
    say = len(re.findall(r"[A-Za-z0-9']+", disp))
    checks = {
        "line 1 is a 'more than anyone / most in NBA history' accusation": bool(low) and bool(re.search(r"(more|most|fewer)\b.*(than anyone|in nba history|ever)", low[0])),
        "the count is its own sentence (2nd)": len(sents) > 1 and bool(re.fullmatch(r"[\d,.%]+\.?", sents[1].strip())) or (len(low) > 1 and len(low[1].split()) <= 6 and bool(re.search(r"\d|" + NW, low[1]))),
        "a paradox line 'And he's / And he is ...' by sentence 4": any(re.match(r"and (he|she)('s| is| was| has)", s) for s in low[1:4]),
        "a turn 'So is/was he ...? No.'": any(re.match(r"so (is|was|does|did) ", s) and s.endswith("?") for s in low) and any(s in ("no.", "no!") for s in low),
        "the last sentence carries the flip number": bool(sents) and bool(re.search(r"\d|\b(" + NW + r")\b", sents[-1].lower())),
        "65-85 spoken words": 65 <= say <= 85,
    }
    return {"ok": all(checks.values()), "checks": checks}


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
        if mean < 8 and not format42(disp)["ok"]: risks.append(f"short choppy sentences (mean {mean:.1f} words): the fact-chain style our weak Shorts used (not a risk inside THE #42 FORMAT, where #42 averaged 6.3 words)")
    words = [w for w in re.findall(r"[a-z']+", low) if w not in STOP and len(w) > 3]
    rep = sorted({w for w in words if words.count(w) >= 3})
    if rep: risks.append("repeated words (3+): " + ", ".join(rep))
    # Readability (Growth Study, Nov 3 2026: Jenny Hoyos checks every script for about a 5th-grade level; one jargon word moved hers
    # from grade 5 to 8). Flesch-Kincaid grade on the spoken words; capitalised names are skipped (a star's name is not jargon).
    def syl(w):
        w = w.lower().strip("'")
        n = len(re.findall(r"[aeiouy]+", w)) - (1 if w.endswith("e") and not w.endswith(("le", "ee")) and len(w) > 3 else 0)
        return max(1, n)
    plain = [w for w in re.findall(r"[A-Za-z']+", disp) if not w[0].isupper()]
    if plain and sents:
        grade = 0.39 * (len(re.findall(r"[A-Za-z']+", disp)) / len(sents)) + 11.8 * (sum(map(syl, plain)) / len(plain)) - 15.59
        out["reading_grade"] = round(grade, 1)
        if grade > 6:
            longw = sorted({w.lower() for w in plain if syl(w) >= 3}, key=lambda w: -syl(w))[:6]
            risks.append(f"reading level about grade {grade:.1f} (aim 6 or under): swap the long words for plain ones: {', '.join(longw) or 'shorter sentences'}")
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


def channel_of(path):
    return "fc" if "soccer channel" in os.path.abspath(path).lower().replace("\\", "/") else "nba"


def gate(path, r=None):
    """Pre-voice gate (Nov 7): (fix, warn) lists. A FIX costs a re-voice later; fixing the text now costs nothing."""
    r = r or lint(path)
    raw = open(path, encoding="utf-8-sig").read().strip()
    disp, say = shown(raw), spoken(raw)
    ch, n = channel_of(path), r["spoken_words"]
    fix, warn = [], []
    est = lambda w: n / w * 60 + 0.3
    if ch == "nba":
        if est(WPM_FAST) > 28 or est(WPM_SLOW) < 16:
            fix.append(f"{n} words is about {est(WPM):.0f} s ({est(WPM_FAST):.0f}-{est(WPM_SLOW):.0f} s): NBA target 20-25 s (rule S2; 25 s or less had 7.1K vs 3.0K views); aim for 78-97 words")
        elif not (20 <= est(WPM) <= 25.5):
            warn.append(f"{n} words is about {est(WPM):.1f} s: NBA target 20-25 s (78-97 words)")
    else:
        if n > 240 or n < 185:
            fix.append(f"{n} words: FC scripts run 190-240 words (rule F2; about {est(WPM):.0f} s; qa_short fails a story outside 50-59.9 s)")
        elif est(WPM) > 59.5:
            fix.append(f"{n} words is about {est(WPM):.1f} s at the house pace (234 wpm): over 59.5 s shows as 1:00. Cut a sentence (aim 200-225 words)")
        elif est(WPM_SLOW) > 59.5:
            warn.append(f"{n} words could run {est(WPM_SLOW):.1f} s at a slow take (220 wpm): over 59.5 s shows as 1:00; cut a sentence now, it is free")
        elif est(WPM_FAST) < 50:
            warn.append(f"{n} words could run only {est(WPM_FAST):.1f} s at a fast take (250 wpm): under the 50 s story floor")
    first = re.split(r"(?<=[.?!])\s+", disp.strip())[0] if disp.strip() else ""
    fw = len(re.findall(r"[A-Za-z0-9'$%-]+", first))
    if fw > 11:
        fix.append(f"line 1 has {fw} words (rule S1: 11 or fewer; 12+ engaged 0.490 vs 0.557): '{first[:70]}'")
    w0 = re.sub(r"[^a-z']", "", (say.split() or [""])[0].lower())
    if w0 in FILLER:
        fix.append(f"the first spoken word is '{w0}' (qa_short fails a filler opener: start on the name, number or stakes)")
    sents = [s.strip() for s in re.split(r"(?<=[.?!])\s+", disp) if s.strip()]
    if sents and (sents[-1].endswith("?") or any(c in sents[-1].lower() for c in CTA)):
        fix.append(f"the last line is a question or a CTA ('{sents[-1][:60]}'): end on the payoff")
    bare = re.sub(r"\{[^{}]*\}", " ", raw)
    sc = sorted(set(re.findall(r"(?<![\w$.])\d{1,2}\s?[-\u2013]\s?\d{1,2}(?![\w%])", bare)))
    if sc:
        fix.append(f"score(s) {', '.join(sc)} outside braces: the voice can read them as 'minus'. Write {{{sc[0]}|{num_words(sc[0])}}}")
    tb = sorted(set(m.lower() for m in re.findall(TIMEBOUND, say, re.I)))
    if tb:
        warn.append(f"time-bound words {tb}: voice within 30 h of the slot (qa_final fails it later), or write it time-free")
    try:
        sys.path.insert(0, HERE)
        import lab
        pr = lab.predict_folder(os.path.dirname(os.path.abspath(path)))
        msg = f"predicted score {pr['score']} (about {pr['predicted']:,} views at 72 h)" + (": " + ", ".join(pr["why"]) if isinstance(pr.get("why"), list) and pr["why"] else "")
        (warn if pr["score"] < 35 else r.setdefault("info", [])).append(msg + (" - under 35 is filler (rule Q2)" if pr["score"] < 35 else ""))
    except Exception:
        pass
    return fix, warn


def num_words(s):
    ones = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    def w(n):
        return ones[n] if n < 20 else tens[n // 10] + ("-" + ones[n % 10] if n % 10 else "")
    a, b = [int(x) for x in re.findall(r"\d+", s)[:2]]
    return f"{w(a)}-{'nil' if b == 0 else w(b)}"


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    any_fix = False
    for p in args:
        r = lint(p)
        print(f"\n== {p}\n{r['spoken_words']} spoken words, about {r['est_seconds']} s at {WPM} wpm; first sentence ends about {r['first_sentence_ends_s']} s")
        print("first sentence:", r["first_sentence"])
        for x in r["risks"]:
            print("  RISK", x)
        fx, wn = gate(p, r)
        for x in fx:
            print("  FIX ", x)
        for x in wn:
            print("  WARN", x)
        for x in r.get("info", []):
            print("  info", x)
        print("  PRE-VOICE GATE:", "FIX the lines above before voicing (voice credits)" if fx else "PASS")
        any_fix |= bool(fx)
        if "--format42" in sys.argv:
            f = format42(shown(open(p, encoding="utf-8-sig").read().strip()))
            print("  THE #42 FORMAT:", "FITS" if f["ok"] else "does not fit")
            for k, v in f["checks"].items():
                print("    " + ("ok  " if v else "MISS") + " " + k)
    sys.exit(1 if any_fix else 0)
