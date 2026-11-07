r"""The auto queue (v2, Nov 7, 2026; owner: "automatically make your own queue based off what should go out on each time").
v1 (Nov 6) ranked built drafts with hand-set weights; v2 plans EVERY slot of the next days from everything we have, scored by the lab's data.

  python Tools/queue_rank.py               # plan the next 7 days -> Research Notes/Auto Queue.md + Research Notes/Lab/queue.json (+ Queue Rank.md)
  python Tools/queue_rank.py --days 10     # a longer view
  python Tools/queue_rank.py --apply       # also write the planned slot into each READY draft's card ("**Slot:** ... (queue_rank)") so
                                           # schedule_ready.py (PC, 6:30 AM/PM) books it. Owner-set future slots are never moved.

What fills a slot, in this order (the posting grid comes from next_gap.grid_for: NBA 7:15 AM + 3:30 PM, FC 12 PM; POSTING_TEST.txt odd days change it):
  ON YOUTUBE  already booked in Scheduled Uploads.csv: fixed.
  PINNED      a built draft whose card has an owner-set future slot.
  READY       a built draft with qa_final SHIP or FIX (no FAIL), not live, not booked. Paid-for voice goes out unless the lab predicts it terrible (< 30).
  BUILD       a prepped folder (script + sources, no DRAFT): the builder voices and cuts it by the deadline (slot - 20 h).
  IDEA        an Idea Candidates line (80%+): research + build by the deadline (slot - 44 h).
  MOMENT      NBA 3:30 PM is reserved for last night's moment (research 3:43 AM, build by noon) unless a fresh moment draft is READY.
  EMPTY       nothing fits: the gap-fill run builds the best idea, or the slot is skipped (skipping beats a weak Short).
Priority (0-100+): the lab's predicted score (0-100, 50 = a typical Short for the channel) + 25 for READY (credits already spent, unless predicted < 30)
+ 40 PINNED + 8 when it feeds a live lab lane test that still needs Shorts - 8 when it repeats the lane of the channel's previous slot - 10 for IDEA.
HOLD drafts (a QA FAIL) are listed with the first thing to fix and never slotted. Run `python Tools/qa_sweep.py` first so the QA cache is fresh.
"""
import argparse, csv, datetime, glob, json, os, re, statistics as st, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
ET = ZoneInfo("America/New_York")
RN = os.path.join(ROOT, "Research Notes")
SCHED_DIRS = set()
MIN_GAP_H, MAX_PER_DAY = 6, 3
BUILD_LEAD_H, IDEA_LEAD_H, TERRIBLE = 20, 44, 30


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


STOP = {"the", "and", "who", "his", "her", "for", "nba", "was", "with", "that", "this", "music", "draft", "awaiting", "approval", "real",
        "audio", "version", "just", "did", "has", "had", "are", "from", "into", "out", "its", "their", "they", "him", "shorts"}


def toks(s):
    return {w for w in norm(s).split() if len(w) > 2 and w not in STOP}


def posted_titles():
    """Titles already live or scheduled on YouTube, from the newest API daily files of both channels (Nov 7 fix: the owner also posts by
    hand, so Scheduled Uploads.csv alone missed them and the ranker offered already-posted Shorts for new slots). Used by schedule_ready.py too."""
    out = []
    for sub in ("api", "api FC"):
        files = sorted(glob.glob(os.path.join(RN, "Studio exports", sub, "daily *.csv")))
        if files:
            out += [toks(r.get("title", "")) for r in csv.DictReader(open(files[-1], encoding="utf-8"))]
    return [t for t in out if t]


def already_posted(names, posted):
    for n in names:
        t = toks(n)
        if not t:
            continue
        for p in posted:
            if len(t & p) >= 3 and len(t & p) / len(t | p) >= 0.6:  # Jaccard: near-identical titles only (a 'Part 2' list must pass)
                return True
    return False


def booked():
    out = []
    global SCHED_DIRS
    SCHED_DIRS = set()
    for r in csv.DictReader(open(os.path.join(RN, "Scheduled Uploads.csv"), encoding="utf-8")):
        if norm(r.get("title")) in ("", "unknown"):
            continue  # the deleted placeholder uploads
        try:
            out.append((r["channel"], datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET), r["title"]))
        except (KeyError, ValueError):
            continue
        parts = re.split(r"[\\/]", r.get("file", ""))
        if len(parts) >= 2:
            SCHED_DIRS.add(parts[-2].lower())
    return out


