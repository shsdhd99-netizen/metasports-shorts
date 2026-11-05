# Case study: MetaSports Clips (NBA Shorts), Nov 5, 2026

Owner's ask (Nov 5): "review how our channels are doing, how they can do better, how close we are to monetization, and how we're doing vs competitors. A full case study on both channels." This is the NBA channel; the soccer channel has its own file (`Case Study - MetaSports FC (Nov 5, 2026).md`). The index of every study and rule is `Master Index - Studies and Rules (Nov 5, 2026).md`.

Evidence tiers: **[V]** measured by us or stated by YouTube; **[S]** small sample or seen on other channels; **[H]** a guess to test. Data pulled today: YouTube Analytics API (read-only, both channels), `yt-dlp` public counts for 16 channels, YouTube's own eligibility page (support.google.com/youtube/answer/72851) and our Oct 23-24 monetization notes. Reproduce with `Tools/channel_totals.py`, `Tools/yt_analytics.py daily`, `Tools/learn.py report`.

## 1. The answer in six lines
1. **Growing, from a restart.** Views per day: 28-day average 14.9K, 14-day 18.6K, **7-day 23.9K** (up 60% in a month). Subscribers 634. The channel earned 292K-802K Shorts views a month in Nov 2025-Feb 2026, then fell to about 500 a month for seven months (Mar-Sep), and was restarted in October: 434K in Oct, 53K in the first 4 days of Nov. [V, API]
2. **A typical Short gets about 7K views; hits get 24-29K.** Median of 40 mature Shorts: 6,516 (API) to 7,250 (public, last 30). 7 of 40 reached 20K+; 12 of 40 reached 10K+; 16 of 40 stayed under 5K. The top 10 Shorts carry 60% of all views. [V]
3. **Monetization is far away.** The Shorts route needs 1,000 subscribers and 10M qualified Shorts views in 90 days (and 20M for new applicants after Feb 1, 2027). We have 634 subs and 488K public Shorts views in the last 90 days: **4.9% of the 10M line, 2.4% of the 20M line**, before the engaged-views haircut (about 54% of public views count). [V]
4. **The closest real milestone is the lower tier** (500 subs, 3 public uploads in 90 days, 3M Shorts views in 90 days: fan funding, no ad money). We pass the subs and uploads; views are 16% of the way (needs 33K a day, we do 24K). **At our recent growth that is about 2-4 months; it is the first thing to aim for.** [V rules, H timing]
5. **Against competitors we are about 8-40x smaller per Short.** Our median is 7.3K; the narrated-story peers sit at 54K-300K, and even the smallest of them (21.7K subs) gets 54K a Short. [V]
6. **What separates our hits from our misses is the subject, not the edit** (family, a watchable curiosity, a live star record chase vs rules, history, trivia). That is also the lever with the most room. [S, n small but consistent across 3 studies]

## 2. Where we are (numbers)
| Measure | Value | Source |
|---|---|---|
| Subscribers | 634 (+176 in 28 days, 8 lost; 0.43 subs per 1K views) | yt-dlp Nov 5; API |
| Shorts on the channel | 140 | public |
| Shorts views, last 90 days | **488,275** (watch hours 1,845) | API, `creatorContentType==shorts` |
| Shorts views, last 365 days | 2,710,180 (watch hours 9,522), almost all of it Nov 2025-Feb 2026 | API |
| Long-form views / watch hours, last 365 days | none (the channel is Shorts-only) | API |
| Views per day, 7 / 14 / 28 day average | 23,851 / 18,589 / 14,927 | API daily |
| Median public views, newest 30 Shorts | 7,250 (mean 9,660, max 29,000, min 1,000) | yt-dlp |
| Engaged-view ratio (median, 39 Shorts) | 0.55; 10 of 39 under 0.50 (a likely swipe-away problem) | API |
| Subs per 1K views | 0.43 | API |
| Median length | 23.5 s | API |

Monthly Shorts views (API): Nov 2025 292K, Dec 534K, Jan 802K, Feb 591K, Mar-Sep under 2K a month, **Oct 434K**, Nov (4 days) 53K. The earlier era was driven by "watchable curiosity" Shorts ("NBA Players Are Doing THIS" 80K, "Why NBA Players Stopped Shooting Underhand" 73K); see `Topic and Script Reset (Nov 2026).md`.

