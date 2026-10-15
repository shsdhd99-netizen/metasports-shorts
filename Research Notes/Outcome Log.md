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

## Daily check, Oct 13 2026 23:09 UTC run (free public numbers only)
516 subs (513 earlier today), 101 Shorts. Last 7 median 3,350 (old normal 21,500) -> trend DOWN.

| Short (newest first) | Public views | vs earlier today |
|---|---|---|
| #25 Did Bronny Actually Get Better (re-post, Oct 13) | 180 | 177 (too new; judge at 48 h) |
| #29 Why Won't Big Men Shoot Underhand | 1,200 | 1,029 |
| #20 Is Bad Boys Pistons Defense Illegal Now | 1,600 | 1,593 |
| #35 Why Did Wemby Train With A Rugby Team | 2,800 | 2,698 |
| #01 Why LeBron Took a 92% Pay Cut | 3,900 | 3,900 |
| #34 Are Three Of 2007's Top Four Picks Still Playing | 4,500 | 4,420 |
| #23 Why Is LeBron Playing Against His Son | 7,400 | 6,502 (still growing on day 2) |

Retention benchmarks (Studio, unchanged): Wemby 79.5% stayed / 100.3% AVD; Duren 63.0% / 59.7%. No new retention data: the vidIQ top_videos report was already pulled earlier today (Oct 13), so no second paid call.
Lesson: none added. n is under 3 for any new pattern; the only movement is #23 still climbing on day 2, which matches the "read at 48 h" rule already in place [V].

## Oct 14, 2026: pre-registered experiments and predictions (written BEFORE results)
Source of the scores: Creative System v3 rubric (`Production Queue.md`). The view guesses are mine. They are logged so the rubric can be checked against reality at 10 posts (Rules Audit D1). They are not targets.

| Short | Posted (UTC) | Version | Score v3 (/70) | 3-pt formula | 48 h guess (views) | 48 h actual | Avg % viewed | Notes |
|---|---|---|---|---|---|---|---|---|
| #39 Oldest triple-double | Oct 13 23:49 | plain | 46 | 3 (weak 1 and 3) | 4,000 | | | posted **without** Critic v2; post-mortem found wrong-game shots at 9.6-14.8 s and a blurry 3.8 s archive shot at 2.6 s. 2,181 views at 11 h |
| #40 Jokic pass | (owner) Oct 14 | **ring** | 63 | 3 | 5,000 (range 1.5K-20K) | | | experiment 1, ring half |
| #41 Taller than Wemby | (owner) Oct 15 | plain | 53 | 3 | 3,500 | | | experiment 1, plain half; re-check his status first |
| #21 Jokic record v3 | (owner) Oct 16 if the re-check passes | plain | 55 | 3 | 3,000 | | | 16.9 s: the first post under the new "length follows the story" rule |

