"""Voice audition, Oct 14 2026: one test script, many voices/settings, the same objective measures for each.
Run:  . key.sh && python3 audition.py [--only name,name] [--measure-only]
Writes takes/<name>.mp3 (raw TTS), takes/<name>_lufs16.mp3 (loudness-matched for listening), takes/<name>_phone.wav (phone-speaker
simulation) and results.json. Reads the API key from the environment (or Tools/.env) and never prints it. Measures are proxies: nobody can 'hear'
naturalness from numbers; the owner's ear decides between the finalists."""
import json, os, re, subprocess, sys, urllib.request, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "Tools"))
REF = ("Victor Wembanyama is not the tallest man in this story. Jamarion Sharp is listed seven-foot-five, and he's never played "
       "an NBA game that counts. Dallas cut him twice. The Clippers cut him in September. Even Nikola Jokic and Giannis "
       "Antetokounmpo never faced him in a game that counts. So what's missing? Three-point tries last season: Wembanyama, "
       "three hundred and fifty. Sharp, in the G League: zero.")
RESPELL = {"Wembanyama": "wem-bun-YAH-muh", "Jokic": "Yoki-ch"}   # the pipeline's {name|respelling} method
CLONE, CLONE_OLD = "GDS7e7WiI4GqkoRxZAFG", "H2ovX6h6fD6dmyrg5SkI"
V2 = "eleven_multilingual_v2"
def s(stab=0.65, sim=0.7, speed=1.15, style=0.0):
    d = {"stability": stab, "similarity_boost": sim, "use_speaker_boost": True, "style": style}
    if speed: d["speed"] = speed
    return d
CANDS = [  # name, voice_id, model, settings, respell
    ("A_clone_prod",      CLONE, V2, s(), True),                     # current production default (clone 'pham v2', setting C)
    ("A2_clone_prod_take2", CLONE, V2, s(), True),                   # same again: take-to-take consistency
    ("A3_clone_raw_names", CLONE, V2, s(), False),                   # same, names not respelled (pronunciation-method test)
    ("B_clone_expressive", CLONE, V2, s(stab=0.45, style=0.35), True),
    ("C_clone_v3",        CLONE, "eleven_v3", s(stab=0.5, sim=0.75, speed=None), True),
    ("D_clone_old_pham",  CLONE_OLD, V2, s(), True),
    ("E_clone_flash",     CLONE, "eleven_flash_v2_5", s(), True),
    ("F_liam_v2",         "TX3LPaxmHKxFdv7VOQHJ", V2, s(stab=0.5, sim=0.75), True),
    ("G_liam_v3",         "TX3LPaxmHKxFdv7VOQHJ", "eleven_v3", s(stab=0.5, sim=0.75, speed=None), True),
    ("H_chris_v2",        "iP95p4xoKVk53GoZ742B", V2, s(stab=0.5, sim=0.75), True),
    ("I_eric_v2",         "cjVigY5qzO86Huf0OWal", V2, s(stab=0.5, sim=0.75), True),
    ("J_charlie_v2",      "IKne3meq5aSn9XLyUdCD", V2, s(stab=0.5, sim=0.75), True),
]
def key():
    k = os.environ.get("ELEVENLABS_API_KEY", "")
    if not k:
        for l in open(os.path.join(ROOT, "Tools", ".env")):
            if l.startswith("ELEVENLABS_API_KEY="): k = l.split("=", 1)[1].strip().strip('"')
    if not k: raise SystemExit("no ElevenLabs key in the environment (run: . key.sh)")
    return k
def tts(vid, model, settings, text, out):
    body = json.dumps({"text": text, "model_id": model, "voice_settings": settings}).encode()
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}?output_format=mp3_44100_128", data=body,
                                 headers={"xi-api-key": key(), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r: open(out, "wb").write(r.read())
def sh(*a): return subprocess.run(a, capture_output=True, text=True)
NUMWORDS = {"zero","one","two","three","four","five","six","seven","eight","nine","ten","fifty","hundred","and","foot"}
def norm(t):
    t = t.lower().replace("-", " ")
    t = re.sub(r"[^a-z0-9' ]", " ", t)
    return [w for w in t.split() if w]
def content(ws):  # words without numbers/number words, for a WER that doesn't punish '350' vs 'three hundred and fifty'
    return [w for w in ws if not re.match(r"^\d", w) and w not in NUMWORDS]
def wer(ref, hyp):
    r, h = content(norm(ref)), content(norm(hyp))
    d = [[0]*(len(h)+1) for _ in range(len(r)+1)]
    for i in range(len(r)+1): d[i][0] = i
    for j in range(len(h)+1): d[0][j] = j
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+(0 if r[i-1] == h[j-1] or close(r[i-1], h[j-1]) else 1))
    return round(100*d[len(r)][len(h)]/max(1, len(r)), 1)
def close(a, b):  # name spellings the recogniser varies on
    import difflib
    return len(a) >= 6 and difflib.SequenceMatcher(None, a, b).ratio() >= 0.75
