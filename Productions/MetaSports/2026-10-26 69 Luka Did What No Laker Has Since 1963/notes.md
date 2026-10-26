# #69 Luka did what no Laker has done since 1963 (DRAFT, Oct 26, 2026)

**Status:** finished draft, QA PASS (`qa_short.py --full`), awaiting the owner's approval. Voice: Alex, take 2 of 2 (take 1 failed the shimmer gate), tightened to 20.0 s. No music.
**Timely:** the game was Sun Oct 25, 2026 (Lakers 132, Jazz 123, in Salt Lake City). Post Mon Oct 26 at 11:00 AM ET, or drop it.

- **Lane:** same-day news with a number gap, household names (#58 style). Not THE #42 FORMAT (no "So is he...? No." beat), so the format rotation stays clean.
- **Concept (8 words):** 52 and 10: no Laker since 1963.
- **Added value:** the coverage leads with "season-high 52"; we lead with the gap. Kobe, Shaq and LeBron never did it as Lakers; only Baylor and West ever had.
- **Copy-check (Oct 26):** "Luka 52 points 10 assists Lakers": FRESH (biggest: 6.9K on an unrelated jersey clip).
- **Script:** 74 spoken words, 20.0 s. Numbers: 52, 10, 1963, 18, 8, 10 of 11, 63.

| Line | Source | Exact words |
|---|---|---|
| 52 points and 10 assists | ESPN box score, game 401909861 (17-30 FG, 8-18 3PT, 10-11 FT, 8 REB, 10 AST, 38 MIN) and the AP recap on ESPN: https://www.espn.com/nba/story/_/id/50282749/luka-doncic-scores-nba-season-high-52-points-lakers-win-vs-jazz | "Luka Doncic scored 52 points, hitting eight 3-pointers" ... "Doncic also had 10 assists" |
| No Laker had done that since 1963; only two ever had (Elgin Baylor, Jerry West) | Yahoo Sports (Lakers Daily), Oct 25 2026: https://sports.yahoo.com/articles/luka-doncics-big-shot-puts-231633474.html | "the first Laker since 1963 to record at least 50 points and 10 assists in a game. He joins Elgin Baylor and Jerry West as the only players in the team's history to accomplish the feat." |
| Kobe / Shaq / LeBron never did it | follows from the line above (all three are Lakers who are not Baylor or West). Said as Lakers only: the script never claims LeBron didn't do it in Cleveland or Miami | |
| Utah led by 18 | AP recap (ESPN): "the Jazz, who blew an 18-point second-quarter lead"; theScore: "clawed back from an 18-point deficit at the end of the first quarter" (sources differ on the quarter, so the script gives no quarter) | |
| Back-to-back threes in the last two minutes | AP recap: "back-to-back 3s that gave Los Angeles a 127-121 lead with 1:42 left" | |
| 8 threes, 10 of 11 free throws | ESPN box score (8-18 3PT, 10-11 FT) | |
| 63 years ago | 2026 - 1963 | |

**Also true, not used (one measure per Short):** his 10th career 50-point game ties Kareem (11th most in NBA history, Yahoo); the first 50-point game of the 2026-27 season (ESPN); NBA on X: "first player in Lakers franchise history to record 50+ PTS, 10+ AST, 5+ REB, and 5+ 3PM".
**Do not say:** "first in NBA history" (it's a Lakers record); a quarter for the 18-point lead (sources differ).

**Footage:** NBA on X, Oct 26 2026 00:01 UTC, "LUKA JUST ERUPTED FOR 52 POINTS" (`src/2114507747983302667.mp4`, 1080x1080, 179 s). The game plays are wide, so they sit whole over a blurred fill (`blurfit`); close-ups are cropped. Photos (Wikimedia Commons): Kobe Bryant, Dec 3 2014 (Keith Allison, CC BY-SA 2.0); Shaquille O'Neal, Sep 19 2023 (TechCrunch, CC BY 2.0; not a Lakers-era photo); LeBron James, Lakers at Cavaliers, Mar 21 2022 (Erik Drost, CC BY 2.0); Elgin Baylor, 1969 Lakers program cover (public domain); Jerry West, 1972 (Malcolm W. Emmons, public domain). Credits for the CC photos are in UPLOAD.md's pinned-comment note.
**Illustrative shots:** A03 (a 2nd-quarter Luka possession) under "52 points and 10 assists"; A07 (a 1st-quarter possession) under "Utah led by 18"; A11 (a close-up between the two late threes) under "10 of 11 free throws".
**Shot A03:** one washed-out frame at 0.9 s removed with `Tools/deflash.py`.
