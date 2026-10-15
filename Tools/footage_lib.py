"""Footage library and source logs for MetaSports Shorts (Oct 14, 2026). See Library/B-roll Sourcing Guide.md.

  python footage_lib.py log    <folder>                    # create/refresh <folder>/sources.csv: one row per clip in shots.json
  python footage_lib.py match  <folder> --src DIR [DIR..]  # find which downloaded post (and which second) each clip came from
  python footage_lib.py sheet  <folder> [clip ...]         # contact sheets of the USED part of each clip -> _audit/clips/*.jpg
  python footage_lib.py verify <folder> <clip> "what it shows" [--no]   # record that you watched it and it matches the line
  python footage_lib.py index                              # every clip in every production -> Library/footage_library.csv
  python footage_lib.py search jokic pass                  # look up reusable footage in the index

Source files named <X post id>.mp4 (what x_clip.py saves) map back to https://x.com/i/status/<id>.
Matching compares small grey thumbnails of the clip with vertical crops of every source frame (several zooms and
positions), so it finds the post and the second even after cropping. A score of 0.80+ is a match, 0.70-0.80 is logged as "probable: <url>" (confirm by eye), under 0.70 is "no match".
"""
import argparse, csv, datetime, glob, json, os, re, subprocess, sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PROD = os.path.join(ROOT, "Productions")
INDEX = os.path.join(ROOT, "Library", "footage_library.csv")
COLS = ["clip", "kind", "used_at_s", "used_for_line", "what_it_shows", "source_url", "source_account", "source_date",
        "source_in_s", "source_out_s", "crop", "match_score", "licence_risk", "verified", "verified_on", "notes"]
STILL = (".png", ".jpg", ".jpeg")


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                        "-of", "json", p], capture_output=True, text=True)
    j = json.loads(r.stdout or "{}")
    s = (j.get("streams") or [{}])[0]
    return float(j.get("format", {}).get("duration", 0) or 0), s.get("width", 0), s.get("height", 0)


def load_shots(folder):
    shots = json.load(open(os.path.join(folder, "shots.json"), encoding="utf-8-sig"))
    w = json.load(open(os.path.join(folder, "words.json"), encoding="utf-8-sig"))
    w = w["words"] if isinstance(w, dict) else w
    total = w[-1]["end"] + 0.4
    out = []
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else total
        line = " ".join(x["word"] for x in w if s["start"] - 0.02 <= x["start"] < end - 0.02)
        out.append(dict(s, end=end, line=line))
    return out


def read_log(folder):
    p = os.path.join(folder, "sources.csv")
    return {r["clip"]: r for r in csv.DictReader(open(p, encoding="utf-8-sig"))} if os.path.exists(p) else {}


def write_log(folder, rows):
    p = os.path.join(folder, "sources.csv")
    w = csv.DictWriter(open(p, "w", encoding="utf-8", newline=""), fieldnames=COLS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in COLS})
    return p


def cmd_log(a):
    F = a.folder
    old = read_log(F)
    rows, seen = [], set()
    for s in load_shots(F):
        c = s["clip"]
        if c in seen:  # one row per clip; the loop shot reuses the first clip
            r = next(x for x in rows if x["clip"] == c)
            r["used_at_s"] += f"; {s['start']:.2f}"
            continue
        seen.add(c)
        r = dict(old.get(c, {}))
        r.update(clip=c, kind=s.get("kind", ""), used_at_s=f"{s['start']:.2f}", used_for_line=s["line"])
        if c.startswith(("c_", "c2", "c21", "src_")) or s.get("kind") == "card":  # our cards; p_ photos are third-party and need a source
            r.setdefault("licence_risk", "own graphic (text/screenshot we made; screenshot sources in notes.md)")
            if not r.get("source_url"):
                r["source_url"] = "made in-house (see notes.md for the page it quotes)"
        r.setdefault("what_it_shows", s.get("why", ""))
        rows.append(r)
    print(write_log(F, rows), f"({len(rows)} clips)")


def gray_frames(path, fps, h):
    d, w0, h0 = probe(path)
    if not w0:
        return np.zeros((0, h, 1)), d, 1.0
    w = int(round(w0 * h / h0 / 2)) * 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    n = len(raw) // (w * h)
    return np.frombuffer(raw[:n * w * h], np.uint8).reshape(n, h, w).astype(np.float32), d, w0 / h0


def norm(x):
    x = x - x.mean(axis=(-2, -1), keepdims=True)
    return x / (np.sqrt((x ** 2).sum(axis=(-2, -1), keepdims=True)) + 1e-6)


def resize(img, h, w):
    ys = (np.arange(h) + 0.5) * img.shape[-2] / h
    xs = (np.arange(w) + 0.5) * img.shape[-1] / w
    return img[..., ys.astype(int)[:, None], xs.astype(int)[None, :]]


def clip_thumb(path, at):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{at:.2f}", "-i", path, "-frames:v", "1", "-vf", "scale=18:32,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    return norm(np.frombuffer(raw[:576], np.uint8).reshape(32, 18).astype(np.float32)) if len(raw) >= 576 else None


