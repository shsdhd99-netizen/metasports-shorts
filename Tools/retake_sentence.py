"""Re-record ONE sentence of a finished voice and splice it in, instead of paying for a whole new take (Oct 24, 2026).

  python Tools/retake_sentence.py --folder F --at 0.35              # the sentence holding this time (a voice_check issue's time)
  python Tools/retake_sentence.py --folder F --sentence 3           # 1-based sentence of script.txt
  python Tools/retake_sentence.py --folder F --at 0.35 --at 14.2 -- --voice backup   # several; extra args go to voiceover.py

Why: take 1 often garbles one name or drops "Back" (#66 take 1: only "Gilgeous-Alexander" was bad), and voice_take.py then
re-recorded all ~550 characters. ElevenLabs bills only the text it reads, so one sentence costs 5-10% of a take. The sentence is
read with the same voice profile (voiceover.py) and with previous_text / next_text, so its pitch and pace carry on from the
neighbours. Cut points sit at the quietest 10 ms of the silence before and after the sentence (30 ms margins when there is no
silence); the new piece keeps the old lead-in and tail lengths, gets the old span's speech loudness and joins with 4 ms fades.
Rewrites voice.mp3, words.json and captions.srt (originals in _voice_preretake/); voice_raw.mp3 is left as the original take.
Works on whichever voice.mp3 is in the folder (a fresh take or a tightened one). Check the result with voice_check.py.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tighten_voice import dur, srt  # noqa: E402
from voiceover import parse_script  # noqa: E402

SR, HOP = 44100, 0.005
norm = lambda w: re.sub(r"[^a-z0-9$%']", "", w.lower())


def sentences(raw):
    """Split a script on . ? ! followed by a space (or the end), never inside {display|spoken} markup."""
    raw, out, cur, depth = re.sub(r"\s+", " ", raw.strip()), [], "", 0
    for i, ch in enumerate(raw):
        cur += ch
        depth += (ch == "{") - (ch == "}")
        if depth == 0 and ch in ".?!" and (i + 1 == len(raw) or raw[i + 1] == " "):
            out.append(cur.strip()); cur = ""
    if cur.strip():
        out.append(cur.strip())
    return out


def spoken(s):
    return " ".join(x for _, x in parse_script(s)).strip()


def pcm(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def env_db(x):
    n = int(HOP * SR)
    k = len(x) // n
    return 20 * np.log10(np.sqrt((x[:k * n].reshape(k, n) ** 2).mean(1)) + 1e-9)


def quietest(env, a, b, win=2):
    """Centre (s) of the quietest win x 5 ms stretch between a and b seconds."""
    i0, i1 = max(0, int(a / HOP)), min(len(env) - win, int(b / HOP))
    if i1 <= i0:
        return (a + b) / 2
    sm = np.convolve(env, np.ones(win) / win, "valid")
    i = i0 + int(np.argmin(sm[i0:i1]))
    return (i + win / 2) * HOP


def sound_edges(env, a, b):
    """First and last 5 ms frame between a and b seconds that is within 35 dB of the file's loud speech: where the sound starts and stops."""
    thr = np.percentile(env, 95) - 35
    i0, i1 = int(a / HOP), min(len(env), int(b / HOP))
    loud = [i for i in range(i0, i1) if env[i] > thr]
    return (loud[0] * HOP, (loud[-1] + 1) * HOP) if loud else (a, b)


def voiced_rms(x):
    e = env_db(x)
    v = e[e > -40]
    return 10 * np.log10(np.mean(10 ** (v / 10))) if len(v) else -60.0


def locate(words, sents):
    """[(first word index, last word index)] of every sentence in words.json (token match, in order)."""
    toks, own = [], []
    for i, w in enumerate(words):
        for t in w["word"].split():
            if norm(t):
                toks.append(norm(t)); own.append(i)
    spans, pos = [], 0
    for s in sents:
        want = [norm(t) for t in " ".join(d for d, _ in parse_script(s)).split() if norm(t)]
        for k in range(pos, len(toks) - len(want) + 1):
            if toks[k:k + len(want)] == want:
                spans.append((own[k], own[k + len(want) - 1])); pos = k + len(want); break
        else:
            raise SystemExit(f"sentence not found in words.json: {s[:60]}")
    return spans


