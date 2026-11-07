"""Free disk from finished Shorts (Nov 3, 2026; owner: "clear out useless files for me and old builds").

  python Tools/cleanup_builds.py            -> dry run: lists what would go and the total
  python Tools/cleanup_builds.py --go       -> deletes it

A folder qualifies when its date prefix is before today (its slot has passed: posted, or dead news) or it is listed in EXTRA.
Folders with a future date are never touched. Inside a qualifying folder only working files go: src/, clips/, _rawclips/,
_voice*/, take*_*/, _sheets/, *.mp4 inside _check/, voice_raw.mp3, *.url, and final.mp4 / final_nocap.mp4 when a DRAFT*.mp4 exists.
Always kept: every DRAFT*.mp4 (the posted version, for a copyright re-cut), and every file git tracks (script, notes, UPLOAD.md, json).
"""
import datetime, glob, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASES = [os.path.join(ROOT, "Productions", "MetaSports"), os.path.join(ROOT, "Soccer Channel", "Productions")]
EXTRA = {"2026-11-03 93 Pacers Had Six Players And Almost Won"}  # bumped Nov 3 (stale news)
DIRS = re.compile(r"^(src|clips|_rawclips|_voice.*|take\d+_.*|_sheets)$")


def tracked():
    out = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True).stdout.decode("utf-8", "replace")
    return {os.path.normcase(os.path.join(ROOT, p)) for p in out.split("\0") if p}


def size(p):
    if os.path.isfile(p):
        return os.path.getsize(p)
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(p) for f in fs)


def main():
    go = "--go" in sys.argv
    today = datetime.date.today().isoformat()
    keep = tracked()
    total, items = 0, []
    for base in BASES:
        for d in sorted(glob.glob(os.path.join(base, "*"))):
            name = os.path.basename(d)
            m = re.search(r"(\d{4}-\d{2}-\d{2})", name)
            if not os.path.isdir(d) or "DEMO" in name or not m:
                continue
            if not (m.group(1) < today or name in EXTRA):
                continue
            has_draft = bool(glob.glob(os.path.join(d, "DRAFT*.mp4")))
            for e in os.listdir(d):
                p = os.path.join(d, e)
                if os.path.isdir(p) and DIRS.match(e):
                    if any(os.path.normcase(os.path.join(r, f)) in keep for r, _, fs in os.walk(p) for f in fs):
                        continue  # never delete a folder holding tracked files
                    items.append(p)
                elif os.path.isdir(p) and e == "_check":
                    items += [x for x in glob.glob(os.path.join(p, "**", "*.mp4"), recursive=True) if os.path.normcase(x) not in keep]
                elif os.path.isfile(p) and os.path.normcase(p) not in keep and (
                        e == "voice_raw.mp3" or e.endswith(".url") or (has_draft and e in ("final.mp4", "final_nocap.mp4"))):
                    items.append(p)
    for p in items:
        s = size(p); total += s
        print(f"{s / 1e6:9.1f} MB  {os.path.relpath(p, ROOT)}")
        if go:
            shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else os.remove(p)
    print(f"{'DELETED' if go else 'would free'} {total / 1e9:.2f} GB in {len(items)} items")


if __name__ == "__main__":
    main()
