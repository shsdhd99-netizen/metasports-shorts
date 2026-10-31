"""Free stock video for abstract lines ("the phone rang", "a children's charity"): Mixkit (Mixkit Free License:
commercial use incl. monetized YouTube, no attribution; not for broadcast/CD/games; mixkit.co/license).
The story format (Research Notes/Story Format Study - Ahmed) shows a literal picture for every phrase; real
footage of the named person comes first, stock only for lines with no person or event in them.

  python Tools/stock.py search fireworks --sheet out.jpg        # ids + one contact sheet of first frames
  python Tools/stock.py get 12724 --out src/stock_12724.mp4      # 1080p (falls back to 720p/360p), logs to src/downloads.csv
"""
import argparse, csv, os, re, subprocess, sys, tempfile

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def fetch(url, out=None):
    cmd = ["curl", "-sL", "-A", UA, url] + (["-o", out] if out else [])
    r = subprocess.run(cmd, capture_output=True)
    return r.stdout.decode("utf-8", "replace") if not out else (r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > (2000 if out.endswith(".jpg") else 20000))


def search(term, n=12):
    slug = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
    html = fetch(f"https://mixkit.co/free-stock-video/{slug}/")
    ids = []
    for m in re.finditer(r"assets\.mixkit\.co/videos/(\d+)/\1-(?:360\.mp4|thumb-360-0\.jpg)", html):
        if m.group(1) not in ids:
            ids.append(m.group(1))
    return ids[:n]


def cmd_search(a):
    ids = search(a.term, a.n)
    if not ids:
        print("no results (try a simpler word: 'money', 'fireworks', 'newspaper', 'hotel-room')")
        return
    print(" ".join(ids))
    if a.sheet:
        tmp = tempfile.mkdtemp()
        tiles = []
        for i in ids:
            p = os.path.join(tmp, f"{i}_t.jpg")  # the page's own thumbnail: no video download needed
            if fetch(f"https://assets.mixkit.co/videos/{i}/{i}-thumb-360-0.jpg", p) or fetch(f"https://assets.mixkit.co/videos/{i}/{i}-360.mp4", p.replace("_t.jpg", ".mp4")):
                p = p if os.path.exists(p) and os.path.getsize(p) > 2000 else p.replace("_t.jpg", ".mp4")
                jpg = os.path.join(tmp, f"{i}.jpg")
                subprocess.run(["ffmpeg", "-v", "error", "-y", *(["-ss", "1"] if p.endswith(".mp4") else []), "-i", p, "-frames:v", "1", "-vf",
                                f"scale=320:180:force_original_aspect_ratio=decrease,pad=320:180:(ow-iw)/2:(oh-ih)/2,"
                                f"drawtext=text='{i}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black", jpg])
                if os.path.exists(jpg):
                    tiles.append(jpg)
        if tiles:
            cols = min(4, len(tiles))
            rows = (len(tiles) + cols - 1) // cols
            ins = sum((["-i", t] for t in tiles), [])
            lay = "|".join(f"{(k % cols) * 320}_{(k // cols) * 180}" for k in range(len(tiles)))
            subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex",
                            "".join(f"[{k}]" for k in range(len(tiles))) + f"xstack=inputs={len(tiles)}:layout={lay}:fill=black",
                            a.sheet] if len(tiles) > 1 else ["cp", tiles[0], a.sheet])
            print(a.sheet)


def cmd_get(a):
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    for q in ("1080", "720", "360"):
        if fetch(f"https://assets.mixkit.co/videos/{a.id}/{a.id}-{q}.mp4", a.out):
            break
    else:
        raise SystemExit(f"could not download Mixkit video {a.id}")
    log = os.path.join(os.path.dirname(os.path.abspath(a.out)), "downloads.csv")
    rows = list(csv.DictReader(open(log, encoding="utf-8"))) if os.path.exists(log) else []
    cols = ["id", "url", "account", "date", "text", "duration_size", "downloaded"]
    sid = os.path.splitext(os.path.basename(a.out))[0]
    rows = [r for r in rows if r.get("id") != sid]
    rows.append({"id": sid, "url": f"https://mixkit.co/free-stock-video/ (id {a.id})", "account": "Mixkit (stock)",
                 "text": f"Mixkit Free License; {a.note}".strip("; "), "duration_size": q + "p"})
    w = csv.DictWriter(open(log, "w", encoding="utf-8", newline=""), fieldnames=cols)
    w.writeheader()
    w.writerows({k: r.get(k, "") for k in cols} for r in rows)
    print(f"{a.out}  (Mixkit {a.id}, {q}p)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("term"); p.add_argument("--n", type=int, default=12); p.add_argument("--sheet")
    p = sub.add_parser("get"); p.add_argument("id"); p.add_argument("--out", required=True); p.add_argument("--note", default="")
    a = ap.parse_args()
    {"search": cmd_search, "get": cmd_get}[a.cmd](a)


if __name__ == "__main__":
    main()
