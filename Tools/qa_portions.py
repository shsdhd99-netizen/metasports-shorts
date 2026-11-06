"""QA by portion (Nov 6, 2026; owner: "make QA better for each portion"). One table, one verdict per stage of a Short, so a problem is caught at the stage that causes it.

  python Tools/qa_portions.py --folder "<Short folder>" [--video <mp4>] [--channel nba|fc] [--video-id <youtube id>]

Portions: SCRIPT (words, line 1, claim words vs sources, lint risks) | VOICE (pace, tail, gaps, take gate) | FOOTAGE (sources verified, files exist, resolution,
precut_lint) | EDIT (shot rhythm, reuse, frame 1) | AUDIO (loudness, true peak, silence; needs --video) | PACKAGE (title, tags, pinned comment, slot, cover,
empty description) | LIVE (only with --video-id: title/tags/privacy/publish time as YouTube actually has them).
Each portion prints PASS, WARN or FAIL with the reason; exit code 1 if any FAIL. It reuses script_lint, precut_lint, edit_lint, yt_schedule.parse_card and ffmpeg,
so a fix to those tools improves this table. Add a check here when qa_audit.py shows a problem that fires late (QA Changelog.md).
"""
import argparse, csv, glob, json, os, re, subprocess, sys, urllib.parse

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "Tools")
sys.path.insert(0, TOOLS)
BAD_TITLES = {"", "unknown", "untitled", "none"}
CLAIM = re.compile(r"\b(still|record|first|never|only|most|every|ever|biggest|worst|best)\b", re.I)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr)


class P:
    def __init__(self, name):
        self.name, self.fails, self.warns, self.oks = name, [], [], []
    def fail(self, m): self.fails.append(m)
    def warn(self, m): self.warns.append(m)
    def ok(self, m): self.oks.append(m)
    @property
    def verdict(self): return "FAIL" if self.fails else ("WARN" if self.warns else "PASS")


def words_json(F):
    p = os.path.join(F, "words.json")
    if not os.path.exists(p):
        return []
    j = json.load(open(p, encoding="utf-8"))
    out = []
    for w in (j if isinstance(j, list) else j.get("words", [])):
        t = w.get("word") or w.get("w") or ""
        out.append((t, float(w.get("start", w.get("s", 0))), float(w.get("end", w.get("e", 0)))))
    return out


def script_portion(F, ch):
    p = P("SCRIPT")
    sp = os.path.join(F, "script.txt")
    if not os.path.exists(sp):
        p.fail("no script.txt"); return p
    txt = open(sp, encoding="utf-8-sig").read().strip()
    words = re.findall(r"[A-Za-z0-9'\u2019$%-]+", re.sub(r"\{[^}]*\|([^}]*)\}", "", txt))
    first = re.split(r"(?<=[.!?])\s", txt, 1)[0]
    n1 = len(re.findall(r"\S+", first))
    (p.ok if n1 <= 11 else p.warn)(f"line 1 has {n1} words (rule: 11 or fewer)")
    lo, hi = (45, 59) if ch == "fc" else (15, 33)
    est = len(words) / 3.75
    (p.ok if lo - 4 <= est <= hi + 4 else p.warn)(f"{len(words)} words, about {est:.0f} s at 225 wpm (target {lo}-{hi} s)")
    notes = os.path.join(F, "notes.md")
    if not os.path.exists(notes):
        p.fail("no notes.md (sources)")
    else:
        nt = open(notes, encoding="utf-8", errors="replace").read()
        urls = set(re.findall(r"https?://[^\s)|]+", nt))
        claims = set(m.group(1).lower() for m in CLAIM.finditer(txt))
        if len(urls) < 2:
            p.fail(f"notes.md has {len(urls)} source link(s); every Short needs at least 2 sources")
        elif claims and len(urls) < 3:
            p.warn(f"claim words {sorted(claims)} in the script but only {len(urls)} source links")
        else:
            p.ok(f"{len(urls)} source links in notes.md")
    rc, out = run([sys.executable, os.path.join(TOOLS, "script_lint.py"), sp])
    risks = [l.strip() for l in out.splitlines() if l.strip().startswith("RISK")]
    if len(risks) > 3:
        p.warn(f"{len(risks)} lint risks (first: {risks[0][5:90]})")
    return p


