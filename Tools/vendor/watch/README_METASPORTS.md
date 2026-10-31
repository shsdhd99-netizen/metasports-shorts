# watch (vendored from github.com/bradautomates/claude-video, MIT licence; supplied by the owner Oct 15, 2026)

**What we use it for:** previewing a long source before cutting b-roll.
- It prints **scene-change frames with exact timestamps** (where the source cuts, and where each moment starts), with near-identical frames removed.
- That finds the right seconds fast, and shows a source's own internal cuts before they end up inside one of our shots (`footage_qc.py` flags those after the fact).

**Commands** (from the repo root; local engine, no keys):
```
python Tools/vendor/watch/scripts/watch.py "<file or URL>" --engine local --max-frames 40 --out-dir <scratch folder>
python Tools/vendor/watch/scripts/watch.py "<file or URL>" --engine local --start 0:30 --end 1:10   # one stretch only
```
Then open the listed frames and pick `--at` times for `broll.py cut`.

**Rules for us:**
- **Never pass `--cookies` or `--cookies-from-browser` in the cloud**, and never to get around a platform block.
- YouTube refuses the cloud server ("confirm you're not a bot"). Run YouTube URLs **on the PC**, where they work normally. X posts work from the cloud; `x_clip.py` downloads them too.
- **Don't use the Gemini engine without the owner's OK.** It uploads the video to Google and needs a key. Keys go only in `~/.config/watch/.env` on the machine, never in this repo.
- Transcripts: the local engine needs captions or a speech backend. In the cloud we transcribe with faster-whisper (already installed, free) via `export_check.py` / `voice_check.py`.

**Tested Oct 15 (cloud):** a local 33 s Mavs post gave 12 scene-change frames with timestamps. The transcript step needs an API key, so it was skipped.
