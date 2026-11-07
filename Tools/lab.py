"""The lab: tests that run, log and score themselves, plus a repeatable study of every part of a Short (Nov 7, 2026).
Owner, Nov 7: "auto run and log tests yourself with a score on them. make sure you can also do this same study for editing, etc."
Zero Claude credits. Read-only: it reads the API files the daily stats pull writes (`Research Notes/Studio exports/api*/daily *.csv`), the
production folders, `Scheduled Uploads.csv` and `Shorts Dataset.csv`. It never touches YouTube.

  python Tools/lab.py measure                    # every Short: features (topic, script, edit, package, length) + results -> Research Notes/Lab/shorts.csv
  python Tools/lab.py study [--part all|topic|script|edit|package|length] [--channel nba|fc]
                                                 # the ranked study: which features go with more views -> Research Notes/Lab/Study - <part> (<date>).md
  python Tools/lab.py assign nba|fc [--folder F] # which arm every live test wants for the NEXT Short; --folder writes an `**Arms:**` line into F/UPLOAD.md
  python Tools/lab.py score [--no-apply]         # score every live test -> Research Notes/Lab/Scoreboard.md; decided tests close, the next queued one starts
  python Tools/lab.py auto                       # measure + score + study all (daily-run step 6 and the daily stats check run this)

How a test works (Research Notes/Lab/tests.json; at most 3 live per channel, the rest queue):
  - "ab": two arms of one feature (A = control, B = the new thing). `assign` hands out the arm with fewer Shorts, so arms stay balanced.
  - "lane": one group (e.g. record lists) against every other Short of the channel posted in the same window.
  - Arms are DETECTED from the files whenever possible (title, script, cuts.json, the uploaded file name), so a Short counts even if nobody
    logged it; the `**Arms:**` line only matters for features no file shows (e.g. foreshadow).
  - Metric: views at 72 h as the API reports them (the API runs ~2 days behind, so the first daily snapshot 5-8 days after go-live),
    else current views once 5+ days old. Secondary: avg % viewed.
  - Score = 100 x the chance that a random B Short beats a random A Short (50 = no difference). p = permutation test.
  - Decision: each arm at min_n (6) and score >= 70 (or <= 30) with p <= 0.2 -> B WINS (or A WINS). Both arms at max_n (12) without that ->
    NO DIFFERENCE (keep the cheaper arm). A decided test names the rule it changes; the daily run updates that rule line.
Tiers in the study: n under 5 on a side = "too few"; p < 0.05 and a 1.3x+ gap = "likely real"; p < 0.2 = "maybe"; else "no sign".
"""
import argparse, csv, datetime as dt, glob, json, math, os, random, re, statistics as st, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RN = os.path.join(ROOT, "Research Notes")
LAB = os.path.join(RN, "Lab")
TESTS = os.path.join(LAB, "tests.json")
SHORTS = os.path.join(LAB, "shorts.csv")
PLANS = os.path.join(LAB, "plans.csv")
LABELS = os.path.join(LAB, "labels.csv")
ET = ZoneInfo("America/New_York")
ERA = {"nba": "2026-09-25", "fc": "2026-10-01"}  # the NBA restart; older uploads (2025) had near-zero views and skew everything
FOLDERS = {"nba": os.path.join(ROOT, "Productions", "MetaSports"), "fc": os.path.join(ROOT, "Soccer Channel", "Productions")}
sys.path.insert(0, HERE)
import review_measure as rm  # word_feats, shot_feats, ass_feats, toks, load


def today():
    return dt.datetime.now(ET).date()


def num(x):
    try:
        v = float(x)
        return None if math.isnan(v) else v
    except (TypeError, ValueError):
        return None


def norm(s):
    return " ".join(re.findall(r"[a-z0-9']+", (s or "").lower()))


# ---------------------------------------------------------------- results (every daily snapshot)
def results():
    """{video_id: {...}} with views at 72 h (v72), current views, avg % viewed, engaged, subs, hour/date in ET."""
    out = {}
    for ch, sub in (("nba", "api"), ("fc", "api FC")):
        for f in sorted(glob.glob(os.path.join(RN, "Studio exports", sub, "daily *.csv"))):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(f))
            fdate = dt.date.fromisoformat(m.group(1)) if m else None
            for r in csv.DictReader(open(f, encoding="utf-8")):
                vid = r["video_id"]
                o = out.setdefault(vid, dict(video_id=vid, channel=ch, snaps=[]))
                o["title"] = r["title"]
                o["published_raw"] = r["published"]
                o["length_s"] = num(r["length_s"])
                views = num(r["views"])
                if views is not None and fdate:
                    o["snaps"].append((fdate, views, num(r["averageViewPercentage"]), num(r["engaged_ratio"]), num(r["subscribersGained"])))
    golive = {}  # a scheduled upload's API "published" is its upload time; the real go-live is publish_et in Scheduled Uploads.csv
    sp = os.path.join(RN, "Scheduled Uploads.csv")
    if os.path.exists(sp):
        for r in csv.DictReader(open(sp, encoding="utf-8")):
            try:
                golive[r["video_id"]] = dt.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
            except (KeyError, ValueError):
                pass
    for vid in [v for v, o in out.items() if norm(o.get("title")) in ("unknown", "")]:
        del out[vid]  # the deleted "unknown"-title duplicates of Nov 5-6
    for o in out.values():
        try:
            p = golive.get(o["video_id"]) or dt.datetime.fromisoformat(o["published_raw"].replace("Z", "+00:00")).astimezone(ET)
        except Exception:
            p = None
        o["date"] = p.date().isoformat() if p else ""
        o["hour_et"] = round(p.hour + p.minute / 60, 2) if p else None
        o["age_days"] = (today() - p.date()).days if p else None
        s72 = [s for s in o["snaps"] if p and 5 <= (s[0] - p.date()).days <= 8]  # 72 h of data: the API runs ~2 days behind, so read it on day 5-8 after go-live
        last = o["snaps"][-1] if o["snaps"] else None
        o["v72"] = s72[0][1] if s72 else None
        o["avg72"] = s72[0][2] if s72 else None
        o["views_now"] = last[1] if last else None
        o["avg_now"] = last[2] if last else None
        o["engaged"] = last[3] if last else None
        o["subs"] = last[4] if last else None
        mature = (o["age_days"] or 0) >= 5
        o["views"] = o["v72"] if o["v72"] is not None else (o["views_now"] if mature else None)
        o["avg_pct"] = o["avg72"] if o["avg72"] is not None else (o["avg_now"] if mature else None)
        o["metric_src"] = "72h" if o["v72"] is not None else ("now" if o["views"] is not None else "")
        del o["snaps"]
    # stayed % (Studio export, owner's Monday download) from the dataset
    dsp = os.path.join(RN, "Shorts Dataset.csv")
    if os.path.exists(dsp):
        for r in csv.DictReader(open(dsp, encoding="utf-8")):
            if r["video_id"] in out:
                out[r["video_id"]]["stayed"] = num(r.get("stayed_pct"))
    return out


