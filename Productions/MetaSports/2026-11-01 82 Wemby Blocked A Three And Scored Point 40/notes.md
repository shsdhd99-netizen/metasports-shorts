# #82 Wemby blocked a three and scored point 40 (one clip, one oddity) - SCRIPT ONLY, NOT RENDERED

Made by the NBA daily run, Sun Nov 1, 2026 (about 11:45 UTC). **Blocked:** `ELEVENLABS_API_KEY` is not in this session's environment
(`cloud_setup.sh`: `key: MISSING`), so no voice, render or QA. No voice faked. No analytics tokens (YT_* missing).
**News window:** game Sat Oct 31. Post Sun Nov 1 or drop it.

## Lane
One clip, one oddity (a block and the 40th point five game-seconds apart), a household-name star. Last NBA builds: #78 evergreen,
#79 moment (skipped), #80 news (skipped), so a moment fits the rotation. Music side: none.

## Facts and exact source words
Game: Spurs 121, Timberwolves 111, Sat Oct 31, 2026, San Antonio. ESPN game 401909901.
- ESPN play-by-play (`site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909901`), 4th quarter:
  - 6:20, MIN 101-105 SAS: "Victor Wembanyama blocks Jonathan Kuminga 's 24-foot three point step back jumpshot"
  - 6:15, 101-107: "Victor Wembanyama makes running dunk (Dylan Harper assists)" = his 40th point (running total from the same feed: 38 before it).
  - 5:04 "blocks Joan Beringer's layup"; 2:52 "blocks Jonathan Kuminga's driving floating jump shot"; 2:40 "makes 23-foot three point jumper (Devin Vassell assists)" = 43.
  - "Five seconds later" = game clock 6:20 to 6:15. "Spurs up four" = 105-101.
- ESPN box score: 43 PTS, 17-34 FG, 3-8 3PT, 6-9 FT, 7 REB, 4 AST, 6 BLK.
- AP recap (https://www.espn.com/nba/recap?gameId=401909901): "Wembanyama was 17 of 34 from the field in reaching 40 points for the 10th time in the regular season and the 11th time in his career. After blocking Jonathan Kuminga's 3-point attempt, Wembanyama raced downcourt for a two-handed dunk to give him 40 points." Also: Minnesota "without injured starters Anthony Edwards (knee surgery) and Rudy Gobert (back spasms)".
- Not used (single source / conflict): a French outlet's "first Spur since David Robinson with 40 and 5 blocks"; one outlet citing ESPN says 5 blocks (the box score and AP say 6).

## Copy check
`copy_check.py "Wembanyama off the backboard to himself"`: FRESH. `"Wembanyama block 40th point dunk"`: TAKEN, but a false match: the hits are old unrelated Wemby dunks (Chaz NBA's Ja Morant poster 1.85M, an AD and-1), not this play.
Also in the game: Wemby threw the ball off the backboard to himself for a layup (AP), but #71 Haliburton already did the alley-oop-to-himself idea; not picked.

## Footage (ESPN public clips, game 401909901; downloaded and frame-checked Nov 1)
- **50343302 "Victor Wembanyama throws down the hammer" (19 s): the play itself.** Scorebug MIN 101 - 105 SAS at 6:28 (0:00) through 6:15 and 107 (about 0:12-0:13); replays from 0:13 (baseline and overhead-rim angles, 0:16-0:19.5).
- 50343548 game highlights (74 s), 50342108 "elevates for the big-time block", 50343198 "skies for big slam dunk", 50343091 alley-oop, 50342995 and-1.
- URLs: `curl https://content.core.api.espn.com/v1/video/clips/<id>` -> videos[0].links.source.HD.href

## Cut plan
- Frame 1: the block itself in 50343302 (find the exact frame near 0:09-0:11 at full size; the frame sheet is too small to be sure), words "BLOCK" then "40" over the dunk.
- Line 2-3 over the pull-up and block (slow it, `"speed": 0.5`, on the contact). Lines 4-6 over the run and dunk (0:10-0:13), "POINT 40" on the rim.
- Replay angle (0:16-0:19.5) for "He wasn't done"; then 50342108 for "two more blocks"; end on "43 / 6 BLK" over Wemby, nothing after the last line.
- Real-audio option: the broadcast call on the dunk (`nat_sound.py`, as #79).

## Open checks before voicing
- Confirm by eye which seconds of 50343302 show the block vs the dunk (scorebug 105 -> 107 marks the dunk).
