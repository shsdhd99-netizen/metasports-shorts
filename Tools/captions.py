"""Burned-in captions for MetaSports Shorts, in the look of your old Shorts (or Coach Clank's).

  python captions.py --folder "<Short folder>"                    # writes captions.ass from words.json
  python captions.py --folder "..." --style clank                 # sentence case, smaller, like Coach Clank
  python captions.py --folder "..." --frame 3.2 --video final_nocap.mp4   # a test picture at 3.2 s
  python captions.py --burn final_nocap.mp4 --ass captions.ass --out final.mp4

Styles
  metasports (default): ALL CAPS, Montserrat Black, white with a thick black outline, 1-3 words a card.
  Spelled numbers stay together ("two hundred nine", "five point four") and a card that is only a number goes green.
                        a little below the middle. Shock words turn red, numbers and big moments green.
  clank:                sentence case, Montserrat Bold, white with a thin outline, 2-5 words, dead centre.
  karaoke (Round 5 test, not yet A/B tested): sentence case, Montserrat Bold 80 px, black outline 6, 2-3 words a card at 54% height,
                        the word being spoken turns yellow (numbers green). One ASS event per word, layout never moves.

To colour a card by hand, put emphasis.json next to words.json:
  {"red": ["nobody"], "green": ["100 voters"], "white": ["first"]}   (matched inside each card's text)
assemble.py runs this for you.
"""
import argparse, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")

STYLES = {
    # font, size, outline, shadow, y (centre of the text, of 1920), max words, max chars, ideal words, caps, pop
    "metasports": dict(font="Montserrat Black", size=86, scalex=95, outline=6, shadow=3, blur=1.2, y=1100, spacing=1, maxw=3, maxc=19, ideal=2.0,
                       caps=True, pop=True, colors=True),
    "clank": dict(font="Montserrat Bold", size=58, scalex=100, outline=3, shadow=1, blur=0.6, y=960, spacing=0, maxw=5, maxc=30, ideal=3.5,
                  caps=False, pop=False, colors=False),
    # Round 5 candidate: sentence case + word-by-word highlight (REBOUND/Hormozi family) with Clank's calm sizing. Needs an A/B test.
    "karaoke": dict(font="Montserrat Bold", size=80, scalex=100, outline=6, shadow=2, blur=0.5, y=1040, spacing=0, maxw=3, maxc=22, ideal=2.4,
                    caps=False, pop=False, colors=False, kara=True),
    # Oct 21: the Ahmed's Goal/Basketball/Business look, measured on their own frames (Research Notes/Story Format Study): TikTok Sans
    # SemiBold, "did not slow down" 514 px wide x 41 px tall at 1080x1920 = size 80, white, thin black outline, centred at y 960,
    # 2-3 words a card as spoken (sentence case, punctuation kept). title_caption.txt (if present) is shown over the spoken title.
    "ahmed": dict(font="TikTok Sans SemiBold", size=80, scalex=100, outline=3.2, shadow=1, blur=0.5, y=960, spacing=0, maxw=3, maxc=20, ideal=2.6,
                  caps=False, pop=False, colors=False, title=True),
}
KARA_HI = "&H000AD6FF&"   # warm yellow FFD60A (ASS is BGR)
KARA_NUM = "&H0040E33A&"  # numbers/money in green so the key figure stays readable
RED = "&H002A2AFF&"    # ASS colours are &HAABBGGRR
GREEN = "&H0040E33A&"

DANGLING = {"the", "a", "an", "of", "to", "in", "on", "at", "for", "with", "by", "from", "and", "or", "but", "nor",
            "his", "her", "their", "its", "my", "your", "our", "this", "that", "these", "those", "every", "each",
            "is", "are", "was", "were", "be", "been", "as", "than", "into", "onto", "over", "under", "about",
            "after", "before", "who", "which", "whose", "where", "when", "if", "so", "just", "very", "most",
            "more", "some", "any", "no", "not", "it's", "he's", "she's", "they're", "we're", "you're", "i'm", "had",
            "has", "have", "will", "would", "could", "should", "can", "did", "does", "do", "got", "get", "put", "per"}
