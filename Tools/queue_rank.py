r"""Queue ranker (Nov 6, 2026; owner: "rate waiting Shorts and give them a time slot in order of priority; best go out asap, bad ones wait for filler").

  python Tools/queue_rank.py                 # rank every waiting Short, print the plan, write Research Notes/Queue Rank.md
  python Tools/queue_rank.py --qa            # also run qa_portions on each (slower; otherwise the cached qa_final.json / a quick check is used)
  python Tools/queue_rank.py --apply         # put the assigned slot at the top of each UPLOAD.md ("**Slot:** ... (queue_rank)") so schedule_ready.py books it

A WAITING Short = a folder with an UPLOAD.md and a DRAFT*.mp4, folder dated within 8 days, whose title is not already in Scheduled Uploads.csv.
SCORE (0-100), every part printed so you can argue with it:
  lane      30  the lane's measured median 72 h views (Test Log.csv) vs the channel median; an unmeasured lane gets 40% of the points
  topic     20  lightning-rod names in the title/script (stars the audience argues about); two stars = full points
  QA        20  PASS 20, each WARN -2 (floor 8), any FAIL = 0 and the Short is held until fixed
  proof     10  sources.csv rows all verified = 10, partly = 5, none = 0
  idea      10  the Idea Candidates gauge % for that idea (80% = 8 points), else 5
  package   10  title <= 60 chars, 24+ tags, pinned comment, cover.jpg, empty description (2 each)
PERISHABLE (a game-night moment or a live chase) is NOT ranked against evergreen: it takes the first slot before it goes stale. Stale = more than 20 h after
the game for NBA moments, which the card says ("skip it if it misses"); stale ones are dropped to notes.
SLOTS: the posting grid (next_gap.grid_for) minus what Scheduled Uploads.csv already books, 6 h minimum gap, 3 a day max. Best score takes the earliest
open slot (prime slots first). A score under 55 is FILLER: it takes a slot only within 36 h of now (so something is posted) and never a prime slot a better
Short could take later. A FAIL holds a Short out of every slot.
Predictions are a ranking aid, not views: check Outcome Log.md afterwards and tune WEIGHTS below.
"""
import argparse, csv, datetime, glob, json, os, re, statistics as st, subprocess, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import schedule_ready as sr
import next_gap as ng

ET = ZoneInfo("America/New_York")
RN = os.path.join(ROOT, "Research Notes")
STARS = ["lebron", "curry", "steph", "jokic", "wemby", "wembanyama", "luka", "doncic", "giannis", "durant", "jordan", "kobe", "shaq", "flagg", "bronny", "kawhi",
         "messi", "ronaldo", "mbappe", "haaland", "kane", "bellingham", "yamal", "neymar", "salah", "de bruyne", "ballon d'or", "world cup", "real madrid", "barcelona",
         "man united", "manchester united", "liverpool", "arsenal", "chelsea", "klay", "rodman", "draymond"]
PRIME = {"nba": {(7, 15), (15, 30)}, "fc": {(12, 0)}}
LANES = []
SCHED_DIRS = set()
MIN_GAP_H, MAX_PER_DAY, FILLER_BELOW, FILLER_WITHIN_H = 6, 3, 55, 36


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def booked():
    out, titles = [], set()
    global SCHED_DIRS
    SCHED_DIRS = set()
    for r in csv.DictReader(open(os.path.join(RN, "Scheduled Uploads.csv"), encoding="utf-8")):
        try:
            out.append((r["channel"], datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)))
        except ValueError:
            pass
        titles.add(norm(r["title"]))
        SCHED_DIRS.add(os.path.normpath(os.path.dirname(r["file"].replace("\\", os.sep))).lower())
    return out, titles


def lane_medians():
    rows = list(csv.DictReader(open(os.path.join(RN, "Test Log.csv"), encoding="utf-8")))
    by, allv = {}, {}
    for r in rows:
        try:
            v = float(r["views_72h"])
        except (ValueError, KeyError):
            continue
        by.setdefault((r["channel"], r["lane"].lower()), []).append(v)
        allv.setdefault(r["channel"], []).append(v)
    med = {k: st.median(v) for k, v in by.items() if len(v) >= 2}
    base = {c: st.median(v) for c, v in allv.items()}
    return med, base


def card_field(text, name):
    m = re.search(r"\*\*" + name + r":?\*\*:?\s*(.+)", text, re.I)
    return m.group(1).strip() if m else ""


def title_of(text):
    t = card_field(text, "Title")
    if not t:
        m = re.search(r"^#\s*(?:DRAFT[^\-]*-\s*awaiting approval\s*-\s*)?(?:\[[^\]]+\]\s*)?(?:Upload:\s*)?(.+?)(?:\s*\(DRAFT.*)?$", text, re.M)
        t = m.group(1).strip() if m else ""
    return t