# ---------------------------------------------------------------- folders and the video they became
def folders():
    out = []
    for ch, base in FOLDERS.items():
        for d in sorted(glob.glob(os.path.join(base, "*"))):
            if os.path.isdir(d) and (os.path.exists(os.path.join(d, "UPLOAD.md")) or os.path.exists(os.path.join(d, "script.txt"))):
                out.append((ch, d))
    return out


def card(d):
    import yt_schedule as ys
    p = os.path.join(d, "UPLOAD.md")
    if not os.path.exists(p):
        return "", "", ""
    try:
        title, tags = ys.parse_card(p)
    except Exception:
        title, tags = "", ""
    return title or "", tags or "", open(p, encoding="utf-8-sig").read()


def link(res):
    """{video_id: (folder, uploaded_file_name)} from Scheduled Uploads.csv, then exact titles, then a strict fuzzy title match."""
    got, used = {}, set()
    sp = os.path.join(RN, "Scheduled Uploads.csv")
    byname = {os.path.basename(d): (ch, d) for ch, d in folders()}
    if os.path.exists(sp):
        for r in csv.DictReader(open(sp, encoding="utf-8")):
            parts = re.split(r"[\\/]", r.get("file", ""))
            if len(parts) >= 2 and parts[-2] in byname and r["video_id"] in res:
                got[r["video_id"]] = (byname[parts[-2]][1], parts[-1])
                used.add(byname[parts[-2]][1])
    cards = []
    for ch, d in folders():
        if d in used:
            continue
        t, _, _ = card(d)
        name = re.sub(r"^\d{4}-\d{2}-\d{2}\s+(A2\s+)?(S?\d+\s+)?", "", os.path.basename(d))
        cards.append((ch, d, t, name))
    for vid, r in res.items():  # exact title
        if vid in got:
            continue
        for ch, d, t, name in cards:
            if d not in used and ch == r["channel"] and t and norm(t) == norm(re.sub(r"#\w+", "", r["title"])):
                got[vid] = (d, "")
                used.add(d)
                break
    for vid, r in res.items():  # fuzzy, strict: 75%+ of the folder's words, and clearly better than the runner-up
        if vid in got:
            continue
        vt = set(rm.toks(r["title"]))
        scored = []
        for ch, d, t, name in cards:
            if d in used or ch != r["channel"]:
                continue
            ft = set(rm.toks(t or name))
            if ft and vt:
                scored.append((len(ft & vt) / len(ft) * 0.7 + 0.3 * len(ft & vt) / len(ft | vt), d))
        scored.sort(reverse=True)
        if scored and scored[0][0] >= 0.75 and (len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.1):
            got[vid] = (scored[0][1], "")
            used.add(scored[0][1])
    return got


def labels():
    out = {}
    if os.path.exists(LABELS):
        for r in csv.DictReader(open(LABELS, encoding="utf-8")):
            out.setdefault(r["video_id"], {})[r["feature"]] = r["value"]
    return out


# ---------------------------------------------------------------- features
FAMILY = re.compile(r"\b(dad|dads|father|son|sons|kid|kids|brother|brothers|mom|mother|family|daughter|bronny|boozer|rookie|teammates)\b", re.I)
LIST = re.compile(r"\bmost\b.*\b(in|nba) history\b|\bhistory\?", re.I)
SHOOTOUT = re.compile(r"shoot-?out|for (the )?penalties|on penalties|save[sd]? a penalty|penalty save", re.I)
WHW = re.compile(r"^\s*(why|how|what|who)\b", re.I)
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")
NUMWORD = re.compile(r"\d|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred|thousand|million)\b", re.I)


def sentences(t):
    t = re.sub(r"\{[^|}]*\|([^}]*)\}", r"\1", t or "")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s.strip()]