UNITS = {"feet", "foot", "ft", "inches", "inch", "million", "billion", "percent", "points", "point", "rebounds",
         "assists", "blocks", "steals", "years", "year", "seasons", "season", "games", "game", "voters", "votes",
         "wins", "losses", "times", "picks", "pick", "straight", "minutes", "seconds", "players", "teams", "men",
         "titles", "rings", "mvps", "mvp", "first-place", "dollars", "%", "ppg", "days", "months", "-0", "and-0"}
CAPS_STOP = {"The", "And", "But", "So", "You", "He", "His", "It", "In", "Every", "Which", "That", "This", "Until",
             "All", "One", "A", "An", "If", "When", "Then", "Now", "Here's", "There", "They", "We", "I", "Not", "No",
             "Just", "Even", "Only", "What", "Why", "How", "Who", "Because", "After", "Before", "Since", "With", "For",
             "Of", "To", "On", "At", "As", "Or", "Yes", "Today", "Last", "Next", "Most", "Some", "Both", "Each"}
PAIRS = {("free", "throw"), ("free", "throws"), ("three", "point"), ("three-point", "line"), ("no", "one"),
         ("at", "least"), ("first", "round"), ("second", "round"), ("player", "of"), ("of", "the"), ("the", "year"),
         ("all", "star"), ("hall", "of"), ("number", "one"), ("one", "voter"), ("pay", "cut"), ("big", "three")}
SHOCK = {"no", "not", "never", "nobody", "nothing", "none", "zero", "worst", "lost", "lose", "losing", "miss",
         "missed", "misses", "can't", "cannot", "won't", "didn't", "doesn't", "isn't", "wasn't", "aren't", "killed",
         "cut", "banned", "illegal", "fired", "lie", "lying", "fake", "wrong", "until", "except", "weird", "crazy",
         "insane", "impossible", "broke", "broken", "shattered", "airball", "brick", "bricked", "unheard",
         "gone", "traded", "dumped", "ended", "died", "injured", "injury", "ejected", "fined", "suspended", "booed"}
BIG = {"first", "unanimous", "unanimously", "record", "mvp", "mvps", "champion", "champions", "championship",
       "title", "titles", "ring", "rings", "perfect", "greatest", "goat", "undefeated", "superteam", "dynasty",
       "banner", "all-time", "legend", "million", "billion", "youngest", "oldest", "club"}


def bare(w):
    return re.sub(r"[^\w'%$-]+", "", w).lower()


def ends_sentence(w):
    return w.rstrip("\"')”’")[-1:] in ".?!…"


def soft_end(w):
    return w.rstrip("\"')”’")[-1:] in ",;:—–"


NUMWORD = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
           "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
           "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
           "hundred", "thousand"}


def is_numword(w):
    """A spelled number, including 'ninety-eight' and 'sixty-five'. Not 'point'."""
    b = bare(w)
    if b in NUMWORD:
        return True
    parts = b.split("-")
    return len(parts) == 2 and all(p in NUMWORD for p in parts)


def glued(a, b):
    """True when breaking between a and b would split a unit like '15 feet', 'Victor Wembanyama' or 'free throw'."""
    if ends_sentence(a) or soft_end(a):
        return False
    ba, bb = bare(a), bare(b)
    if re.match(r"^\$?\d", ba) and (bb in UNITS or re.match(r"^\d", bb)):
        return True
    if ba in UNITS and re.match(r"^\d", bb):  # "13 feet 9"
        return True
    if is_numword(a) and (is_numword(b) or bb == "point"):
        return True  # "two hundred nine", "five point"
    if ba == "point" and is_numword(b):
        return True  # "point four"
    if (ba, bb) in PAIRS:
        return True
    ca, cb = a.strip("\"'“‘"), b.strip("\"'“‘")
    if ca[:1].isupper() and cb[:1].isupper() and ca not in CAPS_STOP and not ca.isupper():
        return True  # names: "Victor Wembanyama", "Rick Barry", "Adam Silver"
    return False


