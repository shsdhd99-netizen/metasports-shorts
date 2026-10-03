"""Build voice.mp3 + words.json from narration pieces and real quote cuts (real audio from a clip).

  python splice_voice.py --folder "<Short folder>" --plan plan.json [--stt-dir <dir>]
plan.json: [{"vo": "_n1"},                                   # folder with voice.mp3 + words.json from voiceover.py
            {"quote": "clips/adams_full.mp4", "stt": "adams_stt.json", "from": 13.26, "to": 17.0},
            {"vo": "_n2"}, ...]
Writes voice.mp3, words.json (all word times on the final timeline) and _timeline.json (start of each piece, for shots.json).
Each piece is loudnormed to -18 LUFS, 0.12 s gap between pieces. Quote words come from ElevenLabs STT json (scribe).
"""
import argparse, json, os, subprocess

GAP = 0.12


def run(*a):
    subprocess.run(a, check=True, capture_output=True)


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
            run("ffmpeg", "-y", "-i", src, "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-ar", "44100", "-ac", "1", out)
            ws = json.load(open(os.path.join(F, p["vo"], "words.json")))
            for w in ws:
                words.append({"word": w["word"], "start": round(t + w["start"], 3), "end": round(t + w["end"], 3)})
            kind = "vo"
        else:
            src = p["quote"] if os.path.isabs(p["quote"]) else os.path.join(F, p["quote"])
            f, to = p["from"], p["to"]
            run("ffmpeg", "-y", "-ss", str(f), "-t", str(to - f), "-i", src, "-af", "loudnorm=I=-18:TP=-2:LRA=7,afade=t=in:d=0.02,afade=t=out:st=%.2f:d=0.04" % (to - f - 0.04), "-ar", "44100", "-ac", "1", out)
            d = json.load(open(p["stt"]))
            for w in d.get("words", d):
                if w.get("type", "word") != "word":
                    continue
                if w["start"] >= f - 0.02 and w["end"] <= to + 0.1:
                    words.append({"word": w["text"], "start": round(t + w["start"] - f, 3), "end": round(t + min(w["end"], to) - f, 3)})
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
    run("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:a", "libmp3lame", "-q:a", "2", os.path.join(F, "voice.mp3"))
    json.dump(words, open(os.path.join(F, "words.json"), "w"), indent=1)
    json.dump(tl, open(os.path.join(F, "_timeline.json"), "w"), indent=1)
    print("total", round(t - GAP, 2), "s;", len(words), "words")
    for x in tl:
        print(x)


main()