def features(r, d, fname, lab):
    ch = r["channel"]
    f = {}
    title = re.sub(r"#\w+", "", r.get("title", "")).strip()
    script = open(os.path.join(d, "script.txt"), encoding="utf-8").read() if d and os.path.exists(os.path.join(d, "script.txt")) else ""
    ctitle, tags, ctext = card(d) if d else ("", "", "")
    sents = sentences(script)
    # topic
    f["topic_family_kid"] = bool(FAMILY.search(title + " " + (sents[0] if sents else ""))) if ch == "nba" else None
    f["topic_record_list"] = bool(LIST.search(title)) if ch == "nba" else None
    lane_line = ""
    for nm in ("notes.md", "UPLOAD.md"):
        pth = os.path.join(d, nm) if d else ""
        if pth and os.path.exists(pth):
            m = re.search(r"\*\*Lane[^*]*:\*\*\s*(.+)", open(pth, encoding="utf-8-sig").read())
            if m:
                lane_line = m.group(1)
                break
    # FC lane: the folder's own Lane line says "shootout" (builders write it); else the title; labels.csv wins for posted Shorts
    f["topic_shootout"] = (bool(re.search(r"shoot-?out", lane_line, re.I)) if lane_line else bool(SHOOTOUT.search(title))) if ch == "fc" else None
    f["topic_countdown"] = bool(re.search(r"\b(\d|three|five) times\b|\btop (\d|five|three)\b", title, re.I))
    # script
    w = rm.word_feats(os.path.join(d, "words.json")) if d else {}
    f["script_words"] = w.get("n_words")
    f["script_wpm"] = w.get("wpm")
    f["script_wpm_gt230"] = (w["wpm"] > 230) if w.get("wpm") else None
    f["script_line1_words"] = w.get("line1_words")
    f["script_line1_le11"] = (w["line1_words"] <= 11) if w.get("line1_words") else None
    f["script_number_by_3s"] = (w.get("first_number_s") is not None and w["first_number_s"] <= 3.0) if w else None
    f["script_questions"] = sum(s.endswith("?") for s in sents) if sents else None
    f["script_last_line_words"] = len(sents[-1].split()) if sents else None
    f["script_payoff_number"] = bool(NUMWORD.search(sents[-1])) if sents else None
    f["script_title_first"] = (len(set(rm.toks(sents[0])) & set(rm.toks(title))) / max(1, len(set(rm.toks(title)))) >= 0.7) if sents and title else None
    f["script_live_audio"] = bool(w.get("live_words")) if w else None
    # edit: the real timeline is shots.json (start times as rendered); cuts.json adds sources, overlays and replays when it exists
    s = rm.shot_feats(d) if d else {}
    sj = rm.load(os.path.join(d, "shots.json"), []) if d else []
    total = r.get("length_s") or (w.get("voice_s") and w["voice_s"] + 0.3)
    if isinstance(sj, list) and len(sj) >= 2 and total and all(isinstance(x, dict) and "start" in x for x in sj):
        starts = [float(x["start"]) for x in sj]
        lens = [b - a for a, b in zip(starts, starts[1:])] + [max(0.0, total - starts[-1])]
        s.update(n_shots=len(sj), shots_first3=sum(t < 3 for t in starts), shot1_len=lens[0], median_shot=round(st.median(lens), 2),
                 last_shot_len=round(lens[-1], 2), replays=s.get("replays") or sum(1 for x in sj if x.get("replay")))
        f["edit_cards"] = any(x.get("kind") == "card" for x in sj)
    f["edit_shots"] = s.get("n_shots")
    f["edit_shots_le15"] = (s["n_shots"] <= 15) if s.get("n_shots") else None
    f["edit_shots_first3_le2"] = (s["shots_first3"] <= 2) if s.get("n_shots") else None
    f["edit_shot1_ge2"] = (s["shot1_len"] >= 2.0) if s.get("n_shots") else None
    f["edit_median_shot"] = s.get("median_shot")
    f["edit_last_shot_ge2"] = (s["last_shot_len"] >= 2.0) if s.get("n_shots") else None
    f["edit_replay"] = bool(s.get("replays")) if s.get("n_shots") else None
    f["edit_overlays"] = s.get("overlays")
    f["edit_blurfit_share"] = s.get("blurfit_share")
    f["edit_sources"] = s.get("n_sources")
    cj = rm.load(os.path.join(d, "cuts.json"), {}) if d else {}
    shots = cj.get("shots") if isinstance(cj, dict) else None
    if shots:
        tot = sum(x.get("len") or 0 for x in shots) or 1
        by = {}
        for x in shots:
            by[x.get("src", "")] = by.get(x.get("src", ""), 0) + (x.get("len") or 0)
        f["edit_one_source_share"] = round(max(by.values()) / tot, 2)
        f["edit_count_up"] = any(isinstance(o, dict) and o.get("count") for x in shots for o in (x.get("overlay") or []))
        f["edit_cards"] = any(x.get("kind") == "card" for x in shots)
        f["edit_loop"] = bool(cj.get("loop")) or (shots[-1].get("src") == shots[0].get("src") and abs((shots[-1].get("at") or 0) - (shots[0].get("at") or 0)) < 1.0)
    sfx = rm.load(os.path.join(d, "sfx.json"), []) if d else []
    f["edit_sfx"] = len(sfx) if isinstance(sfx, list) else (len(sfx.get("sfx", [])) if isinstance(sfx, dict) else None)
    cap = rm.ass_feats(os.path.join(d, "captions.ass")) if d else {}
    f["edit_caption_colour"] = (cap.get("cap_colored_screens", 0) > 0) if cap.get("cap_screens") else None
    # package
    f["pkg_title_words"] = len(title.split())
    f["pkg_opener_whw"] = bool(WHW.search(title))
    f["pkg_question"] = "?" in title
    f["pkg_emoji"] = bool(EMOJI.search(r.get("title", "")))
    f["pkg_digit"] = bool(re.search(r"\d", title))
    f["pkg_hashtags"] = len(re.findall(r"#\w+", r.get("title", "")))
    tl = [x for x in (tags or "").split(",") if x.strip()]
    f["pkg_tags_full"] = (len(tags) >= 380) if tags else None
    f["pkg_pinned"] = bool(re.search(r"pinned comment[^\n]*:\**\s*\S", ctext, re.I)) if ctext else None
    f["pkg_hour_et"] = r.get("hour_et")
    f["pkg_morning"] = (r["hour_et"] < 10) if r.get("hour_et") is not None else None
    name = (fname or "") + " " + " ".join(os.path.basename(x) for x in glob.glob(os.path.join(d, "DRAFT*.mp4"))) if d else (fname or "")
    up = fname or ""
    f["pkg_music_arm"] = ("music" if re.search(r"\(music\)|, music\)|with music", up, re.I) else "no music" if re.search(r"no music", up, re.I) else "")
    f["pkg_real_audio"] = bool(re.search(r"real audio", up, re.I)) if up else None
    # length
    L = r.get("length_s")
    f["len_s"] = L
    if ch == "nba" and L:
        f["len_le25"] = L <= 25
        f["len_20_25"] = 20 <= L <= 25
    # the card's Arms line (only for features no file shows)
    m = re.search(r"\*\*Arms:\*\*\s*(.+)", ctext or "")
    f["arms"] = m.group(1).strip() if m else ""
    for k, v in (lab or {}).items():  # hand labels win (Research Notes/Lab/labels.csv)
        f[k] = {"true": True, "false": False}.get(v.lower(), v)
    return f


