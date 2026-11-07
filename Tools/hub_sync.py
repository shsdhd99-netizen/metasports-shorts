r"""Hub sync (Nov 7, 2026; owner: "automatically update shorts hubs with new updates").

Keeps the two Shorts Hubs and the task list in step with reality, from the repo's own records. Zero Claude credits for the work; a Claude
session applies the writes with ONE ArtifactData batch per artifact (Python can't reach the Hub database itself).

  1. In the session, save each Hub's documents:   ArtifactData list (collection shorts, then ideas; limit 1000, out_dir .hub_cache/<nba|fc>)
     and the task list:                           ArtifactData query (collection tasks, section == post, out_dir .hub_cache/tasks)
     and paste each listing's text (it has the versions) into .hub_cache/<nba|fc|tasks>/versions.txt.
  2. python Tools/hub_sync.py                     -> .hub_cache/out/<nba|fc|tasks>.json: the writes, pinned to those versions, ready for one batch call
  3. ArtifactData batch with each file's `writes`  (the file says which artifact url).

What it changes (only fields it owns; never an owner tick, never a rejected/held card's status):
  - shorts cards that are live on YouTube: status "posted", ytId, and `results` from the API (views, avg % watched, engaged %, the go-live date,
    note "auto <date>, 72 h: N"). A results note the owner typed is kept.
  - shorts cards still "ready": slotLabel = where the auto queue or YouTube has them ("Scheduled on YouTube: Wed Nov 11, 7:15 AM ET").
  - ideas: "UP NEXT" cards (doc ids q-1, q-2, ...) for the coming week from Research Notes/Lab/queue.json (BUILD / IDEA / MOMENT / EMPTY slots),
    so the Hub shows what is being made for which slot; old q- cards are deleted.
  - tasks: a "Post: <title>" task is ticked done (doneAt) once that Short is live. Never unticked.
"""
import csv, datetime, glob, json, os, re, sys
from zoneinfo import ZoneInfo

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RN = os.path.join(ROOT, "Research Notes")
CACHE = os.path.join(ROOT, ".hub_cache")
ET = ZoneInfo("America/New_York")
URL = {"nba": "https://claude.ai/artifact/EZrk8n855PyYpMFnMnMJd4", "fc": "https://claude.ai/artifact/LFsQtwomdpLAshoz4Xw62H",
       "tasks": "https://claude.ai/artifact/Ki1UXnbxsdykE4dy7BwyLT"}
sys.path.insert(0, HERE)


def norm(t):
    return " ".join(re.findall(r"[a-z0-9']+", re.sub(r"#\w+", "", (t or "").lower())))


def toks(t):
    return {w for w in norm(t).split() if len(w) > 2 and w not in {"the", "and", "who", "his", "her", "for", "with", "that", "this", "just", "has", "had"}}


def versions(kind):
    p = os.path.join(CACHE, kind, "versions.txt")
    v = {}
    if os.path.exists(p):
        t = open(p, encoding="utf-8").read()
        for m in re.finditer(r'"([\w.~:@+-]+)"\s+\d+\s+bytes\s+version\s+(\d+)', t):
            v[m.group(1)] = int(m.group(2))
        for m in re.finditer(r'"([\w.~:@+-]+)"\s+(\d+)(?=[,\]])', t):
            v.setdefault(m.group(1), int(m.group(2)))
    return v


def docs(kind, coll):
    out = {}
    for f in glob.glob(os.path.join(CACHE, kind, coll, "*.json")):
        out[os.path.basename(f)[:-5]] = json.load(open(f, encoding="utf-8"))
    return out


def live_videos():
    """{video_id: row} from the lab's table (API numbers) + go-live times from Scheduled Uploads.csv."""
    p = os.path.join(RN, "Lab", "shorts.csv")
    rows = {r["video_id"]: r for r in csv.DictReader(open(p, encoding="utf-8"))} if os.path.exists(p) else {}
    return rows


