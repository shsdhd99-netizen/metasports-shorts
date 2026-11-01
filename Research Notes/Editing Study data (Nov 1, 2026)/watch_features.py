"""Editing Study (Nov 1, 2026): turn every Gemini watch report into one row of editing and sound features, join it to the
channel's public view counts, and compare groups (100K+ competitor Shorts vs the same channels' below-median ones vs ours).

  python "Research Notes/Editing Study data (Nov 1, 2026)/watch_features.py" --flat /tmp/es/flat
      --flat: a folder of `yt-dlp --flat-playlist -J https://www.youtube.com/<handle>/shorts` outputs, one <handle>.json each

Writes watch_features.csv and watch_summary.md next to this file. Every number comes from a model's watch (Gemini flash /
flash-lite at 1-4 fps), so it is [S] at best: shot counts can be off by about 3, and sound effects under music are often missed.
"""
import argparse, csv, glob, json, os, re, statistics as st
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPORTS = os.path.join(os.path.dirname(HERE), "Watch Reports")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
KW = {  # visual / edit devices, searched in every free-text field of a report
    "zoom": r"zoom|punch[- ]?in|push[- ]?in|zooms? in",
    "slowmo": r"slow[- ]?mo|slow motion|slowed|speed ramp|ramp(ed)? (up|down)|half[- ]speed",
    "freeze": r"freeze|frozen|still frame|paus(e|ed) (on|the)",
    "circle_arrow": r"circle|arrow|red ring|highlight(ed)? (box|ring|circle)|spotlight|outlined",
    "split": r"split[- ]?screen|side[- ]by[- ]side",
    "replay": r"replay|again from|second angle|another angle|rewind",
    "shake": r"shake|shaking|camera shake|impact zoom",
    "flash": r"flash|white frame|strobe|glitch",
    "meme": r"meme|reaction gif|movie clip|cutaway",
    "transition": r"transition|whip|wipe|swipe",
    "countdown_badge": r"#\s?\d\b|number \d (badge|label)|ranking|countdown|top \d",
}
SFX = {  # sound effect families
    "whoosh": r"whoosh|swoosh|swish transition|woosh|swipe",
    "impact_bass": r"boom|bass|impact|thud|hit|punch|explosion|blast|slam|drop",
    "riser": r"riser|rising|build|tension",
    "crowd_cheer": r"crowd|cheer|ooh|roar|applause|gasp",
    "comic": r"record scratch|cartoon|sad trombone|vine|bruh|funny|laugh|crying|sob",
    "game_sound": r"buzzer|whistle|swish|net|rim|dribble|stick|kick|bat|horn",
    "ui_pop": r"ding|pop|click|snap|fanfare|chime|clink",
}
MUSIC = {
    "hiphop_trap_phonk": r"hip[- ]?hop|trap|rap|phonk|drill|urban",
    "cinematic_dramatic": r"cinematic|dramatic|orchestral|epic|documentary",
    "suspense": r"suspense|tension|dark|ominous",
    "upbeat_pop_edm": r"upbeat|electronic|pop|edm|remix|hype|dance",
    "meme_comic": r"meme|comedic|funny|cartoon|trending",
    "emotional": r"piano|emotional|sad|inspirational",
}


def lenient(path):
    """Load a report; repair the 19 'raw' ones (unquoted helper keys, cut-off endings)."""
    d = json.load(open(path, encoding="utf-8"))
    if "raw" not in d:
        return d
    r = re.sub(r"^```json|```$", "", d["raw"].strip()).strip()
    r = "\n".join(l for l in r.split("\n") if not re.match(r"^\s*[A-Za-z_]\w*\s*:", l))
    for attempt in range(2):
        try:
            out = json.loads(r)
            out["_meta"] = dict(d.get("_meta", {}), repaired=True)
            return out
        except Exception:
            s, stack, ins, esc = r.rstrip().rstrip(","), [], False, False
            for ch in s:
                if ins:
                    esc = (not esc) and ch == "\\"
                    if ch == '"' and not esc:
                        ins = False
                elif ch == '"':
                    ins = True
                elif ch in "[{":
                    stack.append(ch)
                elif ch in "]}" and stack:
                    stack.pop()
            r = s + ('"' if ins else "") + "".join("]" if c == "[" else "}" for c in reversed(stack))
    return None


