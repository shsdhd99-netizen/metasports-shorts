# Deep-dive case study: MetaSports (NBA + FC), Nov 6, 2026 night
Builds on `Case Study - MetaSports NBA (Nov 5, 2026).md` and `Case Study - MetaSports FC (Nov 5, 2026).md` (read those for competitors and monthly history). This file adds: what changed in 48 hours, the monetization math with the new YouTube rule, an operations audit of how Shorts are made and gated, scenario planning, risks, and a ranked action list.
Tiers: **[V]** measured by us (YouTube Analytics API, our logs) or stated by YouTube; **[P]** press or secondary source; **[S]** small sample; **[H]** my judgement. Data: weekly review written Nov 6 from the API files of Nov 5-6, `Test Log.csv` lane states, `queue_rank.py` and `qa_final.py` runs today.

## 1. The verdict in eight lines
1. **Reach is working; monetization is not close.** NBA 7-day average is 23.9K views a day, up 108% on the prior 28 days; FC is flat at 9.6K a day. [V]
2. **YouTube raised the bar for new applicants on Feb 1, 2027:** 20M Shorts views in 90 days (or 8,000 watch hours) plus 1,000 subs, versus 10M today; existing members keep 10M [P: ppc.land, newscaststudio, Aug 2026 reporting of YouTube's Aug 10 announcement; confirm on YouTube's Help Center]. Our channels are not partners, so the 20M line is the realistic target date risk. NBA needs 222K views a day (9.3x now); FC needs 23x. [V math]
3. **The reachable milestone is the lower tier (500 subs + 3M Shorts views in 90 days, fan funding, no ad money).** NBA needs 33K a day (1.4x now): 6-12 weeks at the current trend. FC needs 3.5x. [V math, P rules]
4. **What drives views is the subject, not the edit.** Moment and family stories carry NBA; goalkeeper-odd-device carries FC (6 of 6 above 10K, median 18K, PROVEN). Rules, history, records and lists sit below the channel median. [V/S]
5. **The factory has a quality-control gap at the last step.** All five Shorts I ran through the new final QA failed (HOLD): placeholder or missing titles, no QA line, no covers, too few tags, missing source clips. Four of those were already "built" and queued. A cheap final gate was missing. Fixed today (`qa_final.py`, `queue_rank.py`). [V]
6. **Two public incidents in two days came from the same gap:** S27 and S28 uploaded with the title "unknown", which forced delete-and-reupload. Guard rails now stop empty titles, second uploads and duplicates. [V]
7. **Concentration risk:** a few Shorts carry the channel (FC: top 5 = 84% of views; NBA top 10 = 60%). One wrong move on idea supply, and views fall back to the Mar-Sep 2026 floor (under 2K a month), which already happened once. [V]
8. **The bigger asset is the system, not YPP income.** Even if the 20M line is missed, the pipeline (research, gates, QA, scheduling, analytics) is a transferable portfolio piece for an AI-and-business student; see section 9.

## 2. What changed since Nov 5 (the 48 hours)
- **Built:** `qa_portions.py` (QA by stage), `qa_final.py` (SHIP/FIX/HOLD), `queue_rank.py` (score and slot waiting Shorts), `pin_helper.py`, `weekly_review.py`, `acct.py` (3 accounts, 1 terminal), `reel_read.py`/`reel_watch.py` (research from saved reels), edit access to both channels (YouTube `youtube` scope, tokens only on the PC).
- **Rewritten:** `daily-run` skill 243 to about 90 lines, old rules archived in `Rule History - daily-run skill before Nov 6 rewrite.md`.
- **Replaced/fixed:** S27 and S28 re-uploaded with real titles; #92 and S30 scheduled for 7:30 PM; five held Shorts' cards repaired by a background agent (3 now FIX, 2 HOLD).
- **Decided (owner):** selective autopilot Nov 9 to 22 (only ideas rated 10 of 12), never more than 3 posts a day per channel, 6 hours apart, skipping beats a weak Short.

