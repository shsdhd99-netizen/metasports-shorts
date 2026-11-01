"""Viewer-comfort and retention audit of a finished Short (Oct 30, 2026; owner: "always edit for best retention and viewer comfort").

qa_short.py --full is the gate (length, captions, flashes, softness, upscale). This adds what it doesn't measure:
  - loudness jumps that make a viewer flinch (a live broadcast call or an effect much louder than the voice before it),
    true peak, and quiet holes;
  - shot lengths (a cut under 0.45 s is hard to read; a shot over 4 s with nothing new is where people swipe);
  - frozen picture;
  - caption reading speed (characters per second per caption event).

    python Tools/comfort_audit.py <video.mp4> [--ass captions.ass] [--json out.json]

Prints one line per finding and a summary. Thresholds are starting points [H], not proven rules.
"""
import argparse, json, re, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def loudness(path):
    """Momentary (400 ms) and short-term (3 s) loudness every 0.1 s, plus integrated and true peak."""
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"])
    pts = []
    for m in re.finditer(r"t:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)\s+S:\s*(-?[\d.]+)", err):
        pts.append((float(m.group(1)), float(m.group(2)), float(m.group(3))))
    integ = re.search(r"Integrated loudness:\s*I:\s*(-?[\d.]+)", err)
    peak = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+)", err)
    return pts, float(integ.group(1)) if integ else None, float(peak.group(1)) if peak else None


def startles(pts, rise=7.0):
    """A jump: momentary loudness rises `rise` LU above the median of the previous 1.5 s within 0.5 s, and lands above -18 LUFS."""
    out, last = [], -9
    for i, (t, m, s) in enumerate(pts):
        prev = [p[1] for p in pts if t - 2.0 <= p[0] < t - 0.5 and p[1] > -60]
        if len(prev) < 5 or m < -18:
            continue
        base = sorted(prev)[len(prev) // 2]
        if m - base >= rise and t - last > 1.5:
            out.append((t, round(m - base, 1), m))
            last = t
    return out


def holes(pts, dur, floor=-40.0, min_len=0.35):
    out, start = [], None
    for t, m, s in pts:
        if m < floor and start is None:
            start = t
        elif m >= floor and start is not None:
            if t - start >= min_len and t < dur - 0.6 and start > 0.5:
                out.append((round(start, 2), round(t - start, 2)))
            start = None
    return out


def shots(path, thr=0.30):
    err = run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-"])
    cuts = [float(x) for x in re.findall(r"pts_time:([\d.]+)", err)]
    return cuts


def freezes(path):
    err = run(["ffmpeg", "-hide_banner", "-i", path, "-vf", "freezedetect=n=0.003:d=0.6", "-an", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", err)]
    durs = [float(x) for x in re.findall(r"freeze_duration: ([\d.]+)", err)]
    return list(zip(starts, durs))


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout
    return float(out.strip() or 0)


def ass_events(path):
    ev = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("Dialogue:"):
            continue
        parts = line.split(",", 9)
        def ts(x):
            h, m, s = x.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
        text = re.sub(r"\{[^}]*\}", "", parts[9]).replace("\\N", " ").strip()
        ev.append((ts(parts[1]), ts(parts[2]), text))
    # karaoke styles repeat a line per highlighted word: merge identical consecutive texts
    merged = []
    for a, b, t in ev:
        if merged and merged[-1][2] == t and abs(merged[-1][1] - a) < 0.05:
            merged[-1] = (merged[-1][0], b, t)
        else:
            merged.append((a, b, t))
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--ass")
    ap.add_argument("--json")
    a = ap.parse_args()
    dur = duration(a.video)
    find = []
    pts, integ, peak = loudness(a.video)
    for t, jump, m in startles(pts):
        find.append(("loud-jump", t, f"+{jump} LU in under 0.5 s (to {m} LUFS momentary)"))
    for t, ln in holes(pts, dur):
        find.append(("quiet-hole", t, f"{ln} s near silence"))
    if peak is not None and peak > -1.0:
        find.append(("peak", 0, f"true peak {peak} dBTP (over -1)"))
    if integ is not None and not (-16.5 <= integ <= -12.5):
        find.append(("loudness", 0, f"integrated {integ} LUFS (target about -14)"))
    loud_m = sorted([p[1] for p in pts if p[1] > -60])
    cuts = shots(a.video)
    bounds = [0.0] + cuts + [dur]
    lens = [(round(bounds[i], 2), round(bounds[i + 1] - bounds[i], 2)) for i in range(len(bounds) - 1)]
    for st, ln in lens:
        if ln < 0.45 and st > 0.2 and st < dur - 0.5:
            find.append(("fast-cut", st, f"shot lasts {ln} s"))
        if ln > 4.0:
            find.append(("long-shot", st, f"shot lasts {ln} s (check something new happens)"))
    for st, ln in freezes(a.video):
        if st < dur - 0.7:
            find.append(("freeze", st, f"picture frozen {round(ln, 2)} s"))
    if a.ass:
        for s, e, t in ass_events(a.ass):
            d = e - s
            cps = len(t) / d if d > 0 else 99
            if d < 0.25 and len(t) > 3:
                find.append(("caption-flash", s, f"'{t}' shows only {d:.2f} s"))
            elif cps > 22:
                find.append(("caption-fast", s, f"'{t}' {cps:.0f} chars/s"))
    find.sort(key=lambda x: x[1])
    for kind, t, msg in find:
        print(f"{t:6.2f}s  {kind:13s} {msg}")
    avg = sum(l for _, l in lens) / max(1, len(lens))
    p95 = loud_m[int(len(loud_m) * 0.95)] if loud_m else None
    p50 = loud_m[len(loud_m) // 2] if loud_m else None
    print(f"SUMMARY {dur:.1f} s | {len(lens)} shots, avg {avg:.2f} s | integrated {integ} LUFS, true peak {peak} dBTP | "
          f"momentary median {p50}, 95th pct {p95} (spread {round(p95 - p50, 1) if p50 is not None else '?'} LU) | {len(find)} findings")
    if a.json:
        json.dump({"duration": dur, "findings": find, "shots": lens, "integrated": integ, "true_peak": peak,
                   "momentary_p50": p50, "momentary_p95": p95}, open(a.json, "w"), indent=1)


if __name__ == "__main__":
    main()
