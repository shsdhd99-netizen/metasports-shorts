# Held Shorts Fix Report (Nov 6, 2026)

Paperwork-only pass. No video, voice, captions or script changed; nothing posted, voiced, rendered or downloaded. `qa_final.py` re-run after the fixes.

Common to all five: `src/` is not in this clone (git-ignored), so the FOOTAGE warns ("could not be probed") are expected here and were not touched. No source URLs were re-downloaded. `cover.jpg` was made with `Tools/thumb.py --shape short` from a frame of the draft MP4, but `*.jpg` is git-ignored, so the covers exist only on this machine and are not in the commit. All original slots had already passed by Nov 6; each card now says so.

| Short | Before | After | Fixed | Still needs a human or rebuild |
|---|---|---|---|---|
| #77 Bronny (Oct 29) | HOLD, 3 fail | HOLD, 1 fail | Title ("Bronny Is Shooting 100% This Season", card's own pick 2), 28 tags (451 chars), Slot line (marked passed), cover.jpg, description line, 2 real links added to notes.md (NBA.com/AP and The Athletic on the Knecht waive) | "QA PASS line" left missing on purpose (verdict is HOLD, not SHIP). Last line "He just hasn't played since" is probably stale (written Oct 28/29); re-check his games since before any post. Stat lines still only cite Basketball-Reference with no verified URL. |
| #80 Warriors/Lakers (Oct 31) | HOLD, 2 fail | FIX, 0 fail | Title ("The Lakers Led By 23 And Lost By 17" = the spoken line 1, folder name is the old idea), 26 tags (489 chars), cover.jpg. Slot and pinned comment were already there. | Warns only: H04 bug clipped, 'still' claim word with 2 sources, missing src. News piece from Oct 30 game, now stale. The card's own "QA PASS (full)" line is older than this qa_final run; qa_final says FIX, not SHIP. |
| #78 Rodman (Oct 29) | HOLD, 3 fail | HOLD, 1 fail | Title (line 1 of the Short), 30 tags (458 chars), Slot line, cover.jpg, 3 real links in notes.md (SI 2020, ESPN/Raimondi 2026, ESPN WWE HOF 2026) | "QA PASS line" left missing (HOLD). Script is 204 words, 55 s file (under the 59.5 s cap, but the story profile flags it as long). Needs a human decision on length and the Content ID risk noted in notes.md. |
| S16 Fabregas/Como (Oct 29) | HOLD, 1 fail | FIX, 0 fail | 29 tags (485 chars), Slot line, cover.jpg, explicit `**Title:**` = the full spoken line plus "Against Manchester United" per the Oct 29 review. Notes already had 6 links. | Warns: line 1 has 12 words, 61.9 s lint (file 57.3 s), F11 bug clipped. Fine to leave or re-cut. |
| S18 Mourinho (Oct 31) | HOLD, 3 fail | FIX, 0 fail | Title (card pick 1), 29 tags (482 chars), Slot line, 5 real links added to notes.md (BBC, Independent, Marca, Inter.it, beIN), cover.jpg | notes.md says voice.mp3/words.json/captions are the PRE-fix versions (54.3 s vs the 51.9 s file): run `word_edit.py` on the two spans before any re-render. Clip reuse warn (M01 shown 2-3 times). |

Cover texts: BRONNY 100%, 38-15 FLIPPED, RODMAN SKIPPED FINALS, STOP RUNNING, SPRINKLER REVENGE.

Nothing here is a QA SHIP. Only #77 and #78 still FAIL, and only on the missing "QA PASS" line, which is correct while the verdict is not SHIP.
