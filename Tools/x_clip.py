"""Download the video from X (Twitter) posts. Works from the cloud, where YouTube downloads are blocked.

  python x_clip.py https://x.com/NBA/status/2104605201990877584 [more links...] --out src
  python x_clip.py --file links.txt --out src

Saves src/<tweet id>.mp4 (best quality, usually 720p) and prints length, size and the post's text.
Find posts with a web search such as:  site:x.com NBA Kawhi Leonard Raptors media day video
Official league/team accounts (NBA, Raptors, LAClippers, DetroitPistons, ESPN, ClutchPoints, House of Highlights) post the cleanest clips.
Then cut moments with:  python broll.py cut src/<id>.mp4 --at 3.2 --len 2 --x 0.5 --out clips/V01.mp4
Every download is logged in <out>/downloads.csv (account, date, post text) and every cut in the Short's sources.csv (Oct 14).
"""
import argparse, json, os, re, subprocess, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("links", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--out", default="src")
    a = ap.parse_args()
    links = list(a.links)
    if a.file:
        links += [l.strip() for l in open(a.file) if l.strip() and not l.startswith("#")]
    os.makedirs(a.out, exist_ok=True)
    for url in links:
        m = re.search(r"status/(\d+)", url)
        if not m:
            print("skip (no status id):", url)
            continue
        tid = m.group(1)
        dest = os.path.join(a.out, tid + ".mp4")
        if not os.path.exists(dest):
            r = subprocess.run(["yt-dlp", "-q", "--no-warnings", "-f", "best[ext=mp4]/best", "-o", dest, "https://x.com/i/status/" + tid],
                               capture_output=True, text=True)
            if r.returncode or not os.path.exists(dest):
                print(f"{tid}: no video ({(r.stderr or '').strip()[-90:]})")
                continue
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height", "-of", "csv=p=0", dest],
                             capture_output=True, text=True).stdout.split()
        print(f"{tid}: {dest} {' '.join(dur)} {os.path.getsize(dest) // 1024} KB")
        log_download(a.out, tid, url, dur)


def log_download(out, tid, url, dur):
    """Oct 14: keep who posted it, when and what it says (broll.py cut copies this into the Short's sources.csv)."""
    import csv, datetime
    p = os.path.join(out, "downloads.csv")
    rows = list(csv.DictReader(open(p, encoding="utf-8"))) if os.path.exists(p) else []
    if any(r["id"] == tid for r in rows):
        return
    m = subprocess.run(["yt-dlp", "-q", "--no-warnings", "--skip-download", "--print", "%(uploader_id)s\t%(upload_date)s\t%(title).300s",
                        "https://x.com/i/status/" + tid], capture_output=True, text=True).stdout.strip().split("\t")
    acct, date, text = (m + ["", "", ""])[:3]
    rows.append({"id": tid, "url": url, "account": acct, "date": date, "text": text.replace("\n", " "),
                 "duration_size": " ".join(dur), "downloaded": datetime.date.today().isoformat()})
    w = csv.DictWriter(open(p, "w", encoding="utf-8", newline=""), fieldnames=["id", "url", "account", "date", "text", "duration_size", "downloaded"])
    w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    main()
