# #80 The Warriors flipped the exact same score (same-day news, number gap) - BUILT Oct 31 (voice + render + QA PASS)

Made by the NBA daily run, Sat Oct 31, 2026 (10:45 UTC). **Blocked:** `ELEVENLABS_API_KEY` is not in this session's environment
(`cloud_setup.sh`: `key: MISSING`), so no voice, render or QA. No voice faked. No analytics tokens either (YT_* missing).
**News window:** the game was Fri Oct 30 (10:30 PM ET tip). Post Sat Oct 31 or drop it (late news rule, #63).

## Lane
Same-day news with a number gap (household names: Luka, Curry). Last 6 NBA builds: #74 evergreen, #75 moment, #76 evergreen, #77 news,
#78 evergreen, #79 moment (skipped), so news is within 1 in 3. Music side: no music (news Short; NBA music test is 2 and 2).

## Facts and exact source words
Game: Warriors 112, Lakers 95, Fri Oct 30, 2026, San Francisco, NBA Cup. ESPN game 401909285.
- Quarters (ESPN box score linescore, `site.api.espn.com/.../summary?event=401909285`): GSW 15-38-32-27 = 112; LAL 38-15-27-15 = 95.
  So 53-53 at halftime. "Won a quarter by 23" = Q1 38-15. "Lost by 17" = 112-95.
- AP recap (on ESPN, https://www.espn.com/nba/recap?gameId=401909285):
  - "the Golden State Warriors erased an early 25-point deficit then ran away from Luka Doncic and the Los Angeles Lakers for a 112-95 win"
  - "Doncic had 21 points on 7 for 12 shooting with five 3-pointers, five assists and a pair of steals through the first quarter as the Lakers raced ahead 38-15."
  - "The Warriors then outscored the Lakers by the same 38-15 score in the second. That made Golden State the first team in the shot clock era — including playoffs — to trail by 23 or more points at the end of the first quarter and be tied or better at halftime."
  - "It was the largest margin of victory in the shot clock era for a team that trailed by 20 or more points at end of the first quarter. On March 4, 1976, the Warriors trailed the Bulls 41-18 after one quarter and won by 14 at 124-110 — the previous best."
  - "In the fourth, Curry passed Dominique Wilkins (26,668) for 18th place on the NBA's all-time scoring list."
  - "Doncic had 37 points, seven rebounds and five assists"; "Stephen Curry had 31 points, six assists and four rebounds".
- Box score: Doncic 37 pts, 12-27 FG; Curry 31 pts, 8-14 3PT, +19.
Script line check: every number above; "the shot clock era" kept on both record lines (AP's qualifier).

## Copy check
`copy_check.py "Lakers 38-15 Warriors same score"`: FRESH. ("Warriors Lakers 25 point comeback": CROWDED, but only old games.)

## Footage (ESPN public clips, game 401909285; checked Oct 31 10:45 UTC, all downloadable)
- 50333448 "Warriors erase big early deficit and beat the Lakers at home" 86 s (frame sheet: scorebugs 19-11, 22-11 (0:06), 31-14 (0:12-0:15), 42-31 (0:18-0:27), 53-50 (0:33-0:39), Luka close-up 0:09, Curry close-up 0:48, Curry celebration 1:03, Luka 1:12). The 38-15 scorebug itself is not in it: show the numbers as words over footage.
- 50332790 "Luka Doncic lets the crowd hear it after an and-1" 19 s; 50333194 "Luka Doncic drains fadeaway 3-pointer" 16 s
- 50333380 "Curry puts on a dribbling clinic vs. Doncic on way to a triple" 17 s; 50332985 "Stephen Curry hits the shimmy after a 3-pointer" 19 s; 50332754 "Steph Curry splashes a trey" 15 s
- Get the URLs: `curl https://content.core.api.espn.com/v1/video/clips/<id>` -> videos[0].links.source.HD.href

## Cut plan (for the render)
- Frame 1: Luka scoring/celebrating in the first quarter (50332790 or recap 0:09), words "38-15 LAKERS" over it. Hold 2+ s.
- "Then the second quarter ended 38 to 15": Curry three (50332754), words "38-15 WARRIORS". "Same score, flipped": the two lines side by side.
- Record line over the recap's 53-50 scorebug run (0:33-0:39). "Luka still scored 37": Luka fadeaway (50333194), "37".
- "Curry passed Dominique Wilkins": Curry shimmy (50332985), "18TH ALL-TIME". End on Curry celebration (recap 1:03); nothing after the line.
- Real-audio option: the shimmy/three calls are strong; a real-audio version follows the `nat_sound.py` pattern from #79.

## Open checks before voicing
- Confirm the Wilkins pass happened in this game in a second source (NBA.com or Warriors PR) if one is up.


## Build log (Oct 31, 2026, build agent)
Script v2 (original kept in `_script_v0_original.txt`): line 1 is now 11 words ("The Lakers led by 23 after one and lost by 17."), 25.2 s, 465 characters of voice (one take, HNR 8.1). Added "53 to 53 at halftime"; "tied or better" kept from AP; payoff last (the 20-or-more, shot clock era record line).
Wilkins pass: still one source (AP on ESPN). Kept, attributed nowhere in speech; if a second source shows otherwise, cut that line with word_edit.py.

### Claims table (all re-checked Oct 31 against ESPN summary API event 401909285 and the AP recap on ESPN)
| Line | Source | Exact words / data |
|---|---|---|
| "Lakers led by 23 after one" | ESPN linescore | LAL 38, GSW 15 after Q1 (38-15 = 23) |
| "lost by 17" | ESPN final | Warriors 112, Lakers 95 |
| "Luka had 21 points in that quarter alone" | AP recap | "Doncic had 21 points on 7 for 12 shooting with five 3-pointers, five assists and a pair of steals through the first quarter as the Lakers raced ahead 38-15." |
| "second quarter ended 38 to 15, for Golden State" | ESPN linescore + AP | GSW 15-38-32-27; "outscored the Lakers by the same 38-15 score in the second" |
| "53 to 53 at halftime" | ESPN linescore | GSW 15+38 = 53; LAL 38+15 = 53 |
| "No team in the shot clock era had trailed by 23 or more after one and been tied or better by halftime" | AP recap | "the first team in the shot clock era - including playoffs - to trail by 23 or more points at the end of the first quarter and be tied or better at halftime." |
| "Luka still finished with 37" | AP + box score | "Doncic had 37 points, seven rebounds and five assists" (12-27 FG) |
| "Curry passed Dominique Wilkins on the all-time list" | AP recap (single source) | "In the fourth, Curry passed Dominique Wilkins (26,668) for 18th place on the NBA's all-time scoring list." Overlay says "18TH / ALL-TIME SCORING" |
| "no team down 20 or more after one has won by more in the shot clock era" | AP recap | "the largest margin of victory in the shot clock era for a team that trailed by 20 or more points at end of the first quarter" (previous best: Warriors over Bulls, Mar 4 1976, by 14) |
Overlays: "38-15 LAKERS AFTER ONE", "21 PTS", "38-15 WARRIORS IN Q2", "Q1/Q2 38-15", "53-53 HALFTIME", "FIRST EVER / SHOT CLOCK ERA" (AP qualifier kept in the sub-label), "37 PTS", "18TH", "WON BY 17" (112-95).

### Footage (ESPN public clip API, 1080p60, all game 401909285; src/ is git-ignored)
50333448 recap (86 s), 50332790 Luka and-1, 50332985 Curry shimmy, 50333380 Curry clinic. Illustrative, flagged: H02/H07 Luka close-ups and H06 are Q1/Q3 footage under lines about Q1/Q3 totals; H05 is the crowd reacting at the end of the first half (bug 53-50 with 5.5 s left; not a proof shot of the tie, the 53-53 is the overlay and the linescore); H03/H08 Curry shimmy is a Q2 clip (bug 40-25 at start).
Audio: limiter added after the render (decoded peak was 1.1); final -14.2 LUFS.

### Not done
Real-audio version: ESPN clips do carry live calls (shimmy clip: "Ten unanswered points by Golden State." 0-3 s, "His third triple of the ballgame" about 12 s, "Boys!" about 17 s), but none lines up with a script beat without re-cutting narration. Left for a follow-up if wanted (nat_sound.py recipe).
Gemini pre-check said FIX ("narrator says The Mavericks", tier S). A local speech-to-text pass on the export reads "The Lakers led by 23 after 1 and lost by 17" and the whole script correctly, so the FIX is a false positive.
Credits: 465 characters (one take). Before: 36,452 used; ceiling check passed (84,772 left minus 66,500 reserve).