def retake(F, idx, sents, spans, rest):
    """Re-record sentence idx (0-based) and splice it into F/voice.mp3. Returns characters billed."""
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8-sig"))
    i0, i1 = spans[idx]
    vp = os.path.join(F, "voice.mp3")
    total, x = dur(vp), pcm(vp)
    env = env_db(x)
    s0, s1 = words[i0]["start"], words[i1]["end"]
    pe = words[i0 - 1]["end"] if i0 > 0 else None
    ns = words[i1 + 1]["start"] if i1 + 1 < len(words) else None
    A = 0.0 if pe is None else (quietest(env, pe - 0.02, s0 + 0.02) if s0 - pe > 0.04 else s0 - 0.03)
    B = total if ns is None else (quietest(env, s1 - 0.02, ns + 0.02) if ns - s1 > 0.04 else s1 + 0.03)
    # lead-in / tail measured to the real sound edges (TTS word times sit tens of ms off the sound; on the first test the
    # alignment-based trim added a 0.12 s gap)
    on, off = sound_edges(env, A, B)
    lead, tail = max(0.0, on - A), max(0.0, B - off)
    # the piece: same voice profile, the neighbours as context so the tone carries on
    tmp = tempfile.mkdtemp(prefix="retake_", dir=F)
    try:
        open(os.path.join(tmp, "script.txt"), "w", encoding="utf-8").write(sents[idx])
        prev = " ".join(spoken(s) for s in sents[max(0, idx - 2):idx])
        nxt = spoken(sents[idx + 1]) if idx + 1 < len(sents) else ""
        r = subprocess.run([sys.executable, os.path.join(HERE, "voiceover.py"), "--script", os.path.join(tmp, "script.txt"),
                            "--prev-text", prev, "--next-text", nxt, "--min-secs", "0"] + rest, capture_output=True, text=True)
        piece = os.path.join(tmp, "voice.mp3")
        if r.returncode or not os.path.exists(piece):
            raise SystemExit("voiceover.py failed: " + (r.stderr or r.stdout)[-300:])
        pw = json.load(open(os.path.join(tmp, "words.json"), encoding="utf-8"))
        pdur, px = dur(piece), pcm(piece)
        p_on, p_off = sound_edges(env_db(px), 0.0, pdur)
        pad = max(0.0, lead - p_on)  # the piece has less lead-in than the old span: add silence in front
        pa, pb = max(0.0, p_on - lead), min(pdur, p_off + tail)
        gain = float(np.clip(voiced_rms(x[int(A * SR):int(B * SR)]) - voiced_rms(px[int(pa * SR):int(pb * SR)]), -6, 6))
        ch = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=sample_rate,channels",
                             "-of", "csv=p=0", vp], capture_output=True, text=True).stdout.strip().split(",")
        fmt = f"aformat=sample_rates={ch[0]}:channel_layouts={'mono' if ch[1] == '1' else 'stereo'}"
        f = 0.004
        parts, labels = [], []
        if A > 0.001:
            parts.append(f"[0:a]atrim=0:{A:.4f},asetpts=PTS-STARTPTS,{fmt},afade=t=out:st={max(0, A - f):.4f}:d={f}[a]"); labels.append("[a]")
        parts.append(f"[1:a]atrim={pa:.4f}:{pb:.4f},asetpts=PTS-STARTPTS,{fmt},volume={gain:.2f}dB,afade=t=in:d={f},"
                     f"afade=t=out:st={max(0, pb - pa - f):.4f}:d={f}" + (f",adelay=delays={pad * 1000:.0f}:all=1" if pad > 0.001 else "")
                     + "[b]"); labels.append("[b]")
        if B < total - 0.001:
            parts.append(f"[0:a]atrim={B:.4f},asetpts=PTS-STARTPTS,{fmt},afade=t=in:d={f}[c]"); labels.append("[c]")
        out = os.path.join(tmp, "spliced.mp3")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vp, "-i", piece, "-filter_complex",
                        ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(labels)}:v=0:a=1[o]", "-map", "[o]",
                        "-c:a", "libmp3lame", "-q:a", "0", out], check=True)
        shift = (pb - pa + pad) - (B - A)
        new = [w for w in words[:i0]]
        new += [{"word": w["word"], "start": round(max(w["start"], pa) - pa + pad + A, 3), "end": round(min(w["end"], pb) - pa + pad + A, 3)} for w in pw]
        new += [{"word": w["word"], "start": round(w["start"] + shift, 3), "end": round(w["end"] + shift, 3)} for w in words[i1 + 1:]]
        bk = os.path.join(F, "_voice_preretake")
        if not os.path.exists(bk):
            os.makedirs(bk)
            for n in ("voice.mp3", "words.json", "captions.srt"):
                if os.path.exists(os.path.join(F, n)):
                    shutil.copy2(os.path.join(F, n), bk)
        shutil.move(out, vp)
        json.dump(new, open(os.path.join(F, "words.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        srt(new, os.path.join(F, "captions.srt"))
        billed = len(spoken(sents[idx]))
        print(f"sentence {idx + 1} re-recorded ({billed} characters billed): \"{sents[idx][:60]}\" "
              f"{B - A:.2f}s -> {pb - pa + pad:.2f}s, gain {gain:+.1f} dB, cuts at {A:.2f}s and {B:.2f}s")
        return billed
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--at", type=float, action="append", default=[], help="a time (s) inside the sentence to redo")
    ap.add_argument("--sentence", type=int, action="append", default=[], help="1-based sentence number in script.txt")
    ap.add_argument("rest", nargs="*", help="extra voiceover.py arguments (after --), e.g. --voice backup")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    sents = sentences(open(os.path.join(F, "script.txt"), encoding="utf-8-sig").read())
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8-sig"))
    spans = locate(words, sents)
    want = {n - 1 for n in a.sentence}
    starts = [words[i0]["start"] for i0, _ in spans]
    for t in a.at:  # sentence k runs from its first word to the next sentence's first word
        want.add(max([k for k, s in enumerate(starts) if s <= t + 0.02] or [0]))
    if not want:
        raise SystemExit("give --at or --sentence")
    billed = 0
    for k in sorted(want, reverse=True):  # last first, so earlier sentences keep their times
        billed += retake(F, k, sents, locate(json.load(open(os.path.join(F, "words.json"), encoding="utf-8")), sents), a.rest)
    print(f"done: {billed} characters billed (a whole take is {sum(len(spoken(s)) for s in sents) + len(sents) - 1}). "
          "Check it: python Tools/voice_check.py --folder <folder> --stt whisper")


if __name__ == "__main__":
    main()
