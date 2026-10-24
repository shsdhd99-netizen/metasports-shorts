# Critique Round 5

Reviewed the cuts that produced the v2 READY files for Shorts 17, 29, and 16. Frames are in each folder's `_crit5`. `qa_short.py` was run on those folders. `ffmpeg freezedetect=n=-50dB:d=0.4` was run on each `final_nocap.mp4`. No v2 was overwritten. No v3 was made. Taste was not a reason to recut.

The user is posting 29 first and 17 second. Short 16 was the swap only if 17 failed. It did not.

## 17 — Will The NBA Finally Punish Flopping

`qa_short.py` on `_v2`: PASS. Exit 0. Warn only: shots under 0.6 s `[0.32]`. Length 23.4s, average shot 1.7s, `flop_kings.mp4` 21%, 8 source clips, talking head 23%, b-roll 77%, cards 0%, loudness -14.0 LUFS. The 0.32s is the loop after "flop." ends at 23.040s.

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "Flopping" 0.000–0.341. `17_final_00045.jpg` is a player in white on the floor, caption "FLOPPING HAS" in the lower third, no title across the top. qa: opens on "Flopping"; 3 shots in the first 3s. |
| Turn | KEEP | "But" is word 11 of 95, at 2.251s. Spoken: "But not every fall is a flop." |
| Chris Finch | KEEP | "Chris Finch" 10.063–10.441. `17_nocap_01015.jpg` is the Timberwolves coach at a mic. The hoodie reads TIMBERWOLVES. The source line reads "COACH IS FED UP WITH FLOPPING." |
| Mark Daigneault | KEEP | "Mark Daigneault" 14.764–15.313. `17_nocap_01490.jpg` is that coach. The shirt reads THUNDER. |
| Pascal Siakam | KEEP | The name is one token, 17.866–18.444, on `siakam.mp4` from 17.15s. `17_nocap_01720.jpg` reads 43, white headband, ball in hand. `17_nocap_01860.jpg` reads SIAKAM 43 on the floor during "sitting" (18.500–18.699). |
| "is not a flop" | KEEP | "not" is 19.597–19.711, still the Siakam sentence (19.474–20.071). `17_nocap_01965.jpg` is white 43 getting up. The referee is standing with nothing at his mouth. Walsh 27 is not in the frame. |
| Deni Avdija | KEEP | "Deni Avdija" 20.203–21.139. `17_nocap_02040.jpg` is Portland 8. "head snap" is 21.187–21.508. `17_nocap_02140.jpg` is the same red 8, head back. |
| Frozen shot | KEEP | `freezedetect` on `final_nocap.mp4`: freeze_start 19.466667, freeze_duration 0.6, freeze_end 20.066667. That is `siakam_hold.mp4`, the 43 hold through "is not a flop." No other freeze. A still of the right player, under a second, is the fix that removed Walsh. |
| Ending | KEEP | Last line: "A Deni Avdija head snap after minimal contact is not a flop." "flop." ends 23.040s. `17_final_02260.jpg` is still the red jersey, caption "NOT A FLOP." The loop starts at 23.08s. `17_nocap_02315.jpg` is the opening floor. No question after the payoff. qa: loops to the first shot. |
| Loudness | KEEP | qa: loudness -14.0 LUFS. |
| Facts | KEEP | Fadeaway World, Sep 30, 2026, https://fadeawayworld.net/nba/minnesota-timberwolves/chris-finch-and-mark-daigneault-address-nbas-focus-to-punish-flopping-this-season : Daigneault, "Flopping's been a rule," and "they might be flailing to try to bait those calls." Joe Nelson, Oct 1, 2026, https://bringmethesports.com/chris-finch-calls-out-nbas-flopping-problem-hopefully-the-league-cleans-up-this-crap : "Siakam simply sits down after releasing the shot" and "Portland's Deni Avdija snaps his head after minimal contact." |
| thud 4.95 | KEEP | Catalog gain -14. `17_nocap_00495.jpg`: a player in white is on the floor during "exaggerated" (4.947–5.439). |
| whoosh 7.20 | KEEP | Catalog gain -11. Cut at 7.2s. `17_nocap_00720.jpg` is a different scene, a player low by the Cavs bench, on "defender" (7.216). Not a swish. |
| whoosh_long 20.05 | KEEP | Catalog gain -17. Cut into the Avdija payoff. `17_nocap_02040.jpg` is Portland 8. |
| ding 22.52 | KEEP | Catalog gain -17. On "not" (22.520–22.633). `17_final_02260.jpg` is still Avdija. Four effects, all after 1.0s, no file twice, none within 1.5s. No whistle. |

