# Jokic triple-double record: pre-build (Sun Nov 1, 2026)

**Status: `voice-ready`** (research, script with record-night slots, footage list and day-of checklist done; no voice, no footage downloaded). Not voiced on purpose: line 1 and the night line depend on the night.

## 1. Verified facts (as of Sun Nov 1, 2026)
| Fact | Source | Note |
|---|---|---|
| Jokic recorded his **200th regular-season triple-double on Wed Oct 28, 2026**, a 104-91 win at New Orleans: 21 points, 13 rebounds, 10 assists. | [ESPN, Oct 28](https://www.espn.com/nba/story/_/id/50314211/nuggets-nikola-jokic-notches-200th-career-triple-double-win-vs-pelicans) | His 2nd of this season |
| He is the 2nd player past 200. Westbrook reached 200 in his **1,175th game**, Jokic in his **814th**. | same ESPN piece | |
| Westbrook's record is **209** regular-season triple-doubles. | [Fantasy Nerds, Aug 12, 2026](https://fantasynerds.com/news/story/2026/08/12/russell-westbrook-retires-as-nbas-triple-double-king-jokic-poised-to-take-crown-1595127); [AOL, Apr 2026](https://www.aol.com/articles/nba-announces-nikola-jokics-latest-055320212.html) | Regular season only. A search summary also mentioned a combined regular-season + playoff count of 221 each; **unverified, do not use** |
| **The gap is reported two ways.** ESPN's text says he "needs 10 more" to supplant Westbrook; the same page's headline says "9 behind". 200 vs 209 means 9 to tie and 10 to break. | ESPN link above | Word it "ties at 209, breaks at 210". Never "9 away from the record" |
| 2025-26: 32 triple-doubles in 61 games as of early April 2026 (about 0.52 per game). | [AOL, Apr 2026](https://www.aol.com/articles/nba-announces-nikola-jokics-latest-055320212.html) | Final season total not verified |
| 2024-25: 34 triple-doubles in 70 games. | a search summary of Eurohoops reports; ESPN's Oct 28 piece also says 34 last season | Second-hand, unverified in full |
| **Count now: 200 confirmed.** The Oct 30 game at Phoenix (W 127-120) is not confirmed: no source found with his line. So "200, possibly 201". | [Land of Basketball schedule](https://www.landofbasketball.com/results_by_team/2026_2027_nuggets.htm) (result only) | First task on the day: Basketball-Reference game log |
| Debut Oct 28, 2015, 2 points. | Account 2 brief, citing Basketball-Reference | **Not re-verified.** The script does not use it |

## 2. Projected record night
Nuggets schedule from [Land of Basketball](https://www.landofbasketball.com/results_by_team/2026_2027_nuggets.htm) (secondary source; check NBA.com): game 6 is Nov 2 (POR), then Nov 4, 7, 9, 11, 14, 16, 18 (BOS), 20, 22, 24, 27, 29, 30, Dec 2 (game 20), a gap to Dec 12 (game 21), Dec 15, 17 (ATL), 19 (LAL, game 24), 21 (@LAC), 23 (@LAL, game 26), 25 (@GSW, game 27), 27, 28, 31 (game 30).

**This is a projection, not a fact.** He needs 10 to break (9 to tie). At last season's pace of about 0.52 per game, 10 takes about 19 games from game 6, so around game 24 to 25.
- **Fast case** (0.6 per game, no missed games): about 17 games, game 22-23, **Dec 15-17**.
- **Central case** (0.52): game 24-25, **Dec 19-23** (the Lakers twice).
- **Slow case** (0.4 per game, or missed games): game 30-31, **Dec 31 to Jan 2**, or mid-January.
- **Window to hold open: Dec 12 to Jan 14.** The tie (209) comes about one triple-double earlier and is also postable.
- Caveat: this season's start is 2 known triple-doubles in 4 games before Oct 30; the sample is small.

## 3. Script (house style, 20-30 s)
Rules applied from [THE 42 FORMAT](../../Library/THE%2042%20FORMAT.md): line 1 is 11 words or fewer and states the news, each number is its own sentence, one fact the clip cannot show (the games comparison), end on the payoff, no CTA, no question. `{a|b}` is our caption|spoken pair.

**Record-night version** (about 45 words plus the slots, about 20-24 s):

> Nikola Jokic just passed Russell Westbrook for the most triple-doubles ever.
> [SLOT A] {210|Two hundred ten}.
> Westbrook needed {1,175|eleven hundred seventy-five} games to reach {200|two hundred}.
> Jokic did it in {814|eight fourteen}.
> [SLOT B] Tonight, against [OPPONENT]: [X] points, [Y] rebounds, [Z] assists.
> [SLOT C, only if verified on the day] one human detail from the night (the assist he got it on, who passed him the ball).

- Line 1 is 11 words.
- **Tie version:** "Nikola Jokic just tied Russell Westbrook's triple-double record." Slot A = "{209|Two hundred nine}."
- The 1,175 and 814 figures are verified (ESPN, Oct 28). Slots A and B come from the box score. Slot C is optional and must be sourced.
- After filling the slots run `script_lint.py` and `copy_check.py`, then `voice_take.py`.

## 4. Footage list to prepare (nothing downloaded yet)
Frame 1 must show the record moment, so the night's clip leads. Everything else is cut ahead.
1. **Record night:** the stat-completing assist or rebound plus the arena reaction. **Slot, added the night of.**
2. **Jokic's 200th, Oct 28 at New Orleans** (21/13/10): the completing play, from the ESPN game video via the summary API (see `Footage Sources.md`).
3. **Westbrook** triple-double highlights of a recent season (pick one with a verifiable date; source it in notes.md).
4. **Jokic passing** highlights from 2025-26 for the middle shots, one player on screen per line.
5. Words over footage, no cards: `210`, `1,175`, `814`.
Footage test: frame 1 plus one proof clip per beat must exist before voicing.

## 5. Re-check on the day (before voicing)
1. Jokic's regular-season count after the game (NBA.com game log, Basketball-Reference), regular season only.
2. Westbrook's total is still 209 on Basketball-Reference (earlier sources show 202 in Jan 2025 and 203, which were older counts).
3. Opponent, date, final score, exact line, and when in the game the record-making stat came.
4. Whether it was the tie (209) or the break (210); word the script for the one that happened.
5. 1,175 and 814 are fixed for the 200th, but re-confirm if any line talks about the 210th.
6. Pronunciation entries for Jokic and Westbrook in `Tools/pronunciation.json`.
7. Timing: news, so post the morning after the night.