def card_field(text, name):
    m = re.search(r"\*\*" + name + r":?\*\*:?\s*(.+)", text, re.I)
    return m.group(1).strip() if m else ""


def ideas():
    p = os.path.join(RN, "Idea Candidates.md")
    out, ch = [], None
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            h = re.match(r"## (NBA|FC) candidates", l)
            if h:
                ch = h.group(1).lower()
            elif l.startswith("## "):
                ch = None
            m = re.match(r"- \*\*(\d+)%\*\*\s+(.*)", l)
            if m and ch:
                shape = (re.search(r"\[([^\]]*)\]", m.group(2)) or [None, ""])[1]
                dd = re.search(r"\((\d{4}-\d{2}-\d{2})\)", m.group(2))
                age = (datetime.date.today() - datetime.date.fromisoformat(dd.group(1))).days if dd else 0
                if shape.lower() in ("moment", "news") and age >= 1:
                    continue  # a moment idea is stale after a day (posted the morning after or not at all)
                out.append(dict(ch=ch, pct=int(m.group(1)), text=re.sub(r"\s*\[[^\]]*\].*$", "", m.group(2)).strip()))
    return out


def lane_name(row):
    if row.get("channel") == "fc":
        return "shootout" if row.get("topic_shootout") else "premise"
    if row.get("topic_record_list"):
        return "list"
    if row.get("topic_family_kid"):
        return "family"
    return "other"


