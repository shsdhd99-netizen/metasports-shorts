"""Builds the upload kit text for a finished cut: image-spot timestamps + optional chapters located from the final word list.
usage: python make_kit.py final_words.json  -> prints the two blocks (spots, chapters); also returns them for other scripts"""
import json, re, sys

def norm(w): return re.sub(r"[^a-z0-9'-]", "", w.lower())

def load(path):
    fw = json.load(open(path))
    return [(norm(x["word"]), x["start"]) for x in fw if norm(x["word"])]

def find(toks, phrase, after=0.0):
    seq = [norm(p) for p in phrase.split()]
    for i in range(len(toks) - len(seq) + 1):
        if toks[i][1] >= after and all(toks[i + j][0] == seq[j] for j in range(len(seq))):
            return toks[i][1]
    return None

def mmss(t): t = int(round(t)); return f"{t // 60}:{t % 60:02d}"

SPOTS = [  # (phrase, what you'd show, how long)
    ("called east brickton", "your own old East Brickton screenshots / channel art", 3),
    ("micro instagram trends", "screenshot of an Instagram note (blur names)", 3),
    ("heading over to the block button", "the block-gif trend (blur usernames)", 3),
    ("running out of mall", "free stock crowd-running photo", 2),
    ("yard epidemic", "optional: plain photo or skip (ad safety)", 2),
    ("back in nineteen", "generic archive photo of 90s smoking, no real face", 2),
    ("brazskills podcast", "podcast cover art", 2),
    ("plaques on my wall", "YouTube Play Button plaque photo", 3),
]
CHAPTERS = [  # (anchor phrase, title, seconds before the anchor where the chapter starts)
    (None, "the roblox kid", 0),
    ("and if you die tomorrow", "if you died tomorrow", 1),
    ("micro instagram trends", "the block gif", 8),
    ("running out of mall", "the mall test", 6),
    ("yard epidemic", "the yard epidemic", 6),
    ("life is not promised to you", "life is not promised", 1),
    ("plaques on my wall", "the 100k plaque", 12),
    ("basically what i'm saying", "what makes you proud", 1),
]

def build(path):
    toks = load(path)
    spots, chap, last = [], [], -1.0
    for ph, what, _ in SPOTS:
        t = find(toks, ph)
        spots.append((mmss(t) if t is not None else "??", ph, what, t))
    for ph, title, back in CHAPTERS:
        t = 0.0 if ph is None else find(toks, ph, after=last + 5)
        if t is None: continue
        t = max(0.0, t - back); last = t
        chap.append((mmss(t), title))
    return spots, chap

if __name__ == "__main__":
    spots, chap = build(sys.argv[1])
    print("IMAGE SPOTS"); [print(f"  {a}  \"{b}\"  -> {c}") for a, b, c, _ in spots]
    print("CHAPTERS"); [print(f"  {a} {b}") for a, b in chap]