def match_vid(d, rows, ch):
    if d.get("ytId") and d["ytId"] in rows:
        return d["ytId"]
    names = [d.get("title") or ""] + list(d.get("titles") or [])[:3] + [d.get("name") or ""]
    best = (0, None)
    for vid, r in rows.items():
        if r["channel"] != ch:
            continue
        for n in names:
            if n and norm(n) == norm(r["title"]):
                return vid
            a, b = toks(n), toks(r["title"])
            if a and b and len(a & b) >= 3:
                j = len(a & b) / len(a | b)
                if j > best[0]:
                    best = (j, vid)
    return best[1] if best[0] >= 0.6 else None


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def hub_writes(ch, rows, queue, booked, today):
    D = docs(ch, "shorts")
    V = versions(ch)
    writes, notes = [], []
    for doc_id, d in D.items():
        st = str(d.get("status") or "").lower()
        if st.startswith(("reject", "abandon", "hold", "block", "skip")):
            continue
        vid = match_vid(d, rows, ch)
        r = rows.get(vid) if vid else None
        upd = {}
        live = r is not None and r.get("date") and r["date"] <= today.isoformat() and (num(r.get("views_now")) or 0) > 0
        if live:
            views, avg, eng = num(r.get("views_now")), num(r.get("avg_pct")), num(r.get("engaged"))
            old = d.get("results") or {}
            auto_note = not old.get("note") or bool(re.match(r"(auto|views|public count|api|rss)", str(old.get("note")), re.I))
            res = dict(old)
            res["views"] = int(views)
            if avg is not None:
                res["avgPct"] = round(avg, 1)
            stayed = num(r.get("stayed"))
            if old.get("viewedPct") is None and (stayed is not None or eng is not None):  # never overwrite a real stayed % already on the card
                res["viewedPct"] = round(stayed, 1) if stayed is not None else round(eng * 100)
            res["when"] = old.get("when") or r["date"]
            if auto_note:
                v72 = num(r.get("views")) if r.get("metric_src") == "72h" else None
                res["note"] = f"auto {today:%b %d}" + (f", 72 h: {int(v72):,}" if v72 else "")
            if (old.get("views") or 0) == 0 or abs(res["views"] - (old.get("views") or 0)) / max(1, old.get("views") or 1) >= 0.03 or set(res) - set(old):
                upd["results"] = res
            if not st.startswith("posted"):
                upd["status"] = "posted"
            if not d.get("ytId"):
                upd["ytId"] = vid
        elif st.startswith(("ready", "draft")):
            t = norm(d.get("title") or (d.get("titles") or [""])[0])
            bk = next((b for b in booked if b[0] == ch and (norm(b[2]) == t or len(toks(b[2]) & toks(t)) >= 3)), None)
            if bk and bk[1] <= datetime.datetime.now(ET):  # went live by schedule; the API numbers follow in about 2 days
                upd.update(status="posted", ytId=d.get("ytId") or bk[3],
                           results=dict(d.get("results") or {}, when=bk[1].date().isoformat(), note=f"auto: live since {bk[1]:%b %d %I:%M %p} ET, numbers in ~2 days"))
                bk = None
            q = next((s for s in queue if s["ch"] == ch and s.get("title") and (norm(s["title"]) == t or len(toks(s["title"]) & toks(t)) >= 3)), None)
            if bk:
                label = f"Scheduled on YouTube: {bk[1]:%a %b} {bk[1].day}, {int(bk[1].strftime('%I'))}:{bk[1]:%M %p} ET (goes live by itself)"
            elif q:
                s = datetime.datetime.fromisoformat(q["slot"])
                label = f"Auto queue: {s:%a %b} {s.day}, {int(s.strftime('%I'))}:{s:%M %p} ET" + (f" · score {q['score']}" if q.get("score") is not None else "") + \
                        (f" · QA {q['qa']} {q.get('verdict') or ''}".rstrip() if q.get("qa") is not None else "")
            else:
                label = None
            if label and d.get("slotLabel") != label and "status" not in upd:
                upd["slotLabel"] = label
        if upd:
            w = dict(op="update", collection="shorts", doc_id=doc_id, data=upd)
            if doc_id in V:
                w["if_version"] = V[doc_id]
            writes.append(w)
            notes.append(f"{doc_id}: " + ", ".join(upd))
    # live Shorts with no card at all (posted outside the Hub, e.g. by the PC scheduler): add a posted card so the Published list is complete
    matched = {match_vid(d, rows, ch) for d in D.values()}
    for vid, r in rows.items():
        if r["channel"] != ch or vid in matched or not r.get("date") or r["date"] > today.isoformat() or (num(r.get("views_now")) or 0) <= 0:
            continue
        if r["date"] < "2026-10-15":
            continue  # the old era stays as it is
        nm = 0
        m = re.search(r"(?:^|/)\d{4}-\d{2}-\d{2}\s+S?(\d+)\b", r.get("folder") or "")
        if m:
            nm = int(m.group(1))
        data = dict(num=nm, name=r["title"], title=r["title"], status="posted", ytId=vid, versions=[], titles=[r["title"]],
                    postNote="Added by hub sync: posted without a Hub card (PC scheduler or by hand).",
                    results=dict(views=int(num(r["views_now"])), avgPct=round(num(r["avg_pct"]), 1) if num(r.get("avg_pct")) is not None else None,
                                 viewedPct=(round(num(r["stayed"]), 1) if num(r.get("stayed")) is not None else (round(num(r["engaged"]) * 100) if num(r.get("engaged")) is not None else None)),
                                 when=r["date"], note=f"auto {today:%b %d}"))
        writes.append(dict(op="set", collection="shorts", doc_id=f"yt-{vid}", data=data))
        notes.append(f"yt-{vid}: NEW posted card ({r['title'][:40]})")
    # UP NEXT cards in `ideas`
    I = docs(ch, "ideas")
    VI = versions(ch)
    upnext = [s for s in queue if s["ch"] == ch and s["kind"] in ("BUILD", "BUILD (filler)", "IDEA", "MOMENT", "EMPTY", "READY", "READY (filler)", "PINNED")]
    keep = set()
    for i, s in enumerate(upnext, 1):
        t = datetime.datetime.fromisoformat(s["slot"])
        did = f"q-{i}"
        keep.add(did)
        data = dict(rank=round(i / 100, 2), name=f"UP NEXT · {t:%a %b} {t.day}, {int(t.strftime('%I'))}:{t:%M %p} ET · {s['kind']}",
                    lane=f"{s['kind']}" + (f" · score {s['score']}" if s.get("score") is not None else ""),
                    title=s.get("title") or ("last night's best moment" if s["kind"] == "MOMENT" else "(open slot)"),
                    facts=(s.get("why") or "") + (" · Next: " + s["action"] if s.get("action") else ""), checked=s["kind"] in ("READY", "PINNED", "BUILD"),
                    footage="", hook="", pinned="")
        w = dict(op="set", collection="ideas", doc_id=did, data=data)
        if did in I and did in VI:
            w["if_version"] = VI[did]
        if did not in I or any(I[did].get(k) != v for k, v in data.items()):
            writes.append(w)
    for did in I:
        if did.startswith("q-") and did not in keep:
            w = dict(op="delete", collection="ideas", doc_id=did)
            if did in VI:
                w["if_version"] = VI[did]
            writes.append(w)
    return writes, notes