NAMES = {"wembanyama": ["wemba", "wembun", "wem bun", "wembana", "wembe"], "jamarion": ["jamari"], "jokic": ["jokic", "yokic", "jokich", "yokich", "yokitch"],
         "antetokounmpo": ["anteto", "antetok", "adetok", "antito"], "giannis": ["giannis", "yanis", "yannis"]}
def names_ok(hyp):
    h = hyp.lower().replace("-", "")
    return {n: any(v.replace(" ", "") in h.replace(" ", "") for v in vs) for n, vs in NAMES.items()}
def numbers_ok(hyp):
    h = hyp.lower()
    return {"350": bool(re.search(r"350|three hundred and fifty", h)), "zero": bool(re.search(r"\bzero\b|\b0\b", h)),
            "7-5": bool(re.search(r"7.?.?5|seven.?foot.?five|7 foot 5", h))}
_model = None
def stt(path):
    global _model
    from faster_whisper import WhisperModel
    if _model is None: _model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = _model.transcribe(path, language="en", word_timestamps=True, beam_size=5, temperature=0, vad_filter=True, condition_on_previous_text=False)
    ws = [(w.word.strip(), w.start, w.end) for sg in segs for w in sg.words]
    return " ".join(w for w, _, _ in ws), ws
def prosody(wav):
    import numpy as np, parselmouth
    snd = parselmouth.Sound(wav)
    p = snd.to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=400).selected_array["frequency"]
    v = p[p > 0]
    semis = 12*np.log2(v/np.median(v))
    inten = snd.to_intensity(time_step=0.01).values[0]
    inten = inten[inten > np.percentile(inten, 40)]
    return round(float(np.std(semis)), 2), round(float(np.std(inten)), 2)
def measure(name):
    T = os.path.join(HERE, "takes")
    mp3 = os.path.join(T, name + ".mp3"); wav = os.path.join(T, name + ".wav"); ph = os.path.join(T, name + "_phone.wav")
    sh("ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", "22050", wav)
    sh("ffmpeg", "-v", "error", "-y", "-i", mp3, "-f", "lavfi", "-i", "anoisesrc=color=pink:amplitude=0.03:seed=7", "-filter_complex",
       "[0]aformat=channel_layouts=mono,highpass=f=300,lowpass=f=3400,volume=-4dB[a];[1]highpass=f=300,lowpass=f=3400[n];[a][n]amix=inputs=2:duration=first:normalize=0,aresample=8000",
       "-ar", "16000", ph)
    sh("ffmpeg", "-v", "error", "-y", "-i", mp3, "-af", "loudnorm=I=-16:TP=-1.5:LRA=7", "-ar", "44100", os.path.join(T, name + "_lufs16.mp3"))
    hyp, ws = stt(wav); hyp_ph, _ = stt(ph)
    import voice_quality as vq
    q = vq.measure(wav)
    speech = ws[-1][2] - ws[0][1] if ws else 0
    gaps = [b[1]-a[2] for a, b in zip(ws, ws[1:])]
    psd, isd = prosody(wav)
    return dict(name=name, dur=q["dur"], speech_s=round(speech, 2), wpm=round(len(norm(REF))/speech*60) if speech else 0,
                gaps_over_0p3=sum(g > 0.3 for g in gaps), max_gap=round(max(gaps), 2) if gaps else 0, wer_clean=wer(REF, hyp), wer_phone=wer(REF, hyp_ph),
                names_clean=names_ok(hyp), names_phone=names_ok(hyp_ph), numbers_clean=numbers_ok(hyp), numbers_phone=numbers_ok(hyp_ph),
                pitch_sd_semitones=psd, loudness_sd_db=isd, hnr=q["hnr"], jitter=q["jitter"], shimmer=q["shimmer"], f0_med=q["f0_med"],
                heard_clean=hyp, heard_phone=hyp_ph)
def main():
    only = None
    if "--only" in sys.argv: only = set(sys.argv[sys.argv.index("--only")+1].split(","))
    os.makedirs(os.path.join(HERE, "takes"), exist_ok=True)
    resf = os.path.join(HERE, "results.json")
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    for name, vid, model, st_, rs in CANDS:
        if only and name not in only: continue
        out = os.path.join(HERE, "takes", name + ".mp3")
        text = REF
        if rs:
            for k, v in RESPELL.items(): text = text.replace(k, v)
        if "--measure-only" not in sys.argv or not os.path.exists(out):
            try:
                tts(vid, model, st_, text, out)
            except Exception as e:
                res[name] = {"name": name, "error": str(e)[:300]}; print(name, "ERROR", str(e)[:200]); continue
        m = measure(name); m.update(voice_id=vid, model=model, settings=st_, respelled=rs, chars=len(text))
        res[name] = m; json.dump(res, open(resf, "w"), indent=1, default=float)
        print(f"{name:22} {m['dur']:>5}s wpm{m['wpm']:>4} WER {m['wer_clean']:>5}/{m['wer_phone']:>5} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']} gaps>.3 {m['gaps_over_0p3']}")
main()
