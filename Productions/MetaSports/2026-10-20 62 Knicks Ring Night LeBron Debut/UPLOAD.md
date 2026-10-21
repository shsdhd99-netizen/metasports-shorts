# UPLOAD: #62 Why LeBron Isn't A Knick (opening night, news + paradox)

**DRAFT, awaiting your approval. Not posted, not scheduled.**
**File:** `DRAFT - awaiting approval - 62 MSG chant at LeBron, Knicks title v2 (no music).mp4` (same as `final.mp4`, 31.4 s, 1080x1920). v2 (Oct 21, second QA): "Tonight" became "On opening night" and "his debut was tonight" became "his Sixers debut was", so it reads right on any day. v1 is in `_v1/`. Video files are not in git; rebuild with `python Tools/assemble.py --folder "<this folder>" --no-music` after re-cutting from `src/` (every in-point and crop is in `sources.csv`; voice pieces `_n1`-`_n3` + `plan.json` for `splice_voice.py`).
**Timing:** Oct 21, the 5-7 PM ET slot (best 6 PM). It is the LeBron Short of the night. #65 (LeBron vs the Knicks fan) is held: Chaz NBA already has 546K views on that clip.

**Title (exactly as written):** Why LeBron Isn't A Knick 😳
**Other titles:** MSG Told LeBron "We Don't Want You" 💀 / The Knicks' Title Cost Them LeBron 😳
**Hashtags (up to 3):** #nba #lebron #knicks
**Tags:** lebron james, lebron sixers, lebron knicks, we dont want you chant, knicks fans chant lebron, msg chant, knicks ring night, knicks banner, knicks championship, sixers vs knicks, 76ers knicks, lebron sixers debut, rich paul, rich paul whiteboard, lebron free agency, knicks 2026 champions, jalen brunson, madison square garden, nba opening night, nba 2026-27, lebron 76ers, sixers win, nba shorts, basketball shorts
**Pinned comment:** Rich Paul says LeBron would be a Knick right now if New York had lost the Finals. Worth the trade?

**Music:** none. **Voice:** Alex, plus two real-audio bursts (the MSG crowd, Rich Paul).

## What's on screen (all clips checked frame by frame; `sources.csv`)
| Time | Line | Footage |
|---|---|---|
| 0.0 | "LeBron James dreamed of finishing" | LeBron in a suit walking the MSG tunnel on opening night |
| 1.4 | "his career in Madison Square Garden." | The MSG scoreboard ring and the new banner |
| 3.0 | "On opening night, the Garden chanted this:" | Knicks fans filming the ceremony |
| 5.3 | **Crowd: "We don't want you!"** (real audio) | Fan video: LeBron at the free-throw line |
| 8.1 | "And the craziest part?" | LeBron in the tunnel, side view |
| 9.3 | "The only reason he's not a Knick" | Knicks team photo under the banner |
| 10.4 | "is that the Knicks won." | The 2025-26 banner |
| 11.5 | "In June, they beat the Spurs" | Brunson driving on the Spurs, Finals |
| 12.8 | "for their first title in 53 years," | The trophy, then the Knicks walking out; **FIRST TITLE / IN 53 YEARS** |
| 14.7 | "and LeBron said, 'Hey, I can't.'" | LeBron at Sixers media day; **"HEY, I CAN'T."** |
| 16.5 | "His agent said if they hadn't won:" | Rich Paul's whiteboard; **RICH PAUL, LEBRON'S AGENT** |
| 18.4 | **Rich Paul: "There would be no board. He'd be going to the Knicks."** (real audio) | Rich Paul pointing at the board |
| 20.3 | "So he signed with Philly." | LeBron close-up in a PHILA jersey at MSG, opening night |
| 21.4 | "And his Sixers debut was in the Garden, on ring night." | Brown to LeBron at the rim; Knicks players holding up their rings |
| 23.9 | "LeBron had 14, 9 and 7," | LeBron at the rim; **14 · 9 · 7** |
| 25.9 | "and the Sixers won, 106 to 100." | Sixers possession at MSG; **FINAL SIXERS 106 / KNICKS 100** |
| 28.4 | "The Garden didn't want him, so he spoiled their ring night." | Back to the tunnel shot (loop) |

**Effects (2):** ding on 53 YEARS, boom on the final score (a camera click on the media-day cut sat 1.05 s after the ding, so the renderer always dropped it).

## QA (`qa_short.py --full`, Oct 21, second QA of v2): PASS
- Audio: -14.2 LUFS, peak -1.6 dBFS, no clipping; no flash frames. The re-voiced first piece came back 5 dB quiet and was gain-matched by `splice_voice.py` like every piece.
- Hook warning (kept): the first 8 words carry no number; the conflict lands with the real chant at 5.3 s.
- **Overlap note:** posted #10 ("Did The NBA Plan LeBron's First Game?") also mentioned ring night. #62's story is different (why he isn't a Knick, the chant, Rich Paul).
- **Listen to the chant (5.3-8.0 s):** speech-to-text couldn't make out the crowd ("we know about you"); the caption uses the words Barstool, the fan poster and CBS reported.
- Several sources are small (the Finals clip 640x640 at 3.0x, the fan video and the podcast at about 2.7x), so those shots are softer than broadcast.
- Talking-head share 47% (guideline 45%); the last word ends 0.64 s before the end (loop tail wants 0.4).

**Facts:** ESPN (LeBron's Garden quote), Field Level Media (Rich Paul), NBA and USA Today (Finals), ESPN box score (final); exact quotes in `notes.md`.
**Rights:** NBA/NBC broadcast footage via official posts, a fan video via Barstool, a podcast clip via Heat Central; a Content ID claim is possible.
