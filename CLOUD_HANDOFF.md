# Cloud handoff: MetaSports Shorts (2026-10-03)

This repo is a slim, private copy of the user's PC folder `C:\Users\Admin\Documents\YouTube-Playbooks`. In this file, the repo root stands in for that path. Skill files and docs still mention Windows paths; read them relative to the repo root.

The user is non-technical. Answer in plain English and keep updates short.

## The job
1. **Redo Short #1 (LeBron's 92% pay cut), strictly by the CoachClank playbook.**
   - Read `MetaSports - Playbook.md`, `Productions/MetaSports/2026-09-28 01 Why LeBron Took a 92 Pay Cut/CLANK_STYLE_SPEC.md`, `Tools/data/title_patterns.md`, and `Research Notes/Round 3 - Deeper Findings.md`.
   - Re-script it if the playbook demands it: a scene, claim or broken-rule opener; a "You see"/"But" turn in the first third; an ending people will argue with; 22–34 s; ~250–290 wpm.
   - Then voice, B-roll, captions, sound effects and the final cut.
   - Build in `_claude_v4/`. The v3 build (`_claude_v3/`, with shots.json, clips and screenshots) and the source footage (`_broll_src/`) are in the repo.
2. **Brainstorm, create and test 3 NEW Shorts end to end**, from script to an upload-ready file.
   - New topics only. Don't duplicate Batch 2 (#1–#10, see `MetaSports - Scripts (Batch 2).md`), and never retell a story a bigger channel already posted (copy-check it).
   - Today is Oct 3, 2026 and the season tips off Oct 20. Fresh preseason, training-camp and offseason moments are the edge.
   - Use the `/nba-short`, `/voiceover`, `/assemble` and `/titles` skills in `.claude/skills/`.
3. **NEVER upload or publish anything, and never open YouTube Studio.** The user posts the files themselves, then shares the analytics so we can review what worked.

## Deliverables (per video)
- **Folder:** `Productions/MetaSports/<YYYY-MM-DD> NN <Title>/`.
- **Files in it:**
  - script.txt, notes.md
  - voice.mp3, words.json, captions.srt
  - shots.json, sfx.json, clips/
  - final.mp4, copied to `READY TO POST - <Title> (Claude cut).mp4`
  - `UPLOAD.md`: title by title_patterns.md (4–7 words, a question, one emoji optional, no hashtags), a one-line description, a pinned argument-starter comment, and a time between 6 and 11 AM ET. Use #3's `UPLOAD.md` as the template.
  - A short "what I did / why" note.
- **Getting it back:** commit and push to this branch. Finished Shorts are about 30–40 MB, under GitHub's 100 MB limit. The PC pulls them later.

## Quality bar (from the user's direct feedback)
- **Every shot matches its spoken line**, or is a real shock cut that belongs to that line.
  - Don't reuse a clip unless it still matches.
  - Check every player's identity frame by frame. A Robinson panel once showed Tree Rollins.
- **Fact lines get a Basketball-Reference or ESPN screenshot with a red box timed to the word.** Use `Tools/webshot.mjs` (`--cells`, `--mark`, `--js`) and then `Tools/broll.py page`.
  - Keep cards above the caption band: captions sit about 60% down the frame, so use `--y 0.12–0.2` for tall cards.
- **Sound effects only from `Tools/sfx`** (see `catalog.json`): 2–5 per Short, each tied to something on screen. Measure each file's onset and peak and line them up.
- **Voice QA:** run `Tools/voice_check.py` and redo a take only when it's clearly bad.
  - The checker falsely flags spoken-out numbers ("fifty-two million dollars") as stretched.
  - Use the same ElevenLabs voice as before.
- **Captions:** the user's standing preference is ALL CAPS, bold Montserrat, white with a thick black outline, and red/green keyword pops (`captions.py`, `--caption-style metasports`).
  - `CLANK_STYLE_SPEC.md` says CoachClank really uses white sentence case with a soft shadow (`--caption-style clank`).
  - The user said "strictly follow the CoachClank playbook" for the LeBron redo. So check real CoachClank frames first. If they confirm the spec, use the Clank look on LeBron, keep the ALL CAPS look on the 3 new Shorts, and write in the notes that this is an A/B test.
- **Before delivering:** check `storyboard.jpg` card by card. Loudness should be about -14 LUFS; `assemble.py` does that.

## Making the tools run on Linux (do this first; keep Windows behaviour unchanged)
The PC and the user's other agent (Grok) still use these tools.

**Setup (needs network):**
- ffmpeg with libass
- python3 with pillow and numpy
- yt-dlp
- Node 22 or newer (webshot uses the global WebSocket)
- a Chromium for webshot, e.g. `pip install playwright && playwright install --with-deps chromium`

**Code changes:**
- **`Tools/assemble.py`:** it drives the Windows-only Drift editor (`C:\Program Files\Drift\drift.exe`). Add an ffmpeg engine, used automatically when Drift is missing:
  1. Trim each shots.json entry (honouring `in`).
  2. Scale or crop to 1080x1920 at 30 fps.
  3. Concat the shots and mux in voice.mp3.
  4. Reuse `finish()` for captions, sound effects, loudness and the storyboard.
- **`Tools/webshot.mjs`:** the browser list is Windows-only. Add Linux paths and a `BROWSER_PATH` env var, and add `--no-sandbox` on Linux.
- **Fonts:** `Tools/broll.py` FONT and `Tools/thumb.py` FONT point at `C:\Windows\Fonts`. Fall back to `Tools/fonts/`.

**ElevenLabs:**
- `voiceover.py` and `voice_check.py` read `Tools/.env` or the env vars `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID`.
- The voice ID is in `Tools/.env.cloud`; copy that file to `Tools/.env`.
- The API key must come from the cloud environment's settings, and the user adds it there.
- **Never print, paste, commit or ask for the key in chat.** If it's missing, tell the user where to add it.

**Network:**
- Needs basketball-reference.com, espn.com, youtube.com/googlevideo.com and api.elevenlabs.io.
- If those are blocked, ask the user to switch the cloud environment's network access to Full.
- If YouTube blocks downloads from the cloud:
  - LeBron: use `_broll_src/` and `_claude_v3/clips/`.
  - The 3 new Shorts: finish scripts, voice, screenshots and an exact shot list (YouTube IDs plus timestamps) in the cloud, and leave cutting and rendering for the PC.

## Usage plan (the user's instruction)
- The user's weekly plan limit was at 85% on Oct 3, against a 50% ceiling they set themselves. This cloud session is meant to run on their unused cloud credits.
- **After the weekly reset (about Sun Oct 4, 9 PM ET), switch to hybrid:** cloud for research and writing, the PC for voiceover, B-roll and rendering.

## Coordination and status
- Grok edits the same production folders on the PC. Read the tail of each folder's `GROK_CLAUDE_SYNC.md`, append a dated Claude status block when you start and finish, and never overwrite Grok's `final.mp4`, `clips/` or voice files.
- **#3 Wemby:** being uploaded by the user today (its `UPLOAD.md`). Leave it alone.
- **#1 LeBron:** v3 is the current READY TO POST on the PC (16 shots, BBRef/ESPN cards). Its media isn't in the repo, except `_claude_v3`.
- **#5–#10:** scripted and scheduled. Don't touch them.
