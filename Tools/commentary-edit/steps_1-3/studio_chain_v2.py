"""Render voice_v3: v2 studio chain on the full canonical source, then the v3 EDL with declick fades."""
import json, re, subprocess, numpy as np, soundfile as sf

W = r"D:\OBS\ClaudeWork\commentary_v3"
SRC = W + r"\src\src_48k.wav"
N_SRC = 37931008
SR = 48000
# v2 chain, identical to commentary_edit\_work\build_studio.py EQ + final_studio.py PRE (the approved "way better" sound)
EQ = ("highpass=f=70:poles=2,"
      "equalizer=f=350:t=q:w=0.9:g=-3,"
      "equalizer=f=2000:t=q:w=1.4:g=2.5,"
      "equalizer=f=3500:t=q:w=1.0:g=1.5,"
      "deesser=i=0.35:m=0.5:f=0.35,"
      "equalizer=f=8000:t=q:w=0.8:g=-2")
COMP = ("acompressor=threshold=0.18:ratio=4:attack=2:release=60:knee=2:makeup=1,"
        "acompressor=threshold=0.03:ratio=2.5:attack=15:release=250:knee=4:makeup=1")
PRE = (EQ + "," + COMP + ",volume=19dB,alimiter=limit=0.66:attack=3:release=40:level=disabled,"
       "lowpass=f=18500:poles=2,atrim=start_sample=143,asetpts=N/SR/TB,"
       f"apad=whole_len={N_SRC},atrim=end_sample={N_SRC}")
ENH = W + r"\audio\enh_full_v2chain.wav"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", SRC, "-af", PRE, "-c:a", "pcm_f32le",
                "-ar", "48000", "-ac", "1", ENH], check=True)

x, sr = sf.read(ENH, dtype="float64")
assert sr == SR and len(x) == N_SRC, (sr, len(x))
edl = json.load(open(W + r"\edl\edl_v3.json"))
FADE = int(0.010 * SR)
ramp = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, FADE))
parts = []
for s in edl["segments"]:
    if "silence" in s:
        parts.append(np.zeros(int(round(s["silence"] * SR))))
        continue
    a, b = int(round(s["src"][0] * SR)), int(round(s["src"][1] * SR))
    seg = x[a:b].copy()
    seg[:FADE] *= ramp
    seg[-FADE:] *= ramp[::-1]
    parts.append(seg)
y = np.concatenate(parts)
PREW = W + r"\audio\voice_v3_pregain.wav"
sf.write(PREW, y.astype(np.float32), SR, subtype="FLOAT")

def measure(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                        "loudnorm=I=-16:TP=-1.5:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    j = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
    return float(j["input_i"]), float(j["input_tp"]), float(j["input_lra"])

I, TP, LRA = measure(PREW)
gain = round(min(-16.0 - I, -1.9 - TP), 2)
out = y * 10 ** (gain / 20)
OUT = W + r"\audio\voice_v3.wav"
sf.write(OUT, out.astype(np.float32), SR, subtype="PCM_24")
I2, TP2, LRA2 = measure(OUT)
print(json.dumps({"pregain": {"I": I, "TP": TP, "LRA": LRA}, "gain_dB": gain,
                  "final": {"I": I2, "TP": TP2, "LRA": LRA2},
                  "samples": len(out), "seconds": len(out) / SR,
                  "clipped_samples": int(np.sum(np.abs(out) >= 0.999))}, indent=1))
