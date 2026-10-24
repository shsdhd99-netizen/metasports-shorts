# #39 How Old Is The Oldest Triple-Double Ever? (2026-10-06)

Lane: record oddity. Concept: LeBron owns the oldest-triple-double record and has broken it three times; he will be 41y 294d on opening night. Added value: verified day-counts, 46-day span, opening-night age math.

## What is actually new? (premise audit) - CLAIM FIXED
The idea bank said 'LeBron broke Malone's record in Feb 2026 and is 41 now'. That is incomplete: he broke it THREE times in 2025-26. Sources:
- Feb 12 2026 vs DAL: 41y 44d, broke Malone's 40y 127d (Nov 28 2003). NBC News https://www.nbcnews.com/sports/nba/lebron-james-becomes-oldest-player-triple-double-nba-history-rcna258886 ; NBA X post 2022191714077954154.
- Mar 19 2026 at MIA: 41y 79d, 124th career TD (19-15-10), per Lakers via Ryan Ward https://x.com/RyanWardLA/status/2034827442888835487
- Mar 30 2026 vs WAS: 41y 90d, 125th career TD (21-10-12), 'passing his own mark (41 years, 79 days)' per Dave McMenamin (ESPN) https://x.com/mcten/status/2038831375508467791 ; Brett Siegel https://x.com/BrettSiegelNBA/status/2038831031692693943
- Basketball-Reference LeBron 2025-26 game log (read Oct 5): exactly three triple-doubles, dates 2026-02-12 DAL (28-10-12), 2026-03-19 MIA (19-15-10), 2026-03-30 WAS (21-10-12); no playoff triple-doubles. https://www.basketball-reference.com/players/j/jamesle01/gamelog/2026/
- Malone: 40y 127d, Nov 28 2003 vs Spurs (10 pts, 11 reb, 10 ast), ESPN/NBC. The B-Ref 'oldest to record a triple-double' list page was not reachable from this cloud (404/Cloudflare); the game log + ESPN/NBC are the sources.
- Date math (python): Feb 12 -> Mar 30 = 46 days; Mar 19 -> Mar 30 = 11 days; Dec 30 1984 birth -> Oct 20 2026 = 41y 294d. Opening night = Sixers at Knicks Tue Oct 20 2026 7:00p ET (B-Ref 2026-27 PHI schedule https://www.basketball-reference.com/teams/PHI/2027_games.html).
- 'Nobody else is close': not claimed. The record is LeBron's own, so any new LeBron triple-double is by definition the oldest ever (he is past 41y 90d on Mar 31 2026).

## NOT verified / warnings
- FOOTAGE MISMATCH: no official clips of the Mar 19 (MIA) and Mar 30 (WAS) games were found. Shots under 'record 2' and 'record 3' are other 2025-26 Lakers LeBron footage (Feb 12 DAL game and an April GSW game, official NBA X posts 2022191714077954154 and 2042459600360714737), not the March games. The Feb record shots ARE from Feb 12. Consider swapping if the user finds the Heat/Wizards clips.
- Malone shots are his 2003 Lakers introductory press conference (X, Ballislife 1945913184876925407, 320x240), not the triple-double game.
- voice_check flagged 'a hundred twenty-seven' as REDO but its own text shows it heard '127': a false positive from number parsing; listen once.
- The age numbers on screen (41Y 44D etc.) are baked into the footage, not cards.
- If LeBron gets hurt or the opener moves, the last two lines change. Post before Oct 20.
