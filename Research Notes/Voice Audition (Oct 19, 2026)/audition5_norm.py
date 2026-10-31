"""Round 5, stage 2: pace-normalised takes. Eleven v4/v3 have no speed control and read about 150 wpm with long pauses, so each
take is (1) pause-tightened with Tools/voice_fx.tighten_gaps (pauses over 0.30 s cut to 0.18 s, only between words) and
(2) time-stretched with ffmpeg atempo to the CONTROL's length (the #42 voice, Alex v2 at 1.2), capped at x1.35.
Then the same measures run again, so voices are compared at the same pace. No new credits are spent.
"""
import json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
src = open(os.path.join(ROOT, "Research Notes", "Voice Audition (Oct 14, 2026)", "audition.py")).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
sys.path.insert(0, os.path.join(ROOT, "Tools"))
import voice_fx, voiceover
RAW = open(os.path.join(ROOT, "Productions", "MetaSports", "2026-10-14 42 Who Has Missed The Most Shots Ever", "_v3", "script.txt")).read().strip()
ns["REF"] = " ".join(s for _, s in voiceover.parse_script(voiceover.apply_dictionary(RAW, "default")[0]))
T = os.path.join(HERE, "takes")
res = json.load(open(os.path.join(HERE, "results5.json")))
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
target = dur(os.path.join(T, "R5_A_v2_t1.mp3"))
out = {}
for nm in sorted(res):
    if "error" in res[nm] or not nm.startswith("R5_"):
        continue
    srcf = os.path.join(T, nm + ".mp3"); n2 = nm.replace("R5_", "R5n_")
    dst = os.path.join(T, n2 + ".mp3")
    if nm == "R5_A_v2_t1":
        shutil.copy(srcf, dst); factor = 1.0
    else:
        hyp, ws = ns["stt"](os.path.join(T, nm + ".wav"))
        tight = os.path.join(T, n2 + "_tight.mp3")
        voice_fx.tighten_gaps(srcf, ws, tight, keep=0.18, thresh=0.30)
        factor = min(1.35, max(1.0, dur(tight) / target))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tight, "-af", f"atempo={factor:.4f}", "-c:a", "libmp3lame", "-q:a", "0", dst], check=True)
        os.remove(tight)
    m = ns["measure"](n2); m.update(stretch=round(factor, 3), source=nm, label=res[nm]["label"])
    out[n2] = m
    print(f"{n2:15} x{factor:.2f} {m['dur']:>5}s wpm{m['wpm']:>4} WERphone {m['wer_phone']:>5} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']} jit {m['jitter']} shim {m['shimmer']} gaps>.3 {m['gaps_over_0p3']}")
json.dump(out, open(os.path.join(HERE, "results5_norm.json"), "w"), indent=1, default=float)
