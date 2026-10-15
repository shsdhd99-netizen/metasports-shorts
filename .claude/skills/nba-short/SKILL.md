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
   - `ROOT\Research Notes\Lessons Learned (running log).md`
   - `ROOT\Research Notes\Creation Process (Oct 10, 2026).md`
   - `ROOT\MetaSports - Playbook.md`
   - `ROOT\MetaSports - Scripts (Batch 2).md` (match this style exactly)
   - `ROOT\Tools\data\title_patterns.md`
   Lessons and the Creation Process win over the playbook where they conflict. The playbook's "post 6–7 a week" line and its "fresh search means go" line are retired.
2. **No topic given?**
   - Run `python fresh_moments.py`.
   - Run the kill test in step 4 on each candidate before offering it. Present at most two that pass, each with the second-0 clip and the last-line payoff. Reject the rest in one line each. If none pass, say so and stop.
3. **Copy-check, then doubt it.** Run `python copy_check.py "<topic in 4–6 words>"`.
   - TAKEN: say so, then offer a fresh angle or a different moment. Never retell another channel's viral story. A shared name is not the same story. Read the titles.
   - CROWDED: go only with a sharper, newer angle.
   - FRESH, including an empty result: unknown, not a yes. On Oct 10 an empty result hid a Short with 10.9 million views. Open any known giant by URL. A person reads a raw search before the script is saved.
4. **Kill test, before writing.** Name the second-0 clip. The first eight words must be paid off by the last line with a new fact. No why-title the script cannot answer. No question as the last line. No sentence that repeats, lists names, or previews an unplayed game. Not the same visible fact as a post from the last seven days. If any of those fail, reject the premise and do not write the script.
5. **Verify every fact** with a source link from a page opened that day.
   - No rumors stated as facts, no invented quotes, no fake results.
   - Add a ⚠️ note with the date to anything time-sensitive. Re-check it the morning of a voiceover.
6. **Length.** 90–110 spoken words, about 22–26 seconds. Never over 45 seconds. "But" inside the first 40% of the words. Two escalations after the turn. Every line adds one fact.
   - **Opener:** a scene or a broken rule, claim in the first eight words. Avoid "Did you know".
   - **Turn:** "But / Until / You see", then a fact, not a tease.
   - **Ending:** a consequence the opening clip still supports, because the last shot loops that clip. No "subscribe". No question ending. The posted number 6 cut ended on "six is gone," not on a question.
   - **Picture and sound, in the same notes:** shot for every sentence, jersey matches the name, music off, effects only when the frame shows the sound, none in the first second, and zero effects is allowed. Do not save the folder, and do not spend ElevenLabs, until six moving clips exist and step 4 still passes.
7. **Title.** Write 5 options using the title_patterns.md rules and mark the pick:
   - 4–7 words, no hashtags; a question is welcome only when the script answers it
   - optional 1 reaction emoji at the end
   - no "This…" opener, no ALL-CAPS words
8. **Save the package before the folder.** Write `script.txt` words and `notes.md` (titles, the shot list, the pinned comment, sources) into `Research Notes` first. Create `ROOT\Productions\MetaSports\<YYYY-MM-DD> <short title>\` only after step 4 still passes and six moving clips are named. Then:
   - `script.txt`: ONLY the words the voice says, in one paragraph.
     - Hard names as `{Giannis|YAH-nis}`. Captions show the left side; the voice says the right.
     - Numbers the voice might misread, spelled out.
   - `notes.md`:
     - the titles, with the pick marked
     - the shot list: what's on screen from second 1, one line per sentence, a new shot every 2–4 s, footage filling the 9:16 frame
     - the pinned-comment question
     - the sources and ⚠️ notes
   - Also append one line (date · title · folder) to `ROOT\MetaSports - Scripts Inbox.md` once the production folder exists.
9. **Voice.**
   - Run `python voiceover.py --script "<folder>\script.txt" --dry-run`. It shows the length and the ElevenLabs cost.
   - Ask: "Make the voiceover now? (about N ElevenLabs characters)". On yes, run it without `--dry-run`.
   - If `Tools\.env` is missing, point the user to the 2-minute setup in `ROOT\Tools Guide.md`. Never ask for the key in chat.
10. **Finish with 3 lines:** the folder, the title pick, and the next step ("drop the clips in the clips folder, then type /assemble"), plus a reminder to post between 6 and 11 AM ET.
