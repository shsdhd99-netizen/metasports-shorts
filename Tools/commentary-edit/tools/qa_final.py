"""Final-file QA: specs, loudness of the actual mp4 (integrated, LRA, short-term max, true peak), full decode for errors,
black / freeze, A/V length match, click check at every cut (calibrated against random positions), frame sheet.
usage: python qa_final.py final.mp4 voice_mono.wav edl.json out_dir"""
import sys, json, re, subprocess, numpy as np, soundfile as sf
from PIL import Image, ImageDraw
final, voice, edlp, outd = sys.argv[1:5]
import os; os.makedirs(outd, exist_ok=True)
rep = {}
p = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                    "stream=codec_type,codec_name,width,height,r_frame_rate,bit_rate,sample_rate,channels,duration:format=duration,bit_rate",
                    "-of", "json", final], capture_output=True, text=True)
rep["ffprobe"] = json.loads(p.stdout)

# loudness of the real file (decoded AAC, both channels)
r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", final, "-vn", "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"],
                   capture_output=True, text=True)
S = r.stderr[r.stderr.rfind("Summary:"):]
g = lambda pat: float(re.search(pat, S).group(1))
rep["loudness"] = {"integrated_LUFS": g(r"I:\s+(-?[\d.]+) LUFS"), "LRA": g(r"LRA:\s+(-?[\d.]+) LU"), "true_peak_dBTP": g(r"Peak:\s+(-?[\d.]+) dBFS")}
# short-term (3 s) distribution
r2 = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", final, "-vn", "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
st = [float(m) for m in re.findall(r"S:\s+(-?[\d.]+)", r2.stderr) if float(m) > -60]
if st:
    rep["loudness"]["short_term_LUFS_p5_p50_p95_max"] = [round(float(np.percentile(st, q)), 1) for q in (5, 50, 95)] + [round(max(st), 1)]

# full decode: any error text at all
d = subprocess.run(["ffmpeg", "-v", "error", "-i", final, "-f", "null", "-"], capture_output=True, text=True)
rep["decode_errors"] = d.stderr.strip().splitlines()[:10]

# black / freeze (video only)
b = subprocess.run(["ffmpeg", "-hide_banner", "-i", final, "-vf", "scale=320:-1,blackdetect=d=0.5:pix_th=0.08,freezedetect=n=0.002:d=3",
                    "-an", "-f", "null", "-"], capture_output=True, text=True)
rep["black"] = re.findall(r"black_start:\S+ black_end:\S+", b.stderr)
rep["freeze"] = re.findall(r"freeze_start: \S+|freeze_end: \S+", b.stderr)

# click check at every cut vs random positions (2nd-order prediction residual, +-1.5 ms around the crossfade centre)
y, sr = sf.read(voice, dtype="float64")
edl = json.load(open(edlp)); segm = edl["seg_map"]; F = 0.005
def score(t):
    k = int(round(t * sr)); a = y[k - int(0.2 * sr): k + int(0.2 * sr)]
    if len(a) < 100: return None
    res = a[2:] - 2 * a[1:-1] + a[:-2]
    c = len(res) // 2; w = int(0.0015 * sr)
    return float(np.abs(res[c - w: c + w]).max() / (np.percentile(np.abs(res), 99) + 1e-12))
joins = [segm[k + 1][2] - F for k in range(len(segm) - 1)]
js = [(score(t), round(t, 3)) for t in joins]; js = [x for x in js if x[0] is not None]
rng = np.random.default_rng(1); rs = [score(t) for t in rng.uniform(1, len(y) / sr - 1, 1500)]
thr = float(np.percentile([x for x in rs if x is not None], 99.5))
worst = sorted(js, reverse=True)[:8]
rep["clicks"] = {"cuts": len(js), "random_position_p99.5": round(thr, 2), "cuts_above_threshold": [(round(s, 2), t) for s, t in js if s > thr],
                 "worst8": [(round(s, 2), t) for s, t in worst], "median_cut": round(float(np.median([s for s, _ in js])), 2)}
rep["voice_clipped_samples"] = int(np.sum(np.abs(y) >= 0.999))
dur_v = float(rep["ffprobe"]["format"]["duration"]); rep["av_len"] = {"file": dur_v, "voice": len(y) / sr}

# frames
dur = dur_v; times = [0.5, 3.0, 20, dur * .15, dur * .3, dur * .45, dur * .6, dur * .75, dur * .9, dur - 1.0]
ims = []
for i, t in enumerate(times):
    fp = os.path.join(outd, f"fr_{i:02d}.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", final, "-frames:v", "1", "-vf", "scale=480:-1", fp], check=True)
    ims.append(Image.open(fp))
w, h = ims[0].size; sheet = Image.new("RGB", (w * 5, h * 2))
for i, im in enumerate(ims):
    sheet.paste(im, ((i % 5) * w, (i // 5) * h)); ImageDraw.Draw(sheet).text(((i % 5) * w + 6, (i // 5) * h + 6), f"t={times[i]:.1f}", fill="yellow")
sheet.save(os.path.join(outd, "frames_sheet.jpg"), quality=80)
json.dump(rep, open(os.path.join(outd, "qa_final.json"), "w"), indent=1)
print(json.dumps(rep, indent=1)[:4000])
