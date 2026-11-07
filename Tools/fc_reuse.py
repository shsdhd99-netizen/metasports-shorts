"""Clip-reuse measurement for story Shorts (Nov 4, 2026). Used by edit_lint.py (guard) and the FC Clip Repetition Study.

  python Tools/fc_reuse.py                      # table for every Soccer Channel/Productions/* folder with cuts.json
  python Tools/fc_reuse.py --visual             # adds a picture-level repeat count from the rendered DRAFT/final mp4 (dhash, 2 fps)

Metadata measures (from cuts.json):
  overlap_pairs   pairs of shots whose source file AND time range overlap (same footage twice); `replay: true` on the LATER shot excuses it
  max_src_share   largest share of the runtime taken by one source file (long matches are normal, so this is only a warning above 35%)
  consec_same     number of back-to-back shots from the same source file
  min_gap_s       shortest time between two shots that overlap (the viewer sees the same moment again after this long)
Visual measure: frames sampled at 2 fps, 8x8 difference hash of the centre crop; a "repeat" is a frame within 6 bits of one at least 3 s earlier.
"""
import glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def timeline(shots, starts=None, total_len=None):
    """starts: optional list of shot start times from shots.json (the on-screen timeline); cuts.json `len` includes handles and
    overstates runtime by 5-20%, so use starts when given."""
    t, out = 0.0, []
    for i, s in enumerate(shots):
        ln = float(s.get("len") or 0)
        if starts and len(starts) == len(shots):
            t = float(starts[i])
            nxt = float(starts[i + 1]) if i + 1 < len(shots) else (total_len or t + ln)
            ln_view = max(0.0, nxt - t)
        else:
            ln_view = ln
        src = s.get("src") or (("stock:%s" % s["stock"]) if s.get("stock") else (("still:%s" % s["still"]) if s.get("still") else None))
        at = float(s.get("at") or 0)
        span = ln * float(s.get("speed") or 1.0) if s.get("src") else ln
        out.append({"clip": s.get("clip"), "src": src, "at": at, "end": at + span, "t0": t, "t1": t + ln_view, "replay": bool(s.get("replay")),
                    "still": bool(s.get("still"))})
        if not (starts and len(starts) == len(shots)):
            t += ln
    return out, (out[-1]["t1"] if out else 0.0)


def reuse(shots, starts=None, total_len=None):
    tl, total = timeline(shots, starts, total_len)
    pairs, gaps, consec, share = [], [], 0, {}
    for i, a in enumerate(tl):
        if a["src"]:
            share[a["src"]] = share.get(a["src"], 0.0) + (a["t1"] - a["t0"])
        if i and a["src"] and a["src"] == tl[i - 1]["src"] and not a["still"]:
            consec += 1
        for b in tl[:i]:
            if a["src"] and a["src"] == b["src"] and a["end"] > b["at"] + 0.05 and b["end"] > a["at"] + 0.05:
                pairs.append((b["clip"], a["clip"], a["replay"]))
                gaps.append(a["t0"] - b["t1"])
    unexcused = [p for p in pairs if not p[2]]
    top = max(share.items(), key=lambda kv: kv[1]) if share else (None, 0.0)
    lens = [x["t1"] - x["t0"] for x in tl]
    return {"shots": len(tl), "runtime": total, "mean_shot": total / max(1, len(tl)), "overlap_pairs": len(pairs),
            "unexcused": unexcused, "n_unexcused": len(unexcused), "max_src": top[0], "max_src_s": top[1],
            "max_src_share": top[1] / total if total else 0.0, "consec_same": consec, "min_gap_s": min(gaps) if gaps else None,
            "longest_on_one_src_s": top[1]}


def visual_repeats(mp4, fps=2, minsep=3.0, thr=6):
    import numpy as np
    w, h = 9, 8
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-vf", f"fps={fps},crop=iw:ih*0.5:0:ih*0.12,scale={w}:{h},format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.int16)
    bits = (fr[:, :, 1:] > fr[:, :, :-1]).reshape(len(fr), -1)
    # ignore near-flat frames (cards, black): need contrast
    contrast = fr.reshape(len(fr), -1).std(1)
    rep, first = 0, None
    for i in range(len(bits)):
        if contrast[i] < 6:
            continue
        j0 = int(i - minsep * fps)
        if j0 >= 0:
            d = (bits[:j0 + 1] != bits[i]).sum(1)
            ok = (d <= thr) & (contrast[:j0 + 1] >= 6)
            if ok.any():
                rep += 1
                first = first or i / fps
    return rep, len(bits), first


def load_starts(d):
    p = os.path.join(d, "shots.json")
    try:
        return [float(x.get("start")) for x in json.load(open(p, encoding="utf-8"))]
    except Exception:
        return None


def folders():
    return sorted(d for d in glob.glob(os.path.join(ROOT, "Soccer Channel", "Productions", "*")) if os.path.exists(os.path.join(d, "cuts.json")))


def draft(d):
    c = [p for p in glob.glob(os.path.join(d, "*.mp4")) if "nocap" not in p and "(music)" in p] or \
        [p for p in glob.glob(os.path.join(d, "*.mp4")) if os.path.basename(p).startswith(("final_music", "final_nomusic"))]
    return c[0] if c else None


if __name__ == "__main__":
    vis = "--visual" in sys.argv
    print("folder|shots|runtime|mean_shot|overlap_pairs|unexcused|max_src_share|consec_same|min_gap_s" + ("|visual_repeats|frames" if vis else ""))
    for d in folders():
        r = reuse(json.load(open(os.path.join(d, "cuts.json"), encoding="utf-8"))["shots"], load_starts(d))
        line = f"{os.path.basename(d)[:40]}|{r['shots']}|{r['runtime']:.1f}|{r['mean_shot']:.2f}|{r['overlap_pairs']}|{r['n_unexcused']}|{r['max_src_share']:.2f}|{r['consec_same']}|{r['min_gap_s'] if r['min_gap_s'] is None else round(r['min_gap_s'],1)}"
        if vis:
            m = draft(d)
            if m:
                v = visual_repeats(m)
                line += f"|{v[0]}|{v[1]}"
            else:
                line += "|n/a|0"
        print(line, flush=True)