## 3. What is working (and the evidence)
- **Family stories** (Bronny, the Boozers, LeBron vs his son): median 25.0K, 3.7x the channel, 4 of 4 above the median [S, n=4].
- **A watchable curiosity or moment you can see** ("Why NBA Players Refuse This Free Throw" 29K, "This Kid Felt Every Free Throw" 24K, Bones Hyland's fake-throw technical 12.7K, the rookie's overtime 10.9K): median 7.7K and the recent hits [S, n=5 plus one rule-shaped exception].
- **Live record chases with a star** ("Who Has Missed The Most Shots/Threes In NBA History" 25.6K and 23.9K) [S].
- **Line 1 of 11 words or fewer** (8.0K vs 3.4K median, n=18 vs 6) and **voice 22 s or less for a moment** (10.0K vs 3.1K, n=8 vs 16) [V small]; the first 1-3 seconds decide the Short, and 15 of 16 retention curves drop hardest in the first 4 s [V]. Edit style matters little: the better and worse halves of six competitors edit alike [S, n=128].
- **Frame 1 shows the thing line 1 is about; no cards; footage big and moving; 10-15 shots** [S/V, `Full Review for Retention (Nov 2026).md`].
- **Official footage and a fact the clip can't show** satisfy YouTube's originality rule [V official].

