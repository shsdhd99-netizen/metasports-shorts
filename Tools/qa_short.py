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
Oct 14 2026 (Research Notes/Rules Audit): rules without support in our own data were DEMOTED from FAIL to warn: >=3 shots in the
first 3 s, average shot <=2.6 s, talking head <=45%, b-roll >=35%, cards <=25%, last shot = first clip, and the 21 s length floor
(old era: Shorts under 18 s had the BEST median, 32.8K, n=9). Removed: "turn word in first 40%" and "title starts with a name"
(no effect in our data). Added: dead air over 0.6 s inside the speech = FAIL (the rule above was documented but never checked);
slow hook (first sentence ends after 3.5 s) and naked-number opening (warn). Hard length limits are now 12-60 s (warn under 15 / over 35).
"""
import argparse, csv, json, os, re, subprocess, sys

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

    def soft(cond, good, msg):  # Oct 14: a guideline, not a gate (Rules Audit B2-B5, B7, A8)
        (ok if cond else warn).append(good if cond else msg)

    segs = []
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        segs.append((s, s["start"], end, end - s["start"]))
    kinds = {k: sum(d for s, _, _, d in segs if s.get("kind") == k) for k in ("face", "quote", "action", "card")}
    missing = [s["clip"] for s in shots if "kind" not in s]
    chk(not missing, "every shot has a kind", f"shots missing 'kind': {missing[:3]}")
    chk(12 <= total <= 60, f"length {total:.1f}s", f"length {total:.1f}s (outside 12-60 s)")
    soft(15 <= total <= 35, f"length {total:.1f}s in 15-35", f"length {total:.1f}s (length follows the story; our old era had no length effect, 10-33 s)")
    first = words[0]
    chk(first["start"] <= 0.4, "voice starts at once", f"first word at {first['start']}s (want <=0.4)")
    fw = re.sub(r"[^a-z']", "", first["word"].lower())
    chk(fw not in FILLER, f"opens on '{first['word']}'", f"opens on filler word '{first['word']}' (start on the name/number/stakes)")
    in3 = [s for s, st, e, d in segs if st < 3.0]
    soft(len(in3) >= 3, f"{len(in3)} shots in first 3 s", f"only {len(in3)} shots in first 3 s (guideline 3; shot length did not separate winners)")
    chk(any(s.get("kind") == "action" for s in in3), "real action footage in first 3 s", "no 'action' footage in the first 3 s (a talking head or card hook gets swiped)")
    hook = " ".join(w["word"] for w in words if w["start"] < 3.0)
    chk(bool(re.search(r"\d|[A-Z][a-z]+ [A-Z]|million|billion|percent|first|never|only|banned|illegal|rule|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)\b", hook, re.I)) , "hook line has a name/number/stakes", f"hook line weak: '{hook}'")
    long_ = [(s["clip"], round(d, 1)) for s, _, _, d in segs if d > (4.5 if s.get("kind") == "quote" else 3.6)]
    chk(not long_, "no shot too long", f"shots too long: {long_}")
    avg = total / len(segs)
    soft(avg <= 2.6, f"average shot {avg:.1f}s", f"average shot {avg:.1f}s (guideline <=2.6)")
    by = {}
    for s, _, _, d in segs:
        by[s["clip"]] = by.get(s["clip"], 0) + d
    top = max(by.items(), key=lambda x: x[1])
    chk(top[1] / total <= 0.35, f"most-used clip {top[0]} {top[1]/total:.0%}", f"{top[0]} fills {top[1]/total:.0%} of the video (want <=35%): add more footage")
    chk(len(by) >= 6, f"{len(by)} source clips", f"only {len(by)} source clips (want >=6)")
    face = (kinds["face"] + kinds["quote"]) / total
    soft(face <= 0.45, f"talking head {face:.0%}", f"talking head {face:.0%} of runtime (guideline <=45%): is every claim proven on screen?")
    soft(kinds["action"] / total >= 0.35, f"b-roll {kinds['action']/total:.0%}", f"b-roll {kinds['action']/total:.0%} (guideline >=35%)")
    soft(kinds["card"] / total <= 0.25, f"cards {kinds['card']/total:.0%}", f"cards {kinds['card']/total:.0%} (guideline <=25%)")
    two_cards = [i for i in range(1, len(shots)) if shots[i].get("kind") == "card" and shots[i - 1].get("kind") == "card"]
    soft(not two_cards, "no two cards in a row", f"two cards in a row at shots {two_cards} (the critic flags back-to-back reading)")
    dup = [i for i in range(1, len(shots)) if shots[i]["clip"] == shots[i - 1]["clip"] and shots[i].get("in") == shots[i - 1].get("in")]
    chk(not dup, "no repeated neighbours", f"identical neighbouring shots at {dup}")
    # Oct 14 (critic): the same footage shown twice ANYWHERE reads as a replay (#21 and #30 had 3 the check above missed).
    # Overlap of clip time used by two shots; the last shot re-using the first clip (the loop) is allowed; mark intentional replays "replay": true.
    used, replays = {}, []
    for k, (s, st, e, d) in enumerate(segs):
        if s.get("kind") == "card" or s.get("replay") or (k == len(segs) - 1 and s["clip"] == shots[0]["clip"]):
            continue
        a0 = float(s.get("in", 0) or 0); a1 = a0 + d
        for (b0, b1, j) in used.get(s["clip"], []):
            ov = min(a1, b1) - max(a0, b0)
            if ov > 0.3:
                replays.append((s["clip"], j + 1, k + 1, round(ov, 2)))
        used.setdefault(s["clip"], []).append((a0, a1, k))
    soft(not replays, "no footage shown twice", f"the same footage appears twice (clip, shot, shot, overlap s): {replays}; mark an intentional replay with \"replay\": true")
    soft(shots[-1]["clip"] == shots[0]["clip"], "loops to the first shot", "last shot is not the first clip (fine if the ending image serves the payoff; never add a sub-0.6 s shot just to loop)")
    gaps = [(round(words[i]["end"], 2), round(words[i + 1]["start"] - words[i]["end"], 2)) for i in range(len(words) - 1) if words[i + 1]["start"] - words[i]["end"] > 0.6]
    chk(not gaps, "no dead air inside the speech", f"dead air over 0.6 s inside the speech at (s, gap): {gaps}")
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
    stem = os.path.splitext(os.path.basename(fin))[0]
    logs = [os.path.join(F, f"_render_{x}.json") for x in (stem, stem.replace("_pointer", ""))] + [os.path.join(F, "_render.json")]
    rinfo = next((x for x in logs if os.path.exists(x)), None)  # final.mp4 -> _render.json; other renders -> _render_<name>.json
    rinfo = json.load(open(rinfo)) if rinfo else {}  # variants (e.g. final_pointer.mp4) are made from their base render
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
    # Oct 14 (critic on #38): a quote shot that was slowed/held drifts out of lip sync with the real audio
    quote_fits = [f for f in rinfo.get("fits", []) if f.get("shot") and 0 < f["shot"] <= len(shots)
                  and shots[f["shot"] - 1].get("kind") == "quote" and f.get("fit") in ("slowed", "held")]
    chk(not quote_fits, "quote shots play at normal speed (lip sync)",
        f"quote shot slowed/held, so the lips drift from the real audio: {quote_fits}; re-cut the quote clip to cover the whole shot at 1.0x")
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
    if not re.search(r"\d|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred)\b|\b(but|never|banned|caught|first|only|wrong|illegal|fine|fined|suspended|record|why|how|what|did|is|will|doesn't|isn't|not|no|taller|zero|count|counts)\b", first8):
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
    if not 200 <= wpm <= 265:  # Oct 14 night: our old hits' own voice recordings measured 206-252 wpm (median 220; audit section 11); new-era posts 224-250. Display words: digits count as one word, so number-heavy scripts read low
        warn.append(f"speech pace {wpm:.0f} wpm (guideline 200-265: our old hits ran 206-252, Clank's 265-309; don't drag, don't rush. Digits count as one word here)")
    if not 0.15 <= tail <= 0.6:
        warn.append(f"last word ends {tail:.2f}s before the end (loop tail wants 0.15-0.4 s)")
    last6 = " ".join(w["word"].lower() for w in words[-6:])
    if re.search(r"subscribe|follow|like|comment|thanks for watching|let me know", last6):
        warn.append("CTA in the last 6 words: end on the payoff instead")
    # Oct 14: the hook must be understood fast (Posted Video Audit: #13's 6.1 s hook and #20's "Ninety-two point nine." flopped)
    end1 = next((w["end"] for w in words if w["word"].rstrip("\"')")[-1:] in ".?!"), None)
    if end1 and end1 > 3.5:
        warn.append(f"slow hook: the first sentence ends at {end1:.1f} s (aim for the question to be clear by about 3 s; one fact, no compound sentence)")
    s1 = []
    for w in words:
        s1.append(w["word"])
        if w["word"].rstrip("\"')")[-1:] in ".?!":
            break
    if len(s1) <= 4 and re.match(r"^(\d|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)", s1[0].lower()):
        warn.append(f"naked-number opening: '{' '.join(s1)}' (a number with no subject means nothing at second 1; #20 got 1.6K)")
    # Oct 14 night (owner): NO generic background bed by default. Clean narration, effects where the picture makes the sound,
    # and a real song only through the platform's own music library (added by the owner in the app). If a bed IS baked in,
    # check it is logged, licensed and leaves the speech band clear.
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mus = rinfo.get("music")
    if mus:
        warn.append("a background bed is baked in: the house default is none since Oct 14 night (Library/Sound Library.md); say why in PACKAGE.md")
        lib = os.path.join(ROOT, "Library", "Music", "music_library.csv")
        rows = {r["file"]: r for r in csv.DictReader(open(lib, encoding="utf-8"))} if os.path.exists(lib) else {}
        key = os.path.relpath(os.path.join(ROOT, mus["track"]), os.path.dirname(lib)).replace("\\", "/")
        row = rows.get(key)
        chk(row is not None, f"music licence logged ({key})", f"music track {mus['track']} is not in Library/Music/music_library.csv: log source + licence before use")
        if row:
            st_ = row.get("status", "").lower()
            chk("rejected" not in st_ and "unclear" not in st_, f"music licence status: {row.get('status')}", f"music licence not cleared: {row.get('status')}")
            if "candidate" in st_:
                warn.append(f"music track '{row.get('title')}' is a candidate the owner has not approved by ear")
        if mus.get("bed_lu") is not None:
            soft(-24 <= mus["bed_lu"] <= -16, f"music bed {mus['bed_lu']} LU under the voice", f"music bed {mus['bed_lu']} LU under the voice (house range -24 to -16)")
        # speech-band clarity: voice vs the music stem (worst case: no ducking), 1-4 kHz, over the speech
        try:
            import numpy as np
            def pcm(cmd):
                return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32)
            t_in, t_out = float(mus.get("in", 0)), float(mus.get("out", total))
            m_ = pcm(["ffmpeg", "-v", "error", "-ss", str(mus["track_start"]), "-t", f"{t_out - t_in:.2f}", "-i", os.path.join(ROOT, mus["track"]),
                      "-af", f"volume={mus['gain_db']}dB", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"])
            vfile = os.path.join(F, "voice.mp3")
            vl = re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", vfile, "-af", "ebur128", "-f", "null", "-"],
                                                                     capture_output=True, text=True).stderr)
            v_ = pcm(["ffmpeg", "-v", "error", "-i", vfile, "-af", f"volume={-14 - float(vl[-1]):.2f}dB", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"])
            a0, b0 = int((max(words[0]["start"], t_in)) * 16000), int(min(words[-1]["end"], t_out) * 16000)
            mm = m_[max(0, a0 - int(t_in * 16000)):max(0, b0 - int(t_in * 16000))]
            vv = v_[a0:a0 + len(mm)]
            def band(x):
                X = np.abs(np.fft.rfft(x)) ** 2; f_ = np.fft.rfftfreq(len(x), 1 / 16000)
                return X[(f_ > 1000) & (f_ < 4000)].sum() + 1e-12
            snr = 10 * np.log10(band(vv) / band(mm)) if len(mm) > 16000 else 99
            chk(snr >= 12, f"speech band clear of music: {snr:.0f} dB (1-4 kHz, before ducking)", f"music crowds the voice: speech-band margin {snr:.0f} dB (want >= 18, fail < 12): lower bed_lu or pick a sparser track")
            if 12 <= snr < 18:
                warn.append(f"speech-band margin only {snr:.0f} dB: consider bed_lu 3 dB lower")
        except Exception as e:
            warn.append(f"could not measure the music margin: {e}")
    # Oct 14 (owner): every clip used needs a source-log row (Library/B-roll Sourcing Guide.md)
    src = os.path.join(F, "sources.csv")
    used = sorted({s["clip"] for s in shots})
    if not os.path.exists(src):
        warn.append("no sources.csv (source log: clip, url, timestamp, what it shows, verified): required for new builds")
    else:
        logged = {r.get("clip", "").strip(): r for r in csv.DictReader(open(src, encoding="utf-8-sig"))}
        miss = [c for c in used if c not in logged]
        chk(not miss, "every clip has a source-log row", f"clips missing from sources.csv: {miss}")
        unv = [c for c in used if c in logged and not str(logged[c].get("verified", "")).strip().lower().startswith(("y", "true", "1"))]
        chk(not unv, "every clip verified against the narration", f"clips not verified (watch them: player, uniform, scorebug, date match the line): {unv}")
    print("PASS" if not bad else "FAIL")
    for x in warn:
        print("  warn", x)
    for x in ok:
        print("  ok  ", x)
    for x in bad:
        print("  FIX ", x)
    sys.exit(1 if bad else 0)


main()
