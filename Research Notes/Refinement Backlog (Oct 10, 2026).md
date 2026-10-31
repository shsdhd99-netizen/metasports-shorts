# Refinement backlog (Oct 10, 2026)

Diagnosed from the production folders, the voiced scripts, the Oct 10 Studio cards, and the public counts in `Outcome Log.md`. No posted file was recut. No READY was overwritten. No ElevenLabs spend. The only new production text is an unvoiced replacement for short 27.

Stayed%, average view duration, and views are separate. A low view count is not a copyright finding. Bad Boys was posted the same day as this read (about 210 public views) and has no stayed% yet.

80% stayed is the bar (number 6, 82.4%, average view 0:30 on a 0:26 video). Under 55% stayed is a swipe. About 65% is not a win. Once a viewer stays, average view duration usually reaches the length. The exceptions on Oct 10 are the Cup final (0:16 of 0:23), Bronny-got-better (0:17 of 0:25), and the rugby upload (0:19).

## Ranked work

### 1. Post short 21 v3. Do not recut it.

File: `Productions\MetaSports\2026-10-04 21 How Close Is Jokic To Westbrooks Record\READY TO POST - How Close Is Jokic To Westbrooks Record (v3).mp4`

The voiced script is `_v2\script.txt`. It ends on a closed pace: "At that pace, eleven more takes about twenty-one games." QA passed on the v3 cut (24.9s, about −14 LUFS). Second 0 is Jokic in 15 with the ball. The rim hit at 11.29 is on number 0 at the rim.

What is still imperfect, and why it does not earn another render:

- The first line is a question. The last line answers it with a pace. Revoicing only to change those opening words is a new spend for a cut that already has a person and the record in frame.
- The triple-double count is not a picture. The jerseys are. That was the feasible fix, and v3 already made it.
- The W on Westbrook's back is cropped in two frames. Shifting the in-point on a short clip would loop it. Leave it.
- 198 and 209 were preseason-safe on Oct 10. Re-check both the morning it is posted. The season opens Oct 20, 2026.

Do not restore the parent `script.txt`. That file still ends "So does Jokic pass Westbrook before Christmas, or does the record survive?" Those words are not in the voice.

Critique Round 6 saw the older cut. It is not a review of v3.

### 2. Short 27. Keep the picture. Replace the script. Do not voice until asked.

Current file, leave it in place: `Productions\MetaSports\2026-10-04 27 Why The Worst Team Gets Fewer Balls\READY TO POST - Why The Worst Team Gets Fewer Balls (v2).mp4`

Picture diagnosis: v2 already opens on a hand dropping lottery ball 12 (`03_balls.mp4`, in 0.05) and loops that clip. That part is salvaged. Round 6's "stage open" note is stale.

The biggest problem is the spoken script, and an edit cannot delete a sentence that is already in `voice.mp3`.

- The Jazz fine is a different event. NBA.com, Feb. 13, 2026, fined Utah $500,000 for sitting Markkanen and Jackson. That is not the lottery rule.
- "A fine was not the twist" is forced suspense. It tells the viewer the previous sentence was a detour.
- "Draft relegated" is the league's own phrase (NBA Communications, May 28, 2026). It is still jargon in a 27-second short.
- The last line is a second rule, not the ball count. The same release says no team's pick can be first in two consecutive drafts. The title and the open are about fewer balls. Two premises in one short.
- Runtime is 27.6s, past the 22–26s target. The extra seconds are the fine and the second rule.
- Sound follows the detour. The ding at 15.55 marks the Jazz fine, and there is no money graphic on screen. The boom at 21.10 sits on the lottery stage. Dropping those two effects would still leave the sentences in the voice. Do not re-assemble v2 for the mix.
- Middle pictures (Tatum, a hug, the stage) do not show two balls versus three. Reordering them under the current voice does not remove the fine.

Replacement, spoken only, not voiced: `script_replacement.txt` in that folder. 95 words. "But" is word 19, inside the first 40%. The first seven words are the fact. The Washington line is the 2026 result under the old drawing. It does not say the Wizards are barred in 2027. Sources are already in `notes.md`.

