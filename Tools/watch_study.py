"""Top-vs-bottom study: Gemini watches each channel's best and worst recent Shorts and we compare what differs.

Why (Oct 27 2026): the owner asked for evidence on our theories (hold the opening, no cards, music, replays,
countdowns, a short first line) without burning credits. Gemini's free tier does the watching; Claude reads one CSV.
Comparing a channel with ITSELF (same creator, same audience, same era) is the fairest test we can run on other
channels.

Usage:
  python Tools/watch_study.py --channels @swishyhoopz @HoopiverseYT --name "NBA narrated"
Options: --window 60 (recent Shorts to rank, newest first), --skip-new 5 (too new to judge), --top 10 --bottom 10,
         --no-hook (skip the second, sharper look at the first 6 s; halves the requests).
Needs GEMINI_API_KEY (see Tools/yt_watch.py). Reports are cached in 'Research Notes/Watch Reports/' (re-running only
watches what is missing), so a run cut short by the free daily limit can simply be started again the next day.
Output: 'Research Notes/Watch Study/<name> (<date>).csv' (one row per Short) and '... summary.md' (top vs bottom).
Every number is [S] model-observed: the Oct 27 calibration on two of our own Shorts got the shots in the first 3 s
and 5 s exactly right but missed total shot counts by up to 3, and said "music" on two Shorts posted without a bed.
"""
import argparse, csv, datetime, json, os, re, statistics, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_watch as w

REPORTS = os.path.join(w.ROOT, "Research Notes", "Watch Reports")
OUT = os.path.join(w.ROOT, "Research Notes", "Watch Study")


def shorts(handle):
    """[(id, views, title)] newest first."""
    url = f"https://www.youtube.com/{handle.lstrip('/')}/shorts"
    r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", url], capture_output=True, text=True, timeout=600)
    ents = (json.loads(r.stdout) if r.stdout.strip() else {}).get("entries") or []
    return [(e["id"], e.get("view_count") or 0, e.get("title") or "") for e in ents if e.get("id")]


def patient(fn, *args):
    """Call fn; on a 429/503 from the last model wait and retry (free-tier per-minute limits).
    Gives up on a per-day limit so the run can be resumed tomorrow."""
    for attempt in range(6):
        try:
            return fn(*args)
        except SystemExit as e:
            msg = str(e)
            if re.search(r"PerDay|per day|daily", msg, re.I):
                raise SystemExit("free daily limit reached; run the same command again tomorrow (cached reports are kept)")
            if not re.search(r"error (429|503|500)", msg) or attempt == 5:
                raise
            wait = 30 * (attempt + 1)
            print(f"  busy, waiting {wait} s", file=sys.stderr)
            time.sleep(wait)