def gather(now):
    import lab, schedule_ready as sr
    rows = lab.load_rows()
    fits = {ch: lab.fit(rows, ch) for ch in ("nba", "fc")}
    T = lab.tests()
    posted = posted_titles()
    bk = booked()
    btitles = {norm(t) for _, _, t in bk} | {norm(' '.join(p)) for p in posted}
    need = {}  # live lane tests still short of samples -> (channel, feature, value)
    for t in T["live"]:
        if t["kind"] == "lane":
            m = lab.members(t, rows)
            if len(m["B"]) < t.get("min_n", T["rules"]["min_n"]):
                need[t["id"]] = (t["channel"], t["feature"], t["arms"]["B"])
    items, holds = [], []
    for ch, d in lab.folders():
        name = os.path.basename(d)
        title, _, txt = lab.card(d)
        title = title or re.sub(r"^\d{4}-\d{2}-\d{2}\s+(A2\s+)?(S?\d+\s+)?", "", name)
        notes_txt = open(os.path.join(d, "notes.md"), encoding="utf-8").read() if os.path.exists(os.path.join(d, "notes.md")) else ""
        if re.search(r"LIVE ON YOUTUBE|^\s*#?\s*TRASH\b|\*\*Queue:\*\*\s*no|^\s*HOLD\b", (txt or "") + "\n" + notes_txt, re.I | re.M):
            continue  # "**Queue:** no (why)" in a card or notes keeps a folder out of the queue
        if name.lower() in SCHED_DIRS or norm(title) in btitles or already_posted([title, re.sub(r"^\S+ \S+ ", "", name)], posted):
            continue
        drafts = glob.glob(os.path.join(d, "DRAFT*.mp4"))
        has_script = os.path.exists(os.path.join(d, "script.txt")) and os.path.exists(os.path.join(d, "notes.md"))
        if not drafts and not has_script:
            continue
        if any(len(toks(title) & toks(b)) >= 3 for b in btitles):
            continue  # a near-duplicate of something already booked (e.g. an account-2 copy of a scheduled Short)
        if not drafts:  # BUILD only for recent prep: folder dated within 6 days (or ahead), or marked ready in its notes
            md = re.match(r"(?:A2\s+)?(\d{4})-(\d{2})-(\d{2})", name)
            recent = bool(md) and (now.date() - datetime.date(*map(int, md.groups()))).days <= 6
            notes = open(os.path.join(d, "notes.md"), encoding="utf-8").read()
            if not (recent or re.search(r"PREP: ready to voice|SCRIPT ONLY", notes)):
                continue
            scr = open(os.path.join(d, "script.txt"), encoding="utf-8").read()
            lane_l = (re.search(r"\*\*Lane[^*]*:\*\*\s*(.+)", notes) or [None, ""])[1]
            perishable = bool(re.search(r"\b(last night|tonight|yesterday|this morning)\b", scr, re.I) or re.search(r"\b(moment|news)\b", lane_l, re.I))
            if perishable and md and (now.date() - datetime.date(*map(int, md.groups()))).days >= 1:
                continue  # news or a moment that wasn't built in time: stale
        row = lab.folder_row(d)
        pv, score, why = lab.predict_row(fits[ch], row)
        it = dict(ch=ch, dir=d, name=name, title=title, pred=score, pred_views=round(pv), why=why, lane=lane_name(row), row=row, qa=None, verdict=None, first="")
        it["tests"] = [tid for tid, (c, f, v) in need.items() if c == ch and row.get(f) == v]
        if drafts:
            age_h = (now - datetime.datetime.fromtimestamp(max(os.path.getmtime(x) for x in drafts), ET)).total_seconds() / 3600
            perish = bool(re.search(r"last night|skip it if it misses|game night|within 20 h", (txt or "") + " " + (open(os.path.join(d, "script.txt"), encoding="utf-8").read() if has_script else ""), re.I))
            if perish and age_h > 30:
                continue  # a stale moment: never posted late
            if not perish and age_h > 21 * 24:
                continue  # older than 3 weeks: archive, not queue
            cache = os.path.join(d, "qa_final.json")
            j = json.load(open(cache, encoding="utf-8")) if os.path.exists(cache) else {}
            it.update(kind="READY", perish=perish, qa=j.get("qa_score"), verdict=j.get("verdict") or "NOT RUN",
                      first=((j.get("fail_list") or j.get("warn_list") or [""])[0])[:110])
            if it["verdict"] == "HOLD":
                holds.append(it)
                continue
            sl = sr.slot_of(txt or "", now.year)
            if sl and sl > now and "(queue_rank)" not in (re.search(r"\*\*Slot:\*\*[^\n]*", txt or "") or [""])[0]:
                it.update(kind="PINNED", pin=sl)
        else:
            it.update(kind="BUILD", perish=False)
        items.append(it)
    used = {norm(i["title"]) for i in items}
    for idea in ideas():
        if any(len(toks(idea["text"]) & toks(u)) >= 3 for u in used):
            continue
        items.append(dict(ch=idea["ch"], dir="", name="", title=idea["text"][:90], pred=max(0, min(100, idea["pct"] - 37)), pred_views=None, why=[f"gauge {idea['pct']}%"],
                          lane="idea", row={}, kind="IDEA", perish=False, qa=None, verdict=None, first="", tests=[]))
    return items, holds, bk, need


def priority(it, prev_lane):
    p = it["pred"]
    if it["kind"] == "PINNED":
        p += 40
    elif it["kind"] == "READY" and it["pred"] >= TERRIBLE:
        p += 25
    elif it["kind"] == "IDEA":
        p -= 10
    if it["tests"]:
        p += 8
    if prev_lane and it["lane"] == prev_lane and it["lane"] not in ("idea",):
        p -= 8
    return p


