"""CTC forced alignment of the CrisperWhisper verbatim words (canonical time) with torchaudio.
Usage: fa.py <bundle: LV60K|MMS> ; writes fa_<bundle>.json"""
import os, sys, json, re, time
BASE = r"D:\OBS\ClaudeWork\commentary_v3"
for k, v in {"HF_HOME": r"cache\hf", "TORCH_HOME": r"cache\torch", "PIP_CACHE_DIR": r"cache\pip",
             "U2NET_HOME": r"cache\u2net", "XDG_CACHE_HOME": r"cache\xdg"}.items():
    os.environ[k] = os.path.join(BASE, v)
import numpy as np, soundfile as sf, torch, torchaudio
import torchaudio.functional as F
WHICH = sys.argv[1]
OFF = 48.917333333333333
dev = "cuda"
x, sr = sf.read(os.path.join(BASE, r"src\src_16k.wav"), dtype="float32"); assert sr == 16000
emis_path = os.path.join(BASE, rf"asr\work\emis_{WHICH}.npy")
if WHICH == "LV60K":
    bundle = torchaudio.pipelines.WAV2VEC2_ASR_LARGE_LV60K_960H
    labels = bundle.get_labels(); lab = {c: i for i, c in enumerate(labels)}
    to_chars = lambda w: [c for c in w.upper() if c in lab and c not in "-|"]
else:
    bundle = torchaudio.pipelines.MMS_FA
    lab = bundle.get_dict(star=None); labels = list(lab)
    to_chars = lambda w: [c for c in w.lower() if c in lab and c not in "-|"]
print(WHICH, "labels", labels[:6], len(lab), flush=True)
t0 = time.time()
if os.path.exists(emis_path):
    E = np.load(emis_path)
else:
    model = bundle.get_model(with_star=False).to(dev).eval() if WHICH == "MMS" else bundle.get_model().to(dev).eval()
    # file-by-file (no context across the splice), 20 s windows with 2 s context each side
    parts = [(0, int(round(OFF * sr))), (int(round(OFF * sr)), len(x))]
    outs = []
    for a, b in parts:
        seg = x[a:b]; nfr = (len(seg) - 400) // 320 + 1  # nominal frame count
        frames = []
        W, C = 20 * sr, 2 * sr
        pos = 0
        while pos < len(seg):
            s0 = max(0, pos - C); s1 = min(len(seg), pos + W + C)
            wav = torch.from_numpy(seg[s0:s1]).to(dev)[None]
            with torch.inference_mode():
                em, _ = model(wav)
                em = torch.log_softmax(em.float(), dim=-1)[0].cpu().numpy()
            f0 = (pos - s0) // 320; f1 = f0 + (min(pos + W, len(seg)) - pos) // 320
            frames.append(em[f0:f1]); pos += W
        e = np.concatenate(frames)
        # pad/trim to exact frame grid length of this part (frames every 320 samples from part start)
        need = int(np.ceil((b - a) / 320))
        if len(e) < need: e = np.concatenate([e, np.repeat(e[-1:], need - len(e), 0)])
        outs.append(e[:need])
    # map to canonical frame grid: part2 starts at sample cut; cut/320 is not integral -> keep per-part arrays
    np.save(emis_path, np.array(outs, dtype=object), allow_pickle=True)
    E = np.load(emis_path, allow_pickle=True)
    del model; torch.cuda.empty_cache()
E = np.load(emis_path, allow_pickle=True)
print("emissions", [e.shape for e in E], round(time.time() - t0, 1), "s", flush=True)

d = json.load(open(os.path.join(BASE, r"asr\work\crisper_raw.json")))
out = []
FR = 320 / sr
for pi, p in enumerate(d["parts"]):
    em = torch.from_numpy(E[pi].astype(np.float32))
    Tn = em.shape[0]
    Wd = p["words"]
    # segments split at CW gaps > 0.35 s or when longer than 15 s
    segs, cur = [], [0]
    for k in range(1, len(Wd)):
        gap = Wd[k]["start"] - Wd[k - 1]["end"]
        if gap > 0.35 or (Wd[k]["start"] - Wd[cur[0]]["start"] > 15 and gap > 0.05) or Wd[k]["start"] - Wd[cur[0]]["start"] > 25:
            segs.append(cur); cur = [k]
        else: cur.append(k)
    segs.append(cur)
    for si, sg in enumerate(segs):
        ws = [Wd[k] for k in sg]
        prev_end = Wd[segs[si - 1][-1]]["end"] if si > 0 else 0.0
        next_start = Wd[segs[si + 1][0]]["start"] if si + 1 < len(segs) else Tn * FR
        left = max(prev_end + (ws[0]["start"] - prev_end) * 0.5, ws[0]["start"] - 0.8, 0.0)
        right = min(ws[-1]["end"] + (next_start - ws[-1]["end"]) * 0.5, ws[-1]["end"] + 0.8, Tn * FR)
        f0 = int(np.floor(left / FR)); f1 = int(np.ceil(right / FR))
        chars = [to_chars(w["word"]) for w in ws]
        keep = [j for j, c in enumerate(chars) if c]
        tg = [lab[c] for j in keep for c in chars[j]]
        res = {}
        if tg and len(tg) <= (f1 - f0):
            try:
                ali, sc = F.forced_align(em[f0:f1][None], torch.tensor([tg], dtype=torch.int32), blank=0)
                spans = F.merge_tokens(ali[0], sc[0].exp())
                pos = 0
                for j in keep:
                    n = len(chars[j]); sp = spans[pos:pos + n]; pos += n
                    res[j] = ((f0 + sp[0].start) * FR, (f0 + sp[-1].end) * FR,
                              float(np.mean([s.score for s in sp])))
            except Exception as ex:
                print("align fail seg", pi, si, repr(ex), flush=True)
        for j, w in enumerate(ws):
            r = res.get(j)
            out.append({"word": w["word"], "cw_start": w["start"] + p["offset"], "cw_end": w["end"] + p["offset"],
                        "fa_start": None if r is None else r[0] + p["offset"], "fa_end": None if r is None else r[1] + p["offset"],
                        "fa_score": None if r is None else r[2], "seg": f"{pi}:{si}"})
json.dump(out, open(os.path.join(BASE, rf"asr\work\fa_{WHICH}.json"), "w"), indent=0)
print("WROTE", len(out), "missing", sum(o["fa_start"] is None for o in out), round(time.time() - t0, 1), "s", flush=True)