## 3. Numbers now (API files Nov 5-6) [V]
| | NBA (MetaSports Clips) | FC (MetaSports FC) |
|---|---|---|
| Subscribers | 634 | 151 |
| Views a day (7-day avg) | 23,851 (28-day prior avg 11,452) | 9,565 (prior 28-day 9,290) |
| Shorts views, last 90 days | 488,299 | 120,771 |
| Median views, Shorts aged 3-14 d | 7,434 (n=18) | 3,113 (n=13) |
| Subs gained, last 28 days | 176 (6.3 a day) | 162 (5.8 a day) |
| Subs per 1K views | 0.43 | 1.36 |
| Top Shorts (3-14 d) | Why NBA Players Refuse This Free Throw 29.2K; Bronny Is Shooting 100% 28.5K; Cameron Boozer Outshot His Dad's Whole Career 27.2K | Goalkeepers hid a cheat sheet on a water bottle 29.2K; goalkeepers subbed on for penalties 23.5K (36 subs); goalkeepers danced on the line 15.6K |
| Bottom Shorts | Luka Did What Kobe Never Did 1.3K; All Three Williamses Got A Technical 1.5K; Caitlin Clark 2.8K | Players sent off in their last game 2.0K; Barcelona paid a fortune 1.1K; Messi paper napkin 1.0K |
Notable: average % viewed above 100% on several NBA hits (looping Shorts rewatch), and the best FC subscriber event (36 subs) came from the "subbed on for penalties" Short, not the highest-view one.

## 4. Funnel and unit economics [V/H]
- NBA: a typical Short returns about 7.4K views and about 3 subs. A hit (28K) returns about 12 subs. So **one hit is worth about 4 typical Shorts for subscribers, and about 4x for views**: the system's job is to find hits more often, not to make more typical Shorts.
- FC: 1.36 subs per 1K views means a 25K-view goalkeeper Short is worth 30+ subs, roughly 3x NBA per view. FC is the better subscriber engine; NBA is the better view engine. [V]
- Production cost per Short: ElevenLabs credits (67K characters left until Nov 19 at last count) plus 1-3 hours of agent time. Credits cap the volume near 2-3 Shorts a day across both channels. [V from owner notes]
- Cost of a bad Short is not the credits: it is a slot and, on FC, the channel's audience signal (club-story Shorts under 2K views). [S]

## 5. Monetization scenarios (math in section 3)
Required daily views (90-day window): lower tier 3M = 33,333 a day; YPP today 10M = 111,111; new-applicant YPP after Feb 1 2027 = 222,222.
NBA views over the next 13 weeks from 23.9K a day with weekly growth: 0% = 2.17M, 5% = 2.96M, 10% = 4.09M. So the **lower tier is reachable if growth keeps 5% a week** (about 3M) and only just; 10M needs about 3x more growth than the best case modelled. FC is 3.5x short of the lower tier at the current level.
Subs: NBA 634 to 1,000 in about 58 days at 6.3 a day; FC 151 to 500 in about 60 days, to 1,000 in about 146 days.
Reading: **do not plan around ad income from these channels in 2027.** Plan around (a) the lower tier as a first milestone, (b) a long-form or non-Shorts path if ad income is wanted, (c) brand and skill value.
Policy risk to keep in mind [P, verify at YouTube Help "Inauthentic content" and "Reused content"]: YouTube's July 2025 rename ("repetitious" to "inauthentic content") did not change the reused-content rules for clips, but monetization can be removed for a whole channel that looks mass-produced or unoriginal. Our defence: official footage, a fact the clip cannot show, a human-decided premise, and varied scripts. AI voice itself is not the target; templated, mass-produced output is. Keep the "one new fact per Short" rule.

