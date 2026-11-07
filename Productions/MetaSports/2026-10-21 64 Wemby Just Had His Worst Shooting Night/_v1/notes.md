# #64 "Wemby just had the worst shooting night of his career" (THE #42 FORMAT, opening night)

- **Owner's ask (Oct 21):** "do a deep dive on the best/biggest stories of last night, then make 2 shorts for the best stories." Deep dive: `Research Notes/Opening Night Deep Dive (Oct 21, 2026).md`.
- **Why this story:** Legion Hoops' "worst shooting night of his career" post drew 2,725 likes and 130 replies overnight; CBS led its overreactions with it. Wemby is the No. 1 player in CBS's rankings and the MVP/DPOY favorite, so a career-worst night is a record story about the biggest young star.
- **Lane:** record (THE #42 FORMAT). **Concept (8 words):** The best defender alive just shot 1-for-13.
- **Added value:** his previous career low (checked in every ESPN game log), the unanimous-DPOY paradox, the 0-for-12 start and the flip (12 points from 1 basket).
- **Format check (`script_lint.py`):** fits 5 of 6 (count, paradox, turn, flip, length). Line 1 is a career record, not an all-time one.

## Script (Alex voice, 20.0 s)
> Victor Wembanyama just had the worst shooting night of his career. 1 for 13. And he's the first unanimous Defensive Player of the Year ever. His old low was 3 for 13, as a rookie. On opening night, he missed his first 12 shots, and a rookie blocked his dunk. So did he play badly? No. He had 13 rebounds and 6 blocks. And he still scored 12 points, with one basket.

## Claims and sources (read Oct 21, 2026)
| Claim | Source (exact words) | Check |
|---|---|---|
| Worst shooting night of his career; 1 for 13 | ESPN box score, game 401909090 (Final): Wembanyama 1-13 FG, 0-4 3PT, 10-12 FT, 12 PTS. ESPN game logs, every season 2023-24 to now: no other game with 10+ shots under 23% (next worst 3-13). Legion Hoops: "Victor Wembanyama just had the worst shooting night of his career" | PASS (by FG% on 10+ shots; a 1-for-5 in Oct 2024 was 20% on 5 shots, so the on-screen qualifier says 10+ SHOTS) |
| First unanimous Defensive Player of the Year ever | NBA on X: "first-ever unanimous DPOY"; NBA: "He's the first unanimous winner ... since the award's inception in 1982-83"; Shams: "Wembanyama is the first ever unanimous DPOY" | PASS |
| His old low was 3 for 13, as a rookie | ESPN game log 2023-24: 3-13 vs DAL, Mar 19 2024 (rookie season); the other lows are 3-12 (twice) and 4-15 | PASS (on 10+ shots; on screen: MARCH 2024, 10+ SHOTS) |
| He missed his first 12 shots | CBS live blog: "He had missed his first 12 shots before a make at the rim"; ESPN play-by-play: first make at 0.0 of the 3rd | PASS |
| A rookie blocked his dunk | ESPN play-by-play, 3rd 4:20: "Aday Mara blocks Victor Wembanyama's alley oop dunk"; SI: "OKC rookie Aday Mara" | PASS |
| 13 rebounds and 6 blocks | ESPN box score | PASS |
| 12 points with one basket | ESPN box score: 1-13 FG (a 2-point dunk) + 10-12 FT = 12 | PASS |

## Footage
Tonight's NBC broadcast via posts on X (Legion Hoops' misses compilation, ClutchPoints, Hoop Central, Spurs), the NBA's DPOY posts (trophy presentation, Apr 2026), and Spurs highlights from his rookie year (vs Golden State, Mar 11 2024; the 3-13 game itself had no Wemby-only clip). Full log in `sources.csv`.

## Titles
1. Wemby Just Had The Worst Night Of His Career 😳
2. The Best Defender Alive Just Went 1 For 13 💀
3. Wembanyama Missed His First 12 Shots 😳

**Pinned comment:** 1-for-13 with 13 rebounds and 6 blocks. Bad game or good game?

## QA notes (Oct 21)
- Voice check flagged the last word "basket" as stretched on both takes; its envelope is a normal two-syllable word (0.45 s with the k stop), kept take 1. Listen to the end.
- Most game shots are wide broadcast angles (Wemby is small in frame); the misses compilation has no close angles.
- One flash frame in the Mara block clip (a broadcast frame glitch) was replaced by the frame before.
