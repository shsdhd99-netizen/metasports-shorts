# UPLOAD: #63 All Three Williamses Got A Technical (opening night, one-second oddity)

**DRAFT, awaiting your approval. Not posted, not scheduled.**
**File:** `DRAFT - awaiting approval - 63 Three Williams three technicals (no music).mp4` (same as `final.mp4`, 28.5 s, 1080x1920). Video files are not in git; rebuild with `python Tools/assemble.py --folder "<this folder>" --no-music` after re-cutting from `src/` (every in-point and crop is in `sources.csv`; voice pieces `_n1`, `_n2` + `plan.json` for `splice_voice.py`).
**Timing:** tonight/tomorrow. The game ended 04:25 UTC Oct 21; the scuffle clips are about two hours old.

**Title (exactly as written):** All Three Williamses Got A Technical 😳
**Other titles:** Three Williamses, Three Technicals 💀 / Why Three Thunder Players Got Technicals 😳
**Hashtags (up to 3):** #nba #thunder #spurs
**Tags:** thunder spurs, thunder vs spurs, thunder spurs fight, de'aaron fox chet holmgren, fox throws chet, jaylin williams, jalen williams, kenrich williams, three williams technical, wembanyama technical, victor wembanyama, wemby 1 for 13, shai gilgeous-alexander, sga 32 points, aday mara block, nba opening night, nba 2026-27, flagrant foul, nba fight, western conference finals rematch, okc thunder, san antonio spurs, nba shorts, basketball shorts
**Pinned comment:** Fox threw Chet to the floor and three Williamses got T'd up for it. Who was right?

**Music:** none. **Voice:** Alex.

## What's on screen (all clips checked frame by frame; `sources.csv`)
| Time | Line | Footage |
|---|---|---|
| 0.0 | "All three Thunder players named Williams" | Kenrich Williams yelling at Fox, Jaylin's WILLIAMS nameplate beside them (slow-mo replay) |
| 1.5 | "got a technical foul, on the same play." | Overhead of the scrum; wide of both teams converging |
| 3.4 | "It started when De'Aaron Fox threw Chet Holmgren to the floor." | Wide of the post-up; baseline replay of Chet hitting the floor |
| 6.3 | "Jaylin Williams shoved Fox." | Close: #6 WILLIAMS shoving, Chet on the floor |
| 7.9 | "Victor Wembanyama got into a shoving match with Jaylin." | Wemby close-up; replay of Wemby and #6 shoving |
| 10.5 | "Then Jalen Williams and Kenrich Williams jumped in." | Overhead: #34 WILLIAMS in the scrum |
| 12.6 | "Fox got a flagrant. Wemby got a technical." | Mid-court replay of the throw (**FLAGRANT 1, DE'AARON FOX**); Wemby at the bench (**TECHNICAL, WEMBANYAMA**) |
| 14.5 | "And so did all three Williamses." | Overhead: #8 and #34 WILLIAMS held back; **T: JAYLIN / JALEN / KENRICH** |
| 15.8 | "But Wemby's night got worse. He missed his first 12 shots." | Wemby close; Aday Mara blocks Wemby's dunk (**0 FOR 12**) |
| 19.2 | "He finished 1 for 13." | Wemby blocking Chet (**1 FOR 13**) |
| 20.5 | "The Thunder won, 116 to 104, and SGA had 32." | SGA isolating on Dylan Harper (**FINAL THUNDER 116 / SPURS 104**); SGA close-up (**32 PTS**) |
| 24.7 | "Three Williamses, three technicals, and a 12-point win." | Slow-mo faces (a Thunder player at Wemby); back to the opening shot (loop) |

**Effects (3):** thud as Chet hits the floor, whistle on the flagrant, boom on the final score.

## QA (`qa_short.py --full`, Oct 21): PASS
- **Listen to the names:** speech-to-text heard "Kendrick" for Kenrich and "Jaylen" for Jaylin and Jalen.
- The Spurs posts are 720x720 (2.67x blow-up), so two Wemby shots are softer.
- The last word ends 0.6 s before the end (loop tail wants 0.4).

**Facts:** ESPN play-by-play and final box score, CBS live blog, ClutchPoints; exact quotes in `notes.md`.
**Rights:** NBA on NBC broadcast footage via posts on X; a Content ID claim is possible.
