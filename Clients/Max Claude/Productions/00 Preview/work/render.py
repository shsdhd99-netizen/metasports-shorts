"""Render the Fingerprints preview in 16x9 and/or 9x16.

  python render.py [16x9|9x16|both]

Shots come from SHOTS below (times are on the voice.mp3 timeline). Opening/closing shots use his photo with a
slow push-in, unless the Hedra talking-head clips exist in work/ (open_talk.mp4 / close_talk.mp4 for 16x9,
open_talk_9x16.mp4 / close_talk_9x16.mp4 for 9x16; a missing 9x16 clip falls back to a centre crop of the 16x9 one).
"""
import json, os, re, subprocess, sys, tempfile

W = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(W)
REPO = os.path.abspath(os.path.join(ROOT, "../../../.."))
FONT_DIR = os.path.join(REPO, "Tools/fonts")
MUSIC = os.path.join(REPO, "Library/Music/eleven_story_01.mp3")
PHOTO = os.path.join(ROOT, "input/photo.jpg")
FPS = 30
CLOSE_T0 = 39.12          # close.mp3 starts here on the voice timeline
END = 43.20 + 0.25        # last word ends 43.20; 0.25 s tail, nothing after

# (start, src, source offset, framing x 0..1 for 9x16 crop, zoom start, zoom end)
SHOTS = [
    (0.00, "OPEN", 0, 0.5, 1.00, 1.06),
    (3.55, "mk_18308", 0.0, 0.55, 1.00, 1.06),   # finger touching frosted glass: "every time you touch something"
    (6.85, "mk_15054", 2.0, 0.45, 1.00, 1.06),   # ultrasound print: "before you were born"
    (10.98, "mk_12962", 2.0, "fit", 1.00, 1.05),    # two sisters: "identical twins"
    (13.45, "mk_47323", 3.0, 0.5, 1.05, 1.12),   # glowing fingerprint: "pattern of ridges"
    (17.77, "mk_13807", 0.0, 0.3, 1.00, 1.06),   # magnifying glass: "tiny details"
    (20.95, "mk_18308", 9.0, 0.45, 1.00, 1.06),  # the mark left on glass: "touch a glass ... perfect copy"
    (24.76, "mk_32791", 0.0, 0.2, 1.00, 1.05),  # investigator under UV
    (27.44, "mk_32791", 7.0, 0.15, 1.25, 1.32),  # the print appears (close on the handprint)
    (29.34, "mk_23678", 0.0, 0.6, 1.00, 1.05),   # fingerprint on a computer screen: "a computer can compare"
    (31.66, "mk_47323", 9.0, 0.5, 1.00, 1.06),   # print data: "millions of prints in seconds"
    (33.73, "mk_23678", 12.0, 0.72, 1.45, 1.52), # close on the monitor: "only suggests a match"
    (36.34, "mk_4773", 3.0, 0.4, 1.00, 1.05),    # examiner at a microscope: "makes the final call"
    (CLOSE_T0, "CLOSE", 0.0, 0.5, 1.06, 1.08),
    (40.18, "mk_33712", 0.0, 0.4, 1.00, 1.04),   # door handle: "open a door"
    (41.09, "CLOSE", 41.09 - CLOSE_T0, 0.5, 1.08, 1.12),
]
KEY = {"hundred", "signature", "born", "never", "twins", "ridges", "yours", "glass", "copy", "powder", "invisible",
       "computer", "millions", "seconds", "match", "examiner", "final", "door", "signed", "name"}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-3000:])


def talk_clip(kind, fmt):
    base = os.path.join(W, f"{kind}_talk")
    if fmt == "9x16" and os.path.exists(base + "_9x16.mp4"):
        return base + "_9x16.mp4"
    return base + ".mp4" if os.path.exists(base + ".mp4") else None


