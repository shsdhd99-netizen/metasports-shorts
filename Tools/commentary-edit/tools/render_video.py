"""Mux: muted gameplay segments (approved order) + the final voice (dual mono) -> 1080p60 h264_nvenc + AAC 320k.
usage: python render_video.py voice_mono.wav out.mp4 plan.json
plan.json = {"source": "<gameplay file>", "segments": [[ss, length], ..., [ss, null]]}   (null = fill to the voice length)"""
import sys, json, subprocess, soundfile as sf
voice, out, planp = sys.argv[1], sys.argv[2], sys.argv[3]
plan = json.load(open(planp))
info = sf.info(voice); total = info.frames / info.samplerate
fixed = sum(t for _, t in plan["segments"] if t is not None)
segs = [(ss, (t if t is not None else round(total - fixed + 0.5, 3))) for ss, t in plan["segments"]]
cmd = ["ffmpeg", "-y", "-v", "error", "-stats"]
for ss, t in segs:
    cmd += ["-ss", str(ss), "-t", str(t), "-i", plan["source"]]
cmd += ["-i", voice]
n = len(segs)
vin = "".join(f"[{i}:v]" for i in range(n))
fc = f"{vin}concat=n={n}:v=1:a=0,scale=1920:1080:flags=lanczos,fps=60,format=yuv420p[v];[{n}:a]pan=stereo|c0=c0|c1=c0[a]"
cmd += ["-filter_complex", fc, "-map", "[v]", "-map", "[a]",
        "-c:v", "h264_nvenc", "-preset", "p7", "-tune", "hq", "-rc", "vbr", "-cq", "19", "-b:v", "14M", "-maxrate", "16M",
        "-bufsize", "32M", "-profile:v", "high", "-c:a", "aac", "-b:a", "320k", "-ar", "48000",
        "-t", f"{total:.3f}", "-movflags", "+faststart", out]
print("voice seconds", round(total, 3), "last gameplay segment", segs[-1], flush=True)
r = subprocess.run(cmd)
print("RENDER_EXIT", r.returncode)
sys.exit(r.returncode)
