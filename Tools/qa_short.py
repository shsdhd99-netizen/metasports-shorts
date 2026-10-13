"""Quality gate. Run BEFORE delivering any Short. Exit code 1 = do not ship, fix the listed items.

  python qa_short.py --folder "<Short folder>"

Reads shots.json (each shot needs "kind": face|quote|action|card), words.json, final.mp4.
Rules (from the retention research; each has burned a Short before):
  HOOK   first word on screen/spoken by 0.4 s; the first spoken word is not filler; >=3 different shots in the first 3 s;
         >=1 'action' shot (real footage of the story) in the first 3 s; the hook has a number/name/stakes.
  PACE   no shot longer than 3.0 s (quotes 4.0 s); average shot <= 1.9 s.
  VISUAL <=35% of runtime on any single source clip; >=6 distinct source clips; <=45% of runtime talking head ('face'+'quote');
         >=35% 'action' (b-roll that shows the story); cards <=25%; no 2 identical neighbours (same clip + same in-point).
  AUDIO  loudness -14 +-1.5 LUFS; no silence over 0.6 s inside the voice.
  LENGTH 18-35 s. Last shot repeats the first clip (loop).
  PICTURE (Oct 13, from commentary-edit qa_final.py) no frozen footage over 0.6 s outside still cards; no black frames; true peak <= -1 dBTP (warn).
  CLIPS  (Oct 13 2026) no shot longer than what is left of its clip: assemble.py before Oct 13 LOOPED the clip (visible
         jump-back; found in 22 of 27 folders). Since then it slows small gaps (<=1.33x) and holds the last frame on big ones;
         a hold over 0.5 s fails (frozen picture). Renders made after the fix write _render.json.
  OPENING (warn only, HYPOTHESIS n=14) a card/screenshot in the first 4 s: the 4 most-viewed Oct posts had none before 7 s.
"""
import argparse, json, os, re, subprocess, sys

