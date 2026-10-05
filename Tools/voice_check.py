"""Is this voiceover good enough, or should it be generated again? Run it right after voiceover.py.

  python voice_check.py --folder "<Short folder>"          # checks voice.mp3 against script.txt
  python voice_check.py --folder "..." --no-stt            # timing/level checks only (no ElevenLabs call)

What it checks
  1. Every word was said, and said right: ElevenLabs speech-to-text hears the take back and compares it with the
     script (skipped, swapped or garbled words; names that came out wrong).
  2. Pace: rushed (> 320 words/min) or dragging (< 180 words/min) sentences.
  3. Odd pauses in the middle of a sentence, or dead air between sentences.
  4. Stretched or swallowed words (a word that takes far too long or far too short).
  5. Sudden loud or quiet words, clipping, and an ending that gets cut off.
Verdict: PASS, CHECK (listen to the flagged spots) or REDO (generate again; maybe respell a name with {Name|spelling}).
Writes voice_check.json next to the voice. Speech-to-text uses a few ElevenLabs credits (about 25 s of audio).
"""
import argparse, difflib, json, os, re, subprocess, sys, unicodedata, uuid, urllib.request, urllib.error
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voiceover import load_env, parse_script  # noqa: E402

API = "https://api.elevenlabs.io/v1/speech-to-text"
NUMS = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
        "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20",
        "thirty": "30", "forty": "40", "fifty": "50", "hundred": "100"}


def spoken_len(w):
    """Rough count of letters actually spoken: '$52 million' says 'fifty-two million dollars'."""
    letters = len(re.sub(r"[^A-Za-z]", "", w))
    return letters + 7 * w.count("$") + 7 * w.count("%") + 5 * len(re.sub(r"\D", "", w))


def norm_words(text):
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    text = text.lower().replace("’", "'").replace("—", " ").replace("–", " ").replace("-", " ")
    text = re.sub(r"\$(\d+(?:\.\d+)?)\s*m\b", r"\1 million", text)
    text = text.replace("%", " percent")
    toks = re.findall(r"[a-z0-9']+", text)
    return [NUMS.get(t, t).strip("'") for t in toks if t.strip("'")]


NUMWORDS = set(NUMS) | {"hundred", "thousand", "million", "billion", "sixty", "seventy", "eighty", "ninety", "dollars", "dollar", "percent", "point", "and", "oh"}


def numberish(toks):
    """True when every token is a digit string or a spelled-out number word ('one ninety eight' vs '198' is a formatting difference, not a glitch)."""
    return bool(toks) and all(t.isdigit() or t in NUMWORDS for t in toks)


def stt(path, key):
    boundary = uuid.uuid4().hex
    audio = open(path, "rb").read()
    body = b""
    for k, v in (("model_id", "scribe_v1"), ("language_code", "en"), ("timestamps_granularity", "word"),
                 ("tag_audio_events", "false")):
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"voice.mp3\"\r\n"
             "Content-Type: audio/mpeg\r\n\r\n").encode() + audio + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "xi-api-key": key, "Content-Type": f"multipart/form-data; boundary={boundary}"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"speech-to-text error {e.code}: {e.read().decode()[:300]}")