Implementation, only after a yes on the voice spend:

1. Leave `script.txt`, `voice.mp3`, `words.json`, `shots.json`, `sfx.json`, and the v2 READY untouched.
2. Voice `script_replacement.txt` into a new `_v3` folder. Copy the clips. Do not splice the old voice.
3. Anchor the new words. Open and close on `03_balls.mp4` (in 0.05). Keep `10_tube.mp4` under the two-ball and three-ball lines.
4. Use the pick graphic that reads PICK 1 / WASHINGTON WIZARDS only under "still gave Washington number one." The source tweet is already in `notes.md` (`https://x.com/NBA/status/2053558794823581796`). Do not put Tatum, the hug, or the stage under a line that does not name them.
5. Zero sound effects unless a frame shows the sound. No ding on a fine. No boom. No effect in the first second.
6. Assemble with `--caption-style metasports`. Run `qa_short.py`. Look at second 0 and the Washington frame.
7. Copy `final.mp4` to a new `(v3)` READY. Leave v2.
8. Re-read the 2027 start date on the NBA Communications page the morning of the voice.

### 3. Short 30. The script is usable. The footage is not.

Folder: `Productions\MetaSports\2026-10-05 30 Why A Heave Miss Is Free`

91 words. "But" is word 9. No READY, no voice. The six downloads are makes, plus one fourth-quarter ending with no heave. A make cannot sit under "a miss does not count."

Do not rewrite this script to match the clips on disk. Do not voice it. The next action is one moving post-rule miss from the first three quarters, and one fourth-quarter miss. The Dieng airball is 2023, before the rule. Giddey's shot went in. Copy-check printed FRESH on Oct 5. That is not a saturation verdict.

### 4. Short 06. Hold for one body in the corner.

Folder: `Productions\MetaSports\2026-10-03 06 Why Is the Corner Three Shorter`

The lines earn their place: 23 feet 9 at the top, 22 in the corner, the court is 50 feet wide, so the arc is cut. That is one visible fact. A diagram does not show it. Do not voice until a player is standing in the corner with the line and the body in the same frame.

### 5. Leave these cuts. Do not rebuild them.

| Short | Biggest problem | Why a recut does not pay |
|---|---|---|
| 26 height gap | Same visible fact as Flagg, posted Oct 6 (19K, 73.5% stayed, average view 0:23 of 0:22). The two bodies already show the gap. QA passed, 24.5s. | A second height short. The file can stay. Do not post it to borrow a height concept. |
| 23 Bronny v3 | Third roster short after 24 (5.7K, 68.4% stayed, average view 0:28 of 0:29) and 25 (1.9K, 63.7%, average view 0:17 of 0:25). | Editing cannot make it a different story. The script also stacks quotes, Christmas, and a deadline. Leave the file. |
| 28 Hart | The quote is real. The open is a presser. The rebound clip does not show his name, so the mic has to stay. `surprise` at 14.04 is not a pictured sound. | A mix pass would not change the open. Do not start a new production. |
| 02 free throw | The fact is a 15-inch offset: the line is measured from the backboard, the rim sits off the glass, so the shot is 13 feet 9. The READY opens on an overhead free throw, Rockets 21 at the line, hoop in frame. That is a free throw. It is not the offset. Parent `shots.json` opens on a shoe. Do not assemble that list. | Reordering current clips cannot show the inches. A measuring graphic is the thing the picture gate resists. New side-on footage of rim, glass, line, and a shooter would be a different video. Ranked under 21, 27, 30, and 06. |
| 04 Giannis trade | A return list in the contract lane. Duren, the posted contract short, stayed 67.5% on Oct 4 and sits at about 2,800 public views. The open is a face. No in-game Giannis play is in the folder. | A new game clip would fix the open and would leave the lane. Do not produce it. |

### 6. Do not voice these. The premise is the problem.

