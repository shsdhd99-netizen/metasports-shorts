# Outcome log (fill from YouTube Studio 24 h and 7 d after posting)
Purpose: test whether our gate metrics predict results. One row per posted Short. Paste Studio numbers from the user.

| Short | Posted (date/time ET) | Lane | Title opener | Avg shot (s) | Length (s) | Caption style | Hook text | Music | Viewed % (24 h) | Avg % viewed | Views 48 h | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #12 Duren (v2) | Oct 3-4 | contract | Did | 1.9 | 33 | metasports | no | no | 63.0% (stayed) | 59.7% | 1.5K (5 h 27 min), rank 8 of 10 | 38 likes. User's Studio screenshots, Oct 4 ~12:30 |
| #03 Wembanyama (How Did Nobody Vote Against Wemby) | Oct 3-4 | rule/record oddity | How | n/a (Claude v3 cut) | 24 | clank-style | no | no | 79.5% (stayed) | 100.3% | 20.6K (9 h 52 min), rank 2 of 10 | 413 likes, subs +11 and up; comments are about the name spelling |

## Read of the first two results (Oct 4; n=2, early, topics differ, so a pattern not a proof)
- Wemby 24 s beat Duren 33 s on every metric: stayed-to-watch 79.5% vs 63.0%, avg % viewed 100.3% vs 59.7%, ~14x the views per hour.
- Wemby script: universal rule hook ('Every Defensive Player of the Year ... had at least one voter who picked somebody else'), 'Until Wembanyama', 'but that's not even the crazy part', a 3-name list payoff ('That's the whole list'), ends on the payoff, NOT a question. Duren: contract story with a $ gap and a 'did he lose?' question.
- Matches Round 5 lane data (rule/record oddity strong, contract flat). Does NOT support 'longer is better' for us: the shorter Short did better. Retention curves not yet processed (up to 2 days).

| #18 LeBron helicopter | Oct 4 | funny/petty | LeBron | 1.2 | 26.8 | metasports | yes | no | ? | ? | 9 views in first 59 min (rank 8 of 10), Wemby now ~18K | posted by user; read at 24 h |

