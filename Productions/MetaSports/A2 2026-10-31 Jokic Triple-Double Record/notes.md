# A2 Jokic breaks Westbrook's triple-double record (pre-build, Account 2, Oct 31 2026)

**Status: voice-ready. NOT voiced (the record night has not happened).** The main account adds the night's numbers in the SLOT, voices it, adds the night's clip and posts the next morning (news: it must go up the morning after the game).

- **Lane:** news / star paradox hybrid: a household-name star, one idea a casual fan gets in second 1 (his first game was two points).
- **Concept (8 words):** Two points in his debut; now the record.
- **Added value (facts the clip can't show):** the 200th triple-double came on the 11th anniversary of his debut (Oct 28, 2015 and Oct 28, 2026); the games-to-200 comparison (814 vs 1,175); 16 of them against New Orleans, six more than any other team.
- **Copy check:** `copy_check.py "Jokic Westbrook triple-double record"` finds only reaction/interview videos (Chaz NBA 167K "tells Westbrook he'll pass Russ", Fresh Stats 163K, Hoops Reaction 112K); nobody tells the debut-to-record arc. **Our own #21 "Jokic Could Break Westbrook's Record By Christmas" is already posted (about 2.5K views).** This is a different angle (debut callback, the record night itself).
- **Hook:** line 1 = "Nikola Jokić scored two points in his NBA debut." (9 words, a statement, the strange thing).
- **Pronunciation:** `{Jokić|Yoh-kitch}` in the script; use whichever spelling `Tools/pronunciation.json` already maps (older scripts used `Yoki-ch`) and check the take.

## State of the numbers (verified Oct 31 2026)
- Jokić has **200** regular-season triple-doubles. He did NOT add one on Oct 30 at Phoenix (ESPN box score, event 401909286: 18 pts, 7 reb, 10 ast). No other Nuggets game since Oct 28 (ESPN scoreboard Oct 29-31). He needs **9 to tie, 10 to break**.
- Westbrook's record is **209** (retired; ESPN).
- The Nuggets' next game was not checked: main account, look at the schedule before slotting.

## Claims table
| Script line | Source | Exact words / data |
|---|---|---|
| Jokić scored two points in his NBA debut | Basketball-Reference game log 2015-16, https://www.basketball-reference.com/players/j/jokicni01/gamelog/2016/ (row 1) | Game 1: date 2015-10-28, DEN @ HOU, "W, 105-85", MP 03:55, FG 1-1, TOV 1, PTS 2. Player page: "NBA Debut: October 28, 2015". StatMuse agrees (2 points in 4 minutes) |
| October twenty-eighth, twenty fifteen | same | "NBA Debut: October 28, 2015" |
| Eleven years later, to the day, his two hundredth triple-double | ESPN https://www.espn.com/nba/story/_/id/50314211/nuggets-nikola-jokic-notches-200th-career-triple-double-win-vs-pelicans ; ESPN game 401909889 (Nuggets at Pelicans, Wed Oct 28 2026, 104-91) ; NBA on X https://x.com/NBA/status/2115628934293524805 (posted Oct 29 02:16 UTC = evening of Oct 28 ET) | "had 21 points, 13 rebounds and 10 assists for his 200th career triple-double in the regular season" ; ESPN box: 21 pts, 13 reb, 10 ast, 34 min ; NBA: "becoming the second player to reach 200 triple-doubles" |
| Only Russell Westbrook has more, with two hundred nine | same ESPN article | headline "now 9 behind Westbrook's NBA record"; "Jokic needs 10 more regular season triple-doubles to supplant Russell Westbrook, who retired after last season, as the NBA leader" (200 + 9 = 209); "They are the only two players in NBA history to eclipse 200." Stat Defender on X (tier [S]) lists "Russell Westbrook - 209" |
| Jokić needed 814 games to reach 200; Westbrook 1,175 | same ESPN article | "Westbrook reached 200 triple-doubles in his 1,175th game; Jokic did it in his 814th." |
| Sixteen of those came against New Orleans, six more than any other team | same ESPN article | "Sixteen of Jokic's triple-doubles have come against the Pelicans, six more than any other opponent." (Pelicans = New Orleans) |
| SLOT: date, team, points, rebounds, assists, number | **TO FILL on record night** from the ESPN box score, play-by-play (`summary?event=<id>`) and recap | Copy the exact line from ESPN; the count (210 breaks it, 209 ties it) from the ESPN recap |
| From two points in his debut to the all-time record | follows from the rows above | True only if the slot's number is 210. See variants below |

Caveat: the games-to-200 numbers are ESPN's (Basketball-Reference may count games differently). Keep ESPN's wording.

## Slot variants (the payoff must stay true)
- **210 (breaks it):** "On {DATE}, against {TEAM}, he had {PTS} points, {REB} rebounds and {AST} assists. That was number two hundred ten, the all-time record." Payoff: "From two points in his debut to the all-time record."
- **209 (ties it):** "... That was number two hundred nine, tying Westbrook." Payoff: "From two points in his debut to tied for the record." (The break is the news; a tie Short is the owner's call.)
- Word budget: the slot is about 20 words (about 5 s). Total script about 95 words, about 24 s.

## Footage (all public league/broadcaster sources, in src/)
| File | Source | Used for |
|---|---|---|
| `espn_jokic_andone_gsw.mp4` (20.7 s, 1080p) | ESPN public clip API, event 401909876 (Warriors at Nuggets, Oct 26 2026), video 50294134 "Nikola Jokic gets the and-1 to fall" | J01 frame 1 (face, 7.7-9.8 s; dissolve at 9.86) |
| `x_nba_35_15_10_gsw.mp4` (219 s, 1080x1080) | NBA on X https://x.com/NBA/status/2114215144867659914 (35 pts, 15 reb, 10 ast, 23-point comeback; via `Tools/x_clip.py`) | J02, J05, J07, J08 (Jokic vs Pelicans) |
| `espn_pels_highlights.mp4` (73.5 s) | ESPN API, event 401909889, video 50313476 "Denver Nuggets vs. New Orleans Pelicans: Game Highlights" | J03 (final seconds, 104-91 scorebug, Jokic #15) |
| `espn_jokic_slam_phx.mp4` (25.6 s) | ESPN API, event 401909286 (Nuggets at Suns, Oct 30), video 50333123 "Nikola Jokic rocks the rim with slam" | J04, J06 |
| `x_nba_xmas_56_16_15.mp4` | NBA on X https://x.com/NBA/status/2004448562327765394 | NOT used (wide shots, no Jokic close-ups); spare |

- **Illustrative, flagged:** no public 2015 debut footage exists (archive.org has only AP radio audio and the 2015-16 media guide; the "Summer League debut" video on X is a fan account, ThrowbackHoops, and is not the NBA debut anyway). The two-points line is carried by a "2 PTS / NBA debut, Oct 28, 2015" overlay on a current Jokić face. No Westbrook footage from a league source was found (only fan accounts such as Ballislife, not allowed as a base), so his name is carried by overlays.
- Rights: league/broadcaster footage, shots of 2-3 s. Narrated version only (no live call planned).

## What's missing on record night
1. **The night itself:** which game, the final line and the number (210 or 209). It can't be pre-built. Fill the SLOT in `script.txt` (remove the `[[SLOT ...]]` brackets) and the `{NUM}` overlay on RN1.
2. **The night's clip**, saved as `src/record_night.mp4` (ESPN clip API for that game's event id, `videos[].links.source.HD.href`, or NBA on X via `Tools/x_clip.py`): RN1 build-up, RN2 the play that completes it, RN3 = replay of RN2 at 0.5x with zoom 1.3 (set its `at` equal to RN2's).
3. **Voice and build:** check credits (script about 95 words, about 600 characters); `voice_take.py`, `tighten_voice.py --thresh 0.25 --keep 0.12`, `fill_len.py`, copy `cuts_plan.json` to `cuts.json` (drop the `est_start`/`pending` notes if the tools complain), `cut_list.py`, `anchor_shots.py`, assemble, `qa_short.py --full`, Gemini pre-check, UPLOAD.md.
4. **Re-check the count the day of.** A Nuggets game before then could be a triple-double (200 becomes 201+): then "his two hundredth, to the day" must be reworded to "his two hundredth, on the anniversary of his debut" or similar.
5. Optional: a Westbrook clip from a league source (ESPN clip of his record or retirement) for the line "Only Russell Westbrook has more".
6. Quick checks: J01 ends before the source dissolve (9.86 s); J07 shows Jokić on screen at 26-29 s of the X video; run `deflash.py --check` on cut clips only.