## 4. What is not working
- **Paused shapes keep getting built.** Rule (why X isn't allowed) median 3.8K (0.56x), history 3.5K (6 of 6 under the median), news explainers 4.3K. Three of this week's scheduled Shorts (Jokic Taco Bell, Warriors shot-clock first, Rodman No. 69) are in those shapes. [S]
- **Subs per view is low** (0.43 per 1K vs 1.36 for FC). NBA explainers earn views but not follows; FC's story format converts about 3x better. [V]
- **Concentration:** 60% of views come from 10 Shorts, so one more hit moves the channel more than ten more average posts. [V]
- **Low engaged ratio on 10 of 39 Shorts** (under 0.50, likely under 60% stayed); those are mostly the history/rule/trivia shapes. [S]
- **Late news loses**: late-news Shorts median 2.7K vs 8.5K evergreen (n=2 vs 6) and #63 held 58% a day late vs 75-80% same day. #95 (Lendeborg, a Nov 1 game) is therefore a risk; judge it at 72 h. [S]
- **Data gaps:** "Stayed to watch" is Studio-only and the NBA Studio account is not signed in here, so the 74% line is checked only on the API stand-in. [V gap]
- **Voice and format sameness**: an AI narrator over highlight footage is what every narrated-story peer does; nothing about the format is ours. [H]

## 5. How close are we to monetization
Official lines (YouTube Help, read Nov 5; our Oct 23-24 notes add the Aug 2026 YouTube Blog details):

| Step | Needs | Us (NBA) | Gap |
|---|---|---|---|
| Lower tier (expanded YPP, fan funding only, no ad money) | 500 subs + 3 public uploads in 90 days + 3M Shorts views in 90 days [S: Expanded YPP page, YouTube Blog Aug 2026; the page I fetched today links but does not list these numbers] | 634 subs, daily uploads, 488K views | views: 6x; needs 33K/day |
| Full YPP, ads and Premium (today's bar) | 1,000 subs + 10M qualified Shorts views in 90 days, or 4,000 public long-form watch hours in 12 months [V, official page] | 634 subs, 488K (4.9%), no long-form | subs: +366; views: 20x; needs 111K/day |
| Full YPP for **new applicants from Feb 1, 2027** | 1,000 subs + **20M** Shorts views in 90 days, or 8,000 watch hours [V, YouTube Blog Aug 10 2026, per our Oct 23 note] | | 41x; needs 222K/day |
| **Shorts pay floor from Feb 1, 2027** | 10M qualified Shorts views per rolling 90 days to be paid from the Shorts pool [V, same] | | |
| Other | no active strikes, AdSense, 2-step verification, accept the new terms in Studio by Jan 31, 2027 | | |

**Counts use engaged/qualified views, not the public counter** (about 54% of public on this channel), so the real distance is about double what the public numbers show. [V ratio, Oct note]

**Projection** (daily views grow by a steady factor each 30 days; the 90-day total must reach the line; start from the 7-day average 23.9K, a 14.9K start gives about 1.3x longer):

| Monthly growth | 3M in 90 days (lower tier) | 10M in 90 days (full YPP) |
|---|---|---|
| none (stay at 24K/day) | never (2.2M) | never |
| +15% | about 115 days (early Mar 2027) | about 374 days |
| +30% | about 90 days (early Feb 2027) | about 218 days (mid-June 2027) |
| +50% | about 90 days | about 154 days (Apr 2027) |
| doubling | | about 104 days |

Subscribers to 1,000: +366 at the current +6.3 a day is about **58 days (early Jan 2027)** if the rate holds; subs follow views at 0.43 per 1K, so growth in views brings them faster.

**Honest reading.** Flat performance never gets us there; the full line is a 4.7x jump from today's best week that must then be held for 90 days, and the Feb 1 change doubles the bar for a new application. Do not plan around Shorts ad money before mid-2027. **Do plan for the lower tier by about Feb-Mar 2027**, and for sub 1,000 by about January. Money at these levels is small anyway: typical Shorts RPM is $0.03-$0.20 per 1K views (US-heavy about $0.33) [S, AIR Media-Tech 274 channels], so today's 488K quarterly views would be about $15-$100, and 10M views a quarter about $300-$2,000. **The channel's near-term value is audience and proof for other income:** the On Demand AI-video service (the Max Claude demo is built on this exact pipeline), sponsorships, affiliate links, TikTok/Instagram Creator Rewards (RPM $0.40-$1.00 per 1K but need 10K followers [S]), and a long-form channel for the 4,000-hour route (the commentary channel "carnage" is separate and long-form).

## 6. Versus competitors (fresh Nov 5 pull, newest 30 Shorts each, public counts)
| Channel | Type | Subs | Median views | Mean | Max | We are |
|---|---|---|---|---|---|---|
| **MetaSports Clips (us)** | narrated moment | 634 | **7,250** | 9,660 | 29K | |
| @swishyhoopz | narrated moment | 21.7K | 54,000 | 212K | 1.1M | 7.4x smaller |
| @HoopiverseYT | narrated moment | 16.6K | 77,500 | 316K | 4.2M | 10.7x |
| @AhmedsBasketball | narrated story | 122K | 82,000 | 116K | 583K | 11x |
| @docbooo | clip + caption | 29.1K | 69,000 | 596K | 7.4M | 9.5x |
| @ReboundRewind | narrated | 237K | 121,500 | 174K | 997K | 17x |
| @GlobalHoopss | clip + caption | 288K | 113,000 | 742K | 9.5M | 16x |
| @breakawayclips | clip + caption | 122K | 102,000 | 426K | 5.2M | 14x |
| @ChazNBA | clip + caption | 673K | 198,500 | 329K | 1.8M | 27x |
| @CoachClank (our model) | narrated story | 146K | 299,000 | 1.55M | 26M | 41x |
| @roycebball | countdown device | 62.3K | 716,500 | 4.6M | 42M | 99x |

Reading it:
- **Their views are 2-4x their subscriber count; ours are 11x.** Our views come from the feed, not a following, so every Short must win its test audience on its own. [V]
- **Even channels with only 16-22K subscribers (swishyhoopz, Hoopiverse) sit 7-11x above us per Short.** The gap is not just channel size. [V]
- **Three winning families** (`Similar Channels (Oct 26, 2026).md`, 61 channels): game or countdown devices (median 180K), reposted clip plus one funny caption (86K), narrated story or moment (76K, our family; best all-time hit rate, 62% of Shorts at 100K+ but newest Shorts weaker than old). Their top Shorts rarely edit differently from their flops: it is the premise. [S]
- Shorts are a feed game: Sherman (YouTube Shorts lead) says the first number is viewed vs swiped away; likes, comments and shares did not move reach for Hoyos. [V, Growth Study Nov 3]

## 7. Why the gap: ranked hypotheses
1. **Premise and subject (the stranger test).** Someone who does not follow basketball should stop for it: kids, family, giants, spectacle, the top 3-4 names, or a scandal about them. History trivia and role-player stories do not. Backed by our shapes table, three studies and the 7-of-40 hit rate. [S, strongest]
2. **Too many paused-shape builds** dilute the channel's signal to the algorithm. [S]
3. **Restart effect.** The channel was dormant for seven months; the seed audience and the "coherence" the feed gives a consistent channel (Sherman, Dec 2024) are being rebuilt. Expect the base to keep rising even with the same content. [H, consistent with the 7-day rise]
4. **No format of our own.** The peers' hits often come from a device (countdown, ranking, a game) that makes the Short rewatchable; ours are mostly one-off stories. [S/H]
5. **Speed.** Morning-after news is a feed advantage; late stories lose. The gap-fill automation exists but builds are slow. [S]
6. **Conversion**, not reach: subs per 1K views is a third of FC's. [V]

## 8. What to do (ranked; each has a test and a date)
| # | Action | Why | Test and decision |
|---|---|---|---|
| 1 | **Stop building paused shapes.** 70% family / watchable curiosity / moment / live star chase; 30% one-variable experiments | table in section 3-4 | Judge at 72 h; after 10 more Shorts, if the 70% set's median is not at least 1.5x the old median, change the shape list |
| 2 | **Same-day moment pipeline**: 6:45 AM gap-fill builds only from last night's games; no building from week-old stories | late news loses | Count how many Shorts per week go out within 24 h of the game; target 5 of 7 |
| 3 | **Gauge every idea** (`idea_gauge.py`, `copy_check.py`) and kill flop shapes before voicing | saves voice credits and slots | Log the gauge score with the 72 h result for 20 Shorts; check the correlation |
| 4 | **A rewatchable device lane:** a weekly countdown ("3 times X did Y", badge in a corner) | peers' top family; our [H] test already specced | 4 posts; keep if median at least the channel median |
| 5 | **Edits from the Dyson study:** a literal picture per phrase, a counting number on the proof (`overlay.py count`), the opponent/league label on screen at the key beat, hold the payoff number 3 s | observed on a 2.7M-view Short [S] | A/B on 4 Shorts: stayed % and engaged ratio |
| 6 | **Length test:** 30-35 s vs 18-25 s, same lane, 4 each | Growth Study [H] | 72 h views and engaged ratio |
| 7 | **Hook with a foreshadow** (line 2 says what the ending is about) | Hoyos [S] | 4 Shorts |
| 8 | **Raise follows per view:** end each story on a payoff that makes a follow rational (a series promise), pin a comment that asks about the *next* one, and test a "part 2 tomorrow" only if the story is a true series | FC converts 3x better with series-like stories [S] | Subs per 1K views, target 0.7 |
| 9 | **TikTok/Instagram crossposting continues** (same file, captions from `crosspost.py`) | other revenue and audiences; 10K followers is needed for TikTok rewards | Track followers; only add the 60 s+ cut when near 10K |
| 10 | **Fix the data gap:** weekly Studio export (Monday) for stayed %, and sign in the NBA Studio account | the 74% line is only a stand-in | Owner |

**Targets** (so we know if it is working): 7-day average views per day 35K by Dec 5; at least 3 of every 10 Shorts over 15K; subs per 1K views 0.6; 1,000 subs by mid-Jan; 3M Shorts views in a rolling 90 days by Feb-Mar 2027 (33K a day).

## 9. Risks
- The Feb 1, 2027 YouTube terms change (bar and payout floor): read the Jan 31 notice; the exact treatment of existing vs new applicants is unclear [H/uncertain].
- Content ID claims on league footage; keep narrated fallbacks and use team-site footage first.
- YouTube's Oct 2026 originality change: narration of real footage plus a fact the clip can't show stays safe [V official].
- One hit carries the channel (60% of views from 10 Shorts); a quiet month can happen.
- Heavy dependence on AI tools and keys; the cloud routines were blocked on Nov 5 (YouTube keys missing there).

## 10. Files and reproduction
`Research Notes/Studio exports/api/channel_daily 2026-11-05.csv` (365 days of Shorts views/subs by day), `daily 2026-11-05.csv`, `retention 2026-11-05.csv`, `Research Notes/_competitors_nov5.json`, `Research Notes/_channel_trend_nov5.json`, `Tools/channel_totals.py`. Deep dives: `Full Review for Retention (Nov 2026).md`, `Posting Study (Oct 26, 2026).md`, `Similar Channels (Oct 26, 2026).md`, `Growth Study (Nov 3, 2026).md`, `Topic and Script Reset (Nov 2026).md`, `Monetization Research (Oct 23, 2026).md`, `Shorts Mechanics and Policy (Oct 24, 2026).md`.