def measure(quiet=False):
    res = results()
    lk = link(res)
    lab = labels()
    # posts the same ET day, per channel
    perday = {}
    for r in res.values():
        perday[(r["channel"], r["date"])] = perday.get((r["channel"], r["date"]), 0) + 1
    rows = []
    for vid, r in res.items():
        if not r["date"] or r["date"] < ERA[r["channel"]]:
            continue
        d, fname = lk.get(vid, ("", ""))
        f = features(r, d, fname, lab.get(vid))
        f["pkg_two_a_day"] = perday.get((r["channel"], r["date"]), 0) >= 2
        row = dict(video_id=vid, channel=r["channel"], date=r["date"], title=r["title"], age_days=r["age_days"], views=r["views"],
                   metric_src=r["metric_src"], views_now=r["views_now"], avg_pct=r["avg_pct"], engaged=r["engaged"], subs=r["subs"],
                   stayed=r.get("stayed"), folder=os.path.relpath(d, ROOT) if d else "")
        row.update(f)
        rows.append(row)
    os.makedirs(LAB, exist_ok=True)
    cols = list(dict.fromkeys(k for r in rows for k in r))
    with open(SHORTS, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["channel"], r["date"])))
    if not quiet:
        lin = sum(1 for r in rows if r["folder"])
        print(f"lab measure: {len(rows)} Shorts ({sum(r['channel']=='nba' for r in rows)} NBA, {sum(r['channel']=='fc' for r in rows)} FC), "
              f"{lin} linked to a production folder, {sum(r['views'] is not None for r in rows)} with a result -> {os.path.relpath(SHORTS, ROOT)}")
    return rows


def load_rows():
    if not os.path.exists(SHORTS):
        return measure(quiet=True)
    rows = list(csv.DictReader(open(SHORTS, encoding="utf-8")))
    for r in rows:
        for k, v in r.items():
            if v in ("True", "False"):
                r[k] = v == "True"
            elif k not in ("video_id", "channel", "date", "title", "folder", "arms", "metric_src", "pkg_music_arm") and v not in ("", None):
                r[k] = num(v) if num(v) is not None else v
            elif v == "":
                r[k] = None
    return rows


# ---------------------------------------------------------------- statistics
def auc(b, a):
    """P(random b beats random a); ties count half."""
    if not a or not b:
        return None
    wins = sum((x > y) + 0.5 * (x == y) for x in b for y in a)
    return wins / (len(a) * len(b))


def perm_p(b, a, n=2000, seed=7):
    if len(a) < 2 or len(b) < 2:
        return None
    obs = abs(auc(b, a) - 0.5)
    pool, k = a + b, len(b)
    rnd, hit = random.Random(seed), 0
    for _ in range(n):
        rnd.shuffle(pool)
        if abs(auc(pool[:k], pool[k:]) - 0.5) >= obs - 1e-12:
            hit += 1
    return (hit + 1) / (n + 1)


def med(xs):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else None


def fn(x, fmt="{:,.0f}", none="-"):
    return none if x is None else fmt.format(x)


def pair(a, b):
    return f"{fn(a, '{:.0f}')}% vs {fn(b, '{:.0f}')}%" if a is not None and b is not None else "-"


# ---------------------------------------------------------------- study
PARTS = {"topic": "topic_", "script": "script_", "edit": "edit_", "package": "pkg_", "length": "len_"}
SKIP = {"pkg_music_arm", "arms"}
RULECHECK = [  # rule, feature, channel, value that should win ("+") or "0" = expected no effect (a scrapped rule)
    ("A3 FC lane = famous penalty shootout", "topic_shootout", "fc", "+"),
    ("A4 NBA family / kid / rookie lane", "topic_family_kid", "nba", "+"),
    ("B1 NBA record lists", "topic_record_list", "nba", "+"),
    ("A5 NBA length 25 s or less", "len_le25", "nba", "+"),
    ("A6 line 1 is 11 words or fewer", "script_line1_le11", "all", "+"),
    ("A8 pace over 230 wpm (NBA)", "script_wpm_gt230", "nba", "+"),
    ("A7 payoff held (last shot 2 s+)", "edit_last_shot_ge2", "all", "+"),
    ("Edit: shot 1 at least 2 s", "edit_shot1_ge2", "all", "+"),
    ("C2 scrapped: 2 or fewer shots in the first 3 s", "edit_shots_first3_le2", "all", "0"),
    ("C2 scrapped: one source under 35%", "edit_one_source_share", "all", "0"),
    ("C4 scrapped: question titles", "pkg_question", "all", "0"),
    ("C4 scrapped: emoji in titles", "pkg_emoji", "all", "0"),
    ("C3 scrapped: pinned comment", "pkg_pinned", "all", "0"),
    ("Tags filled (owner rule; no reach claim)", "pkg_tags_full", "all", "0"),
    ("C6 scrapped: posting before 10 AM ET", "pkg_morning", "all", "0"),
]