def flat_lists(folder):
    vids, chans = {}, {}
    for f in glob.glob(os.path.join(folder, "*.json")):
        ch = os.path.basename(f)[:-5].lstrip("_")
        es = [e for e in json.load(open(f)).get("entries", []) if e]
        views = [e.get("view_count") or 0 for e in es]
        chans[ch] = {"n": len(es), "median": st.median(views) if views else 0}
        for i, e in enumerate(es):
            vids[e["id"]] = {"channel": ch, "views": e.get("view_count") or 0, "title": e.get("title", ""), "rank_newest": i}
    return vids, chans


def text_of(d):
    parts = []
    for s in d.get("shots") or []:
        parts.append(str(s.get("shows", "")))
    for k in ("retention_tricks", "what_makes_it_work"):
        parts += [str(x) for x in d.get(k) or []]
    parts += [str(o.get("text", "")) for o in d.get("text_overlays") or [] if isinstance(o, dict)]
    parts += [str(d.get("framing", "")), json.dumps(d.get("hook", {})), json.dumps(d.get("ending", {}))]
    return " | ".join(parts).lower()


def features(d):
    L = float(d.get("length_s") or 0) or None
    shots = [s for s in d.get("shots") or [] if isinstance(s, dict)]
    n = d.get("shot_count") or len(shots) or None
    starts = sorted(float(s.get("start_s") or 0) for s in shots)
    first_len = (float(shots[0].get("end_s") or 0) - float(shots[0].get("start_s") or 0)) if shots else None
    kinds = Counter(str(s.get("kind", "")).lower() for s in shots)
    txt = text_of(d)
    cap = d.get("captions") or {}
    mus = d.get("music") or {}
    voice = d.get("voice") or {}
    end = d.get("ending") or {}
    dev = d.get("devices") or {}
    hook = d.get("hook") or {}
    sfx = [s for s in d.get("sound_effects") or [] if isinstance(s, dict)]
    sfx_txt = [str(s.get("sound", "")).lower() for s in sfx]
    hl = str(cap.get("highlight_style", "")).lower()
    colours = json.dumps(cap.get("colours", "")).lower()
    style = str(mus.get("style", "")).lower()
    present = bool(mus.get("present")) and style not in ("none", "")
    overlays = [o for o in d.get("text_overlays") or [] if isinstance(o, dict)]
    row = {
        "lane": d.get("lane"), "length_s": L, "shots": n,
        "shots_per_10s": round(10 * n / L, 2) if n and L else None,
        "avg_shot_s": d.get("average_shot_s"), "longest_shot_s": d.get("longest_shot_s"),
        "first_shot_s": round(first_len, 2) if first_len is not None else None,
        "shots_first3": hook.get("shots_in_first_3s"), "shots_first5": sum(1 for s in starts if s < 5.0) if starts else None,
        "subject_0_1s": d.get("subject_visible_0_1s"),
        "text_0_3s": bool(str(hook.get("on_screen_text_0_3s") or "").strip() not in ("", "none", "None")),
        "first_frame": str(hook.get("first_frame", ""))[:90], "first_words": str(hook.get("first_words", ""))[:80],
        "share_face": round(kinds.get("face", 0) / len(shots), 2) if shots else None,
        "share_still_card": round((kinds.get("still", 0) + kinds.get("card", 0) + kinds.get("graphic", 0)) / len(shots), 2) if shots else None,
        "cards": d.get("cards_or_graphics"), "overlays": len(overlays),
        "overlays_per_10s": round(10 * len(overlays) / L, 2) if L else None,
        "emoji_on_screen": bool(EMOJI.search(" ".join(str(o.get("text", "")) for o in overlays) + str(hook.get("on_screen_text_0_3s", ""))))
                           or "emoji" in txt,
        "framing": ("split" if "split" in str(d.get("framing", "")).lower() else "blur" if "blur" in str(d.get("framing", "")).lower()
                    else "letterbox" if "letterbox" in str(d.get("framing", "")).lower() else "crop"),
        "cap_present": cap.get("present"), "cap_words_line": cap.get("words_per_line"), "cap_case": cap.get("case"),
        "cap_position": cap.get("position"), "cap_word_highlight": bool(re.search(r"word|active|pop", hl)) and "none" not in hl,
        "cap_colour_accent": bool(re.search(r"yellow|green|red|pink|cyan|blue|purple|teal|colou?r", colours + " " + hl)),
        "sfx_n": len(sfx), "sfx_per_10s": round(10 * len(sfx) / L, 2) if L else None,
        "music": present, "music_level": mus.get("level_vs_voice") if present else "none",
        "music_from_0": (float(mus.get("starts_at_s") or 0) <= 0.5) if present else None,
        "voice": voice.get("type"), "wpm": voice.get("words_per_minute_estimate"), "tone": voice.get("tone"),
        "real_audio_under_voice": voice.get("original_audio_under_voice"),
        "loops": end.get("loops_to_start"), "cta": str(end.get("call_to_action", "")).lower() not in ("none", "", "false"),
        "ends_on_payoff": dev.get("ends_on_payoff"), "dev_replay": dev.get("replay_of_key_moment"),
        "dev_reaction": dev.get("reaction_shot"), "dev_countdown": dev.get("countdown_or_ranking"),
    }
    for k, rx in KW.items():
        row["kw_" + k] = bool(re.search(rx, txt))
    for k, rx in SFX.items():
        row["sfx_" + k] = sum(1 for s in sfx_txt if re.search(rx, s))
    for k, rx in MUSIC.items():
        row["mus_" + k] = bool(present and re.search(rx, style))
    row["sfx_list"] = "; ".join(f"{s.get('at_s')}:{str(s.get('sound'))[:30]}" for s in sfx)
    row["music_style"] = style[:50]
    return row


