"""Does the export match the approved script and timeline? Run on the final render, after qa_short.py.

  python Tools/export_check.py "<Short folder>"                    # final.mp4
  python Tools/export_check.py "<Short folder>" --video final_F.mp4 --no-stt

Checks (Oct 15, 2026):
  CAPTIONS   the burned caption text (captions.ass) word for word against script.txt (case ignored). Any difference = FAIL:
             a caption the viewer reads must be the approved wording and spelling (names included).
  TIMING     every spoken word (words.json) is on screen while it is said (0.15 s grace); no caption shorter than 0.25 s;
             no two captions overlap.
  SAFE AREA  caption centre inside the house band (45-65% of the height: clear of the Shorts title/buttons at the bottom and
             the top bar), and the widest line under 820 px measured with the real font (centred, its right edge then stays left
             of x=950, where the like/comment column sits).
  AUDIO      the export's own speech, transcribed locally (faster-whisper small.en, free), against script.txt. Numbers are
             compared as "a number here" (digit vs word formatting is not an error). Missing/extra words = CHECK.
  TIMELINE   shots.json starts at 0, runs in order, no shot under 0.3 s; picture and sound run the same length (0.1 s);
             1080x1920; the last word ends before the video does.
  CLIPPING   runs of 3+ samples at full scale in voice.mp3 or the export's audio = FAIL (audible distortion).
Exit code 1 on any FAIL. It can't judge whether the picture matches the line; that's footage_qc.py plus the human check.
"""
import argparse, difflib, json, os, re, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
NUMW = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
           "eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion and point "
           "half quarter percent first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth "
           "fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth thirtieth fortieth fiftieth".split())


def shown(text):
    return re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", text)


def toks(text):
    # the recogniser writes "eight million dollars" as "$8 million": put "dollars" back where it is spoken
    text = re.sub(r"\$(\d[\d,.]*)(\s*(?:thousand|million|billion))?", lambda m: m.group(1) + (m.group(2) or "") + " dollars", text, flags=re.I)
    t = text.lower().replace("’", "'").replace("—", " ").replace("-", " ")
    return [re.sub(r"^(\d+)(st|nd|rd|th)$", r"\1", x) for x in re.findall(r"[a-z0-9']+(?:\.[0-9]+)?", t)]


def numfold(ts):
    """Collapse each run of number tokens to '#', so '198' == 'one ninety eight' (formatting is not an error)."""
    out = []
    for t in ts:
        ordinal = t in ("first", "second", "third") or (t.endswith("th") and t in NUMW)
        isnum = t[0].isdigit() or (t in NUMW and t not in ("and", "point", "half", "quarter", "percent") and not ordinal) \
            or (ordinal and out and out[-1] == "#")
        if isnum or (t in ("and", "point", "percent") and out and out[-1] == "#"):
            if not out or out[-1] != "#":
                out.append("#")
        else:
            out.append(t)
    return out


def diffs(a, b, label_a, label_b, limit=8):
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"{label_a} '{' '.join(a[i1:i2]) or '(nothing)'}' vs {label_b} '{' '.join(b[j1:j2]) or '(nothing)'}'")
    return out[:limit], len(out), sm.ratio()


def ass_events(path):
    ev = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("Dialogue:"):
            continue
        parts = line.rstrip("\n").split(",", 9)
        st, en, text = parts[1], parts[2], parts[9]
        sec = lambda x: int(x.split(":")[0]) * 3600 + int(x.split(":")[1]) * 60 + float(x.split(":")[2])
        pos = re.search(r"\\pos\((\d+),(\d+)\)", text)
        clean = re.sub(r"\{[^}]*\}", "", text).replace("\\N", " ")
        fx = re.findall(r"\\fscx([\d.]+)", text)  # the last one is the size the card settles at (after the pop)
        ev.append({"start": sec(st), "end": sec(en), "text": clean, "y": int(pos.group(2)) if pos else None,
                   "scale": float(fx[-1]) / 100 if fx else None})
    return ev


def ass_style(path):
    for line in open(path, encoding="utf-8"):
        if line.startswith("Style:"):
            f = line[6:].split(",")
            return {"font": f[1].strip(), "size": float(f[2]), "scale_x": float(f[11]) / 100, "align": int(f[18]), "margin_v": int(f[21])}
    return {}


def caption_width(ev, stl):
    """Rendered width in px of the widest caption: real font width x the card's final scale x 0.745 (libass draws an ASS font
    size smaller than PIL's em size). Calibrated Oct 15 on #36 v2's 'STARTED SEVENTY-FIVE': PIL 1115 px, burned 831 px at \\fscx100."""
    from PIL import ImageFont
    fp = os.path.join(HERE, "fonts", stl["font"].replace(" ", "-") + ".ttf")
    if not os.path.exists(fp):
        wide = max(ev, key=lambda e: len(e["text"]))["text"]
        return len(wide) * stl["size"] * 0.52 * stl["scale_x"], wide
    f = ImageFont.truetype(fp, int(stl["size"]))
    best = max(((lambda b: b[2] - b[0])(f.getbbox(e["text"])) * (e["scale"] or stl["scale_x"]) * 0.745, e["text"]) for e in ev)
    return best


def probe(path):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,duration,avg_frame_rate",
                                   "-of", "json", path], capture_output=True, text=True).stdout)
    return {s["codec_type"]: s for s in j["streams"]}


