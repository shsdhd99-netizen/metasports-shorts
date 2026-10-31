"""Is a name's first sound a 'Y' (glide) or a 'J' (affricate)? An affricate has a burst of hiss (energy above 2.5 kHz, many
zero crossings) in its first ~70 ms; a glide is voiced and smooth. Measured on whisper's word timings. Reference points:
the same voice saying 'Yokitch'/'Yannis' (Y) and 'Jusuf'/'Jonas' when respelled with a J (J). Usage: python3 onset_check.py"""
import json, os, re, subprocess, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
from faster_whisper import WhisperModel
wm = WhisperModel("small", device="cpu", compute_type="int8")
def onset(wav, targets):
    segs, _ = wm.transcribe(wav, language="en", word_timestamps=True)
    ws = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", wav, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout, np.int16).astype(np.float32)
    out = []
    for w, a, b in ws:
        k = re.sub(r"[^a-z]", "", w.lower())
        if any(k.startswith(t) for t in targets):
            seg = x[int(a * 16000): int(a * 16000) + 1120]
            if len(seg) < 400: continue
            S = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))) ** 2; f = np.fft.rfftfreq(len(seg), 1 / 16000)
            hf = S[f > 2500].sum() / S.sum(); zcr = np.mean(np.abs(np.diff(np.sign(seg)))) / 2 * 16000
            out.append((w, round(a, 2), round(float(hf) * 100, 1), int(zcr)))
    return out
T = os.path.join(HERE, "takes")
for name in ["N_alex_plain", "N_alex_respelled", "R3_X1_ref", "R3_P1_ref", "A3_clone_raw_names", "A_clone_prod"]:
    wav = os.path.join(T, name + ".wav")
    if os.path.exists(wav):
        print(name, onset(wav, ["jok", "yok", "gian", "yan", "yus", "jus", "jon", "yon", "don"]))