def plan(now, days):
    import next_gap as ng, schedule_ready as sr
    items, holds, bk, need = gather(now)
    out, prev = [], {"nba": None, "fc": None}
    premise_days = []
    pool = list(items)
    for i in range(days):
        day = now.date() + datetime.timedelta(days=i)
        for ch in ("nba", "fc"):
            for h, m in ng.grid_for(ch, day):
                t = datetime.datetime.combine(day, datetime.time(h, m), tzinfo=ET)
                if t < now + datetime.timedelta(hours=2):
                    continue
                hit = next((b for b in bk if b[0] == ch and abs((b[1] - t).total_seconds()) < 60), None)
                if hit:
                    out.append(dict(slot=t, ch=ch, kind="ON YOUTUBE", title=hit[2], score=None, why="booked (Scheduled Uploads.csv)", action="nothing: goes live by itself"))
                    continue
                c = sr.clash(ch, t, [(b[0], b[1], b[2][:40]) for b in bk])
                if c:
                    out.append(dict(slot=t, ch=ch, kind="BLOCKED", title="", score=None, why=c, action="none (6 h rule)"))
                    continue
                pin = next((x for x in pool if x["kind"] == "PINNED" and x["ch"] == ch and abs((x["pin"] - t).total_seconds()) < 60), None)
                if pin:
                    pool.remove(pin)
                    out.append(dict(slot=t, ch=ch, kind="PINNED", it=pin))
                    prev[ch] = pin["lane"]
                    continue
                moment_slot = ch == "nba" and (h, m) == (15, 30)
                lead = (t - now).total_seconds() / 3600
                cand = []
                for x in pool:
                    if x["ch"] != ch or x["kind"] == "PINNED":
                        continue
                    if moment_slot and not (x["kind"] == "READY" and x.get("perish")):
                        continue
                    if not moment_slot and x.get("perish") and x["kind"] == "READY":
                        pass  # a fresh moment can also take a morning slot
                    if x["kind"] == "BUILD" and (lead < BUILD_LEAD_H or x["pred"] < 40):
                        continue  # a prepped Short predicted under 40 only fills a slot nothing else wants (second pass)
                    if x["kind"] == "IDEA" and lead < IDEA_LEAD_H:
                        continue
                    if ch == "fc" and x["lane"] == "premise" and x["kind"] != "READY" and any(abs((day - p).days) < 7 for p in premise_days):
                        continue  # one new FC premise a week (fc-premise test); shootouts fill the rest
                    if x["kind"] == "READY" and x["pred"] < TERRIBLE and lead > 36:
                        continue  # a weak paid-for draft is filler: only near-term slots nothing better wants
                    cand.append((priority(x, prev[ch]), x))
                if not cand and not moment_slot:  # second pass: rather than an empty slot, a near-typical prepped/built Short as FILLER
                    cand = [(priority(x, prev[ch]) - 15, x) for x in pool if x["ch"] == ch and x["kind"] in ("READY", "BUILD") and x["pred"] >= 40
                            and not (x["kind"] == "BUILD" and lead < BUILD_LEAD_H)]
                    for _, x in cand:
                        x["filler"] = True
                if cand:
                    pr, x = max(cand, key=lambda c: c[0])
                    pool.remove(x)
                    if ch == "fc" and x["lane"] == "premise":
                        premise_days.append(day)
                    out.append(dict(slot=t, ch=ch, kind=x["kind"], it=x, priority=round(pr)))
                    prev[ch] = x["lane"]
                elif moment_slot:
                    out.append(dict(slot=t, ch=ch, kind="MOMENT", title="last night's best moment", score=None,
                                    why="the 3:30 PM slot is the morning-after moment (Playbook N2)",
                                    action=f"research {t - datetime.timedelta(hours=11, minutes=47):%a %I:%M %p}, build by {t - datetime.timedelta(hours=3, minutes=30):%a %I:%M %p}"))
                else:
                    out.append(dict(slot=t, ch=ch, kind="EMPTY", title="", score=None, why="nothing ready, prepped or rated 80%+", action="gap-fill builds the best new idea, or skip"))
    for o in out:
        x = o.get("it")
        if not x:
            continue
        if x.get("filler"):
            o["kind"] = x["kind"] + " (filler)"
        o.update(title=x["title"], score=x["pred"], qa=x.get("qa"), verdict=x.get("verdict"), lane=x["lane"], folder=os.path.relpath(x["dir"], ROOT) if x["dir"] else "",
                 why="; ".join(x["why"][:3]) + (f"; feeds test {', '.join(x['tests'])}" if x["tests"] else ""))
        if x["kind"] in ("READY", "PINNED"):
            o["action"] = "schedule (schedule_ready.py)" if x.get("verdict") in ("SHIP", "FIX") else "run qa_final first"
        elif x["kind"] == "BUILD":
            o["action"] = f"voice + cut by {o['slot'] - datetime.timedelta(hours=BUILD_LEAD_H):%a %I:%M %p} (lab.py assign {x['ch']} --folder first)"
        else:
            o["action"] = f"research + build by {o['slot'] - datetime.timedelta(hours=BUILD_LEAD_H):%a %I:%M %p}"
    left = [x for x in pool if x["kind"] in ("READY", "BUILD")]
    return out, holds, left