def cached(path, make):
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    rep = make()
    json.dump(rep, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    time.sleep(4)  # stay under the free per-minute limits
    return rep


def first_sentence_words(script):
    s = re.split(r"(?<=[.?!])\s", (script or "").strip(), maxsplit=1)[0]
    return len(s.split()) if s else None


def row(ch, grp, vid, views, title, med, rep, hook):
    sh = [x for x in rep.get("shots", []) if isinstance(x, dict)]
    st = [x.get("start_s") for x in sh if isinstance(x.get("start_s"), (int, float))]
    dev, mus, voi, cap, end = (rep.get(k) or {} for k in ("devices", "music", "voice", "captions", "ending"))
    hk = rep.get("hook") or {}
    txt = str(hk.get("on_screen_text_0_3s", "")).strip().lower()
    return {
        "channel": ch, "group": grp, "id": vid, "views": views, "x_median": round(views / med, 2) if med else None,
        "title": title, "length_s": rep.get("length_s"), "lane": rep.get("lane"),
        "shots": len(sh) or rep.get("shot_count"), "avg_shot_s": rep.get("average_shot_s"),
        "shots_first3": sum(t < 3 for t in st) if st else None, "shots_first5": sum(t < 5 for t in st) if st else None,
        "hook_shots_first3": (hook or {}).get("shots_in_first_3s"), "hook_shots_first5": (hook or {}).get("shots_in_first_5s"),
        "first_shot_kind": sh[0].get("kind") if sh else None, "subject_visible_0_1s": rep.get("subject_visible_0_1s"),
        "text_on_screen_0_3s": bool(txt) and txt not in ("none", "unknown"),
        "first_line_words": first_sentence_words(rep.get("script")), "cards": rep.get("cards_or_graphics"),
        "voice": voi.get("type"), "wpm": voi.get("words_per_minute_estimate"), "music": mus.get("present"),
        "music_level": mus.get("level_vs_voice"), "countdown": dev.get("countdown_or_ranking"),
        "replay": dev.get("replay_of_key_moment"), "promise_first_line": dev.get("promise_in_first_line"),
        "ends_on_payoff": dev.get("ends_on_payoff"), "reaction_shot": dev.get("reaction_shot"),
        "loops": end.get("loops_to_start"), "captions_case": cap.get("case"), "captions_position": cap.get("position"),
        "first_words": hk.get("first_words"), "model": rep.get("_meta", {}).get("model"),
    }


def summary(rows):
    """Top vs bottom per channel and pooled: medians for numbers, share of 'true' for yes/no features."""
    num = ["length_s", "shots", "avg_shot_s", "shots_first3", "shots_first5", "hook_shots_first3", "hook_shots_first5",
           "first_line_words", "cards", "wpm"]
    yes = ["subject_visible_0_1s", "text_on_screen_0_3s", "music", "countdown", "replay", "promise_first_line",
           "ends_on_payoff", "reaction_shot", "loops"]
    groups = sorted({r["channel"] for r in rows}) + ["ALL"]
    out = []
    for ch in groups:
        rs = [r for r in rows if ch == "ALL" or r["channel"] == ch]
        top, bot = [r for r in rs if r["group"] == "top"], [r for r in rs if r["group"] == "bottom"]
        out.append(f"\n### {ch} (top n={len(top)}, bottom n={len(bot)})\n\n| Feature | Top | Bottom |\n|---|---|---|")
        for k in num:
            a = [float(r[k]) for r in top if isinstance(r[k], (int, float))]
            b = [float(r[k]) for r in bot if isinstance(r[k], (int, float))]
            if a and b:
                out.append(f"| {k} (median) | {statistics.median(a):g} | {statistics.median(b):g} |")
        for k in yes:
            a = [r[k] for r in top if isinstance(r[k], bool)]
            b = [r[k] for r in bot if isinstance(r[k], bool)]
            if a and b:
                out.append(f"| {k} (% yes) | {100 * sum(a) // len(a)}% ({len(a)}) | {100 * sum(b) // len(b)}% ({len(b)}) |")
        for k in ("lane", "first_shot_kind", "voice", "music_level"):
            ct = lambda g: ", ".join(f"{v} {sum(1 for r in g if r[k] == v)}" for v in sorted({str(r[k]) for r in g}))
            out.append(f"| {k} | {ct(top)} | {ct(bot)} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--channels", nargs="+", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--window", type=int, default=60)
    ap.add_argument("--skip-new", type=int, default=5)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--bottom", type=int, default=10)
    ap.add_argument("--no-hook", action="store_true")
    ap.add_argument("--fps", type=float, default=4.0)
    ap.add_argument("--reports-dir", help="where the per-Short reports are cached (default Research Notes/Watch Reports)")
    ap.add_argument("--out-dir", help="where the study CSV and summary go (default Research Notes/Watch Study)")
    a = ap.parse_args()
    global REPORTS, OUT
    REPORTS, OUT = a.reports_dir or REPORTS, a.out_dir or OUT
    os.makedirs(REPORTS, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    models = w.pick_models(None)
    rows, stop = [], False
    for ch in a.channels:
        if stop:
            break
        win = shorts(ch)[a.skip_new:a.skip_new + a.window]
        if len(win) < a.top + a.bottom:
            print(f"{ch}: only {len(win)} Shorts in the window, skipped")
            continue
        med = statistics.median(v for _, v, _ in win)
        ranked = sorted(win, key=lambda e: e[1], reverse=True)
        picks = [("top", e) for e in ranked[:a.top]] + ([("bottom", e) for e in ranked[-a.bottom:]] if a.bottom else [])
        print(f"{ch}: {len(win)} Shorts in the window, median {med:,.0f} views; watching {len(picks)}")
        for grp, (vid, views, title) in picks:
            def full():
                _, rep, model = w.watch(vid, models, a.fps, None)
                rep["_meta"] = {"source": vid, "model": model, "fps": a.fps, "watched": datetime.date.today().isoformat(),
                                "tier": "[S] model-observed, not measured"}
                return rep
            try:
                rep = cached(os.path.join(REPORTS, f"{vid}.json"), lambda: patient(full))
                hook = None if a.no_hook else cached(os.path.join(REPORTS, f"{vid}_hook.json"),
                                                     lambda: patient(lambda: w.hook_cuts(vid, models)[0]))
            except SystemExit as e:
                if "daily limit" not in str(e):
                    print(f"  skipped {vid}: {str(e)[:150]}")  # one bad Short doesn't end the study
                    continue
                print(f"  stopped: {e}")
                stop = True
                break
            rows.append(row(ch, grp, vid, views, title, med, rep, hook))
            print(f"  {grp:6} {views:>10,}  {title[:50]}")
    if not rows:
        sys.exit("nothing watched")
    stem = os.path.join(OUT, f"{a.name} ({datetime.date.today().isoformat()})")
    with open(stem + ".csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)
    md = (f"# Watch study: {a.name} ({datetime.date.today().isoformat()})\n\nChannels: {', '.join(a.channels)}. "
          f"Each channel's {a.window} most recent Shorts (skipping the newest {a.skip_new}), its top {a.top} and bottom "
          f"{a.bottom} by views. Watched by Gemini; every number is [S] model-observed (see Tools/watch_study.py).\n"
          + summary(rows) + "\n")
    open(stem + " summary.md", "w", encoding="utf-8").write(md)
    print(md)
    print("wrote", os.path.relpath(stem + ".csv", w.ROOT))


if __name__ == "__main__":
    main()
