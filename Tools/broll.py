"""Find and cut B-roll for a Short (free: yt-dlp + ffmpeg). Claude runs this for you inside /assemble.

  python broll.py search "lebron 76ers press conference"          # candidates, official channels first
  python broll.py sheet <youtube id | url | file> --from 0 --to 90 --every 3 --out sheet.jpg
                                                                  # a labelled contact sheet to pick clean moments
  python broll.py cut <youtube id | url | file> --at 12.5 --len 5 --x 0.5 --out clips\\01.mp4
                                                                  # a clean 1080x1920 clip, no audio
  python broll.py still picture.png --len 5 --out clips\\03.mp4    # a picture as a slow-zoom video clip

--x is where the subject sits across the frame: 0 = left edge, 0.5 = middle, 1 = right edge.
Cuts download only the seconds you need, in the best quality up to 1080p.
"""
import argparse, json, math, os, re, shutil, subprocess, sys, tempfile

OFFICIAL = {"NBA", "ESPN", "House of Highlights", "Bleacher Report", "NBA on TNT", "Inside the NBA", "NBA on ESPN",
            "Philadelphia 76ers", "Los Angeles Lakers", "New York Knicks", "Milwaukee Bucks", "Miami HEAT", "San Antonio Spurs",
            "Oklahoma City Thunder", "Dallas Mavericks", "Boston Celtics", "Golden State Warriors", "Cleveland Cavaliers",
            "NBA on Prime", "NBC Sports", "ClutchPoints", "Sports Illustrated", "The Athletic", "Yahoo Sports"}
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
if not os.path.exists("C:/Windows/Fonts/arialbd.ttf"):  # Linux: bundled font
    FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Montserrat-Bold.ttf")


def src(s):
    if os.path.exists(s):
        return s, True
    if re.fullmatch(r"[\w-]{11}", s):
        return f"https://www.youtube.com/watch?v={s}", False
    return s, False


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"Failed: {' '.join(cmd[:3])}...\n{(r.stderr or r.stdout)[-800:]}")
    return r


def section(url, start, end, fmt, tmp):
    """Download only [start, end] seconds of a YouTube video (video only)."""
    out = os.path.join(tmp, "section.%(ext)s")
    run(["yt-dlp", "-q", "--no-warnings", "-f", fmt, "--download-sections", f"*{start:.2f}-{end:.2f}",
         "--force-keyframes-at-cuts", "-o", out, url])
    files = [f for f in os.listdir(tmp) if f.startswith("section.")]
    if not files:
        raise SystemExit("Download failed (the video may be private, age-restricted or removed).")
    return os.path.join(tmp, files[0])


def probe(path):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
             "-show_entries", "format=duration", "-of", "json", path])
    j = json.loads(r.stdout)
    st = (j.get("streams") or [{}])[0]
    return st.get("width", 0), st.get("height", 0), float(j.get("format", {}).get("duration", 0))


def cmd_search(a):
    r = run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", f"ytsearch{a.n}:{a.query}"])
    ents = [e for e in (json.loads(r.stdout or "{}").get("entries") or []) if e]
    ents.sort(key=lambda e: ((e.get("channel") or "") not in OFFICIAL, -(e.get("view_count") or 0)))
    for e in ents:
        dur = int(e.get("duration") or 0)
        print(f"{e.get('id')}  {dur // 60:>2}:{dur % 60:02d}  {(e.get('view_count') or 0):>11,}  "
              f"{'*' if (e.get('channel') or '') in OFFICIAL else ' '} {(e.get('channel') or '')[:22]:<22}  {(e.get('title') or '')[:70]}")


