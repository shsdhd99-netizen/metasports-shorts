"""Make the four talking-head clips with Hedra Character-3 through the v3 API.

  python3 hedra.py [open|close] [16x9|9x16]     (default: all four; existing clips are skipped)

Needs HEDRA_API_KEY (a v3 key) and money in the Hedra API wallet: about 6.25 cents per second at 1080p, so roughly
$1 for all four. The web-app plan credits do not count; GET /v3/balance shows the API wallet. Inputs: ../input/photo.jpg,
open.mp3, close.mp3 (make them with prep.py). Outputs: open_talk.mp4, close_talk.mp4, open_talk_9x16.mp4,
close_talk_9x16.mp4. His photo and voice go only to Hedra; the outputs are git-ignored. The key is never printed.
"""
import json, os, sys, time, urllib.request, uuid

W = os.path.dirname(os.path.abspath(__file__))
API = "https://api.hedra.com/v3"
PROMPT = ("A friendly teacher talking to camera in his classroom, natural small head movements, warm smile, "
          "steady camera.")
KEY = os.environ.get("HEDRA_API_KEY") or sys.exit("HEDRA_API_KEY is not set (add it in the environment settings)")


def call(path, body=None, method=None, headers=None):
    h = {"X-API-Key": KEY, **(headers or {})}
    data = None
    if isinstance(body, dict):
        data = json.dumps(body).encode(); h["Content-Type"] = "application/json"
    elif body is not None:
        data = body
    req = urllib.request.Request(API + path, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"{path}: HTTP {e.code} {e.read()[:800].decode(errors='replace')}")


def upload(path):
    b = "----" + uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{os.path.basename(path)}\"\r\n"
            f"Content-Type: application/octet-stream\r\n\r\n").encode() + open(path, "rb").read() + f"\r\n--{b}--\r\n".encode()
    return call("/files", body, "POST", {"Content-Type": f"multipart/form-data; boundary={b}"})["url"]


def make(kind, fmt, photo_url):
    out = os.path.join(W, f"{kind}_talk{'_9x16' if fmt == '9x16' else ''}.mp4")
    if os.path.exists(out):
        print("exists:", os.path.basename(out)); return
    job = call("/models/hedra-character-3", {"input": {
        "prompt": PROMPT, "start_image": {"source": "url", "url": photo_url},
        "audio": {"source": "url", "url": upload(os.path.join(W, f"{kind}.mp3"))},
        "aspect_ratio": "16:9" if fmt == "16x9" else "9:16", "resolution": "1080p"}}, "POST")
    jid = job["job_id"]
    print(f"{kind} {fmt}: job {jid}")
    while True:
        st = call(f"/jobs/{jid}/status")["status"]
        if st in ("COMPLETED", "FAILED"):
            break
        time.sleep(10)
    res = call(f"/jobs/{jid}")
    o = (res.get("outputs") or [{}])[0]
    if st != "COMPLETED" or not o.get("url"):
        sys.exit(f"{kind} {fmt}: {st} {json.dumps(res)[:800]}")
    urllib.request.urlretrieve(o["url"], out)
    print(f"{kind} {fmt}: saved {os.path.basename(out)} ({o.get('width')}x{o.get('height')}, {o.get('duration_ms')} ms)")


if __name__ == "__main__":
    bal = call("/balance")
    print("Hedra API wallet:", bal.get("balance"), bal.get("currency"))
    if not bal.get("balance"):
        sys.exit("The API wallet is empty: add funds on Hedra's API billing page, or use the manual steps in ../HEDRA.md")
    kinds = [a for a in sys.argv[1:] if a in ("open", "close")] or ["open", "close"]
    fmts = [a for a in sys.argv[1:] if a in ("16x9", "9x16")] or ["16x9", "9x16"]
    photo_url = upload(os.path.join(os.path.dirname(W), "input", "photo.jpg"))
    for k in kinds:
        for f in fmts:
            make(k, f, photo_url)