def source_crops(src, fps=4):
    """All vertical crops of every sampled frame of one source: (array [crops, frames, 32, 18], labels)."""
    fr, dur, asp = gray_frames(src, fps, 96)
    if not len(fr):
        return None, []
    H, W = fr.shape[1:]
    arrs, labels = [], []
    for z in (1.0, 1.25, 1.6, 2.0):
        ch = int(H / z) if asp >= 0.7 else int(W * 16 / 9 / z)  # vertical sources: crop inside banners/letterbox too
        ch = min(ch, H); cw = min(W, int(ch * 9 / 16))
        for y0 in sorted({(H - ch) // 2, max(0, (H - ch) // 4), max(0, 3 * (H - ch) // 4)}):
            for x0 in range(0, max(1, W - cw + 1), 4):
                arrs.append(norm(resize(fr[:, y0:y0 + ch, x0:x0 + cw], 32, 18)))
                labels.append((z, x0, y0, cw, ch))
    return np.stack(arrs), labels


def refine(src, crop, t_guess, th, tmid, fps=15):
    """Re-score one source and crop at 15 fps within 1.5 s of the coarse match."""
    z, x0, y0, cw, ch = crop
    a = max(0.0, t_guess - 1.5)
    d, w0, h0 = probe(src)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{a:.2f}", "-t", "3", "-i", src, "-vf",
                          f"fps={fps},scale=-2:96,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    W = int(round(w0 * 96 / h0 / 2)) * 2
    n = len(raw) // (W * 96)
    if not n:
        return -1, t_guess
    fr = np.frombuffer(raw[:n * W * 96], np.uint8).reshape(n, 96, W).astype(np.float32)
    sc = (norm(resize(fr[:, y0:y0 + ch, x0:x0 + cw], 32, 18)) * th).sum(axis=(1, 2))
    i = int(np.argmax(sc))
    return float(sc[i]), a + i / fps


def cmd_match(a):
    F = a.folder
    rows = read_log(F)
    if not rows:
        cmd_log(argparse.Namespace(folder=F)); rows = read_log(F)
    srcs = sorted(p for d in a.src for p in glob.glob(os.path.join(d, "*.mp4")))
    shots = {s["clip"]: s for s in reversed(load_shots(F))}
    todo = {}
    for c, r in rows.items():
        p = os.path.join(F, "clips", c)
        if c.lower().endswith(STILL) or not os.path.exists(p) or r.get("source_url", "").startswith("made in-house"):
            continue
        s = shots[c]; cin = float(s.get("in", 0) or 0); length = s["end"] - s["start"]
        th = clip_thumb(p, cin + length / 2)
        if th is not None:
            todo[c] = (th, cin + length / 2, cin, length)
    best = {c: (-1, 0, "", "") for c in todo}
    fps = 4
    for sp in srcs:  # decode each source once, compare every clip against it
        arr, labels = source_crops(sp, fps)
        if arr is None:
            continue
        for c, (th, tmid, cin, length) in todo.items():
            sc = (arr * th).sum(axis=(2, 3))  # [crops, frames]
            k, i = np.unravel_index(int(np.argmax(sc)), sc.shape)
            if sc[k, i] > best[c][0]:
                best[c] = (float(sc[k, i]), i / fps - tmid, labels[k], sp)
    for c, (score, off, crop, sp) in best.items():
        r = rows[c]; th, tmid, cin, length = todo[c]
        if sp:
            s2, t_mid_src = refine(sp, crop, tmid + off, th, tmid)
            if s2 > score:
                score, off = s2, t_mid_src - tmid
        z, x0, y0, cw, ch = crop if crop else (0, 0, 0, 0, 0)
        crop = f"zoom {z} x {x0}..{x0 + cw} y {y0}..{y0 + ch} of the 96-px-high frame" if crop else ""
        sid = os.path.splitext(os.path.basename(sp))[0] if sp else ""
        url = f"https://x.com/i/status/{sid}" if sid.isdigit() else os.path.basename(sp or "")
        if score < 0.70:
            r.update(match_score=f"{score:.2f}")
            print(f"{c:18} no match (best {score:.2f} in {os.path.basename(sp) if sp else '-'})")
            continue
        if score < 0.80:  # same post, different crop/zoom than we search: keep it, flagged for a human look
            src_in = max(0.0, cin + off)
            r.update(source_url="probable: " + url, source_in_s=f"{src_in:.1f}", match_score=f"{score:.2f}")
            print(f"{c:18} probable {score:.2f} {url} at {src_in:.1f}s (confirm by eye)")
            continue
        src_in = max(0.0, cin + off)
        r.update(source_url=url, source_in_s=f"{src_in:.1f}", source_out_s=f"{src_in + length:.1f}", crop=crop, match_score=f"{score:.2f}")
        print(f"{c:18} {score:.2f} {url} at {src_in:.1f}s ({crop})")
    write_log(F, list(rows.values()))


def cmd_sheet(a):
    F = a.folder
    out = os.path.join(F, "_audit", "clips"); os.makedirs(out, exist_ok=True)
    shots = load_shots(F)
    want = set(a.clips or [s["clip"] for s in shots])
    for s in shots:
        if s["clip"] not in want or s["clip"].lower().endswith(STILL):
            continue
        want.discard(s["clip"])
        p = os.path.join(F, "clips", s["clip"])
        cin = float(s.get("in", 0) or 0); length = s["end"] - s["start"]
        cdur = probe(p)[0] or (cin + length)
        last = min(cin + length, cdur) - 0.05
        ts = [cin + (last - cin) * k / 5 for k in range(6)]  # 6 frames across the part that is actually used
        tiles = []
        for k, t in enumerate(ts):
            f = os.path.join(out, f"_t{k}.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t):.2f}", "-i", p, "-frames:v", "1", "-vf",
                            f"scale=216:384,drawtext=text='{t:.1f}':x=4:y=4:fontsize=22:fontcolor=yellow:box=1:boxcolor=black", f])
            if os.path.exists(f):
                tiles.append(f)
        if len(tiles) < 2:
            print("  could not read frames from", s["clip"]); continue
        dst = os.path.join(out, os.path.splitext(s["clip"])[0] + ".jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-y"] + sum([["-i", t] for t in tiles], []) +
                       ["-filter_complex", "".join(f"[{i}]" for i in range(len(tiles))) + f"hstack={len(tiles)}", dst])
        for t in tiles:
            os.remove(t)
        print(dst, "|", s["line"])


