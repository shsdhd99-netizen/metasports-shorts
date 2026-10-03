"""Verbatim re-transcription (CrisperWhisper: keeps um/uh/false starts) of any wav -> json with word times.
Runs in 150 s pieces (10 s overlap) so GPU memory stays bounded on a 12 GB card shared with the desktop
(one 12-minute call once filled VRAM and crawled). Words are accepted from the middle of each piece only.
usage: python asr_check.py in.wav out.json"""
import os, sys, json, time
base = r"D:\OBS\ClaudeWork\commentary_v3"
for k, v in {"HF_HOME": r"cache\hf", "TORCH_HOME": r"cache\torch", "PIP_CACHE_DIR": r"cache\pip",
             "U2NET_HOME": r"cache\u2net", "XDG_CACHE_HOME": r"cache\xdg"}.items():
    os.environ[k] = os.path.join(base, v)
import numpy as np, soundfile as sf, torch
from scipy.signal import resample_poly
from crisperwhisper import CrisperWhisperModel

def load16(path):
    x, sr = sf.read(path, dtype="float32", always_2d=True)
    x = x.mean(axis=1)
    if sr != 16000:
        g = np.gcd(sr, 16000); x = resample_poly(x, 16000 // g, sr // g).astype(np.float32)
    return x

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    x = load16(src); dur = len(x) / 16000
    t = time.time()
    model = CrisperWhisperModel("large", backend="transformers", compute_type="float16", device="cuda")
    print("loaded", round(time.time() - t, 1), "s; audio", round(dur, 1), "s", flush=True)
    PIECE, HOP, EDGE = 150.0, 140.0, 5.0
    words, s0 = [], 0.0
    while s0 < dur - 1:
        s1 = min(dur, s0 + PIECE); last = s1 >= dur - 0.01
        t = time.time()
        r = model.transcribe(x[int(s0 * 16000): int(s1 * 16000)], sr=16000, language="en", mode="verbatim", word_timestamps=True)
        lo = 0.0 if s0 == 0 else EDGE; hi = (s1 - s0) if last else (s1 - s0 - EDGE)
        for w in (r.words or []):
            c = (w.start + w.end) / 2
            if lo <= c < hi: words.append({"word": w.word, "start": w.start + s0, "end": w.end + s0})
        print(f"piece {s0:.0f}-{s1:.0f}s done in {time.time() - t:.0f}s, words so far {len(words)}, "
              f"vram {torch.cuda.memory_allocated() / 2**30:.1f}/{torch.cuda.max_memory_allocated() / 2**30:.1f} GB", flush=True)
        torch.cuda.empty_cache()
        if last: break
        s0 += HOP
    json.dump({"words": words, "dur": dur}, open(dst, "w"), indent=0)
    print("done", len(words), "words", flush=True)
