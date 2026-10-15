"""Footage quality check for one Short: is every shot sharp enough, not blown up too far, unique, flash-free and calm enough?

  python Tools/footage_qc.py "<Short folder>"            # reads shots.json + clips/, checks only the seconds each shot uses
  python Tools/footage_qc.py "<Short folder>" --json     # also writes _audit/footage_qc.json

Checks (Oct 15, 2026; thresholds calibrated on our own clips, see Library/Editing and Sound Standards.md section 6):
  UPSCALE    how much each shot is blown up from its source pixels, from the source log (sources.csv: "source WxH" and the
             crop zoom written by broll.py cut) times the shot's push-in. A full-height vertical crop of a 1080p landscape
             broadcast is 1.78x and is the house standard; a 720p source is 2.67x. Warn over 2.0x, FAIL over 3.0x. When the log
             has no source size the result is "unknown" (it is NOT guessed from pixels: a pixel-only upscale test was tried on
             Oct 15 and could not tell 1.8x from 2.7x on our compressed clips).
  SHARPNESS  variance of the Laplacian (edge contrast). Warn when a shot is far below the Short's own median (soft, smeared).
  DUPLICATES the same footage used twice under different file names (b7L / b7M, a1 / a1_df): perceptual hashes of the used
             seconds, compared across shots. qa_short.py only catches reuse of the same file.
  FLASHES    single washed-out or stray frames (Tools/deflash.py) inside the used seconds.
  MOTION     frame-to-frame change. Warn on the busiest seconds (top 10% of our 51 calibration clips: p90 change > 38 on a
             0-255 scale); warn on a push-in faster than 4% per second.
  CUTS       a hard cut inside the used seconds (the source's own edit). The footage after it may be another game: #21's a3
             montage cuts from a Kings game to a Warriors game at 1.8 s. Warn with the time so the verifier checks it.
Exit code 1 if any FAIL. It measures pixels; it cannot see a wrong jersey or scorebug: that is the human "verified" step.
"""
import json, os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
W, H = 1080, 1920


def frames(path, t0, dur, fps, w=W, h=H):
    """Gray frames of the used seconds, scaled the way assemble.py fills the 1080x1920 frame."""
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={fps},scale={w}:{h},format=gray"
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", path, "-vf", vf, "-f", "rawvideo", "-"]
    if path.lower().endswith((".png", ".jpg", ".jpeg")):
        cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", vf.replace(f",fps={fps}", ""), "-frames:v", "1", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32) if raw else np.zeros((0, h, w), np.float32)


def lapvar(img):
    import cv2
    return float(cv2.Laplacian(img, cv2.CV_32F, ksize=3).var())


def upscale_from_log(folder, clip, zoom_end):
    """Source pixels -> 1080x1920, from sources.csv ('source WxH' in notes, 'zoom Z' in crop). None when not logged."""
    import csv, re
    p = os.path.join(folder, "sources.csv")
    if not os.path.exists(p):
        return None, "no sources.csv"
    row = next((r for r in csv.DictReader(open(p, encoding="utf-8-sig")) if r.get("clip") == clip), None)
    if not row:
        return None, "no source-log row"
    m = re.search(r"source (\d+)x(\d+)", row.get("notes", "") + " " + row.get("source_res", ""))
    if not m:
        return None, "source size not logged"
    w, h = int(m.group(1)), int(m.group(2))
    z = re.search(r"zoom ([\d.]+)", row.get("crop", ""))
    z = float(z.group(1)) if z else 1.0
    if w / h > 9 / 16:
        f = 1920 * z / h
    else:
        f = max(1080 * z / w, 1920 * z / h)
    return round(f * (1 + zoom_end), 2), f"{w}x{h}, crop zoom {z}"


def dhash(img):
    import cv2
    s = cv2.resize(img, (9, 8), interpolation=cv2.INTER_AREA)
    return (s[:, 1:] > s[:, :-1]).flatten()


def segments(folder):
    shots = json.load(open(os.path.join(folder, "shots.json")))
    fin = os.path.join(folder, "final.mp4")
    total = None
    if os.path.exists(fin):
        total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", fin],
                                     capture_output=True, text=True).stdout or 0)
    out = []
    for i, s in enumerate(shots):
        end = shots[i + 1]["start"] if i + 1 < len(shots) else (total or s["start"] + 2.0)
        out.append((i + 1, s, float(s.get("in", 0) or 0), end - s["start"]))
    return out


