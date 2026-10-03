"""Splice helpers shared by the EDL builder and the ASR-verified join search.
A join removes source audio between a (end of the kept audio on the left) and b (start of the kept audio on the right)
and blends 10 ms around each point. In voiced speech b is nudged by up to +-4 ms so the pitch cycles line up
(waveform-similarity alignment, as in WSOLA/PSOLA splicing) which removes the click a plain crossfade can leave."""
import numpy as np

SR = 48000
F = int(0.010 * SR)              # crossfade length (samples)


def ncc(x, y):
    x = x - x.mean(); y = y - y.mean()
    return float((x * y).sum() / (np.sqrt((x * x).sum() * (y * y).sum()) + 1e-12))


def align_b(enh, a, b, search=0.004):
    """shift b (seconds) within +-search so the signal around b continues the signal around a; returns (b', ncc)"""
    ia = int(round(a * SR)); ib0 = int(round(b * SR)); h = F // 2
    tail = enh[ia - h: ia + h].astype(np.float64)
    best = (-2.0, ib0)
    for d in range(-int(search * SR), int(search * SR) + 1):
        c = ncc(tail, enh[ib0 + d - h: ib0 + d + h].astype(np.float64))
        if c > best[0]: best = (c, ib0 + d)
    return best[1] / SR, best[0]


def blend(tail, head, c):
    """equal-power for uncorrelated material, amplitude-preserving (linear) when the two sides are coherent"""
    t = np.linspace(0, 1, len(tail))
    lin = tail * (1 - t) + head * t
    eqp = tail * np.cos(t * np.pi / 2) + head * np.sin(t * np.pi / 2)
    w = float(np.clip((c - 0.3) / 0.4, 0, 1))        # 0 below ncc 0.3, 1 above 0.7
    return w * lin + (1 - w) * eqp


def assemble(enh, segs, joins, fade_in=0.010, fade_out=0.060):
    """segs[k] = (src_start, src_end) of kept audio k; joins[k] = (a, b) with a == segs[k][1], b == segs[k+1][0].
    returns (audio float64, seg_map[(src_lo, src_hi, out_start)])"""
    out, seg_map, cur = [], [], 0
    for k, (s0, e0) in enumerate(segs):
        i0, i1 = int(round(s0 * SR)), int(round(e0 * SR))
        lo = i0 + (F // 2 if k > 0 else 0)
        hi = i1 - (F // 2 if k < len(segs) - 1 else 0)
        chunk = enh[lo:hi].astype(np.float64).copy()
        if k == 0 and fade_in:
            fi = int(fade_in * SR); chunk[:fi] *= 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, fi))
        if k == len(segs) - 1 and fade_out:
            fo = int(fade_out * SR); chunk[-fo:] *= 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, fo))
        seg_map.append((lo / SR, hi / SR, cur / SR))
        out.append(chunk); cur += len(chunk)
        if k < len(segs) - 1:
            ja, jb = int(round(joins[k][0] * SR)), int(round(joins[k][1] * SR))
            tail = enh[ja - F // 2: ja + F // 2].astype(np.float64)
            head = enh[jb - F // 2: jb + F // 2].astype(np.float64)
            xf = blend(tail, head, ncc(tail, head))
            out.append(xf); cur += len(xf)
    return np.concatenate(out), seg_map
