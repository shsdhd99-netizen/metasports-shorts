# Hook teardown: the first 3 seconds, Saturday 2026-10-31 (Account 2)

Question: why do our three best soccer Shorts lose viewers sharply at 2-3% of runtime, and why do some NBA Shorts have engaged ratio under 0.5?

**Evidence tiers.** [A] = our private API analytics (`Research Notes/Studio exports/api/` and `api FC/`, 2026-10-31). [M] = measured by me from the local DRAFT mp4 with ffmpeg/ffprobe, plus the `words.json`, `captions.srt`, `captions.ass` beside it. [L] = I looked at the extracted frames myself (contact sheets, frames at 0, 0.5, 1, 1.5, 2, 3 s). [S] = a Gemini report in `Research Notes/Watch Reports/` (one model's view; I did not watch or listen to any competitor video myself; for 7 of the 8 I also looked at YouTube's own 160x90 preview frames, [L], which only confirmed roughly what Gemini said). Rule: a pattern is a finding only if 3+ Shorts show it, otherwise "n too small".

**Caveats that apply to everything below**
- Our frames come from the `(no music)` DRAFT files in the Productions folders (S06 from the non-UNDER-60 draft). I did not check that the posted file is byte-identical to the draft. Where there were two drafts I used the one named in the table.
- The retention file has only 100 points (1% steps). For a 60 s Short a step is 0.6 s; for a 22 s Short it is 0.22 s. "2-3%" is therefore 1.2-1.8 s on a 60 s Short but only 0.4-0.7 s on a 22 s one.
- `audience_watch_ratio` is above 1.0 early (rewatches/loops), so I compare relative change, not an absolute "% still watching".
- Scene-cut counts use ffmpeg `scene > 0.25`. They can miss soft or same-scene cuts. Treat as +/-1.
- Silence check: ffmpeg `silencedetect` (-45 dB, 0.05 s) found no silence in the first 3 s of any of the 14 files, so audio is present from 0.0 s in all of them [M]. `words.json` puts the first word at 0.0 s in all 14 [M].

---

## 1. Which Shorts (6 best, 6 worst, both channels) [A]

Chosen by avg % viewed and engaged ratio, then limited to Shorts with a local draft. Three per channel per side, plus two extra NBA low-engaged ones the owner named.

| Side | Channel | Short (id) | Views | Avg % viewed | Engaged ratio | Draft used |
|---|---|---|---|---|---|---|
| Best | FC | Sock cheat sheet (`Wcaa80VvBmU`) | 28,173 | 92.9 | 0.557 | S01 |
| Best | FC | Water-bottle cheat sheet (`DfDEyHM33is`) | 27,637 | 96.8 | 0.553 | S05 |
| Best | FC | Danced on the line (`9GJgflHx7pE`) | 15,532 | 82.9 | 0.608 | S03 |
| Best | NBA | Haliburton alley-oop (`lU6xSO1cAOY`) | 7,573 | 110.7 | 0.575 | #71 |
| Best | NBA | Kid felt every free throw (`-sFQhpw-bQ0`) | 21,241 | 99.0 | 0.569 | #72 |
| Best | NBA | Most missed threes (`_Oahi9sBi1A`) | 23,870 | 95.9 | 0.591 | #48 |
| Worst | FC | 5 goals in 9 minutes (`ORnkQcenDd8`) | 2,040 | 63.7 | 0.533 | S06 |
| Worst | FC | Barcelona paid a fortune (`WCeenVoseEM`) | 1,016 | 68.5 | 0.554 | S15 |
| Worst | FC | Sent off in last game (`svDicOCeh7I`) | 1,889 | 72.6 | 0.596 | S04 |
| Worst | NBA | Caitlin Clark (`q5rCS_qVspk`) | 2,745 | 77.4 | 0.584 | #60 |
| Low engaged | NBA | SGA streak (`cBo01-uem4w`) | 8,400 | 94.6 | 0.495 | #66 |
| Low engaged | NBA | Chuck test (`qHeq-Yujpa0`) | 3,211 | 113.4 | 0.455 | #70 |
| Extra | NBA | Steve Kerr lookalike (`z63RYPffwZc`) | 6,429 | 106.6 | 0.495 | #49 |
| Extra | NBA | 2007 top picks (`Ctm9TiDMl4k`) | 5,626 | 98.3 | 0.484 | #34 |

"Worst" NBA by avg % viewed was thin (Caitlin Clark 77.4, then the rest are 85+), so NBA's weak side is mostly the low engaged ratio group. Note #34 (2007 picks) has no retention curve in the export, so it is in the frame teardown only.

## 2. Frame-level teardown of our 14 Shorts [M][L]