def voice_portion(F, ch):
    p = P("VOICE")
    v = os.path.join(F, "voice.mp3")
    if not os.path.exists(v):
        p.fail("no voice.mp3"); return p
    w = words_json(F)
    if not w:
        p.fail("no words.json"); return p
    rc, out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v])
    try:
        dur = float(out.strip().splitlines()[-1])
    except Exception:
        dur = w[-1][2]
    wpm = len(w) / max(1.0, w[-1][2] - w[0][1]) * 60
    lo, hi = (200, 255) if ch == "fc" else (205, 270)
    (p.ok if lo <= wpm <= hi else p.warn)(f"pace {wpm:.0f} wpm (range {lo}-{hi})")
    tail = dur - w[-1][2]
    (p.ok if 0.1 <= tail <= 0.5 else p.warn)(f"tail after the last word {tail:.2f} s (want 0.15-0.4)")
    gaps = [(w[i + 1][1] - w[i][2], w[i][0]) for i in range(len(w) - 1)]
    big = [g for g in gaps if g[0] > 0.6]
    (p.warn if big else p.ok)(f"{len(big)} pause(s) over 0.6 s" + (f" (longest {max(big)[0]:.2f} s after '{max(big)[1]}')" if big else ""))
    vt = os.path.join(F, "voice_take.json")
    if os.path.exists(vt):
        j = json.load(open(vt, encoding="utf-8"))
        last = j[-1] if isinstance(j, list) and j else {}
        if last.get("issues"):
            p.fail(f"voice check issues: {last['issues'][:2]}")
        elif last.get("verdict") not in (None, "PASS"):
            p.warn(f"voice take verdict {last.get('verdict')}")
        else:
            p.ok(f"take gate {last.get('verdict', 'n/a')} (HNR {last.get('hnr')})")
    return p


def footage_portion(F):
    p = P("FOOTAGE")
    cp = os.path.join(F, "cuts.json") if os.path.exists(os.path.join(F, "cuts.json")) else os.path.join(F, "cuts_plan.json")
    if not os.path.exists(cp):
        p.fail("no cuts.json / cuts_plan.json"); return p
    rc, out = run([sys.executable, os.path.join(TOOLS, "precut_lint.py"), "--folder", F])
    for l in out.splitlines():
        if l.strip().startswith("FIX"):
            p.fail(l.strip()[4:].strip()[:140])
        elif l.strip().startswith("warn"):
            p.warn(l.strip()[5:].strip()[:140])
    sc = os.path.join(F, "sources.csv")
    if not os.path.exists(sc):
        p.fail("no sources.csv")
    else:
        rows = list(csv.DictReader(open(sc, encoding="utf-8")))
        unv = [r["clip"] for r in rows if not str(r.get("verified", "")).lower().startswith(("y", "t", "1"))]
        nourl = [r["clip"] for r in rows if not (r.get("source_url") or "").startswith("http")]
        (p.fail if unv else p.ok)(f"{len(rows) - len(unv)}/{len(rows)} clips verified" + (f"; not verified: {unv[:4]}" if unv else ""))
        if nourl:
            p.warn(f"{len(nourl)} clip(s) with no source URL logged: {nourl[:4]}")
    miss = [s["clip"] for s in json.load(open(cp, encoding="utf-8"))["shots"] if not os.path.exists(os.path.join(F, "clips", s["clip"] + ".mp4"))]
    if miss:
        p.warn(f"{len(miss)} clip file(s) missing locally (re-cut before QA): {miss[:4]}")
    return p


def edit_portion(F, ch):
    p = P("EDIT")
    rc, out = run([sys.executable, os.path.join(TOOLS, "edit_lint.py"), "--folder", F])
    flags = [l.strip()[5:].strip() for l in out.splitlines() if l.strip().startswith("FLAG")]
    for f in flags:
        (p.warn)(f[:150])
    if not flags:
        p.ok("edit_lint clean")
    sj = os.path.join(F, "shots.json")
    if os.path.exists(sj):
        starts = [float(s.get("start", 0)) for s in json.load(open(sj, encoding="utf-8"))]
        if len(starts) > 1:
            first = starts[1] - starts[0]
            (p.ok if first >= 1.9 or ch == "fc" else p.warn)(f"shot 1 holds {first:.1f} s")
            short = sum(1 for i in range(len(starts) - 1) if starts[i + 1] - starts[i] < 0.6)
            (p.warn if short > 2 else p.ok)(f"{short} shot(s) under 0.6 s")
    return p


def audio_portion(video):
    p = P("AUDIO")
    if not video or not os.path.exists(video):
        p.warn("no --video given (audio not checked)"); return p
    rc, out = run(["ffmpeg", "-nostats", "-i", video, "-af", "ebur128=peak=true", "-f", "null", "-"])
    m = re.findall(r"I:\s+(-?\d+\.\d+) LUFS", out); tp = re.findall(r"Peak:\s+(-?\d+\.\d+) dBFS", out)
    if m:
        i = float(m[-1]); (p.ok if -15.5 <= i <= -12.5 else p.warn)(f"loudness {i:.1f} LUFS (target -14, +-1.5)")
    if tp:
        t = float(tp[-1]); (p.ok if t <= -1.0 else p.fail)(f"true peak {t:.1f} dBFS (must be under -1.0)")
    rc, out = run(["ffmpeg", "-nostats", "-i", video, "-af", "silencedetect=n=-45dB:d=0.5", "-f", "null", "-"])
    sil = re.findall(r"silence_start: ([\d.]+)", out)
    dur = re.findall(r"Duration: (\d+):(\d+):([\d.]+)", out)
    d = (int(dur[0][0]) * 3600 + int(dur[0][1]) * 60 + float(dur[0][2])) if dur else 0
    inner = [s for s in sil if 0.5 < float(s) < d - 1.0]
    (p.warn if inner else p.ok)(f"{len(inner)} silence(s) over 0.5 s inside the video")
    rc, out = run(["ffmpeg", "-v", "error", "-ss", "0", "-i", video, "-frames:v", "1", "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YAVG", "-f", "null", "-"])
    rc2, out2 = run(["ffmpeg", "-nostats", "-ss", "0", "-i", video, "-frames:v", "1", "-vf", "signalstats,metadata=print", "-f", "null", "-"])
    y = re.findall(r"YAVG=([\d.]+)", out + out2)
    if y:
        (p.ok if float(y[0]) > 25 else p.fail)(f"frame 1 brightness {float(y[0]):.0f} (dark frame 1 gets swiped)")
    return p


