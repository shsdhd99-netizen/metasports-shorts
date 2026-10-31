# UPLOAD: #63 All Three Williamses Got A Technical (opening night, one-second oddity)

**DRAFT, awaiting your approval. Not posted, not scheduled.**
**File:** `DRAFT - awaiting approval - 63 Three Williams three technicals v2 (no music).mp4` (same as `final.mp4`, 26.8 s, 1080x1920). v2 (Oct 21): the referee's own announcement replaces the Wemby 1-for-13 section, which now lives only in #64. v1 is in `_v1/`. Video files are not in git; rebuild with `python Tools/assemble.py --folder "<this folder>" --no-music` after re-cutting from `src/` (every in-point and crop is in `sources.csv`; voice pieces `_n1`, `_n2` + `plan.json` for `splice_voice.py`).
**Timing:** Oct 22, late-morning slot (a day after #64, same game, different story, no shared footage). An oddity, so it ages slower than a result story.

**Title (exactly as written):** All Three Williamses Got A Technical 😳
**Other titles:** Three Williamses, Three Technicals 💀 / Why Three Thunder Players Got Technicals 😳
**Hashtags (up to 3):** #nba #thunder #spurs
**Tags:** thunder spurs, thunder vs spurs, thunder spurs fight, de'aaron fox chet holmgren, fox throws chet, jaylin williams, jalen williams, kenrich williams, three williams technical, williams technical fouls, referee announcement, nba referee mic, wembanyama technical, victor wembanyama, flagrant foul, nba fight, nba scuffle, nba opening night, nba 2026-27, western conference finals rematch, okc thunder, san antonio spurs, nba shorts, basketball shorts
**Pinned comment:** Fox threw Chet to the floor and three Williamses got T'd up for it. Who was right?

**Music:** none. **Voice:** Alex.

## What's on screen (all clips checked frame by frame; `sources.csv`)
| Time | Line | Footage |
|---|---|---|
| 0.0 | "All three Thunder players named Williams" | Kenrich Williams yelling at Fox, Jaylin's WILLIAMS nameplate beside them (slow-mo replay) |
| 1.4 | "got a technical foul, on the same play." | Overhead of the scrum; wide of both teams converging |
| 3.4 | "It started when De'Aaron Fox threw Chet Holmgren to the floor." | Wide of the post-up; baseline replay of Chet hitting the floor |
| 6.1 | "Jaylin Williams shoved Fox." | Close: #6 WILLIAMS shoving, Chet on the floor |
| 7.6 | "Victor Wembanyama got into a shoving match with Jaylin." | Wemby close-up; replay of Wemby and #6 shoving |
| 9.9 | "Then Jalen Williams and Kenrich Williams jumped in." | Overhead: #34 WILLIAMS in the scrum |
| 12.2 | "Fox got a flagrant. Wemby got a technical." | Mid-court replay of the throw (**FLAGRANT 1, DE'AARON FOX**); Wemby at the bench (**TECHNICAL, WEMBANYAMA**) |
| 14.3 | "And then the referee read this out:" | The crew chief at the courtside mic (OFFICIAL REVIEW on the scorebug) |
| 15.9 | **Real referee audio:** "And then Kenrich Williams, Jalen Williams, and Jaylin Williams will receive technical fouls." | #34 WILLIAMS held back (**T: KENRICH**); Jalen Williams smiling (**T: JALEN**); #6 shoving (**T: JAYLIN**); overhead of #8 and #34 (**3 WILLIAMSES, 3 TECHNICALS**) |
| 20.7 | "And the Thunder beat the Spurs by 12." | SGA isolating (**FINAL: THUNDER 116 / SPURS 104**) |
| 23.3 | "Three Williamses, three technicals, one win." | Slow-mo faces (a Thunder player at Wemby); back to the opening shot (loop) |

**Effects (3):** thud as Chet hits the floor, whistle on the flagrant, boom on the final score.

## QA (`qa_short.py --full`, Oct 21, second QA of v2)
- Audio: -14.2 LUFS, peak -1.3 dBFS, no clipping; no flash frames; captions match the script.
- **Names:** the QA's speech-to-text scores 88% (FIX) only because it hears "Kendrick" for Kenrich, "Jalen" for Jaylin (same sound), "the Aaron" for De'Aaron. Re-run with the players' names as a hint, it hears "Kenrich", "De'Aaron" and "Wembanyama" correctly in the narration; the referee's own words transcribe as "Kenrich Williams, Jalen Williams, and Jaylin Williams". Listen once to the names anyway.
- The referee audio is ESPN's clip of the NBC broadcast; the 0.5 s pause in the middle of his sentence was cut.
- The last word ends 0.6 s before the end (loop tail wants 0.4).

**Facts:** ESPN play-by-play and final box score, the referee's announcement (ESPN clip), CBS live blog, ClutchPoints; exact quotes in `notes.md`.
**Rights:** NBA on NBC broadcast footage via posts on X and ESPN; a Content ID claim is possible.
