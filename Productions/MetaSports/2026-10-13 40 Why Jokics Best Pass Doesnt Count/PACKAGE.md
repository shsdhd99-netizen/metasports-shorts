# #40 production package (v2, Oct 13, 2026 late: re-cut after Critic v2)

**Status: ready** once the owner has listened once on a phone speaker. Automated QA PASS (plain and pointer). All the Critic v2 required edits are applied (list below); a second, independent critic re-checked v2: **PASS** (`Research Notes/Critic v2 Review (Oct 13, 2026).md`, "Re-check of v2"). It logs the pointer twin as "ring, no pill".
**Premise:** Jokic said this pass was probably the best of his NBA career, but it came in a preseason game, so it isn't one of his 6,080 official assists.
**Viewer question in second 1:** "Why doesn't this pass count?"
**v1 (pre-critic) files:** `_v1_precritic/` (script, shots, sfx, final, pointer twin, docs).

## What changed from v1 (Critic v2, Oct 13)
| Critic finding | Fix in v2 |
|---|---|
| The hook voiced "best pass ever" as fact (Jokic said "probably", "in my NBA career") | New hook: "This pass doesn't even count. A week later, Jokic said it was probably the best pass of his NBA career." The paradox is still the first sentence, over the pass |
| "No look. Behind the back." played over Cam Johnson's catch; the make shown from 3 angles | Shot 1 runs through the release until the ball is gone; "No look. Behind the back." sits on a slowed replay of the release; one angle of the make |
| Caption chunk "EVER DOESN'T" | Gone: the cards now read "THIS PASS" / "DOESN'T EVEN COUNT." |
| "College gym" over a frame with no college marking | M_pass, with the BUFFALOES lettering readable, under the whole line |
| Quote card + StatMuse card back to back (3.5 s of reading) | Quote card removed (the attribution is now spoken over his face); one card for the 6,080 proof |
| The last line restated the hook | It now ends on the answer as one number: "So his total still reads six thousand and eighty. Not eighty-one." over the opening image (loop) |
| Pointer ring on his torso, gone before the release | Ring on the hands and ball, 0-1.5 s |

## 1. Script (86 words)
This pass doesn't even count. A week later, Jokic said it was probably the best pass of his NBA career. No look. Behind the back. Corner to corner. Cam Johnson buries the three. Jokic has six thousand and eighty assists in the record book. So this should be number six thousand and eighty-one. It isn't. It happened in a preseason game, in a college gym in Boulder. And preseason assists never go in the book. So his total still reads six thousand and eighty. Not eighty-one.

## 2. Voice
- Provisional clone voice C, one take (`voice_take.json`): gate PASS, HNR 9.2, jitter 2.77, shimmer 10.71; 250 wpm (house range 247-289).
- Speed: speed 1.06 via a light time-stretch (auto speed made it 19.5 s, under the 21 s QA floor). Plus 0.3 s of silence at the end for the loop tail.
- voice_check (whisper): all 86 words heard, including "6,080, not 81" and "6,081". Notes only: "Yokic" (the respelling) and "pre-season".
- **Owner listen points:**
  - 12.3 s and 19.5-20.6 s: the watch tool's small recogniser heard "6,0801"; the larger one heard it right.
  - The name "Jokic".