def task_writes(rows, today):
    D = docs("tasks", "tasks")
    V = versions("tasks")
    writes, notes = [], []
    for doc_id, d in D.items():
        if d.get("done") or d.get("section") != "post":
            continue
        title = next((c.get("text") for c in (d.get("copy") or []) if str(c.get("label", "")).lower().startswith("title")), "") or re.sub(r"^Post:\s*", "", d.get("title") or "")
        ch = "fc" if str(d.get("channel", "")).upper() == "FC" else "nba"
        vid = match_vid({"title": title}, rows, ch)
        r = rows.get(vid) if vid else None
        if r and r.get("date") and r["date"] <= today.isoformat() and (num(r.get("views_now")) or 0) > 0:
            w = dict(op="update", collection="tasks", doc_id=doc_id, data={"done": True, "doneAt": f"{r['date']}T12:00:00Z"})
            if doc_id in V:
                w["if_version"] = V[doc_id]
            writes.append(w)
            notes.append(f"{doc_id}: done (live, {int(num(r['views_now'])):,} views)")
    return writes, notes


def main():
    today = datetime.datetime.now(ET).date()
    rows = live_videos()
    qp = os.path.join(RN, "Lab", "queue.json")
    queue = json.load(open(qp, encoding="utf-8"))["slots"] if os.path.exists(qp) else []
    booked = []
    for r in csv.DictReader(open(os.path.join(RN, "Scheduled Uploads.csv"), encoding="utf-8")):
        if norm(r.get("title")) in ("", "unknown"):
            continue
        try:
            booked.append((r["channel"], datetime.datetime.strptime(r["publish_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET), r["title"], r["video_id"]))
        except (KeyError, ValueError):
            pass
    os.makedirs(os.path.join(CACHE, "out"), exist_ok=True)
    for kind in ("nba", "fc", "tasks"):
        if not os.path.isdir(os.path.join(CACHE, kind)):
            print(f"{kind}: no cache (list the artifact first)")
            continue
        w, n = (task_writes(rows, today) if kind == "tasks" else hub_writes(kind, rows, queue, booked, today))
        missing = [x["doc_id"] for x in w if x["op"] != "set" and "if_version" not in x] + \
                  [x["doc_id"] for x in w if x["op"] == "set" and x["doc_id"] in docs(kind, "ideas" if kind != "tasks" else "tasks") and "if_version" not in x]
        od = os.path.join(CACHE, "out", kind)
        os.makedirs(od, exist_ok=True)
        for f in glob.glob(os.path.join(od, "*.json")):
            os.remove(f)
        compact = []
        for x in w:  # data goes to one file per document, so the batch call only carries paths
            y = {k: v for k, v in x.items() if k != "data"}
            if "data" in x:
                fp = os.path.join(od, f"{x['collection']}__{x['doc_id']}.json")
                json.dump(x["data"], open(fp, "w", encoding="utf-8"), ensure_ascii=False)
                y["file_path"] = fp
            compact.append(y)
        json.dump(dict(url=URL[kind], writes=compact, missing_versions=missing), open(os.path.join(CACHE, "out", f"{kind}.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"{kind}: {len(w)} write(s) -> .hub_cache/out/{kind}.json" + (f"  (MISSING versions for {missing[:5]}: paste the listing into .hub_cache/{kind}/versions.txt)" if missing else ""))
        for x in n[:40]:
            print("   ", x)


if __name__ == "__main__":
    main()