def cmd_sheet(a):
    s, local = src(a.source)
    tmp = tempfile.mkdtemp()
    try:
        path, offset = (s, a.start) if local else (section(s, a.start, a.end, "bv*[height<=360][vcodec^=avc1]/bv*[height<=480][vcodec^=avc1]/bv*[height<=480][vcodec^=vp]/bv*[vcodec!^=av01]/b", tmp), a.start)
        seek = ["-ss", f"{a.start:.2f}", "-t", f"{a.end - a.start:.2f}"] if local else []
        n = max(1, int((a.end - a.start) // a.every) + 1)
        rows = math.ceil(n / 5)
        # select (not fps): each tile is the first real frame at/after every step, labelled with its true time
        vf = (f"select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,{a.every - 0.02})',scale=288:-2,"
              f"drawtext=fontfile='{FONT}':text='%{{pts\\:hms\\:{offset}}}':"
              f"x=6:y=6:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.65,tile=5x{rows}:padding=4:margin=4")
        run(["ffmpeg", "-y", "-loglevel", "error", *seek, "-i", path, "-vf", vf, "-fps_mode", "vfr", "-frames:v", "1", "-q:v", "4", a.out])
        w, h, d = probe(path)
        print(f"{a.out}  ({n} frames, every {a.every}s from {a.start}s; source {w}x{h})")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def vertical(w, h, x, zoom=1.0, y=0.5):
    """ffmpeg filter that fills 1080x1920 from any frame. x/y (0..1) place the crop; zoom > 1 crops tighter
    (use it to cut off tickers, score bugs or channel logos)."""
    if w / h > 9 / 16:
        ch = f"ih/{zoom:.3f}"
        cw = f"{ch}*9/16"
        return (f"crop={cw}:{ch}:(iw-{cw})*{x:.3f}:(ih-{ch})*{y:.3f},scale=1080:1920:flags=lanczos")
    return (f"crop=iw/{zoom:.3f}:ih/{zoom:.3f}:(iw-iw/{zoom:.3f})*{x:.3f}:(ih-ih/{zoom:.3f})*{y:.3f},"
            "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920")


def scene_bounds(s, local, at, tmp, pad=4.0):
    """Start and end of the camera shot that contains second `at` (so a clip never starts mid-cut)."""
    lo, hi = max(0.0, at - pad), at + pad
    if local:
        path, seek, offset = s, ["-ss", f"{lo:.2f}", "-t", f"{hi - lo:.2f}"], lo
    else:
        sub = tempfile.mkdtemp(dir=tmp)
        path, seek, offset = section(s, lo, hi, "bv*[height<=360][vcodec^=avc1]/bv*[height<=480][vcodec^=avc1]/bv*[height<=480][vcodec^=vp]/bv*[vcodec!^=av01]/b", sub), [], lo
    err = subprocess.run(["ffmpeg", "-hide_banner", *seek, "-i", path, "-vf", "select='gt(scene,0.3)',showinfo", "-f", "null", "-"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    cuts = [offset + float(t) for t in re.findall(r"pts_time:([\d.]+)", err)]
    # no cut found nearby: stay close to `at` rather than trusting the window edge
    start = max([c for c in cuts if c <= at] or [max(lo, at - 0.3)])
    end = min([c for c in cuts if c > at] or [hi])
    return start, end


def cmd_cut(a):
    s, local = src(a.source)
    tmp = tempfile.mkdtemp()
    try:
        if a.snap:
            s0, s1 = scene_bounds(s, local, a.at, tmp)
            a.at = s0 + 0.04
            if s1 - a.at < a.len - 0.05:
                print(f"  note: that shot only lasts {s1 - a.at:.1f}s, so the clip runs into the next shot")
        if local:
            path, seek = s, ["-ss", f"{a.at:.2f}"]
        else:
            path = section(s, max(0, a.at), a.at + a.len + 0.6, "bv*[height<=1080][vcodec^=avc1]/bv*[height<=1080][vcodec^=vp]/bv*[height<=1080][vcodec!^=av01]/bv*[vcodec!^=av01]", tmp)
            seek = []
        w, h, _ = probe(path)
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        dl = ""
        if a.delogo:  # Oct 21: blur a TV channel bug (fractions of the source frame: x,y,w,h)
            fx, fy, fw, fh = (float(v) for v in a.delogo.split(","))
            dl = f"delogo=x={int(fx * w)}:y={int(fy * h)}:w={int(fw * w)}:h={int(fh * h)},"
        if a.blurfit:  # Oct 21 (story format): the whole wide frame, full width, over a blurred, darkened fill of itself
            fg_w = int(1080 * a.blurfit_width) // 2 * 2
            fc = (f"[0:v]{dl}split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,"
                  f"eq=brightness=-0.12[bg];[b]crop=iw/{a.zoom:.3f}:ih/{a.zoom:.3f},scale={fg_w}:-2:flags=lanczos{',hflip' if a.flip else ''}[fg];"
                  f"[bg][fg]overlay=(W-w)/2:(H-h)*{a.y:.3f},fps=30,format=yuv420p[v]")
            run(["ffmpeg", "-y", "-loglevel", "error", *seek, "-i", path, "-t", f"{a.len:.2f}", "-filter_complex", fc,
                 "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "medium", a.out])
        else:
            vf = dl + vertical(w, h, a.x, a.zoom, a.y) + (",hflip" if a.flip else "") + ",fps=30,format=yuv420p"
            run(["ffmpeg", "-y", "-loglevel", "error", *seek, "-i", path, "-t", f"{a.len:.2f}", "-vf", vf, "-an",
                 "-c:v", "libx264", "-crf", "18", "-preset", "medium", a.out])
        print(f"{a.out}  ({a.len:.1f}s from {a.at:.1f}s, source {w}x{h}{', upscaled' if h < 1080 else ''})")
        log_cut(a, s, local, w, h)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def log_cut(a, s, local, w, h):
    """Oct 14: every cut writes its source-log row (<production>/sources.csv; see Library/B-roll Sourcing Guide.md)."""
    import csv
    clip_dir = os.path.dirname(os.path.abspath(a.out))
    folder = os.path.dirname(clip_dir) if os.path.basename(clip_dir) == "clips" else clip_dir
    url = s
    if local:
        sid = os.path.splitext(os.path.basename(s))[0]
        url = f"https://x.com/i/status/{sid}" if sid.isdigit() else os.path.relpath(os.path.abspath(s), folder)
        meta = os.path.join(os.path.dirname(os.path.abspath(s)), "downloads.csv")  # written by x_clip.py
        acct = date = text = ""
        if os.path.exists(meta):
            for r in csv.DictReader(open(meta, encoding="utf-8")):
                if r.get("id") == sid:
                    acct, date, text = r.get("account", ""), r.get("date", ""), r.get("text", "")
    else:
        acct = date = text = ""
    p = os.path.join(folder, "sources.csv")
    cols = ["clip", "kind", "used_at_s", "used_for_line", "what_it_shows", "source_url", "source_account", "source_date",
            "source_in_s", "source_out_s", "crop", "match_score", "licence_risk", "verified", "verified_on", "notes"]
    rows = list(csv.DictReader(open(p, encoding="utf-8-sig"))) if os.path.exists(p) else []
    clip = os.path.basename(a.out)
    rows = [r for r in rows if r.get("clip") != clip]
    rows.append({"clip": clip, "source_url": url, "source_account": acct, "source_date": date, "source_in_s": f"{a.at:.1f}",
                 "source_out_s": f"{a.at + a.len:.1f}", "crop": f"x {a.x} zoom {a.zoom} y {a.y}" + (" flipped" if a.flip else "") + (" blurfit" if getattr(a, "blurfit", False) else ""),
                 "notes": (f"post text: {text[:120]}" if text else "") + (f" | source {w}x{h}" if w else ""), "verified": ""})
    wr = csv.DictWriter(open(p, "w", encoding="utf-8", newline=""), fieldnames=cols)
    wr.writeheader()
    wr.writerows({k: r.get(k, "") for k in cols} for r in rows)


def cmd_page(a):
    """A screenshot (or any picture) as a 9:16 clip: centred on a blurred copy of itself, slow push-in toward
    --focus, and red circles/boxes (like the old MetaSports Shorts) drawn on around --box areas."""
    from PIL import Image, ImageDraw, ImageFilter
    W, H, FPS = 1080, 1920, 30
    src_im = Image.open(a.source).convert("RGB")
    if a.trim:  # cut half-visible text lines off the top/bottom edges
        t, b = a.trim
        src_im = src_im.crop((0, int(t), src_im.width, src_im.height - int(b)))
        a.boxes = [(b[0], b[1] - t) + tuple(b[2:]) for b in a.boxes]
    if a.margin:  # breathing room around the screenshot, in its own background colour
        m = int(a.margin)
        bgc = src_im.getpixel((2, 2))
        framed = Image.new("RGB", (src_im.width + 2 * m, src_im.height + 2 * m), bgc)
        framed.paste(src_im, (m, m))
        src_im = framed
        a.boxes = [(b[0] + m, b[1] + m) + tuple(b[2:]) for b in a.boxes]
    sw, sh = src_im.size
    if a.focus is None:  # push in toward the first highlight
        x, y, w, h = a.boxes[0][:4]
        a.focus = ((x + w / 2) / sw, (y + h / 2) / sh)
    # foreground width: screenshots sit with a margin; tall pictures fill the width
    fg_w = int(W * a.width)
    scale = fg_w / sw
    fg_h = int(sh * scale)
    if fg_h > H * 0.92:  # very tall: crop around the focus instead of shrinking the text
        keep = int(H * 0.92 / scale)
        fy = a.focus[1] * sh
        top = int(min(max(0, fy - keep / 2), sh - keep))
        src_im = src_im.crop((0, top, sw, top + keep))
        a.boxes = [(b[0], b[1] - top) + tuple(b[2:]) for b in a.boxes]
        a.focus = (a.focus[0], (fy - top) / keep)
        sw, sh = src_im.size
        fg_h = int(sh * scale)
    S = 2  # render at 2x then downscale per frame for crisp text
    canvas = Image.new("RGB", (W * S, H * S), (12, 12, 14))
    bsrc = Image.open(a.bg).convert("RGB") if a.bg else src_im  # e.g. a frame of court footage
    bw0, bh0 = bsrc.size
    bg = bsrc.resize((int(W * S * 1.0), int(W * S * bh0 / bw0)), Image.LANCZOS)
    if bg.height < H * S:
        bg = bsrc.resize((int(H * S * bw0 / bh0), H * S), Image.LANCZOS)
    bg = bg.crop(((bg.width - W * S) // 2, (bg.height - H * S) // 2, (bg.width - W * S) // 2 + W * S, (bg.height - H * S) // 2 + H * S))
    bg = bg.filter(ImageFilter.GaussianBlur(28 * S)).point(lambda v: int(v * a.dim))
    canvas.paste(bg, (0, 0))
    fg = src_im.resize((fg_w * S, fg_h * S), Image.LANCZOS)
    ox, oy = (W * S - fg_w * S) // 2, int((H * S - fg_h * S) * a.y)
    shadow = Image.new("RGBA", (fg.width + 60 * S, fg.height + 60 * S), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([30 * S, 30 * S, fg.width + 30 * S, fg.height + 30 * S], 18 * S, fill=(0, 0, 0, 150))
    canvas.paste(shadow.filter(ImageFilter.GaussianBlur(14 * S)), (ox - 30 * S, oy - 24 * S), shadow.filter(ImageFilter.GaussianBlur(14 * S)))
    mask = Image.new("L", fg.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, fg.width, fg.height], 14 * S, fill=255)
    canvas.paste(fg, (ox, oy), mask)
    # boxes in canvas (2x) coordinates
    boxes = [(ox + b[0] * scale * S, oy + b[1] * scale * S, b[2] * scale * S, b[3] * scale * S,
              b[4] if len(b) > 4 else a.mark_at) for b in a.boxes]
    fx, fy = ox + a.focus[0] * fg_w * S, oy + a.focus[1] * fg_h * S
    z0, z1 = a.zoom
    if boxes:  # never push in so far that a highlight leaves the frame
        widest = max(b[2] for b in boxes) + 2 * 30 * S
        z1 = max(z0, min(z1, (W * S * 0.97) / widest))
    n = int(round(a.len * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "17", "-preset", "medium",
                          "-pix_fmt", "yuv420p", a.out], stdin=subprocess.PIPE)
    ease = lambda t: t * t * (3 - 2 * t)
    for i in range(n):
        t = i / max(1, n - 1)
        z = z0 + (z1 - z0) * ease(t)
        cw, ch = W * S / z, H * S / z
        # drift the window toward the focus point as we zoom in
        q = (z - z0) / (z1 - z0) if abs(z1 - z0) > 1e-6 else ease(t)
        cx = W * S / 2 + (fx - W * S / 2) * q * 0.9
        cy = H * S / 2 + (fy - H * S / 2) * q * 0.9
        x0 = min(max(0, cx - cw / 2), W * S - cw)
        y0 = min(max(0, cy - ch / 2), H * S - ch)
        frame = canvas.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
        sec = i / FPS
        if boxes:
            d = ImageDraw.Draw(frame)
            for bx, by, bw, bh, bt in boxes:
                if sec < bt:
                    continue
                k = min(1.0, (sec - bt) / 0.22)  # quick draw-on
                X0, Y0 = (bx - x0) * W / cw, (by - y0) * H / ch
                X1, Y1 = (bx + bw - x0) * W / cw, (by + bh - y0) * H / ch
                padx, pady = 18 + (1 - k) * 40, 14 + (1 - k) * 30
                rect = [X0 - padx, Y0 - pady, X1 + padx, Y1 + pady]
                if a.circle:
                    d.ellipse(rect, outline=(255, 34, 34), width=9)
                else:
                    d.rounded_rectangle(rect, 10, outline=(255, 34, 34), width=8)
        p.stdin.write(frame.tobytes())
    p.stdin.close()
    p.wait()
    print(f"{a.out}  ({a.len:.1f}s page clip, zoom {z0}->{z1}, {len(boxes)} highlight(s))")


def cmd_circle(a):
    """Red circle on a finished 1080x1920 clip (the old MetaSports look): pops in at --from and stays."""
    from PIL import Image, ImageDraw
    tmp = tempfile.mkdtemp()
    try:
        cx, cy = (float(v) for v in a.at.split(","))
        w, h = (float(v) for v in a.size.split(","))
        pad = 12
        ring = Image.new("RGBA", (int(w) + 2 * pad, int(h) + 2 * pad), (0, 0, 0, 0))
        d = ImageDraw.Draw(ring)
        if a.box:
            d.rounded_rectangle([pad, pad, pad + w, pad + h], 14, outline=(0, 0, 0, 120), width=a.width + 6)
            d.rounded_rectangle([pad, pad, pad + w, pad + h], 14, outline=(255, 34, 34, 255), width=a.width)
        else:
            d.ellipse([pad, pad, pad + w, pad + h], outline=(0, 0, 0, 120), width=a.width + 6)
            d.ellipse([pad, pad, pad + w, pad + h], outline=(255, 34, 34, 255), width=a.width)
        png = os.path.join(tmp, "ring.png")
        ring.save(png)
        x, y = int(cx * 1080 - ring.width / 2), int(cy * 1920 - ring.height / 2)
        t0, t1 = a.start, a.start + 0.12
        # quick pop: 115% for 4 frames, then 100%
        big = ring.resize((int(ring.width * 1.15), int(ring.height * 1.15)), Image.LANCZOS)
        bpng = os.path.join(tmp, "ring_big.png")
        big.save(bpng)
        bx, by = int(cx * 1080 - big.width / 2), int(cy * 1920 - big.height / 2)
        end = f"lt(t,{a.until})" if a.until else "1"
        fc = (f"[0:v][2:v]overlay={bx}:{by}:enable='between(t,{t0},{t1})'[v1];"
              f"[v1][1:v]overlay={x}:{y}:enable='gte(t,{t1})*{end}'[v]")
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.source, "-loop", "1", "-i", png, "-loop", "1", "-i", bpng,
             "-filter_complex", fc, "-map", "[v]", "-t", f"{probe(a.source)[2]:.3f}", "-an", "-c:v", "libx264",
             "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", a.out])
        print(f"{a.out}  (red {'box' if a.box else 'circle'} at {a.at} from {a.start}s)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cmd_still(a):
    frames = int(a.len * 30)
    vf = (f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
          f"zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps=30,format=yuv420p")
    run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", a.source, "-vf", vf, "-frames:v", str(frames),
         "-c:v", "libx264", "-crf", "18", a.out])
    print(f"{a.out}  ({a.len:.1f}s slow zoom)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--n", type=int, default=12)
    p = sub.add_parser("sheet"); p.add_argument("source"); p.add_argument("--from", dest="start", type=float, default=0)
    p.add_argument("--to", dest="end", type=float, default=60); p.add_argument("--every", type=float, default=3)
    p.add_argument("--out", default="sheet.jpg")
    p = sub.add_parser("cut"); p.add_argument("source"); p.add_argument("--at", type=float, required=True)
    p.add_argument("--len", type=float, default=5); p.add_argument("--x", type=float, default=0.5); p.add_argument("--out", required=True)
    p.add_argument("--zoom", type=float, default=1.0); p.add_argument("--y", type=float, default=0.5)
    p.add_argument("--snap", action="store_true", help="start at the beginning of the camera shot that contains --at")
    p.add_argument("--flip", action="store_true", help="mirror left-right (fixes reversed text, e.g. an embroidery preview)")
    p.add_argument("--blurfit", action="store_true", help="keep the whole wide frame: full width over a blurred fill (story format)")
    p.add_argument("--blurfit-width", dest="blurfit_width", type=float, default=1.0, help="foreground width share for --blurfit")
    p.add_argument("--delogo", help="blur a channel logo: x,y,w,h as fractions of the source frame, e.g. 0.85,0.02,0.13,0.14")
    p = sub.add_parser("still"); p.add_argument("source"); p.add_argument("--len", type=float, default=5); p.add_argument("--out", required=True)
    p = sub.add_parser("page", help="a screenshot as a clip: push-in + red circle/box highlights")
    p.add_argument("source"); p.add_argument("--len", type=float, default=3); p.add_argument("--out", required=True)
    p.add_argument("--box", action="append", default=[], help="x,y,w,h in the picture's pixels (repeatable); webshot.mjs --mark prints these")
    p.add_argument("--circle", action="store_true", help="red ellipse instead of a box")
    p.add_argument("--focus", default="0.5,0.5", help="where to push in, 0-1 across,down the picture (default: the first box)")
    p.add_argument("--zoom", default="1.0,1.18", help="start,end zoom")
    p.add_argument("--width", type=float, default=0.94, help="picture width as a share of the frame")
    p.add_argument("--y", type=float, default=0.42, help="vertical placement 0=top 1=bottom")
    p.add_argument("--mark-at", dest="mark_at", type=float, default=0.35, help="second the highlight appears")
    p.add_argument("--trim", default="", help="top,bottom pixels to cut off the picture (half-visible lines)")
    p.add_argument("--margin", type=float, default=36, help="padding around the picture, in its pixels")
    p.add_argument("--dim", type=float, default=0.28, help="background brightness 0-1")
    p.add_argument("--bg", help="picture to blur behind the screenshot (e.g. a frame of the footage around it)")
    p = sub.add_parser("circle", help="red circle (or box) on a finished vertical clip, like the old Shorts")
    p.add_argument("source"); p.add_argument("--out", required=True)
    p.add_argument("--at", required=True, help="centre x,y as 0-1 of the vertical frame")
    p.add_argument("--size", default="260,260", help="width,height in pixels (of 1080x1920)")
    p.add_argument("--from", dest="start", type=float, default=0.3, help="second it pops in")
    p.add_argument("--until", type=float, default=0, help="second it disappears (0 = stays)")
    p.add_argument("--width", type=int, default=10, help="line thickness")
    p.add_argument("--box", action="store_true", help="rounded box instead of a circle")
    a = ap.parse_args()
    if a.cmd == "page":
        a.boxes = [tuple(float(v) for v in b.split(",")) for b in a.box]
        a.trim = tuple(float(v) for v in a.trim.split(",")) if a.trim else None
        a.zoom = tuple(float(v) for v in a.zoom.split(","))
        a.focus = None if (a.focus == "0.5,0.5" and a.boxes) else tuple(float(v) for v in a.focus.split(","))
    {"search": cmd_search, "sheet": cmd_sheet, "cut": cmd_cut, "still": cmd_still, "page": cmd_page,
     "circle": cmd_circle}[a.cmd](a)


if __name__ == "__main__":
    main()
