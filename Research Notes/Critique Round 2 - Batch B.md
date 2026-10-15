# Critique Round 2 — Batch B (#19–#25)

Date checked: 2026-10-04. Scope is the seven MetaSports folders from that day. Nothing in `script.txt`, shots, voice, or video was edited. Length is the last `words.json` word end. Word count is the `words.json` token count (spoken words, not the markup in `script.txt`).

Story standard used here: 90–120 words, 22–30s, tension in the first 8 words, a turn in the first 40% of that length, 2+ escalation beats, a clear payoff, end on the payoff (a question only after the payoff has landed), every sentence a new fact, and every claim sourced in `notes.md`.

## Verdicts

| # | Short | Words | Voice end | File length | Verdict |
|---|---|---:|---:|---:|---|
| 19 | How Tall Is Cooper Flagg Really | 86 | 21.895s | 22.03s | **REWRITE** |
| 20 | Would Bad Boys Defense Be Legal Now | 83 | 23.229s | 23.63s | **REWRITE** |
| 21 | How Close Is Jokic To Westbrooks Record | 87 | 23.514s | 23.93s | **REWRITE** |
| 22 | Why Can Only One Man Wear Six | 97 | 23.369s | 23.73s | **DO NOT POST** |
| 23 | Why Is Bronny Staying Without LeBron | 84 | 23.343s | not measured | **REWRITE** |
| 24 | Is Bronnys Roster Spot Really Safe | 108 | 27.546s | not measured | **REWRITE** |
| 25 | Did Bronny Actually Get Better | 97 | 23.083s | 23.43s | **PASS** |

#23, #24, and #25 are one Bronny story family. Do not post them as a same-day stack even where a script passes.

## #22 is a false cut

The current script says: "Only one NBA player can still wear number six" and "Now one man is left. Jaylin Williams." That is not true on the rosters opened today.

Both ESPN and NBA.com list two current number 6s:

