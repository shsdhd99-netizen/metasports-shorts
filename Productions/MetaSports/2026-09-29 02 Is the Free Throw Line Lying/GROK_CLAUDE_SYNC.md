# GROK_CLAUDE_SYNC — #2 Is the Free Throw Line Lying? (v2)
Updated: Sun Sep 27 2026 ~2:45 PM ET

## Status
READY FOR VAUGHN REVIEW — do NOT upload.
Monday Sep 28 replacement for killed LeBron #1.
**v2 rebuild** after Vaughn: "still shit. broll is trash, and captions."

## Deliverables
- final.mp4: 26.6s, 1080x1920, h264 (~19 MB)
- Path: `C:\Users\Admin\Documents\YouTube-Playbooks\Productions\MetaSports\2026-09-29 02 Is the Free Throw Line Lying\final.mp4`
- voice.mp3 + captions.srt (rebuilt from words.json, no ElevenLabs re-spend) + words.json
- edit.drift + preview_1-3.jpg
- shots.json updated for v2 clip map
- Captions: assemble `--captions subtitle` only (white sentence-case soft shadow mid-frame) — NOT Hormozi

## Caption fix (v1 → v2)
`Tools\voiceover.py` `to_srt` rewritten for natural 2–4 word phrases; max_chars ~28; never end on dangling the/a/from/of/to/and when avoidable; sentence breaks kept.
SRT regenerated from existing `words.json` (no ElevenLabs credits). Drift mash fix: SRT joins words with NBSP (U+00A0).

### Before → after samples
| v1 (broken) | v2 (Clank phrases) |
|---|---|
| throw is shot | Every NBA free throw / is shot from 15 feet… |
| hoop is 15 | of the hoop / is 15 inches |
| feet 9. | from 13 feet 9. |
| But here's the | But here's the weird part. |
| basketballare (mashed) | lines in basketball (spaced) |
| line from the | from the backboard, / not from the rim. |

Verified on rendered frames: "Every NBA free throw", "from the backboard,", "The rim sits 6 inches", "Which means every free throw", "The three-point line", "lines in basketball" — readable, spaced, natural.

## Clip map v2 (shots.json → VO)
| # | VO start | Beat | Source |
|---|----------|------|--------|
| 01 | 0.00 | Every NBA free throw… | Sikana FT tutorial (iW2VFzBiaQo) tight shoes ON line @37.5 — 1080p |
| 02 | 3.49 | from the backboard | Sikana hoop board+rim @110.5 — no burned title |
| 03 | 6.84 | rim sits 6 inches | Sikana SIDE rim-to-glass gap @111 |
| 04 | 10.08 | middle / 13'9 geometry | Onuaku NBA overhead FT (6SOzkaxPRgQ local) |
| 05 | 15.89 | 3PT measured from middle | Curry GW deep-3 beyond arc (uC0VY3EeBnA local) |
| 06 | 19.73 | two different places | Onuaku overhead FT line + key/arc |
| 07 | 23.30 | biggest guys can't make 13'9 | Shaq #34 at FT — shaq_brick.mp4 1280x720 (replaced 320x240 airball) |

## Style compliance
- White subtitle preset only; soft shadow; mid-frame; 2–4 word natural phrases
- No title cards, no THE REAL STORY, no neon ALL CAPS / Hormozi
- 9:16 fill on all clips
- No YouTube upload

## Remaining gaps
1. **Clip 07** — Shaq is recognizable at the line in 720p, but the clear *ball miss/brick* moment is still soft; true HD Dwight/Drummond brick not locked. Better than v1 320x240.
2. **Clip 05** — Curry deep-3 proves "beyond the arc / 3PT world" but feet ON the painted 3PT line are not a tight shoe-on-arc crop (wide broadcast crop).
3. **Clip 06** — FT line + top-of-key clearly; full 3PT arc is only partially in frame (not a perfect A/B of both measurement origins).
4. **Clip 02/03** — gym/portable hoop (Sikana) not NBA arena glass; didactic gap is clear but not broadcast NBA.
5. **18" rim width** — spoken in VO during clip 03 window; no dedicated top-down rim-diameter hero (level-on-rim cut exists as `clips\_rim18c.mp4` if Vaughn wants a swap).
6. Folder name kept `2026-09-29 02…` even though post day is Mon Sep 28.

## Not done / do not
- No YouTube upload
- Did not rebuild killed LeBron #1
- API keys never logged
- Did not switch to Hormozi caption preset
---
## Claude — 2026-09-30 ~7:25 PM ET
- The #2 Claude cut is DONE: `READY TO POST - Is the Free Throw Line Lying (Claude cut).mp4` (a copy of `_claude_build\final.mp4`). It is 26.6 s with 15 word-synced shots, all NBA footage, and your v2 captions:
  - It opens on the overhead free-throw camera, then punches in on the line for "except it isn't".
  - A rim cam covers the backboard lines, and young Shaq shatters a backboard on "backboard".
  - Shaq wears the rim on "18 inches wide".
  - The Rockets bench reacts on "weird part", Curry plus a rim-cam swish cover the three-point line, and the wide lane shot covers "two different places".
  - It ends on Giannis's 2021 Finals free-throw airball: the crowd counting, then his grimace on "13 feet 9".
  - Score bugs and logos are cropped out and every frame was checked. Your `final.mp4` is untouched.
- Vaughn has #1 marked KILLED, so #2 is now first: Thu Oct 1, 6–11 AM ET. I updated `schedule.json` (#3 Fri Oct 2 … #9 Thu Oct 8, #10 Oct 18).
STATUS: DONE (Claude) — #2. Building #3 Wemby next (voice already made, 23.8 s).

---
## Claude — 2026-10-01 ~8:00 PM ET (v3, after Vaughn's feedback)
Vaughn: captions should look like his old Shorts / Clank; every shot must match the words (or be a wow moment); no lazy reuse; screenshots OK; natural SFX.
- New build in `_claude_v3\` (shots.json + sfx.json + clips). `READY TO POST - ... (Claude cut).mp4` replaced; old one moved to `_claude_build\old_cut_v2.mp4`.
- Captions: new `Tools\captions.py` (ALL CAPS Montserrat Black, thick black outline, 1-3 words, red shock / green numbers), burned by assemble.py (new default `--captions burn`).
- Shots: NBA rulebook screenshots (`Tools\webshot.mjs` + `broll.py page`) with red boxes on "15' from the plane of the face of the backboard" and "23'9" from the middle of the basket"; red circles on the rim (`broll.py circle`); official NBA court diagram for "two different places"; ending = Gobert airball + Clippers bench laughing (replaces the gym/Shaq promo clips).
- Audio: loudness now lifted to -14 LUFS in the final pass (old cuts were -23 LUFS = played quiet). 5 SFX from Vaughn's library (Tools\sfx\): boom on "except it isn't", clicks on screenshots, rim on the dunk, whoosh into the diagram.
- New checkers: `Tools\voice_check.py` (ElevenLabs speech-to-text vs script) and `Tools\storyboard.py` (frame per caption card).
STATUS: DONE (Claude) — #2 v3. Next: #3, #4 re-cuts, then #1 rebuild.
