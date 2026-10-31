# UPLOAD: #62 Why LeBron Isn't A Knick (opening night, news + paradox)

**DRAFT, awaiting your approval. Not posted, not scheduled.**
**File:** `DRAFT - awaiting approval - 62 MSG chant at LeBron, Knicks title (no music).mp4` (same as `final.mp4`, 31.7 s, 1080x1920). Video files are not in git; rebuild with `python Tools/assemble.py --folder "<this folder>" --no-music` after re-cutting from `src/` (every in-point and crop is in `sources.csv`; voice pieces `_n1`-`_n3` + `plan.json` for `splice_voice.py`).
**Timing:** tonight. The chant clips are hours old and the game ended at 02:00 UTC Oct 21; the earlier it goes up, the better.

**Title (exactly as written):** Why LeBron Isn't A Knick 😳
**Other titles:** MSG Told LeBron "We Don't Want You" 💀 / The Knicks' Title Cost Them LeBron 😳
**Hashtags (up to 3):** #nba #lebron #knicks
**Tags:** lebron james, lebron sixers, lebron knicks, we dont want you chant, knicks fans chant lebron, msg chant, knicks ring night, knicks banner, knicks championship, sixers vs knicks, 76ers knicks, lebron sixers debut, rich paul, rich paul whiteboard, lebron free agency, knicks 2026 champions, jalen brunson, madison square garden, nba opening night, nba 2026-27, lebron 76ers, sixers win, nba shorts, basketball shorts
**Pinned comment:** Rich Paul says LeBron would be a Knick right now if New York had lost the Finals. Worth the trade?

**Music:** none. **Voice:** Alex, plus two real-audio bursts (the MSG crowd, Rich Paul).

## What's on screen (all clips checked frame by frame; `sources.csv`)
| Time | Line | Footage |
|---|---|---|
| 0.0 | "LeBron James dreamed of finishing" | LeBron in a suit walking the MSG tunnel tonight |
| 1.3 | "his career in Madison Square Garden." | The MSG scoreboard ring and the new banner |
| 2.9 | "Tonight, the Garden chanted this:" | Knicks fans filming the ceremony |
| 4.8 | **Crowd: "We don't want you!"** (real audio) | Fan video: LeBron at the free-throw line |
| 7.6 | "And the craziest part?" | LeBron in the tunnel, side view |
| 8.7 | "The only reason he's not a Knick" | Knicks team photo under the banner |
| 9.9 | "is that the Knicks won." | The 2025-26 banner |
| 11.0 | "In June, they beat the Spurs" | Brunson driving on the Spurs, Finals |
| 12.3 | "for their first title in 53 years," | The trophy, then the Knicks walking out; **FIRST TITLE / IN 53 YEARS** |
| 14.2 | "and LeBron said, 'Hey, I can't.'" | LeBron at Sixers media day; **"HEY, I CAN'T."** |
| 16.0 | "His agent said if they hadn't won:" | Rich Paul's whiteboard; **RICH PAUL, LEBRON'S AGENT** |
| 17.9 | **Rich Paul: "There would be no board. He'd be going to the Knicks."** (real audio) | Rich Paul pointing at the board |
| 19.7 | "So he signed with Philly." | LeBron close-up in a PHILA jersey tonight |
| 20.9 | "And his debut was tonight, in the Garden, on ring night." | Brown to LeBron at the rim; Knicks players holding up their rings |
| 23.8 | "LeBron had 14, 9 and 7," | LeBron at the rim; **14 · 9 · 7** |
| 26.0 | "and the Sixers won, 106 to 100." | Sixers possession at MSG; **FINAL SIXERS 106 / KNICKS 100** |
| 28.7 | "The Garden didn't want him, so he spoiled their ring night." | Back to the tunnel shot (loop) |

**Effects (3):** ding on 53 YEARS, camera on the media-day cut, boom on the final score.

## QA (`qa_short.py --full`, Oct 21): PASS
- **Listen to the chant (4.8-7.5 s):** speech-to-text couldn't make out the crowd ("we know about you"); the caption uses the words Barstool, the fan poster and CBS reported.
- Several sources are small (the Finals clip 640x640 at 3.0x, the fan video and the podcast at about 2.7x), so those shots are softer than broadcast.
- Talking-head share 47% (guideline 45%); the last word ends 0.64 s before the end (loop tail wants 0.4).

**Facts:** ESPN (LeBron's Garden quote), Field Level Media (Rich Paul), NBA and USA Today (Finals), ESPN box score (final); exact quotes in `notes.md`.
**Rights:** NBA/NBC broadcast footage via official posts, a fan video via Barstool, a podcast clip via Heat Central; a Content ID claim is possible.
