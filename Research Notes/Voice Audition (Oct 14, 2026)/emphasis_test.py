"""Voice part 2 (Oct 14, 2026): do our takes stress the key numbers, and can we get a beat of silence before the punchline?

Why: the old hit Shorts (Posted Video Audit section 10) stressed every number and paused ~0.4 s before the final word.
Part 1 (free): measures the voices of the ready Shorts (#40, #41, #21, #38): loudness and pitch of number words vs other words.
Part 2 (about 1.4K ElevenLabs characters): #40's script in 4 variants (production / "..." before the punchline /
expressive settings / both), measured the same way plus the pause before "Not" and the word error rate.
I cannot hear audio: these are measurements, the owner's ear decides. Writes emphasis_results.json.
"""
import json, os, re, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
src = open(os.path.join(HERE, "audition.py")).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
tts, s, CLONE, V2, wer = ns["tts"], ns["s"], ns["CLONE"], ns["V2"], ns["wer"]
NUM = re.compile(r"\d|^(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fifteen|sixteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|zero)", re.I)

def word_feats(audio, words):
    import parselmouth
    snd = parselmouth.Sound(audio)
    pitch = snd.to_pitch(time_step=0.01)
    f0 = pitch.selected_array["frequency"]; tt = pitch.xs()
    x = snd.values[0]; sr = snd.sampling_frequency
    out = []
    for w in words:
        a, b = int(w["start"] * sr), int(w["end"] * sr)
        if b - a < 50:
            continue
        db = 20 * np.log10(np.sqrt(np.mean(x[a:b] ** 2)) + 1e-9)
        sel = f0[(tt >= w["start"]) & (tt <= w["end"]) & (f0 > 0)]
        out.append((w["word"], db, float(np.median(sel)) if len(sel) else None))
    return out

def prominence(feats):
    num = [f for f in feats if NUM.search(f[0].strip(".,:;!?\"'"))]
    oth = [f for f in feats if not NUM.search(f[0].strip(".,:;!?\"'")) and len(f[0].strip(".,")) > 3]
    if not num or not oth:
        return None
    ddb = np.mean([f[1] for f in num]) - np.mean([f[1] for f in oth])
    pn = [f[2] for f in num if f[2]]; po = [f[2] for f in oth if f[2]]
    dst = 12 * np.log2(np.median(pn) / np.median(po)) if pn and po else None
    return {"number_words": len(num), "loudness_vs_other_db": round(float(ddb), 2), "pitch_vs_other_semitones": round(float(dst), 2) if dst is not None else None}

def transcribe(path):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(path, language="en", word_timestamps=True)
    words = [{"word": w.word.strip(), "start": w.start, "end": w.end} for sg in segs for w in sg.words]
    return words

res = {"part1_ready_shorts": {}, "part2_variants": {}}
P = os.path.join(ROOT, "Productions", "MetaSports")
for name in ["2026-10-13 40 Why Jokics Best Pass Doesnt Count", "2026-10-13 41 Is Anyone Taller Than Wemby",
             "2026-10-04 21 How Close Is Jokic To Westbrooks Record", "2026-10-06 38 What Did LeBron Promise Sixers Fans"]:
    F = os.path.join(P, name)
    w = json.load(open(os.path.join(F, "words.json"))); w = w["words"] if isinstance(w, dict) else w
    wav = os.path.join(HERE, "takes", "_tmp.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(F, "voice.mp3"), "-ac", "1", "-ar", "22050", wav])
    res["part1_ready_shorts"][name[11:]] = prominence(word_feats(wav, w))
    print(name[11:40], res["part1_ready_shorts"][name[11:]])

if "--part2" in sys.argv:
    base = open(os.path.join(P, "2026-10-13 40 Why Jokics Best Pass Doesnt Count", "script.txt")).read().strip()
    base = re.sub(r"\{([^|}]*)\|([^}]*)\}", r"\2", base)  # spoken forms
    pause_txt = base.replace("six thousand and eighty. Not eighty-one.", "six thousand and eighty... Not eighty-one.")
    variants = {"V0_production": (base, s()), "V1_ellipsis": (pause_txt, s()),
                "V2_expressive": (base, s(stab=0.45, style=0.35)), "V3_ellipsis_expressive": (pause_txt, s(stab=0.45, style=0.35))}
    for k, (text, st) in variants.items():
        mp3 = os.path.join(HERE, "takes", f"E_{k}.mp3"); wav = mp3.replace(".mp3", ".wav")
        if not os.path.exists(mp3):
            tts(CLONE, V2, st, text, mp3)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", "22050", wav])
        words = transcribe(wav)
        heard = " ".join(x["word"] for x in words)
        idx = max(i for i, x in enumerate(words) if x["word"].lower().startswith("not"))
        pause = words[idx]["start"] - words[idx - 1]["end"]
        dur = words[-1]["end"] - words[0]["start"]
        r = {"chars": len(text), "seconds": round(dur, 2), "wpm": round(len(text.split()) / dur * 60), "pause_before_Not_s": round(pause, 2),
             "wer": wer(base, heard), "prominence": prominence(word_feats(wav, words)), "heard": heard}
        res["part2_variants"][k] = r
        print(k, {kk: vv for kk, vv in r.items() if kk != "heard"})
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-af", "loudnorm=I=-16:TP=-1.5:LRA=7", "-ar", "44100", mp3.replace(".mp3", "_lufs16.mp3")])
json.dump(res, open(os.path.join(HERE, "emphasis_results.json"), "w"), indent=1, default=float)
