"""Cut or swap words in a finished voice track, using only the same voice's own audio (no new TTS, no credits).

  python Tools/word_edit.py --folder F --edit 13.665-14.275=59.49-59.845   # replace "William Hill" with "Bookmakers" from 59.49 s
  python Tools/word_edit.py --folder F --edit 61.20-61.31                  # cut a word out ("the")

For a fact fix when re-voicing is not possible (Oct 23 2026: no ElevenLabs key on the new account). Each --edit is a span
A-B of the voice (seconds) to remove, optionally =C-D: a span of the same voice to put in its place. Put every cut point in
a silence or a stop closure (the dip before k/g/t/d/p/b): print the loudness envelope around the words first and pick the
lowest 10 ms. Words whose middle falls inside A-B are dropped; the words inside C-D are copied in with their own timings.
Each joint gets a 4 ms fade (--fade), so there is no click. Rewrites voice.mp3, words.json and captions.srt; the originals go to
_voice_preedit/. Then fix script.txt by hand (QA checks the captions against it), and re-run cut_list.py and assemble.py.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tighten_voice import dur, srt  # noqa: E402


def mid(w):
    return (w["start"] + w["end"]) / 2


def parse(e):
    cut, _, src = e.partition("=")
    a, b = (float(x) for x in cut.split("-"))
    return (a, b, tuple(float(x) for x in src.split("-")) if src else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--edit", action="append", required=True, help="A-B to remove, or A-B=C-D to replace with C-D (seconds)")
    ap.add_argument("--fade", type=float, default=0.004, help="fade at each joint, s (longer when a piece ends inside a vowel)")
    a = ap.parse_args()
    F = a.folder
    vp, wp = os.path.join(F, "voice.mp3"), os.path.join(F, "words.json")
    words = json.load(open(wp, encoding="utf-8-sig"))
    edits = sorted(parse(e) for e in a.edit)
    for (a1, b1, _), (a2, _, _) in zip(edits, edits[1:]):
        if a2 < b1:
            raise SystemExit("edits overlap")
    bk = os.path.join(F, "_voice_preedit")
    if not os.path.exists(bk):
        os.makedirs(bk)
        for f in ("voice.mp3", "words.json", "captions.srt"):
            if os.path.exists(os.path.join(F, f)):
                shutil.copy2(os.path.join(F, f), bk)
    total = dur(vp)
    # the new timeline: (source start, source end) pieces in order
    pieces, t = [], 0.0
    for x, y, src in edits:
        pieces.append((t, x))
        if src:
            pieces.append(src)
        t = y
    pieces.append((t, total))
    parts, new_words, pos = [], [], 0.0
    for k, (s, e) in enumerate(pieces):
        fade = (f",afade=t=in:d={a.fade}" if k else "") + (f",afade=t=out:st={max(0, e - s - a.fade):.4f}:d={a.fade}" if k < len(pieces) - 1 else "")
        parts.append(f"[0:a]atrim=start={s:.4f}:end={e:.4f},asetpts=PTS-STARTPTS{fade}[s{k}]")
        for w in words:
            if s <= mid(w) < e:  # TTS word timings overlap the real sound by a few ms, so place a word by its middle
                new_words.append({"word": w["word"], "start": round(max(w["start"], s) - s + pos, 3), "end": round(min(w["end"], e) - s + pos, 3)})
        pos += e - s
    fc = ";".join(parts) + ";" + "".join(f"[s{k}]" for k in range(len(pieces))) + f"concat=n={len(pieces)}:v=0:a=1[out]"
    tmp = os.path.join(tempfile.mkdtemp(), "voice.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vp, "-filter_complex", fc, "-map", "[out]", "-c:a", "libmp3lame", "-q:a", "0", tmp], check=True)
    shutil.move(tmp, vp)
    json.dump(new_words, open(wp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    srt(new_words, os.path.join(F, "captions.srt"))
    dropped = [w["word"] for w in words if any(x <= mid(w) < y for x, y, _ in edits)]
    added = [w["word"] for w in words if any(src and src[0] <= mid(w) < src[1] for _, _, src in edits)]
    print(f"{os.path.basename(F)}: {total:.2f}s -> {dur(vp):.2f}s. Dropped {dropped}, put in {added}. Originals in _voice_preedit/. "
          "Fix script.txt, then re-run cut_list.py and assemble.py.")


if __name__ == "__main__":
    main()
