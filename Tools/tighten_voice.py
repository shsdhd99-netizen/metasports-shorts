"""Take the dead air out of a finished voice track (owner, Oct 22 2026: "make sure videos have no unnecessary pauses").

  python Tools/tighten_voice.py --folder F                      # every pause over 0.09 s -> 0.06 s, tail -> 0.25 s
  python Tools/tighten_voice.py --folder F --end-after "notepad." # also cut everything after that word (drop an outro)

voiceover.py already trims pauses to the profile's max_pause (0.38 s). This goes further for the story format: every silence
longer than --thresh (measured on the audio, ffmpeg silencedetect at --db) is cut down to --keep. Cuts happen only inside silence.
Rewrites voice.mp3, words.json and captions.srt; the originals go to _voice_pretighten/. Then re-run cut_list.py (or
anchor_shots.py) and assemble.py: shot starts come from words.json.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import voice_fx  # noqa: E402


def silences(path, db=-38.0, min_len=0.09):
    """Silent stretches of the audio itself (ffmpeg silencedetect): word timings from the TTS often swallow the pauses."""
    err = subprocess.run(["ffmpeg", "-i", path, "-af", f"silencedetect=n={db}dB:d={min_len}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    return list(zip(st, en + [dur(path)] * (len(st) - len(en))))


def cut_silences(src, words, out, keep, thresh, db):
    """Shorten every silence longer than thresh to keep (a little before the next word, a little after the last)."""
    total = dur(src)
    runs = [(a, b) for a, b in silences(src, db, thresh) if a > 0.05 and b < total - 0.05]
    keeps, t0, shift, removed = [], 0.0, [], 0.0
    for a, b in runs:
        ca, cb = a + keep * 0.45, b - keep * 0.55
        if cb - ca < 0.02:
            continue
        keeps.append((t0, ca)); t0 = cb
        shift.append((ca, cb)); removed += cb - ca
    keeps.append((t0, None))
    parts = []
    for k, (x, y) in enumerate(keeps):
        trim = f"atrim=start={x:.4f}" + (f":end={y:.4f}" if y is not None else "")
        parts.append(f"[0:a]{trim},asetpts=PTS-STARTPTS" + (",afade=t=in:d=0.004" if k else "") + f"[s{k}]")
    fc = ";".join(parts) + ";" + "".join(f"[s{k}]" for k in range(len(keeps))) + f"concat=n={len(keeps)}:v=0:a=1[out]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[out]", "-c:a", "libmp3lame", "-q:a", "0", out], check=True)

    def m(t):
        r = 0.0
        for ca, cb in shift:
            if t >= cb:
                r += cb - ca
            elif t > ca:  # inside a cut: clamp to the cut point
                return ca - r
        return t - r
    return [(w, m(s), m(e)) for w, s, e in words], removed


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)


def srt(words, path, per=3):
    def ts(t):
        h, r = divmod(t, 3600); m, s = divmod(r, 60)
        return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")
    out = []
    for k in range(0, len(words), per):
        g = words[k:k + per]
        out.append(f"{len(out) + 1}\n{ts(g[0]['start'])} --> {ts(g[-1]['end'])}\n{' '.join(w['word'] for w in g)}\n")
    open(path, "w", encoding="utf-8").write("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--keep", type=float, default=0.06, help="pause left between words, s")
    ap.add_argument("--thresh", type=float, default=0.09, help="only pauses longer than this are cut, s")
    ap.add_argument("--tail", type=float, default=0.25, help="silence kept after the last word, s")
    ap.add_argument("--end-after", help="cut the voice after the LAST occurrence of this word (e.g. drop a promo outro)")
    ap.add_argument("--db", type=float, default=-38.0, help="silence level for the audio-based cut, dBFS")
    a = ap.parse_args()
    F = a.folder
    vp, wp = os.path.join(F, "voice.mp3"), os.path.join(F, "words.json")
    words = json.load(open(wp, encoding="utf-8-sig"))
    bk = os.path.join(F, "_voice_pretighten")
    if not os.path.exists(bk):
        os.makedirs(bk)
        for f in ("voice.mp3", "words.json", "captions.srt"):
            if os.path.exists(os.path.join(F, f)):
                shutil.copy2(os.path.join(F, f), bk)
    before = dur(vp)
    tmp = tempfile.mkdtemp()
    src = vp
    if a.end_after:
        idx = max(i for i, w in enumerate(words) if w["word"].strip().lower() == a.end_after.strip().lower())
        words = words[:idx + 1]
        cut = os.path.join(tmp, "cut.mp3")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vp, "-t", f"{words[-1]['end'] + 0.6:.3f}", "-c:a", "libmp3lame", "-q:a", "0", cut], check=True)
        src = cut
    tight = os.path.join(tmp, "tight.mp3")
    nw, removed = cut_silences(src, [(w["word"], w["start"], w["end"]) for w in words], tight, a.keep, a.thresh, a.db)
    words = [{"word": w, "start": round(s, 3), "end": round(e, 3)} for w, s, e in nw]
    # the tail: where the speech really stops, not the last word's timing (TTS timings often run past the audio, and a
    # breath or click at the very end can keep the last silence from touching the end of the file)
    last_sound = next((x for x, y in silences(tight, a.db, 0.15) if x > words[-1]["start"]), dur(tight))
    end = min(words[-1]["end"], last_sound) + a.tail
    words[-1]["end"] = round(min(words[-1]["end"], last_sound + 0.03), 3)  # the word ends where its sound ends (QA wants a real tail)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tight, "-t", f"{end:.3f}", "-af", f"afade=t=out:st={max(0, end - 0.08):.3f}:d=0.08",
                    "-c:a", "libmp3lame", "-q:a", "0", vp], check=True)
    json.dump(words, open(wp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    srt(words, os.path.join(F, "captions.srt"))
    print(f"{os.path.basename(F)}: {before:.2f}s -> {dur(vp):.2f}s ({removed:.2f}s of pauses removed, tail {a.tail}s"
          + (f", cut after '{a.end_after}'" if a.end_after else "") + "). Originals in _voice_pretighten/. Re-run cut_list.py, then assemble.py.")
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