def shot(i, fmt, tmp):
    t0, src, off, fx, z0, z1 = SHOTS[i]
    t1 = SHOTS[i + 1][0] if i + 1 < len(SHOTS) else END
    d = t1 - t0
    ow, oh = (1920, 1080) if fmt == "16x9" else (1080, 1920)
    n = round(d * FPS)
    out = os.path.join(tmp, f"s{i:02d}.mp4")
    if src in ("OPEN", "CLOSE"):
        clip = talk_clip(src.lower(), fmt)
        if clip:   # Hedra clip: trim at the same voice offset, cover-fit, very slight push-in
            inp = ["-ss", f"{off:.3f}", "-t", f"{d + 0.2:.3f}", "-i", clip]
            pre = f"fps={FPS},scale={ow}:{oh}:force_original_aspect_ratio=increase,crop={ow}:{oh},scale={ow*2}:{oh*2}"
            z0, z1 = 1.0, 1.03
        else:      # placeholder: his photo, full frame
            inp = ["-loop", "1", "-framerate", str(FPS), "-t", f"{d + 0.2:.3f}", "-i", PHOTO]
            crop = "crop=1200:675:0:470" if fmt == "16x9" else "crop=900:1600:170:0"
            pre = f"{crop},scale={ow*2}:{oh*2}"
            fx = 0.5
    else:
        inp = ["-ss", f"{off:.3f}", "-t", f"{d + 0.2:.3f}", "-i", os.path.join(W, "src", src + ".mp4")]
        if fmt == "16x9":
            pre = f"fps={FPS},scale={ow*2}:{oh*2}:force_original_aspect_ratio=increase,crop={ow*2}:{oh*2}"
        elif fx == "fit":  # 9x16, both subjects must stay in: full width over a blurred fill
            pre = (f"fps={FPS},split[a][b];[a]scale={ow*2}:{oh*2}:force_original_aspect_ratio=increase,crop={ow*2}:{oh*2},"
                   f"gblur=sigma=40,eq=brightness=-0.08[bg];[b]scale={ow*2}:-2[fg];[bg][fg]overlay=0:(H-h)/2")
        else:  # 9x16: crop a vertical window placed by fx
            pre = (f"fps={FPS},scale=-2:{oh*2},crop={ow*2}:{oh*2}:(iw-{ow*2})*{fx}:0")
    zx = "(iw-iw/zoom)/2"
    zy = "(ih-ih/zoom)/2"
    vf = (f"{pre},zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='{zx}':y='{zy}':d=1:s={ow}x{oh}:fps={FPS},"
          f"setsar=1,format=yuv420p,trim=end_frame={n}")
    run(["ffmpeg", "-v", "error", "-y", *inp, "-vf", vf, "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "16", out])
    return out


def ass(fmt, path):
    words = json.load(open(os.path.join(W, "words.json")))
    ow, oh = (1920, 1080) if fmt == "16x9" else (1080, 1920)
    size, y = (80, 1000) if fmt == "16x9" else (84, 1380)  # 16x9: below his chin in the talking shots
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {ow}
PlayResY: {oh}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,TikTok Sans SemiBold,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,5,2,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    groups, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 3 or re.search(r"[.,:;!?]$", w["w"]):
            groups.append(cur); cur = []
    if cur:
        groups.append(cur)

    def ts(t):
        cs = round(t * 100); return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"
    lines = []
    for k, g in enumerate(groups):
        st = g[0]["s"]
        en = groups[k + 1][0]["s"] if k + 1 < len(groups) else END
        if en - g[-1]["e"] > 0.6:
            en = g[-1]["e"] + 0.35
        txt = " ".join(r"{\c&H00D4FF&}" + w["w"] + r"{\c&HFFFFFF&}" if re.sub(r"\W", "", w["w"]).lower() in KEY else w["w"] for w in g)
        lines.append(f"Dialogue: 0,{ts(st)},{ts(en)},C,,0,0,0,,{{\\pos({ow // 2},{y})}}{txt}")
    open(path, "w").write(head + "\n".join(lines) + "\n")


def render(fmt):
    tmp = tempfile.mkdtemp(prefix=f"r{fmt}_", dir=W)
    segs = [shot(i, fmt, tmp) for i in range(len(SHOTS))]
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    sub = os.path.join(tmp, "cap.ass"); ass(fmt, sub)
    out = os.path.join(ROOT, f"PREVIEW - Fingerprints ({fmt}).mp4")
    # voice to about -14 LUFS, music bed about 20 dB under, faded out at the end
    af = (f"[1:a]loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,apad[v];"
          f"[2:a]aresample=48000,atrim=0:{END},volume=-21dB,afade=t=in:d=1,afade=t=out:st={END - 1.2}:d=1.2[m];"
          f"[v][m]amix=inputs=2:duration=shortest:normalize=0,volume=4.2dB,alimiter=limit=0.8:level=false,atrim=0:{END}[a]")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(W, "voice.mp3"),
         "-i", MUSIC, "-filter_complex", f"[0:v]subtitles='{sub}':fontsdir='{FONT_DIR}'[vv];{af}",
         "-map", "[vv]", "-map", "[a]", "-t", f"{END}", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    subprocess.run(["rm", "-rf", tmp])
    print("wrote", out)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    for f in (["16x9", "9x16"] if which == "both" else [which]):
        render(f)
