"""Side-by-side numbers for two takes of the SAME script (Oct 15, 2026). Read-only: no API calls, no credits.

  py -3 Tools/voice_ab.py "<folder A>" "<folder B>" [--labels Alex,pham]

Each folder holds voice.mp3, words.json and script.txt, as written by voiceover.py / voice_take.py. Needs numpy, ffmpeg and
praat-parselmouth, so run it with `py -3` on the owner's PC (plain `python` there is 3.12 without parselmouth).

Prints, per take:
  real pace        spoken words over the speech span. voice_check's wpm counts "15,541" as ONE word, so it under-reads scripts with
                   numbers (#42: 163 and 169 against a real 210 and 217).
  pauses           gaps between words over 0.30 s, the three longest gaps, total silence between words.
  loudness SD      spread of word loudness in dB (a flat read has a small number).
  numbers vs rest  loudness (dB) and pitch (semitones) of number words against the other content words. Negative = the voice dips on numbers.
  last word        how long the alignment says it lasts, how long it is audible (within 25 dB of its own peak), and its loudest 50 ms.
                   voice_check flags a long last word as "stretched"; a short audible length means a quiet tail, not a stretched word.
It measures. It cannot hear: the owner's ear decides between voices.
"""
import argparse, json, os, re, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voiceover import parse_script  # noqa: E402

FUNC = set("the a an and or but so of in on at to for with is was are were be he she it his her its that this than has have had".split())
SMALL_NUMS = ("fifty-one", "forty-five", "percent")


def pcm(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0, sr


def db(x):
    return 20 * np.log10(max(1e-9, float(np.sqrt(np.mean(np.square(x)))))) if len(x) else -120.0


def is_num(w):
    t = w.lower().strip(".,:?!")
    return bool(re.search(r"\d", t)) or t in SMALL_NUMS


def content(w):
    return w.lower().strip(".,:?!'s") not in FUNC


def analyse(folder):
    import parselmouth
    words = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8-sig"))
    segs = parse_script(open(os.path.join(folder, "script.txt"), encoding="utf-8-sig").read())
    spoken_words = len(re.findall(r"[A-Za-z0-9']+", " ".join(sp for _, sp in segs)))  # same rule as script_lint.py ("forty-one" is two words)
    x, sr = pcm(os.path.join(folder, "voice.mp3"))
    span = words[-1]["end"] - words[0]["start"]
    out = {"file length (s)": round(len(x) / sr, 2), "spoken words": spoken_words, "real pace (wpm)": round(spoken_words / span * 60, 1)}

    gaps = [(words[i + 1]["start"] - words[i]["end"], f"{words[i]['word']} -> {words[i + 1]['word']}", words[i]["end"]) for i in range(len(words) - 1)]
    out["pauses over 0.30 s"] = sum(1 for g in gaps if g[0] > 0.30)
    out["longest gaps (s, between, at s)"] = [(round(g[0], 2), g[1], round(g[2], 2)) for g in sorted(gaps, reverse=True)[:3]]
    out["silence between words (s)"] = round(sum(max(0, g[0]) for g in gaps), 2)

    lv = [(w["word"], db(x[int(w["start"] * sr):int(w["end"] * sr)])) for w in words]
    out["loudness SD (dB)"] = round(float(np.std([v for _, v in lv])), 2)
    nums = [v for w, v in lv if is_num(w)]
    rest = [v for w, v in lv if not is_num(w) and content(w)]
    out["numbers vs content words, loudness (dB)"] = round(float(np.mean(nums) - np.mean(rest)), 2) if nums and rest else None

    pitch = parselmouth.Sound(x, sampling_frequency=sr).to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=400)
    t, f = pitch.xs(), pitch.selected_array["frequency"]
    med = np.median(f[f > 0])

    def wp(w):
        m = (t >= w["start"]) & (t <= w["end"]) & (f > 0)
        return float(np.median(12 * np.log2(f[m] / med))) if m.any() else None
    pn = [p for p in (wp(w) for w in words if is_num(w["word"])) if p is not None]
    po = [p for p in (wp(w) for w in words if not is_num(w["word"]) and content(w["word"])) if p is not None]
    out["numbers vs content words, pitch (semitones)"] = round(float(np.mean(pn) - np.mean(po)), 2) if pn and po else None

    last = words[-1]
    seg = x[int(last["start"] * sr):]
    hop = int(0.01 * sr)
    env = np.array([db(seg[i:i + 2 * hop]) for i in range(0, max(1, len(seg) - 2 * hop), hop)])
    peak = float(env.max())
    w50 = int(0.05 * sr)
    peak50 = max(db(seg[i:i + w50]) for i in range(0, max(1, len(seg) - w50), hop))  # loudest 50 ms of the word
    near = np.where(env > peak - 25)[0]
    out["last word"] = {"word": last["word"], "alignment (s)": round(last["end"] - last["start"], 2),
                        "audible, within 25 dB of peak (s)": round(float((near[-1] + 2) * 0.01), 2) if len(near) else None,
                        "loudest 50 ms (dBFS)": round(float(peak50), 1)}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder_a")
    ap.add_argument("folder_b")
    ap.add_argument("--labels", default="A,B")
    a = ap.parse_args()
    la, lb = (a.labels.split(",") + ["B"])[:2]
    ra, rb = analyse(a.folder_a), analyse(a.folder_b)
    print(f"{'':44} {la:>28} {lb:>28}")
    for k in ra:
        va, vb = ra[k], rb[k]
        if isinstance(va, dict):
            for kk in va:
                print(f"{k + ': ' + kk:44} {str(va[kk]):>28} {str(vb[kk]):>28}")
        elif isinstance(va, list):
            print(f"{k}")
            print(f"   {la}: {va}")
            print(f"   {lb}: {vb}")
        else:
            print(f"{k:44} {str(va):>28} {str(vb):>28}")


if __name__ == "__main__":
    main()
