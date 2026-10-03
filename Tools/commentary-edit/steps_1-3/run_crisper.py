import os, sys, json, time
base = r"D:\OBS\ClaudeWork\commentary_v3"
for k, v in {"HF_HOME": r"cache\hf", "TORCH_HOME": r"cache\torch", "PIP_CACHE_DIR": r"cache\pip",
             "U2NET_HOME": r"cache\u2net", "XDG_CACHE_HOME": r"cache\xdg"}.items():
    os.environ[k] = os.path.join(base, v)
import numpy as np, soundfile as sf, torch
from crisperwhisper import CrisperWhisperModel, __version__ as cwv
OFF = 48.917333333333333
audio, sr = sf.read(os.path.join(base, r"src\src_16k.wav"), dtype="float32")
assert sr == 16000, sr
cut = int(round(OFF * sr))
parts = [("file1", 0.0, audio[:cut]), ("file2", cut / sr, audio[cut:])]
print("crisperwhisper", cwv, "torch", torch.__version__, "cuda", torch.cuda.is_available(), "dur", len(audio) / sr, flush=True)
t0 = time.time()
model = CrisperWhisperModel("large", backend="transformers", compute_type="float16", device="cuda")
print("loaded", model.backend, round(time.time() - t0, 1), "s", flush=True)
out = {"engine": "crisperwhisper", "version": cwv, "model": "nyralabs/CrisperWhisper2.0_large", "parts": []}
for name, offset, x in parts:
    t1 = time.time()
    r = model.transcribe(x, sr=sr, language="en", mode="verbatim", word_timestamps=True)
    print(name, "done", round(time.time() - t1, 1), "s", "words", len(r.words or []), flush=True)
    out["parts"].append({"name": name, "offset": offset, "text": r.text,
        "words": [{"word": w.word, "start": w.start, "end": w.end} for w in (r.words or [])],
        "chunks": [{"i": c.chunk_idx, "s": c.start_sec, "e": c.end_sec, "text": c.text} for c in (r.chunks or [])]})
json.dump(out, open(os.path.join(base, r"asr\work\crisper_raw.json"), "w"), indent=1)
print("WROTE crisper_raw.json total", round(time.time() - t0, 1), flush=True)
