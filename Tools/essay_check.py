r"""Essay checker (Nov 6, 2026): objective, local, offline feedback on a college essay draft. It never rewrites anything.

  python Tools/essay_check.py "<draft.txt>" [--limit 650] [--min 250]

Reports: word count vs the limit; sentence-length spread (a flat rhythm reads dull); repeated sentence openers; "I" density; filler and cliche phrases
(passionate, hard work, "I learned that", "ever since I was", "changed my life", dictionary/quotation openers); tell-words that should be a scene
(realized, learned, grateful, inspired); vague nouns (things, stuff, a lot, very, really); passive voice hints; paragraph count; numbers/proper nouns
(specifics) per 100 words; the first and last sentence so you can judge the opening and ending; the 5 most repeated content words.
The output is a list of lines to look at, not a score. Nothing leaves the machine; the file is only read.
"""
import argparse, collections, re, statistics as st, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CLICHE = ["passionate", "passion for", "hard work", "i learned that", "ever since i was", "changed my life", "life-changing", "step out of my comfort zone",
          "make a difference", "give back", "in today's society", "since the dawn of time", "webster", "dictionary defines", "thrive", "at the end of the day",
          "journey", "overcame", "taught me the value", "never give up", "dream big", "a whole new world"]
TELL = ["realized", "realised", "learned", "grateful", "inspired", "i understood", "i discovered", "taught me"]
VAGUE = ["things", "thing", "stuff", "a lot", "very", "really", "so many", "many people", "everyone", "always", "amazing", "great", "good"]
STOP = set("the a an and or but of to in on for with at by from as is was were are be been it its i my me we our you your he his she her they their this that these those not no so if then than into out up down over just have has had do did does would could should can will".split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--limit", type=int, default=650)
    ap.add_argument("--min", type=int, default=250)
    a = ap.parse_args()
    t = open(a.file, encoding="utf-8-sig").read().strip()
    words = re.findall(r"[A-Za-z0-9'’-]+", t)
    n = len(words)
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", t)) if s.strip()]
    paras = [p for p in re.split(r"\n\s*\n", t) if p.strip()]
    print(f"WORDS {n}  (limit {a.limit}, min {a.min})  paragraphs {len(paras)}  sentences {len(sents)}")
    if n > a.limit:
        print(f"  CUT {n - a.limit} words")
    elif n < a.min:
        print(f"  SHORT by {a.min - n} words")
    lens = [len(re.findall(r"[A-Za-z0-9'’-]+", s)) for s in sents]
    if len(lens) > 3:
        sd = st.pstdev(lens)
        print(f"RHYTHM  avg {st.mean(lens):.1f} words/sentence, spread {sd:.1f}" + ("  -> flat: mix short punches with longer lines" if sd < 5 else "  -> good variety"))
        print("  longest:", max(lens), "words:", sents[lens.index(max(lens))][:110])
    op = collections.Counter(" ".join(s.split()[:2]).lower() for s in sents)
    rep = [(k, v) for k, v in op.items() if v >= 3]
    if rep:
        print("OPENERS repeated 3+ times:", ", ".join(f"'{k}' x{v}" for k, v in rep))
    i_rate = sum(1 for w in words if w in ("I", "I'm", "I've", "I'd", "I'll")) / max(1, n) * 100
    print(f"I-DENSITY {i_rate:.1f} per 100 words" + ("  -> many sentences start with I; lead with the scene sometimes" if i_rate > 7 else ""))
    low = t.lower()
    hits = [c for c in CLICHE if c in low]
    print("CLICHES:", ", ".join(hits) if hits else "none found")
    tells = [(w, low.count(w)) for w in TELL if w in low]
    print("TELL-WORDS (turn into a scene):", ", ".join(f"{w} x{c}" for w, c in tells) if tells else "none")
    vg = [(w, len(re.findall(r"\b" + re.escape(w) + r"\b", low))) for w in VAGUE]
    vg = [(w, c) for w, c in vg if c]
    print("VAGUE words:", ", ".join(f"{w} x{c}" for w, c in vg) if vg else "none")
    passive = re.findall(r"\b(?:was|were|been|being|is|are)\s+\w+ed\b", t)
    print(f"PASSIVE hints: {len(passive)}" + (f"  e.g. '{passive[0]}'" if passive else ""))
    spec = len(re.findall(r"\b\d[\d,.$%]*\b", t)) + len(re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]+", t))
    print(f"SPECIFICS (numbers and names) per 100 words: {spec / max(1, n) * 100:.1f}" + ("  -> add concrete numbers, names, places" if spec / max(1, n) * 100 < 4 else ""))
    cw = collections.Counter(w.lower() for w in words if w.lower() not in STOP and len(w) > 3)
    print("MOST REPEATED:", ", ".join(f"{w} x{c}" for w, c in cw.most_common(5) if c > 2) or "none over 2")
    if sents:
        print("\nFIRST SENTENCE:", sents[0])
        print("LAST SENTENCE: ", sents[-1])
        print("Ask: does the first line put a reader inside a moment? does the last line point forward instead of summarising?")


if __name__ == "__main__":
    main()
