# #21 production package (v3, Oct 14, 2026: rewritten after the Oct 14 queue critic)

**Status (v3.1, Oct 14):** ready. The critic re-check of v3 (`Research Notes/Critic v2 Review (Oct 13, 2026).md`, "Re-check of #21 v3") said NEEDS REVISION, re-cut only. All four required fixes were applied and checked frame by frame at 30 fps (QA PASS, 16.8 s, same voice):

| Re-check finding | v3.1 fix | Checked |
|---|---|---|
| 4.70-5.32 s: "Twelve breaks it" on Memphis #24 | b13 ends at 4.67 s; new shot **b4c** (Jokic close-up, in 0.2) to 5.30 s | frames 4.67-5.30: Jokic |
| 2.87 s: one-frame hoop/crowd flash (a3's first frame) | a3 `in` 0.04 | frames 2.70-3.00: clean |
| 7.03 s: one-frame Westbrook-in-Rockets flash (a1's own cut at 1.70 s) | b2 starts at 7.00 s | frames 6.83-7.16: clean |
| 1.20-1.45 s: "HAS 198" on Jokic's mouth | new `cap_y` 1305 (68%) on shots 1 and 12 (`captions.py` option) | frame 1.30: below the mouth |
| optional: source-text sliver at the bottom edge | b4/b13/b5 cropped 3% (`b4c`, `b13c`, `b5c`) | |
| optional: 19 tags incl. Oscar | 12 tags, Oscar dropped | |

Not changed (needs the owner's ear): the slow line "Westbrook needed 1,301 games" (142 wpm). The v3 render is in `_v3_before_recheck/`.
**Deadline:** post **before Oct 22**. The 198 changes as soon as Denver plays a game that counts; the queue's old "before Christmas" was wrong.
**Before/after:** v2 (pre-review) is in `_v2_precritic_oct14/` (script, shots, words, voice, final, cover); v1 is in `_voice_v1/` and `script_v1.txt`. This is the Oct 14 **production-quality** before/after test. Neither version has been posted, so no audience claim is made.

## What changed (critic finding → fix)
| Critic finding (Oct 14) | v3 fix |
|---|---|
| Line 1 asked "who passed Oscar?"; the real question came at 6.9 s | Opens on the chase: "Nikola Jokic has 198 triple-doubles. Russell Westbrook retired with the record: 209." The question is clear by about 3.4 s |
| Frame 1 was an old ceremony under a cut-off "HISTORY" graphic; 209/198/34 never on screen | Frame 1 is Jokic close (scorebug cropped). The numbers show as digits in the captions (198, 209, 1,301, 810, 34, 65) |
| 21% of the runtime hopped to a box-score record (56-16-15, "first 55-15-15") | Cut. The new escalation stays on triple-doubles: "Westbrook needed 1,301 games. Jokic has played 810." |
| Two exact replays (b8, b11) and a "JOKIC 32 PTS" graphic | b8 and b11 removed; nothing replays except the closing loop to frame 1. QA now catches replays anywhere |
| Knicks-bench flash at 2.20 s; tiny schedule card | Flash gone; new readable card (`clips/c21_xmas.png`): "AT LAST SEASON'S PACE · about 23 games · GAME 27 · FRI, DEC 25 · AT GOLDEN STATE" |
| End on Jokic | The last shot is Jokic close, looping into frame 1 |

## Script (61 words; braces = shown | spoken)
Nikola {Jokic|Yoki-ch} has 198 triple-doubles. Russell Westbrook retired with the record: 209. Eleven ties it. Twelve breaks it. Westbrook needed {1,301|thirteen hundred and one} games. {Jokic|Yoki-ch} has played {810|eight hundred and ten}. Last season, he had 34 triple-doubles in just 65 games. About one every two. At that pace, twelve takes about twenty-three games. Denver's twenty-seventh game is Christmas Day, at Golden State. Four games to spare.

- Format 1 (paradox / record chase); one measure (triple-doubles).
- Length 16.8 s (v3.1; v3 was 16.9 s). Allowed by the Oct 14 Rules Audit (A8): length follows the story. The old 21 s floor would have forced padding.

## Voice
- Clone voice C, speed 1.15, one take: gate PASS. HNR 9.7, jitter 3.0, shimmer 11.28.
- voice_check **PASS**: every word heard, "1,301" and "810" included.
- An earlier take used "810" as digits and was heard as "8-10" (as in "eight-ten"). The spoken form is now forced: {810|eight hundred and ten}, {1,301|thirteen hundred and one}.
- `voice_check.py` was also fixed today: ordinals ("27th" vs "twenty-seventh") no longer raise false REDOs.

## EDL
| # | t (s) | clip (kind) | words | why |
|---|---|---|---|---|
| 1 | 0.00-1.99 | b1c.mp4 (action) | Nikola Jokic has 198 triple-doubles. | Frame 1 = Jokic himself, close, as '198' appears in the captions (scorebug cropped off; critic Oct 14 edit 1); captions lowered to 68% so 'HAS 198' clears his mouth (critic re-check Oct 14) |
| 2 | 1.99-2.87 | a2.mp4 (face) | Russell Westbrook retired | Westbrook, close, on his own name (a5 panned to an empty court after 0.5 s) |
| 3 | 2.87-4.02 | a3.mp4 (action) | with the record: 209. | Westbrook in action on 'the record: 209'; in 0.04 skips a one-frame hoop/crowd flash (re-check) |
| 4 | 4.02-4.70 | b13c.mp4 (action) | Eleven ties it. | Jokic passing on 'Eleven ties it' (ends at 4.70 s: after that a Memphis player fills the frame; bottom 3% cropped to drop a source-text sliver) |
| 5 | 4.70-5.32 | b4c.mp4 (face) | Twelve breaks it. | Jokic close-up on 'Twelve breaks it' (critic re-check Oct 14; bottom 3% cropped) |
| 6 | 5.32-7.00 | a1.mp4 (action) | Westbrook needed 1,301 games. | Westbrook (OKC tribute, then Wizards): a long career; ends at 7.00 s, before the clip's own cut to a Rockets frame at 1.70 s |
| 7 | 7.00-8.51 | b2.mp4 (action) | Jokic has played 810. | Jokic in a game, on '810'; starts at 7.00 s (re-check: avoids a1's Rockets frame) |
| 8 | 8.51-10.00 | b7.mp4 (action) | Last season, he had 34 triple-doubles | Jokic last season |
| 9 | 10.00-11.70 | b5c.mp4 (action) | in just 65 games. About one every two. | Jokic in action: the rate (in 0.25 skips a non-Jokic first frame); bottom 3% cropped (source-text sliver) |
| 10 | 11.70-13.48 | b12.mp4 (face) | At that pace, twelve takes about twenty-three games. | Jokic (media day) on the projection |
| 11 | 13.48-15.52 | c21_xmas.png (card) | Denver's twenty-seventh game is Christmas Day, at Golden State. | Readable proof: pace = about 23 games; game 27 = Fri Dec 25 at Golden State (B-Ref schedule; critic Oct 14 edit 4) |
| 12 | 15.52-16.80 | b1c.mp4 (action) | Four games to spare. | End on Jokic (critic edit 4) and loop into frame 1 |

## QA (Oct 14)
- `qa_short.py` (new rules): **PASS**. No dead air, no frozen or black frames, no footage shown twice, -14 LUFS.
- Warnings:
  - Pace 224 wpm. Digits count as one word, so this under-reads.
  - Tail 0.61 s.
  - Slowed clips: all at most 1.2x.
- Frames checked (`_audit/watch/sheet.jpg`):
  - Westbrook is on screen for his name (a2).
  - Jokic is on screen for "810", "34" and "65 games".
  - The card is readable; the ending is Jokic.
- **Not verified:** naturalness by ear (owner).


## Music and sound (Oct 14, 2026; `Library/Music Guide.md`)
- **Track:** `Library/Music/eleven_hype_01.mp3` (Trap pulse).
  - **Source and licence:** ElevenLabs Music, generated Oct 14 on our Starter plan. All online commercial use, no attribution (elevenlabs.io/music-terms). Logged in `Library/Music/music_library.csv`.
  - **Status:** candidate until the owner approves it by ear.
- **Mood and plan:** Record-chase countdown = the 'hype' bed (trap, 144 BPM, 2% speech-band energy). The track's own break (27.0-27.4 s) falls under the Christmas card and its re-entry hit lands on 'Four games to spare.'
- **Placement** (from the render log): track from 11.98 s, video 0.0-16.927347 s, bed -21.0 LU under the voice (gain -22.8 dB), lift in no-speech gaps 3.0 dB [[16.32, 16.93]], drops [].
- **Sound effects:** unchanged from `sfx.json`. Their licence is unknown (the "Downloads/music" origin is flagged in the Rules Audit).
- **Checks:** QA PASS. Speech band clear of the music before ducking (1-4 kHz margin in the QA output). Every drop, hit and stop was confirmed by isolating the music (music render minus dry render).
