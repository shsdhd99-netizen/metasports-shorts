---
name: assemble
description: >
  Build a finished MetaSports Short automatically: find and cut B-roll yourself (Tools\broll.py), sync
  the cuts to the words, then edit in the free Drift editor (voice + footage + CoachClank-style captions),
  giving final.mp4 (1080x1920, ready to upload) plus an editable Drift project. Use when the user types
  /assemble, or asks to edit, find B-roll, put together or render a Short. Argument: a production folder
  or Short number (optional; defaults to the newest folder).
---

# /assemble

The user is not technical and wants you to find the B-roll yourself. Keep chat short.
ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`. Run from `ROOT\Tools` with `python` and PYTHONIOENCODING=utf-8.

0. **Coordinate first.**
   - If the folder has `GROK_CLAUDE_SYNC.md` (another agent, Grok, also works here), read its tail STATUS line.
   - Never overwrite files it's working on. Build in your own `_claude_build\` subfolder if it's active.
   - Append your status to that file when you start and when you finish.
1. **Find the folder**, in this order:
   - the folder the user named
   - a Short number: the folder in `ROOT\Productions\MetaSports` whose name has that number
   - the newest folder there
2. **Voice first.** The folder needs `voice.mp3`, `words.json` and `captions.srt`.
   - If they're missing, follow the /voiceover steps. Credits: ask unless the user already said to go.
   - Never regenerate an existing voice without a reason.
3. **B-roll: find it yourself** with `broll.py`.
   1. **Plan the shots.** Read the script, `notes.md` (shot list) and `words.json`.
      - One shot per phrase, 1–4 s each.
      - Cut exactly when a name is spoken (e.g. "Embiid", "Maxey").
      - Open on the most on-topic image, e.g. the player in his NEW team's jersey.
   2. **Search:** `python broll.py search "<query>"`. Prefer official channels (marked *), such as the NBA, team channels, ESPN and local news. Never use other creators' edited Shorts.
   3. **Look:** `python broll.py sheet <id or url> --from A --to B --every 4 --out "%TEMP%\sheet.jpg"`, then view the sheet with Read.
      - Pick moments with no burned-in captions and no big graphics.
      - Watch for score bugs.
      - Pass ids that start with "-" as full URLs.
   4. **Cut:** `python broll.py cut <id> --at <second you saw it> --len <shot length + 0.2> --x <subject position 0..1> [--zoom 1.12 --y 0.25 to crop off tickers] --snap --out "<folder>\clips\NN.mp4"`.
      - `--snap` starts the clip where that camera shot begins.
      - Run up to ~10 cuts in parallel in the background. Downloads can take minutes.
   5. **Write `<folder>\shots.json`:** `[{"clip": "01.mp4", "start": 0.0}, …]` with start times from `words.json`. `assemble.py` then cuts exactly there.
   6. **Check the clips:** extract one frame per clip into a single strip and view it. Re-cut any clip that shows the wrong moment.
4. **Build:** `python assemble.py --folder "<folder>"`.
   - Optional music: `--music "<file>"`.
   - Optional caption style: `--captions subtitle|caption|hormozi|one-word-color`. The default is the clean CoachClank look.
5. **Verify:** `python broll.py sheet "<folder>\final.mp4" --from 0 --to <length> --every 1.5 --out "%TEMP%\final.jpg"`, then view it.
   - Every shot should match its words.
   - There should be no black bars, and captions should be readable.
   - Fix and rebuild at most twice.
6. **Tell the user in 3–4 lines:**
   - `final.mp4` is ready. Post between 6 and 11 AM ET; the title and pinned comment are in `notes.md`.
   - It uses NBA and broadcast footage, so a Content ID claim is possible.
   - `edit.drift` opens in Drift for tweaks.
   - Never upload without the user's yes.
7. **Live tweaks (optional).**
   - If Drift is open with Settings → Agent access on, use the `drift-live` tools: `catalog`, then `search`, then `apply`. Check the result with `capture`.
   - Never delete or overwrite the user's clips.
