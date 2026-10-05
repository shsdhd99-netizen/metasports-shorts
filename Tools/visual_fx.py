"""Optional visual/editing upgrades for MetaSports Shorts. Nothing here runs unless you call it; assemble.py is untouched.

  python visual_fx.py audit    --folder F [--video final.mp4]     measure shots: faces, repeats, motion, luma, caption-band clutter, quote loudness
  python visual_fx.py reframe  SRC --at 12.0 --len 3 --out clips/V03.mp4 [--face-y 0.36]
                               face-tracked 9:16 crop of a landscape source (replaces hand-picked broll.py --x/--y)
  python visual_fx.py statcard --big "$1.3M" --of "of $2.3M guaranteed" --label "BRONNY'S DEAL" --out clips/s01.mp4 [--len 2] [--color green]
  python visual_fx.py level    --folder F                          even out quote-vs-narration loudness -> voice_fx.mp3
  python visual_fx.py render   --folder F --out-name final_fx.mp4 [--punch 0.07] [--kenburns 0.06] [--grade] [--level] [--fx fx.json]
                               experimental builder: same inputs as assemble.py (shots.json, sfx.json ...) plus the options above

fx.json (optional, in the Short folder): {"statcards":[{"at":7.26,"big":"$1.3M","of":"of $2.3M","label":"GUARANTEED","color":"green"}],
                                          "nametags":[{"at":22.4,"until":25.0,"name":"LUKA DONCIC","sub":"LAKERS"}]}
Every option is off by default. Evidence tiers: Research Notes/Visuals and Editing Playbook (Oct 5, 2026).md
"""
import argparse, json, os, re, shutil, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
RED, GREEN = (255, 42, 42), (58, 227, 64)
sys.path.insert(0, HERE)


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def dur(p):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout.strip() or 0)


def lufs(path, ss=None, t=None):
    cmd = ["ffmpeg", "-hide_banner"] + (["-ss", f"{ss:.3f}"] if ss is not None else []) + (["-t", f"{t:.3f}"] if t else []) + ["-i", path, "-af", "ebur128", "-f", "null", "-"]
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", sh(cmd).stderr)
    return float(m[-1]) if m else None


# ------------------------------------------------------------------ detection
_cas = None


def faces(img_bgr):
    """Frontal faces (Haar alt2) on a small copy; returns [(x,y,w,h)] as 0-1 shares. A lower bound: profiles/back views are missed."""
    import cv2
    global _cas
    if _cas is None:
        _cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    h0, w0 = img_bgr.shape[:2]
    s = cv2.resize(img_bgr, (int(360 * w0 / h0), 360) if w0 > h0 else (360, int(360 * h0 / w0)))
    g = cv2.equalizeHist(cv2.cvtColor(s, cv2.COLOR_BGR2GRAY))
    sh_, sw_ = g.shape
    return [(x / sw_, y / sh_, w / sw_, h / sh_) for x, y, w, h in _cas.detectMultiScale(g, 1.1, 5, minSize=(24, 24))]


def frames_at(path, times):
    import cv2
    cap = cv2.VideoCapture(path)
    fps = cap.get(5) or 30
    out = []
    for t in times:
        cap.set(1, int(t * fps))
        ok, im = cap.read()
        if ok:
            out.append(im)
    cap.release()
    return out


# ------------------------------------------------------------------ audit
def load_shots(folder):
    p = json.load(open(os.path.join(folder, "shots.json"), encoding="utf-8"))
    total = dur(os.path.join(folder, "voice.mp3"))
    starts = [float(s["start"]) for s in p] + [total]
    return [dict(p[i], t0=starts[i], t1=starts[i + 1]) for i in range(len(p))], total


