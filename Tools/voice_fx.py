"""Voice post-processing that raises pace WITHOUT time-stretching (stretching is what made the voice sound artificial).

tighten_gaps(in_audio, words, out_audio, keep=0.10, thresh=0.22):
    Where a pause is longer than `thresh` seconds, cut it down to `keep` seconds (a jump-cut, like a human editor does).
    words = [(word, start, end), ...] on in_audio's timeline, or None. Returns (new_words, seconds_removed). Pitch and tone are untouched.

    Oct 13 2026 fix (VERIFIED defect): the first version cut wherever the TTS alignment said there was a gap. The alignment's
    word ends can be early, so the cut removed real speech: in the Oct 5 lab, whisper heard '198' as '190' (charlie_v3_tight)
    and '198. 11' as '1-9-11' (liam_v3_tight), while the untrimmed takes read '198' correctly.
    Now a cut is made ONLY inside audio that is actually silent (frame level below the take's speech level minus `floor_db`),
    so a wrong timestamp can shorten a pause but can never remove a syllable.
    Typical effect: expressive models (eleven_v3, ~110-130 wpm) gain 15-30% pace and keep natural sentence pauses.
CLI test:  python voice_fx.py in.mp3 out.mp3 [words.json]
"""
import json, subprocess, sys

import numpy as np

HOP = 0.01  # analysis frame, seconds


def _levels(in_audio, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", in_audio, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
    n = int(sr * HOP)
    frames = len(x) // n
    rms = np.sqrt((x[:frames * n].reshape(frames, n) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(rms)


def silent_runs(db, floor_db=32.0, min_len=0.0):
    """[(start_s, end_s)] of runs quieter than (95th-percentile level - floor_db)."""
    thr = np.percentile(db, 95) - floor_db
    quiet = db < thr
    runs, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if (j - i) * HOP >= min_len:
                runs.append((i * HOP, j * HOP))
            i = j
        else:
            i += 1
    return runs


def tighten_gaps(in_audio, words, out_audio, keep=0.10, thresh=0.22, extra_filter="", floor_db=32.0):
    db = _levels(in_audio)
    total = len(db) * HOP
    runs = [r for r in silent_runs(db, floor_db, min_len=thresh) if r[0] > 0.05 and r[1] < total - 0.05]  # never touch lead-in/tail
    if words:  # only pauses that sit between two words (ignore breaths inside a word's span)
        bounds = [(words[i][2], words[i + 1][1]) for i in range(len(words) - 1)]
        runs = [r for r in runs if any(r[0] < s + 0.08 and r[1] > e - 0.08 for e, s in bounds)]
    keeps, removed, t0, shift = [], 0.0, 0.0, []
    for a, b in runs:
        cut_a, cut_b = a + keep / 2, b - keep / 2
        if cut_b - cut_a < 0.02:
            continue
        keeps.append((t0, cut_a)); t0 = cut_b
        removed += cut_b - cut_a; shift.append((cut_b, removed))
    keeps.append((t0, None))
    parts = []
    for k, (a, b) in enumerate(keeps):
        trim = f"atrim=start={a:.4f}" + (f":end={b:.4f}" if b is not None else "")
        fade = ",afade=t=in:d=0.004" if k else ""  # tiny fade so a join inside silence can never click
        parts.append(f"[0:a]{trim},asetpts=PTS-STARTPTS{fade}[s{k}]")
    cc = "".join(f"[s{k}]" for k in range(len(keeps)))
    fc = ";".join(parts) + f";{cc}concat=n={len(keeps)}:v=0:a=1[out]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", in_audio, "-filter_complex", fc, "-map", "[out]"]
    if extra_filter:
        cmd += ["-af", extra_filter]
    subprocess.run(cmd + ["-c:a", "libmp3lame", "-q:a", "0", out_audio], check=True)

    def new_t(t):
        r = 0.0
        for boundary, cum in shift:
            if t >= boundary - 1e-6:
                r = cum
            else:
                break
        return t - r
    return [(w, new_t(s), new_t(e)) for w, s, e in (words or [])], removed


if __name__ == "__main__":
    ws = [(w["word"], w["start"], w["end"]) for w in json.load(open(sys.argv[3]))] if len(sys.argv) > 3 else None
    nw, rem = tighten_gaps(sys.argv[1], ws, sys.argv[2])
    print(f"removed {rem:.2f} s of pauses; {len(nw)} words")
