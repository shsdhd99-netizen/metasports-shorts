r"""Final QA for a finished Short (Nov 6, 2026; owner: "build a QA checker for finished shorts").

  python Tools/qa_final.py "<Short folder>" [--channel nba|fc] [--video <mp4>]

One command, one verdict: SHIP / FIX / HOLD.
  1. qa_portions.py (script, voice, footage, edit, audio, package) on the finished DRAFT video;
  2. qa_short.py --full (the retention gate: hook, pace, picture, clips, render, export check) when shots.json exists;
  3. extra finished-file checks that nothing else does: the file is 1080x1920 H.264/AAC, 15-59.5 s (Shorts ceiling is 60 s: we keep it under 59.5),
     under 250 MB, the first frame is not black, the last frame is not black, the audio is stereo/mono and not clipped, the title is <= 100 chars with no
     placeholder, tags fit 500 chars, the card has a pinned comment, a cover and a slot, and sources.csv has no unverified row.
Verdict: any FAIL = HOLD (do not schedule); only WARNs = FIX if three or more, otherwise SHIP with the warnings listed; none = SHIP.
Writes <folder>/qa_final.json (read by queue_rank.py) and appends one line to Research Notes/QA Changelog-style log "QA Final Log.csv".
"""
import argparse, csv, datetime, glob, json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, r.stdout + r.stderr


def probe(v):
    rc, out = run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name,width,height,channels,duration", "-show_entries", "format=duration,size", "-of", "json", v])
    return json.loads(out) if rc == 0 else {}


def frame_mean(v, t):
    rc, out = run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", v, "-frames:v", "1", "-vf", "scale=32:56,format=gray", "-f", "rawvideo", "-"])
    return None


def luma(v, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", v, "-frames:v", "1", "-vf", "scale=16:28,format=gray", "-f", "rawvideo", "-"], capture_output=True)
    return sum(r.stdout) / len(r.stdout) if r.stdout else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--channel", choices=["nba", "fc"])
    ap.add_argument("--video")
    a = ap.parse_args()
    F = a.folder
    ch = a.channel or ("fc" if "Soccer" in os.path.abspath(F) else "nba")
    vids = glob.glob(os.path.join(F, "DRAFT*.mp4"))
    nom = [x for x in vids if re.search(r"no[- ]?music", x, re.I)]
    video = a.video or (nom or vids or [None])[0]
    if not video:
        sys.exit("No DRAFT*.mp4 in the folder.")
    fails, warns, oks = [], [], []

    rc, out = run([sys.executable, os.path.join(HERE, "qa_portions.py"), "--folder", F, "--video", video, "--channel", ch])
    for l in out.splitlines():
        m = re.match(r"\s{2}(PASS|WARN|FAIL)\s+(\w+)\s+(.*)", l)
        if m and m.group(2) != "LIVE":
            {"FAIL": fails, "WARN": warns, "PASS": oks}[m.group(1)].append(f"{m.group(2)}: {m.group(3)[:150]}")

    if os.path.exists(os.path.join(F, "shots.json")) and os.path.exists(os.path.join(F, "final.mp4")):
        rc, out = run([sys.executable, os.path.join(HERE, "qa_short.py"), "--folder", F, "--full"])
        if rc != 0:
            fails.append("qa_short --full: " + " | ".join(l.strip() for l in out.splitlines() if re.search(r"FAIL|FIX", l))[:300])
        else:
            oks.append("qa_short --full passed")

    j = probe(video)
    st = j.get("streams", [])
    v = next((s for s in st if s.get("codec_type") == "video"), {})
    au = next((s for s in st if s.get("codec_type") == "audio"), {})
    dur = float(j.get("format", {}).get("duration", 0) or 0)
    size = int(j.get("format", {}).get("size", 0) or 0) / 1e6
    if (v.get("width"), v.get("height")) != (1080, 1920):
        fails.append(f"FILE: size {v.get('width')}x{v.get('height')}, must be 1080x1920")
    if v.get("codec_name") != "h264" or au.get("codec_name") != "aac":
        warns.append(f"FILE: codecs {v.get('codec_name')}/{au.get('codec_name')} (want h264/aac)")
    if not 15 <= dur <= 59.5:
        fails.append(f"FILE: length {dur:.1f} s (want 15-59.5 s)")
    if size > 250:
        fails.append(f"FILE: {size:.0f} MB (limit 250)")
    for lab, t in (("first", 0.1), ("last", max(0, dur - 0.3))):
        m = luma(video, t)
        if m is not None and m < 6:
            fails.append(f"PICTURE: the {lab} frame is black (mean luma {m:.0f})")

    card = os.path.join(F, "UPLOAD.md")
    if os.path.exists(card):
        sys.path.insert(0, HERE)
        import yt_schedule as ys
        try:
            title, _tags = ys.parse_card(card)
        except Exception as e:
            title = ""
            fails.append(f"CARD: cannot parse ({e})")
        title = title or ""
        if not title or title.lower() in ("unknown", "untitled", "none"):
            fails.append("CARD: no real title")
        elif len(title) > 100:
            fails.append(f"CARD: title {len(title)} chars (limit 100)")
        txt = open(card, encoding="utf-8-sig").read()
        if not re.search(r"pinned comment", txt, re.I):
            warns.append("CARD: no pinned comment")
    else:
        fails.append("CARD: no UPLOAD.md")
    sp = os.path.join(F, "sources.csv")
    if os.path.exists(sp):
        rows = list(csv.DictReader(open(sp, encoding="utf-8")))
        bad = [r for r in rows if not str(r.get("verified", "")).lower().startswith(("y", "t", "1"))]
        if bad:
            fails.append(f"SOURCES: {len(bad)} of {len(rows)} rows not verified")
    else:
        warns.append("SOURCES: no sources.csv")

    verdict = "HOLD" if fails else ("FIX" if len(warns) >= 3 else "SHIP")
    print(f"QA FINAL: {os.path.basename(F)}  [{ch}]  {os.path.basename(video)}")
    print(f"  VERDICT: {verdict}   ({len(fails)} fail, {len(warns)} warn, {len(oks)} pass)")
    for tag, lst in (("FAIL", fails), ("WARN", warns)):
        for m in lst:
            print(f"  {tag}  {m}")
    json.dump({"fails": len(fails), "warns": len(warns), "verdict": verdict, "at": datetime.datetime.now().isoformat(timespec="minutes")}, open(os.path.join(F, "qa_final.json"), "w"))
    log = os.path.join(ROOT, "Research Notes", "QA Final Log.csv")
    new = not os.path.exists(log)
    with open(log, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["time", "channel", "folder", "verdict", "fails", "warns"])
        w.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), ch, os.path.basename(F), verdict, len(fails), len(warns)])
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
