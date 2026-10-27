"""Watch a YouTube Short (or one of our own drafts) with Google's Gemini and get a scene-by-scene report.

Why (Oct 26 2026): vidIQ's watcher is out of credits until Nov 5 and Everygen's needs a paid plan. Gemini takes a
YouTube link directly (public videos only) and has a free tier, so it is the cheapest "eyes and ears" we can use
from the cloud. It also watches a local mp4, so it can review our own DRAFTs before the owner posts them.

Setup (once, by the owner, never in chat): make a free key at https://aistudio.google.com/apikey and add it to the
cloud environment's settings as GEMINI_API_KEY (or put GEMINI_API_KEY=... in Tools/.env on the PC; that file is
git-ignored). This script never prints the key.

Usage:
  python Tools/yt_watch.py https://youtube.com/shorts/ID [more links or ids...]
  python Tools/yt_watch.py "Productions/.../DRAFT - ....mp4"            # one of our own files
  python Tools/yt_watch.py ID --ask "Is there a music bed? How loud vs the voice?"
  python Tools/yt_watch.py --channel @swishyhoopz --top 5               # watch a channel's 5 most-viewed Shorts
  python Tools/yt_watch.py "<DRAFT>.mp4" --precheck --out-dir "Research Notes/Watch Reports/drafts"   # check before posting
  Top-vs-bottom studies of whole channels: Tools/watch_study.py. What else the key is good for:
  'Research Notes/Gemini Uses (Oct 27, 2026).md'.
Options: --fps 4 (frames per second the model looks at; default 4 so it can count cuts), --model NAME,
         --out-dir DIR (default 'Research Notes/Watch Reports').
Models (Oct 27 2026): tries the newest flash, then gemini-flash-latest, then the newest flash-lite, moving on when one
answers 503 "high demand" or 429. On the first day only flash-lite answered free-tier calls.
Accuracy check (Oct 27, flash-lite, #48 and #64): the narration transcript and the shot timing matched our files, but it
said "music: present" on both and both were posted without music (it likely hears crowd noise or sound effects as music).
Don't trust its music field without a second check.
Output: one JSON report per video plus a line in <out-dir>/index.csv. Tier every number in it as [S] (model-observed);
it is a model's watch, not a measurement, so spot-check anything surprising against the frames (Tools/yt_sheet.py).
"""
import argparse, csv, datetime, json, os, re, subprocess, sys, time, urllib.error, urllib.request