- Jaylin Williams, Oklahoma City Thunder, **6**. ESPN roster cell reads `Jaylin Williams` immediately followed by `6` (https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder). NBA.com roster row: `Jaylin Williams | 6 | F` (https://www.nba.com/team/1610612760/thunder). His ESPN player page also says `#6` and `Status Active` (https://www.espn.com/nba/player/_/id/4432823/jaylin-williams).
- DeAndre Jordan, New Orleans Pelicans, **6**. ESPN roster cell reads `DeAndre Jordan` immediately followed by `6` (https://www.espn.com/nba/team/roster/_/name/no/new-orleans-pelicans). NBA.com roster row: `DeAndre Jordan | 6 | C | … | Exp 18 | … | Signed on 10/23/25` (https://www.nba.com/team/1610612740/pelicans).

No roster page printed an "updated" date. ESPN's footer is `Copyright: © 2026 ESPN Enterprises, LLC.` NBA.com team pages show 0–0 records. Fantasy-news stamps on those same NBA.com pages are 10/02/2026 (Thunder, Pelicans) and 10/03/2026 (Wizards).

LeBron is not a third number 6. ESPN's 76ers roster cell is `LeBron James` followed by `23` (https://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers).

A possible third did not survive both sites. An ESPN roster-API scan of all 30 teams returned only three `jersey=6` rows: Jordan, Jaylin Williams, and Deandre Ayton (Wizards, status active). The ESPN Wizards HTML roster also glues `6` to `Deandre Ayton` (https://www.espn.com/nba/team/roster/_/name/wsh/washington-wizards). NBA.com's Wizards roster does not: `Deandre Ayton | 8 | C | … | Traded from LAL on 07/07/26` (https://www.nba.com/team/1610612764/wizards). A third current number 6 is **not confirmed**. Two are. The current #22 cut still says one. **DO NOT POST** this cut. `notes.md` already warned that the Yahoo "last player" line is from October 2025 and that all 30 rosters were not scanned. The script did not use that warning.

The 2022 rule, from the NBA release (https://pr.nba.com/bill-russells-no-6-jersey-to-be-retired-throughout-nba/):

> "The National Basketball Association (NBA) and National Basketball Players Association (NBPA) announced today that they will honor the life and legacy of 11-time NBA champion and civil rights pioneer Bill Russell by permanently retiring his uniform number, 6, throughout the league."

> "Russell's jersey number, which he wore for his entire 13-season career from 1956-69, will not be issued again by any NBA team to any player. Players who currently wear No. 6 will be grandfathered."

Grandfathered means already wearing it, not "only one man left." Jordan wearing 6 in 2026-27 is allowed by that sentence. "When Jaylin retires, six disappears forever" is false while Jordan is also listed at 6.

## DeAndre Jordan's 2026 deal

Opened https://www.hoopsrumors.com/2026/07/pelicans-deandre-jordan-reportedly-received-two-year-deal.html (Rory Maher, July 12, 2026). Do not upgrade 19 to 20.

> "Jordan received two fully guaranteed years from New Orleans. He'll earn about $7.9MM over the next two seasons, Fischer adds, which means it's a minimum-salary contract."

> "The Pelicans will carry a $3.88MM cap hit for Jordan next season, followed by a $4.07MM charge for 2027/28."

> "He's entering his 19th season and 2027/28 will be year 20."

So: two years, fully guaranteed, about $7.9 million total, cap hits about $3.88 million then $4.07 million. The article's season number is **19th**, with 2027-28 as year 20. NBA.com's Pelicans row lists `Exp 18`, which matches "entering his 19th," not a 20th season now. #22's script does not mention the deal. The deal is why "one man left" is stale.

## LeBron and Bronny shooting

Opened https://www.basketball-reference.com/players/j/jamesle01.html and https://www.basketball-reference.com/players/j/jamesbr02.html.

LeBron, summary box: Career **FG3% 34.8**, Career G 1622. Regular-season totals career row, same column order as the age-41 / 2025-26 row (G, GS, MP, FG, FGA, FG%, 3P, 3PA, 3P%): **3P 2636, 3PA 7565, 3P% .348**. The per-game career row shows 3P 1.6, 3PA 4.7, 3P% .348. None of #19–#25 say LeBron's career percentage. It is not a script error. It also matches Bronny's career FG3% on the same site, which is a different number from Bronny's sophomore year.

Bronny summary box: 2025-26 G **42**, PTS **2.9**, FG% **40.9**, FG3% **38.6**. Career FG3% **34.8** (career, not the sophomore line).

Per-game table, regular season, read off the page (the converter dropped the season-link cell, so the first number is age):

- Age 20, LAL: G 27, GS 1, MP 6.7, FG% .313, 3P 0.3, 3PA 1.2, 3P% **.281**, TOV 0.5, PTS 2.3
- Age 21, LAL: G **42**, GS **1**, MP **8.9**, FG% **.409**, 3P 0.5, 3PA **1.4**, 3P% **.386**, TOV **0.6**, PTS **2.9**

Totals table agrees: 2024-25 3P 9, 3PA 32, 3P% .281, G 27, GS 1, TOV 13; 2025-26 3P 22, 3PA 57, 3P% .386, G 42, GS 1, TOV 25, PTS 122, MP 375.

What the Bronny scripts say against that page:

- #23 "two point nine points in forty-two games" matches PTS 2.9 and G 42.
- #24 "two point nine points in under nine minutes" matches PTS 2.9 and MP 8.9.
- #25 "twenty-eight percent to thirty-nine" is .281 to .386. Thirty-nine is ordinary rounding of 38.6. `notes.md` already prints `.386`. "Forty-one percent" is .409. "Thirty-one" is .313. "Nearly three points" is 2.9. "Started just one of those forty-two" is GS 1, G 42. "Under nine minutes" is 8.9. "Turnovers ticked up" is 0.5 to 0.6. Those lines match the page. The script never says the attempt count: 57 threes all season, 1.4 per game. That is a missed fact, not a false one.

The $2.3 million guarantee, the 16-for-15 roster, the October 21 date, the Knecht line, and the June 29 partial guarantee were **not** re-opened this pass. They stand only as written in each `notes.md`.

## #21 record chase

Opened https://www.basketball-reference.com/leaders/trp_dbl_career.html. Both the NBA/ABA table and the NBA table start:

> 1. Russell Westbrook 209
> 2. Nikola Jokić 198
> 3. Oscar Robertson 181

Jokić is in bold (active). Westbrook is not. "Eleven away" is 209 − 198. "Only those two ever passed Oscar Robertson" matches this list: Robertson is third. The page's own caveat is that a small number of pre-1980 triple-doubles may still be missing. It does not put anyone between Westbrook and Jokić, or between Jokić and Robertson.

Christmas line is real. Opened https://www.nba.com/news/a-classic-christmas-jokic-ant-duel-in-ot-knicks-come-back-spurs-drop-okc-again (NBA.com Staff, December 26, 2025 2:47 PM):

> **Nikola Jokić:** 56 points, 16 rebounds, 15 assists.

> Jokić finished with 56 points, 16 rebounds and 15 assists – marking the first 55/15/15 game in NBA history

Not re-opened this pass, so the notes.md figures stay: 42 triple-doubles in 2016-17, 34 triple-doubles in 65 games in 2025-26, "about 21 games," and "this month" for the opener. The pace math is labeled as pace math in `notes.md`. It is not a prediction the page can confirm.

## #20 narration quote

https://official.nba.com/2026-27-points-of-emphasis/ **loaded**. It is not blocked. It also does not contain the words "moves him off that path." There is no transcript on the page. The narration quote in the script cannot be checked for clipping from this page. What the page does say:

> See below for Part 2 of the 2026-27 Points of Emphasis video (narrated by SVP, Head of Referee Development and Training Monty McCutchen), which provides examples and guidance regarding Freedom of Movement – Perimeter & Post and Straight-Line Pathway Plays:

92.9 and 107.9 were not re-opened. They stay as cited in `notes.md`. "A hundred and eight" is a fair rounding of the notes' 107.9, if that figure holds.

## Audio (five READY files)

`ffmpeg` silencedetect `noise=-30dB:d=0.35`, then `ebur128`. Working directory `C:\Users\Admin\Documents\YouTube-Playbooks`. One silence at or above 0.35s was found in each file. Integrated loudness is tight across the five, about −14.3 to −14.6 LUFS. None of these loudness numbers is a reason to hold a file. #23 and #24 were not in the check.

| # | File duration | Longest silence | Where | Integrated |
|---|---:|---:|---|---:|
| 19 | 22.03s | 0.754s (18.024–18.778) | Inside the cut, before the closing question (that question starts at 20.708s). Not an end pad. | −14.4 LUFS (peak −0.5 dBFS) |
| 20 | 23.63s | 0.376s (18.792–19.168) | Inside the cut. Voice continues to 23.229s. | −14.5 LUFS (peak −0.5 dBFS) |
| 21 | 23.93s | 0.510s (23.337–23.847) | Tail. Last word ends 23.514s. | −14.6 LUFS (peak −0.6 dBFS) |
| 22 | 23.73s | 0.358s (23.233–23.591) | Tail. Last word ends 23.369s. | −14.3 LUFS (peak −0.7 dBFS) |
| 25 | 23.43s | 0.370s (22.943–23.313) | Tail. Last word ends 23.083s. | −14.4 LUFS (peak −0.5 dBFS) |

#19 is the only dead-air problem in the set: three-quarters of a second under −30 dB while the story is still going.

## Per short

### #19 REWRITE — How Tall Is Cooper Flagg Really

86 words (under 90). Voice ends at 21.895s (under 22). The file is 22.03s only because of picture after the last word. First 8 words, ending at 1.664s: "Cooper Flagg grew an inch in one sentence." That is tension. Turn: "Until" at 4.338s, inside the first 40% (8.758s). Escalation is the ladder: draft 6-8, site 6-9, media-day 6-10, trainer will not confirm, then maybe 6-11. The ladder lands, then the question. That shape is fine. "One inch" is the 6-9 to 6-10 step, which `notes.md` sources to Flagg ("I was like 6-9 last year"), not the two inches from the draft page. Those height pages were not re-opened this pass. Failures that force the rewrite: word count, voice length, and a 0.754s silence at 18.0s.

### #20 REWRITE — Would Bad Boys Defense Be Legal Now

83 words (under 90). Voice 23.229s is inside 22–30s. First 8 words, ending at 2.556s: "92.9. That's all the Bad Boy Pistons allowed." Turn: "But" at 8.861s, inside 9.292s. Beats: 92.9, then 108, then the two whistle rules, then the league line. The questions come after that line. Word count is the hard miss. The league sentence used as a quote is **not on the official page** (video only, no transcript), so this pass cannot prove it was not clipped. A 0.376s dip at 18.8s is just over the 0.35s detector and is not, by itself, a reason to hold the file.

### #21 REWRITE — How Close Is Jokic To Westbrooks Record

87 words, three under the floor. Voice 23.514s is in range. First 8 words, ending at 2.173s: "Can Jokic catch Westbrook's two hundred nine triple-doubles?" Turn: "But" at 8.931s, inside 9.406s. Beats: 198, eleven away, 42 in a season, only those two past Robertson, then 34 in 65, then the Christmas line, then 21 games. The question comes after the pace line. 209, 198, Robertson at 181, and the Christmas 56-16-15 line all checked out on the pages above. This is a length miss, not a fact miss. The tail silence (0.510s) starts as the last word is ending.

### #22 DO NOT POST — Why Can Only One Man Wear Six

97 words and 23.369s would have cleared the length gates. First 8 words end at 1.638s and the turn words ("so" 3.447s, "But" 5.866s, "Now" 7.429s) are inside the first 40% (9.348s). None of that matters. The hook, the middle ("Now one man is left"), and the payoff ("When Jaylin retires, six disappears forever") are one false claim. ESPN and NBA.com both list DeAndre Jordan at 6 as well as Jaylin Williams. Loudness (−14.3 LUFS) and the 0.358s tail are fine. Do not upload this cut.

### #23 REWRITE — Why Is Bronny Staying Without LeBron

84 words (under 90). Voice 23.343s is in range. First 8 spoken tokens, ending at 1.794s: "16 Lakers, 15 spots, and one of them." Turn: "But" at 8.102s, inside 9.337s. The sourced beats that were re-checked (2.9 points, 42 games) match Basketball-Reference. "Fifteen spots." lands, then the yes/no question. Word count fails. It is also the same roster-crunch story as #24, told again with a different closer. The 16-for-15 count, October 21, and the $2.3 million line were not re-opened.

### #24 REWRITE — Is Bronnys Roster Spot Really Safe

108 words and 27.546s are inside the gates. First 8 words end at 2.031s: "A guaranteed deal does not guarantee a roster." Turns "Until" (5.580s) and "But" (10.566s) are inside 11.018s. The counting stats that were re-checked match (2.9 points, 8.9 minutes). The last two sentences are not facts: "So the money buys him time. The preseason buys him the spot." The second one states an outcome. The script has just said Yahoo has his name up as a waiver option. `notes.md` sources that waiver line and does not source "the preseason buys him the spot." Do not upload this ending. The partial-guarantee dollars and the Knecht line were not re-opened.

### #25 PASS — Did Bronny Actually Get Better

97 words, voice 23.083s, file 23.43s. First 8 words end at 1.870s: "Bronny's three-point shooting jumped from twenty-eight percent to." Turns "So" (2.427s) and "But" (8.651s) are inside 9.233s. Escalation: field-goal jump and 2.9 points, then one start, under nine minutes, turnovers up, then the guaranteed deal. The question comes after those facts. The percentages, games, starts, minutes, and turnovers match the Basketball-Reference rows above, with .386 spoken as thirty-nine. "Supporters say yes" and "critics say look closer" are labels, not new facts. They are one clause each and they do not carry a false number. Loudness −14.4 LUFS. Longest silence 0.370s at the tail. The guarantee citation in `notes.md` was not re-opened. Post this one, not as a same-day set with #23 or #24.

## What this pass did not verify

- Cooper Flagg height pages, the 51-point game, and the trainer quote. Left as `notes.md` cites them.
- 92.9 (1989 playoffs) and 107.9 (2025-26 playoffs). Left as `notes.md` cites them.
- The Part 2 narration sentence. The official page loaded and does not contain it.
- Jokic's 34 triple-doubles, 65 games, the 42-in-a-season line, and the October opener date. Left as `notes.md` cites them. 209, 198, and 56-16-15 were opened.
- Lakers 16-for-15, October 21, Bronny's dollar figures, the Knecht expectation, and the Doncic quote. Left as `notes.md` cites them. Bronny's Basketball-Reference counting line was opened.
- All 30 NBA.com roster HTML pages. The all-30 scan was ESPN's roster API. NBA.com HTML was opened for the Thunder, the Pelicans, and the Wizards.
