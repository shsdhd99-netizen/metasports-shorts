# #51 "Who Has The Most Turnovers In NBA History?" (LeBron James): THE #42 FORMAT, voice A/B slot 2

**Status (Oct 19, updated): still needs frame 1 (see Footage: every reachable angle of a LeBron turnover is too wide). Script FITS the format (`script_lint`), fact-checked, narrated in both A/B voices. NOT EDITED: frame 1 (LeBron losing the ball) needs a close clip the PC can get. Not posted.**
- `_voice_designed/` (Designed Narrator v4): 21.5 s, HNR 9.4, pitch variety 5.19, stretched x1.30. **A/B slot 2 = Designed** (order: Alex, Designed, Alex, Designed; #48 was slot 1).
- `_voice_alex/` (Alex v2): 22.5 s, HNR 8.6, pitch variety 5.08. Kept so the order never waits on a re-voice.

## Script (`script.txt`)
> LeBron James has turned the ball over more than anyone in NBA history. 5,650. And he's fourth all-time in assists. Second in turnovers is Russell Westbrook: 5,038. The NBA didn't even count them before 1977. So is he careless? No. LeBron turns it over 3.5 times a game. Westbrook: 3.9. LeBron just played more minutes than anyone, ever: 61,030.

76 spoken words. Beats: accusation, count, paradox (assists), second holder, the 1977 qualifier (it keeps "in NBA history" honest), turn, two proof numbers, the flip (volume: minutes).

## Fact check (Basketball-Reference, read Oct 19, 2026; regular season, through 2025-26)
| Claim | Source | Check |
|---|---|---|
| Most turnovers in NBA history: LeBron 5,650 | https://www.basketball-reference.com/leaders/tov_career.html (LeBron #1, active) | PASS |
| Second: Westbrook 5,038 | same page (#2; Karl Malone #3, 4,524; Harden #4, 4,505) | PASS |
| Turnovers counted only since 1977-78 | same page: "Turnovers since 1977-78 (1967-68 for ABA). Earlier totals were tracked by team, but unofficial." | PASS ("didn't even count them before 1977" = the 1977-78 season) |
| LeBron 4th all-time in assists (12,016) | https://www.basketball-reference.com/leaders/ast_career.html : Stockton 15,806, Paul 12,552, Kidd 12,091, LeBron 12,016 | PASS (checked Oct 19 earlier) |
| LeBron 3.5 turnovers a game | https://www.basketball-reference.com/players/j/jamesle01.html career row: 5,650 TOV in 1,622 G = 3.48 | PASS (rounded) |
| Westbrook 3.9 a game | https://www.basketball-reference.com/players/w/westbru01.html career row: 5,038 in 1,301 G = 3.87 | PASS (rounded) |
| Most minutes ever: 61,030 | LeBron career MP 61,030; minutes leaders #2 Kareem 57,446 | PASS |

**Shelf life (important):** the 2026-27 season starts Oct 20-21 and LeBron is still playing (41, 24th season). After his first game, 5,650 / 61,030 change. **On posting day:** re-read the two numbers and re-voice those sentences (a few credits). "Fourth in assists" holds until he passes Kidd (76 assists away, about 10 games). 3.5 and 3.9 hold all season. Not used, on purpose: "his 5,000th turnover was a Grayson Allen steal" (CBS says 2nd quarter, the play-by-play shows Allen's steal in the 3rd: sources disagree).

## Footage (edit to THE #42 FORMAT spec: frame 1 = the bad thing, 11-13 shots of about 2 s, words over footage)
**Frame 1, must have (PC, YouTube 1080p):** LeBron losing the ball, close replay. Best: **Mar 27, 2025, Lakers at Bulls, the last 10 seconds**: LeBron's inbound bounce pass is stolen by Josh Giddey (then Coby White's three; Giddey's half-court winner). Search: "Lakers Bulls ending Giddey" on the NBA / Bulls / ESPN channels; the replays show LeBron's pass up close.
- Cloud checked (Oct 19, owner away from the PC, so sourced here): **no close angle of the steal is reachable.**
  - X: @chicagobulls "6 POINTS IN 6 SECONDS" (1905447799832924646) shows it only from the high wide camera; @NBA (1905450119442694602) starts after the steal; @chicagobulls bench cam (1905453813676335253) and Dan Woike's phone video (1905448146601210346) are of the winner. Files in `src/`, logged in `src/downloads.csv`.
  - @shaqtin's 2019 LeBron inbound blooper (1102061312039927808): the replay doesn't show the pass clearly.
  - The Nov 10 2023 recap at Phoenix (NBA.com): its LeBron close-up is a foul he drew (play-by-play 1st Q 4:22), not a turnover.
  - Bulls' official "every bucket" video (`src/bulls_every_bucket_lal_0327.mp4`, 4:34-4:37) shows it only from the high wide camera (players about 40 px tall): not usable.
- Backup: any LeBron "bad pass / stripped" replay; the Nov 10, 2023 game at Phoenix has four (Q2 5:52 Nurkić steal, Q3 8:41 Allen steal, Q3 7:00 Bates-Diop strip, Q4 11:47 Bates-Diop steal). The cloud recap shows them only wide.

**Shot list (the rest can come from `Tools/nba_videos.py` in the cloud or YouTube on the PC):**
| Line | Picture | Words over footage |
|---|---|---|
| accusation | LeBron's turnover (above) | none (silent, like #42) |
| "5,650." | the same play again, slower, tighter | 5,650 TURNOVERS |
| "And he's fourth all-time in assists." | a LeBron no-look or cross-court assist | none |
| "Second in turnovers is Russell Westbrook: 5,038." | Westbrook handling / a Westbrook turnover if one exists | WESTBROOK 5,038 |
| "The NBA didn't even count them before 1977." | archival late-1970s NBA game footage (NBA channel classics) | 1977 |
| "So is he careless? No." | LeBron close-up | none |
| "LeBron turns it over 3.5 times a game." | LeBron driving | LEBRON 3.5 |
| "Westbrook: 3.9." | Westbrook driving | WESTBROOK 3.9 |
| "LeBron just played more minutes than anyone, ever: 61,030." | LeBron in a recent game, then a face | 61,030 MINUTES |

**Effects:** whoosh into LEBRON 3.5, ding on WESTBROOK 3.9, riser into the flip, pop on 61,030. None on the turnover.

## Critic (self-review, Script Critic v3 + format gate)
| Premise | Hook | Clarity | Progression | Payoff | Voice | Visual | Originality | Retention | Total | Accuracy | Format |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | **36/45 APPROVE** | PASS | FITS |

Originality is 3 because it is the second LeBron post in the format (#42 was LeBron). Star spacing: fine right after #48 (Harden); never next to another LeBron Short.