def ideas():
    p = os.path.join(RN, "Idea Candidates.md")
    out = []
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            m = re.match(r"- \*\*(\d+)%\*\*\s+(.*)", l)
            if m:
                out.append((int(m.group(1)), norm(m.group(2))))
    return out


def lane_of(text, folder):
    m = re.search(r"\blane:?\*{0,2}:?\s*([A-Za-z \-/]+)", text, re.I)
    return m.group(1).strip().lower() if m else ""


def qa_of(ch, d, video, run_qa):
    cache = os.path.join(d, "qa_final.json")
    if not run_qa and os.path.exists(cache) and os.path.getmtime(cache) >= os.path.getmtime(video):
        j = json.load(open(cache, encoding="utf-8"))
        return j["fails"], j["warns"], "cached"
    if not run_qa:
        return None, None, "not run (use --qa)"
    r = subprocess.run([sys.executable, os.path.join(HERE, "qa_portions.py"), "--folder", d, "--video", video, "--channel", ch], capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = [l for l in r.stdout.splitlines() if re.match(r"\s{2}(PASS|WARN|FAIL)\s", l)]
    fails = sum(l.strip().startswith("FAIL") for l in lines)
    warns = sum(l.strip().startswith("WARN") and " LIVE " not in l for l in lines)
    json.dump({"fails": fails, "warns": warns}, open(cache, "w"))
    return fails, warns, "run"


def waiting(now, run_qa):
    bk, titles = booked()
    med, base = lane_medians()
    global LANES
    LANES = list(med.keys())
    idl = ideas()
    out = []
    for ch, d in sr.candidates():
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", os.path.basename(d))
        if not m or (now.date() - datetime.date(*map(int, m.groups()))).days > 8:
            continue
        drafts = [x for x in glob.glob(os.path.join(d, "DRAFT*.mp4"))]
        if not drafts:
            continue
        if os.path.normpath(os.path.relpath(d, ROOT)).lower() in SCHED_DIRS:
            continue
        text = open(os.path.join(d, "UPLOAD.md"), encoding="utf-8-sig").read()
        title = re.sub(r"^(?:UPLOAD(?: package)?:?\s*)(?:#?S?\d+\s*)?", "", title_of(text), flags=re.I).strip(" *:-") or title_of(text)
        if not title or title.lower().startswith(("upload", "(")) or "DRAFT" in title:
            title = re.sub(r"^\d{4}-\d{2}-\d{2}\s+", "", os.path.basename(d))
        if not title or norm(title) in titles or "HOLD" in text.upper().split("\n")[0]:
            continue
        nom = [x for x in drafts if re.search(r"no[- ]?music", x, re.I)]
        video = (nom or drafts)[0]
        script = open(os.path.join(d, "script.txt"), encoding="utf-8").read() if os.path.exists(os.path.join(d, "script.txt")) else ""
        hay = norm(title + " " + script[:400])
        parts = {}
        lane = lane_of(text, d)
        mv = next((v for (c, l), v in med.items() if c == ch and lane and (l in lane or lane in l)), None)
        parts["lane"] = round(30 * min(1.0, 0.25 + 0.75 * (mv / (2.0 * base.get(ch, mv or 1)))) if mv and base.get(ch) else 12, 1)
        n_stars = sum(1 for s in STARS if s in hay)
        parts["topic"] = 20 if n_stars >= 2 else (13 if n_stars == 1 else 4)
        fails, warns, how = qa_of(ch, d, video, run_qa)
        parts["qa"] = 10 if fails is None else (0 if fails else max(8, 20 - 2 * warns))
        sp = os.path.join(d, "sources.csv")
        if os.path.exists(sp):
            rows = list(csv.DictReader(open(sp, encoding="utf-8")))
            ok = sum(1 for r in rows if str(r.get("verified", "")).lower().startswith(("y", "t", "1")))
            parts["proof"] = 10 if rows and ok == len(rows) else (5 if ok else 0)
        else:
            parts["proof"] = 3
        gm = next((p for p, i in idl if any(w in i for w in norm(title).split()[:3] if len(w) > 4)), None)
        parts["idea"] = round(gm / 10, 1) if gm else 5
        tags = card_field(text, r"Tags[^:*]*")
        parts["package"] = sum([len(title) <= 60, tags.count(",") >= 23, bool(card_field(text, "Pinned comment")), os.path.exists(os.path.join(d, "cover.jpg")), True])*2
        perish = bool(re.search(r"skip it if it misses|game night|last night|breaking|within 20 h", text, re.I)) or bool(re.search(r"\bnews\b", card_field(text, "Slot"), re.I))
        score = round(sum(parts.values()), 1)
        out.append(dict(ch=ch, dir=d, name=os.path.basename(d), title=title, parts=parts, score=score, fails=fails, warns=warns, qa=how, perish=perish, lane=lane or "?",
                        age_h=(now - datetime.datetime.fromtimestamp(os.path.getmtime(video), ET)).total_seconds() / 3600))
    return out


def open_slots(now, bk):
    slots = []
    for ch in ("nba", "fc"):
        for i in range(0, 6):
            day = now.date() + datetime.timedelta(days=i)
            for h, m in ng.grid_for(ch, day):
                t = datetime.datetime.combine(day, datetime.time(h, m), tzinfo=ET)
                if t < now + datetime.timedelta(hours=3):
                    continue
                slots.append((ch, t, (h, m) in PRIME[ch]))
    slots.sort(key=lambda x: x[1])
    free = []
    for ch, t, prime in slots:
        mine = [b for c, b in bk if c == ch]
        if any(abs((b - t).total_seconds()) < MIN_GAP_H * 3600 for b in mine) or sum(b.date() == t.date() for b in mine) >= MAX_PER_DAY:
            continue
        free.append((ch, t, prime))
    return free


def assign(items, free, now, bk):
    plan, chosen = [], {"nba": [b for c, b in bk if c == "nba"], "fc": [b for c, b in bk if c == "fc"]}
    def take(it, pred=lambda s: True):
        for s in list(free):
            ch, t, prime = s
            if ch != it["ch"] or not pred(s):
                continue
            if any(abs((b - t).total_seconds()) < MIN_GAP_H * 3600 for b in chosen[ch]) or sum(b.date() == t.date() for b in chosen[ch]) >= MAX_PER_DAY:
                continue
            free.remove(s); chosen[ch].append(t); return t
        return None
    order = sorted([i for i in items if i["fails"] in (None, 0)], key=lambda i: (not i["perish"], -i["score"]))
    for it in order:
        if it["perish"] and it["age_h"] > 20 and it["ch"] == "nba":
            it["state"], it["slot"] = "STALE: drop to notes (past 20 h)", None
        elif it["score"] < FILLER_BELOW:
            t = take(it, lambda s: not s[2] and (s[1] - now).total_seconds() < FILLER_WITHIN_H * 3600)
            it["state"], it["slot"] = ("FILLER: placed in a quiet slot", t) if t else ("FILLER: waits (no quiet slot within 36 h)", None)
        else:
            t = take(it)
            it["state"], it["slot"] = ("SCHEDULE", t) if t else ("WAIT: no open slot in 5 days", None)
    for it in items:
        if it["fails"]:
            it["state"], it["slot"] = "HOLD: QA FAIL, fix first", None
    return sorted(items, key=lambda i: (i["slot"] is None, i["slot"] or now, -i["score"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qa", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    bk, _ = booked()
    items = waiting(now, a.qa)
    if not items:
        print("No waiting Shorts."); return
    plan = assign(items, open_slots(now, bk), now, bk)
    lines = [f"# Queue ranking, {now:%a %b %d %H:%M} ET (auto: Tools/queue_rank.py)", "",
             "| Slot (ET) | Ch | Score | Short | Perishable | QA | Why (lane/topic/QA/proof/idea/pkg) | State |", "|---|---|---|---|---|---|---|---|"]
    for it in plan:
        p = it["parts"]
        qa = "-" if it["fails"] is None else f"{it['fails']}F {it['warns']}W"
        lines.append(f"| {it['slot']:%a %b %d %H:%M} | {it['ch']} | **{it['score']}** | {it['title'][:55]} | {'yes' if it['perish'] else 'no'} | {qa} | {p['lane']}/{p['topic']}/{p['qa']}/{p['proof']}/{p['idea']}/{p['package']} | {it['state']} |"
                     if it["slot"] else f"| - | {it['ch']} | **{it['score']}** | {it['title'][:55]} | {'yes' if it['perish'] else 'no'} | {qa} | {p['lane']}/{p['topic']}/{p['qa']}/{p['proof']}/{p['idea']}/{p['package']} | {it['state']} |")
    open(os.path.join(RN, "Queue Rank.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    if a.apply:
        for it in plan:
            if it["slot"] and it["state"].startswith(("SCHEDULE", "FILLER")):
                f = os.path.join(it["dir"], "UPLOAD.md")
                t = open(f, encoding="utf-8-sig").read()
                t = re.sub(r"^\*\*Slot:\*\* [^\n]*\(queue_rank\)\n", "", t, flags=re.M)
                s = it["slot"]
                line = f"**Slot:** {s:%a %b} {s.day}, {int(s.strftime('%I'))}:{s:%M %p} ET (queue_rank)\n"
                open(f, "w", encoding="utf-8").write(line + t)
        print("applied: the first Slot line of each UPLOAD.md is now the assigned slot.")


if __name__ == "__main__":
    main()
