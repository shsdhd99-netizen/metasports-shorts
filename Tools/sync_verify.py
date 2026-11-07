"""Merge the cloud copy (this repo) back into the desktop project folder safely, then prove it worked.

Nothing is deleted, ever. Desktop files that differ from the cloud are kept; the cloud version is saved next to them for review
unless the desktop file is older than the day the cloud copy was made (Oct 3, 2026), i.e. it can't hold newer desktop work.

  (cloud)   python Tools/sync_verify.py make
            -> Tools/sync_manifest.csv: every file in the cloud copy with its size and SHA-256 (committed with the repo)
  (desktop) python "<cloud copy>/Tools/sync_verify.py" plan  "<cloud copy>" "C:/Users/Admin/Documents/YouTube-Playbooks"
            -> prints and writes "<desktop>/SYNC PLAN (cloud Oct 15).csv": new / same / differs (which side is newer) / desktop-only
  (desktop) python "<cloud copy>/Tools/sync_verify.py" apply "<cloud copy>" "C:/Users/Admin/Documents/YouTube-Playbooks"
            -> copies "new" files; "differs": replaces only desktop files last changed before Oct 3, 2026; every other
               differing file stays as it is and the cloud version is saved beside it as "<name> (cloud Oct 15)<ext>"
  (desktop) python "<cloud copy>/Tools/sync_verify.py" verify "<cloud copy>" "C:/Users/Admin/Documents/YouTube-Playbooks"
            -> re-hashes every manifest file on the desktop: identical / kept-desktop (with its cloud twin) / MISSING.
               Exit 0 only when nothing is missing. Only then may the cloud copy be retired (the owner decides).

Back up the desktop folder BEFORE apply (the plan step prints the command). Keys never travel: Tools/.env is not in the
manifest and is never copied.
"""
import csv, datetime, hashlib, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANIFEST = "Tools/sync_manifest.csv"
CLOUD_START = datetime.datetime(2026, 10, 3).timestamp()  # first cloud commit: Oct 3, 2026
TAG = " (cloud Oct 15)"
NEVER = {"Tools/.env", MANIFEST}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def make():
    files = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True, text=True).stdout.split("\0")
    rows = []
    for rel in sorted(f for f in files if f and f not in NEVER):
        p = os.path.join(ROOT, rel)
        if os.path.isfile(p):
            rows.append({"path": rel, "bytes": os.path.getsize(p), "sha256": sha(p)})
    with open(os.path.join(ROOT, MANIFEST), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256"]); w.writeheader(); w.writerows(rows)
    print(f"wrote {MANIFEST}: {len(rows)} files, {sum(r['bytes'] for r in rows) / 1e6:.1f} MB")


def load(cloud):
    return list(csv.DictReader(open(os.path.join(cloud, MANIFEST), encoding="utf-8")))


def plan(cloud, desk, write=True):
    rows = []
    for r in load(cloud):
        rel = r["path"]
        c, d = os.path.join(cloud, rel), os.path.join(desk, *rel.split("/"))
        if not os.path.exists(c) or sha(c) != r["sha256"]:
            rows.append({**r, "status": "CLOUD COPY CHANGED SINCE MANIFEST (re-run make)", "action": "stop"}); continue
        if not os.path.exists(d):
            rows.append({**r, "status": "new", "action": "copy"}); continue
        if sha(d) == r["sha256"]:
            rows.append({**r, "status": "same", "action": "none"}); continue
        old = os.path.getmtime(d) < CLOUD_START
        rows.append({**r, "status": "differs; desktop file " + ("older than the cloud copy" if old else "changed on the desktop since Oct 3"),
                     "action": "replace" if old else "keep desktop + save cloud twin"})
    known = {tuple(r["path"].split("/")) for r in load(cloud)}
    only = 0
    for top in sorted({r["path"].split("/")[0] for r in load(cloud)}):
        base = os.path.join(desk, top)
        if os.path.isdir(base):
            for dp, _, fs in os.walk(base):
                for f in fs:
                    rel = os.path.relpath(os.path.join(dp, f), desk).replace("\\", "/")
                    if tuple(rel.split("/")) not in known:
                        only += 1
    if write:
        out = os.path.join(desk, f"SYNC PLAN{TAG}.csv")
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256", "status", "action"]); w.writeheader(); w.writerows(rows)
    n = lambda a: sum(1 for r in rows if r["action"] == a)
    print(f"{len(rows)} cloud files: {n('copy')} new, {n('none')} identical, {n('replace')} replace (desktop file older than Oct 3), "
          f"{n('keep desktop + save cloud twin')} keep desktop + save cloud twin, {n('stop')} STOP")
    print(f"{only} desktop-only files inside the same folders (media, Grok's work, keys): never touched")
    stamp = datetime.date.today().strftime("%Y%m%d")
    print(f"BACK UP FIRST (Windows):  robocopy \"{desk}\" \"{desk}-backup-{stamp}\" /E /COPY:DAT /R:1 /W:1")
    return rows


def apply(cloud, desk):
    rows = plan(cloud, desk)
    if any(r["action"] == "stop" for r in rows):
        sys.exit("STOP: the cloud copy changed after the manifest was made. Run make on the cloud copy again.")
    done = {"copy": 0, "replace": 0, "twin": 0}
    for r in rows:
        rel = r["path"].split("/")
        c, d = os.path.join(cloud, *rel), os.path.join(desk, *rel)
        if r["action"] in ("copy", "replace"):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(c, d); done["copy" if r["action"] == "copy" else "replace"] += 1
        elif r["action"].startswith("keep"):
            stem, ext = os.path.splitext(d)
            shutil.copy2(c, stem + TAG + ext); done["twin"] += 1
    print(f"copied {done['copy']} new, replaced {done['replace']} older desktop files, saved {done['twin']} cloud twins for review")


def verify(cloud, desk):
    ok = kept = 0
    missing = []
    for r in load(cloud):
        rel = r["path"].split("/")
        d = os.path.join(desk, *rel)
        if os.path.exists(d) and sha(d) == r["sha256"]:
            ok += 1
            continue
        stem, ext = os.path.splitext(d)
        twin = stem + TAG + ext
        if os.path.exists(d) and os.path.exists(twin) and sha(twin) == r["sha256"]:
            kept += 1
            continue
        missing.append(r["path"])
    print(f"identical: {ok}; kept desktop version with cloud twin beside it: {kept}; MISSING or wrong: {len(missing)}")
    for m in missing[:30]:
        print("  MISSING", m)
    print("VERIFIED: every cloud file is on the desktop" if not missing else "NOT VERIFIED: do not retire the cloud copy")
    sys.exit(0 if not missing else 1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "make":
        make()
    elif cmd in ("plan", "apply", "verify") and len(sys.argv) == 4:
        {"plan": plan, "apply": apply, "verify": verify}[cmd](os.path.abspath(sys.argv[2]), os.path.abspath(sys.argv[3]))
    else:
        print(__doc__)