def med(xs):
    out = []
    for x in xs:
        try:
            out.append(float(x))
        except (TypeError, ValueError):
            pass
    xs = out
    return round(st.median(xs), 2) if xs else None


def pct(xs):
    xs = [x for x in xs if x is not None and x != ""]
    return f"{round(100 * sum(1 for x in xs if x is True or x == 'True') / len(xs))}%" if xs else "-"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--flat", default="/tmp/es/flat")
    a = ap.parse_args()
    vids, chans = flat_lists(a.flat)
    rows = []
    hooks = {}
    for f in sorted(glob.glob(os.path.join(REPORTS, "*.json"))):
        vid = os.path.basename(f)[:-5]
        if vid.endswith("_hook"):
            hooks[vid[:-5]] = json.load(open(f, encoding="utf-8"))
            continue
        d = lenient(f)
        if not d or "shots" not in d:
            continue
        v = vids.get(vid, {})
        ch = v.get("channel", "?")
        cm = chans.get(ch, {}).get("median") or 0
        views = v.get("views", 0)
        ours = ch in ("MetaSportsClips", "UCIYlW84gYcChQtdys5L9pOg")
        group = ("ours" if ours else "top_100k" if views >= 100_000 else "below_own_median" if views < cm else "mid")
        row = {"id": vid, "channel": ch, "views": views, "channel_median": cm, "x_median": round(views / cm, 2) if cm else None,
               "group": group, "model": d.get("_meta", {}).get("model"), "title": v.get("title", "")[:70]}
        row.update(features(d))
        h = hooks.get(vid)
        row["hook_music_audible"] = h.get("music_or_beat_audible") if h else None
        rows.append(row)
    out = os.path.join(HERE, "watch_features.csv")
    cols = list(rows[0].keys())
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    # ---- summary ----
    G = ("top_100k", "mid", "below_own_median", "ours")
    by = defaultdict(list)
    for r in rows:
        by[r["group"]].append(r)
    num = ["length_s", "shots_per_10s", "avg_shot_s", "first_shot_s", "shots_first3", "shots_first5", "overlays_per_10s",
           "sfx_per_10s", "wpm", "cap_words_line"]
    boo = ["subject_0_1s", "text_0_3s", "emoji_on_screen", "cap_word_highlight", "cap_colour_accent", "music", "real_audio_under_voice",
           "loops", "cta", "dev_replay", "dev_reaction", "dev_countdown"] + ["kw_" + k for k in KW]
    lines = ["# Watch-report features by group (generated by watch_features.py)", "",
             f"Reports parsed: {len(rows)} (Gemini, [S]). Channels: " + ", ".join(f"{k} {v}" for k, v in Counter(r['channel'] for r in rows).most_common()), "",
             "Groups: top_100k = competitor Short with 100K+ views now; below_own_median = under its channel's median (all its Shorts); "
             "mid = the rest; ours = our own Shorts that Gemini watched.", "",
             "| feature | " + " | ".join(f"{g} (n={len(by[g])})" for g in G) + " |", "|---|" + "---|" * len(G)]
    for k in num:
        lines.append(f"| {k} (median) | " + " | ".join(str(med(r[k] for r in by[g])) for g in G) + " |")
    for k in boo:
        lines.append(f"| {k} (% yes) | " + " | ".join(pct([r[k] for r in by[g]]) for g in G) + " |")
    for k in SFX:
        lines.append(f"| sfx_{k} (% with any) | " + " | ".join(pct([r['sfx_' + k] > 0 for r in by[g]]) for g in G) + " |")
    lines.append("| sfx any (% with any) | " + " | ".join(pct([r['sfx_n'] > 0 for r in by[g]]) for g in G) + " |")
    for k in MUSIC:
        lines.append(f"| music {k} (% of all) | " + " | ".join(pct([r['mus_' + k] for r in by[g]]) for g in G) + " |")
    for lv in ("quiet", "equal", "loud"):
        lines.append(f"| music level {lv} (% of all) | " + " | ".join(pct([r['music_level'] == lv for r in by[g]]) for g in G) + " |")
    for k in ("cap_case", "cap_position", "framing", "voice"):
        for val, _ in Counter(str(r[k]) for r in rows).most_common(4):
            lines.append(f"| {k} = {val} (%) | " + " | ".join(pct([str(r[k]) == val for r in by[g]]) for g in G) + " |")
    # within-channel: top half vs bottom half by views, channels with 8+ reports
    lines += ["", "## Same channel, top half vs bottom half by views (channels with 8+ reports)", "",
              "| channel (n) | median views top / bottom | shots/10s | first shot s | sfx/10s | music % | music loud/equal % | word highlight % | zoom % | slowmo % | replay % | circle/arrow % | meme % |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    pooled = {"top": [], "bot": []}
    for ch, rs in sorted(defaultdict(list, {c: [r for r in rows if r["channel"] == c] for c in set(r["channel"] for r in rows)}).items()):
        if len(rs) < 8 or ch in ("MetaSportsClips",):
            continue
        rs = sorted(rs, key=lambda r: -r["views"])
        h = len(rs) // 2
        top, bot = rs[:h], rs[-h:]
        pooled["top"] += top
        pooled["bot"] += bot
        f = lambda rs, k: med(r[k] for r in rs)
        p = lambda rs, k: pct([r[k] for r in rs])
        lines.append(f"| {ch} ({len(rs)}) | {med(r['views'] for r in top):,.0f} / {med(r['views'] for r in bot):,.0f} | "
                     f"{f(top,'shots_per_10s')} / {f(bot,'shots_per_10s')} | {f(top,'first_shot_s')} / {f(bot,'first_shot_s')} | "
                     f"{f(top,'sfx_per_10s')} / {f(bot,'sfx_per_10s')} | {p(top,'music')} / {p(bot,'music')} | "
                     f"{pct([r['music_level'] in ('loud','equal') for r in top])} / {pct([r['music_level'] in ('loud','equal') for r in bot])} | "
                     f"{p(top,'cap_word_highlight')} / {p(bot,'cap_word_highlight')} | {p(top,'kw_zoom')} / {p(bot,'kw_zoom')} | "
                     f"{p(top,'kw_slowmo')} / {p(bot,'kw_slowmo')} | {p(top,'kw_replay')} / {p(bot,'kw_replay')} | "
                     f"{p(top,'kw_circle_arrow')} / {p(bot,'kw_circle_arrow')} | {p(top,'kw_meme')} / {p(bot,'kw_meme')} |")
    t, b = pooled["top"], pooled["bot"]
    lines += ["", f"## Pooled within-channel halves (top n={len(t)}, bottom n={len(b)})", "", "| feature | top half | bottom half |", "|---|---|---|"]
    for k in num:
        lines.append(f"| {k} (median) | {med(r[k] for r in t)} | {med(r[k] for r in b)} |")
    for k in boo:
        lines.append(f"| {k} | {pct([r[k] for r in t])} | {pct([r[k] for r in b])} |")
    lines.append(f"| sfx any | {pct([r['sfx_n'] > 0 for r in t])} | {pct([r['sfx_n'] > 0 for r in b])} |")
    for lv in ("quiet", "equal", "loud", "none"):
        lines.append(f"| music level {lv} | {pct([r['music_level'] == lv for r in t])} | {pct([r['music_level'] == lv for r in b])} |")
    for k in MUSIC:
        lines.append(f"| music {k} | {pct([r['mus_' + k] for r in t])} | {pct([r['mus_' + k] for r in b])} |")
    open(os.path.join(HERE, "watch_summary.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{len(rows)} reports -> {out}\n" + "\n".join(lines))


if __name__ == "__main__":
    main()