| Short | What is wrong |
|---|---|
| 05 Sixers superteam | A roster list, then "their first real test tells us everything." The ending is a banner-night preview that overlaps 09 and 10. |
| 07 SGA | A name list, then Thunder at Spurs on opening night. A place and a list. |
| 08 Kyrie | The payoff is Macao on October 9. That date has passed. The return angle was already rejected as a new video. |
| 09 LeBron calendar | A schedule of buildings and dates. The Cup final already tested a late place twist: 51.5% stayed, average view 0:16 of 0:23. |
| 10 Knicks banner | The 1973 open is a real fact. The script then becomes another LeBron debut preview and overlaps 09. |

## Posted files. Diagnosed and left alone.

A new file on disk does not change the upload.

| Video | What the numbers say | Biggest problem | Class |
|---|---|---|---|
| 22 number 6 | 82.4% stayed, average view 0:30 of 0:26, about 31,000 views | None that this read supports. Closed consequence. Person and the number in second 0. | Leave. This is the bar. The parent script's question ending is not the posted cut. |
| 03 Wemby vote | 80.1% stayed, average view 0:25 of 0:24, about 26,000 | None. Closed list. | Leave. |
| 19 Flagg | 73.5% stayed, average view 0:23 of 0:22, 19,000 | The question ending held people and still missed 80%. | Leave. Do not copy the ending. |
| 01 pay cut | 71.8% stayed, average view 0:24 of 0:24, about 2,800, one day old on Oct 10 | Retention matched the length. Views did not. Salary lane. | Leave. A recut is not distribution. |
| 17 flopping | about 69% stayed, average view 0:23 of 0:29, about 5,200 | A bit long against its average view. People stayed. | Leave. |
| 24 Bronny spot | 68.4% stayed, average view 0:28 of 0:29, about 5,700 | First of the family. It held. | Leave. |
| 15 Adams | 66.2% stayed, average view 0:21 of 0:23, about 5,900 | A bit, and it held better than the place shorts. | Leave. |
| 18 helicopter | 65.9% stayed, average view 0:24 of 0:27, about 2,700 | Training-day story. Updated from 60.1%. Still not a win. | Leave. |
| 16 Vice City | 65.5% stayed, average view 0:20 of 0:26, about 2,700 | Average view falls short of the length. | Leave. The sag is inside a posted voice. |
| 25 Bronny better | 63.7% stayed, average view 0:17 of 0:25, about 1,900 | Second video in the only family pair. The middle was lost. | Leave. This is why 23 stays unposted. |
| 14 four stars | 63.2% stayed, average view 0:28 of 0:24, about 1,500 | People replayed it. Views stayed low. | Leave. Replay did not buy reach. |
| 12 Duren | 67.5% stayed on Oct 4, average view 0:22 of 0:33, about 2,800 | Contract lane, and the cut is long. | Leave. This is why 04 stays unproduced. |
| Rugby upload, Oct 9 | 54.8% stayed, average view 0:19, about 1,700 | A swipe. No project folder in this tree names the mechanism. | Leave. Do not invent a cause. |
| 29 Cup final | 51.5% stayed, average view 0:16 of 0:23, about 2,300 | A building and a calendar. The "does not count" lands late. | Leave. A recut cannot put a person on that fact. |
| 13 Kawhi | 48.4% stayed, average view 0:20 of 0:23, about 1,500 | Pick-count lead and empty floor under names. | Leave. Already posted. |
| 11 Jordan | 34 views on the Oct 10 card. No engagement page. | Cause unknown. | Leave. 34 views is not a rewrite brief. |
| 20 Bad Boys v3 | Posted Oct 10. About 210 public views that day. | Unread. | Leave. Do not judge it and do not recut it. |

## Not in this backlog

The Ja signature package in `Research Notes\Next Short - He Signed The Wrong Number.md` is the next new short. It is not a recut of an existing folder. Do not voice it before Oct 12, and do not voice it if the 12 on the jersey is unreadable.

## What was verified

- Short 27 `notes.md` quotes NBA.com and NBA Communications for the ball counts, the 5.4% and 8.1% odds, the 2027–2029 window, the separate consecutive-No.-1 rule, the Jazz fine, and the 2026 Wizards result. The replacement uses those and drops the fine and the second rule.
- The replacement is 95 words and "But" is word 19. Confirmed by a word count after the file was written.
- v2 READY, v3 Jokic READY, and every posted READY were not rewritten.