**Experiments running:**
1. Ring vs plain (#40 vs #41, pair 1 of 3).
2. No card before 4 s (every new build).
3. **Posting rate: 1 a day Oct 14-19** vs the 2-a-day weeks (Oct 5-13 per-post median 2.8K). Read each post at 48 h from public counts (the daily routine logs them at 23:07 UTC) plus vidIQ avg % viewed when credits allow (70 left; renews Nov 5).

**Decision rule (set in advance):** change nothing on one pair. Adopt the ring only if it wins 2 of 3 pairs by 5+ points of avg % viewed AND has the higher 48 h views. Call 1-a-day better only if this week's per-post 48 h median beats 2.8K by 50%+.

## Oct 14, 2026 (later): music, footage and voice experiments, pre-registered (written BEFORE any result)
**What changed:** every ready Short now has a music version (Library/Music Guide.md); the owner picks per post. Log the version actually posted ("+ music" / "no music") in the table above.

**Confounding warning (read this before drawing any conclusion):** this week changes TWO things at once, posting rate (1 a day) and music. A week-level change in views can't be credited to either. Only within-pair comparisons that hold one of them fixed count.

| # | Hypothesis | Measure | Decision rule (set now) | Status |
|---|---|---|---|---|
| M1 | A quiet music bed does not hurt and may help avg % viewed | Avg % viewed and 48 h views: the next 6 posts with music vs the last 6 posts without (Oct 5-13), same rate where possible | Credit music only if the music posts' median avg % viewed is 5+ points higher AND the median 48 h views is higher. Otherwise keep music as house style (owner preference) without claiming a reach effect | open |
| M2 | The ring test stays valid only if #40 and #41 go up with the same audio | the version column above | If they differ (one with music, one without), pair 1 is void and doesn't count toward the 3 pairs | open |
| Q1 | A concrete question hook ("Why would X do Y?") keeps more viewers in the first 3 s than a statement hook on a comparable topic | The audience-retention ratio at 3 s (vidIQ) | 3 pairs, alternating hook form on comparable topics. Adopt questions only if they win 2 of 3 by 5+ points. Old hits used questions 3/4, new posts 0/20; our two best new Shorts were statements | open |
| P1 | One cut-in 0.3-0.4 s silence before the final line (music out too) improves the ending (rewatch/loop) | Avg % viewed (over 100% = rewatches) on Shorts that have it vs comparable ones that don't | 3 Shorts with it vs 3 matched without. Adopt only with a 5+ point gap. One old hit used it (Bronny "...son."): n=1 | open |
| S1 | Keeping the broadcast scorebug and circling the number when it's named (instead of our own card) holds viewers at least as well | Retention-curve dip at the proof moment vs card moments in other Shorts | Descriptive only for now (n small); revisit at 6 Shorts | open |

**Not hypotheses (just facts to keep):**
- #41 v3 swapped an agency photo for broadcast footage. That was a licensing fix, not a retention test.
- All the music-version "improvements" are craft changes. No claim about views is made unless a row above shows it.

## Oct 14, 2026 (night): the formula freeze and the voice change (written BEFORE any result)
**Owner's brief:** stop running many experiments at once. So from now on:
- **One A/B test at a time.**
- **Everything else is house style.** It is logged, not "tested".

| # | Item | Status | How it's read |
|---|---|---|---|
| E1 | Ring vs plain (pair 1: #40 vs #41) | **the one running test.** Finish pair 1 only if both go up with the same voice and the same music setting (M2) | as above |
| V1 | **House voice → Alex** (if the owner approves it on the Sound Check page). A house change, not a test | log the voice in the version column ("Alex" / "clone") | Descriptive: the first 6 Alex posts vs the last 6 clone posts, on avg % viewed and 48 h views. **Confounded** with posting rate, music and topic, so it can only flag a big drop (10+ points of avg % viewed), not prove a gain |
| R1 | "Story voice" scripts (a turn such as "But the craziest part…", one aside, a reframe or feeling ending) vs fact chains | **Adopted as house style** (Winning Formula, supported by multiple examples: our old hits, Curry, Giannis, CoachClank) | Descriptive only |
| R2 | Reframe ending ("The question isn't X, it's Y") | Parked: use it when the story supports it, not as a test | — |
| Q1, P1 | Question hooks; the cut-in pause | **Parked.** Statements are the default (11/12 old voiced Shorts, Curry, Giannis); the pause stays an editing option | — |
| M1, S1 | Music cohort; scorebug-as-proof | House style; read descriptively at 6 posts | as above |

**Voice facts for the record:**
- Old voice: about 259-267 wpm on our scripts.
- Alex: 220-229 wpm.
- The v4 renders of #40, #41 and #21 run 23-24 s (old: 16.8-21.3 s).
- If an Alex post is read against an old-voice post, length differs too. Say so in any comparison.

## Oct 14, 2026 (late night): first results and the next posts (written before the next results)
| Short | Posted | Version | Old rubric | Critic v3 | 48 h guess | Notes |
|---|---|---|---|---|---|---|
| #40 Jokic pass | Oct 14 (owner) | ring, old voice, v2 (21 s) | 63 | 28 REJECT | (was 5,000) | **655 views and 29 likes at under a day.** Read at 48 h and 7 days |
| #41 Taller than Wemby | Oct 14 (owner) | old voice | 53 | 30 REJECT | (was 3,500) | 1,600 at under a day |
| #21 v5 | not yet | A or F (owner's pick), no music | — | 39 APPROVE | 6,000 | rewritten |
| #36 v2 | not yet | A or F, no music | — | 38 APPROVE | 8,000 | rewritten; needs the owner's OK on fan-account clips |

**What gets checked at 10 posts:**
- Critic v3 total vs 48 h views (Spearman). If it's under 0.3, revise the critic's anchors.
- Music is off by default from now on. The music cohort (M1) is closed: no bed is the house style.

## Daily check, Oct 14, 2026, 23:50 UTC (free public numbers only; routine "MetaSports daily stats check")
`channel_check.py`: 520 subscribers, 104 Shorts. **Median of the last 7: 2,950** (the channel's earlier normal: 13,350). Trend: down.

| Short | Views |
|---|---|
| Why Is LeBron Playing Against His Son? (#23) | 9,800 |
| Are Three Of 2007's Top Four Picks Still Playing? (#34) | 5,100 |
| How Old Is The Oldest Triple-Double Ever? (#39, about 24 h) | 4,200 |
| Is Anyone Taller Than Wemby? (#41, under 1 day) | 1,700 |
| Why Won't Big Men Shoot Underhand? (#29) | 1,600 |
| Why Jokic's Best Pass Doesn't Count (#40, under 1 day) | 752 |
| Did Bronny Actually Get Better (repost) | 194 |

**Retention:** there are no new retention numbers.
- The only ones on file are from the owner's screenshots: Wembanyama 79.5% stayed / 100.3% average view duration; Duren 63.0% / 59.7%.
- vidIQ has 5 credits, under the 10 needed, so I skipped it.
- Metricool's per-video data is still empty.

**Lesson:** none new. #40 and #41 are under 48 h old, and n<3, so no rule changes.
- It is consistent with tonight's audit §12: the technicality (#40) is last among the new posts so far.

## Oct 15, 2026: YouTube Studio export read (Sep 16 to Oct 14; owner upload)
- **Window totals:** 141,000 views, 76,347 engaged, stayed to watch 72.9%, average % viewed 100.4, 51 subscribers, 89% new viewers.
- **The main finding:** stayed to watch tracks views at +0.77 (n=20). Full table: `Research Notes/Posted Video Audit (Oct 14, 2026).md` §13. Merged per-video file: `Research Notes/Posted Shorts - metrics (Oct 15, 2026, with Studio export).csv` (the Oct 14 file is kept as it was).
- **#40 and #41 are not in the export** (posted Oct 14, after the window). Their 48 h and 7-day reads still need Studio or Metricool.

**Pre-registered for the next posts** (written before any result):
- **Hypothesis:** a first line that passes the new hook check (an absolute, curious claim about a famous name) gets **70%+ stayed**.
- **Check at 5 posts:** stayed % for posts whose line 1 passes vs posts flagged by `script_lint.py`.
- **Not a test of:** voice or music. One variable at a time stays the rule.
- **Ask:** export the same Studio "Content" table again at each check (Advanced mode, Shorts, the last 28 days). It has stayed to watch, which neither Metricool nor vidIQ gives us.