API = "https://generativelanguage.googleapis.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROMPT = """You are a short-form video editor studying a YouTube Short. Watch and listen to the whole video.
Report ONLY what you can see and hear; write "unknown" when you can't tell. Return JSON with these keys:
- length_s: total length in seconds
- topic: one sentence, what the Short is about
- lane: one of "moment" (something that happens on camera), "explainer" (why/how/history/stat), "list", "other"
- hook: {first_words: exact words spoken in the first 3 s, first_frame: what frame 1 shows, on_screen_text_0_3s: text on screen in the first 3 s or "none", shots_in_first_3s: number}
- shots: list of {start_s, end_s, shows, kind} for EVERY shot (a new camera angle, clip or still = a new shot; kind is one of face, action, replay, still, text_card, screenshot, stock, other)
- shot_count, average_shot_s, longest_shot_s
- voice: {type: "AI" | "human" | "none" | "unknown", gender, words_per_minute_estimate, tone, original_audio_under_voice: true/false}
- music: {present: true/false/"unknown", style, level_vs_voice: "quiet" | "equal" | "loud" | "none", starts_at_s}
- sound_effects: list of {at_s, sound}
- captions: {present, words_per_line, case: "ALL CAPS" | "sentence" | "mixed", position: "top" | "middle" | "lower-middle" | "bottom", colours, highlight_style}
- text_overlays: list of {at_s, text} other than captions
- cards_or_graphics: number of full-screen cards, stat graphics or screenshots
- framing: how 16:9 footage is fitted to 9:16 (crop, zoom, blurred background, letterbox)
- ending: {last_words, last_frame, loops_to_start: true/false, call_to_action: text or "none"}
- script: the full narration, word for word
- retention_tricks: list of concrete techniques you see (open loops, reveals, pattern interrupts, zooms, replays)
- subject_visible_0_1s: true/false, is the main person or moment of the story already on screen in the first second
- devices: {countdown_or_ranking: true/false (a visible #3/#2/#1, 1/10 or similar), replay_of_key_moment: true/false
  (the same moment shown again, slowed or from another angle), promise_in_first_line: true/false (the first sentence
  promises something still to come, e.g. "wait for the last one"), ends_on_payoff: true/false (the last line answers
  or tops the first), reaction_shot: true/false (a close-up of someone reacting)}
- what_makes_it_work: 3 short bullets, from the video only
"""

PRECHECK = """You are checking this YouTube Short before it is posted. Watch and listen to all of it. Report only problems you
actually see or hear, with timestamps. 1) Voice: any word mispronounced, slurred, cut off or repeated; any glitch or robotic
artifact. 2) Captions: any caption that does not match the words spoken, or is misspelled. 3) Sound: music or sound effects too
loud over the voice; any jump in loudness. 4) Picture: any frozen, flashing or black frame; any 2+ seconds where nothing new
happens. 5) Mismatch: anything on screen that contradicts what the voice says (wrong player, team or number). 6) Is it clear
within the first second what the Short is about? Write 'none' for a category with no problems. End with one line:
VERDICT: READY or VERDICT: FIX (what)."""

HOOK_PROMPT = """This is the first 6 seconds of a YouTube Short, sampled at a high frame rate. List the time in seconds
(0.1 precision) of EVERY hard cut: the picture changes to a different clip, camera angle, image or card. Do not count
zooms, pans or text appearing over the same shot. Return JSON: {"cuts": [times], "first_shot_shows": "...",
"first_words": "exact words spoken in the first 3 s", "text_on_screen_0_3s": "text or none",
"music_or_beat_audible": true/false/"unknown"}"""


def hook_cuts(target, models, end_s=6, fps=10):
    """Second, sharper look at the opening only (shot counts in the full report can be off by 1-3).
    Returns (report, model)."""
    yt = yt_url(target)
    uri, mime = (yt[0], None) if yt else (upload(target), "video/mp4")
    part = {"file_data": {"file_uri": uri, **({"mime_type": mime} if mime else {})},
            "video_metadata": {"start_offset": "0s", "end_offset": f"{end_s}s", "fps": fps}}
    body = {"contents": [{"parts": [part, {"text": HOOK_PROMPT}]}],
            "generationConfig": {"temperature": 0.1, "responseMimeType": "application/json"}}
    r, model = generate(models, body)
    text = "".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"])
    rep = parse_json(text)
    cuts = []
    for c in sorted(c for c in rep.get("cuts", []) if isinstance(c, (int, float)) and 0.15 < c < end_s):
        if not cuts or c - cuts[-1] >= 0.35:  # Oct 27 calibration: it sometimes reports one cut twice (2.3, 2.4)
            cuts.append(c)
    rep["cuts_merged"] = cuts
    rep["shots_in_first_3s"] = 1 + sum(c < 3 for c in cuts)
    rep["shots_in_first_5s"] = 1 + sum(c < 5 for c in cuts)
    return rep, model


def key():
    k = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not k:
        env = os.path.join(ROOT, "Tools", ".env")
        if os.path.exists(env):
            for line in open(env, encoding="utf-8"):
                m = re.match(r"\s*(GEMINI_API_KEY|GOOGLE_API_KEY)\s*=\s*(\S+)", line)
                if m:
                    k = m.group(2).strip("'\"")
    if not k:
        sys.exit("GEMINI_API_KEY is not set. Owner: make a free key at https://aistudio.google.com/apikey and add it to "
                 "the cloud environment settings as GEMINI_API_KEY (never paste it in chat).")
    return k


def call(path, body=None, method=None, headers=None, raw=None):
    h = {"x-goog-api-key": key(), **(headers or {})}
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    if body is not None:
        h.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(path if path.startswith("http") else API + path, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")[:600]
        raise SystemExit(f"Gemini API error {e.code}: {msg}")


def versions(names, suffix):
    """Stable gemini-N-<suffix> models (no preview/tts/image variants), newest first."""
    def score(n):
        v = re.match(rf"gemini-(\d+(?:\.\d+)?)-{suffix}$", n)
        return float(v.group(1)) if v else -1
    return sorted((n for n in names if score(n) > 0), key=score, reverse=True)


def pick_models(want):
    """The models to try, in order; watch() moves to the next one when a model is overloaded (503) or
    rate-limited (429). Oct 27 2026 on a free key: 3.8 and 3.7 flash answered 503 "high demand", 3.6 and 3.5 flash
    worked, pro models answered 429 (not on the free tier) and gemini-2.5-* is closed to new keys (404)."""
    if want:
        return [want]
    if os.environ.get("GEMINI_MODEL"):
        return [os.environ["GEMINI_MODEL"]]
    try:
        out, _ = call("/v1beta/models?pageSize=200")
        names = [m["name"].split("/")[-1] for m in json.loads(out).get("models", [])
                 if "generateContent" in m.get("supportedGenerationMethods", [])]
    except SystemExit:
        names = []
    order = versions(names, "flash")[:4] + versions(names, "flash-lite")[:1]
    return order or ["gemini-flash-latest"]


BUSY = {}  # model -> time it last answered 503/429; skipped for 10 minutes within one run


def generate(models, body):
    """POST generateContent to the first model that answers. Returns (response dict, model)."""
    live = [m for m in models if time.time() - BUSY.get(m, 0) > 600] or models
    for i, model in enumerate(live):
        try:
            out, _ = call(f"/v1beta/models/{model}:generateContent", body, method="POST")
            return json.loads(out), model
        except SystemExit as e:
            if i == len(live) - 1 or not re.search(r"error (503|429)", str(e)):
                raise
            BUSY[model] = time.time()
            print(f"{model} is busy ({str(e)[17:20]}); trying {live[i + 1]}", file=sys.stderr)
            time.sleep(2)


def upload(path):
    """Gemini File API (resumable upload), then wait until the file is ACTIVE."""
    size = os.path.getsize(path)
    _, hdr = call("/upload/v1beta/files", {"file": {"display_name": os.path.basename(path)[:120]}}, method="POST",
                  headers={"X-Goog-Upload-Protocol": "resumable", "X-Goog-Upload-Command": "start",
                           "X-Goog-Upload-Header-Content-Length": str(size),
                           "X-Goog-Upload-Header-Content-Type": "video/mp4"})
    url = {k.lower(): v for k, v in hdr.items()}["x-goog-upload-url"]
    out, _ = call(url, raw=open(path, "rb").read(), method="POST",
                  headers={"X-Goog-Upload-Offset": "0", "X-Goog-Upload-Command": "upload, finalize"})
    f = json.loads(out)["file"]
    for _ in range(90):
        if f.get("state") == "ACTIVE":
            return f["uri"]
        if f.get("state") == "FAILED":
            raise SystemExit(f"upload failed: {f}")
        time.sleep(2)
        out, _ = call("/v1beta/" + f["name"])
        f = json.loads(out)
    raise SystemExit("upload did not become ACTIVE in 3 minutes")


def yt_url(s):
    if os.path.exists(s):
        return None
    m = re.search(r"(?:shorts/|v=|youtu\.be/)([\w-]{11})", s)
    vid = m.group(1) if m else (s if re.fullmatch(r"[\w-]{11}", s) else None)
    if not vid:
        raise SystemExit(f"not a YouTube link, video id or local file: {s}")
    return f"https://www.youtube.com/watch?v={vid}", vid


def parse_json(text):
    """The model's JSON answer as a dict (some models wrap it in a one-item list)."""
    try:
        v = json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text}
    if isinstance(v, list) and v and isinstance(v[0], dict):
        v = v[0]
    return v if isinstance(v, dict) else {"raw": text}


