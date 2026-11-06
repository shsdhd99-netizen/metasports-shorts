r"""Reel inbox processor (Nov 6, 2026): turns a queue of saved reels/TikToks/Shorts into categorised notes, only reading each link once.

  python Tools/reel_watch.py                         # process every NEW link in PrivateCollege\reel_queue.txt
  python Tools/reel_watch.py --add URL [URL ...]     # add links to the queue first
  python Tools/reel_watch.py --playlist <TikTok favorites / collection / profile / IG saved URL> [--limit 30]   # list its videos and queue them
  python Tools/reel_watch.py --index                 # rebuild PrivateCollege\Reel Notes\INDEX.md only

Flow: link -> reel_read.py (transcript, else download + Gemini watch; Instagram/TikTok use your Brave login via --cookies brave) -> categorise by what was said
(AI, COLLEGE, CONTENT, MONEY, OTHER) -> keep the note under Reel Notes\<category>\ -> INDEX.md lists every note with a one-line summary, so only the categories you
care about (default: AI, COLLEGE, CONTENT) are read first. State in PrivateCollege\reel_seen.json (a link is never read twice). Nothing is posted anywhere; the
only network calls are the video downloads and the Gemini watch. Privacy: notes live in PrivateCollege (hidden, locked, outside git).
Grabbing links out of an Instagram DM thread is done by Claude with the browser extension (see the reel-inbox skill), which appends them to the queue.
"""
import argparse, json, os, re, shutil, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
PRIV = os.path.join(os.path.expanduser("~"), "PrivateCollege")
QUEUE = os.path.join(PRIV, "reel_queue.txt")
SEEN = os.path.join(PRIV, "reel_seen.json")
NOTES = os.path.join(PRIV, "Reel Notes")
CATS = {
    "AI": r"\b(ai|a\.i\.|claude|chatgpt|gpt|openai|anthropic|gemini|llm|prompt|agent|automation|machine learning|cursor|copilot|n8n|vibe cod)",
    "COLLEGE": r"\b(college|scholarship|common app|sat\b|act\b|fafsa|admission|essay|university|financial aid|gpa|major|campus)",
    "CONTENT": r"\b(youtube|shorts|tiktok|instagram|reel|views|subscribers|retention|hook|thumbnail|algorithm|creator|content|viral|editing|capcut|monetiz)",
    "MONEY": r"\b(invest|stock|finance|business|startup|side hustle|revenue|profit|entrepreneur|resale|ecommerce|shopify|credit|budget)",
}
PRIORITY = ["COLLEGE", "AI", "CONTENT", "MONEY"]


def seen():
    return json.load(open(SEEN, encoding="utf-8")) if os.path.exists(SEEN) else {}


def key(url):
    m = re.search(r"/(?:reel|reels|p|tv|shorts|video)/([A-Za-z0-9_-]+)", url) or re.search(r"[?&]v=([A-Za-z0-9_-]+)", url)
    return m.group(1) if m else url.strip()


def queue_add(urls):
    os.makedirs(PRIV, exist_ok=True)
    have = set(open(QUEUE, encoding="utf-8").read().split()) if os.path.exists(QUEUE) else set()
    new = [u for u in urls if u not in have and key(u) not in seen()]
    with open(QUEUE, "a", encoding="utf-8") as f:
        for u in new:
            f.write(u + "\n")
    print(f"queued {len(new)} new link(s) ({len(urls) - len(new)} already known)")


def playlist(url, limit):
    r = subprocess.run(["yt-dlp", "-q", "--no-warnings", "--flat-playlist", "--playlist-end", str(limit), "--cookies-from-browser", "brave", "--print", "%(webpage_url)s", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    urls = [l.strip() for l in r.stdout.splitlines() if l.startswith("http")]
    if not urls:
        print("No videos listed:", (r.stderr or "").strip().splitlines()[-1][:200] if r.stderr else "empty")
    return urls


def categorise(text):
    low = text.lower()
    score = {c: len(re.findall(p, low)) for c, p in CATS.items()}
    best = max(score.values())
    if best < 2:
        return "OTHER", score
    top = [c for c in PRIORITY if score[c] >= max(2, best * 0.6)]
    return (top[0] if top else "OTHER"), score


def summary(text):
    t = re.sub(r"\s+", " ", re.sub(r"^#.*$|^- .*$", "", text, flags=re.M)).strip()
    m = re.search(r"Verbatim Transcript\s*(.{40,300})", t)
    return (m.group(1) if m else t[:260]).strip()


def process():
    q = [u for u in (open(QUEUE, encoding="utf-8").read().split() if os.path.exists(QUEUE) else []) if key(u) not in seen()]
    if not q:
        print("nothing new in the queue"); return
    s = seen()
    tmp = os.path.join(NOTES, "_incoming")
    for u in q:
        shutil.rmtree(tmp, ignore_errors=True)
        subprocess.run([sys.executable, os.path.join(HERE, "reel_read.py"), u, "--cookies", "brave", "--out", tmp], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1200)
        f = next((os.path.join(tmp, x) for x in os.listdir(tmp) if x.endswith(".md")), None) if os.path.isdir(tmp) else None
        if not f:
            s[key(u)] = {"url": u, "cat": "UNREAD", "sum": "could not read"}; print("UNREAD", u); continue
        text = open(f, encoding="utf-8").read()
        cat, score = ("UNREAD", {}) if "Method: NOT READ" in text else categorise(text)
        dest = os.path.join(NOTES, cat); os.makedirs(dest, exist_ok=True)
        shutil.move(f, os.path.join(dest, os.path.basename(f)))
        s[key(u)] = {"url": u, "cat": cat, "sum": summary(text)[:240], "file": os.path.join(cat, os.path.basename(f))}
        print(cat, key(u))
        json.dump(s, open(SEEN, "w", encoding="utf-8"), indent=1)
    shutil.rmtree(tmp, ignore_errors=True)
    index()


def index():
    s = seen()
    os.makedirs(NOTES, exist_ok=True)
    out = ["# Reel notes index (auto: Tools/reel_watch.py)", "", "Read order: COLLEGE, AI, CONTENT first. Open the file for the full transcript and takeaways. Claims are the creators' claims, unverified.", ""]
    for c in PRIORITY + ["OTHER", "UNREAD"]:
        rows = [(k, v) for k, v in s.items() if v.get("cat") == c]
        if rows:
            out += [f"## {c} ({len(rows)})"] + [f"- [{k}]({v.get('file', '')}) {v['url']}: {v['sum'][:200]}" for k, v in rows] + [""]
    open(os.path.join(NOTES, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out))
    print("index updated:", os.path.join(NOTES, "INDEX.md"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--add", nargs="*")
    ap.add_argument("--playlist")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--index", action="store_true")
    a = ap.parse_args()
    if a.add:
        queue_add(a.add)
    if a.playlist:
        queue_add(playlist(a.playlist, a.limit))
    if a.index:
        index(); return
    process()


if __name__ == "__main__":
    main()
