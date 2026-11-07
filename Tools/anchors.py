"""Shared anchor matching (Nov 7, 2026): one place that turns each shot's "anchor" (the first words of its phrase) into a start time.
Used by anchor_shots.py, fill_len.py, cut_list.py (auto-fills missing "len") and precut_lint.py, so all four agree and an ambiguous anchor is caught
BEFORE cutting (the #99 Luka build lost a re-cut to an anchor "Last" that matched the wrong word).

  from anchors import fill_lengths
  starts, problems = fill_lengths(plan, words, pad=0.25)   # sets s["len"] where missing; problems = list of strings (FIX: ... / WARN: ...)
"""
import re


def norm(w):
    return re.sub(r"[^a-z0-9$%']", "", (w or "").lower())


def tokens(words):
    toks, own = [], []
    for i, w in enumerate(words):
        for t in str(w.get("word", "")).split():
            if norm(t):
                toks.append(norm(t)); own.append(i)
    return toks, own


def occurrences(toks, a):
    return [k for k in range(len(toks) - len(a) + 1) if toks[k:k + len(a)] == a]


def boundary(words, own, k):
    """True when token k starts a phrase: the first word, or the word before it ends in punctuation."""
    if k == 0:
        return True
    if own[k - 1] == own[k]:
        return False
    return bool(re.search(r"[.,!?:;\u2014\"')-]$", str(words[own[k - 1]].get("word", "")).strip()))


def starts_for(shots, words):
    """[(start or None)], problems. Anchors are matched in order, each after the previous one (the way anchor_shots.py does)."""
    toks, own = tokens(words)
    pos, starts, problems = 0, [], []
    for i, s in enumerate(shots):
        ph = s.get("anchor")
        if not ph:
            starts.append(0.0 if i == 0 else None)
            continue
        a = [norm(t) for t in str(ph).split() if norm(t)]
        hits = occurrences(toks, a)
        nxt = [k for k in hits if k >= pos]
        if not nxt:
            problems.append(f"FIX: shot {s.get('clip')}: anchor '{ph}' not found after the previous anchor (check the spelling against words.json)")
            starts.append(None)
            continue
        k = nxt[0]
        # Nov 7: an anchor is "the first words of its phrase", so the intended hit normally starts a phrase. When the first hit is
        # mid-sentence ("his LAST seven games") and a later hit starts one ("games. LAST night"), it is probably the wrong word
        # (the #99 Luka re-cut). Plain repeats are fine: matching is in order, so only this pattern steals a shot.
        later = [j for j in nxt[1:] if boundary(words, own, j)]
        raw = lambda m: " ".join(str(words[own[x]]["word"]) for x in range(m, min(len(toks), m + len(a)))).strip()
        # the anchor's exact spelling (case + punctuation, e.g. "Yugoslavia," vs "Yugoslavia") settles it when only the first hit has it
        exact = bool(later) and raw(k) == str(ph).strip() and raw(later[0]) != str(ph).strip()
        if not boundary(words, own, k) and later and not exact:
            j = later[0]
            ctx = lambda m: " ".join(words[own[x]]["word"] for x in range(max(0, m - 2), min(len(toks), m + len(a) + 3)))
            problems.append(f"WARN: shot {s.get('clip')}: anchor '{ph}' pins mid-sentence ('...{ctx(k)}...' at {words[own[k]]['start']:.2f} s), "
                            f"but '...{ctx(j)}...' at {words[own[j]]['start']:.2f} s starts a phrase. Use a longer anchor if the later one is meant")
        starts.append(0.0 if i == 0 else round(max(0.0, words[own[k]]["start"] - float(s.get("lead", 0.03))), 2))
        pos = k + 1  # as anchor_shots.py: the next anchor may share words with this one, but never its first word
    return starts, problems


def fill_lengths(plan, words, pad=0.25):
    """Fill every missing "len" = time to the next shot + pad. Returns (starts, problems)."""
    shots = plan["shots"]
    starts, problems = starts_for(shots, words)
    total = words[-1]["end"] + 0.3 if words else 0
    # shots without an anchor follow the previous shot: estimate from its len
    for i in range(len(starts)):
        if starts[i] is None and i > 0 and starts[i - 1] is not None and shots[i - 1].get("len"):
            starts[i] = starts[i - 1] + float(shots[i - 1]["len"]) - pad
    for i, s in enumerate(shots):
        if s.get("len") or starts[i] is None:
            continue
        nxt = next((starts[j] for j in range(i + 1, len(starts)) if starts[j] is not None), total)
        s["len"] = round(max(0.3, nxt - max(0.0, starts[i])) + pad, 2)
    return starts, problems


def table(shots, starts, words):
    """One line per shot: clip, start, duration, the words said over it (LONG over 3.5 s, short under 0.6 s)."""
    total = words[-1]["end"] + 0.3 if words else 0
    out = []
    for i, s in enumerate(shots):
        st = starts[i] if starts[i] is not None else 0.0
        end = next((starts[j] for j in range(i + 1, len(starts)) if starts[j] is not None), total)
        d = end - max(0.0, st)
        said = " ".join(w["word"] for w in words if st - 0.02 <= w["start"] < end - 0.02)
        flag = "  <-- LONG" if d > 3.5 else ("  <-- short" if d < 0.6 else "")
        out.append(f"{s.get('clip', '?'):5} {max(0.0, st):6.2f} {d:5.2f}  {said[:80]}{flag}")
    return out
