# #78 The NBA star who skipped a Finals practice to go wrestling (Ahmed-style TEST, Oct 28 2026)

- **Why:** owner, Oct 28: "a short in ahmed style for metasports clips? for test purposes". First story-format (Ahmed's Basketball shape) Short on the NBA channel: spoken title as line 1, "Back in 1998...", a turn every 8-12 s, ironic payoff with a number, about 55 s, centred captions + title card, music and no-music renders.
- **Lane:** refused/defiant + rivalry that leaves the sport (study: `Research Notes/NBA Viral Topics + Ahmed Basketball (Oct 23, 2026).md`, pick #2).
- **Concept (8 words):** Rodman skipped Finals practice for wrestling, then won.
- **Copy check:** `copy_check.py "Rodman skipped Finals practice wrestling"` = FRESH (WWE's long video, three small channels); Ahmed's Basketball has no Rodman Short.
- **Added value:** the Game 4 box score (14 rebounds, 5-of-6 free throws in the 4th by a .550 shooter), Bob Costas' real on-air line, and the 2026 WWE Hall of Fame payoff.
- **Real audio:** Costas, NBC, Game 6, in his own voice: "...scheduled to wrestle in one of those bogus events next month."

## Claims and sources
| Line | Source | Exact |
|---|---|---|
| 1998, Bulls two wins from a sixth title, just beat Utah by 42 | Wikipedia "1998 NBA Finals"; Bleacher Report | "Game 3 June 7 Utah Jazz 54–96 Chicago Bulls"; "a 96–54 loss... the 42-point loss"; B/R: "The Bulls were two wins away" |
| The next day Rodman was gone, flew to Michigan, live wrestling TV with Hogan | SI (Justin Barrasso, Apr 27 2020); Bleacher Report | SI: "Rodman flew from Chicago to Detroit to appear live on Nitro at the Palace of Auburn Hills... where he and Hogan attacked Diamond Dallas Page" |
| NBA fined him $10,000 | Bleacher Report (2018) | "The NBA fined Rodman $10,000 for missing his mandated media availability." (Wikipedia says $20,000; the team fine is reported as undisclosed; we use the NBA's $10,000 only) |
| Agent: the Bulls quietly gave their blessing | Bleacher Report, Dwight Manley | "Behind the scenes, Jerry and Phil gave their blessing" |
| Game 4, guarding Karl Malone, MVP the year before | Wikipedia Rodman; 1997 MVP Malone | "again shutting down Malone in Game Four" |
| 14 rebounds | Basketball-Reference box 199806100CHI; NBC graphic on screen | Rodman 29:38, 6 pts, 14 reb (7 off.) |
| 4th quarter: 5 of 6 FTs, a 55% shooter | BR box (4th-quarter split) + BR season | Q4: 5-6 FT; 1997-98 FT% .550 |
| Bulls won by four | BR / NBC graphic | 86-82 |
| Game 6: tripped Malone, technical; announcer on air | Bleacher Report; NBC broadcast audio (Ballislife clip) | "Rodman drawing a technical foul after tripping Malone"; Costas: "...scheduled to wrestle in one of those bogus events next month" |
| Jordan hit the last shot, Bulls won the title | Wikipedia | Game 6 87-86 |
| Less than a month later, Rodman & Hogan vs Malone & DDP; Rodman won | Wikipedia "Bash at the Beach (1998)" | July 12 1998; "less than a month after Rodman and Malone clashed in the 1998 NBA Finals" |
| 580,000 pay-per-views | Wikipedia (Wrestlenomics) | "buy rate of 1.50 which is equivalent to 580,000 total buys" |
| 28 years later, the WWE Hall of Fame | Wikipedia Rodman; WWE on X (Apr 18 2026); Shams (Mar 20 2026) | "WWE Hall of Fame (Class of 2026)"; WWE: "Dennis Rodman is officially in the #WWEHOF!!" |

## Footage
- NBC's 1998 Finals broadcasts of Games 3, 4 and 6 from archive.org (low resolution, 4:3).
- HD Game 6 clip of the Rodman-Malone tangle with Costas' commentary (Ballislife on X, July 2024).
- Bash at the Beach 1998 clips (@big_business_ and Covers on X); WWE's official Hall of Fame 2026 video (WWE on X). WCW footage is WWE-owned: kept to short shots, its own sound muted under the narration.
- **Illustrative:** K06/K07 Nitro shots are from WCW Nitro broadcasts in the WWE video, not proven to be the June 8 1998 episode. K02/K11 HD Finals shots are Game 6 (the line is about the series). K04's graphic reads 94-54 with 36 s left (final 96-54).
- **Archive blow-ups (no better source exists):** the 1998 NBC broadcasts on archive.org are 720x480 (4:3). Face shots K05, K08 and K11B use a 3:4 blur-fit window (about 3x); the HD X clips (1280x720) are blown up about 2.7x. One-frame flashes in nine clips (K01, K06, K09, K11, K13, K18, K19, K25, K29) were removed with `Tools/deflash.py`; the originals are in `_check/preflash/`.

## Real audio
- Bob Costas' Game 6 line ("scheduled to wrestle in one of those bogus events next month") plays in his own voice from the HD clip at 33.84-37.72 s; K18/K19 are cut from the same seconds so the picture matches. Mixed with `Tools/nat_sound.py --burst 33.84-37.72 --bed-db -30 --tail 0.1`, with the WCW/WWE-source shots and the Costas clip's other shots muted (`--clip-db ...=-60`).
- Risk: 4 s of NBC broadcast audio makes a Content ID claim more likely. If one blocks the Short, re-render without the burst (narrate the line instead).

## QA
- Both versions (music, no music): `qa_short.py --profile story --full` PASS, 55.0 s. Gemini pre-check (music version): READY (report: `Research Notes/Watch Reports/drafts/78_rodman_precheck.json`, tier [S]). Warns left: talking head 58% (the story is about two people), hook has no number in the first 8 words (Ahmed's titles rarely do), one caption under 0.25 s at 33.47 s (the splice into Costas' line).