FILLER = {"so", "look", "that's", "thats", "mate", "um", "uh", "well", "okay", "hey", "today", "welcome"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--video", help="video to test (default final.mp4)")
    ap.add_argument("--infer-kinds", action="store_true", help="old Shorts: cards by clip name, everything else counts as action")
    a = ap.parse_args()
    F = a.folder
    shots = json.load(open(os.path.join(F, "shots.json")))
    words = json.load(open(os.path.join(F, "words.json")))
    fin = a.video or os.path.join(F, "final.mp4")
    if a.infer_kinds:
        for x in shots:
            x.setdefault("kind", "card" if re.match(r"c\d", x["clip"]) else "action")
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", fin], capture_output=True, text=True).stdout)
    bad, ok, warn = [], [], []

    def chk(cond, good, msg):
        (ok if cond else bad).append(good if cond else msg)

    segs = []
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        segs.append((s, s["start"], end, end - s["start"]))
    kinds = {k: sum(d for s, _, _, d in segs if s.get("kind") == k) for k in ("face", "quote", "action", "card")}
    missing = [s["clip"] for s in shots if "kind" not in s]
    chk(not missing, "every shot has a kind", f"shots missing 'kind': {missing[:3]}")
    chk(21 <= total <= 45, f"length {total:.1f}s", f"length {total:.1f}s (want 21-45; Clank 21 s+ stories beat <=20 s, 848K vs 291K)")
    first = words[0]
    chk(first["start"] <= 0.4, "voice starts at once", f"first word at {first['start']}s (want <=0.4)")
    fw = re.sub(r"[^a-z']", "", first["word"].lower())
    chk(fw not in FILLER, f"opens on '{first['word']}'", f"opens on filler word '{first['word']}' (start on the name/number/stakes)")
    in3 = [s for s, st, e, d in segs if st < 3.0]
    chk(len(in3) >= 3, f"{len(in3)} shots in first 3 s", f"only {len(in3)} shots in first 3 s (want >=3)")
    chk(any(s.get("kind") == "action" for s in in3), "real action footage in first 3 s", "no 'action' footage in the first 3 s (a talking head or card hook gets swiped)")
    hook = " ".join(w["word"] for w in words if w["start"] < 3.0)
    chk(bool(re.search(r"\d|[A-Z][a-z]+ [A-Z]|million|billion|percent|first|never|only|banned|illegal|rule|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)\b", hook, re.I)) , "hook line has a name/number/stakes", f"hook line weak: '{hook}'")
    long_ = [(s["clip"], round(d, 1)) for s, _, _, d in segs if d > (4.5 if s.get("kind") == "quote" else 3.6)]
    chk(not long_, "no shot too long", f"shots too long: {long_}")
    avg = total / len(segs)
    chk(avg <= 2.6, f"average shot {avg:.1f}s", f"average shot {avg:.1f}s (want <=2.6)")
    by = {}
    for s, _, _, d in segs:
        by[s["clip"]] = by.get(s["clip"], 0) + d
    top = max(by.items(), key=lambda x: x[1])
    chk(top[1] / total <= 0.35, f"most-used clip {top[0]} {top[1]/total:.0%}", f"{top[0]} fills {top[1]/total:.0%} of the video (want <=35%): add more footage")
    chk(len(by) >= 6, f"{len(by)} source clips", f"only {len(by)} source clips (want >=6)")
    face = (kinds["face"] + kinds["quote"]) / total
    chk(face <= 0.45, f"talking head {face:.0%}", f"talking head {face:.0%} of runtime (want <=45%): add story b-roll")
    chk(kinds["action"] / total >= 0.35, f"b-roll {kinds['action']/total:.0%}", f"b-roll only {kinds['action']/total:.0%} (want >=35%)")
    chk(kinds["card"] / total <= 0.25, f"cards {kinds['card']/total:.0%}", f"cards {kinds['card']/total:.0%} (want <=25%)")
    dup = [i for i in range(1, len(shots)) if shots[i]["clip"] == shots[i - 1]["clip"] and shots[i].get("in") == shots[i - 1].get("in")]
    chk(not dup, "no repeated neighbours", f"identical neighbouring shots at {dup}")
    chk(shots[-1]["clip"] == shots[0]["clip"], "loops to the first shot", "last shot should reuse the first clip so it loops")
    r = subprocess.run(["ffmpeg", "-nostats", "-i", fin, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r)
    if m:
        lu = float(m[-1])
        chk(abs(lu + 14) <= 1.5, f"loudness {lu} LUFS", f"loudness {lu} LUFS (want -14)")
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)
    # Oct 13 2026, ported from Tools/commentary-edit/tools/qa_final.py: true peak, frozen picture, black frames
    if tp and float(tp[-1]) > -1.0:
        warn.append(f"true peak {tp[-1]} dBTP (want <= -1.0; lossy re-encodes can clip above it; renders since Oct 13 limit at -2 dBFS)")
    v = subprocess.run(["ffmpeg", "-nostats", "-i", fin, "-vf", "freezedetect=n=-60dB:d=0.6,blackdetect=d=0.2:pix_th=0.10", "-an", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    fr = [(float(a), float(b)) for a, b in re.findall(r"freeze_start: ([\d.]+).*?freeze_end: ([\d.]+)", v.replace("\n", " "))]
    still = [(st, e) for s, st, e, d in segs if s.get("kind") == "card" or s["clip"].lower().endswith((".png", ".jpg", ".jpeg"))]
    frozen = []
    for a0, b0 in fr:  # a held still card is fine; frozen FOOTAGE over 0.6 s is not
        overlap = sum(max(0.0, min(b0, e) - max(a0, st)) for st, e in still)
        if (b0 - a0) - overlap > 0.6:
            frozen.append((round(a0, 1), round(b0, 1)))
    chk(not frozen, "no frozen footage", f"picture frozen on footage at {frozen} s (dead frame: replace or split the shot)")
    blk = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", v)
    chk(not blk, "no black frames", f"black frames at {[(round(float(a), 1), round(float(b), 1)) for a, b in blk]} s")
    tail = total - words[-1]["end"]
    rinfo = os.path.join(F, "_render.json")
    rinfo = json.load(open(rinfo)) if os.path.exists(rinfo) else {}  # variants (e.g. final_pointer.mp4) are made from this render
    clipdur = {}
    short = []
    for s, st, e, d in segs:
        c = os.path.join(F, "clips", s["clip"])
        if not os.path.exists(c) or c.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        if c not in clipdur:
            clipdur[c] = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", c], capture_output=True, text=True).stdout or 0)
        gap = d - (clipdur[c] - float(s.get("in", 0) or 0))
        if gap > 0.08:
            short.append((s["clip"], round(st, 1), round(gap, 2)))
    if rinfo.get("loop_fix"):
        held = [f for f in rinfo.get("fits", []) if f.get("fit") == "held" and f.get("hold_s", 0) > 0.5]
        chk(not held, "no frozen holds", f"frozen last frame over 0.5 s (clip too short): {held}")
        if short:
            warn.append(f"clips shorter than their shots (slowed/held by assemble, not looped): {short}")
    else:
        chk(not short, "no clip replays", f"clip shorter than its shot = visible replay/jump-back (clip, at s, short by s): {short}; re-render with assemble.py (Oct 13+) or use longer clips")
    early_cards = [round(st, 1) for s, st, e, d in segs if s.get("kind") == "card" and st < 4.0]
    if early_cards:
        warn.append(f"card/screenshot in the first 4 s at {early_cards} s (HYPOTHESIS: the Oct posts that broke out had real footage/faces there)")
    if tail < 0.1:
        bad.append(f"voice is cut off: last word ends {tail:.2f}s before the end (add 0.3 s tail: ffmpeg -af apad=pad_dur=0.3)")
    first8 = " ".join(w["word"] for w in words[:8]).lower()
    if not re.search(r"\d|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred)\b|\b(but|never|banned|caught|first|only|wrong|illegal|fine|fined|suspended|record|why|how|what|did|is|will)\b", first8):
        warn.append(f"hook has no number or conflict/question word in the first 8 words: '{first8}' (state the question the viewer needs answered by 1.5 s)")
    tiny = [round(d, 2) for s, _, _, d in segs if d < 0.6]
    if tiny:
        warn.append(f"shots under 0.6 s read as noise: {tiny}")
    if not os.path.exists(os.path.join(F, "notes.md")):
        warn.append("no notes.md (needs Lane, Concept, Added value, claim -> exact source quote)")
    if avg < 1.3:
        warn.append(f"average shot {avg:.1f}s is very fast; a 1.9 vs 2.8 s A/B is pending (HYPOTHESIS)")
    dur_voice = words[-1]["end"] - words[0]["start"]
    wpm = len(words) / dur_voice * 60 if dur_voice else 0
    if not 240 <= wpm <= 290:
        warn.append(f"speech pace {wpm:.0f} wpm (Clank's biggest Shorts: 247-289)")
    if not 0.15 <= tail <= 0.6:
        warn.append(f"last word ends {tail:.2f}s before the end (loop tail wants 0.15-0.4 s)")
    last6 = " ".join(w["word"].lower() for w in words[-6:])
    if re.search(r"subscribe|follow|like|comment|thanks for watching|let me know", last6):
        warn.append("CTA in the last 6 words: end on the payoff instead")
    n = len(words)
    turn = [i for i, w in enumerate(words) if re.sub(r"[^a-z]", "", w["word"].lower()) in ("but", "however", "until", "except", "instead", "now")]
    if not turn or turn[0] > 0.4 * n:
        warn.append("no turn word (But/However/Until/Now) in the first 40% of the script")
    up = os.path.join(F, "UPLOAD.md")
    if os.path.exists(up):
        m = re.search(r"\*\*(.+?)\*\*", open(up, encoding="utf-8").read().split("## Title")[-1])
        if m and re.match(r"^[A-Z][a-z]+ [A-Z]", m.group(1)):
            warn.append(f"title starts with a name ('{m.group(1)[:30]}'): Clank's name-first titles got half the views (n=20), test action-first")
    print("PASS" if not bad else "FAIL")
    for x in warn:
        print("  warn", x)
    for x in ok:
        print("  ok  ", x)
    for x in bad:
        print("  FIX ", x)
    sys.exit(1 if bad else 0)


main()
