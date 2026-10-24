"""How loud can a music bed sit under our narration before a phone listener loses words? (Oct 14, 2026)

Same voice take (Voice Audition take A3, the house setup) lifted to -14 LUFS, mixed with each Library bed held at a
constant level (no gap lift: the worst case) of -14 / -17 / -20 / -23 LU under the voice, then passed through the
audition's phone-speaker simulation and transcribed with faster-whisper "small". Measure: word error rate on
non-name, non-number words (the audition's WER), against the no-music baseline. Writes results.json.
I cannot hear audio: this measures intelligibility only, not taste.
"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
AUD = os.path.join(ROOT, "Research Notes", "Voice Audition (Oct 14, 2026)")
src = open(os.path.join(AUD, "audition.py")).read()
ns = {"__file__": os.path.join(AUD, "audition.py")}
exec(src[:src.index("def main():")], ns)  # REF, norm, content, wer (without running the audition)
REF, wer = ns["REF"], ns["wer"]
VOICE = os.path.join(AUD, "takes", "A3_clone_raw_names.mp3")
TRACKS = ["eleven_stats_01", "eleven_hype_01", "eleven_emotional_01", "eleven_suspense_01"]
LEVELS = [int(x) for x in os.environ.get("LEVELS", "-14,-17,-20,-23").split(",")]
T = os.path.join(HERE, "work"); os.makedirs(T, exist_ok=True)

def sh(*a): subprocess.run(a, check=True, capture_output=True)
def lufs(p):
    import re
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1])
def phone(src, out):
    sh("ffmpeg", "-v", "error", "-y", "-i", src, "-f", "lavfi", "-i", "anoisesrc=color=pink:amplitude=0.03:seed=7", "-filter_complex",
       "[0]aformat=channel_layouts=mono,highpass=f=300,lowpass=f=3400,volume=-4dB[a];[1]highpass=f=300,lowpass=f=3400[n];[a][n]amix=inputs=2:duration=first:normalize=0,aresample=8000",
       "-ar", "16000", out)
from faster_whisper import WhisperModel
M = WhisperModel("small", device="cpu", compute_type="int8")
def hear(p): return " ".join(s.text for s in M.transcribe(p, language="en", beam_size=5)[0])

v14 = os.path.join(T, "voice_m14.wav")
sh("ffmpeg", "-v", "error", "-y", "-i", VOICE, "-af", f"volume={-14 - lufs(VOICE):.2f}dB", "-ar", "48000", v14)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v14], capture_output=True, text=True).stdout)
res = {"voice": "A3_clone_raw_names", "voice_lufs": lufs(v14), "levels_lu": LEVELS, "runs": {}}
phone(v14, os.path.join(T, "base_phone.wav"))
h = hear(os.path.join(T, "base_phone.wav")); res["runs"]["no_music"] = {"wer_phone": wer(REF, h), "heard": h}
print("no music", res["runs"]["no_music"]["wer_phone"])
for tr in TRACKS:
    tp = os.path.join(HERE, "..", tr + ".mp3")
    seg = lufs(tp)
    for L in LEVELS:
        g = (-14 + L) - seg
        mix = os.path.join(T, f"{tr}_{-L}.wav")
        sh("ffmpeg", "-v", "error", "-y", "-i", v14, "-stream_loop", "-1", "-i", tp, "-filter_complex",
           f"[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g:.2f}dB[m];[0:a]aformat=sample_rates=48000:channel_layouts=stereo[v];"
           f"[v][m]amix=inputs=2:normalize=0:duration=first", "-t", f"{dur:.2f}", mix)
        ph = mix.replace(".wav", "_phone.wav"); phone(mix, ph)
        h = hear(ph)
        res["runs"][f"{tr}@{L}"] = {"track": tr, "bed_lu": L, "track_lufs": seg, "gain_db": round(g, 2), "wer_phone": wer(REF, h), "heard": h}
        print(tr, L, res["runs"][f"{tr}@{L}"]["wer_phone"])
json.dump(res, open(os.path.join(HERE, os.environ.get("OUT", "results.json")), "w"), indent=1)