Frame time 0 / 0.5 / 1 / 1.5 / 2 / 3 s. "Cuts" = detected cut times inside 0-3 s. Caption timing is from `captions.srt` (chunk 1 on-screen window).

| Short | Line 1 (spoken, exact) | Frame 1 shows | Caption timing and style | Cuts in 3 s | Audio start |
|---|---|---|---|---|---|
| FC sock (S01) | "Goalkeepers who hid a cheat sheet in their sock." (9 words) | A keeper bent over, back/legs, tight crop on a red board. Then a "LEHMANN 1" shirt at 1 s, camera operator at 1.5 s, ball on grass at 2 s. Never shows the sock itself in 0-3 s [L] | One static 2-line block (small, mid-screen, CHEAT SHEET in caps) 0.00-1.94 s, then "Back in 2006," | 2 (1.9, 3.0) | 0.0 |
| FC bottle (S05) | "Goalkeepers who hid a cheat sheet on their water bottle." (10 words) | Extreme close-up of a keeper's face looking down. The bottle with the sheet is on screen 0.5-1 s [L] | Same static small block 0.00-2.0 s, then "Back in 2018," | 1 (2.4) | 0.0 |
| FC danced (S03) | "Goalkeepers who danced on the line to win a final." (10 words) | A man's face, talking, tight, green pitch behind; the same unnamed face fills 0-2 s. No dancing in 0-3 s [L] | Static block 0.00-2.1 s, then "Back in 2005," | 1 (2.13) | 0.0 |
| FC 5 goals (S06) | "The player who scored five goals in nine minutes." (9 words) | Bayern player mid bicycle-kick, horizontal in air. The frame looks identical at 0, 0.5, 1, 1.5 and 2 s, so a freeze or near-freeze for about 2.1 s [L] | Static block 0.00-2.1 s, then "Back in 2015," | 1 (2.13) | 0.0 |
| FC Coutinho (S15) | "Barcelona paid a fortune for the player who knocked them out." (11 words) | Players hugging, "COUTINHO 10" shirt back; then a close-up in a Bayern shirt on a yellow board from 1 s [L] | Static block, text slightly smaller than the others; then "Back in January" | 4 (0.33, 1.0, 2.43, 2.67) | 0.0 |
| FC Zidane (S04) | "Players who got sent off in their very last game." (10 words) | Zidane standing still on the pitch with a broadcast score bug (2006 FIFA World Cup final, ITA 1 1 OT) [L]; the shot barely changes through 2 s | Static block 0.00-2.3 s, then "Back in 2006," | 1 (2.27) | 0.0 |
| NBA Haliburton (#71) | "Tyrese Haliburton just threw an alley-oop to himself." (8 words) | Haliburton dribbling in his Pacers jersey; ball in the air at 1 s, dunk at 1.5-2 s. Line 1 is happening [L] | Word chunks, big, lower third: "TYRESE HALIBURTON" 0.00-0.94, "JUST THREW" ..., "AN ALLEY-OOP" ... | 2 (2.63, 2.97) | 0.0 |
| NBA FT kid (#72) | "This kid felt every second of Jamal Murray's free throws." (10 words) | Close-up of a crying/clenching Nuggets kid, Denver jersey; the reaction is the line [L] | "THIS KID" 0-0.70, "FELT EVERY SECOND" 0.82-1.60 ... | 1 (3.03) | 0.0 |
| NBA missed threes (#48) | "James Harden has missed more threes than anyone in NBA history." (11 words) | Harden dribbling, then shooting at MSG; the shot goes up at 1.5-3 s. Line 1 is happening [L] | "JAMES HARDEN" 0-0.78, "HAS MISSED" (red) ..., "MORE THREES" ... | 1 (2.37) | 0.0 |
| NBA Caitlin Clark (#60) | "Caitlin Clark did something no NBA player has ever done." (10 words) | Clark close-up, mouth open, Indy jersey, scorebug 102-105 4TH. Face only, not the stat [L] | "CAITLIN CLARK" 0-0.70, "DID SOMETHING" ..., "NO NBA PLAYER" (red) | 2 (1.27, 3.03) | 0.0 |
| NBA SGA (#66) | "Shai Gilgeous-Alexander just ended the longest scoring streak in NBA history." (11 words) | Extreme close-up of SGA's face, headband; three identical-looking frames 0-1 s, then a game clip at 1.5 s [L] | Chunk 1 is the name only, on screen 0.00-1.45 s (longest first chunk of the set), then "JUST ENDED" etc. | 2 (1.27, 2.93) | 0.0 |
| NBA Chuck (#70) | "Charles Barkley just failed a test after they gave him the answers." (12 words) | Barkley laughing, head tilted, TV-studio close-up for 0-2.7 s; the "Who He Play For" set appears at 3 s [L] | "CHARLES BARKLEY" 0-0.76, "JUST FAILED" 0.79-1.31, "A TEST" ... | 1 (2.73) | 0.0 |
| NBA Kerr (#49) | "This is not Steve Kerr. But his name is Steve." (10 words) | Side-profile of an unlabeled older man in a Warriors blue jacket. The "STEVE GILLIS" and the real Kerr split-screen appears at 1.5 s [L] | "THIS IS" 0-0.5, "NOT STEVE KERR." (red) 0.5-1.4, then label at 1.5 s | 2 (1.4, 2.83) | 0.0 |
| NBA 2007 picks (#34) | "Greg Oden went first in the 2007 draft and played 105 games." (12 words) | Close-up of Greg Oden talking, with a visible "THE /pivot/" show logo top right (another creator's logo) [L]. Cut to young Durant at 1.5 s, table of picks at 3 s | "GREG ODEN" 0-0.71, "IN THE 2007" (green) ... | 2 (1.13, 2.03) | 0.0 |

Things the numbers say about timing: line 1 at 0.0 s, first caption at 0.0 s, no cards: **14 of 14 identical**. These cannot be the difference between the drop and no-drop Shorts.

## 3. Frame-level teardown of the top 8 competitor outliers [S] (+[L] on previews)

Source: `Research Notes/Account 2/Competitors 2026-10-31.md`, top 8 rows. Gemini reports in `Research Notes/Watch Reports/`; I ran `yt_watch.py` for `HVdbxbds7jU` (the only one of the 8 without a report). No yt-dlp downloads; I used `yt_sheet.py` previews where it returned frames (not for `n-jl3ZlpIbs`). Per-second ladders were not retrieved; I give what Gemini timed.

| # | Short | Line 1 / voice | Frame 1 (Gemini; preview where I could see it) | On-screen text in first 3 s | Shot 1 length | Shots in 0-3 s |
|---|---|---|---|---|---|---|
| 1 | SparkBalls `n-jl3ZlpIbs` (52M) | no voice | NFL punt coverage, overhead broadcast angle [S] | "One in a million" at 0 s | 2.75 s | 2 |
| 2 | CoachClank `keHURX3t594` (26M) | Spoken: "When a player is falling out of bounds, they usually throw it off an opponent to keep possession." AI male, about 160 wpm, 4-word white captions | Mitchell leaping out of bounds against Brunson [S]; preview shows a player jumping into a shot with a caption at the bottom [L, low-res] | the spoken line is also the caption | 3.7 s | 1 |
| 3 | GlobalHoopss `zXwHnwj_NR8` (9.1M) | no voice | Student section holding a white sheet behind the basket [S] | "The distraction worked" + skull emoji at 0 s | 1.75 s | 2 |
| 4 | docbooo `MNa-A2EpoNU` (6.7M) | no voice | A fan in 2003 pulling up his shirt, "WOLVES" on his stomach [S]; preview shows the shirt-lift at ~1.5 s [L, low-res] | "2003" at 0 s | 7.1 s | 1 |
| 5 | SparkBalls `9stUR8bcKsM` (21M) | no voice | NFL player catching near the endzone [S] | "One in a million" at 0 s | 3.0 s | 1 |
| 6 | docbooo `nNuQs1RSTtc` (4.9M) | no voice | Jokic holding the ball next to a rookie [S]; preview matches (a "ROOKIE" tag on a player at ~0.7-1.3 s) [L, low-res] | "ROOKIE" at 0.35 s, "*TROLLS ROOKIE*" at 5 s | 2.75 s | 1 |
| 7 | roycebball `JQ440kmooUU` (40M) | no voice reported (Gemini output was malformed, raw text read) | A boy on a bean bag kicking a ball into a mini hoop, girl reacting [S]; preview shows a girl on a chair, a mini hoop, a kicked ball, the boy on the bean bag [L] | a creator handle at 0 s (not a hook line), "8/10" card at 2 s | 2.0 s | 2 |
| 8 | Jaredlovessports `HVdbxbds7jU` (22M) | no voice, no music per Gemini | Batter vs a pitcher with a yoga ball [S]; preview shows "Hitting Every Sports Ball" on a dark title area at 0 s then a "Bowling Ball" label at 2.8 s [L, low-res] | title text at 0 s | 2.85 s | 2 |

Not repeated here: `HVdbxbds7jU` Gemini's other fields (45 s, 15 shots) are in its JSON.

## 4. Observed patterns

Drop group = the three FC Shorts the owner flagged (sock, bottle, danced). No-drop group = other six FC Shorts; for NBA, low-engaged (under 0.5: SGA, Chuck, Kerr, 2007 picks) vs high-engaged (0.569-0.591: Haliburton, FT kid, missed threes).

| # | Pattern | Evidence | Status |
|---|---|---|---|
| P1 | **The "2-3% drop" scales with reach, not with hook craft.** Relative drop from 1% to 3% of runtime: sock 17%, bottle 17%, danced 17%, other six FC 8-15% (trouble-before-derby 14%, Loch Ness 15%, sent-off 13%, 5 goals 12%, Hand of God 10%, Coutinho 8%) [A]. The three big-drop Shorts are also the three biggest FC Shorts by views (15,532-28,173 views vs 1,016-2,964 for the rest; Loch Ness and the derby Short are the exceptions at 14-15% drop on 2,454 and 1,810 views). Spearman of drop vs views: **0.70 (n=9 FC)**, 0.29 (n=19 NBA). Their level at 3 s (interpolated) is still the highest of any FC Short (1.31, 1.29, 1.27 vs 1.12-1.28 for the rest) [A] | 3 of 3 flagged Shorts, plus the rank correlation | **Finding (n=9; association, not cause).** Bigger reach means more cold swipe-aways in the first second. Not proof the hook is weak. |
| P2 | **In all three flagged FC Shorts the steepest step of the first 9% lands at 1.2-1.8 s (sock 0.19, bottle 0.22 retention points at the 2%-3% step), at or just before the end of line 1** (sock line 1 ends 1.94 s, bottle 2.0 s). Danced is split across 1%-3% (0.15 then 0.13). The six other FC Shorts have their steepest early step at 1%-2% and it is smaller (0.07-0.11) [A][M] | 3 of 3 | **Finding.** The exit is during the title read-aloud, before "Back in [year]". The Back-in cut (1.9-2.4 s) comes after the damage. |
| P3 | Every FC Short opens with a static, small, 2-line title block for the whole line 1 (about 2 s), at mid-screen, not synced to the voice; every NBA Short opens with big 2-3 word chunks in sync with the voice, key word coloured [M][L] | 6 of 6 FC, 14 of 14 including NBA split by channel | **Fact, but it does not separate drop from no-drop** (all six FC share it). No FC Short exists without it, so I cannot test it. n too small for an effect. |
| P4 | Frame 1 shows what line 1 says. Yes in Haliburton, Harden (missed threes) and FT kid (the kid's reaction is the line). No in SGA, Chuck, Kerr, 2007 picks (all close-ups of a face, no streak, no test, no name label or the wrong one). Also no in Caitlin Clark (face, no stat) [L] | High-engaged 3 of 4 (incl. Clark as the miss); low-engaged 0 of 4 | **Finding (n=8, observation).** Engaged ratio here is a narrow band (0.455-0.591) and sample is tiny, so treat as the one to test first. |
| P5 | Shot 1 shorter than the 2.0 s bar in our NBA: SGA 1.27 s, Kerr 1.4 s, 2007 picks 1.13 s (low-engaged) and Clark 1.27 s; held 2.4-3.0 s in Haliburton, FT kid, missed threes, Chuck (2.73) [M] | Low-engaged 3 of 4 break the bar, high-engaged 1 of 4 | **Finding (n=8).** It matches our own written rule in START HERE section 8, so it is a compliance miss, not a new idea. |
| P6 | Shot 1 is a frozen or near-static frame: S06 5 goals (~2.1 s freeze, the worst-retention FC Short, 63.7%) and S04 Zidane (standing, 72.6%) vs motion in shot 1 of the sock, bottle and danced Shorts [L] | 2 of the 3 worst FC | **n too small** (needs 3+). S15 is the third-worst and has the opposite issue (4 cuts in 2.7 s). |
| P7 | Competitors: 7 of 8 have text or voice on screen by 0.35 s (all but #7, whose text is a creator handle); 7 of 8 have 1-2 shots in 3 s; shot 1 of 6 of 8 runs 2.75 s or more [S] | 7/8 and 6/8 | **Finding, tier [S].** Our rules already say this. The competitor shot 1 is longer than our FC shot 1 (1.9-2.4 s). Caution: 6 of 8 are voiceless clip or compilation channels, a different lane. |
| P8 | Another creator's logo in frame 1 (2007 picks: "THE /pivot/") and a broadcaster bug (Kerr: NBC at 1.5 s) [L] | 1 and 1 | **n too small.** Already banned by rule 8 in START HERE section 8 (no logos from other creators). |

Not claimed: any effect of music, voice or caption style on the early drop (all 14 are identical on voice and caption timing); any competitor retention number (we have none); the posted files' exact frames.

## 5. Five hook rules to try

Each is a test, not a proven fix. Change one thing per Short where possible; the first post after the change is the data point.

1. **Make frame 1 the thing line 1 names (evidence P4).** Pick shot 1 from the clip of the exact moment in line 1, not a face close-up. Edit: in the cut list, set shot 1 to the first play/clip named in line 1; for the four low-engaged Shorts that would have been SGA's streak-ending game clip, the answer sheet in Chuck's test, the "STEVE GILLIS" frame instead of an unlabeled profile, a draft-night clip of the named picks instead of a talking head. For FC, the sock Short's frame 1 should show a sock or a keeper's sock (we have the bent-over keeper, but 0-3 s never shows the sheet), and the danced Short should show a keeper dancing, not a talking face.
2. **Shot 1 holds 2.7 s or more, then the second shot (evidence P5, P7).** Edit: set shot 1 `dur` to 2.7+ s in the NBA cut list (3 of 4 low-engaged Shorts and Clark had 1.1-1.4 s); in FC, hold shot 1 through the end of line 1 (about 2.0-2.4 s) and put the "Back in [year]" cut at or after 2.7 s. The FC best three cut to "Back in" at 1.9, 2.13 and 2.4 s.
3. **Lead FC line 1 with the strange thing, and make the title block bigger and synced (evidence P2, P3).** The exit step lands at the end of the read-aloud title. Edit (A/B on S21+ using `title_caption.txt` and `assemble.py --caption-style`): keep the same line 1 words, but (a) split the title block into two chunks that appear with the voice (chunk 1 on at 0.0, chunk 2 at about 0.9 s, key word in caps and colour as in our NBA captions), (b) increase its font size so it matches NBA chunk size. This is the least-supported rule (P3 is a fact, not a difference), so run it as an A/B, one Short, not a mass change.
4. **Do not open on a frozen frame (evidence P6, n too small).** Edit: when `visual_fx.py`/the cut uses a still, give shot 1 visible motion for its whole hold (use the seconds of the clip before the peak). Check S06 and S04 for the pattern. Only keep this rule if the next 3 Shorts show it.
5. **Name the payoff on screen by 0.35 s in one big line or word (evidence P7).** Competitors with 7 of 8 text at 0 to 0.35 s. We already put chunk 1 on at 0.0 s, so the edit is to make chunk 1 carry the strange noun, not a bare name or filler: SGA's chunk 1 was only the name ("SHAI GILGEOUS-ALEXANDER", 1.45 s on screen), Kerr's was "THIS IS", Chuck's was a bare name. Edit: rewrite chunk 1 to include the verb or the number ("SGA ENDED 141", "BARKLEY FAILED A TEST") so the first caption already states the strange thing. Note `script_lint.py` will want the same words as line 1 spoken.

Not a rule: "start the voice at 0.0 s" and "no title card in first 4 s". All 14 already do both and 8 of 8 competitors do too.

## 6. 10-second frame-1 checklist for the editor

Open the first 3 seconds, pause at frame 0, then 1.0, then 2.0 s.

1. Frame 0: say line 1 out loud. Does the picture show that thing happening (the play, the object, the person doing it)? If it's a face, is the face the thing (a kid crying)? If not, swap shot 1. (3 s)
2. Is the voice audible at 0.0 s and is caption chunk 1 on at 0.0 s? (1 s)
3. Does chunk 1 state something strange (a number, an odd verb, a named oddity), not just a bare name or "THIS IS"? (1 s)
4. Does shot 1 run 2.7 s or more? If you can see a cut at under 2 s in the first 3 s, move it. At most 2 shots in 3 s. (2 s)
5. Is there motion in shot 1 for its full length (no frozen frame)? (1 s)
6. Any other creator's logo, handle or broadcaster bug on frame 0-3 s (for example "/pivot/", NBC)? Crop or swap. (1 s)
7. Is anything a card or follow ask in the first 4 s? Must be none. (1 s)

## 7. What to measure next (so the next teardown has more than n=3)

- Pull the same retention at the 2%/3% points for the next 6 FC Shorts and compare drop to views again (P1 says the drop moves with views; if it doesn't, the hook is the cause).
- A/B rule 3 on one FC Short against a matched topic.
- Competitor retention is unknown to us; the competitor part of this doc is shape only [S].

Files: frames and contact sheets are in the session scratchpad only, not in the repo. Gemini report added: `Research Notes/Watch Reports/HVdbxbds7jU.json` (plus the index line the tool appends).