## 3. EDL (every beat → the picture that proves it)
| # | t (s) | clip (kind) | in | words over it | why |
|---|---|---|---|---|---|
| 1 | 0.00-1.93 | R_close.mp4 (action) | 0.0 | This pass doesn't even count. A week later, | Frame 1 = the object: Jokic with the ball on the baseline. Runs through the behind-the-back release (clip ~1.8 s) until the ball is gone (critic v2 edit 2) |
| 2 | 1.93-2.71 | M_close.mp4 (face) | 0.0 | Jokic said it was | The person whose ranking it is, on 'Jokic said it was probably the best pass of his NBA career' (attributed, critic v2 edit 1) |
| 3 | 2.71-4.71 | K_wide.mp4 (action) | 0.4 | probably the best pass of his NBA career. | The broadcast wide angle of the same pass under 'probably the best pass of his NBA career' (third cut inside 3 s) |
| 4 | 4.71-5.96 | R_close.mp4 (action) | 0.95 | No look. Behind the back. | Slowed replay of the release itself, so 'No look. Behind the back.' sits on the pass, not the catch (critic v2 edit 2) |
| 5 | 5.96-6.83 | R_wide.mp4 (action) | 0.1 | Corner to corner. | High angle: the ball crosses the whole baseline to the corner |
| 6 | 6.83-8.23 | R_shot.mp4 (action) | 0.0 | Cam Johnson buries the three. | The one angle of the make (critic v2: keep one angle) |
| 7 | 8.23-10.78 | c_assists.png (card) | - | Jokic has six thousand and eighty assists in the record book. | Proof of 6,080 (StatMuse, checked Oct 13) |
| 8 | 10.78-13.36 | M_gym.mp4 (action) | 0.0 | So this should be number six thousand and eighty-one. It isn't. | The same pass from the broadcast camera: this is the would-be 6,081st |
| 9 | 13.36-15.91 | M_pass.mp4 (action) | 0.0 | It happened in a preseason game, in a college gym in Boulder. | BUFFALOES lettering readable under the whole line 'It happened in a preseason game, in a college gym in Boulder' (CU Events Center; critic v2 recommended edit) |
| 10 | 15.91-17.71 | M_close.mp4 (face) | 1.9 | And preseason assists never go in the book. | Jokic again on the rule that erases his assist |
| 11 | 17.71-19.80 | c_6080.mp4 (card) | - | So his total still reads six thousand and eighty. | The answer as one number: still 6,080 |
| 12 | 19.80-21.27 | R_close.mp4 (action) | 0.0 | Not eighty-one. | Back to the opening image so the Short loops into 'This pass doesn't even count.' |

- **Cards:** 22% of runtime, none before 8.2 s.
- **Fits** (`_render.json`): 3 clips are slowed 1.06-1.25x; nothing loops or holds.
- **Sources:** as in v1 (NBA and Kevin O'Connor posts on X; every cut 2.4 s or less, cropped, under commentary).

## 4. Captions
House metasports captions from `words.json`. Checked on `_audit/watch/sheet.jpg`: clear of the cards, no split hook phrase.

## 5. Sound
| t | effect | gain | why |
|---|---|---|---|
| 8.13 | swish | -10 dB | the corner three goes in on screen (R_shot +1.30 s) |
| 12.86 | boom_cinematic | -12 dB | "It isn't." |

## 6. Variants and covers
- **A (plain):** `final.mp4` = `READY TO POST - ...mp4`.
- **B (pointer):** `final_pointer.mp4`, a red ring at (460, 790), r 190, 0-1.5 s, around his hands and the ball.
- **Covers:** `cover_A.png` (frame 1) and `cover_B_pointer.png` (0.4 s, ball inside the ring).

## 7. QA (Oct 13 late)
- `qa_short.py`: **PASS** for both versions (`_audit/qa.txt`, `_audit/qa_pointer.txt`). Values: 21.3 s, 3 cuts in the first 3 s, -14.7 LUFS, no frozen footage, no black frames, no holds.
- Warnings, all known:
  - The word list doesn't count "doesn't count" as a conflict word.
  - The turn "It isn't." falls at 60%.
  - The loop tail is 0.63 s.
  - The title starts with a name.
- `voice_check.py`: CHECK, with notes only.
- `voice_quality.py`: PASS.
- `watch_short.py`: report and sheet are in `_audit/watch/`.
- **Not verified:** naturalness by ear (owner).


## Music and sound (Oct 14, 2026; `Library/Music Guide.md`)
- **Track:** `Library/Music/eleven_stats_01.mp3` (Clever pulse).
  - **Source and licence:** ElevenLabs Music, generated Oct 14 on our Starter plan. All online commercial use, no attribution (elevenlabs.io/music-terms). Logged in `Library/Music/music_library.csv`.
  - **Status:** candidate until the owner approves it by ear.
- **Mood and plan:** Paradox/record story = the 'stats' bed (clever pulse, 92 BPM, 4% speech-band energy). One beat of silence before the turn 'It isn't.'; the music decays before the punchline 'Not eighty-one.' so it lands dry (the old 'Why does no one like Bronny' hit did this on its last word).
- **Placement** (from the render log): track from 0.0 s, video 0.0-19.8 s, bed -20.0 LU under the voice (gain -15.1 dB), lift in no-speech gaps 4.0 dB [], drops [[12.6, 12.9]].
- **Sound effects:** unchanged from `sfx.json`. Their licence is unknown (the "Downloads/music" origin is flagged in the Rules Audit).
- **Checks:** QA PASS. Speech band clear of the music before ducking (1-4 kHz margin in the QA output). Every drop, hit and stop was confirmed by isolating the music (music render minus dry render).
