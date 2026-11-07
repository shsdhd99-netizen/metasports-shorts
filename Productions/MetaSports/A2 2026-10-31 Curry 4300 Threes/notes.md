# A2 Curry's 4,300th three-pointer (pre-build, Account 2, Oct 31 2026)

**Status: voice-ready. NOT voiced (the milestone night has not happened).** The main account fills the SLOT and {GAP}, voices it, adds the night's clip and posts the morning after (news: must go up the morning after the game).

- **Lane:** star paradox / news hybrid. A household name, one idea a casual fan gets in second 1 (nobody is even close to him).
- **Concept (8 words):** Nobody is within 800 threes of Curry.
- **Hook:** line 1 = "No one is within eight hundred threes of Stephen Curry." (10 words, a statement, present tense). Present tense on purpose: Ray Allen was one three behind him in Dec 2021, so "has come within" would be false.
- **Added value (facts the clip can't show):** the record he took was Allen's 2,973, passed Dec 14 2021 (his 2,974th); he has made 1,300+ more since; 42.2% career; the gap to second place.
- **Copy check:** NOT run (no network access to YouTube search in this session). Main account: run `copy_check.py "Curry 4300 threes"` before voicing.

## Re-verified TODAY (Oct 31 2026, before the Warriors' next game, Nov 1 vs LAC)
- **ESPN** (public athlete stats API, `site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/3975/stats`, career totals row): 3PT = **4270-10123**, 3P% 42.2. 2026-27 row: 22-50 in 5 games.
- **Basketball-Reference** `https://www.basketball-reference.com/leaders/fg3_career.html` (fetched Oct 31): 1. Stephen Curry 4270; 2. James Harden 3402; 3. Ray Allen * 2973. (The page is the all-time list, not active-only.)
- **Harden (ESPN, athlete 3992, career totals):** 3PT 3402-9362. Matches BBRef.
- **Gap to 4,300: 30.** Lead over Harden today: 868. Warriors games (ESPN team schedule, ET): Nov 1 LAC, Nov 2 PHX, Nov 5 MIA, Nov 7 ORL, Nov 9 NO, Nov 11 @HOU, Nov 13 @SA, Nov 16 @NO, Nov 18 @DAL. At 4.4 per game (22 in 5), about 7 games: **Nov 9 to Nov 13**.
- Warriors did not play Oct 31 (ESPN scoreboard has no GS game).

## Claims table
| Script line | Source | Exact words / data |
|---|---|---|
| No one is within eight hundred threes of Stephen Curry | BBRef list above; ESPN | Curry 4270, Harden 3402 (gap 868). At the milestone Curry has 4,300+, so the gap is about 870-900 unless Harden adds ~70+ in the same weeks. **Re-check Harden on the night** |
| SLOT: date, team, his 4,300th three-pointer | **TO FILL** from the ESPN box score / play-by-play and recap of the night | Use the exact count line ("4,300th career three"). Say "his four thousand three hundredth" only if the 4,300th happened that night |
| The record he took was Ray Allen's, at two thousand nine hundred seventy-three | BBRef list: "Ray Allen * 2973" | Allen's regular-season total. Wikipedia (Stephen Curry): "made his 2,974th career three-pointer to pass Ray Allen" (2,973 + 1) |
| He passed it on December fourteenth, twenty twenty-one, at Madison Square Garden, with his 2,974th | Wikipedia, Stephen Curry (2021-22 season): "On December 14 at Madison Square Garden against the New York Knicks, Curry made his 2,974th career three-pointer to pass Ray Allen and become the NBA's all-time three-point scoring leader." The next dated sentence is "January 21, 2022", so the year is 2021 | Tier: Wikipedia only. Confirm on ESPN/NBA.com before voicing if possible |
| Since then he has made more than thirteen hundred more | arithmetic: 4,300 - 2,974 = 1,326 after that shot | **True only when he has 4,300+.** Today (4,270) it would be 1,296, so do not voice before the milestone |
| He has made them at forty-two percent | ESPN career totals: 3PT 4270-10123, 3P% 42.2 | Stays 42.2-42.3 after 30 more makes. Re-read on the night |
| Second place, James Harden, is {GAP} behind | BBRef / ESPN: Harden 3402. GAP = Curry's total minus Harden's total on the night, in words | Today 868 (4270 - 3402). About 898+ on the night if Harden stands still |

## Slot (about 18 words, about 4 s)
"On {DATE}, against {TEAM}, he made his four thousand three hundredth three-pointer." Total script about 78 words, about 20-22 s. If tighten_voice brings it under 20 s, the main account can add one ESPN fact (2025-26: 190-484 on 39.3%) or leave it; payoff stays the last line.

## Footage (all ESPN public clip API, 1080p60 unless noted, in `src/`; list in `src/downloads.csv`)
| File | Source | Used for |
|---|---|---|
| `espn_curry_range_min.mp4` (15.2 s) | event 401909888 (Warriors at Timberwolves, Oct 28 2026), video 50313021 "Stephen Curry shows off the range on triple" | C01 frame 1 (face 8.2-9.9 s, slowed 0.8 to hold 2.1 s), C05 (dribble and shot, 10.0-12.2) |
| `espn_curry_trey_lal.mp4` (15.3 s) | event 401909285 (Lakers at Warriors, Oct 30), video 50332754 "Steph Curry splashes a trey" | C02 (11.0-13.4) |
| `espn_curry_clinic_lal.mp4` (17.3 s) | same event, video 50333380 "Curry puts on a dribbling clinic vs. Doncic on way to a triple" | C03 (15.0-17.2, Curry running up court) |
| `espn_curry_shimmy_lal.mp4` (19.3 s) | same event, video 50332985 "Stephen Curry hits the shimmy after a 3-pointer" | C04 (17.0-19.2, celebration with teammates) |
| `espn_curry_cooking_lal_opener.mp4` (49 s, **720p**) | event 401909092 (Warriors at Lakers, Oct 21), video 50244237 "Chef Curry is cooking with 3 consecutive buckets" | C06 (front-face close-up 46.3-48.6) |
| `espn_gsw_lal_highlights.mp4` (86.7 s) | event 401909285, video 50333448 "Warriors erase big early deficit and beat the Lakers at home" | C07 payoff (Curry arms out, 47.1-48.5, slowed 0.7) |

- **Illustrative, flagged:** no public footage of the Dec 14 2021 shot or of Ray Allen from a league source. C03 and C04 are current Curry footage; the names and dates are carried by overlays. NBA on X posts were not searched (no search tool in this session); `Tools/x_clip.py` is there if the main account wants more.
- Rights: league/broadcaster footage, narrated version only, shots of 2-3 s.
- Frames were checked on 1-3 fps contact sheets only. `footage_qc.py` and `deflash.py --check` (cut clips only) were NOT run: do both before `--verified`.

## What's missing on milestone night
1. **The night itself:** which game and the exact count. Fill the SLOT (remove the `[[SLOT ...]]` brackets), `{GAP}` (script and C07 overlay) and the "4,300" overlay on RN1. If he is still under 4,300 after a game, nothing is postable.
2. **The night's clip** as `src/record_night.mp4` (ESPN `summary?event=<id>`, `videos[].links.source.HD.href`, or NBA on X via `Tools/x_clip.py`): RN1 build-up, RN2 the shot going in, RN3 = RN2 at 0.5x, zoom 1.3, same `at`.
3. **Voice and build:** check credits (script about 480 characters); `voice_take.py`, `tighten_voice.py --thresh 0.25 --keep 0.12`, `fill_len.py`, copy `cuts_plan.json` to `cuts.json` (drop `est_*`/`pending` notes if tools complain), `cut_list.py`, `anchor_shots.py`, assemble, `qa_short.py --full`, Gemini pre-check, UPLOAD.md.
4. **Re-check all counts the day of** (Curry, Harden, 42.2%).
5. **Quick checks:** C02 release visible at 11.0-12.5; C06 blow-up on the 720p source; first 3 s = C01 (2.1 s) + C02 (2 shots).
