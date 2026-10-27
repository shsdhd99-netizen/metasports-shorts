"""Script study: what the narration of top Shorts does differently from the bottom ones (Gemini transcripts, no re-watching).

Why (Oct 27 2026): the owner asked to "review more shorts, and competitor channel editing formats, and scripts". The watch
studies (Tools/watch_study.py) already saved each Short's word-for-word narration in its report, so this reads those
transcripts instead of watching anything again.

Usage:
  python Tools/script_study.py                      # every study CSV in 'Research Notes/Watch Study/'
  python Tools/script_study.py --no-gemini          # simple counts only, no Gemini call
Two layers:
  1. Counts from the text: words, words per second, first-sentence length, a number or a question in line 1, "you",
     where the first turn word (but / until / turns out / however) falls, numbers spoken, a follow/subscribe ask.
  2. Gemini reads the scripts as text (about 15 per request, free tier) and labels the hook type, the payoff type, whether
     there is a twist, and the tone.
Output: 'Research Notes/Watch Study/Script study (<date>).csv' and '... summary.md', plus 'Script Library (<date>).md' with
the full narration of the 20 best-performing Shorts (by views vs their channel's median), for reference when writing.
Every label is [S] (model-coded or from a model's transcript). Transcripts of music-only or caption-only Shorts are skipped.
"""
import argparse, csv, datetime, glob, json, os, re, statistics, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_watch as w

STUDY = os.path.join(w.ROOT, "Research Notes", "Watch Study")
REPORTS = os.path.join(w.ROOT, "Research Notes", "Watch Reports")
TURN = re.compile(r"\b(but|until|turns out|however|instead|except|then)\b", re.I)
NUM = re.compile(r"\b(\d[\d,.]*|one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion)\b", re.I)
CTA = re.compile(r"\b(subscribe|follow (for|me)|like and|comment (below|your)|let me know)\b", re.I)

LABEL_PROMPT = """You label narration scripts from YouTube Shorts. For EACH script below, return one JSON object with:
- id: the id given
- hook_type: one of "question", "bold_claim", "scene", "number", "promise" (tells you something is coming), "name_intro"
  (opens by naming a person), "other"
- hook_words: the first sentence, exactly
- has_twist: true/false (a turn that changes what the viewer expected)
- payoff_type: how it ends: "twist", "number", "quote", "punchline", "emotional", "open_question", "none"
- tone: one of "funny", "hype", "dramatic", "informative", "wholesome"
- beats: how many distinct story steps (count)
- why_it_holds: one short phrase about what keeps a viewer listening
Return a JSON array only, one object per script, same order.

SCRIPTS:
"""


def sentences(t):
    return [s for s in re.split(r"(?<=[.?!])\s+", t.strip()) if s]


def counts(script, length):
    words = script.split()
    ss = sentences(script)
    first = ss[0] if ss else ""
    m = TURN.search(script)
    return {
        "words": len(words),
        "words_per_s": round(len(words) / length, 2) if length else None,
        "first_sentence_words": len(first.split()),
        "line1_number": bool(NUM.search(first)),
        "line1_question": first.endswith("?"),
        "says_you": bool(re.search(r"\byou\b", script, re.I)),
        "line1_you": bool(re.search(r"\byou\b", first, re.I)),
        "turn_at": round(len(script[:m.start()].split()) / max(1, len(words)), 2) if m else None,
        "numbers_spoken": len(NUM.findall(script)),
        "cta": bool(CTA.search(script)),
        "last_sentence_words": len(ss[-1].split()) if ss else 0,
        "ends_question": bool(ss) and ss[-1].endswith("?"),
    }