def pcm(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def clipped_runs(x, thr=0.999, run=3):
    hot = np.abs(x) >= thr
    n, c = 0, 0
    for h in hot:
        c = c + 1 if h else 0
        if c == run:
            n += 1
    return n, (20 * np.log10(np.abs(x).max() + 1e-12) if len(x) else -99)


def check(folder, video=None, stt=True):
    bad, warn, ok = [], [], []
    fin = video or os.path.join(folder, "final.mp4")
    script = open(os.path.join(folder, "script.txt"), encoding="utf-8-sig").read().strip()
    ref = toks(shown(script))
    words = json.load(open(os.path.join(folder, "words.json")))
    # CAPTIONS
    ass = os.path.join(folder, "captions.ass")
    if os.path.exists(ass):
        ev = ass_events(ass)
        cap = toks(" ".join(e["text"] for e in ev))
        d, n, _ = diffs(cap, ref, "caption", "script")
        (bad.append(f"captions differ from script.txt in {n} place(s): " + "; ".join(d)) if n else ok.append(f"captions match script.txt word for word ({len(cap)} words)"))
        short = [round(e["start"], 2) for e in ev if e["end"] - e["start"] < 0.25]
        if short:
            warn.append(f"captions on screen under 0.25 s at {short} s (too fast to read)")
        ov = [round(ev[i + 1]["start"], 2) for i in range(len(ev) - 1) if ev[i + 1]["start"] < ev[i]["end"] - 0.01]
        (bad.append(f"overlapping captions at {ov} s") if ov else ok.append("no overlapping captions"))
        miss = [w["word"] for w in words if not any(e["start"] - 0.15 <= w["start"] and w["end"] <= e["end"] + 0.15 for e in ev)]
        (warn.append(f"{len(miss)} spoken word(s) not on screen while said: {miss[:8]}") if miss else ok.append("every spoken word is captioned while it is said"))
        # SAFE AREA
        stl = ass_style(ass)
        ys = [e["y"] for e in ev if e["y"]]
        if ys:
            lo, hi = min(ys) / 1920, max(ys) / 1920
            (ok.append(f"captions centred at {lo:.0%}-{hi:.0%} of the height (house band 45-65%)") if 0.45 <= lo and hi <= 0.65
             else bad.append(f"captions at {lo:.0%}-{hi:.0%} of the height: outside the 45-65% safe band (Shorts UI covers the bottom ~20%)"))
        if stl:
            est, wide = caption_width(ev, stl)
            (warn.append(f"widest caption '{wide}' is about {est:.0f} px wide; over 820 px its right edge passes x=950, where the Shorts like/comment column sits") if est > 820
             else ok.append(f"widest caption about {est:.0f} px (under 820: clear of the right-hand buttons)"))
    else:
        warn.append("no captions.ass (captions not checked)")
    # TIMELINE
    shots = json.load(open(os.path.join(folder, "shots.json")))
    st = [s["start"] for s in shots]
    pr = probe(fin)
    v, a = pr.get("video", {}), pr.get("audio", {})
    vd, ad = float(v.get("duration", 0) or 0), float(a.get("duration", 0) or 0)
    (bad.append(f"shots.json does not start at 0 ({st[0]})") if st[0] > 0.01 else None)
    unordered = [i + 1 for i in range(len(st) - 1) if st[i + 1] <= st[i]]
    (bad.append(f"shots out of order at {unordered}") if unordered else None)
    tiny = [(shots[i]["clip"], round(st[i + 1] - st[i], 2)) for i in range(len(st) - 1) if st[i + 1] - st[i] < 0.3]
    (warn.append(f"shots under 0.3 s: {tiny}") if tiny else None)
    (bad.append(f"last shot starts at {st[-1]} s, after the video ends ({vd:.2f} s)") if st[-1] >= vd - 0.2 else None)
    if abs(vd - ad) > 0.1:
        bad.append(f"picture {vd:.2f} s and sound {ad:.2f} s differ by {abs(vd - ad):.2f} s")
    else:
        ok.append(f"picture and sound both {vd:.2f} s")
    if (v.get("width"), v.get("height")) != (1080, 1920):
        bad.append(f"export is {v.get('width')}x{v.get('height')}, not 1080x1920")
    if words[-1]["end"] > vd:
        bad.append(f"last word ends at {words[-1]['end']} s, after the video ({vd:.2f} s)")
    # CLIPPING
    for name, path in (("voice.mp3", os.path.join(folder, "voice.mp3")), ("export audio", fin)):
        if os.path.exists(path):
            n, pk = clipped_runs(pcm(path))
            (bad.append(f"{name}: {n} clipped run(s) at full scale (peak {pk:.1f} dBFS): redo the take or lower the gain") if n
             else ok.append(f"{name}: no clipping (peak {pk:.1f} dBFS)"))
    # AUDIO vs SCRIPT (local speech-to-text)
    if stt:
        try:
            from faster_whisper import WhisperModel
            wav = os.path.join("/tmp", f"_exp_{os.getpid()}.wav")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", fin, "-ac", "1", "-ar", "16000", wav], check=True)
            m = WhisperModel("small.en", device="cpu", compute_type="int8")
            segs, _ = m.transcribe(wav, beam_size=5, language="en")
            heard = " ".join(s.text for s in segs)
            os.remove(wav)
            d, n, r = diffs(numfold(toks(heard)), numfold(ref), "heard", "script")
            msg = f"the export says what the script says ({r:.0%} word match after number folding)"
            if n == 0:
                ok.append(msg)
            else:
                (warn if r >= 0.9 else bad).append(f"{msg}; {n} difference(s) to listen for (speech-to-text mishears names): " + "; ".join(d))
        except Exception as e:
            warn.append(f"speech-to-text check skipped: {e}")
    return bad, warn, ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder"); ap.add_argument("--video"); ap.add_argument("--no-stt", action="store_true")
    a = ap.parse_args()
    bad, warn, ok = check(a.folder, a.video, not a.no_stt)
    print("PASS" if not bad else "FAIL")
    for x in warn:
        print("  warn", x)
    for x in ok:
        print("  ok  ", x)
    for x in bad:
        print("  FIX ", x)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
