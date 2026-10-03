"""Final pass for a Short: the house MetaSports captions (captions.py, ALL CAPS, bright red/green accents) + a clean audio mix.
  python Tools/polish.py --folder "<production folder>"
Needs final_nocap.mp4 (from assemble.py), voice.mp3, words.json. Reads sfx.json (keep it to 1-3 effects that match the picture).
Audio: voice is cleaned + levelled first, effects sit well under it, whole mix lands at about -14 LUFS, true peak under -1.5 dB."""
import argparse, json, os, subprocess, sys
from PIL import ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "Montserrat-Black.ttf")
SIZE, MAXW, Y = 100, 940, 1300
pil = ImageFont.truetype(FONT, SIZE)
width = lambda t: pil.getlength(t)


def chunks(words):
    out, cur = [], []
    for w in words:
        t = w["word"].upper()
        trial = cur + [w]
        txt = " ".join(x["word"].upper() for x in trial)
        if cur and (len(trial) > 4 or width(txt) > 2 * MAXW - 80):
            out.append(cur); cur = []
        cur.append(w)
        if t[-1] in ",.?!:;" or (len(cur) >= 3 and width(" ".join(x["word"].upper() for x in cur)) > MAXW):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def lines_of(group):
    """split a chunk into at most two lines that fit MAXW; returns list of word-lists"""
    txt = lambda ws: " ".join(x["word"].upper() for x in ws)
    if width(txt(group)) <= MAXW:
        return [group]
    best = min(range(1, len(group)), key=lambda i: max(width(txt(group[:i])), width(txt(group[i:]))))
    return [group[:best], group[best:]]


def ass_time(t):
    h, m = int(t // 3600), int(t % 3600 // 60)
    return f"{h}:{m:02d}:{t % 60:05.2f}"


def make_ass(words, total):
    ev = []
    gs = chunks(words)
    for gi, g in enumerate(gs):
        ls = lines_of(g)
        nxt = gs[gi + 1][0]["start"] - 0.02 if gi + 1 < len(gs) else total
        for i, w in enumerate(g):
            st = w["start"] if i else max(0.0, g[0]["start"] - 0.02)
            en = g[i + 1]["start"] if i + 1 < len(g) else min(nxt, max(w["end"] + 0.12, w["start"] + 0.3))
            parts = []
            for li, line in enumerate(ls):
                seg = []
                for x in line:
                    on = x is w
                    word = x["word"].upper().replace("{", "").replace("}", "")
                    seg.append((r"{\c&H0000D4FF&\fscx114\fscy114\t(0,110,\fscx106\fscy106)}" if on else r"{\c&H00FFFFFF&\fscx100\fscy100}") + word)
                parts.append(" ".join(seg))
            ev.append(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},Cap,,0,0,0,,{{\\pos(540,{Y})\\an5}}" + r"\N".join(parts))
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat Black,{SIZE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,9,4,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    return head + "\n".join(ev) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--out", default="final.mp4")
    ap.add_argument("--sfx-under", type=float, default=0.0, help="extra dB to add to every effect gain")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8-sig"))
    vid = os.path.join(F, "final_nocap.mp4")
    total = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vid]))
    sys.path.insert(0, HERE)
    import captions  # the house caption style (metasports): never change it
    captions.build(F, "metasports", total)
    cat = json.load(open(os.path.join(HERE, "sfx", "catalog.json"), encoding="utf-8"))
    sp = os.path.join(F, "sfx.json")
    fx = [e for e in json.load(open(sp, encoding="utf-8-sig"))] if os.path.exists(sp) else []
    # 1) voice: rumble off, gentle compression, levelled to -16 LUFS (two-pass loudnorm)
    pre = "highpass=f=70,acompressor=threshold=-21dB:ratio=2.5:attack=8:release=120:makeup=3,"
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", os.path.join(F, "voice.mp3"), "-af", pre + "loudnorm=I=-14.3:TP=-2:LRA=7:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    ln = (f"loudnorm=I=-14.3:TP=-2:LRA=7:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
          f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", os.path.join(F, "voice.mp3")]
    parts = [f"[1:a]{pre}{ln},aformat=sample_rates=48000:channel_layouts=stereo[v]"]
    labels = ["[v]"]
    for k, e in enumerate(fx, 2):
        name = e["sfx"]
        cmd += ["-i", os.path.join(HERE, "sfx", name + ".wav")]
        g = float(e.get("gain", cat.get(name, {}).get("gain", -14))) + a.sfx_under
        ms = int(round(float(e["at"]) * 1000))
        ln2 = float(e.get("len", 1.2))
        parts.append(f"[{k}:a]atrim=0:{ln2},afade=t=out:st={max(0, ln2 - 0.25)}:d=0.25,aformat=sample_rates=48000:channel_layouts=stereo,volume={g}dB,adelay={ms}|{ms}[s{k}]")
        labels.append(f"[s{k}]")
    parts.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,alimiter=limit=0.84:attack=3:release=80:level=disabled,atrim=0:{total:.3f}[a]")
    rel = lambda p: os.path.relpath(p, F).replace("\\", "/")
    vf = f"subtitles='captions.ass':fontsdir='{rel(os.path.join(HERE, 'fonts'))}'"
    tmp = os.path.join(F, "_polish_tmp.mp4")
    for enc in (["-c:v", "libx264", "-crf", "21", "-preset", "veryfast"],):
        r = subprocess.run(cmd + ["-filter_complex", f"[0:v]{vf}[vv];" + ";".join(parts), "-map", "[vv]", "-map", "[a]", "-c:a", "aac", "-b:a", "192k", *enc,
                                  "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp], cwd=F, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr[-800:])
    os.replace(tmp, os.path.join(F, a.out))
    print("done", a.out)


if __name__ == "__main__":
    main()