def label(batch, models):
    text = LABEL_PROMPT + "\n\n".join(f"[id {i}]\n{s}" for i, s in batch)
    body = {"contents": [{"parts": [{"text": text}]}],
            "generationConfig": {"temperature": 0.1, "responseMimeType": "application/json"}}
    for attempt in range(4):
        try:
            r, _ = w.generate(models, body)
            out = json.loads("".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"]))
            return {str(o.get("id")): o for o in out if isinstance(o, dict)}
        except (SystemExit, json.JSONDecodeError, KeyError, IndexError) as e:
            if "daily" in str(e).lower():
                raise
            time.sleep(30 * (attempt + 1))
    return {}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-gemini", action="store_true")
    ap.add_argument("--batch", type=int, default=15)
    a = ap.parse_args()
    rows, seen = [], set()
    for f in sorted(glob.glob(os.path.join(STUDY, "*top vs bottom*.csv")) + glob.glob(os.path.join(STUDY, "Format survey*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r["id"] in seen:
                continue
            p = os.path.join(REPORTS, r["id"] + ".json")
            if not os.path.exists(p):
                continue
            rep = json.load(open(p, encoding="utf-8"))
            script = str(rep.get("script") or "").strip()
            length = rep.get("length_s") if isinstance(rep.get("length_s"), (int, float)) else None
            if len(script.split()) < 15 or script.lower() in ("none", "unknown"):
                continue  # music-only or caption-only Short
            seen.add(r["id"])
            family = "format" if "Format survey" in f else ("soccer" if "Soccer" in f else "nba")
            rows.append({"id": r["id"], "channel": r["channel"], "family": family, "group": r["group"],
                         "views": int(r["views"]), "x_median": float(r["x_median"] or 0), "title": r["title"],
                         "length_s": length, **counts(script, length), "_script": script})
    if not rows:
        sys.exit("no transcripts found; run Tools/watch_study.py first")
    if not a.no_gemini:
        models = w.pick_models(None)
        for i in range(0, len(rows), a.batch):
            chunk = rows[i:i + a.batch]
            got = label([(r["id"], r["_script"]) for r in chunk], models)
            for r in chunk:
                g = got.get(r["id"], {})
                for k in ("hook_type", "has_twist", "payoff_type", "tone", "beats", "why_it_holds", "hook_words"):
                    r[k] = g.get(k)
            time.sleep(4)
    today = datetime.date.today().isoformat()
    stem = os.path.join(STUDY, f"Script study ({today})")
    keys = [k for k in rows[0] if not k.startswith("_")] + [k for k in ("hook_type", "has_twist", "payoff_type", "tone", "beats",
                                                                         "why_it_holds", "hook_words") if k not in rows[0]]
    with open(stem + ".csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore")
        wr.writeheader()
        wr.writerows(rows)

    def med(rs, k):
        v = [float(r[k]) for r in rs if isinstance(r.get(k), (int, float)) and not isinstance(r.get(k), bool)]
        return f"{statistics.median(v):g}" if v else "-"

    def pct(rs, k):
        v = [r[k] for r in rs if isinstance(r.get(k), bool)]
        return f"{100 * sum(v) // len(v)}% ({len(v)})" if v else "-"

    def dist(rs, k):
        vals = [str(r.get(k)) for r in rs if r.get(k) is not None]
        return ", ".join(f"{v} {vals.count(v)}" for v in sorted(set(vals), key=lambda x: -vals.count(x))) or "-"

    out = [f"# Script study ({today})\n",
           "Narration transcripts from the Gemini watch studies (no re-watching). Counts come from the text; hook, payoff, twist "
           "and tone are Gemini labels. All [S]. Groups: each channel's top and bottom Shorts by views (narrated studies); "
           "the format survey has top Shorts only.\n"]
    for fam in ("nba", "soccer", "format"):
        rs = [r for r in rows if r["family"] == fam]
        if not rs:
            continue
        top, bot = [r for r in rs if r["group"] == "top"], [r for r in rs if r["group"] == "bottom"]
        out.append(f"\n## {fam.upper()} (top n={len(top)}, bottom n={len(bot)})\n\n| Feature | Top | Bottom |\n|---|---|---|")
        for k in ("words", "words_per_s", "length_s", "first_sentence_words", "turn_at", "numbers_spoken", "last_sentence_words", "beats"):
            out.append(f"| {k} (median) | {med(top, k)} | {med(bot, k)} |")
        for k in ("line1_number", "line1_question", "line1_you", "says_you", "cta", "ends_question", "has_twist"):
            out.append(f"| {k} (% yes) | {pct(top, k)} | {pct(bot, k)} |")
        for k in ("hook_type", "payoff_type", "tone"):
            out.append(f"| {k} | {dist(top, k)} | {dist(bot, k)} |")
    open(stem + " summary.md", "w", encoding="utf-8").write("\n".join(out) + "\n")

    best = sorted([r for r in rows if r["group"] == "top"], key=lambda r: -r["x_median"])[:20]
    lib = [f"# Script library ({today}): the 20 best-performing narrated scripts in our studies\n",
           "Ranked by views against their own channel's median. Narration as Gemini transcribed it ([S]: small slips "
           "possible). For reference only: never copy a script; learn the shape.\n"]
    for r in best:
        lib.append(f"\n## {r['title']}\n{r['channel']} · {r['views']:,} views ({r['x_median']:g}x its channel's median) · "
                   f"{r['length_s']} s · {r['words']} words · hook: {r.get('hook_type')} · payoff: {r.get('payoff_type')}\n\n"
                   f"> {r['_script']}\n")
    open(os.path.join(STUDY, f"Script Library ({today}).md"), "w", encoding="utf-8").write("\n".join(lib))
    print("\n".join(out))
    print("wrote", os.path.relpath(stem + ".csv", w.ROOT))


if __name__ == "__main__":
    main()