def write(now, days, out, holds, left):
    L = [f"# Auto queue ({now:%a %b %d, %I:%M %p} ET, next {days} days)", "",
         "Auto-written by `python Tools/queue_rank.py` (daily, after `qa_sweep.py`). Every slot of the posting grid, filled from what we have, best first.",
         "**Score** = the lab's prediction (50 = a typical Short for the channel; see `Research Notes/Lab/Study - all`). READY = built and passed QA; BUILD = prepped, needs voice + cut; "
         "IDEA = needs research; MOMENT = the 3:30 PM morning-after slot.", ""]
    for ch in ("nba", "fc"):
        L += [f"## {'NBA (MetaSports)' if ch == 'nba' else 'FC (MetaSports FC)'}", "", "| Slot (ET) | What | Short | Score | QA | Why | Next step |", "|---|---|---|---|---|---|---|"]
        for o in [o for o in out if o["ch"] == ch]:
            L.append(f"| {o['slot']:%a %b %d %I:%M %p} | **{o['kind']}** | {(o.get('title') or '-')[:60]} | {o.get('score') if o.get('score') is not None else '-'} | "
                     f"{(str(o.get('qa')) + ' ' + (o.get('verdict') or '')) if o.get('qa') is not None else (o.get('verdict') or '-')} | {(o.get('why') or '-')[:90]} | {o.get('action', '-')} |")
        L.append("")
    L += ["## Held (QA FAIL: fix first, never slotted)", ""] + ([f"- {h['ch']}: {h['title'][:60]} (score {h['pred']}): {h['first']}" for h in holds] or ["- none"])
    L += ["", "## Waiting with no slot this week", ""] + ([f"- {x['ch']}: {x['kind']} {x['title'][:60]} (score {x['pred']})" for x in left] or ["- none"])
    open(os.path.join(RN, "Auto Queue.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    open(os.path.join(RN, "Queue Rank.md"), "w", encoding="utf-8").write("# Queue ranking\n\nReplaced on Nov 7 by `Research Notes/Auto Queue.md` (queue_rank.py v2).\n")
    js = [dict(slot=o["slot"].isoformat(), ch=o["ch"], kind=o["kind"], title=o.get("title") or "", score=o.get("score"), qa=o.get("qa"), verdict=o.get("verdict"),
               lane=o.get("lane"), folder=o.get("folder", ""), why=o.get("why", ""), action=o.get("action", "")) for o in out]
    os.makedirs(os.path.join(RN, "Lab"), exist_ok=True)
    json.dump(dict(made=now.isoformat(), slots=js, holds=[dict(ch=h["ch"], title=h["title"], score=h["pred"], fix=h["first"]) for h in holds]),
              open(os.path.join(RN, "Lab", "queue.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def apply(out, now):
    n = 0
    for o in out:
        x = o.get("it")
        if not x or x["kind"] != "READY" or x.get("verdict") not in ("SHIP", "FIX"):
            continue
        f = os.path.join(x["dir"], "UPLOAD.md")
        t = open(f, encoding="utf-8-sig").read()
        t = re.sub(r"^\*\*Slot:\*\* [^\n]*\(queue_rank\)\n", "", t, flags=re.M)
        s = o["slot"]
        open(f, "w", encoding="utf-8").write(f"**Slot:** {s:%a %b} {s.day}, {int(s.strftime('%I'))}:{s:%M %p} ET (queue_rank)\n" + t)
        n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    now = datetime.datetime.now(ET)
    out, holds, left = plan(now, a.days)
    write(now, a.days, out, holds, left)
    kinds = {}
    for o in out:
        kinds[o["kind"]] = kinds.get(o["kind"], 0) + 1
    print(f"auto queue: {len(out)} slots in {a.days} days: " + ", ".join(f"{v} {k}" for k, v in sorted(kinds.items())) + f"; {len(holds)} held -> Research Notes/Auto Queue.md")
    if a.apply:
        print(f"applied: {apply(out, now)} READY draft(s) got their slot line (owner-set slots untouched)")


if __name__ == "__main__":
    main()