## Public views snapshot, Oct 5 2026 (free check: `python3 Tools/channel_check.py @MetaSportsClips`, via yt-dlp; views only, no retention)
| Short | Views | Note |
|---|---|---|
| Why Two Men Can Still Wear Six (#22 rebuilt: payoff ending, corrected "two") | ~29,000 | best of last 7 within about a day; first Short built to the new payoff standard |
| This NBA Player Sleeps On The FLOOR? (Steven Adams) | ~28,000 | real-voice Adams quote Short |
| How Did Nobody Vote Against Wemby? | ~26,000 | the benchmark (79.5% stayed / 100.3% AVD) |
| Did Jalen Duren Just Leave $87 Million? | ~2,600 | contract lane, question ending |
| LeBron Left Sixers Practice By Helicopter (#18) | ~2,400 | |
| The NBA Final That Does Not Count | ~249 | |
| Would Jordan's Last Shot Be a Foul Now? | ~7 | |
Reading (HYPOTHESIS, n small, views not retention): surprise-fact / rule-oddity Shorts with a payoff ending and real voices (Wemby, #22, Adams) land 26-29K; contract lane (Duren) and the LeBron helicopter story sit near 2.5K. Matches Round 5 lane rule. Get avg % viewed from Studio screenshots or vidIQ before changing any rule.

## Studio retention, Oct 5 ~9:32 (user screenshots, lifetime; Wemby at ~42 h)
| Short | Length | Stayed to watch | Swiped away | Avg view duration | Views | Notes |
|---|---|---|---|---|---|---|
| Wembanyama (How Did Nobody Vote Against Wemby) | 24 s | 80.1% | 19.9% | 0:24 (104.1%) | 26.8K at 42 h ('about the same as usual', usual range 18.2-31.2K), +15 subs | curve: steady slow decline from 100%, ends near 75%, loops past 100% AVD |
| Duren (Did Jalen Duren Just Leave $87 Million) | 32 s | 68.7% | 31.3% | 0:22 (68.4%) | ~2.6K | curve: sharp cliff at ~0:08-0:10 (down to about 60%), then slow decline to ~33% at the end |
Read (SUPPORTED, n=2): Duren's cliff lands where the hook ends and the exposition starts (about 8-10 s); Wemby has no cliff because every beat adds a new fact. Contract exposition = the cliff. Rule for new Shorts: no flat explanatory stretch after the hook; the first turn must land by ~6-8 s. The user now posts 2 per day (Oct 5); queue regrouped into pairs.

## Channel check, Oct 13 2026 (free public numbers + ONE vidIQ top_videos call, 5 credits; the daily routine's 7 missed runs from Oct 6-12 could not be recovered, the session was idle)
Channel: 513 subs (was 486 on Oct 5), 101 Shorts (was 86, so 15 new posts since Oct 5). Last 7 median 3,250 views vs the old normal 21,500 -> trend DOWN (logged in Tools/data/channel_log.csv).

| Short (posted order, newest first) | Public views Oct 13 | Avg % viewed | Avg view dur | Likes | Note |
|---|---|---|---|---|---|
| #25 Did Bronny Actually Get Better (2nd post, Oct 13) | 177 | not yet | | 4 | same title as the Oct 6 post; judge at 48 h |
| #29 Why Won't Big Men Shoot Underhand (Oct 12) | 1,029 | not yet | | 9 | old underhand topic did 73K; this one 1.0K |
| #34 Are Three Of 2007's Top Four Picks Still Playing (Oct 12) | 4,420 | not yet | | 54 | |
| #23 Why Is LeBron Playing Against His Son (Oct 11) | 6,502 | not yet | | 220 | best like rate (3.4%) and best of the batch after Flagg/#17; was on HOLD in our plan, the user posted it |
| #20 Is Bad Boys Pistons Defense Illegal Now (Oct 10) | 1,593 | 65.8% | 17 s | 14 | lowest retention |
| #35 Why Did Wemby Train With A Rugby Team (Oct 9) | 2,698 | 76.3% | 19 s | 42 | |
| #01 Why LeBron Took a 92% Pay Cut (~Oct 8-9) | 3,900 | 103.0% | 24 s | | |
| #17 Did The NBA Just BAN Flopping (~Oct 8-9) | 6,700 | 81.7% | 23 s | | |
| #13 How Many Picks Did Kawhi Cost (Oct 8) | 1,881 | 93.9% | 21 s | 38 | |
| #14 Did The NBA Call Out Four Stars (Oct 7) | 1,615 | 116.1% | 27 s | 24 | highest retention, low views |
| #16 Why Giannis Faces The Bucks In Vice City (~Oct 6-7) | 2,870 | 80.3% | 20 s | | |
| #25 Did Bronny Actually Get Better (Oct 6) | 1,948 | 68.4% | 17 s | 62 | |
| #19 How Tall Is Cooper Flagg Really (Oct 6) | 20,391 | 103.0% | 22 s | 230 | the only one of the 15 near the old normal |
| #15 Why Steven Adams Fears GTA 6 In November (Oct 6) | 5,974 | 95.0% | 21 s | 113 | |
| #24 Is Bronny's Spot Really Safe (~Oct 5-6) | 5,745 | 97.1% | 28 s | | |
Older posts in the same vidIQ window (avg % viewed / views): #22 Two Men Wear Six 115.6% / 31.8K (AVD 30 s); #03 Wemby vote 104.0% / 27.0K; #12 Duren 71.1% / 2.9K; #18 helicopter 89.8% / 2.7K; "The NBA Final That Does Not Count" 72.7% / 2.3K. (vidIQ avg % is lifetime in the window Sep 20-Oct 13 and lags the public count by about a day, so the four newest posts have no retention yet. Exact upload hours are not public; yt-dlp is bot-blocked for some videos today.)

Reads (evidence tiers; n is small, so these are NOT rule changes):
- PROVEN (public numbers): the 15 Shorts posted Oct 5-13 have a median of ~2.8K views (range 177-20.4K). Wemby and #22 did 26-31K on Oct 3-5, before this batch. Only #19 Flagg reached the old normal.
- SUPPORTED (n=16 with retention): avg % viewed of 100%+ appears in all 3 Shorts above 19K views (#22, #03, #19); all 11 Shorts under 100% stayed under 6.1K. But 2 of the 5 Shorts at 100%+ (#14 116%, #01 103%) stayed under 3.4K, so looping retention looks necessary for a breakout but not sufficient: the other half is the first-second swipe decision (topic, first frame, title), which vidIQ does not show.
- SUPPORTED (n=5): every Short under 77% avg viewed got under 3K (#20 65.8%, #25 68.4%, #12 71.1%, NBA Final 72.7%, #35 76.3%).
- HYPOTHESIS (n=1 each): breakouts so far were a rule oddity (#22 six, #03 Wemby vote) and a famous-prospect curiosity with one checkable fact (#19 Flagg's height). Bronny/LeBron Shorts sit mid-tier (5.7-6.5K). Contract/trade (#12 2.9K, #13 1.9K) stays low, matching Round 5. The 'rule' lane alone does not predict (rule Shorts ran 1.0K to 31.8K). Re-doing an old winner topic by name (underhand, 73K before) did not carry over (1.0K).
- Open: whether 2 posts a day splits reach (needs post times from Studio; not public), whether the Oct 13 'Bronny Get Better' re-post is a changed cut, and whether any of #20 / #29 has a Studio copyright claim (channel_check flags them, but its FLOP rule is relative to the old 21.5K median, so it is noisy now).
- Resources after this check: vidIQ 145 of 150 credits (renews Nov 5); ElevenLabs 1,032 of 52,087 characters used this cycle (plan: starter).

## Oct 13 (later): verified details behind the posted files (handoff audit)
- The posted files are our exports: public durations match local finals (e.g. #19 22 s vs 21.9 s, #23 27 vs 26.7, #29 23 vs 23.23). [V]
- #19 went up as the PREMISE-LINE version (thumbnail shows the "Flagg: 6-8 to 6-11?" pill); #17 went up with CoachClank-style captions. [V, YouTube thumbnails]. So the planned tests ran, but each is n=1 and confounded by topic: premise line #19 20.4K vs #20 1.6K; clank captions #17 6.7K vs house captions #14 1.6K. No rule change.
- Titles changed outside our packages: #17 "Did The NBA Just BAN Flopping? 😳" (misstates our fact sheet: flopping has been a technical since 2023-24) and #20 "Is Bad Boys Pistons Defense Illegal Now 😳?". [V]
- The Oct 13 #25 re-post is the identical file (same duration, same auto-thumbnail) — 177 views in ~6 h. [V]
- Correction to the Oct 5 snapshot above: "This NBA Player Sleeps On The FLOOR?" (28K) is a Feb 2026 upload, not a new result. [V, Winning Formula v2]
- Rating calibration: the Round 3 critic craft score vs views, Spearman −0.63 (n=14): the critic ranking must not set posting order. [V]
- Views plateau after ~2 days (#22 29K→31.8K, #03 26K→27K from Oct 5 to Oct 13), so 48 h is a fair read point. [V]
