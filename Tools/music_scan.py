"""Measure candidate background tracks (no listening needed for the numbers; listening still decides).

  py -3 Tools/music_scan.py "C:/Users/Admin/Downloads/music" --out "Library/Music/scan_oct15.csv"

Per track (loudest steady 30 s window): duration, rough tempo (BPM, autocorrelation of the onset envelope; may be half/double),
speech-band share (300-3400 Hz energy / 150-8000 Hz energy: lower = more room for narration; vocals push it up), vocal-likelihood flag (a high mid-band share
with a flat-ish spectrum is a hint that there are sung/rapped vocals: instrumentals score lower), and RMS dB.
Tracks with voice or sample names (Voice_Audio, Track1_VoiceAudio...) are skipped.
"""
import csv, os, subprocess, sys
import numpy as np

SR = 22050


def load(path, dur=None):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR)]
    if dur:
        cmd += ["-t", str(dur)]
    raw = subprocess.run(cmd + ["-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def window(x, sec=30):
    n = SR * sec
    if len(x) <= n:
        return x
    hop = SR * 5
    best, bi = -1, 0
    for i in range(0, len(x) - n, hop):
        e = np.sqrt((x[i:i + n] ** 2).mean())
        if e > best:
            best, bi = e, i
    return x[bi:bi + n]


def tempo(x):
    hop = 512
    n = len(x) // hop
    if n < 200:
        return 0
    env = np.array([np.abs(x[i * hop:(i + 1) * hop]).mean() for i in range(n)])
    env = np.maximum(np.diff(env), 0)
    env = env - env.mean()
    ac = np.correlate(env, env, "full")[len(env) - 1:]
    fps = SR / hop
    lo, hi = int(fps * 60 / 200), int(fps * 60 / 60)
    lag = lo + int(np.argmax(ac[lo:hi]))
    return round(60 * fps / lag, 1)


def bands(x):
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    f = np.fft.rfftfreq(len(x), 1 / SR)
    tot = spec.sum() + 1e-12
    mid = spec[(f >= 150) & (f <= 8000)].sum() + 1e-12
    return spec[(f >= 300) & (f <= 3400)].sum() / mid, spec[f < 150].sum() / tot


def main():
    folder = sys.argv[1]
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    rows = []
    only = [a for a in sys.argv[2:] if not a.startswith("--") and a != out]
    for name in sorted(os.listdir(folder)):
        if only and not any(o.lower() in name.lower() for o in only):
            continue
        p = os.path.join(folder, name)
        if not name.lower().endswith((".mp3", ".wav", ".m4a")) or os.path.getsize(p) < 800_000:
            continue
        if any(k in name.lower() for k in ("voice", "track1", "track2", "track3", "untitled", "new_project", "new project")):
            continue
        try:
            x = load(p, 240)
            if len(x) < SR * 20:
                continue
            w = window(x)
            sp, low = bands(w)
            rows.append({"file": name, "sec": round(len(x) / SR), "bpm": tempo(w), "speech_band_pct": round(100 * sp), "bass_pct": round(100 * low),
                         "rms_db": round(20 * np.log10(np.sqrt((w ** 2).mean()) + 1e-9), 1)})
        except Exception as e:
            print("skip", name, e)
    rows.sort(key=lambda r: r["speech_band_pct"])
    if out:
        with open(out, "w", newline="", encoding="utf-8") as f:
            wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            wr.writeheader(); wr.writerows(rows)
    for r in rows:
        print(f"{r['speech_band_pct']:3d}% speech | bass {r['bass_pct']:2d}% | {r['bpm']:5.1f} bpm | {r['sec']:3d}s | {r['file'][:70]}")


if __name__ == "__main__":
    main()