READY file changed: no. SHA256 `F0B91D4709FDF1A8AEEE28BFD65156B726645D369CDDA05D078A1709EEF6883A` on `READY TO POST - Will The NBA Finally Punish Flopping (v2).mp4`. It matches `_v2\final.mp4`.

## 29 — The NBA Final That Does Not Count

`qa_short.py`: PASS. Exit 0. No warn lines. Length 22.6s, average shot 1.7s, `hinkle_render.mp4` 22%, 8 source clips, b-roll 100%, loudness -14.1 LUFS.

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | First token "only" 0.000–0.235. `29_final_00045.jpg` is the packed Hinkle floor, players and a ball in the air, caption "ONLY NINE" in the lower third. No burned title across the top. qa: opens on "only"; 3 shots in the first 3s. |
| Turn | KEEP | "But" is word 11 of 93, at 2.736s. Spoken: "But it is not a high school gym." |
| Hinkle / 1928 | KEEP | "Hinkle" 4.137–4.426. "twenty-eight." ends 6.200s, and the board shot runs to 6.2s. `29_nocap_00440.jpg` and `29_nocap_00580.jpg` read "HINKLE FIELDHOUSE" and "HOME OF THE BULLDOGS SINCE 1928." |
| 1954 | KEEP | "nineteen fifty-four" 6.927–7.675, on `hinkle_night.mp4` from 6.2s. `29_nocap_00680.jpg` and `29_nocap_00820.jpg` are the real building at night. Not a fake 1954 game. Not Hoosiers. |
| December 11 / Butler floor | KEEP | "December eleventh" 9.888–10.593, on `hinkle_render.mp4` from 8.88s. `29_nocap_01040.jpg` is the Butler floor with the Emirates NBA Cup mark. `29_nocap_00170.jpg` is that floor after the skyline: the shot `in` is 2.30s. |
| Las Vegas | KEEP | "Las Vegas" 12.165–12.678, on `vegas_court.mp4` from 10.87s. `29_nocap_01140.jpg` and `29_nocap_01240.jpg` read LAS VEGAS and CHAMPIONSHIP, Spurs and Knicks. Not under the 9,100 line. |
| Semis at home | KEEP | "higher seed" through "home." is 13.181–14.623, on `cup_home.mp4`. `29_nocap_01340.jpg` and `29_nocap_01440.jpg` are a moving Emirates NBA Cup game. No LAS VEGAS text and no championship bug. |
| Only the championship | KEEP | "championship" 14.987–15.521, on `cup_final.mp4`. `29_nocap_01510.jpg` reads CHAMPIONSHIP, Emirates NBA CUP. Not a June Finals broadcast. |
| Nine thousand one hundred | KEEP | The callback starts at 17.735s on `hinkle_wide.mp4`. `29_nocap_01810.jpg` is the packed Hinkle bowl, not the Vegas crowd. |
| Every other Cup game | KEEP | "Every other" 19.776. `29_nocap_02030.jpg` reads WEST GROUP C, Warriors and Spurs, ball in the air. Group play is the picture that counts. |
| This one does not | KEEP | "This one" 21.380. `29_final_02210.jpg` is the Hinkle wide, caption "DOES NOT." Not the June 2026 Finals. Not a December 16, 2025 date card. |
| Frozen shot | KEEP | `freezedetect`: 0.366667 for 0.466667s, and 18.066667 for 0.433333s. Both are `hinkle_wide.mp4`. The file is 2.333s. Mean absolute difference between samples from 0.0s to 2.2s is 0.42 to 0.73 on a 0–255 scale, so the whole clip is a near-hold. A later in-point is the same picture. Replacing the open with the empty floor render would put no crowd under the seat line. The frame is the right gym, with players and a ball. Not a false fact. |
| Ending | KEEP | Last words: "This one does not." "not." ends 22.320s. No question after it. The last shot is `hinkle_wide.mp4`, the first clip. qa: loops. |
| Loudness | KEEP | qa: loudness -14.1 LUFS. |
| Facts | KEEP | NBA.com Cup 101, updated Aug. 12, 2026, https://www.nba.com/news/nba-cup-101 : "culminate with the Championship on Friday, Dec. 11 at Hinkle Fieldhouse in Indianapolis." "The Quarterfinals ... and Semifinals ... will be played in NBA team markets, with each game at the home arena of the higher-seeded team." "The Championship will not be counted as a regular-season game, meaning that the game will not count toward a team's regular-season record, and a player's or team's performance will not count toward regular-season statistics." Quarterfinals and semifinals "will count as regular-season games for all purposes." NBA.com, Steve Aschburner, updated June 30, 2026, https://www.nba.com/news/hinkle-fieldhouse-will-host-emirates-nba-cup-championship : "the Fieldhouse has 9,100 seats" and "Butler's Hinkle Fieldhouse has served as the team's home since 1928." Same page: the tape-measure scene was fiction, and the building hosted the 1954 Milan game. The script does not say the movie scene was filmed as fact, and the cut does not use the movie. |
| whoosh 1.58 | KEEP | Catalog gain -11. Cut onto the Butler floor. `29_nocap_00170.jpg` is that floor. |
| ding 17.75 | KEEP | Catalog gain -17. On "Nine" (17.735). `29_nocap_01810.jpg` is the full gym. |
| boom_cinematic 21.40 | KEEP | Catalog gain -10. Once, on "This one" (21.380). The picture is the gym, not a made basket. Three effects. A fourth would not be on screen. No file twice. None before 1.0s. None within 1.5s. |