def watch(target, models, fps, ask):
    """Returns (video id, report, the model that answered). Moves to the next model on 503/429."""
    yt = yt_url(target)
    if yt:
        uri, vid, mime = yt[0], yt[1], None
    else:
        uri, vid, mime = upload(target), re.sub(r"[^\w-]+", "_", os.path.splitext(os.path.basename(target))[0])[:60], "video/mp4"
    part = {"file_data": {"file_uri": uri, **({"mime_type": mime} if mime else {})}, "video_metadata": {"fps": fps}}
    body = {"contents": [{"parts": [part, {"text": ask or PROMPT}]}],
            "generationConfig": {"temperature": 0.2, **({} if ask else {"responseMimeType": "application/json"})}}
    r, model = generate(models, body)
    try:
        text = "".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"])
    except (KeyError, IndexError):
        raise SystemExit(f"no answer: {json.dumps(r)[:600]}")
    if ask:
        return vid, {"question": ask, "answer": text}, model
    return vid, parse_json(text), model


def channel_top(handle, n):
    url = f"https://www.youtube.com/{handle.lstrip('/')}/shorts"
    r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", url], capture_output=True, text=True, timeout=300)
    ents = (json.loads(r.stdout) if r.stdout.strip() else {}).get("entries") or []
    ents = sorted(ents, key=lambda e: e.get("view_count") or 0, reverse=True)
    return [e["id"] for e in ents[:n]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", help="YouTube links / ids / local mp4 files")
    ap.add_argument("--channel", help="@handle: watch its most-viewed Shorts")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--ask", help="ask one free-form question instead of the full report")
    ap.add_argument("--precheck", action="store_true", help="pre-post check of one of our DRAFTs (voice, captions, sound, picture)")
    ap.add_argument("--fps", type=float, default=4.0)
    ap.add_argument("--model")
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "Research Notes", "Watch Reports"))
    a = ap.parse_args()
    a.ask = PRECHECK if a.precheck else a.ask
    targets = list(a.targets) + (channel_top(a.channel, a.top) if a.channel else [])
    if not targets:
        ap.error("give at least one link, id, file or --channel")
    models = pick_models(a.model)
    os.makedirs(a.out_dir, exist_ok=True)
    idx = os.path.join(a.out_dir, "index.csv")
    new = not os.path.exists(idx)
    with open(idx, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["date", "video", "model", "length_s", "lane", "shot_count", "average_shot_s", "shots_in_first_3s",
                        "voice", "music", "cards", "report"])
        for t in targets:
            vid, rep, model = watch(t, models, a.fps, a.ask)
            rep["_meta"] = {"source": t, "model": model, "fps": a.fps, "watched": datetime.date.today().isoformat(),
                            "tier": "[S] model-observed, not measured"}
            path = os.path.join(a.out_dir, f"{vid}{'_ask' if a.ask else ''}.json")
            json.dump(rep, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            h, v, m = rep.get("hook", {}) or {}, rep.get("voice", {}) or {}, rep.get("music", {}) or {}
            w.writerow([rep["_meta"]["watched"], t, model, rep.get("length_s"), rep.get("lane"), rep.get("shot_count"),
                        rep.get("average_shot_s"), h.get("shots_in_first_3s"), v.get("type"), m.get("present"),
                        rep.get("cards_or_graphics"), os.path.relpath(path, ROOT)])
            print(f"{t}: {os.path.relpath(path, ROOT)}" + (f"\n{rep['answer']}" if a.ask else
                  f"  ({rep.get('length_s')} s, {rep.get('shot_count')} shots, voice {v.get('type')}, music {m.get('present')})"))


if __name__ == "__main__":
    main()
