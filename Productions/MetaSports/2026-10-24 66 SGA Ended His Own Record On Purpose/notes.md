# #66 SGA ended his own record on purpose (DRAFT finished Oct 24, 2026)

**Status (Oct 24, cloud):** finished draft, QA PASS, awaiting the owner's approval. Voice: Alex, take 2 of 2 (take 1 garbled "Gilgeous-Alexander"), tightened to 24.6 s. 16 shots, words over footage on 7 (141, 20+ PTS, 126, 72, 17 PTS, 1:43 LEFT, 141). File and upload package: `UPLOAD.md`.
- **Footage:** all official. Thunder team site on the NBA.com CDN (`Tools/nba_videos.py`): "Highlights: OKC 96, DEN 84" (Oct 23, the game itself), "2 Consistent. 2x MVP" (May 17 2026 reel, the close-ups), "SGA - 10/5" press conference (illustrative for the quote); a Chicago Bulls 1996 clip (Jordan); the 1962 AP Wilt photo (public domain, Wikimedia, 960 px).
- **Slowed shots** (`src/*_slow.mp4`, made with ffmpeg `setpts`): face 0.42x, two fingers 0.75x, celebration 0.75x, Braun 0.75x, SGA walking 0.70x, Jordan 0.72x. The reel's close-ups last 0.5-1 s between flash transitions, so slowing was the only way to fill a line with a clean close-up.
- **Overlays:** `_ov/A*.json`, applied by `sh _ov/apply.sh` after `cut_list.py` (keeps the clean cuts as `clips/*_raw.mp4`). Re-cutting with `--force` loses them: run apply.sh again.
- **Illustrative shots (said in UPLOAD.md):** Braun at a 3rd-quarter timeout for "Denver had pulled their starters" (the 1:43 timeout is not in the highlights); SGA walking at 2:53 for "asked to come out"; the Oct 5 press conference for his quote.
- **Not found:** a post-game interview or the moment he sat down (the Thunder site has no post-game video for this game).

**Earlier status:** script verified in a cloud session that could not reach ElevenLabs.
**Timely:** the game was Thu Oct 22, 2026. Post by Sun Oct 25 at the latest, or drop it (Diagnosis rule: news only while fresh).

- **Lane:** THE #42 FORMAT, record variant (a famous record, a paradox, "So was he...? No.", end on the number). Lint: fits on 5 of 6 checks; line 1 is a record line, not a "more than anyone" accusation.
- **Concept (8 words):** the greatest scoring streak, ended by choice, out of respect.
- **Added value:** most coverage says "streak snapped"; we show he asked out because Denver had pulled its starters.
- **Script:** 82 spoken words, about 24 s at the house pace. Numbers: 141, 20, 126, 72, 17, 141 (6).

| Line | Source | Exact quote |
|---|---|---|
| Longest streak in NBA history: 141 straight games with 20+ | ClutchPoints, Oct 23 2026: https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-shai-gilgeous-alexanders-record-141-game-20-point-streak-snapped-win-nuggets | "141 straight regular-season games with at least 20 points" |
| Wilt's record was 126 | same | "longtime mark of 126 straight 20-point games" |
| Jordan's best was 72 | CBS Sports, Oct 23 2026: https://www.cbssports.com/nba/news/shai-gilgeous-alexander-20-point-streak-record-may-never-be-broken/ | Jordan and Durant: 72 games each |
| Thursday; he finished on 17 | ClutchPoints (as above) | "17 points in the Thunder's 96-84 home win over the Denver Nuggets" |
| Under two minutes left; Denver pulled its starters | Bleacher Report, Oct 23 2026: https://bleacherreport.com/articles/25519316-sga-reacts-historic-20-point-game-streak-ending-always-treat-game-respect | Denver called a timeout "1:43 remaining in the fourth" and subbed its starters |
| He asked to come out | same (coach Daigneault) | "asked out of the game" |
| His words | same | "I feel like you always treat the game with respect." |

**Do not say:** the start date (sources differ: Oct 30 vs Nov 1, 2024); "every game for two years" (the streak counts regular-season games played); "reigning MVP" without a fresh check.

**Footage plan (frame 1 = the surprising thing):**
1. Frame 1: SGA walking to the bench / sitting down late in the Oct 22 game (Thunder team site via `Tools/nba_videos.py`, or the ESPN game summary clips, on the PC).
2. The record night: Mar 12, 2026 vs Boston (127th game), official Thunder/NBA clips.
3. Wilt: still photo only (no identifiable Wilt film; see #43). Jordan: official NBA clip or photo.
4. "Denver pulled their starters": the Nuggets' bench at the 1:43 timeout from the same broadcast.
5. Words over footage: 141 / WILT 126 / JORDAN 72 / 17 (zero cards, as in #42).

**Title options (house style):**
- Why SGA Ended His Own NBA Record 😳 #nba
- SGA Ended The Longest Streak In NBA History On Purpose 😳 #nba