## 6. Operations audit: how Shorts are made [V]
Pipeline: research (cloud, 3:43 AM) > gate (`idea_gauge` 80%+, FRESH `copy_check`, open slot, proven lane or one logged variable) > script and sources > voice (ElevenLabs) > footage > cut > render > QA > card > schedule (private + publishAt) > pin comment (manual) > 72-hour judgement > lessons.
Findings:
1. **Upstream gates are strong; the downstream gate was weak.** The gauge and build gate stop bad ideas; nothing stopped incomplete paperwork. `qa_final.py` now combines portion QA, the retention gate and file checks; `queue_rank.py` reads it so a failed Short can never take a slot.
2. **Evidence on the gauge is thin.** Lane rows are mostly n<5 and flagged "guess"; weights in `queue_rank.py` are judgement. Treat rankings as a filter, recalibrate after each 72-hour read. [H]
3. **Footage is the recurring technical debt:** 180+ "blown-up archive frame" warnings, missing `src/` clips on other clones, reuse warnings. A shared footage library or a check that downloads sources into the folder would remove a whole class of late failures. [V]
4. **Manual steps left:** pinning comments (no API), Studio export for "stayed to watch", account sign-ins. The to-do list tracks them.
5. **Single points of failure:** the PC (wake tasks, Brave extension), one ElevenLabs plan, the OAuth app (now "In production" so refresh tokens will not expire after 7 days), the cloud environment lacking YouTube keys (cloud runs are research-only).
6. **Team protocol (A1/A2/A3/CLOUD)** works on paper; only A1 and account 2 are logged in on this PC today, account 3 pending. Claims and handoffs prevent double builds. [V]

## 7. Lane scorecard (Test Log, n = attempts) [V/S]
NBA (channel median 6.8K): size 15.9K (n=2), moment 9.3K (n=6), family 8.8K (n=8), oddity 4.5K (4), news 3.8K (4), business 3.4K (4), rule 2.8K (13), superlative 2.8K (13), history 2.4K (8). All "TESTING"; none PROVEN yet. Two lanes with 13 attempts each sit at 2.8K: that is 26 Shorts at 40% of median; the rest of the evidence says stop making them except as one-variable tests.
FC (median 2.5K): goalkeeper trick 18.2K (n=6, PROVEN); club story 2.0K (7); manager 2.7K (2); player record 2.1K (1).

## 8. Risks, ranked
1. Idea supply for the proven FC premise (each Short needs a genuinely new odd goalkeeper fact).
2. Concentration: hits carry the channel; a flat month returns it to the 2K-a-month floor.
3. Policy: reused or templated content flags (above).
4. Process: another placeholder-title style incident (now guarded) or an over-long script (S16 is about 62 s; Shorts must end before 59.5 s here).
5. Dependence on one PC and the owner's availability for manual steps.
6. Data: "stayed to watch" exists only in Studio exports; the first export for the autopilot test is due Mon Nov 9.

## 9. What I recommend, in order
1. **Judge, don't guess:** after the Nov 9-22 selective autopilot, compare 72-hour median views of scheduled Shorts to the channel medians (NBA 6.8K, FC 2.5K) and count hits (15K+). Success = more hits per slot, not more slots filled. [owner-approved metric]
2. **Make NBA hits repeatable:** family and moment stories only, plus the star record chases; log subject, line 1 and footage type for every Short. Retire rules/history/records except as one-variable tests.
3. **Make FC a second engine on goalkeepers, then test one new lane at a time:** the bargain-scouting money-gap lane (S39 Leicester) from the xeysfc study, with 2 sources per fee.
4. **Fix the footage problem once:** store the downloaded source in each Short's folder at build time and have `qa_final.py` fail on missing `src/`.
5. **Add a long-form or newsletter path only if the owner wants ad income:** Shorts-only ad income needs 10-20M views per 90 days.
6. **Use the system as a portfolio:** write a one-page "what I built" (research gate, QA by stage, ranking, autopilot test, results) for the Common App activities and the essay. It is real data, real iteration, and an honest account of what did not work.
7. **Weekly:** `weekly_review.py` each Sunday; update this file monthly.

## 10. Open questions / data gaps
- Studio "stayed to watch" for both channels (Mon Nov 9).
- 72-hour results for the Nov 6 evening test Shorts (#92 Lendeborg, S30 Kane) and the replacement S27/S28.
- Whether the Feb 1, 2027 rule text matches the press summary (check YouTube Help directly).
- Whether the cloud environment can get the YouTube keys (cloud currently research-only).
- Account 3 login and the real weekly usage percentage per account (the PC meter only counts local transcripts).
