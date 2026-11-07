"""Generate an instrumental music bed with ElevenLabs Music (POST /v1/music) and log its licence.

Why: tracks generated on our paid ElevenLabs plan are cleared for online commercial use (incl. monetized
YouTube) with no attribution on Starter and above (elevenlabs.io/music-terms, Exhibit A, checked Oct 14 2026),
and they are unique, so no third party can have registered them in Content ID.

Usage (the key must come from the environment, never from chat or git):
  . key.sh && python music_gen.py --mood stats --seconds 30 --out ../Library/Music/eleven_stats_01.mp3 --prompt "..."
Writes the mp3 plus <name>.json (prompt, model, length, date, licence) next to it and appends a row to
Library/Music/music_library.csv.
"""
import argparse, csv, datetime, json, os, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "Library", "Music", "music_library.csv")
FIELDS = ["file", "title", "mood", "source", "source_url", "licence", "licence_url", "attribution", "content_id_risk",
          "bpm", "seconds", "lufs", "added", "status", "notes"]
LICENCE = "ElevenLabs Music Terms, Starter plan: all online/offline commercial use except film, TV, radio, Studio Games; no attribution"


def add_row(row):
    os.makedirs(os.path.dirname(LIB), exist_ok=True)
    new = not os.path.exists(LIB)
    rows = [] if new else list(csv.DictReader(open(LIB, encoding="utf-8")))
    rows = [r for r in rows if r["file"] != row["file"]] + [row]
    w = csv.DictWriter(open(LIB, "w", encoding="utf-8", newline=""), fieldnames=FIELDS)
    w.writeheader()
    w.writerows({k: r.get(k, "") for k in FIELDS} for r in rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--mood", required=True, help="hype | stats | emotional | suspense")
    ap.add_argument("--seconds", type=float, default=30)
    ap.add_argument("--model", default="music_v1")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default=None)
    a = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY", "")
    if not key:
        raise SystemExit("no ElevenLabs key in the environment (run: . key.sh in the same command)")
    body = json.dumps({"prompt": a.prompt, "music_length_ms": int(a.seconds * 1000), "model_id": a.model,
                       "force_instrumental": True}).encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128", data=body,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    for wait in (15, 30, 60, None):  # 429 = busy or over the plan's 2 concurrent requests: back off and retry
        try:
            audio = urllib.request.urlopen(req, timeout=300).read()
            break
        except urllib.error.HTTPError as e:
            msg = e.read()[:400].decode(errors="replace")
            if e.code != 429 or wait is None:
                raise SystemExit(f"ElevenLabs music error {e.code}: {msg}")
            print(f"  busy (429), retrying in {wait} s")
            time.sleep(wait)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "wb").write(audio)
    meta = {"prompt": a.prompt, "model": a.model, "seconds": a.seconds, "mood": a.mood,
            "generated": datetime.date.today().isoformat(), "licence": LICENCE,
            "licence_url": "https://elevenlabs.io/music-terms"}
    json.dump(meta, open(os.path.splitext(a.out)[0] + ".json", "w"), indent=1)
    add_row({"file": os.path.relpath(os.path.abspath(a.out), os.path.dirname(LIB)).replace("\\", "/"),
             "title": a.title or os.path.basename(a.out), "mood": a.mood, "source": f"ElevenLabs Music ({a.model})",
             "source_url": "generated via API", "licence": LICENCE, "licence_url": "https://elevenlabs.io/music-terms",
             "attribution": "none required", "content_id_risk": "low (unique generated audio; do not register it in Content ID)",
             "seconds": f"{a.seconds:.0f}", "added": meta["generated"], "status": "candidate (owner has not listened)",
             "notes": a.prompt[:200]})
    print(f"saved {a.out} ({len(audio)//1024} KB)")


if __name__ == "__main__":
    sys.exit(main())
