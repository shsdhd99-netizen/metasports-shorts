"""Build voice.mp3 + words.json from narration pieces and real quote cuts (real audio from a clip).

  python splice_voice.py --folder "<Short folder>" --plan plan.json [--stt-dir <dir>]
plan.json: [{"vo": "_n1"},                                   # folder with voice.mp3 + words.json from voiceover.py
            {"quote": "clips/adams_full.mp4", "stt": "adams_stt.json", "from": 13.26, "to": 17.0, "text": "optional true words", "stt_offset": 0},
            {"vo": "_n2"}, ...]
Writes voice.mp3, words.json (all word times on the final timeline) and _timeline.json (start of each piece, for shots.json).
Each piece is gain-matched (plain volume, no dynamic loudnorm) to -18 LUFS, 0.12 s gap between pieces. Quote words come from ElevenLabs STT json (scribe).
"""
import argparse, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

GAP = 0.12


def run(*a):
    subprocess.run(a, check=True, capture_output=True)


def lufs(*inp):
    """Integrated loudness of an input (ffmpeg input args), so a plain gain can be applied. loudnorm's dynamic mode ducked the last
    0.25 s of short pieces by 1-4 dB (Oct 5 2026 audit), which made sentence ends sound swallowed."""
    import re
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *inp, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else None


LIM = "alimiter=limit=0.794:attack=3:release=50:level=disabled"


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--plan", required=True)
    a = ap.parse_args()
    F = a.folder
    plan = json.load(open(a.plan))
    parts, words, tl, t = [], [], [], 0.0
    os.makedirs(os.path.join(F, "_splice"), exist_ok=True)
    for i, p in enumerate(plan):
        out = os.path.join(F, "_splice", f"p{i}.wav")
        if "vo" in p:
            src = os.path.join(F, p["vo"], "voice.mp3")
            L = lufs("-i", src)
            g = (-18 - L) if L is not None and L > -70 else 0.0
            run("ffmpeg", "-y", "-i", src, "-af", f"volume={g:.2f}dB,{LIM}", "-ar", "44100", "-ac", "1", out)
            ws = json.load(open(os.path.join(F, p["vo"], "words.json")))
            for w in ws:
                words.append({"word": w["word"], "start": round(t + w["start"], 3), "end": round(t + w["end"], 3)})
            kind = "vo"
        else:
            src = p["quote"] if os.path.isabs(p["quote"]) else os.path.join(F, p["quote"])
            f, to = p["from"], p["to"]
            L = lufs("-ss", str(f), "-t", str(to - f), "-i", src)
            g = (-16 - L) if L is not None and L > -70 else 0.0
            run("ffmpeg", "-y", "-ss", str(f), "-t", str(to - f), "-i", src, "-af", f"volume={g:.2f}dB,{LIM},afade=t=in:d=0.02,afade=t=out:st=%.2f:d=0.04" % (to - f - 0.04), "-ar", "44100", "-ac", "1", out)
            off = p.get("stt_offset", 0.0)  # when the stt json was made from a clip cut that started at `off` seconds
            d = json.load(open(p["stt"]))
            got = []
            for w in d.get("words", d):
                if w.get("type", "word") != "word":
                    continue
                ws_, we_ = w["start"] + off, w["end"] + off
                if ws_ >= f - 0.02 and we_ <= to + 0.1:
                    got.append({"word": w["text"], "start": ws_, "end": min(we_, to)})
            if p.get("text"):  # the transcript misheard (names!): use the true words, spread over the same span
                tw = p["text"].split()
                a0, a1 = (got[0]["start"], got[-1]["end"]) if got else (f, to)
                step = (a1 - a0) / len(tw)
                got = [{"word": x, "start": a0 + i * step, "end": a0 + (i + 1) * step} for i, x in enumerate(tw)]
            for w in got:
                words.append({"word": w["word"], "start": round(t + w["start"] - f, 3), "end": round(t + w["end"] - f, 3)})
            kind = "quote"
        d = dur(out)
        tl.append({"i": i, "kind": kind, "start": round(t, 3), "end": round(t + d, 3), "src": p.get("vo") or p.get("quote"), "src_from": p.get("from")})
        parts.append(out)
        t += d + GAP
    lst = os.path.join(F, "_splice", "list.txt")
    with open(lst, "w") as fh:
        for i, p in enumerate(parts):
            fh.write(f"file '{os.path.abspath(p)}'\n")
            if i < len(parts) - 1:
                gp = os.path.join(F, "_splice", "gap.wav")
                run("ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", str(GAP), gp)
                fh.write(f"file '{os.path.abspath(gp)}'\n")
    run("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-af", "apad=pad_dur=0.3", "-c:a", "libmp3lame", "-q:a", "0", os.path.join(F, "voice.mp3"))
    json.dump(words, open(os.path.join(F, "words.json"), "w"), indent=1)
    json.dump(tl, open(os.path.join(F, "_timeline.json"), "w"), indent=1)
    try:
        import voiceover
        open(os.path.join(F, "captions.srt"), "w", encoding="utf-8").write(voiceover.to_srt([(w["word"], w["start"], w["end"]) for w in words]))
    except Exception as e:
        print("captions.srt not written:", e)
    open(os.path.join(F, "script.txt"), "w", encoding="utf-8").write(" ".join(w["word"] for w in words))
    print("total", round(t - GAP, 2), "s;", len(words), "words")
    for x in tl:
        print(x)


main()