def chunk(words, st):
    """Split timed words into caption cards at natural phrase breaks (dynamic programming over break points)."""
    n, INF = len(words), float("inf")
    maxw, maxc, ideal = st["maxw"], st["maxc"], st["ideal"]

    def card_cost(i, j):
        card = words[i:j]
        k = sum(len(w["word"].split()) for w in card)
        text = " ".join(w["word"] for w in card)
        if k > maxw + 1 or len(text) > maxc + 6:
            return INF
        if any(ends_sentence(w["word"]) for w in card[:-1]):
            return INF
        c = (k - ideal) ** 2 * 0.6
        if k == maxw + 1:
            # Oct 14: a sentence may finish on one extra word if it still fits the width ("OF HIS NBA CAREER.") instead of orphaning it
            c += 0.8 if ends_sentence(card[-1]["word"]) and len(text) <= maxc else 2.5
        if len(text) > maxc:
            c += (len(text) - maxc) * 0.7
        c += sum(1.8 for w in card[:-1] if soft_end(w["word"]))
        if k == 1:
            b = bare(card[0]["word"])
            c += 6 if b in DANGLING else (0.2 if len(b) >= 7 or ends_sentence(card[0]["word"]) else 1.0)
            if ends_sentence(card[0]["word"]) and i > 0 and not (ends_sentence(words[i - 1]["word"]) or soft_end(words[i - 1]["word"])):
                c += 2.0  # avoid a lone "list." / "career." hanging off the card before it (Oct 14: was 1.2; #40 showed "OF HIS NBA" / "CAREER.")
        dur = card[-1]["end"] - card[0]["start"]
        if dur < 0.22:
            c += 1.5
        if dur > 1.7:
            c += (dur - 1.7) * 3
        return c

    def break_cost(b):  # break between words[b-1] and words[b]
        if b >= n:
            return 0.0
        a, nx = words[b - 1]["word"], words[b]["word"]
        c = 0.0
        if ends_sentence(a):
            c -= 2.0
        elif soft_end(a):
            c -= 1.5
        if bare(a) in DANGLING and not ends_sentence(a) and not soft_end(a):
            c += 4.0
        if glued(a, nx):
            c += 5.0
        if words[b]["start"] - words[b - 1]["end"] > 0.25:
            c -= 1.0
        return c

    best, prev = [0.0] + [INF] * n, [-1] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - maxw - 1), j):
            if best[i] == INF:
                continue
            c = card_cost(i, j)
            if c == INF:
                continue
            t = best[i] + c + break_cost(j)
            if t < best[j]:
                best[j], prev[j] = t, i
    cards, j = [], n
    while j > 0:
        i = prev[j]
        if i < 0:  # fallback: should not happen, but never lose words
            i = j - 1
        cards.append(words[i:j])
        j = i
    return cards[::-1]


def card_color(text, manual):
    """(colour, priority): hand-picked 3, numbers and shock words 2, big-moment words 1."""
    low = text.lower()
    for col in ("white", "red", "green"):
        if any(p.lower() in low for p in manual.get(col, [])):
            return (None, 3) if col == "white" else (col, 3)
    toks = [bare(t) for t in text.split()]
    if any(t in SHOCK for t in toks):
        return "red", 2
    if any(re.search(r"\d", t) for t in toks) or (toks and all(is_numword(t) or t == "point" for t in toks)):
        return "green", 2
    if any(t in BIG for t in toks):
        return "green", 1
    return None, 0


