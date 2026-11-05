"""Pack a DRAFT for the Hub: re-encode under the 20 MiB asset cap and verify it with qa_short (Nov 5, 2026; backlog item).

  python Tools/hub_pack.py "Productions/MetaSports/<folder>" [more folders]  [--skip-qa] [--cap-mb 19.5]

Reads the DRAFT*.mp4 (or final.mp4) in each folder, writes <folder>/_hub/s.mp4 (h264 crf 28, aac 96k, +faststart; crf goes up by 2 until the
file is under the cap, max crf 36), then runs qa_short.py --full on the packed file so a bad re-encode (lost sync, clipped audio) is caught.
Does NOT upload anything: the Hub store was full on Nov 4 (1 GB), so upload only after the owner deletes superseded assets by exact id.
"""
import argparse, glob, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def pack(folder, cap_mb, qa):
    drafts = [p for p in glob.glob(os.path.join(folder, "DRAFT*.mp4"))]
    src = sorted(drafts)[0] if drafts else os.path.join(folder, "final.mp4")
    if not os.path.exists(src):
        return f"SKIP {folder}: no DRAFT or final.mp4"
    out_dir = os.path.join(folder, "_hub"); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "s.mp4")
    crf = 28
    while True:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-c:v", "libx264", "-preset", "slow", "-crf", str(crf), "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", out], check=True)
        mb = os.path.getsize(out) / 2**20
        if mb <= cap_mb or crf >= 36:
            break
        crf += 2
    msg = f"{os.path.basename(folder)}: {os.path.basename(src)} -> _hub/s.mp4 {mb:.1f} MB (crf {crf})" + ("" if mb <= cap_mb else "  OVER CAP")
    if qa:
        r = subprocess.run([sys.executable, os.path.join(HERE, "qa_short.py"), "--folder", folder, "--video", out, "--full"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        fails = [l.strip() for l in (r.stdout + r.stderr).splitlines() if l.strip().startswith(("FAIL", "FIX"))]
        msg += "  QA " + ("PASS" if r.returncode == 0 and not fails else "FAIL: " + "; ".join(f[:100] for f in fails[:3]))
    return msg


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("folders", nargs="+")
    ap.add_argument("--skip-qa", action="store_true")
    ap.add_argument("--cap-mb", type=float, default=19.5)
    a = ap.parse_args()
    for f in a.folders:
        print(pack(f, a.cap_mb, not a.skip_qa), flush=True)
