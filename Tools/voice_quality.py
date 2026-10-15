"""Objective voice-quality numbers for a Short's narration (what a person hears as 'glitchy', 'robotic', 'gravelly'). Free, local (Praat via parselmouth).

  python voice_quality.py --folder "<Short folder>"             # judges voice.mp3 (narration pieces only if _timeline.json exists) and prints a verdict
  python voice_quality.py --audio some.mp3 [--audio other.mp3]  # any files
Numbers (compare against the Wemby baseline, the take the user liked: HNR ~ 17-20 dB):
  HNR      harmonics-to-noise ratio in dB over voiced frames. Low = noisy/breathy/robotic/garbled. this cloned voice measures 8-10; REDO below 7.
  jitter   % cycle-to-cycle pitch wobble; shimmer % cycle-to-cycle loudness wobble. High = shaky or warbling voice.
  jumps    pitch jumps > 7 semitones between neighbouring 10 ms frames per second of speech (octave flips = glitch).
  clicks   isolated impulsive spikes per minute (pops at joins, codec clicks).
  hf       share of energy above 6 kHz (dull = very low, hissy/phasey = high).
It cannot hear 'wrong accent' or 'weird emphasis'; use voice_check.py for words and send samples to the user for taste.
"""
import argparse, json, os, subprocess, sys, tempfile
import numpy as np
import parselmouth
from parselmouth.praat import call


def to_wav(path, t0=None, t1=None):
    out = tempfile.mktemp(suffix=".wav")
    cmd = ["ffmpeg", "-v", "error", "-y"]
    if t0 is not None:
        cmd += ["-ss", str(t0), "-t", str(t1 - t0)]
    subprocess.run(cmd + ["-i", path, "-ac", "1", "-ar", "22050", out], check=True)
    return out


def measure(wav):
    snd = parselmouth.Sound(wav)
    dur = snd.get_total_duration()
    pitch = snd.to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=400)
    f0 = pitch.selected_array["frequency"]
    voiced = f0 > 0
    vfrac = float(voiced.mean())
    try:
        hnr = call(snd.to_harmonicity_cc(time_step=0.01, minimum_pitch=70), "Get mean", 0, 0)
    except Exception:
        hnr = float("nan")
    pp = call(snd, "To PointProcess (periodic, cc)", 70, 400)
    try:
        jit = call(pp, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3) * 100
        shim = call([snd, pp], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6) * 100
    except Exception:
        jit = shim = float("nan")
    st = 12 * np.log2(np.where(voiced, f0, np.nan) / 100.0)
    d = np.abs(np.diff(st))
    d = d[~np.isnan(d)]
    jumps = float((d > 7).sum()) / max(1.0, dur)
    x = snd.values[0]
    hp = np.abs(np.diff(x, 2))
    med = np.median(hp) + 1e-9
    clicks = float(np.sum(hp > 40 * med) / max(1.0, dur) * 60)
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    fr = np.fft.rfftfreq(len(x), 1 / 22050)
    hf = float(spec[fr > 6000].sum() / (spec.sum() + 1e-12))
    return dict(dur=round(dur, 2), voiced=round(vfrac, 2), hnr=round(float(hnr), 1), jitter=round(jit, 2), shimmer=round(shim, 2),
                jumps=round(jumps, 2), clicks=round(clicks, 1), hf=round(hf * 100, 2), f0_med=round(float(np.nanmedian(np.where(voiced, f0, np.nan))), 0))


def verdict(m):
    """Thresholds are relative to THIS cloned voice (Oct 5 2026 audit of 64 takes: HNR 6.7-9.9, jitter 2.2-3.3, shimmer 7.6-11.8, pitch jumps ~0).
    The clicks number is a crude pop counter and is reported but not used."""
    bad = []
    if m["hnr"] < 7.0: bad.append(f"HNR {m['hnr']} dB (this voice normally 8-10: noisy/garbled)")
    if m["jitter"] > 3.6: bad.append(f"jitter {m['jitter']}% (shaky)")
    if m["shimmer"] > 12: bad.append(f"shimmer {m['shimmer']}% (uneven loudness)")
    if m["jumps"] > 1.0: bad.append(f"{m['jumps']} pitch jumps/s (octave flips)")
    return ("REDO" if bad else "PASS"), bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder")
    ap.add_argument("--audio", action="append", default=[])
    a = ap.parse_args()
    jobs = [(os.path.basename(p), p, None, None) for p in a.audio]
    if a.folder:
        v = os.path.join(a.folder, "voice.mp3")
        tl = os.path.join(a.folder, "_timeline.json")
        if os.path.exists(tl):
            for t in json.load(open(tl)):
                if t["kind"] == "vo":
                    jobs.append((f"{os.path.basename(a.folder)[:30]}#{t['i']}", v, t["start"], t["end"]))
        else:
            jobs.append((os.path.basename(a.folder)[:34], v, None, None))
    rows = []
    for name, p, t0, t1 in jobs:
        w = to_wav(p, t0, t1)
        try:
            m = measure(w)
        finally:
            os.remove(w)
        vd, bad = verdict(m)
        rows.append((name, m, vd, bad))
        print(f"{name:36s} {vd:4s} HNR {m['hnr']:5.1f} jit {m['jitter']:4.2f} shim {m['shimmer']:5.2f} jumps/s {m['jumps']:4.2f} clicks/min {m['clicks']:5.1f} hf% {m['hf']:5.2f} f0 {m['f0_med']:.0f} dur {m['dur']}  {'; '.join(bad)}")
    if a.folder:
        json.dump([{"name": n, **m, "verdict": vd, "problems": b} for n, m, vd, b in rows], open(os.path.join(a.folder, "voice_quality.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
