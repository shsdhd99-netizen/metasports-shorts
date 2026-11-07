"""Move music.json and sfx.json times onto a new voice take of the same script.

  python retime.py --old "<folder with the old words.json>" --new "<folder with the new words.json, music.json, sfx.json>"

Why: music drops, stops and effects are planned on seconds of the old narration ("the drop before 'It isn't.'"). A new voice
(Oct 14 2026: Alex) says the same words at different times. Each time is mapped through the words: a time inside or between
two words keeps its relative position between the same two words in the new take (words matched with difflib, so small
script edits are fine). Writes music.json / sfx.json in --new (originals kept as *_oldvoice.json) and prints old -> new.
Check the result by ear-free means: assemble, then read the music level at the mapped times (Music Guide section 5).
"""
import argparse, bisect, difflib, json, os, re, shutil


def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def anchors(old, new):
    a, b = [norm(w["word"]) for w in old], [norm(w["word"]) for w in new]
    pts = [(0.0, 0.0)]
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            o, n = old[blk.a + k], new[blk.b + k]
            pts += [(o["start"], n["start"]), (o["end"], n["end"])]
    pts.sort()
    return pts


def mapper(pts, old_end, new_end):
    xs = [p[0] for p in pts]

    def f(t):
        if t >= xs[-1]:  # after the last word: keep the same distance past the end of speech
            return round(pts[-1][1] + (t - xs[-1]), 3)
        i = max(1, bisect.bisect_right(xs, t))
        (x0, y0), (x1, y1) = pts[i - 1], pts[i]
        return round(y0 + (t - x0) * ((y1 - y0) / (x1 - x0) if x1 > x0 else 0), 3)
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    a = ap.parse_args()
    old = json.load(open(os.path.join(a.old, "words.json"), encoding="utf-8"))
    new = json.load(open(os.path.join(a.new, "words.json"), encoding="utf-8"))
    f = mapper(anchors(old, new), old[-1]["end"], new[-1]["end"])
    for name, keys in (("music.json", ("in", "out", "hit_on")), ("sfx.json", ("at",))):
        p = os.path.join(a.new, name)
        if not os.path.exists(p):
            continue
        backup = p.replace(".json", "_oldvoice.json")
        if not os.path.exists(backup):
            shutil.copy(p, backup)
        d = json.load(open(backup, encoding="utf-8"))
        items = d if isinstance(d, list) else [d]
        for it in items:
            for k in keys:
                if isinstance(it.get(k), (int, float)):
                    print(f"{name} {it.get('sfx', '')} {k}: {it[k]} -> {f(it[k])}"); it[k] = f(it[k])
            for dr in it.get("drops", []):
                print(f"{name} drop at: {dr['at']} -> {f(dr['at'])}"); dr["at"] = f(dr["at"])
        json.dump(d, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