def split(rows, feat):
    vals = [r[feat] for r in rows if r.get(feat) is not None and r.get("views") is not None]
    if not vals:
        return None
    if all(isinstance(v, bool) for v in vals):
        yes = [r["views"] for r in rows if r.get(feat) is True and r.get("views") is not None]
        no = [r["views"] for r in rows if r.get(feat) is False and r.get("views") is not None]
        ay = [r["avg_pct"] for r in rows if r.get(feat) is True]
        an = [r["avg_pct"] for r in rows if r.get(feat) is False]
        return dict(kind="yes/no", hi=yes, lo=no, hi_lab="yes", lo_lab="no", avg_hi=med(ay), avg_lo=med(an))
    if all(isinstance(v, (int, float)) for v in vals):
        m = st.median(vals)
        hi = [r for r in rows if isinstance(r.get(feat), (int, float)) and r.get("views") is not None and r[feat] > m]
        lo = [r for r in rows if isinstance(r.get(feat), (int, float)) and r.get("views") is not None and r[feat] <= m]
        return dict(kind=f"above vs at/below {m:g}", hi=[r["views"] for r in hi], lo=[r["views"] for r in lo], hi_lab=f">{m:g}", lo_lab=f"<={m:g}",
                    avg_hi=med([r["avg_pct"] for r in hi]), avg_lo=med([r["avg_pct"] for r in lo]))
    return None


def verdict(s):
    nh, nl = len(s["hi"]), len(s["lo"])
    if min(nh, nl) < 5:
        return "too few", None, None, None
    a, p = auc(s["hi"], s["lo"]), perm_p(s["hi"], s["lo"])
    ratio = (med(s["hi"]) or 0) / (med(s["lo"]) or 1)
    if p < 0.05 and (ratio >= 1.3 or ratio <= 1 / 1.3):
        v = "likely real"
    elif p < 0.2:
        v = "maybe"
    else:
        v = "no sign"
    return v, a, p, ratio


def study(part="all", channel=None, write=True):
    rows = [r for r in load_rows() if r.get("views") is not None]
    chans = [channel] if channel else ["nba", "fc"]
    prefixes = list(PARTS.values()) if part == "all" else [PARTS[part]]
    lines = [f"# Lab study: {part} ({today():%b %d, %Y})", "",
             "Auto-written by `python Tools/lab.py study`. Each row splits our Shorts on one feature and compares views (72 h as the API reports it on day 5-8, or current views once 5+ days old).",
             "**Score** = chance a Short on the first side beats one on the second (50 = no difference). **p** = permutation test. n under 5 on a side = too few.",
             "Correlation, not proof: topic is mixed into everything. Re-run any time; rows change as Shorts age.", ""]
    for ch in chans:
        R = [r for r in rows if r["channel"] == ch]
        lines += [f"## {ch.upper()}: {len(R)} Shorts with a result, median {med([r['views'] for r in R]) or 0:,.0f} views", "",
                  "| Feature | Split | Views (n) first side | Views (n) second side | Gap | Score | p | Avg % viewed | Read |", "|---|---|---|---|---|---|---|---|---|"]
        out = []
        feats = [k for k in (R[0].keys() if R else []) if any(k.startswith(p) for p in prefixes) and k not in SKIP]
        for k in feats:
            s = split(R, k)
            if not s or not s["hi"] and not s["lo"]:
                continue
            v, a, p, ratio = verdict(s)
            out.append((p if p is not None else 9, k, s, v, a, ratio))
        for p, k, s, v, a, ratio in sorted(out, key=lambda x: x[0]):
            lines.append(f"| `{k}` | {s['kind']} | {fn(med(s['hi']))} ({len(s['hi'])}) | {fn(med(s['lo']))} ({len(s['lo'])}) | "
                         f"{fn(ratio, '{:.2f}x')} | {fn(None if a is None else a * 100)} | {fn(None if p >= 9 else p, '{:.3f}')} | "
                         f"{pair(s['avg_hi'], s['avg_lo'])} | **{v}** |")
        lines.append("")
    # rule check: is each rule still backed by the data?
    lines += ["## Rule check (does the data still back each rule?)", "",
              "| Rule | Feature | Channel | Result | Status |", "|---|---|---|---|---|"]
    for rule, feat, ch0, want in [(a, b, c, d) for a, b, cc, d in RULECHECK for c in (("nba", "fc") if cc == "all" else (cc,))]:
        ch = ch0  # "all" rules are checked per channel: pooling mixes two medians 2x apart
        R = [r for r in rows if r["channel"] == ch]
        s = split(R, feat) if R else None
        if not s:
            lines.append(f"| {rule} | `{feat}` | {ch} | no data | TOO FEW |")
            continue
        v, a, p, ratio = verdict(s)
        res = f"{med(s['hi']) or 0:,.0f} ({len(s['hi'])}) vs {med(s['lo']) or 0:,.0f} ({len(s['lo'])})" + (f", score {a*100:.0f}, p {p:.2f}" if a is not None else "")
        if v == "too few":
            status = "TOO FEW"
        elif want == "+":
            status = "SUPPORTED" if (v in ("likely real", "maybe") and a > 0.5) else ("AGAINST: revisit" if v in ("likely real", "maybe") else "NOT SHOWN yet")
        else:
            status = "SCRAP STANDS (no effect)" if v == "no sign" else "REVISIT: it may matter"
        lines.append(f"| {rule} | `{feat}` | {ch} | {res} | **{status}** |")
    lines += [""] + scorer_report(load_rows())
    text = "\n".join(lines) + "\n"
    if write:
        p = os.path.join(LAB, f"Study - {part} ({today():%Y-%m-%d}).md")
        open(p, "w", encoding="utf-8").write(text)
        print(f"lab study: wrote {os.path.relpath(p, ROOT)}")
    return text


