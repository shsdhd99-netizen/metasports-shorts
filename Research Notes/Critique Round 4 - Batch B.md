# Critique Round 4 — Batch B

Reviewed only the `_v2` cuts in Shorts 17, 19, 20, 21, and 22. Older READY files were left in place. `DO NOT POST - old only-one cut.mp4` was not opened. Its timestamp is still 2026-10-04 10:15:56 and its size is still 26,929,099 bytes.

Edits were assembled with `python Tools\assemble.py --folder "<_v2>" --caption-style metasports` and `ALLOW_HOOK_TEXT` unset. A spelled-out-number warn is not a rewrite.

## 17 — Will The NBA Finally Punish Flopping

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | `words.json`: "Flopping" 0.00–0.34. `captions.ass` first line is `pos(540,1185)`, "FLOPPING HAS", 0.00–0.51. `after_0.45.jpg` is that caption in the lower middle, a defender on the floor, and no title across the top. |
| Turn | KEEP | "But" is 2.25–2.36, word 12 of 95. Spoken line: "But not every fall is a flop." |
| Chris Finch | KEEP | "Chris Finch" is 10.06–10.44. `nocap_10.30.jpg` is the Timberwolves coach at a mic. The hoodie reads TIMBERWOLVES. The source chyron reads "COACH IS FED UP WITH FLOPPING." |
| Mark Daigneault | KEEP | "Mark Daigneault" is 14.76–15.31. `nocap_14.90.jpg` is the Thunder coach. The shirt reads THUNDER. |
| Pascal Siakam | KEEP | "Pascal Siakam" is one token, 17.87–18.44. `strip_siakam.jpg` shows the white jumper in the air with 43 on the back, then the same player sitting with SIAKAM 43. `nocap_18.70.jpg` is that sit during "sitting" (18.50–18.70). |
| "is not a flop" on Siakam | EDIT | On the cut as reviewed, `nocap_19.60.jpg` is WALSH 27 during "not" (19.60–19.71), which is still the Siakam sentence (19.47–20.07). The tail of `siakam.mp4` dissolves, so the Walsh shot was replaced with `siakam_hold.mp4`, a 0.80s clip of source frame 4.30 (`src_sk_4.30.jpg`, white 43, referee standing). It plays 19.45–20.05. `after_19.60.jpg` is that 43, caption "IS NOT", referee standing with nothing at his mouth. |
| Deni Avdija | KEEP | "Deni Avdija" is 20.20–21.14. `after_20.57.jpg` is Portland 8, caption "A DENI AVDIJA". "head snap" is 21.19–21.51. `after_21.47.jpg` is the same red 8, head back, caption "HEAD SNAP". The clip `in` is 1.35. `src_av_1.35.jpg` is already Portland 8. |
| Ending | EDIT | Last line stays "A Deni Avdija head snap after minimal contact is not a flop." "flop." ends 23.04. On the old cut, `nocap_22.80.jpg` is the Rockets floor under that line. The loop now starts at 23.08. `after_22.70.jpg` is still the red jersey, caption "NOT A FLOP." Source used at the cut is 4.38s of the 4.40s clip. |
| Freeze | KEEP | `freezedetect` (`n=-50dB`, `d=0.4`) on the new `final.mp4`: freeze_start 19.5, freeze_duration 0.566667, freeze_end 20.066667. That is the 43 hold. No other freeze. |
| Loudness | KEEP | qa: "loudness -14.0 LUFS". |
| Facts | KEEP | Fadeaway World, Sep 30, 2026, quotes Finch, "so just stop rewarding the flopping," and Daigneault, "Flopping's been a rule" and "they might be flailing to try to bait those calls" (https://fadeawayworld.net/nba/minnesota-timberwolves/chris-finch-and-mark-daigneault-address-nbas-focus-to-punish-flopping-this-season). Joe Nelson, Oct 1, 2026, quotes Monty McCutchen on the league video: "Siakam simply sits down after releasing the shot. This sit-down action is not exaggerated, nor is it theatrical," and then "Portland's Deni Avdija snaps his head after minimal contact" (https://bringmethesports.com/chris-finch-calls-out-nbas-flopping-problem-hopefully-the-league-cleans-up-this-crap). |
| thud 4.95 | KEEP | `nocap_4.95.jpg`: a player in white is on the floor during "exaggerated" (4.95–5.44). Catalog gain -14. |
| whoosh 7.20 | KEEP | `shots.json` cuts at 7.2. `nocap_7.20.jpg` is a different scene, a player low by the Cavs bench. Catalog gain -11. |
| whoosh_long | EDIT | It was at 17.15, the cut to Siakam. It is now at 20.05, the cut into the Avdija payoff. Catalog gain -17. |
| ding | EDIT | It was at 20.05, on top of that cut. It is now at 22.52, on "not" (22.52–22.63), and `after_22.70.jpg` is still Avdija. Catalog gain -17. Four effects. No whistle. |

qa after the recut: PASS. Warn only, "shots under 0.6 s read as noise: [0.32]". That 0.32s is the loop from 23.08 to the end, after "flop." ends at 23.04. Length 23.4s, average shot 1.7s, `flop_kings.mp4` 21%, talking head 23%, b-roll 77%, loudness -14.0 LUFS.

READY file changed: yes. `READY TO POST - Will The NBA Finally Punish Flopping (v2).mp4` matches `_v2\final.mp4`, SHA256 `F0B91D4709FDF1A8AEEE28BFD65156B726645D369CDDA05D078A1709EEF6883A`. The older READY file was not copied.

## 19 — How Tall Is Cooper Flagg Really

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "Cooper" is 0.00–0.28. `cap_0.45.jpg` is Flagg's face, caption "COOPER FLAGG" in the lower middle, no title across the top. |
| Turn | KEEP | "Until" is word 20 of 103, at 4.69. Spoken line: "Until media day." |
| Cooper Flagg | KEEP | The only spoken player name is 0.00–0.53, on the face in `cap_0.45.jpg`. `nocap_4.80.jpg` is the same player in a Mavericks jersey at a mic during "I'm six-ten" (5.39–5.86). |
| Freeze | KEEP | `freezedetect` (`n=-50dB`, `d=0.4`) on `final.mp4` printed no freeze. |
| Ending | KEEP | Last words are "six-eleven." 24.13–24.72. `nocap_24.20.jpg` is Flagg in the same practice as the open, ball in his hands, shooting. qa: "loops to the first shot". |
| Loudness | KEEP | qa: "loudness -14.0 LUFS". |
| Facts | KEEP | Yahoo / The Big Lead, Stephen Douglas, Sep 25, 2026: the draft page "listed at 6-8", "The NBA's website currently has him listed at 6-9", Flagg "Not very accurate" / "I'm 6-10" / "With no shoes" / "I was like 6-9 last year" / "no shoes, maybe I'm 6-11", and the trainer "I can't confirm or deny he's grown in height" (https://sports.yahoo.com/articles/cooper-flagg-exact-height-nba-171742589.html). NBA.com player page lists HEIGHT 6'9" (https://www.nba.com/player/1642843/cooper-flagg). AP, Apr 4, 2026: "the first teenager to score 51 points in an NBA game" in "Dallas' 138-127 loss to the Orlando Magic" (https://apnews.com/article/mavericks-cooper-flagg-0c6888023bef5635e9a76047f7950240). |
| camera 4.66 | KEEP | `shots.json` cuts at 4.66. `nocap_4.80.jpg` has a mic in front of Flagg. Catalog gain -8. |
| dribble 14.32 | KEEP | `nocap_14.32.jpg`: the ball is in the air beside his hand. `strip_drib.jpg` continues that move: the ball leaves his hand, bounces away, and comes back. Catalog gain -12. |
| whoosh 17.55 | KEEP | `shots.json` cuts at 17.55, the same moment as "But" (17.58–17.70). Catalog gain -11. |
| ding 22.54 | KEEP | `shots.json` cuts at 22.54, the same moment as "Six-eight" (22.57–22.94). The ladder is still Flagg at `nocap_24.20.jpg`. Catalog gain -17. Four effects. |

qa: PASS. Warn only, "hook has no number or conflict/question word in the first 8 words: 'cooper flagg grew an inch in one sentence.'" Length 25.1s, average shot 1.7s, `06_media_b.mp4` 13%, talking head 26%, b-roll 74%, loudness -14.0 LUFS.

READY file changed: no.

## 20 — Would Bad Boys Defense Be Legal Now

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "92.9." is 0.00–0.42. `cap_0.45.jpg` is that number in green at caption height, players running, no title across the top. `captions.ass` uses `pos(540,1185)`. |
| Turn | KEEP | "But" is 11.59–11.70. Spoken line: "But the NBA just posted part two..." |
| Laimbeer | KEEP | "Laimbeer." is 6.49–6.87. `nocap_6.65.jpg` reads Pistons 40. The shot is 6.46–6.90. |
| Rodman | KEEP | "Rodman." is 6.93–7.31. `nocap_7.05.jpg` reads RODMAN 10. |
| Isiah Thomas | KEEP | "Isiah Thomas" is 7.36–8.12. `nocap_7.60.jpg` reads THOMAS 11. |
| Freeze | KEEP | `freezedetect` on the new `final.mp4`: 16.033333–16.533333 (0.5s) and 16.766667–17.166667 (0.4s). Both are inside the Perimeter & Post shot (15.25–17.92). |
| Ending | KEEP | Last line is "So was Detroit just committing fouls nobody called?" "So" is 23.97. "called?" ends 25.68. `nocap_24.30.jpg` is the same Palace floor as the open. The script has no "moves him off that path." |
| Loudness | KEEP | qa: "loudness -14.0 LUFS". |
| Facts | KEEP | Basketball-Reference 1989 playoffs, opponent table: Detroit 17 games, 92.9; league average 104.9 (https://www.basketball-reference.com/playoffs/NBA_1989.html). The series lines on that page are 3-0, 4-0, 4-2, and 4-0, which is 17 games. 2025-26 playoffs row: 85 games, 107.9 PTS (https://www.basketball-reference.com/leagues/NBA_stats_per_game.html). Official page, Part 2: "Freedom of Movement – Perimeter & Post and Straight-Line Pathway Plays," narrated by Monty McCutchen. A search of that page did not find "moves him off that path" (https://official.nba.com/2026-27-points-of-emphasis/). Blazer's Edge, Dave Deckard, Sep 29, 2026: "players cannot hold, grab, or bump an opponent in such a way that stops them from going where they were trying to go" and "a defender using his body to bump a dribbler off of a straight-line drive" (https://www.blazersedge.com/nba-news-rumors/116607/nba-highlights-2026-27-points-of-emphasis-for-referees). |
| whoosh 11.59 | KEEP | `shots.json` cuts from the Pistons scrum to `11_post.mp4` at 11.56, on "But" (11.59). Catalog gain -11. |
| pop 15.28 | KEEP | `nocap_15.28.jpg`: the "Perimeter & Post" banner is on screen and referee 19 is standing, back to the camera, no whistle at his mouth. Catalog gain -16. No whistle was added. |
| punch | EDIT | It was at 17.95. `nocap_18.05.jpg` shows the ball handler and a white arm with no body hit. `hit_18.80.jpg` is an arm reach. `hit_19.15.jpg` is a hand on an arm. `hit_19.50.jpg` is crowded and the contact is not a body hit. The punch was removed. |
| thud | EDIT | It was at 19.98. `nocap_19.98.jpg` has both players in the air. It is now at 20.40. `nocap_20.40.jpg` is the black-jersey player leaning backward and starting to fall under the rim. `strip_fall.jpg` continues that fall through the hoop. Catalog gain -14. Pop at 15.28 is 5.12s earlier. Three effects. |

qa after the sound edit: PASS. Warn only, "shots under 0.6 s read as noise: [0.44, 0.43]". Those are the Laimbeer and Rodman flashes, and the numbers are readable. Length 26.0s, average shot 1.5s, `11_post.mp4` 18%, talking head 0%, b-roll 100%, loudness -14.0 LUFS.

READY file changed: yes. `READY TO POST - Would Bad Boys Defense Be Legal Now (v2).mp4` matches `_v2\final.mp4`, SHA256 `248B887344C6F4074A2EAB11C11A393BC6D34DEB6F8D2088F7F8488D1F2331FC`. The older READY file was not copied.

## 21 — How Close Is Jokic To Westbrooks Record

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "Jokic" is 0.19–0.43. `cap_0.45.jpg` is NUGGETS 15, ball held in both hands, caption "CAN JOKIC CATCH" in the lower middle, no title across the top. |
| Turn | KEEP | "But" is word 26 of 102, in "Eleven away. But he had thirty-four triple-doubles last season." qa printed no turn warning. |
| Jokic, open | KEEP | Same frame as the hook. The ball is in his hands, so no dribble was added. |
| Russell Westbrook, open | KEEP | "Westbrook's" is 0.89–1.20. `strip_wb_open.jpg` goes from NUGGETS 15 to a short blur at the rim, then OKLAHOMA CITY 0 for the drive. `nocap_1.70.jpg` is still OKC 0 during "nine" (1.66–1.80). |
| Westbrook, retired | KEEP | "Westbrook just retired" is 2.95–3.78. `strip_wb_ret.jpg` reaches a Wizards jersey with 4 on the back, then cuts to JOKIĆ 15. |
| Nikola Jokic | KEEP | "Jokic" is 4.21–4.44. `nocap_4.20.jpg` reads JOKIĆ 15. The later "Jokic" is 17.39–17.64. `nocap_17.60.jpg` is the white Nuggets uniform with the mountain logo, same uniform as the 15 at 0.45s. |
| Oscar Robertson | KEEP | "Oscar" is 15.49–15.67. `nocap_15.60.jpg` is the older man at a mic. `shots.json` cuts there at 15.46. |
| Freeze | KEEP | `freezedetect` on the new `final.mp4` printed no freeze. |
| Ending | KEEP | Last line is "At that pace, eleven more takes about twenty-one games." "At" is 22.34. "games." ends 24.48. qa: "loops to the first shot". No season-opening date is in the script. |
| Loudness | KEEP | qa: "loudness -14.0 LUFS". |
| Facts | KEEP | Career triple-doubles: Russell Westbrook 209, Nikola Jokić 198, Oscar Robertson 181 (https://www.basketball-reference.com/leaders/trp_dbl_career.html). Eleven away is 209 minus 198. Season list: Westbrook 42 in 2016-17, Jokić 34 in 2025-26 (https://www.basketball-reference.com/leaders/trp_dbl_season.html). Jokić 2025-26 row: 65 games, 65 starts (https://www.basketball-reference.com/players/j/jokicni01.html). Eleven more at 34 in 65 games is 11 / (34/65) = 21.0 games. Denver Post, Dec 26, 2025: "Jokic amassed 56 points, 16 rebounds and 15 assists" and "the first 55-15-15 stat line in NBA history" (https://www.denverpost.com/2025/12/26/nikola-jokic-nuggets-timberwolves-christmas-highlights-anthony-edwards-shot/). |
| camera 8.30 | KEEP | `nocap_8.40.jpg`: DENVER 15, and a camera on a tripod to his right. Catalog gain -8. |
| swish | EDIT | It was at 12.20. `nocap_12.20.jpg` is WESTBROOK 0 hanging on the rim with the ball below him. `nocap_12.00.jpg` and `nocap_12.45.jpg` are the same: the ball is beside him, then out of the net. `strip_dunk.jpg` never puts the ball through the net. The swish was removed. |
| whoosh 15.49 | KEEP | The Oscar cut above. Catalog gain -11. |
| ding 22.34 | KEEP | "At" is 22.34–22.43, the pace line. Catalog gain -17. Three effects. `nocap_10.40.jpg` has the ball out of frame, so the dribble stayed off. |

qa after the sound edit: PASS. Warn only, "hook has no number or conflict/question word in the first 8 words: 'can jokic catch russell westbrook's two hundred nine'". Length 24.9s, average shot 1.7s, `01_jhook.mp4` 13%, talking head 0%, b-roll 100%, loudness -14.0 LUFS.

READY file changed: yes. `READY TO POST - How Close Is Jokic To Westbrooks Record (v2).mp4` matches `_v2\final.mp4`, SHA256 `A5F112BB1B3A66E75D60F6A207AFC2E2246E6B75A8D5489E3B0F194E4A5E93F7`. The older READY file was not copied.

## 22 — Why Can Only One Man Wear Six

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "Two" is 0.00–0.20. `cap_0.45.jpg` is WILLIAMS 6 on the floor, caption "TWO NBA" in the lower middle. Thunder 7 and 3 are also in the frame. The scorebug is inside the footage. No title across the top. |
| Turn | KEEP | "Until" is at 8.44. The line "Nobody new can ever get it. Until this summer." lands before "DeAndre" at 9.25. |
| Bill Russell | KEEP | "Bill Russell" is 1.81–2.27. `nocap_1.90.jpg` is the Celtics walk-up with BOSTON across the chest. The second "Bill Russell" is inside Jaylin's quote at 19.91–20.37, and that shot (`q_jay.mp4`) runs to 20.46. |
| DeAndre Jordan | KEEP | "DeAndre Jordan" is 9.25–10.05. `nocap_9.40.jpg` reads JORDAN 6, one foot up. "million" through "nineteen." is 11.78–14.64. `shots.json` plays `dj_walk.mp4` from 11.75 to 14.71. `nocap_13.80.jpg` is still JORDAN 6, feet and arm changed from the 9.40 frame, during "That" (13.68–13.83). |
| Jaylin Williams | KEEP | "Jaylin Williams" is 14.74–15.40. His shot starts at 14.71. `nocap_15.30.jpg` is his face, OKC backdrop, mic on the table. `nocap_22.70.jpg` and `nocap_24.20.jpg` both read WILLIAMS 6. |
| Freeze | KEEP | `freezedetect` on `final.mp4`: 10.733333–11.133333 (0.4s) and 11.2–11.766667 (0.566667s). Those sit on `dj_finish.mp4` (10.24–11.75), under "seven point nine" (11.13–11.75). `dj_walk.mp4` is moving by `nocap_13.80.jpg`. |
| Ending | KEEP | Last line is "Two names. When both of them retire, six is gone." "gone." ends 25.05. `nocap_24.20.jpg` is WILLIAMS 6 standing. qa: "loops to the first shot". The script says two players can still wear six. |
| Loudness | KEEP | qa: "loudness -14.0 LUFS". |
| Facts | KEEP | ESPN: Jaylin Williams, Oklahoma City Thunder, #6, Forward, Active (https://www.espn.com/nba/player/_/id/4432823/jaylin-williams). NBC Sports lists "NOP Center #6" and "will return to New Orleans for his 19th NBA season" on "a two-year deal" (https://www.nbcsports.com/nba/deandre-jordan/00000188-9cf0-da6b-abd8-fcfdc2a30183/news). Hoops Rumors, July 12, 2026: "two fully guaranteed years" and "about $7.9MM over the next two seasons", and "He's entering his 19th season" (https://www.hoopsrumors.com/2026/07/pelicans-deandre-jordan-reportedly-received-two-year-deal.html). |
| whoosh 3.44 | KEEP | `shots.json` cuts at 3.44, and "in 2022" starts at 3.47. Catalog gain -11. |
| boom_cinematic 9.22 | KEEP | That is the cut to `dj_6.mp4`. `nocap_9.40.jpg` is the JORDAN 6 reveal. Catalog gain -10. |
| camera 14.90 | KEEP | `nocap_15.30.jpg` has the mic on the table during "Williams" (15.09–15.40). Catalog gain -8. |
| ding 22.49 | KEEP | "Two" of "Two names" is 22.49–22.66. `nocap_22.70.jpg` is WILLIAMS 6. Catalog gain -17. Four effects. |

qa: PASS. Warn only, "hook has no number or conflict/question word in the first 8 words: 'two nba players can still wear number six.'" Length 25.4s, average shot 2.0s, `j_hook.mp4` 18%, talking head 31%, b-roll 69%, loudness -14.0 LUFS.

READY file changed: no. `READY TO POST - Two Men Can Still Wear Six.mp4` is still timestamped 2026-10-04 11:12:07. `DO NOT POST - old only-one cut.mp4` was not opened and was not overwritten.
