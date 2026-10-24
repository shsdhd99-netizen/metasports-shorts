# #58 "The Lakers cut their #17 pick to keep their #55" (Knecht waived, Bronny kept)

- **Owner's ask (Oct 19 evening):** "the lakers just picked dalton knecht over bronny james. make a short about it!" The reports say the reverse: on Monday Oct 19 2026 the Lakers **waived Knecht and kept Bronny**. The Short follows the reports.
- **Lane:** number gap + roster rule (16 players, 15 spots). Contract/roster stories are flat unless a rule or a number gap is the hook (Round 4); here it is #17 vs #55.
- **Concept (8 words):** The 55th pick outlasted the 17th pick.
- **Added value:** both draft slots, Knecht's rookie 37-and-9, the cancelled 2025 trade, the $4.2M the Lakers still owe, and LeBron now playing for Philadelphia.
- **Copy-check (Oct 19):** "lakers waive dalton knecht bronny": FRESH (no results).

## Script (Alex voice, 28.1 s; voice check: no issues)
> The Lakers just cut their seventeenth pick to keep their fifty-fifth. In 2024, they drafted Dalton Knecht seventeenth, and Bronny James fifty-fifth. As a rookie, Knecht hit nine threes and scored thirty-seven in one game. Bronny was the pick critics called a favor to LeBron. But on Monday, the Lakers had sixteen players for fifteen spots. They'd been trying to trade Knecht for over a year. They even traded him once, and the deal fell through. So they waived him, and they still owe him $4.2 million. And LeBron isn't even a Laker anymore. His son is. The fifty-fifth pick outlasted the seventeenth.

"Knecht" is voiced as "Nekt" (the "Connect 4" nickname rhymes with it); speech-to-text hears "neck".

## Claims and sources (read Oct 19, 2026)
| Claim | Source (exact words) | Check |
|---|---|---|
| Lakers waived Knecht on Monday, kept Bronny | Yahoo Sports / California Post, Oct 19 2026: "The Lakers' have decided to waive Knecht ... (h/t ESPN's Shams Charania)" https://sports.yahoo.com/articles/lakers-bronny-james-stance-clear-213524675.html ; EssentiallySports: "ESPN's Shams Charania reported the move Monday, and ClutchPoints' Brett Siegel confirmed it" | PASS |
| Knecht #17, Bronny #55 in 2024 | Yahoo/California Post: "The No. 17 pick in the 2024 draft"; "James was selected 55th overall in the 2024 NBA Draft" | PASS |
| As a rookie: 37 points, 9 threes in one game | Lakers official video title "Knecht Goes Off vs Jazz: 37 points and 9 threes" (Nov 2024); EssentiallySports: "Dalton Knecht scored 37 points against the Jazz as a rookie" | PASS |
| Sixteen players for fifteen spots | Yahoo/California Post: "trim their roster from 16 players signed to standard NBA deals to the maximum of 15 today" | PASS |
| Trying to trade Knecht for over a year | EssentiallySports: "The Lakers had been trying to move Knecht for more than a year" | PASS |
| Traded once; the deal fell through | Yahoo: "The Lakers had briefly dealt Knecht to the Charlotte Hornets as part of that transaction, but the deal fell through and he returned to Los Angeles" (the Mark Williams trade, Feb 2025) | PASS |
| They still owe him $4.2 million | EssentiallySports: "Waiving him means they absorb the $4.2 million he's owed this season" | PASS |
| LeBron isn't a Laker anymore | The Comeback, Oct 19 2026: "Philadelphia 76ers forward LeBron James"; footage of LeBron in a #23 PHILA jersey at Sixers media day (Sep 28 2026) | PASS |
| Critics called Bronny's pick a favor to LeBron | Opinion framing of the 2024 draft debate (attributed to "critics", not stated as fact) | framing |

Not used: a viral "Knecht post" about Bronny that reports say is a parody account's fake.

## Footage and choices
- All Lakers clips are official Lakers.com uploads (NBA.com team site, `Tools/nba_videos.py`); LeBron-as-a-Sixer is The Sporting News' post on X. Full log in `sources.csv`.
- Frame 1 is a split of the two (Media Day 2024): Knecht on top (#17 CUT), Bronny below (#55 KEPT). The last shot flips it: Bronny on top.
- "But on Monday" runs over a 2024 Lakers bench shot (no footage of Monday's decision exists); "sixteen players for fifteen spots" runs over Knecht and Bronny together at 2024 Summer League.

## Titles
1. The Lakers Cut Their #17 Pick For Bronny 😳
2. Why The Lakers Kept Bronny Over Knecht 😳
3. The 55th Pick Just Beat The 17th 😳

**Pinned comment:** Knecht went 17th, Bronny 55th. Two years later only Bronny's still a Laker. Right call?

## Rebuilding the split shots
S1 (Knecht top, Bronny bottom), from `src/md2024_0-120.mp4` (first 120 s of the Media Day 2024 video):
`ffmpeg -ss 23.5 -t 2.86 -i src/md2024_0-120.mp4 -filter_complex "[0:v]split[a][b];[a]crop=600:533:615:60,scale=1080:960[k];[b]crop=600:533:40:0,scale=1080:960[br];[k][br]vstack,drawbox=x=0:y=956:w=1080:h=8:color=black@1:t=fill,fps=30,setsar=1" -c:v libx264 -crf 14 -pix_fmt yuv420p -an clips/S1.mp4`
S13 (flipped): `-ss 41.5 -t 2.62`, crops `[a]crop=600:533:40:60` (Bronny, top) and `[b]crop=600:533:615:0` (Knecht, bottom). Overlays in `_ov/`.