def stt_local(path, size="small"):
    """Free local speech-to-text (faster-whisper) in the same shape as the ElevenLabs scribe reply."""
    from faster_whisper import WhisperModel
    m = WhisperModel(size, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(path, language="en", word_timestamps=True, beam_size=5, temperature=0, vad_filter=True, condition_on_previous_text=False)
    words = [{"type": "word", "text": w.word.strip(), "start": w.start, "end": w.end} for s in segs for w in s.words]
    # Whisper sometimes invents a phrase over the silent tail ("Here's a look at the first half of this year"): words squeezed into < 0.03 s are not speech.
    words = [w for w in words if w["end"] - w["start"] >= 0.03]
    return {"text": " ".join(w["text"] for w in words), "words": words}


def pcm(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0, sr


def db(x):
    return 20 * np.log10(max(1e-9, float(np.sqrt(np.mean(np.square(x))))) if len(x) else -120)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--voice", default="voice.mp3")
    ap.add_argument("--no-stt", action="store_true")
    ap.add_argument("--stt", choices=["whisper", "scribe"], default="whisper",
                    help="whisper = free local faster-whisper (default, no credits); scribe = ElevenLabs speech-to-text (a few credits, better with names)")
    ap.add_argument("--json-out", default="voice_check.json")
    a = ap.parse_args()
    folder = os.path.abspath(a.folder)
    voice = os.path.join(folder, a.voice)
    words = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8-sig"))
    script_raw = open(os.path.join(folder, "script.txt"), encoding="utf-8-sig").read()
    segs = parse_script(script_raw)
    script_display = " ".join(d for d, _ in segs)
    respelled = {" ".join(norm_words(d)): " ".join(norm_words(sp)) for d, sp in segs if d != sp}
    issues, notes = [], []  # issues = serious, notes = minor

    # --- 1. said right? -------------------------------------------------------------------------------------
    heard_text, mismatches = None, []
    if not a.no_stt:
        key = load_env().get("ELEVENLABS_API_KEY", "") if a.stt == "scribe" else "local"
        if not key:
            notes.append("no ElevenLabs key, speech-to-text skipped")
        else:
            try:
                res = stt_local(voice) if a.stt == "whisper" else stt(voice, key)
                heard_text = res.get("text", "")
                hw = [w for w in res.get("words", []) if w.get("type") == "word"]
                want, got = norm_words(script_display), []
                got_t = []
                for w in hw:
                    for t in norm_words(w["text"]):
                        got.append(t)
                        got_t.append(w.get("start", 0))
                sm = difflib.SequenceMatcher(a=want, b=got, autojunk=False)
                for op, i1, i2, j1, j2 in sm.get_opcodes():
                    if op == "equal":
                        continue
                    exp, heard = " ".join(want[i1:i2]), " ".join(got[j1:j2])
                    close = difflib.SequenceMatcher(a=exp.replace(" ", ""), b=heard.replace(" ", "")).ratio()
                    if numberish(exp.split()) and numberish(heard.split()):
                        close = 1.0  # same number written differently
                    for d, sp in respelled.items():  # a name we respelled: compare with how it should sound too
                        if d and d in exp:
                            close = max(close, difflib.SequenceMatcher(a=sp.replace(" ", ""), b=heard.replace(" ", "")).ratio(), 0.72 if close > 0.45 else 0)
                    at = got_t[j1] if j1 < len(got_t) else (got_t[-1] if got_t else 0)
                    mismatches.append({"at": round(at, 2), "script": exp, "heard": heard, "similar": round(close, 2)})
                FUNC = {"the", "a", "an", "and", "in", "of", "to", "it", "is", "at", "on", "for", "point", "but", "so", "i", "he", "that", "as", "or", "uh"}
                for m in mismatches:  # the recogniser often drops tiny unstressed words; that is not a glitch
                    if not m["heard"] and m["script"] in FUNC:
                        m["similar"] = 1.0
                bad = [m for m in mismatches if m["similar"] < 0.72]
                soft = [m for m in mismatches if m["similar"] >= 0.72]
                miss_rate = sum(len(m["script"].split()) for m in bad) / max(1, len(want))
                for m in bad:
                    (issues if (len(m["script"].split()) >= 2 or not m["heard"] or miss_rate > 0.05) else notes).append(
                        f"{m['at']:5.2f}s  script \"{m['script']}\" but heard \"{m['heard'] or '(nothing)'}\"")
                for m in soft:
                    if numberish(m["script"].split()) and numberish(m["heard"].split()):
                        continue
                    notes.append(f"{m['at']:5.2f}s  \"{m['script']}\" heard as \"{m['heard']}\" (close; check the name)")
            except Exception as e:  # never block the pipeline on the checker itself
                notes.append(f"speech-to-text failed: {e}")

    # --- 2-4. pace, pauses, stretched words -----------------------------------------------------------------
    sentences, cur = [], []
    for w in words:
        cur.append(w)
        if w["word"].rstrip("\"')”’")[-1:] in ".?!…":
            sentences.append(cur)
            cur = []
    if cur:
        sentences.append(cur)
    total_words = len(words)
    span = words[-1]["end"] - words[0]["start"] if words else 1
    wpm = total_words / span * 60
    if wpm > 320:
        issues.append(f"whole take is rushed: {wpm:.0f} words/min (aim 240-290)")
    elif wpm < 200:
        notes.append(f"whole take is slow: {wpm:.0f} words/min (aim 240-290)")
    for s in sentences:
        if len(s) < 4:
            continue
        sp = s[-1]["end"] - s[0]["start"]
        r = len(s) / sp * 60 if sp > 0 else 0
        txt = " ".join(w["word"] for w in s)
        if r > 340:
            notes.append(f"{s[0]['start']:5.2f}s  rushed sentence ({r:.0f} wpm): {txt[:60]}")
        if r < 170:
            notes.append(f"{s[0]['start']:5.2f}s  dragging sentence ({r:.0f} wpm): {txt[:60]}")
    per_char = np.median([(w["end"] - w["start"]) / max(1, spoken_len(w["word"])) for w in words]) if words else 0.06
    for i in range(1, len(words)):
        gap = words[i]["start"] - words[i - 1]["end"]
        prev = words[i - 1]["word"]
        ends = prev.rstrip("\"')”’")[-1:] in ".?!…"
        soft = prev.rstrip("\"')”’")[-1:] in ",;:—–"
        if not ends and not soft and gap > 0.42:
            issues.append(f"{words[i - 1]['end']:5.2f}s  odd {gap:.2f}s pause mid-sentence after \"{prev}\"")
        elif ends and gap > 1.0:
            notes.append(f"{words[i - 1]['end']:5.2f}s  {gap:.2f}s of dead air after \"{prev}\"")
    for w in words:
        n = max(1, spoken_len(w["word"]))
        dur = w["end"] - w["start"]
        if dur > max(0.75, per_char * n * 3.2):
            issues.append(f"{w['start']:5.2f}s  stretched/garbled word \"{w['word']}\" ({dur:.2f}s)")
        elif n >= 6 and dur < per_char * n * 0.3:
            notes.append(f"{w['start']:5.2f}s  swallowed word \"{w['word']}\" ({dur:.2f}s)")

    # --- 5. levels ------------------------------------------------------------------------------------------
    x, sr = pcm(voice)
    peak = float(np.max(np.abs(x))) if len(x) else 0
    if peak >= 0.999:
        issues.append("clipping (the voice hits 0 dB) - regenerate or lower the volume")
    levels = []
    for w in words:
        seg = x[int(w["start"] * sr):int(w["end"] * sr)]
        if len(seg) > sr * 0.05:
            levels.append((db(seg), w))
    if levels:
        med = float(np.median([l for l, _ in levels]))
        for l, w in levels:
            if l < med - 11:
                notes.append(f"{w['start']:5.2f}s  very quiet word \"{w['word']}\" ({l - med:+.0f} dB)")
            elif l > med + 8:
                notes.append(f"{w['start']:5.2f}s  very loud word \"{w['word']}\" ({l - med:+.0f} dB)")
    file_len = len(x) / sr if len(x) else 0
    if words and file_len - words[-1]["end"] < 0.04 and db(x[-int(0.05 * sr):]) > -30:
        issues.append("the last word may be cut off (no silence at the end)")

    verdict = "REDO" if issues else ("CHECK" if len(notes) > 3 else "PASS")
    report = {"verdict": verdict, "wpm": round(wpm), "issues": issues, "notes": notes,
              "heard": heard_text, "mismatches": mismatches}
    json.dump(report, open(os.path.join(folder, a.json_out), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"Voice check: {verdict}   ({total_words} words, {span:.1f}s, {wpm:.0f} wpm)")
    for i in issues:
        print("  REDO  " + i)
    for n in notes:
        print("  note  " + n)
    if heard_text:
        print(f"  heard: {heard_text}")


if __name__ == "__main__":
    main()
