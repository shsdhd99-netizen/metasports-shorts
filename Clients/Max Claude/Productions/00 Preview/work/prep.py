"""Rebuild every git-ignored input of the Fingerprints preview in a fresh checkout.

  python3 prep.py [--revoice]

1. input/photo.jpg + input/voice.m4a: newest submission of Netlify form "demo-request" (needs NETLIFY_AUTH_TOKEN).
2. voice.mp3 + words.json: his ElevenLabs voice clone (voice_id.txt) reading script.txt, with word timestamps
   (needs ELEVENLABS_API_KEY). Skipped if voice.mp3 exists, unless --revoice. A new take has new timing:
   words.json is rewritten and render.py's cuts follow it (they are anchored to words, not seconds).
3. open.mp3 + close.mp3: the first and last sentence, cut at render.OPEN_END / render.CLOSE_T0 (for Hedra).
4. src/mk_*.mp4: the Mixkit clips from ../sources.csv (1080p, else 720p).

His photo and voice are private (consent for this private preview only): everything written here is git-ignored.
Keys come only from the environment and are never printed.
"""
import json, os, subprocess, sys, urllib.request

W = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(W)
SITE = "795688f4-76fa-4c8f-b0fd-2a405dbb7415"


def key(name):
    v = os.environ.get(name)
    if not v:
        sys.exit(f"{name} is not set. Add it in the cloud environment settings (never paste it in chat or git).")
    return v


def get(url, headers=None, data=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def fetch_inputs():
    os.makedirs(os.path.join(ROOT, "input"), exist_ok=True)
    if all(os.path.exists(os.path.join(ROOT, "input", f)) for f in ("photo.jpg", "voice.m4a")):
        print("inputs: already there"); return
    h = {"Authorization": "Bearer " + key("NETLIFY_AUTH_TOKEN")}
    forms = json.loads(get(f"https://api.netlify.com/api/v1/sites/{SITE}/forms", h))
    fid = next(f["id"] for f in forms if f["name"] == "demo-request")
    subs = []
    for state in ("verified", "spam"):
        got = json.loads(get(f"https://api.netlify.com/api/v1/forms/{fid}/submissions?state={state}", h))
        print(f"inputs: {len(got)} {state} submission(s)")
        subs += got
    s = max(subs, key=lambda x: x["created_at"])
    print("inputs: using submission of", s["created_at"], "consent:", s["data"].get("consent"))
    for field, name in (("photo", "photo.jpg"), ("voice", "voice.m4a")):
        open(os.path.join(ROOT, "input", name), "wb").write(get(s["data"][field]["url"], h))


def revoice():
    import base64
    body = {"text": open(os.path.join(W, "script.txt")).read().strip(), "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.55, "similarity_boost": 0.8, "speed": 0.9}}
    vid = open(os.path.join(W, "voice_id.txt")).read().strip()
    d = json.loads(get(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_192",
                       {"xi-api-key": key("ELEVENLABS_API_KEY"), "Content-Type": "application/json"},
                       json.dumps(body).encode()))
    open(os.path.join(W, "voice.mp3"), "wb").write(base64.b64decode(d["audio_base64"]))
    a = d.get("normalized_alignment") or d["alignment"]
    words, cur, s, e = [], "", 0, 0
    for c, a0, a1 in zip(a["characters"], a["character_start_times_seconds"], a["character_end_times_seconds"]):
        if c.isspace():
            if cur:
                words.append({"w": cur, "s": round(s, 3), "e": round(e, 3)}); cur = ""
            continue
        if not cur:
            s = a0
        cur += c; e = a1
    if cur:
        words.append({"w": cur, "s": round(s, 3), "e": round(e, 3)})
    old = json.load(open(os.path.join(W, "words.json")))
    if [w["w"] for w in old] != [w["w"] for w in words]:
        sys.exit("words differ from words.json: render.py's word anchors would be wrong; check script.txt")
    diff = max(abs(o["s"] - n["s"]) for o, n in zip(old, words))
    print(f"voice: new take, last word ends {words[-1]['e']:.2f} s (was {old[-1]['e']:.2f}); max word shift {diff:.2f} s")
    json.dump(words, open(os.path.join(W, "words.json"), "w"), indent=0)


def cut_open_close():
    sys.path.insert(0, W)
    import render  # reads words.json, so import after revoice
    for name, args in (("open.mp3", ["-t", f"{render.OPEN_END:.3f}"]), ("close.mp3", ["-ss", f"{render.CLOSE_T0:.3f}"])):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(W, "voice.mp3"), *args,
                        "-c:a", "libmp3lame", "-b:a", "192k", os.path.join(W, name)], check=True)
    print(f"open.mp3 0-{render.OPEN_END:.2f} s, close.mp3 from {render.CLOSE_T0:.2f} s")


def mixkit():
    import csv
    os.makedirs(os.path.join(W, "src"), exist_ok=True)
    for row in csv.DictReader(open(os.path.join(ROOT, "sources.csv"))):
        f = row["file"]
        if not f.startswith("work/src/mk_"):
            continue
        out = os.path.join(ROOT, f)
        if os.path.exists(out) and os.path.getsize(out) > 100000:
            continue
        mid = f.split("mk_")[1].split(".")[0]
        for q in ("1080", "720"):
            try:
                open(out, "wb").write(get(f"https://assets.mixkit.co/videos/{mid}/{mid}-{q}.mp4"))
                print(f"mixkit {mid}: {q}p"); break
            except Exception:
                continue
        else:
            sys.exit(f"mixkit {mid}: not downloadable")


if __name__ == "__main__":
    fetch_inputs()
    if "--revoice" in sys.argv or not os.path.exists(os.path.join(W, "voice.mp3")):
        revoice()
    cut_open_close()
    mixkit()
    print("ready: next python3 hedra.py (or the manual steps in ../HEDRA.md), then bash rebuild.sh")
