"""Record a SPLICED Short's whole narration in ONE take, check it, and cut it into the _nN pieces at the quote joins.

  . key.sh && python voice_pieces.py --folder "<Short folder>" [--takes 3] [--speed auto]

Why (Oct 5 2026 audit): narration recorded as separate 1.5-6 s pieces measured the worst voice quality (HNR 5.7-7.4 vs 8-10 for a full take) and each
piece starts with its own tone, speed and loudness. One continuous take keeps tone/pace consistent; we cut it where a real quote goes.
Reads plan.json ([{"vo":"_n1"}, {"quote":...}, {"vo":"_n2"}, ...]) and each _nN/script.txt ({A|B} respellings work). Writes
_nN/voice.mp3 + voice_raw.mp3 + words.json + captions.srt exactly as voiceover.py did, so splice_voice.py works unchanged. Old files go to _voice_v1/.
Take gate (same as voice_take.py): voice_check has no REDO issue, HNR >= 7.6, jitter <= 3.4, shimmer <= 11.5; up to --takes tries, keeps the best.
"""
import argparse, base64, json, os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voiceover import load_env, call, parse_script, words_from_alignment, map_display, tidy, to_srt, CLEAN  # noqa: E402


def ff(*a):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--takes", type=int, default=3)
    ap.add_argument("--speed", default="auto")
    ap.add_argument("--stability", type=float, default=0.65)
    ap.add_argument("--similarity", type=float, default=0.7)
    ap.add_argument("--model", default="eleven_multilingual_v2")
    ap.add_argument("--min-total", type=float, default=21.5, help="auto speed keeps the finished Short (narration + quotes + gaps) at least this long")
    ap.add_argument("--target-wpm", type=int, default=250)
    ap.add_argument("--max-stretch", type=float, default=1.08)
    ap.add_argument("--clean", choices=["off", "light", "strong"], default="light")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    import voice_quality as vq
    plan = json.load(open(os.path.join(F, "plan.json")))
    vo = [p["vo"] for p in plan if "vo" in p]
    segs = {v: parse_script(open(os.path.join(F, v, "script.txt"), encoding="utf-8-sig").read()) for v in vo}
    spoken = {v: " ".join(s for _, s in segs[v]).strip() for v in vo}
    counts = [len(spoken[v].split()) for v in vo]
    combined = " ".join(spoken[v] for v in vo)
    n_words = sum(counts)
    quote_secs = sum(p["to"] - p["from"] for p in plan if "quote" in p) + 0.12 * (len(plan) - 1)
    env = load_env(); key = env.get("ELEVENLABS_API_KEY", ""); voice = env.get("ELEVENLABS_VOICE_ID", "")
    if not key or not voice:
        raise SystemExit("Missing ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID (source key.sh)")
    if str(a.speed).lower() == "auto":
        est = lambda sp: n_words / (210 + (sp - 1.1) * 580) * 60 + quote_secs
        a.speed = next((sp for sp in (1.2, 1.15) if est(sp) >= a.min_total), 1.1)
        print(f"auto speed -> {a.speed} (about {est(a.speed):.1f} s total: {n_words} narrated words + {quote_secs:.1f} s of quotes/gaps)")
    settings = {"stability": a.stability, "similarity_boost": a.similarity, "use_speaker_boost": True, "speed": max(0.7, min(1.2, float(a.speed)))}
    bk = os.path.join(F, "_voice_v1")
    for v in vo:
        os.makedirs(os.path.join(bk, v), exist_ok=True)
        for f in ("voice.mp3", "voice_raw.mp3", "words.json", "captions.srt"):
            s = os.path.join(F, v, f)
            if os.path.exists(s) and not os.path.exists(os.path.join(bk, v, f)):
                shutil.copy(s, os.path.join(bk, v, f))
    work = os.path.join(F, "_voice_take"); os.makedirs(work, exist_ok=True)
    best, log = None, []
    for k in range(1, a.takes + 1):
        res = call(f"/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128", key,
                   {"text": combined, "model_id": a.model, "voice_settings": settings})
        raw = os.path.join(work, f"raw{k}.mp3"); open(raw, "wb").write(base64.b64decode(res["audio_base64"]))
        words = words_from_alignment(res.get("alignment") or res["normalized_alignment"])
        if len(words) != n_words:
            print(f"take {k}: alignment gave {len(words)} words, expected {n_words}; skipping this take"); continue
        d = words[-1][2]; raw_wpm = len(words) / (d / 60); want = a.target_wpm / raw_wpm
        factor = max(1.0, min(a.max_stretch, want))
        st = os.path.join(work, f"take{k}.mp3")
        ff("-i", raw, "-af", CLEAN[a.clean] + (f"atempo={factor:.3f}," if factor > 1.01 else "") + "apad=pad_dur=0.3", "-c:a", "libmp3lame", "-q:a", "0", st)
        if factor > 1.01:
            words = [(w, s / factor, e / factor) for w, s, e in words]
        else:
            factor = 1.0
        ev = os.path.join(work, f"eval{k}"); os.makedirs(ev, exist_ok=True)
        shutil.copy(st, os.path.join(ev, "voice.mp3"))
        disp = []
        i = 0
        for v, c in zip(vo, counts):
            disp += tidy(map_display(segs[v], words[i:i + c])); i += c
        json.dump([{"word": w, "start": round(s, 3), "end": round(e, 3)} for w, s, e in disp], open(os.path.join(ev, "words.json"), "w"))
        open(os.path.join(ev, "script.txt"), "w", encoding="utf-8").write(" ".join(w for w, _, _ in disp))
        subprocess.run([sys.executable, os.path.join(HERE, "voice_check.py"), "--folder", ev, "--stt", "whisper"], capture_output=True)
        chk = json.load(open(os.path.join(ev, "voice_check.json")))
        wv = vq.to_wav(st)
        try:
            q = vq.measure(wv)
        finally:
            os.remove(wv)
        ok = (not chk["issues"]) and q["hnr"] >= 7.6 and q["jitter"] <= 3.4 and q["shimmer"] <= 11.5
        score = -100 * len(chk["issues"]) + q["hnr"] - 0.5 * q["jitter"] - 0.2 * q["shimmer"]
        log.append({"take": k, "ok": ok, "score": round(score, 1), "raw_wpm": round(raw_wpm), "stretch": round(factor, 2), "issues": chk["issues"][:5], **{x: q[x] for x in ("hnr", "jitter", "shimmer")}})
        print(f"take {k}: {'PASS' if ok else 'FAIL'} raw {raw_wpm:.0f} wpm stretch x{factor:.2f} HNR {q['hnr']} jitter {q['jitter']} shimmer {q['shimmer']} issues {chk['issues'][:2]}", flush=True)
        if best is None or score > best[0]:
            best = (score, k, st, words, factor, ok)
        if ok:
            break
    if not best:
        raise SystemExit("no usable take")
    _, k, st, words, factor, ok = best
    total = dur(st)
    # cut points: tight around the speech of each piece, midpoint when the next piece follows with no real gap
    idx, spans = 0, []
    for c in counts:
        spans.append((words[idx][1], words[idx + c - 1][2])); idx += c
    cuts = []
    for j, (s, e) in enumerate(spans):
        a0 = max(0.0, s - 0.05) if j == 0 else None
        cuts.append([a0, None])
    for j in range(len(spans)):
        s, e = spans[j]
        if j + 1 < len(spans):
            s2 = spans[j + 1][0]; gap = s2 - e
            if gap >= 0.12:
                cuts[j][1] = e + 0.06; cuts[j + 1][0] = s2 - 0.04
            else:
                mid = (e + s2) / 2; cuts[j][1] = mid; cuts[j + 1][0] = mid
        else:
            cuts[j][1] = min(total, e + 0.2)
    idx = 0
    for j, (v, c) in enumerate(zip(vo, counts)):
        a0, b0 = cuts[j]
        out = os.path.join(F, v, "voice.mp3")
        ff("-ss", f"{a0:.3f}", "-to", f"{b0:.3f}", "-i", st, "-af", f"afade=t=in:d=0.008,afade=t=out:st={max(0.0, b0 - a0 - 0.03):.3f}:d=0.03", "-c:a", "libmp3lame", "-q:a", "0", out)
        shutil.copy(out, os.path.join(F, v, "voice_raw.mp3"))
        wl = [(w, s - a0, e - a0) for w, s, e in words[idx:idx + c]]; idx += c
        pw = tidy(map_display(segs[v], wl))
        json.dump([{"word": w, "start": round(s, 3), "end": round(e, 3)} for w, s, e in pw], open(os.path.join(F, v, "words.json"), "w"), indent=1)
        open(os.path.join(F, v, "captions.srt"), "w", encoding="utf-8").write(to_srt(pw))
    json.dump(log, open(os.path.join(F, "voice_take.json"), "w"), indent=1)
    shutil.rmtree(work, ignore_errors=True)
    print(f"USED take {k} ({'passes the voice gate' if ok else 'STILL FAILS the gate: listen before posting'}); pieces: " + ", ".join(f"{v} {cuts[j][1] - cuts[j][0]:.1f}s" for j, v in enumerate(vo)))


if __name__ == "__main__":
    main()