def check(folder):
    from deflash import flashes
    segs = segments(folder)
    res, bad, warn = [], [], []
    hashes = []
    for n, s, t_in, dur in segs:
        clip = os.path.join(folder, "clips", s["clip"])
        if not os.path.exists(clip):
            bad.append(f"shot {n}: clip missing ({s['clip']})"); continue
        still = clip.lower().endswith((".png", ".jpg", ".jpeg")) or s.get("kind") == "card"
        fr = frames(clip, t_in, max(dur, 0.2), 4)
        if not len(fr):
            bad.append(f"shot {n} {s['clip']}: no frames decoded at {t_in:.2f}+{dur:.2f}s"); continue
        sharp = float(np.median([lapvar(f) for f in fr]))
        up, why = (None, "still/card") if still else upscale_from_log(folder, s["clip"], float(s.get("zoom", 0) or 0))
        row = {"shot": n, "clip": s["clip"], "kind": s.get("kind", ""), "in": t_in, "dur": round(dur, 2),
               "upscale": up, "upscale_basis": why, "sharpness": round(sharp, 1)}
        if not still:
            small = frames(clip, t_in, max(dur, 0.2), 30, 96, 170)
            if len(small) > 2:
                d = np.abs(np.diff(small, axis=0)).mean(axis=(1, 2))
                row["motion_med"] = round(float(np.median(d)), 1); row["motion_p90"] = round(float(np.percentile(d, 90)), 1)
                med = float(np.median(d)) or 1.0
                # a hard cut inside the used seconds (the source's own edit): the footage after it may be another game
                row["internal_cuts"] = [round(t_in + (k + 1) / 30, 2) for k, x in enumerate(d) if x > 45 and x > 3.5 * med]
            fl = flashes_in(clip, t_in, dur, flashes)
            row["flashes"] = fl
            z = float(s.get("zoom", 0) or 0)
            row["zoom_per_s"] = round(z / dur, 3) if dur > 0 else 0
        for k, f in enumerate(fr):
            if f.std() > 8:  # skip flat frames (black, fades): they all look alike
                hashes.append((n, s["clip"], round(t_in + k / 4, 2), dhash(f)))
        res.append(row)
    # judgments
    sharp_med = float(np.median([r["sharpness"] for r in res if r["kind"] != "card"] or [1]))
    for r in res:
        tag = f"shot {r['shot']} {r['clip']}"
        if r["upscale"] is not None:
            if r["upscale"] > 3.0:
                bad.append(f"{tag}: blown up {r['upscale']}x from its source ({r['upscale_basis']}): find a 1080p+ source or crop less")
            elif r["upscale"] > 2.0:
                warn.append(f"{tag}: blown up {r['upscale']}x ({r['upscale_basis']}; house standard is a 1080p source, about 1.8x): note in PACKAGE.md that no better source exists")
        if r["kind"] != "card" and r["sharpness"] < 0.35 * sharp_med:
            warn.append(f"{tag}: soft (edge contrast {r['sharpness']:.0f} vs this Short's median {sharp_med:.0f}): motion blur or a poor encode")
        if r.get("flashes"):
            bad.append(f"{tag}: one-frame flash at {r['flashes']} s into the clip: run Tools/deflash.py on it")
        if r.get("motion_p90", 0) > 38:
            warn.append(f"{tag}: very busy picture (90th-percentile frame change {r['motion_p90']}; top 10% of our clips): fast action, a whip pan or shake; check it reads on a phone")
        if r.get("internal_cuts"):
            warn.append(f"{tag}: the clip cuts to other footage at {r['internal_cuts']} s (clip time): check the footage after the cut still matches the line (player, game, scorebug)")
        if r.get("zoom_per_s", 0) > 0.04:
            warn.append(f"{tag}: push-in {r['zoom_per_s'] * 100:.1f}% per second (house limit 4%/s; subtle reads better)")
    dups = {}
    for i in range(len(hashes)):
        for j in range(i + 1, len(hashes)):
            a, b = hashes[i], hashes[j]
            if a[0] == b[0] or a[1] == b[1]:
                continue  # same shot, or the same file (qa_short.py handles same-file reuse)
            if int((a[3] != b[3]).sum()) <= 4:
                dups.setdefault((a[0], a[1], b[0], b[1]), []).append((a[2], b[2]))
    for (n1, c1, n2, c2), m in dups.items():
        if len(m) >= 2:
            bad.append(f"the same footage appears in shot {n1} ({c1}) and shot {n2} ({c2}) ({len(m)} matching frames, e.g. {m[0][0]}s / {m[0][1]}s): use different footage, or mark a deliberate replay")
    unk = [r["clip"] for r in res if r["upscale"] is None and r["upscale_basis"] != "still/card"]
    if unk:
        warn.append(f"source size unknown for {len(unk)} clip(s) ({', '.join(unk[:6])}): cut new clips with broll.py cut (it logs it) or add 'source WxH' to their notes")
    return res, bad, warn


def flashes_in(clip, t_in, dur, flashes):
    tmp = os.path.join("/tmp", f"_fqc_{os.getpid()}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t_in - 0.05):.3f}", "-t", f"{dur + 0.1:.3f}", "-i", clip,
                    "-an", "-c:v", "libx264", "-crf", "12", "-preset", "ultrafast", tmp], capture_output=True)
    try:
        fps = 30.0
        out = [round(i / fps + max(0, t_in - 0.05), 2) for i in flashes(tmp)]
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    return out


def main():
    folder = sys.argv[1]
    res, bad, warn = check(folder)
    print(f"{'shot':>4} {'clip':22} {'kind':6} {'dur':>5} {'upscale':>8} {'sharp':>7} {'motion':>6} {'zoom/s':>6}")
    for r in res:
        print(f"{r['shot']:>4} {r['clip'][:22]:22} {r['kind'][:6]:6} {r['dur']:>5} {str(r['upscale'] or '?'):>8} {r['sharpness']:>7} "
              f"{str(r.get('motion_p90', '')):>6} {str(r.get('zoom_per_s', '')):>6}")
    print("FAIL" if bad else "PASS")
    for x in warn:
        print("  warn", x)
    for x in bad:
        print("  FIX ", x)
    if "--json" in sys.argv:
        os.makedirs(os.path.join(folder, "_audit"), exist_ok=True)
        json.dump({"shots": res, "fail": bad, "warn": warn}, open(os.path.join(folder, "_audit", "footage_qc.json"), "w"), indent=1)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