# ---------------------------------------------------------------- predictor (Nov 7: "go more in depth with the scoring")
# Predicted views = the channel median x the product of each feature's effect, where an effect is the ratio of median views with vs
# without the feature, SHRUNK toward 1 by its sample size (n_small / (n_small + K)), and applied relative to how common the feature is
# (so a feature most Shorts have adds little). Only features with a reason to matter are used (topic + the backed rules); the
# leave-one-out backtest below says honestly how well this ranks Shorts. Score 0-100 = 50 + 25 x log2(predicted / channel median).
MODEL = {"nba": ["topic_family_kid", "topic_record_list", "topic_countdown", "len_le25", "script_line1_le11", "pkg_opener_whw", "pkg_morning", "edit_shots_le15"],
         "fc": ["topic_shootout", "script_line1_le11", "script_payoff_number", "pkg_morning"]}
K = 6


def fit(rows, ch):
    R = [r for r in rows if r["channel"] == ch and r.get("views") is not None]
    base = med([r["views"] for r in R]) or 1
    model = {}
    for f in MODEL[ch]:
        yes = [r["views"] for r in R if r.get(f) is True]
        no = [r["views"] for r in R if r.get(f) is False]
        if min(len(yes), len(no)) < 4:  # under 4 on a side, a feature is mostly the topic it rides with: leave it out
            continue
        eff = math.log(max(1, med(yes)) / max(1, med(no))) * min(len(yes), len(no)) / (min(len(yes), len(no)) + K)
        model[f] = (eff, len(yes) / (len(yes) + len(no)), len(yes), len(no))
    return base, model


def predict_row(fitted, r):
    base, model = fitted
    lp, why = math.log(base), []
    for f, (eff, p, ny, nn) in model.items():
        x = r.get(f)
        if x is None:
            continue
        c = eff * ((1 if x is True else 0) - p)
        lp += c
        if abs(c) >= 0.05:
            why.append(f"{f}={'yes' if x is True else 'no'} {math.exp(c):.2f}x")
    pv = math.exp(lp)
    return pv, max(0, min(100, round(50 + 25 * math.log2(pv / base)))), why