def limit_colors(picks, share=0.35):
    """No three coloured cards in a row and at most ~35% coloured, dropping the least important first."""
    picks = list(picks)
    while True:
        runs, run = [], []
        for i, (c, p) in enumerate(picks):
            if c:
                run.append(i)
            else:
                if len(run) >= 3:
                    runs.append(run)
                run = []
        if len(run) >= 3:
            runs.append(run)
        if not runs:
            break
        r = runs[0]
        drop = min(r[1:-1] or r, key=lambda i: (picks[i][1], abs(i - (r[0] + r[-1]) / 2)))
        if picks[drop][1] >= 3:
            drop = min(r, key=lambda i: picks[i][1])
            if picks[drop][1] >= 3:
                break
        picks[drop] = (None, picks[drop][1])
    cap = max(1, int(len(picks) * share))
    for prio in (1, 2):
        while sum(1 for c, _ in picks if c) > cap:
            cands = [i for i, (c, p) in enumerate(picks) if c and p == prio]
            if not cands:
                break
            picks[cands[len(cands) // 2]] = (None, prio)
    return picks


def ass_time(t):
    t = max(0.0, t)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    cs = int(round((s - int(s)) * 100))
    if cs == 100:
        s, cs = s + 1, 0
    return f"{int(h)}:{int(m):02d}:{int(s):02d}.{cs:02d}"


MAX_CAP_PX = 700  # Oct 25 2026: one layout safe on YouTube, TikTok and Instagram (Research Notes/TikTok and Instagram Playbook, section 5).
# Centred at x=540 a 700 px line ends at x=890: inside YouTube's right margin (888) and left of the icons TikTok and Reels show at the
# right edge. Was 805 (YouTube only); export_check.py warns over 715.


def fit_scale(text, st):
    """Uniform scale (<= 1) that keeps a caption line under MAX_CAP_PX. Width measured with the real font; libass draws an ASS
    font size at about 0.745 of PIL's em width (calibrated Oct 15 on a burned #36 v2 frame: 'STARTED SEVENTY-FIVE' is 1115 px
    in PIL at size 86 and burned 831 px wide at the pop's final \\fscx100)."""
    try:
        from PIL import ImageFont
        fp = os.path.join(HERE, "fonts", st["font"].replace(" ", "-") + ".ttf")
        b = ImageFont.truetype(fp, int(st["size"])).getbbox(text)
        px = (b[2] - b[0]) * (1.0 if st.get("pop") else st["scalex"] / 100) * 0.745
        return min(1.0, MAX_CAP_PX / px) if px else 1.0
    except Exception:
        return 1.0


def make_ass(words, style="metasports", manual=None, total=None, ys=None):
    """ys: optional [(shot_start, y)] from shots.json "cap_y"; a card uses the y of the shot it starts in."""
    st, manual = STYLES[style], manual or {}
    title = manual.get("_title") if st.get("title") else None
    if title:  # the first len(title words) spoken words become one 1-2 line title card (the "Players who ..." opener)
        n = len([t for t in re.split(r"\s+|\\N", title) if re.search(r"\w", t)])
        cards = [words[:n]] + chunk(words[n:], st)
    else:
        cards = chunk(words, st)
    texts = [re.sub(r"\s+", " ", " ".join(w["word"] for w in c)).strip() for c in cards]
    picks = limit_colors([card_color(t, manual) for t in texts]) if st["colors"] else [(None, 0)] * len(cards)
    lines, events = [], []
    for k, card in enumerate(cards):
        text = " ".join(w["word"] for w in card)
        text = re.sub(r"\s+", " ", text).strip()
        start = 0.0 if k == 0 and card[0]["start"] < 0.35 else card[0]["start"]
        if k + 1 < len(cards):
            nxt = cards[k + 1][0]["start"]
            end = nxt if nxt - card[-1]["end"] < 0.5 else card[-1]["end"] + 0.2
        else:
            end = card[-1]["end"] + 0.35
            if total:
                end = min(end, total)
        shown = text.upper() if st["caps"] else text
        if title and k == 0:
            shown = title
        col = picks[k][0]
        y = st["y"]
        for t0, cy in ys or []:
            if t0 <= start + 0.01:
                y = cy or st["y"]
        tags = f"\\pos(540,{y})\\blur{st['blur']}"
        if col:
            tags += f"\\c{RED if col == 'red' else GREEN}"
        fit = min(fit_scale(ln, st) for ln in shown.split("\\N"))  # Oct 15: keep the widest card clear of the Shorts like/comment column (x > 950)
        if st["pop"]:
            tags += f"\\fscx{86 * fit:.0f}\\fscy{86 * fit:.0f}\\t(0,90,\\fscx{100 * fit:.0f}\\fscy{100 * fit:.0f})"
        elif fit < 1:
            tags += f"\\fscx{st['scalex'] * fit:.0f}\\fscy{100 * fit:.0f}"
        shown = shown.replace("{", "(").replace("}", ")").replace("\n", "\\N")
        if st.get("kara"):  # one event per spoken word; the active word is highlighted, layout never moves
            toks = [re.sub(r"[{}]", "", w["word"]) for w in card]
            for wi, w in enumerate(card):
                ws = start if wi == 0 else w["start"]
                we = end if wi == len(card) - 1 else card[wi + 1]["start"]
                if we - ws < 0.04:
                    continue
                hi = KARA_NUM if re.search(r"\d", toks[wi]) else KARA_HI
                parts = [(f"{{\\c{hi}}}{t}{{\\c&H00FFFFFF&}}" if j == wi else t) for j, t in enumerate(toks)]
                events.append(f"Dialogue: 0,{ass_time(ws)},{ass_time(we)},Cap,,0,0,0,,{{{tags}}}{' '.join(parts)}")
            lines.append((start, end, shown, col))
            continue
        events.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Cap,,0,0,0,,{{{tags}}}{shown}")
        lines.append((start, end, shown, col))
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{st['font']},{st['size']},&H00FFFFFF,&H00FFFFFF,&H00000000,&H99000000,0,0,0,0,{st['scalex']},100,{st['spacing']},0,1,{st['outline']},{st['shadow']},5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    return head + "\n".join(events) + "\n", lines


def filter_arg(ass_path, cwd):
    """subtitles= filter text with paths relative to cwd (avoids Windows drive-letter escaping)."""
    rel = lambda p: os.path.relpath(p, cwd).replace("\\", "/").replace("'", r"\'")
    return f"subtitles='{rel(ass_path)}':fontsdir='{rel(FONTS)}'"


def burn(video, ass_path, out):
    cwd = os.path.dirname(os.path.abspath(out))
    vf = filter_arg(os.path.abspath(ass_path), cwd)
    tmp = os.path.join(cwd, "_burn_tmp.mp4")
    for enc in (["-c:v", "h264_nvenc", "-preset", "p6", "-rc", "vbr", "-cq", "18", "-b:v", "14M", "-maxrate", "20M"],
                ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast"]):
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.abspath(video), "-vf", vf, *enc,
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", tmp],
                           cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 10000:
            shutil.move(tmp, out)
            return True
        print(f"  caption burn with {enc[1]} failed: {(r.stderr or '')[-300:]}")
    return False


def frame(video, ass_path, at, out):
    cwd = os.path.dirname(os.path.abspath(out))
    vf = filter_arg(os.path.abspath(ass_path), cwd)
    # -ss after -i keeps subtitle timing exact
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.abspath(video), "-ss", f"{at:.2f}", "-vf", vf,
                    "-frames:v", "1", os.path.abspath(out)], cwd=cwd, check=True)


def build(folder, style="metasports", total=None):
    words = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8-sig"))
    mp = os.path.join(folder, "emphasis.json")
    manual = json.load(open(mp, encoding="utf-8-sig")) if os.path.exists(mp) else {}
    tp = os.path.join(folder, "title_caption.txt")  # ahmed style: on-screen title over the spoken title ("\N" or a newline = line break)
    if os.path.exists(tp):
        manual["_title"] = open(tp, encoding="utf-8-sig").read().strip().replace("\r", "")
    sp = os.path.join(folder, "shots.json")  # a shot may set "cap_y" (pixels of 1920) to move captions off a face
    shots = json.load(open(sp, encoding="utf-8-sig")) if os.path.exists(sp) else []
    ys = sorted(((float(x.get("start", 0)), x.get("cap_y")) for x in shots if isinstance(x, dict)), key=lambda t: t[0])
    ass, lines = make_ass(words, style, manual, total, ys)
    path = os.path.join(folder, "captions.ass")
    open(path, "w", encoding="utf-8").write(ass)
    return path, lines


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", help="Short folder (or _claude_build) with words.json")
    ap.add_argument("--style", default="metasports", choices=sorted(STYLES))
    ap.add_argument("--frame", type=float, help="render one test picture at this second")
    ap.add_argument("--video", help="video for --frame (default: final_nocap.mp4 in the folder)")
    ap.add_argument("--burn", help="video to burn captions onto")
    ap.add_argument("--ass", help="captions.ass to burn")
    ap.add_argument("--out", help="output file for --burn / --frame")
    a = ap.parse_args()
    if a.burn:
        ok = burn(a.burn, a.ass, a.out)
        print(f"{'Done' if ok else 'FAILED'}: {a.out}")
        return
    if not a.folder:
        raise SystemExit("Give --folder (or --burn)")
    path, lines = build(os.path.abspath(a.folder), a.style)
    for s, e, t, c in lines:
        print(f"{s:6.2f}-{e:6.2f}  {t}{'  [' + c + ']' if c else ''}")
    print(f"{len(lines)} cards -> {path}")
    if a.frame is not None:
        video = a.video or os.path.join(a.folder, "final_nocap.mp4")
        out = a.out or os.path.join(a.folder, f"caption_test_{a.frame:.1f}.png")
        frame(video, path, a.frame, out)
        print(out)


if __name__ == "__main__":
    main()
