r"""Read an Instagram reel / TikTok / YouTube Short for its real content (Nov 6, 2026; owner: "a tool to read reels: transcripts, the actual watch").

  python Tools/reel_read.py <url> [<url> ...] [--out "C:\path\to\folder"] [--ask "extra question"] [--cookies brave]
  python Tools/reel_read.py --file links.txt            # one link per line (blank lines and # comments ignored)

Ladder, cheapest first (nothing here spends vidIQ credits):
  1. the /watch plugin script (yt-dlp captions or Whisper) in transcript mode;
  2. download the video with yt-dlp (public first, then with your logged-in Brave cookies if Instagram demands a login: --cookies brave, never your password),
     then Gemini watches the file (needs GEMINI_API_KEY in Tools/.env, via yt_watch.py --ask) and answers: full transcript, on-screen text, steps/tools named,
     claims made, and what is useful for the user's goals;
  3. caption only, clearly marked as such.
Writes one markdown note per link (<out>/<id>.md): source, method used, transcript, on-screen text, the claims (marked CLAIM, unverified), takeaways, and what
could not be read. Never invents content: a gap is written as a gap. Carousels (multi-image posts) cannot be read as video: only the caption is saved.
Default out folder: Research Notes/Reel Notes. Keys are never printed.
"""
import argparse, glob, os, re, subprocess, sys, tempfile, shutil, datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WATCH = next(iter(glob.glob(os.path.expanduser(r"~/.claude/plugins/cache/*/watch/*/skills/watch/scripts/watch.py"))), None)
QUESTION = ("Watch this short video. Give: (1) a full verbatim transcript of everything spoken; (2) all on-screen text in order; (3) any tools, products, "
            "prices, numbers or step-by-step instructions shown; (4) the claims the creator makes, each marked CLAIM (do not verify them); (5) three practical "
            "takeaways for a high-school student going into business / finance / AI who also runs YouTube Shorts channels. If a part is not audible or not visible, "
            "say so instead of guessing.")


def run(cmd, timeout=600):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def vid_id(url):
    m = re.search(r"/(?:reel|reels|p|tv|shorts|video)/([A-Za-z0-9_-]+)", url) or re.search(r"[?&]v=([A-Za-z0-9_-]+)", url)
    return m.group(1) if m else re.sub(r"[^A-Za-z0-9]+", "_", url)[-20:]


def read_one(url, out, ask, cookies):
    vid = vid_id(url)
    tmp = tempfile.mkdtemp(prefix="reel_")
    method, body, gaps = "", "", []
    try:
        if WATCH:
            rc, o = run([sys.executable, WATCH, url, "--detail", "transcript"])
            if rc == 0 and len(o.strip()) > 200:
                method, body = "/watch transcript (yt-dlp captions or Whisper)", o.strip()
        if not body or "--deep" in sys.argv:
            f = None
            for extra in ([], ["--cookies-from-browser", cookies] if cookies else []):
                rc, o = run(["yt-dlp", "-q", "--no-warnings", "-f", "mp4/best", "-o", os.path.join(tmp, "v.%(ext)s"), *extra, url])
                f = next(iter(glob.glob(os.path.join(tmp, "v.*"))), None)
                if f:
                    break
                gaps.append("download failed" + (" with browser cookies" if extra else " (public)") + ": " + o.strip().splitlines()[-1][:160] if o.strip() else "download failed")
            if f:
                rc, o = run([sys.executable, os.path.join(HERE, "yt_watch.py"), f, "--ask", (ask or QUESTION), "--out-dir", tmp], timeout=900)
                txt = o.strip()
                if rc == 0 and len(txt) > 200:
                    method = (method + " + " if method else "") + "Gemini watched the downloaded video"
                    body = (body + "\n\n---\n\n" if body else "") + txt
                else:
                    gaps.append("Gemini watch failed (is GEMINI_API_KEY set in Tools/.env?): " + txt[-200:])
        if not body:
            rc, o = run(["yt-dlp", "-q", "--no-warnings", "--skip-download", "--print", "%(title)s | %(uploader)s | %(description)s", *(["--cookies-from-browser", cookies] if cookies else []), url])
            if rc == 0 and o.strip():
                method, body = "caption only (nothing else could be read)", o.strip()
            else:
                method, body = "NOT READ", "Could not read this link. It may be private, deleted, a multi-image carousel, or it needs a login (try --cookies brave while signed in)."
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, f"{vid}.md")
    open(p, "w", encoding="utf-8").write(
        f"# Reel note {vid}\n\n- Source: {url}\n- Read on: {datetime.date.today()}\n- Method: {method}\n"
        + (f"- Gaps: {'; '.join(gaps)}\n" if gaps else "") + "\nAnything marked CLAIM is the creator's claim, not verified.\n\n" + body + "\n")
    print(f"{vid}: {method} -> {p}")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--out", default=os.path.join(ROOT, "Research Notes", "Reel Notes"))
    ap.add_argument("--ask")
    ap.add_argument("--cookies", help="browser to take login cookies from, e.g. brave (Instagram often needs this)")
    ap.add_argument("--deep", action="store_true", help="also run the Gemini watch even when a transcript was found")
    a = ap.parse_args()
    urls = list(a.urls)
    if a.file:
        urls += [l.strip() for l in open(a.file, encoding="utf-8") if l.strip() and not l.startswith("#")]
    if not urls:
        sys.exit(__doc__)
    for u in urls:
        try:
            read_one(u, a.out, a.ask, a.cookies)
        except Exception as e:
            print(f"{u}: error {e}")


if __name__ == "__main__":
    main()
