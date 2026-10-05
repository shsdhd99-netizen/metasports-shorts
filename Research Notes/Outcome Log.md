# Outcome log (fill from YouTube Studio 24 h and 7 d after posting)
Purpose: test whether our gate metrics predict results. One row per posted Short. Paste Studio numbers from the user.

| Short | Posted (date/time ET) | Lane | Title opener | Avg shot (s) | Length (s) | Caption style | Hook text | Music | Viewed % (24 h) | Avg % viewed | Views 48 h | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #12 Duren (v2) | Oct 3-4 | contract | Did | 1.9 | 33 | metasports | no | no | 63.0% (stayed) | 59.7% | 1.5K (5 h 27 min), rank 8 of 10 | 38 likes. User's Studio screenshots, Oct 4 ~12:30 |
| #03 Wembanyama (How Did Nobody Vote Against Wemby) | Oct 3-4 | rule/record oddity | How | n/a (Claude v3 cut) | 24 | clank-style | no | no | 79.5% (stayed) | 100.3% | 20.6K (9 h 52 min), rank 2 of 10 | 413 likes, subs +11 and up; comments are about the name spelling |

## Read of the first two results (Oct 4; n=2, early, topics differ, so a pattern not a proof)
- Wemby 24 s beat Duren 33 s on every metric: stayed-to-watch 79.5% vs 63.0%, avg % viewed 100.3% vs 59.7%, ~14x the views per hour.
- Wemby script: universal rule hook ('Every Defensive Player of the Year ... had at least one voter who picked somebody else'), 'Until Wembanyama', 'but that's not even the crazy part', a 3-name list payoff ('That's the whole list'), ends on the payoff, NOT a question. Duren: contract story with a $ gap and a 'did he lose?' question.
- Matches Round 5 lane data (rule/record oddity strong, contract flat). Does NOT support 'longer is better' for us: the shorter Short did better. Retention curves not yet processed (up to 2 days).

| #18 LeBron helicopter | Oct 4 | funny/petty | LeBron | 1.2 | 26.8 | metasports | yes | no | ? | ? | 9 views in first 59 min (rank 8 of 10), Wemby now ~18K | posted by user; read at 24 h |

## Public views snapshot, Oct 5 2026 (free check: `python3 Tools/channel_check.py @MetaSportsClips`, via yt-dlp; views only, no retention)
| Short | Views | Note |
|---|---|---|
| Why Two Men Can Still Wear Six (#22 rebuilt: payoff ending, corrected "two") | ~29,000 | best of last 7 within about a day; first Short built to the new payoff standard |
| This NBA Player Sleeps On The FLOOR? (Steven Adams) | ~28,000 | real-voice Adams quote Short |
| How Did Nobody Vote Against Wemby? | ~26,000 | the benchmark (79.5% stayed / 100.3% AVD) |
| Did Jalen Duren Just Leave $87 Million? | ~2,600 | contract lane, question ending |
| LeBron Left Sixers Practice By Helicopter (#18) | ~2,400 | |
| The NBA Final That Does Not Count | ~249 | |
| Would Jordan's Last Shot Be a Foul Now? | ~7 | |
Reading (HYPOTHESIS, n small, views not retention): surprise-fact / rule-oddity Shorts with a payoff ending and real voices (Wemby, #22, Adams) land 26-29K; contract lane (Duren) and the LeBron helicopter story sit near 2.5K. Matches Round 5 lane rule. Get avg % viewed from Studio screenshots or vidIQ before changing any rule.