def cmd_verify(a):
    rows = read_log(a.folder)
    if a.clip not in rows:
        raise SystemExit(f"{a.clip} is not in sources.csv (run: footage_lib.py log)")
    rows[a.clip].update(what_it_shows=a.shows, verified="no" if a.no else "yes", verified_on=datetime.date.today().isoformat())
    write_log(a.folder, list(rows.values()))
    print(a.clip, "verified" if not a.no else "REJECTED", "-", a.shows)


def cmd_index(a):
    rows = []
    for F in sorted(glob.glob(os.path.join(PROD, "*", "*"))):
        cd = os.path.join(F, "clips")
        if not os.path.isdir(cd):
            continue
        log = read_log(F)
        used = {}
        if os.path.exists(os.path.join(F, "shots.json")) and os.path.exists(os.path.join(F, "words.json")):
            try:
                for s in load_shots(F):
                    used.setdefault(s["clip"], (s["line"], s.get("why", "")))
            except Exception:
                pass
        for p in sorted(glob.glob(os.path.join(cd, "*"))):
            c = os.path.basename(p)
            if not c.lower().endswith((".mp4", ".mov") + STILL):
                continue
            d, w, h = probe(p) if not c.lower().endswith(STILL) else (0, 0, 0)
            r = log.get(c, {})
            rows.append({"production": os.path.relpath(F, PROD).replace("\\", "/"), "clip": c, "seconds": f"{d:.1f}", "size": f"{w}x{h}",
                         "used": "yes" if c in used else "no", "used_for_line": used.get(c, ("", ""))[0],
                         "what_it_shows": r.get("what_it_shows") or used.get(c, ("", ""))[1], "source_url": r.get("source_url", ""),
                         "source_in_s": r.get("source_in_s", ""), "verified": r.get("verified", "")})
    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    cols = ["production", "clip", "seconds", "size", "used", "used_for_line", "what_it_shows", "source_url", "source_in_s", "verified"]
    w = csv.DictWriter(open(INDEX, "w", encoding="utf-8", newline=""), fieldnames=cols)
    w.writeheader(); w.writerows(rows)
    print(INDEX, len(rows), "clips,", sum(r["verified"] == "yes" for r in rows), "verified")


def cmd_search(a):
    q = [t.lower() for t in a.terms]
    for r in csv.DictReader(open(INDEX, encoding="utf-8")):
        hay = " ".join(r.values()).lower()
        if all(t in hay for t in q):
            print(f"{r['production'][:44]:44} {r['clip']:16} {r['seconds']:>5}s {r['verified'] or '-':3} {r['what_it_shows'][:70]}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("log"); p.add_argument("folder")
    p = sub.add_parser("match"); p.add_argument("folder"); p.add_argument("--src", nargs="+", required=True)
    p = sub.add_parser("sheet"); p.add_argument("folder"); p.add_argument("clips", nargs="*")
    p = sub.add_parser("verify"); p.add_argument("folder"); p.add_argument("clip"); p.add_argument("shows"); p.add_argument("--no", action="store_true")
    sub.add_parser("index")
    p = sub.add_parser("search"); p.add_argument("terms", nargs="+")
    a = ap.parse_args()
    {"log": cmd_log, "match": cmd_match, "sheet": cmd_sheet, "verify": cmd_verify, "index": cmd_index, "search": cmd_search}[a.cmd](a)


if __name__ == "__main__":
    main()
