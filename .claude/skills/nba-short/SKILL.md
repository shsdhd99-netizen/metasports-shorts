---
name: nba-short
description: >
  Write a ready-to-voice MetaSports (MetaSportsClips) AI NBA story Short in the CoachClank-proven
  style (22–40s stories or 15–25s moments, fast AI voice, scene/rule/opinion opener, turn, argument-starting ending). It finds
  fresh moments, copy-checks the topic, verifies facts, picks a data-backed title, saves an
  ElevenLabs-ready script and offers to make the voiceover. Use when the user types /nba-short or
  asks for a MetaSports / NBA Short script. Argument: the moment or topic (optional).
---

# /nba-short

The user is not technical. Keep chat short, run the tools yourself and put the work in files.
ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`. Run the tools from `ROOT\Tools` with `python`, and set PYTHONIOENCODING=utf-8.

1. **Read first.** These files are the source of truth and win if anything here differs:
   - `ROOT\MetaSports - Playbook.md`
   - `ROOT\MetaSports - Scripts (Batch 2).md` (match this style exactly)
   - `ROOT\Tools\data\title_patterns.md`
2. **No topic given?**
   - Run `python fresh_moments.py`.
   - From the results, pick the 5 most story-worthy NBA moments: funny, petty, rule-weird, wholesome, size mismatch, a streak or a first.
   - One line each, plus why it would work. Ask which one. Stop there.
3. **Copy-check.** Run `python copy_check.py "<topic in 4–6 words>"`.
   - TAKEN: say so, then offer a fresh angle or a different moment. Never retell another channel's viral story.
   - CROWDED: go only with a sharper, newer angle.
   - FRESH: go.
4. **Verify every fact** with a source link from a web search.
   - No rumors stated as facts, no invented quotes, no fake results.
   - Add a ⚠️ note with the date to anything time-sensitive.
5. **Length by type.** Stories: 90–170 words (22–40s at ~250 wpm). CoachClank's 8 biggest 2026 Shorts ran 22–34s with 89–136 words (Research Notes/Round 3 - Deeper Findings.md, section 8). Quick moments: 60–100 words (15–25s). Never over 55s. Get to the turn within the first third.
   - **Opener:** the first 6 words carry the scene, rule, opinion or stakes. A mystery question ("Why did he…?") works too. Avoid trivia-quiz openers like "Did you know" unless the fact is jaw-dropping.
   - **Turn:** "But / However / You see".
   - **Ending:** a punchline, consequence or quote that starts an argument. No "subscribe", no "follow for more".
6. **Title.** Write 5 options using the title_patterns.md rules and mark the pick:
   - 4–7 words, no hashtags; question titles welcome
   - optional 1 reaction emoji at the end
   - no "This…" opener, no ALL-CAPS words
7. **Save** to `ROOT\Productions\MetaSports\<YYYY-MM-DD> <short title>\`:
   - `script.txt`: ONLY the words the voice says, in one paragraph.
     - Hard names as `{Giannis|YAH-nis}`. Captions show the left side; the voice says the right.
     - Numbers the voice might misread, spelled out.
   - `notes.md`:
     - the titles, with the pick marked
     - the shot list: what's on screen from second 1, one line per sentence, a new shot every 2–4 s, footage filling the 9:16 frame
     - the pinned-comment question
     - the sources and ⚠️ notes
   - Also append one line (date · title · folder) to `ROOT\MetaSports - Scripts Inbox.md`.
8. **Voice.**
   - Run `python voiceover.py --script "<folder>\script.txt" --dry-run`. It shows the length and the ElevenLabs cost.
   - Ask: "Make the voiceover now? (about N ElevenLabs characters)". On yes, run it without `--dry-run`.
   - If `Tools\.env` is missing, point the user to the 2-minute setup in `ROOT\Tools Guide.md`. Never ask for the key in chat.
9. **Finish with 3 lines:** the folder, the title pick, and the next step ("drop the clips in the clips folder, then type /assemble"), plus a reminder to post between 6 and 11 AM ET.