def backtest(rows, ch):
    R = [r for r in rows if r["channel"] == ch and r.get("views") is not None]
    pairs = []
    for i, r in enumerate(R):
        fitted = fit(R[:i] + R[i + 1:], ch)
        pairs.append((predict_row(fitted, r)[0], r["views"]))
    if len(pairs) < 8:
        return None
    rho = spearman([a for a, _ in pairs], [b for _, b in pairs])
    base = med([b for _, b in pairs])
    top = sorted(pairs, key=lambda x: -x[0])[: max(1, len(pairs) // 3)]
    bot = sorted(pairs, key=lambda x: x[0])[: max(1, len(pairs) // 3)]
    return dict(n=len(pairs), rho=rho, top_hit=sum(v > base for _, v in top) / len(top), bot_hit=sum(v > base for _, v in bot) / len(bot),
                top_med=med([v for _, v in top]), bot_med=med([v for _, v in bot]))


def spearman(a, b):
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
        for k, i in enumerate(o):
            r[i] = k
        return r
    x, y = rk(a), rk(b)
    n = len(a); mx, my = sum(x) / n, sum(y) / n
    c = sum((i - mx) * (j - my) for i, j in zip(x, y)); vx = sum((i - mx) ** 2 for i in x) ** .5; vy = sum((j - my) ** 2 for j in y) ** .5
    return round(c / (vx * vy), 2) if vx and vy else None


def folder_row(d, slot_hour=None):
    """A pseudo-row for a folder that isn't posted yet (draft, prep or plan), so the same features and model can score it."""
    ch = "fc" if "Soccer Channel" in os.path.abspath(d) else "nba"
    title, _, ctext = card(d)
    if not title:
        title = re.sub(r"^\d{4}-\d{2}-\d{2}\s+(A2\s+)?(S?\d+\s+)?", "", os.path.basename(d))
    L = None
    vids = glob.glob(os.path.join(d, "DRAFT*.mp4"))
    if vids:
        try:
            import subprocess
            L = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vids[0]], text=True).strip())
        except Exception:
            L = None
    if L is None:
        w = rm.word_feats(os.path.join(d, "words.json"))
        if w.get("voice_s"):
            L = w["voice_s"] + 0.4
        elif os.path.exists(os.path.join(d, "script.txt")):
            n = len(re.sub(r"\{[^|}]*\|([^}]*)\}", r"\1", open(os.path.join(d, "script.txt"), encoding="utf-8").read()).split())
            L = n / (225 if ch == "nba" else 230) * 60 + 0.6
    if slot_hour is None:
        try:
            import schedule_ready as sr
            sl = sr.slot_of(ctext or "", today().year)
            slot_hour = sl.hour + sl.minute / 60 if sl else None
        except Exception:
            slot_hour = None
    r = dict(channel=ch, title=title, length_s=L, hour_et=slot_hour if slot_hour is not None else (7.25 if ch == "nba" else 12.0))
    f = features(r, d, "", None)
    r.update(f)
    return r


def predict_folder(d, rows=None, slot_hour=None):
    rows = rows if rows is not None else load_rows()
    r = folder_row(d, slot_hour)
    pv, sc, why = predict_row(fit(rows, r["channel"]), r)
    return dict(channel=r["channel"], title=r["title"], predicted=round(pv), score=sc, why=why, length_s=r.get("length_s"))


def scorer_report(rows):
    lines = ["## How good is the scorer? (leave-one-out backtest: each Short predicted from all the others)", "",
             "| Channel | n | Rank correlation (predicted vs real) | Top third beat the median | Bottom third beat the median | Median views top / bottom third | Features used (effect, n yes/no) |",
             "|---|---|---|---|---|---|---|"]
    for ch in ("nba", "fc"):
        b = backtest(rows, ch)
        base, model = fit(rows, ch)
        feats = "; ".join(f"`{f}` {math.exp(e):.2f}x ({ny}/{nn})" for f, (e, p, ny, nn) in sorted(model.items(), key=lambda x: -abs(x[1][0])))
        if b:
            lines.append(f"| {ch.upper()} | {b['n']} | **{b['rho']}** | {b['top_hit']*100:.0f}% | {b['bot_hit']*100:.0f}% | {fn(b['top_med'])} / {fn(b['bot_med'])} | {feats or '-'} |")
        else:
            lines.append(f"| {ch.upper()} | too few | - | - | - | - | {feats or '-'} |")
    lines += ["", "Read: a rank correlation of 0.3+ means the score is a useful filter; under 0.2 means rank by topic judgement and wait for more data. "
              "The effects are shrunk toward 1x when n is small, so new features move the score slowly.", ""]
    return lines



# ---------------------------------------------------------------- tests
def tests():
    return json.load(open(TESTS, encoding="utf-8"))


def save_tests(T):
    T["updated"] = today().isoformat()
    json.dump(T, open(TESTS, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def arm_of(t, r):
    """'A', 'B' or None for one Short. Detected value first; the card's Arms line for features no file shows."""
    for k, v in (t.get("filter") or {}).items():
        if r.get(k) != v:
            return None
    if t["kind"] == "lane":
        return "B" if r.get(t["feature"]) == t["arms"]["B"] else "A"
    v = r.get(t["feature"])
    if v is None or v == "":
        m = re.search(re.escape(t["id"]) + r"\s*=\s*([AB])", r.get("arms") or "")
        return m.group(1) if m else None
    for k in ("A", "B"):
        if v == t["arms"][k]:
            return k
    return None


def members(t, rows):
    ch = [r for r in rows if r["channel"] == t["channel"]]
    if t["kind"] == "lane":
        lo = (dt.date.fromisoformat(t["start"]) - dt.timedelta(days=t.get("window_days", 30))).isoformat()
        test = [r for r in ch if r["date"] >= t["start"] and arm_of(t, r) == "B"]
        base = [r for r in ch if r["date"] >= lo and arm_of(t, r) == "A"]
        return {"B": test, "A": base}
    return {k: [r for r in ch if r["date"] >= t["start"] and arm_of(t, r) == k] for k in ("A", "B")}


def score_test(t, rows, R):
    m = members(t, rows)
    a = [r["views"] for r in m["A"] if r.get("views") is not None]
    b = [r["views"] for r in m["B"] if r.get("views") is not None]
    sc, p = auc(b, a), perm_p(b, a)
    nmin, nmax = t.get("min_n", R["min_n"]), t.get("max_n", R["max_n"])
    if t["kind"] == "lane":
        enough, full = len(b) >= nmin and len(a) >= nmin, len(b) >= nmax
    else:
        enough, full = min(len(a), len(b)) >= nmin, min(len(a), len(b)) >= nmax
    status = "RUNNING"
    if enough and sc is not None and p is not None and p <= R["p"]:
        if sc >= R["adopt"]:
            status = "B WINS"
        elif sc <= R["drop"]:
            status = "A WINS"
    if status == "RUNNING" and full:
        status = "NO DIFFERENCE"
    return dict(nA=len(a), nB=len(b), medA=med(a), medB=med(b), score=None if sc is None else round(sc * 100), p=p, status=status,
                avgA=med([r["avg_pct"] for r in m["A"]]), avgB=med([r["avg_pct"] for r in m["B"]]),
                pending=sum(1 for r in m["A"] + m["B"] if r.get("views") is None), shorts=m)


def score(apply=True):
    T = tests()
    R = T["rules"]
    rows = load_rows()
    lines = [f"# Test scoreboard ({today():%a %b %d, %Y})", "", "Auto-written by `python Tools/lab.py score` (daily). Metric: views at 72 h (read on day 5-8: the API runs ~2 days behind). "
             "**Score** = chance a B Short beats an A Short (50 = no difference; 70+ = B is winning, 30- = A is winning). "
             f"A test decides at {R['min_n']}+ per arm with p <= {R['p']}; at {R['max_n']} per arm with no winner it closes as NO DIFFERENCE.", "",
             "| Test | Question | A (control) | B (new) | Score | p | Avg % viewed A / B | Status | Next |", "|---|---|---|---|---|---|---|---|---|"]
    decided = []
    for t in T["live"]:
        s = score_test(t, rows, R)
        nxt = {"RUNNING": f"needs {max(0, t.get('min_n', R['min_n']) - (s['nB'] if t['kind']=='lane' else min(s['nA'], s['nB'])))} more" + (f" (+{s['pending']} waiting for 72 h)" if s['pending'] else ""),
               "B WINS": f"adopt B: update {t.get('rule', 'the rule')}", "A WINS": f"keep A: update {t.get('rule', 'the rule')}",
               "NO DIFFERENCE": "keep the cheaper arm; close"}[s["status"]]
        fa = f"{s['medA']:,.0f} (n={s['nA']})" if s["medA"] is not None else f"- (n={s['nA']})"
        fb = f"{s['medB']:,.0f} (n={s['nB']})" if s["medB"] is not None else f"- (n={s['nB']})"
        lines.append(f"| `{t['id']}` | {t['question']} | {t['labels']['A']}: {fa} | {t['labels']['B']}: {fb} | "
                     f"{fn(s['score'])} | {fn(s['p'], '{:.2f}')} | {pair(s['avgA'], s['avgB'])} | **{s['status']}** | {nxt} |")
        if s["status"] != "RUNNING":
            decided.append((t, s))
    lines += ["", "## Shorts in each live test", ""]
    for t in T["live"]:
        s = score_test(t, rows, R)
        ex = "; ".join(f"{k}: " + (", ".join(f"{r['title'][:34]} ({fn(r.get('views'))})" for r in s["shorts"][k][-6:]) or "none yet") for k in ("A", "B"))
        lines.append(f"- `{t['id']}`: {ex}")
    lines += ["", "## Queue (starts when a live test of the same channel closes)", ""] + [f"- `{q['id']}` ({q['channel']}): {q['question']}" for q in T["queue"]]
    lines += ["", "## Decided", ""] + ([f"- {d['decided']}: `{d['id']}` **{d['status']}** (score {d.get('score')}, A {d.get('medA')} n={d.get('nA')}, B {d.get('medB')} n={d.get('nB')}). Rule: {d.get('rule', '-')}" for d in T["done"]] or ["- none yet"])
    if apply and decided:
        for t, s in decided:
            T["live"].remove(t)
            T["done"].append(dict(t, status=s["status"], score=s["score"], p=s["p"], nA=s["nA"], nB=s["nB"], medA=s["medA"], medB=s["medB"], decided=today().isoformat()))
            nxt = next((q for q in T["queue"] if q["channel"] == t["channel"]), None)
            if nxt:
                T["queue"].remove(nxt)
                nxt["start"] = (today() + dt.timedelta(days=1)).isoformat()
                T["live"].append(nxt)
            with open(os.path.join(LAB, "Decisions.md"), "a", encoding="utf-8") as fh:
                fh.write(f"- {today()}: `{t['id']}` {s['status']} (score {s['score']}, A median {s['medA']} n={s['nA']}, B median {s['medB']} n={s['nB']}). "
                         f"Update: {t.get('rule', '-')}. Next test: {nxt['id'] if nxt else 'none queued'}.\n")
        save_tests(T)
    open(os.path.join(LAB, "Scoreboard.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"lab score: {len(T['live'])} live tests, {len(decided)} decided today -> {os.path.relpath(os.path.join(LAB, 'Scoreboard.md'), ROOT)}")
    for t, s in decided:
        print(f"  DECIDED {t['id']}: {s['status']} (score {s['score']}). Update {t.get('rule', 'the rule')}.")


def plans():
    return list(csv.DictReader(open(PLANS, encoding="utf-8"))) if os.path.exists(PLANS) else []


def assign(ch, folder=None):
    T = tests()
    rows = load_rows()
    linked = {r["folder"] for r in rows if r.get("folder")}
    pend = [p for p in plans() if p["channel"] == ch and p["folder"] not in linked]  # planned but not yet posted
    picks = []
    print(f"Live tests for the next {ch.upper()} Short (follow every line; the lab detects most arms from the files):")
    for t in [t for t in T["live"] if t["channel"] == ch]:
        m = members(t, rows)
        pa = sum(1 for p in pend if p["test"] == t["id"] and p["arm"] == "A")
        pb = sum(1 for p in pend if p["test"] == t["id"] and p["arm"] == "B")
        if t["kind"] == "lane":
            due = len(m["B"]) + pb < t.get("min_n", T["rules"]["min_n"])
            arm = "B" if due else "-"
            print(f"  {t['id']}: {'make one if this idea fits' if due else 'enough samples'}: {t['how']['B']} (so far {len(m['B'])} posted + {pb} planned)")
        else:
            na, nb = len(m["A"]) + pa, len(m["B"]) + pb
            arm = "B" if nb <= na else "A"
            only = "".join(f" [only when {k} is {v}]" for k, v in (t.get("filter") or {}).items())
            print(f"  {t['id']}: use {arm} = {t['labels'][arm]}: {t['how'][arm]}{only}  (A {na}, B {nb} so far)")
        if t["kind"] == "ab" and t.get("builder", True):  # lane tests and schedule-driven tests are detected, not planned
            picks.append((t["id"], arm))
    if not [t for t in T["live"] if t["channel"] == ch]:
        print("  none")
    if folder and picks:
        up = os.path.join(folder, "UPLOAD.md")
        line = "**Arms:** " + ", ".join(f"{i}={a}" for i, a in picks)
        if os.path.exists(up):
            txt = open(up, encoding="utf-8").read()
            txt = re.sub(r"^\*\*Arms:\*\*.*$", line, txt, flags=re.M) if re.search(r"^\*\*Arms:\*\*", txt, re.M) else txt.rstrip("\n") + "\n" + line + "\n"
            open(up, "w", encoding="utf-8").write(txt)
        new = not os.path.exists(PLANS)
        with open(PLANS, "a", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(["date", "channel", "folder", "test", "arm"])
            for i, a in picks:
                w.writerow([today().isoformat(), ch, os.path.relpath(os.path.abspath(folder), ROOT), i, a])
        print(f"  logged in {os.path.relpath(PLANS, ROOT)}" + (" and the card's **Arms:** line" if os.path.exists(up) else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["measure", "study", "assign", "score", "auto", "predict"])
    ap.add_argument("ch", nargs="?")
    ap.add_argument("--part", default="all", choices=["all"] + list(PARTS))
    ap.add_argument("--channel", choices=["nba", "fc"])
    ap.add_argument("--folder")
    ap.add_argument("--no-apply", action="store_true")
    a = ap.parse_args()
    if a.cmd == "measure":
        measure()
    elif a.cmd == "study":
        measure(quiet=True)
        study(a.part, a.channel)
    elif a.cmd == "assign":
        if a.ch not in ("nba", "fc"):
            raise SystemExit("usage: lab.py assign nba|fc [--folder F]")
        assign(a.ch, a.folder)
    elif a.cmd == "predict":
        if not a.folder:
            raise SystemExit("usage: lab.py predict --folder F")
        p = predict_folder(a.folder)
        print(f"lab predict: {p['title'][:60]} [{p['channel']}] score {p['score']}/100, about {p['predicted']:,} views at 72 h"
              + (f" ({'; '.join(p['why'])})" if p['why'] else " (no feature moves it)"))
    elif a.cmd == "score":
        measure(quiet=True)
        score(apply=not a.no_apply)
    else:
        measure()
        score()
        study("all")


if __name__ == "__main__":
    main()