def cmd_audit(a):
    import cv2
    folder = os.path.abspath(a.folder)
    shots, total = load_shots(folder)
    video = a.video or os.path.join(folder, "final_nocap.mp4")
    if not os.path.exists(video):
        video = os.path.join(folder, "final.mp4")
    uses = {}
    for s in shots:
        uses[s["clip"]] = uses.get(s["clip"], 0) + 1
    rows, lumas = [], []
    for i, s in enumerate(shots):
        L = s["t1"] - s["t0"]
        fr = frames_at(video, [s["t0"] + L * k for k in (0.2, 0.5, 0.8)])
        fc = [faces(f) for f in fr]
        hit = sum(bool(x) for x in fc)
        big = max((f for x in fc for f in x), key=lambda f: f[2] * f[3], default=None)
        mot = float(np.mean(cv2.absdiff(cv2.resize(fr[0], (108, 192)), cv2.resize(fr[-1], (108, 192))))) if len(fr) > 1 else 0.0
        luma = float(np.mean([cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).mean() for f in fr])) if fr else 0.0
        lumas.append(luma)
        band = [cv2.Canny(cv2.cvtColor(f[int(H * .45):int(H * .62)], cv2.COLOR_BGR2GRAY), 120, 240).mean() / 255 for f in fr if f.shape[0] == H]
        rows.append(dict(i=i, clip=s["clip"], kind=s.get("kind", "?"), t0=round(s["t0"], 2), len=round(L, 2), face_hits=f"{hit}/{len(fr)}",
                         face_h=round(big[3], 2) if big else None, face_cy=round(big[1] + big[3] / 2, 2) if big else None,
                         motion=round(mot, 1), luma=round(luma), band_edges=round(float(np.mean(band)), 3) if band else None,
                         repeat=uses[s["clip"]] > 1))
    print(f"{os.path.basename(folder)}: {len(rows)} shots, {total:.1f}s, video={os.path.basename(video)}")
    print(" i clip          kind   t0    len  faces  faceH  cy    motion luma  capband rep")
    for r in rows:
        print(f"{r['i']:2d} {r['clip'][:12]:12s} {r['kind'][:6]:6s} {r['t0']:5.1f} {r['len']:4.1f}  {r['face_hits']:5s} {str(r['face_h']):5s} {str(r['face_cy']):5s} {r['motion']:5.1f}  {r['luma']:4d}  {str(r['band_edges']):6s} {'Y' if r['repeat'] else ''}")
    st = [(r['i'], r['t0'], r['len']) for r in rows if r["motion"] < 2.0 and r["kind"] != "card"]
    print(f"static non-card shots (motion<2): {st}")
    print(f"luma spread across shots: std={np.std(lumas):.1f} (min {min(lumas):.0f}, max {max(lumas):.0f})")
    print(f"caption-band clutter (edge density > 0.12): {[r['i'] for r in rows if (r['band_edges'] or 0) > 0.12]}")
    tl = os.path.join(folder, "_timeline.json")
    if os.path.exists(tl):
        for p in json.load(open(tl)):
            if p["end"] - p["start"] > 1.0:
                print(f"  audio {p['kind']:5s} {p['start']:6.2f}-{p['end']:6.2f}: {lufs(video, p['start'] + .1, p['end'] - p['start'] - .2)} LUFS")
    json.dump(rows, open(os.path.join(folder, "audit_fx.json"), "w"), indent=1)


# ------------------------------------------------------------------ reframe
def cmd_reframe(a):
    sys.argv = [sys.argv[0]]
    import broll
    s, local = broll.src(a.source)
    w, h, _ = broll.probe(s)
    fr = frames_at(s, np.linspace(a.at, a.at + a.len, a.samples))
    pts = []
    for f in fr:
        fs = faces(f)
        if fs:
            x, y, fw, fh = max(fs, key=lambda q: q[2] * q[3])
            pts.append((x + fw / 2, y + fh / 2, fh))
    if not pts:
        print("no face found: centre crop (x=0.5 y=0.5 zoom=1)")
        x, y, zoom = 0.5, 0.5, 1.0
    else:
        cx, cy, fh = (float(np.median([p[i] for p in pts])) for i in range(3))
        cw = (h * 9 / 16) / w
        x = min(1, max(0, (cx - cw / 2) / (1 - cw))) if cw < 1 else 0.5
        zoom = min(a.max_zoom, max(1.0, a.face_h / fh)) if fh else 1.0
        ch = 1 / zoom
        y = min(1, max(0, (cy - a.face_y * ch) / (1 - ch))) if ch < 1 else 0.5
        print(f"{len(pts)}/{len(fr)} frames with a face: centre=({cx:.2f},{cy:.2f}) face_h={fh:.2f} -> --x {x:.3f} --y {y:.3f} --zoom {zoom:.2f}")
    vf = broll.vertical(w, h, x, zoom, y) + ",fps=30,format=yuv420p"
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    r = sh(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a.at:.2f}", "-i", s, "-t", f"{a.len:.2f}", "-vf", vf, "-an", "-c:v", "libx264", "-crf", "18", a.out])
    print(r.stderr[-200:] or f"wrote {a.out}")


