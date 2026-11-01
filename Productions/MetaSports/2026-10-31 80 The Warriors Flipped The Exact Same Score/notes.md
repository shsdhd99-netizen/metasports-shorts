# #80 The Warriors flipped the exact same score (same-day news, number gap) - SCRIPT ONLY, NOT RENDERED

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
