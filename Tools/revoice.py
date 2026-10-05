"""Re-record an existing Short's narration with the checked voice pipeline, then re-time the pictures to the new words and re-render.

  . key.sh && python revoice.py --folder "<Short folder>" [--takes 3] [--caption-style metasports] [--no-render]

1. backs up voice files to _voice_v1/ (voice.mp3, voice_raw.mp3, words.json, captions.srt, plan.json, shots.json)
2. single-voice Short: voice_take.py on script.txt. Spliced Short (plan.json): voice_take.py on each _nN/script.txt (with the neighbouring text as
   context so tone stays continuous), then splice_voice.py with the same plan (real quotes untouched, plain gain match instead of loudnorm)
3. anchor_shots.py re-times every picture to the words it illustrates (needs "anchor" in shots.json; all queued Shorts have them)
4. assemble.py (captions only, no headline) -> qa_short.py --infer-kinds -> voice_check.py on the final voice -> hub_pack.sh
Credits: about 1 per character per take. Prints a short summary; exits non-zero if QA fails.
"""
import argparse, json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def sh(cmd, **kw):
    return subprocess.run(cmd, text=True, capture_output=True, **kw)


def piece_text(F, p):
    if "vo" in p:
        sp = os.path.join(F, p["vo"], "script.txt")
        return open(sp, encoding="utf-8-sig").read() if os.path.exists(sp) else ""
    if p.get("text"):
        return p["text"]
    try:
        d = json.load(open(p["stt"]))
        return " ".join(w["text"] for w in d.get("words", d) if w.get("type", "word") == "word" and p["from"] - 0.05 <= w["start"] + p.get("stt_offset", 0) <= p["to"] + 0.05)
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--takes", type=int, default=3)
    ap.add_argument("--caption-style", default="metasports")
    ap.add_argument("--no-render", action="store_true")
    ap.add_argument("--speed", default="auto")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    bk = os.path.join(F, "_voice_v1"); os.makedirs(bk, exist_ok=True)
    for f in ("voice.mp3", "voice_raw.mp3", "words.json", "captions.srt", "plan.json", "shots.json", "_timeline.json"):
        if os.path.exists(os.path.join(F, f)) and not os.path.exists(os.path.join(bk, f)):
            shutil.copy(os.path.join(F, f), os.path.join(bk, f))
    plan_path = os.path.join(F, "plan.json")
    extra = ["--speed", str(a.speed)]
    if os.path.exists(plan_path):
        plan = json.load(open(plan_path))
        for i, p in enumerate(plan):
            if "vo" not in p:
                continue
            prev = piece_text(F, plan[i - 1])[-200:] if i > 0 else ""
            nxt = piece_text(F, plan[i + 1])[:200] if i + 1 < len(plan) else ""
            cmd = [PY, os.path.join(HERE, "voice_take.py"), "--script", os.path.join(F, p["vo"], "script.txt"), "--takes", str(a.takes), "--"] + extra
            if prev.strip(): cmd += ["--prev-text", prev.strip()]
            if nxt.strip(): cmd += ["--next-text", nxt.strip()]
            r = sh(cmd); print(f"[{p['vo']}] " + (r.stdout.strip().splitlines() or [""])[-1]); 
            if r.returncode: print(r.stderr[-300:]); sys.exit(1)
        r = sh([PY, os.path.join(HERE, "splice_voice.py"), "--folder", F, "--plan", plan_path]); print(r.stdout.strip().splitlines()[0] if r.stdout else r.stderr[-300:])
        if r.returncode: sys.exit(1)
    else:
        cmd = [PY, os.path.join(HERE, "voice_take.py"), "--script", os.path.join(F, "script.txt"), "--takes", str(a.takes), "--"] + extra
        r = sh(cmd); print(r.stdout.strip()); 
        if r.returncode: print(r.stderr[-300:]); sys.exit(1)
    r = sh([PY, os.path.join(HERE, "anchor_shots.py"), "--folder", F]); print((r.stdout.strip().splitlines() or [r.stderr[-200:]])[-1])
    if r.returncode: print(r.stderr[-400:]); sys.exit(1)
    if a.no_render:
        return
    r = sh([PY, os.path.join(HERE, "assemble.py"), "--folder", F, "--caption-style", a.caption_style]); print((r.stdout.strip().splitlines() or [""])[-1])
    r = sh([PY, os.path.join(HERE, "qa_short.py"), "--folder", F, "--infer-kinds"]); print("\n".join(l for l in r.stdout.splitlines() if l.startswith(("PASS", "FAIL", "  FAIL", "  warn", "  WARN"))))
    sh([PY, os.path.join(HERE, "voice_check.py"), "--folder", F, "--stt", "whisper"])
    sh(["bash", os.path.join(HERE, "hub_pack.sh"), F])
    sys.exit(0 if "PASS" in r.stdout.split("\n")[0:3].__str__() or "FAIL" not in r.stdout else 2)


if __name__ == "__main__":
    main()
