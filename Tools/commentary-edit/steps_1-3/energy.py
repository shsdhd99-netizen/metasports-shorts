"""Short-time RMS envelope of src_48k (canonical) + helpers. Cached to energy_env.npz."""
import os, numpy as np, soundfile as sf
BASE = r"D:\OBS\ClaudeWork\commentary_v3"
HOP = 0.0025  # 2.5 ms hop
WIN = 0.010   # 10 ms window
CACHE = os.path.join(BASE, r"asr\work\energy_env.npz")
def envelope():
    if os.path.exists(CACHE):
        z = np.load(CACHE); return z["db"], float(z["hop"])
    x, sr = sf.read(os.path.join(BASE, r"src\src_48k.wav"), dtype="float32")
    assert sr == 48000
    # high-pass ~80 Hz to drop rumble
    from scipy.signal import butter, sosfiltfilt
    sos = butter(4, 80, "hp", fs=sr, output="sos"); x = sosfiltfilt(sos, x).astype(np.float32)
    h = int(HOP * sr); w = int(WIN * sr)
    n = (len(x) - w) // h + 1
    idx = np.arange(w)[None, :] + h * np.arange(n)[:, None]
    rms = np.sqrt(np.mean(x[idx] ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-9)
    # frame i covers [i*h, i*h+w) -> center time i*HOP + WIN/2
    np.savez(CACHE, db=db, hop=HOP)
    return db, HOP
def t2i(t, hop=HOP): return int(round((t - WIN / 2) / hop))
def i2t(i, hop=HOP): return i * hop + WIN / 2