# ------------------------------------------------------------------ stat card
def font(name, size):
    from PIL import ImageFont
    return ImageFont.truetype(os.path.join(HERE, "fonts", name), size)


def fit(draw, text, name, size, maxw):
    while size > 40:
        f = font(name, size)
        if draw.textlength(text, font=f) <= maxw:
            return f
        size -= 6
    return font(name, 40)


def cmd_statcard(a):
    """Number card in the Wemby style: the spoken number big and boxed, a label above, an optional line below. It sits in the top 40% so the
    centred captions (45-62% height) never cover it. Frames drawn with PIL and piped to ffmpeg (pop-in, box wipe, slow push)."""
    from PIL import Image, ImageDraw
    col = GREEN if a.color == "green" else RED
    fps, n = 30, int(a.len * 30)
    px = np.zeros((H, W, 3), np.uint8)
    for k, (t, b) in enumerate(zip((18, 20, 28), (6, 7, 10))):
        px[:, :, k] = np.linspace(t, b, H)[:, None]
    bg = Image.fromarray(px)
    d0 = ImageDraw.Draw(bg)
    big_f = fit(d0, a.big, "Montserrat-Black.ttf", 300, 880)
    lab_f = fit(d0, a.label.upper(), "Montserrat-Black.ttf", 64, 940)
    of_f = fit(d0, a.of.upper(), "Montserrat-Bold.ttf", 54, 940) if a.of else None
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                          "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", a.out], stdin=subprocess.PIPE)
    cy = int(H * 0.27) + (60 if getattr(a, "down", False) else 0)  # shift down when a premise line sits at the top
    ease = lambda x: 1 - (1 - min(1, max(0, x))) ** 3
    for i in range(n):
        t = i / fps
        sc = (0.82 + 0.18 * ease(t / 0.18)) * (1 + 0.045 * t / a.len)
        im = bg.copy()
        d = ImageDraw.Draw(im)
        if a.label:
            tw = d.textlength(a.label.upper(), font=lab_f)
            d.text(((W - tw) / 2, cy - 330 * sc), a.label.upper(), font=lab_f, fill=(255, 255, 255))
        lay = Image.new("RGBA", (W, 520), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        bb = ld.textbbox((0, 0), a.big, font=big_f)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        ld.text(((W - bw) / 2 - bb[0], 260 - bh / 2 - bb[1]), a.big, font=big_f, fill=col + (255,))
        lay = lay.resize((int(W * sc), int(520 * sc)), Image.LANCZOS)
        im.paste(lay, (int((W - lay.width) / 2), int(cy - lay.height / 2)), lay)
        d = ImageDraw.Draw(im)
        prog = ease((t - 0.25) / 0.30)
        if prog > 0:
            x0, x1 = (W - bw * sc) / 2 - 40, (W + bw * sc) / 2 + 40
            y0, y1 = cy - bh * sc / 2 - 40, cy + bh * sc / 2 + 40
            if prog >= 1:
                d.rounded_rectangle((x0, y0, x1, y1), 26, outline=col, width=12)
            else:
                d.line((x0, y1, x0 + (x1 - x0) * prog, y1), fill=col, width=12)
        if of_f:
            tw = d.textlength(a.of.upper(), font=of_f)
            d.text(((W - tw) / 2, cy + 250 * sc), a.of.upper(), font=of_f, fill=(200, 205, 215))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(f"wrote {a.out} ({a.len}s)")


# ------------------------------------------------------------------ audio levelling
def cmd_level(a):
    level_voice(os.path.abspath(a.folder), a.target, verbose=True)


def level_voice(folder, target=None, verbose=False):
    """Bring every quote piece to the narration loudness (median of narration pieces) using _timeline.json. voice.mp3 is untouched."""
    tl = json.load(open(os.path.join(folder, "_timeline.json")))
    voice = os.path.join(folder, "voice.mp3")
    meas = [lufs(voice, p["start"], p["end"] - p["start"]) if p["end"] - p["start"] > 0.8 else None for p in tl]
    vo = [m for p, m in zip(tl, meas) if p["kind"] == "vo" and m is not None]
    tgt = target if target is not None else float(np.median(vo))
    gains = [(0.0 if (m is None or p["kind"] == "vo") else round(max(-6, min(9, tgt - m)), 2)) for p, m in zip(tl, meas)]
    if verbose:
        for p, m, g in zip(tl, meas, gains):
            print(f"  {p['kind']:5s} {p['start']:6.2f}-{p['end']:6.2f}: {m} LUFS -> gain {g:+.1f} dB (target {tgt:.1f})")
    if not any(gains):
        return voice
    expr = "+".join(f"if(between(t,{p['start']:.3f},{p['end']:.3f}),{g},0)" for p, g in zip(tl, gains) if g)
    out = os.path.join(folder, "voice_fx.mp3")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", voice, "-af", f"volume='pow(10,({expr})/20)':eval=frame", "-b:a", "192k", out])
    if verbose:
        print("  after:", [lufs(out, p["start"], p["end"] - p["start"]) if p["end"] - p["start"] > .8 else None for p in tl])
    return out


# ------------------------------------------------------------------ punch-in / Ken Burns / grade
def plan_punches(words, bounds, gap=1.2):
    """Start times of key words to punch in on: numbers, money, units, SHOCK/BIG words (captions.py sets). One per shot, >= gap apart."""
    import captions
    out, last = [], -9
    for w in words:
        b = re.sub(r"[^\w$.-]", "", w["word"]).lower()
        t = float(w["start"])
        if (re.search(r"\d|\$", w["word"]) or b in captions.UNITS or b in captions.SHOCK or b in captions.BIG) and t - last >= gap \
                and any(t0 + 0.15 < t < t1 - 0.3 for t0, t1 in bounds):
            out.append(t)
            last = t
    return out


def zoom_expr(base, amp, pulses, L):
    """z(t): slow push `base` across the shot + `amp` pulse at each local time in `pulses` (0.12 s ramp up, 0.45 s settle)."""
    terms = [f"{base}*t/{max(L, .1):.3f}"]
    for p in pulses:
        terms.append(f"{amp}*if(lt(t,{p:.3f}),0,if(lt(t,{p + .12:.3f}),(t-{p:.3f})/.12,max(0,1-(t-{p + .12:.3f})/.45)))")
    return "1+" + "+".join(terms)


def shot_filter(base, amp, pulses, L):
    z = zoom_expr(base, amp, pulses, L)
    B = 1.5  # work at 1.5x, scale by z per frame, crop the centre, scale back: sub-pixel smooth (integer scale sizes make the picture shimmer)
    bw, bh = int(W * B), int(H * B)
    return (f"scale={bw}:{bh}:force_original_aspect_ratio=increase,crop={bw}:{bh},fps=30,"
            f"scale=w='trunc({bw}*({z})/2)*2':h='trunc({bh}*({z})/2)*2':eval=frame,"
            f"crop={bw}:{bh}:(iw-{bw})/2:(ih-{bh})*0.4,scale={W}:{H}:flags=bicubic,setsar=1,format=yuv420p")


def grade_filter(clip, off, L, target=105.0):
    """Per-shot exposure/contrast match, clamped (brightness +-0.08, contrast +-12%) so looks stay natural."""
    r = sh(["ffmpeg", "-hide_banner", "-ss", f"{off:.2f}", "-t", f"{min(L, 2):.2f}", "-i", clip, "-vf", "fps=4,signalstats,metadata=print:file=-", "-f", "null", "-"])
    ys = [float(x) for x in re.findall(r"YAVG=([\d.]+)", r.stdout)]
    yl = [float(x) for x in re.findall(r"YLOW=([\d.]+)", r.stdout)]
    yh = [float(x) for x in re.findall(r"YHIGH=([\d.]+)", r.stdout)]
    if not ys:
        return "", None
    m = float(np.mean(ys))
    br = max(-.08, min(.08, (target - m) / 255 * 0.6))
    spread = float(np.mean(yh) - np.mean(yl)) if yl and yh else 150
    ct = max(.88, min(1.12, 150 / max(spread, 60)))
    return f",eq=brightness={br:.3f}:contrast={ct:.3f}", m


def cmd_render(a):
    import assemble
    folder = os.path.abspath(a.folder)
    shots, total = load_shots(folder)
    words = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8"))
    fxp = os.path.join(folder, a.fx or "fx.json")
    fx = json.load(open(fxp, encoding="utf-8")) if os.path.exists(fxp) else {}
    voice = os.path.join(folder, "voice.mp3")
    if a.level and os.path.exists(os.path.join(folder, "_timeline.json")):
        voice = level_voice(folder)
    tmp = os.path.join(folder, "_fx_tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    punches = plan_punches(words, [(s["t0"], s["t1"]) for s in shots], a.punch_gap) if a.punch else []
    print(f"{len(shots)} shots; punch-ins at {[round(p, 2) for p in punches]}")
    parts, lumas = [], []
    for i, s in enumerate(shots):
        L = s["t1"] - s["t0"]
        out = os.path.join(tmp, f"s{i:03d}.mp4")
        card = next((c for c in fx.get("statcards", []) if abs(c["at"] - s["t0"]) < 0.35), None)
        if card:
            cmd_statcard(argparse.Namespace(big=card["big"], of=card.get("of", ""), label=card.get("label", ""), color=card.get("color", "green"), len=L, out=out, down=bool(a.premise_line)))
            parts.append(out)
            continue
        clip = os.path.join(folder, "clips", s["clip"])
        still = clip.lower().endswith((".jpg", ".png", ".jpeg"))
        iscard = s.get("kind") == "card" or os.path.basename(clip).lower().startswith(("c", "p_"))
        base = float(s.get("zoom", 0) or 0) or (a.kenburns if (iscard or still) else a.auto_zoom)
        pl = [p - s["t0"] for p in punches if s["t0"] < p < s["t1"] and not iscard]
        vf = shot_filter(base, a.punch if pl else 0, pl, L) if (base or pl) else \
            f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30,format=yuv420p"
        off = float(s.get("in", 0) or 0)
        if a.grade and not still and not iscard:
            g, m = grade_filter(clip, off, L)
            vf += g
            if m is not None:
                lumas.append(m)
        pre = ["-loop", "1", "-t", f"{L:.3f}"] if still else ["-ss", f"{off:.3f}", "-stream_loop", "-1"]
        r = sh(["ffmpeg", "-y", "-loglevel", "error", *pre, "-i", clip] + ([] if still else ["-t", f"{L:.3f}"]) +
               ["-vf", vf, "-an", "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", out])
        if r.returncode:
            raise SystemExit(f"shot {i} failed: {r.stderr[-300:]}")
        parts.append(out)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    raw = os.path.join(folder, "_fx_nocap.mp4")
    r = sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", voice, "-map", "0:v", "-map", "1:a",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", raw])
    if r.returncode:
        raise SystemExit(r.stderr[-300:])
    tags = fx.get("nametags", [])
    if tags:  # lower-third at 66% height: under the caption band, above the Shorts UI
        vf = []
        fnt = os.path.join(HERE, "fonts", "Montserrat-Black.ttf").replace(":", "\\:")
        for t in tags:
            en = f"between(t,{t['at']},{t['until']})"
            y = int(H * .665)
            vf.append(f"drawbox=x=48:y={y}:w=10:h=118:color=0xFF2A2A:t=fill:enable='{en}'")
            vf.append(f"drawtext=fontfile='{fnt}':text='{t['name'].upper()}':fontsize=54:fontcolor=white:borderw=5:bordercolor=black:x=76:y={y}:enable='{en}'")
            if t.get("sub"):
                vf.append(f"drawtext=fontfile='{fnt}':text='{t['sub'].upper()}':fontsize=34:fontcolor=0xDDDDDD:borderw=4:bordercolor=black:x=78:y={y + 74}:enable='{en}'")
        raw2 = os.path.join(folder, "_fx_tags.mp4")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-vf", ",".join(vf), "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-c:a", "copy", raw2])
        os.replace(raw2, raw)
    if a.premise_line:  # persistent premise line: top safe area (y=7%), 2-4 words, sentence case, subtle dark pill; whole video
        fnt = os.path.join(HERE, "fonts", "Montserrat-Bold.ttf").replace(":", "\\:")
        txt = a.premise_line.replace("\\", "\\\\").replace("'", "\u2019").replace(":", "\\:").replace("%", "\\%")
        raw3 = os.path.join(folder, "_fx_premise.mp4")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-vf",
            f"drawtext=fontfile='{fnt}':text='{txt}':fontsize=44:fontcolor=white:box=1:boxcolor=black@0.45:boxborderw=18:x=(w-text_w)/2:y={int(H * 0.07)}",
            "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-c:a", "copy", raw3])
        os.replace(raw3, raw)
    final = os.path.join(folder, a.out_name)
    assemble.finish(folder, raw, final, total, a.caption_style, music=None)
    shutil.rmtree(tmp, ignore_errors=True)
    if lumas:
        print(f"graded {len(lumas)} shots; source luma std before grade = {np.std(lumas):.1f}")
    print(f"Done: {final} ({dur(final):.1f}s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("audit"); p.add_argument("--folder", required=True); p.add_argument("--video")
    p = sub.add_parser("reframe"); p.add_argument("source"); p.add_argument("--at", type=float, required=True); p.add_argument("--len", type=float, default=3)
    p.add_argument("--out", required=True); p.add_argument("--samples", type=int, default=8); p.add_argument("--face-y", dest="face_y", type=float, default=0.36)
    p.add_argument("--face-h", dest="face_h", type=float, default=0.16, help="minimum face height (share of frame) before it zooms in")
    p.add_argument("--max-zoom", dest="max_zoom", type=float, default=1.6)
    p = sub.add_parser("statcard"); p.add_argument("--big", required=True); p.add_argument("--of", default=""); p.add_argument("--label", default="")
    p.add_argument("--out", required=True); p.add_argument("--len", type=float, default=2.0); p.add_argument("--color", default="green", choices=["green", "red"])
    p = sub.add_parser("level"); p.add_argument("--folder", required=True); p.add_argument("--target", type=float, default=None)
    p = sub.add_parser("render"); p.add_argument("--folder", required=True); p.add_argument("--out-name", dest="out_name", default="final_fx.mp4")
    p.add_argument("--punch", type=float, default=0.0, help="punch-in amount on key words, e.g. 0.07")
    p.add_argument("--punch-gap", dest="punch_gap", type=float, default=1.2)
    p.add_argument("--kenburns", type=float, default=0.0, help="slow push on stills/cards, e.g. 0.06")
    p.add_argument("--auto-zoom", dest="auto_zoom", type=float, default=0.0)
    p.add_argument("--grade", action="store_true"); p.add_argument("--level", action="store_true")
    p.add_argument("--premise-line", dest="premise_line", default="", help='small persistent line at the top, e.g. "Flagg: 6-8 to 6-11?"')
    p.add_argument("--fx", default=None); p.add_argument("--caption-style", dest="caption_style", default="metasports")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    {"audit": cmd_audit, "reframe": cmd_reframe, "statcard": cmd_statcard, "level": cmd_level, "render": cmd_render}[a.cmd](a)


if __name__ == "__main__":
    main()
