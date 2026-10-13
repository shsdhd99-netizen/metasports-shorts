---
name: voiceover
description: >
  Turn a MetaSports script into an ElevenLabs voiceover plus word-timed captions (voice.mp3,
  captions.srt, words.json) with the user's local Tools\voiceover.py. Use when the user types
  /voiceover or asks for a voiceover or captions. Argument: a production folder, a script, or a
  Batch 2 script number (optional; defaults to the newest production folder).
---

# /voiceover

ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`. Run from `ROOT\Tools` with `python` and PYTHONIOENCODING=utf-8.

1. **Find the script.** In order:
   - the folder or file the user named
   - a Batch 2 script number: create `ROOT\Productions\MetaSports\<date> <title>\script.txt` from it, spoken words only
   - the newest folder in `ROOT\Productions\MetaSports`
2. **Hard names?** Make sure they are written `{Display|say-it-like-this}`.
3. **Dry run:** `python voiceover.py --script "<script.txt>" --dry-run`. Show the seconds and characters, then ask to go.
4. **On yes:** `python voiceover.py --script "<script.txt>"`. It makes voice.mp3 (native speed, no time-stretch beyond x1.08 since Oct 5; the permanent voice is the owner's pick from `Research Notes/Voice Lineup (Oct 13, 2026)/`), captions.srt and words.json in the same folder.
5. **Errors:**
   - A missing key means pointing the user to "ElevenLabs (2 minutes)" in `ROOT\Tools Guide.md`. Never ask for the key in chat.
   - A 401 error means the key is wrong.
   - A voice error means running `python voiceover.py --list-voices` and having the user pick one.
6. **Finish:** the folder, plus "Next: drop the clips in the clips folder, then type /assemble."
