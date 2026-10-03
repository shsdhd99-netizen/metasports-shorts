"""pregain voice (float mono 48 kHz) -> final voice at the delivery loudness.
Delivery = dual-mono stereo at -14.0 LUFS integrated (YouTube's reference; it never boosts quiet uploads) with true peak <= -1.6 dBTP.
For dual-mono, stereo loudness = mono loudness + 3.01 dB, so the mono file is scaled to (target - 3.01).
usage: python render_voice.py pregain.wav out_mono.wav [target_stereo_lufs=-14.0] [tp_ceiling=-1.6]"""
import sys, json, re, subprocess, numpy as np, soundfile as sf

def measure(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "loudnorm=I=-16:TP=-1.5:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    j = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
    return float(j["input_i"]), float(j["input_tp"]), float(j["input_lra"])

def limit(x, ceiling_db):
    """transparent look-ahead peak limiter (ffmpeg alimiter) on a float array"""
    import tempfile, os
    a = os.path.join(tempfile.gettempdir(), "lim_in.wav"); b = os.path.join(tempfile.gettempdir(), "lim_out.wav")
    sf.write(a, x.astype(np.float32), 48000, subtype="FLOAT")
    lim = 10 ** (ceiling_db / 20)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", a, "-af", f"alimiter=limit={lim:.4f}:attack=5:release=60:level=disabled",
                    "-c:a", "pcm_f32le", b], check=True)
    y, _ = sf.read(b, dtype="float64"); return y

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    target = float(sys.argv[3]) if len(sys.argv) > 3 else -14.0
    tp_max = float(sys.argv[4]) if len(sys.argv) > 4 else -1.6
    x, sr = sf.read(src, dtype="float64"); assert sr == 48000 and x.ndim == 1
    I0, TP0, LRA0 = measure(src)
    mono_target = target - 3.01
    gain = mono_target - I0
    log = [{"step": "pregain", "I": I0, "TP": TP0, "LRA": LRA0}]
    y = x
    for it in range(4):
        y = x * 10 ** (gain / 20)
        if TP0 + gain > tp_max - 0.3:
            y = limit(y, tp_max - 0.25)
        tmp = dst + ".tmp.wav"; sf.write(tmp, y.astype(np.float32), sr, subtype="FLOAT")
        I, TP, LRA = measure(tmp); log.append({"step": f"iter{it}", "gain_dB": round(gain, 2), "I_mono": I, "TP": TP, "LRA": LRA})
        if abs(I - mono_target) <= 0.12 and TP <= tp_max: break
        gain += (mono_target - I)
    sf.write(dst, y.astype(np.float32), sr, subtype="PCM_24")
    I2, TP2, LRA2 = measure(dst)
    res = {"steps": log, "final_mono": {"I": I2, "TP": TP2, "LRA": LRA2}, "stereo_dual_mono_I_expected": round(I2 + 3.01, 2),
           "clipped_samples": int(np.sum(np.abs(y) >= 0.999)), "seconds": len(y) / sr}
    print(json.dumps(res, indent=1))
    import os; os.remove(dst + ".tmp.wav")
