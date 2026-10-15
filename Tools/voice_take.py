"""Make the narration, CHECK it, and regenerate only when the check fails (best of up to N takes).

  . key.sh && python voice_take.py --script "<Short folder>/script.txt" [--takes 3] [-- <extra voiceover.py args, e.g. --speed 1.15>]

Each take: voiceover.py (new defaults: native speed auto, stability 0.65, similarity 0.7, almost no stretch) -> voice_check.py (free local
speech recognition: every word said? odd pauses, stretched/swallowed words, clipping, cut-off ending) -> voice_quality.py (HNR/jitter/shimmer).
A take PASSES when voice_check has no REDO issue and HNR, jitter and shimmer are inside the profile's gate (voice_config.json hnr_min / jitter_max / shimmer_max; Alex 7.0 / 3.4 / 12.5, the clone 7.6 / 3.4 / 11.5).
The voice and its settings come from voice_config.json (profile "primary" unless you pass -- --voice backup).
It stops at the first passing take (credits: ~1 per character per take); otherwise it keeps the best of N and says why.
Writes voice.mp3, voice_raw.mp3, words.json, captions.srt next to script.txt and voice_take.json (all takes' numbers). Old files go to _voice_prev/.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def run(cmd, cwd=None):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)


def pitch_sd(mp3):
    """Pitch variety in semitones (Praat), the measure the voice auditions used. None if it can't be measured."""
    try:
        import numpy as np, parselmouth, voice_quality as vq
        w = vq.to_wav(mp3)
        try:
            p = parselmouth.Sound(w).to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=400).selected_array["frequency"]
        finally:
            os.remove(w)
        v = p[p > 0]
        return round(float(np.std(12 * np.log2(v / np.median(v)))), 2)
    except Exception:
        return None


def score(chk, q, hnr_min=7.6, jitter_max=3.4, shimmer_max=11.5):
    issues = chk.get("issues", [])
    s = -100 * len(issues) + q["hnr"] - 0.5 * q["jitter"] - 0.2 * q["shimmer"]
    ok = (not issues) and q["hnr"] >= hnr_min and q["jitter"] <= jitter_max and q["shimmer"] <= shimmer_max
    return s, ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--takes", type=int, default=3)
    ap.add_argument("rest", nargs="*")
    a = ap.parse_args()
    import voice_quality as vq
    from voiceover import load_profile
    prof = load_profile(a.rest[a.rest.index("--voice") + 1] if "--voice" in a.rest else None)
    # per voice (Oct 14 audition + first production takes): Alex HNR 7.6-8.7, shimmer 10.6-12.2; the clone HNR 8-10, shimmer 9-11.
    gate = (prof.get("hnr_min", 7.6), prof.get("jitter_max", 3.4), prof.get("shimmer_max", 11.5))
    print(f"voice profile: {prof.get('name', '.env voice')} (gate: HNR >= {gate[0]}, jitter <= {gate[1]}, shimmer <= {gate[2]})")
    folder = os.path.dirname(os.path.abspath(a.script))
    best, log = None, []
    for k in range(1, a.takes + 1):
        tdir = tempfile.mkdtemp(prefix=f"take{k}_", dir=folder)
        try:
            shutil.copy(a.script, os.path.join(tdir, "script.txt"))
            r = run([sys.executable, os.path.join(HERE, "voiceover.py"), "--script", os.path.join(tdir, "script.txt")] + a.rest)
            print(f"take {k}: " + " | ".join(l for l in r.stdout.splitlines() if l.startswith(("auto speed", "Raw pace", "Done"))))
            if r.returncode != 0 or not os.path.exists(os.path.join(tdir, "voice.mp3")):
                print((r.stderr or r.stdout)[-300:]); shutil.rmtree(tdir, ignore_errors=True); continue
            run([sys.executable, os.path.join(HERE, "voice_check.py"), "--folder", tdir, "--stt", "whisper"])
            chk = json.load(open(os.path.join(tdir, "voice_check.json")))
            w = vq.to_wav(os.path.join(tdir, "voice.mp3"))
            try:
                q = vq.measure(w)
            finally:
                os.remove(w)
            s, ok = score(chk, q, *gate)
            # Oct 14 night: reject a flat take. In round 4 one of two "F" takes fell to 3.8 semitones of pitch variety (the other 4.7).
            psd = pitch_sd(os.path.join(tdir, "voice.mp3"))
            q["pitch_sd"] = psd
            if prof.get("pitch_sd_min") and psd is not None and psd < prof["pitch_sd_min"]:
                ok = False; s -= 50
                print(f"  take {k}: flat delivery (pitch variety {psd} < {prof['pitch_sd_min']} semitones)")
            log.append({"take": k, "ok": ok, "score": round(s, 1), "verdict": chk["verdict"], "issues": chk["issues"][:5], "wpm": chk["wpm"], **{x: q.get(x) for x in ("hnr", "jitter", "shimmer", "dur", "pitch_sd")}})
            print(f"  take {k}: {'PASS' if ok else 'FAIL'}  check={chk['verdict']} HNR {q['hnr']} jitter {q['jitter']} shimmer {q['shimmer']} {q['dur']}s  {chk['issues'][:2]}")
            if best is None or s > best[0]:
                if best and os.path.isdir(best[1]): shutil.rmtree(best[1], ignore_errors=True)
                best = (s, tdir, ok)
            else:
                shutil.rmtree(tdir, ignore_errors=True)
            if ok:
                break
        except Exception as e:
            print("take failed:", e); shutil.rmtree(tdir, ignore_errors=True)
    if not best:
        raise SystemExit("no take produced audio")
    prev = os.path.join(folder, "_voice_prev"); os.makedirs(prev, exist_ok=True)
    for f in ("voice.mp3", "voice_raw.mp3", "words.json", "captions.srt"):
        src = os.path.join(folder, f)
        if os.path.exists(src) and not os.path.exists(os.path.join(prev, f)):
            shutil.copy(src, os.path.join(prev, f))
        if os.path.exists(os.path.join(best[1], f)):
            shutil.copy(os.path.join(best[1], f), src)
    shutil.rmtree(best[1], ignore_errors=True)
    json.dump(log, open(os.path.join(folder, "voice_take.json"), "w"), indent=1)
    print("USED take score %.1f (%s)" % (best[0], "passes the voice gate" if best[2] else "STILL FAILS the gate: listen before posting"))


if __name__ == "__main__":
    main()
