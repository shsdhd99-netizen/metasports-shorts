---
name: nba-short
description: >
  Write a ready-to-voice MetaSports (MetaSportsClips) AI NBA story Short in the CoachClank-proven
  style (22–40s stories or 15–25s moments, fast AI voice, scene/rule/opinion opener, turn, an ending on the payoff; the debate question goes in the pinned comment). It finds
  fresh moments, copy-checks the topic, verifies facts, writes a short title, saves an
  ElevenLabs-ready script and offers to make the voiceover. Use when the user types /nba-short or
  asks for a MetaSports / NBA Short script. Argument: the moment or topic (optional).
---

# /nba-short

The user is not technical. Keep chat short, run the tools yourself and put the work in files.
ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`. Run the tools from `ROOT\Tools` with `python`, and set PYTHONIOENCODING=utf-8.

1. **Read first.** THE RULES at the top of `ROOT\MetaSports - Playbook.md` (Oct 26 overnight review) win over everything else, this file included. Then:
   - `ROOT\Research Notes\Rule Changes Applied (Oct 26, 2026).md` (what changed and why)
   - `ROOT\Research Notes\Lessons Learned (running log).md`
   - `ROOT\Research Notes\Creation Process (Oct 10, 2026).md`
   In the cloud, `/cloud-short` is the full pipeline; this skill writes the script. `MetaSports - Scripts (Batch 2).md` and `Tools\data\title_patterns.md` are superseded (Oct 26 overnight review). The playbook's "fresh search means go" line is retired.
2. **No topic given?** Pick by lane (Oct 26 overnight review; Playbook THE RULES §1): about half of NBA Shorts are moments you can watch (game, bench, warm-up, fan, kid, mascot, broadcast desk), narrated who, what, and the reaction. The rest rotate: the star paradox (THE #42 FORMAT), same-day news, a weekly countdown ("3 times [star] did X"). A moment needs one fact the clip can't show.
   - Run `python fresh_moments.py`.
   - Research tools: `python yt_watch.py <link>` (Gemini watches a Short; needs a free `GEMINI_API_KEY` in the environment, never in chat) and `ROOT\Research Notes\Competitor Watchlist.csv` (the channels we watch).
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
   - **Opener:** a scene or a broken rule; line 1 is 11 words or fewer (Oct 26 overnight review; [V] `Research Notes/Retention and Editing Upgrade (Oct 26, 2026).md` §1b). Avoid "Did you know".
   - **Turn:** "But / Until / You see", then a fact, not a tease.
   - **Ending:** the payoff, then stop. No forced loop: loop to the opening clip only when it is the payoff image (Oct 26 overnight review). No "subscribe". No question ending. The posted number 6 cut ended on "six is gone," not on a question.
   - **Picture and sound, in the same notes:** frame 1 shows what line 1 is about, happening; a proof shot for every beat; the key second replayed once before the payoff; jersey matches the name, music off, effects only when the frame shows the sound, none in the first second, and zero effects is allowed. **Footage first (Oct 26 overnight review):** do not save the folder, and do not spend ElevenLabs, until frame 1 and a proof clip for each beat exist (any number of sources) and step 4 still passes. Never add filler to reach a clip count.
7. **Title (Oct 26 overnight review).** Write 3 options and mark the pick:
   - a short statement pointing at the moment or the claim ("He Pretended To Be Klay Thompson"), true to the video
   - no hashtag or one (#nba); no ALL-CAPS words
   - title wording is a small factor ([V] `Research Notes/Similar Channels (Oct 26, 2026).md` §1): don't score titles
   - also write 3-8 optional tags (about 100-150 characters: names, team, event, misspellings), no description
8. **Save the package before the folder.** Write `script.txt` words and `notes.md` (titles, the shot list, the pinned comment, sources) into `Research Notes` first. Create `ROOT\Productions\MetaSports\<YYYY-MM-DD> <short title>\` only after step 4 still passes and frame 1 plus a proof clip per beat are named. Then:
   - `script.txt`: ONLY the words the voice says, in one paragraph.
     - Hard names as `{Giannis|YAH-nis}`. Captions show the left side; the voice says the right.
     - Numbers the voice might misread, spelled out.
   - `notes.md`:
     - the titles, with the pick marked
     - the shot list: what's on screen from second 1 (shot 1 at least 2 s; at most 2 shots in the first 3 s and 3 in the first 5 s), about one shot every 2 s, the replay of the key second, wide plays cropped to about 3:4 so they fill the frame (Oct 26 overnight review)
     - the pinned-comment question
     - the sources and ⚠️ notes
   - Also append one line (date · title · folder) to `ROOT\MetaSports - Scripts Inbox.md` once the production folder exists.
9. **Voice.**
   - Run `python voiceover.py --script "<folder>\script.txt" --dry-run`. It shows the length and the ElevenLabs cost.
   - Ask: "Make the voiceover now? (about N ElevenLabs characters)". On yes, run it without `--dry-run`.
   - If `Tools\.env` is missing, point the user to the 2-minute setup in `ROOT\Tools Guide.md`. Never ask for the key in chat.
10. **Finish with 3 lines:** the folder, the title pick, and the next step ("drop the clips in the clips folder, then type /assemble"), plus the slot from `UPLOAD SCHEDULE.md` (NBA 11 AM ET; news the morning after the game). Never post it yourself.