READY file changed: no. SHA256 `CF87A5A3831891A72DCB1B075C077876A08122201F7CD8C683B816B1FBF1ABFF` on `READY TO POST - The NBA Final That Does Not Count (v2).mp4`. It matches `final.mp4`.

## 16 — Giannis Faces The Bucks In Vice City

`qa_short.py` on `_v2`: PASS. Exit 0. Warn only: speech pace 238 wpm. Length 23.0s, average shot 1.5s, `q_plane.mp4` 27%, 11 source clips, talking head 27%, b-roll 62%, cards 11%, loudness -14.0 LUFS. Not today's file.

| Item | Verdict | Evidence |
|---|---|---|
| Hook | KEEP | "Giannis" 0.000–0.405. `16_final_00045.jpg` is Giannis in the white HEAT jersey, caption "GIANNIS IS" in the lower third. qa: opens on "Giannis"; 3 shots in the first 3s. |
| Turn | KEEP | "But" is word 11 of 90, at 2.200s. Spoken: "But the Heat play that night as Vice City..." |
| Giannis | KEEP | The name is 0.000–0.405 on the HEAT jersey in `16_final_00045.jpg`. |
| "he watched" | KEEP | "he" 12.471–12.540, "watched" 12.589–12.797, on `g_heat.mp4` from 12.05s. `16_nocap_01230.jpg` is Giannis in HEAT. Giddey is not the readable jersey. |
| Bucks fans | KEEP | "fans" 13.556–13.783. `16_nocap_01370.jpg` has the crowd. TURNER 3 is in front and is not named. The spoken word is "fans." |
| Quote | KEEP | "Milwaukee will always be my home" starts 14.576. `16_nocap_01490.jpg` is Giannis in the denim jacket. No mic, so there is no camera effect. |
| Frozen shot | KEEP | No `freeze_start` on `final_nocap.mp4`. |
| Ending | KEEP | Last line: "Now he plays them in a Vice City jersey." "jersey." ends 22.736s. `16_nocap_02090.jpg` reads ANTETOKOUNMPO 7. `16_final_02250.jpg` is the HEAT jersey, caption "CITY JERSEY." `_v2\notes.md`: the Vice City uniform is announced and not yet the jersey in this footage, so the picture is the Miami uniform. qa: loops to the first shot. |
| Loudness | KEEP | qa: loudness -14.0 LUFS. |
| Facts | KEEP | Sun-Sentinel, Oct 2, 2026, https://www.sun-sentinel.com/2026/10/02/grand-theft-heat-game-vs-bucks-to-turn-into-a-night-in-vice-city/ : "marking Giannis Antetokounmpo's first game against his former team since he was dealt to the Heat." Heat post, https://x.com/MiamiHEAT/status/2106007519545974792 : "November 18... never-before-seen court... all-new uniform." `16_nocap_00420.jpg` reads "WELCOME TO Vice city." `16_nocap_00840.jpg` reads "NOVEMBER 18, 2026 7PM EST" and "MILWAUKEE VS VICE CITY." The script has no neon. |
| whoosh 4.04 | KEEP | Catalog gain -11. Cut to the Vice City sign on "court" (4.065). `16_nocap_00420.jpg`. |
| click 8.09 | KEEP | Catalog gain -10. The November 18 poster appears on "November eighteenth" (8.120). `16_nocap_00840.jpg`. |
| whoosh_long 20.76 | KEEP | Catalog gain -17. Cut to ANTETOKOUNMPO 7 on "Now" (20.786). No mic, so the old camera effect stays out. Three effects: 4.04 / 8.09 / 20.76. |

READY file changed: no. SHA256 `494EAF4E3B2CB2ABBEE0CF57BACD5DD37B300AEA3D20F8B854E5AF83F0FFEFBE` on `READY TO POST - Giannis Faces The Bucks In Vice City (v2).mp4`. It matches `_v2\final.mp4`.

## READY files

| Short | READY changed |
|---|---|
| 17 | no |
| 29 | no |
| 16 | no |