def package_portion(F):
    p = P("PACKAGE")
    card = os.path.join(F, "UPLOAD.md")
    if not os.path.exists(card):
        p.fail("no UPLOAD.md"); return p
    import yt_schedule as ys
    title, tags = ys.parse_card(card)
    t = open(card, encoding="utf-8-sig").read()
    if title.strip().lower() in BAD_TITLES:
        p.fail("title missing or a placeholder")
    elif len(title) > 100:
        p.fail(f"title is {len(title)} characters (limit 100)")
    elif re.search(r"\b[A-Z]{5,}\b", title):
        p.warn("title has an ALL-CAPS word")
    else:
        p.ok(f"title ok: {title[:60]}")
    n = len([x for x in tags.split(",") if x.strip()])
    ln = len(tags)
    if n < 10:
        p.fail(f"{n} tags parsed (need 15+)")
    elif ln > 490:
        p.fail(f"tags are {ln} characters (limit 490)")
    else:
        (p.ok if ln >= 380 else p.warn)(f"{n} tags, {ln} characters (fill the box to about 490)")
    (p.ok if re.search(r"pinned comment", t, re.I) else p.warn)("pinned comment " + ("present" if re.search(r"pinned comment", t, re.I) else "missing"))
    (p.ok if re.search(r"slot", t, re.I) else p.warn)("slot " + ("noted" if re.search(r"slot", t, re.I) else "not noted"))
    (p.ok if re.search(r"QA[^\n]{0,40}PASS|PASS[^\n]{0,40}QA", t) else p.fail)("QA PASS line " + ("present" if re.search(r"QA[^\n]{0,40}PASS|PASS[^\n]{0,40}QA", t) else "missing (the scheduler refuses a card without it)"))
    if not glob.glob(os.path.join(F, "cover*")) and not glob.glob(os.path.join(F, "_hub", "cover*")):
        p.warn("no cover image (cover.jpg)")
    if re.search(r"\*\*Description:\*\*\s*\S", t) and not re.search(r"\*\*Description:\*\*\s*(empty|none|-)", t, re.I):
        p.warn("description is not empty (rule: leave it empty)")
    return p


def live_portion(F, ch, vid):
    p = P("LIVE")
    if not vid:
        p.warn("no --video-id (not checked)"); return p
    import yt_analytics as Y, yt_schedule as ys
    if ch == "fc":
        Y.REFRESH_ENV = "YT_REFRESH_TOKEN_FC"; Y.TOKEN = Y.TOKEN.replace("yt_token.json", "yt_token_fc.json")
    at = Y.access_token()
    d = Y.get("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "snippet,status", "id": vid}), at).get("items", [])
    if not d:
        p.fail("video not found on the channel"); return p
    v = d[0]; title, tags = ys.parse_card(os.path.join(F, "UPLOAD.md"))
    (p.ok if v["snippet"]["title"].strip() == title.strip() else p.fail)(f"YouTube title {v['snippet']['title'][:50]!r}" + ("" if v["snippet"]["title"].strip() == title.strip() else f" != card {title[:50]!r}"))
    nt = len(v["snippet"].get("tags", []))
    (p.ok if nt >= 10 else p.fail)(f"{nt} tags on YouTube")
    p.ok(f"privacy {v['status']['privacyStatus']}" + (f", publishAt {v['status'].get('publishAt')}" if v["status"].get("publishAt") else ""))
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--video"); ap.add_argument("--channel", choices=["nba", "fc"]); ap.add_argument("--video-id")
    a = ap.parse_args()
    F = a.folder
    ch = a.channel or ("fc" if "Soccer Channel" in os.path.abspath(F) else "nba")
    if not a.video:
        c = sorted(glob.glob(os.path.join(F, "DRAFT*.mp4")))
        a.video = c[0] if c else (os.path.join(F, "final.mp4") if os.path.exists(os.path.join(F, "final.mp4")) else None)
    ps = [script_portion(F, ch), voice_portion(F, ch), footage_portion(F), edit_portion(F, ch), audio_portion(a.video), package_portion(F), live_portion(F, ch, a.video_id)]
    print(f"QA by portion: {os.path.basename(os.path.abspath(F))} ({ch})")
    for p in ps:
        print(f"  {p.verdict:4}  {p.name:8} " + "; ".join((p.fails + p.warns + p.oks)[:3])[:200])
        for m in p.fails:
            print(f"        FAIL {m}")
        for m in p.warns[:4]:
            print(f"        warn {m}")
    sys.exit(1 if any(p.fails for p in ps) else 0)


if __name__ == "__main__":
    main()
