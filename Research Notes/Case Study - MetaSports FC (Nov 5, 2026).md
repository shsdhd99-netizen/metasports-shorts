# Case study: MetaSports FC (soccer story Shorts), Nov 5, 2026

Companion to `Case Study - MetaSports NBA (Nov 5, 2026).md` (same method, same tiers: **[V]** measured or stated by YouTube, **[S]** small sample or seen elsewhere, **[H]** a guess). Data pulled today: YouTube Analytics API (read-only), `yt-dlp` public counts, YouTube's eligibility page, our Oct 23-24 monetization notes. Reproduce with `Tools/channel_totals.py --channel fc`, `Tools/yt_analytics.py --channel fc daily`, `Tools/fc_study.py`.

## 1. The answer in six lines
1. **A 15-day-old channel with one proven premise.** First Short Oct 21; 16 Shorts; 151 subscribers; 120.8K Shorts views so far (Oct 103.6K, Nov 17.2K in 4 days); about 9.5K views a day over the last two weeks. [V]
2. **The goalkeeper-does-something-odd-in-a-famous-shootout premise is 6 for 6.** Sock cheat sheet 30K (87 subs), water bottle 29K, subbed on for penalties 23.6K, dancing on the line 15.6K, plus the two newest: England penalty subs 17.3K at 2 days and gloves-off 13.0K at 1 day. Everything else (10 Shorts) stayed under 5.3K; 0 of 8 non-goalkeeper Shorts have passed 3.2K. [V]
3. **Our subscribers per view are excellent: 1.36 per 1K views** (NBA 0.43); the sock Short alone earned 87. The follow is earned by the *first* Short of a pattern; its sequel earned 8 at the same views. [V]
4. **Monetization is far on views, near on subs.** 151 of 1,000 subs; 120.8K of 10M Shorts views in 90 days (1.2%). The lower tier needs 500 subs (we are 30% there, about 6 weeks at the current pace) and 3M views in 90 days (4%). [V]
5. **Against competitors we are 14-82x smaller per Short**, but the channel is 15 days old and they are 1-5 years old; the right comparison is trajectory, not level. [V/H]
6. **The risk is idea supply and concentration:** 84% of all views come from 5 Shorts, and the working premise needs a *new* odd goalkeeper fact each time. We have 6 scripts queued. [V]

## 2. Where we are
| Measure | Value | Source |
|---|---|---|
| Subscribers | 151 (162 gained since Oct 21, 0 lost) | yt-dlp, API |
| Shorts | 16 (14 mature, 3+ days old) | public |
| Shorts views, last 90 days (= channel life) | 120,771; watch hours 1,024 | API |
| Views per day, 7 / 14 day average | 9,565 / 9,290 | API daily |
| Median / mean / max public views, newest 16 | 3,150 / 9,337 / 30,000 | yt-dlp |
| Concentration | top 5 Shorts = 84% of views; top 10 = 95% | API, 14 mature Shorts |
| Engaged ratio, median | 0.565 (only 1 of 14 under 0.50) | API |
| Subs per 1K views | 1.36 | API |
| Median length | 57.5 s | API |
| Average % viewed | goalkeeper lane 83-96%; club/manager stories 64-79% | API |

## 3. What is working
- **Premise: a goalkeeper doing something sneaky, odd or unbelievable in a famous shootout** (above). Retention 83-96% average viewed, engaged ratio 0.55-0.62. [V, n=6]
- **Story format** (title read aloud as line 1, "Back in [year]...", a turn every 8-12 s, a hard payoff, nothing after it; 51-60 s) copied from the Ahmed network that has 1.3B views. Our goalkeeper Shorts hold 83-96%, as good as theirs. [S]
- **Real archive and broadcast footage** (archive.org, official uploads) at about 1.6-2.2 s a shot, wide plays over a 3:4 window. [S]
- **First-of-a-pattern earns the subs** (sock 87, sequel 8). [V]
- **Clip repetition is not hurting** (Nov 4-5 study: no negative effect at n=13-15; the heaviest repeater S26 has 13K views in a day; retention check due Nov 7). [V/S]

## 4. What is not working
- **Non-goalkeeper stories top out under 3.3K** (club stories 2.0K median, managers 2.7K, player records 2.1K). Two managers' Shorts were 64-67% viewed. [V, n=10]
- **Sequels of the same trick** (water bottle: 29K views, 8 subs). [V]
- **Every new story needs a fact nobody has told;** copy-checks flagged S31 (baby Messi) TAKEN, S36 (Martinez law) TAKEN, S22 (Ceni) CROWDED. [V]
- **Footage gaps** (no clean ball-throw clip in S29) and 720p sources blown up 2.7x. [V]
- **No Studio "stayed to watch"** for FC beyond one manual export (Nov 4). [gap]
- **TikTok and Instagram are weaker for this format** (Ahmed's Goal TikTok median is 0.47x its YouTube median). [S, Growth Study]

## 5. How close are we to monetization (FC)
| Step | Needs | Us | Gap |
|---|---|---|---|
| Lower tier (fan funding, no ads) | 500 subs + 3 public uploads in 90 days + 3M Shorts views in 90 days [S] | 151 subs; uploads fine; 120.8K views | subs +349 (about 5-7 weeks at 8 a day, **about Dec 19**); views 25x (needs 33K/day vs 9.5K) |
| Full YPP (today's bar) | 1,000 subs + 10M qualified Shorts views in 90 days, or 4,000 long-form hours [V] | 151 / 120.8K (1.2%) | subs +849 (**about 3.5 months, around Feb 20, 2027**); views 83x (needs 111K/day) |
| New applicants from Feb 1, 2027 | 1,000 subs + 20M views / 90 days [V, YouTube Blog Aug 10 2026 via our Oct 23 note] | | 166x |
| Shorts pay floor from Feb 1, 2027 | 10M qualified views per rolling 90 days [V, same] | | |
Counts use engaged/qualified views (about 54% of public on NBA; FC's engaged ratio is slightly higher, 0.565).

Projection from 9.5K a day (steady growth per 30 days): 3M in 90 days: never at flat, about 318 days at +15%, **188 days at +30%**, 135 days at +50%. 10M in 90 days: **never below about +30% a month; 326 days at +30%, 224 days at +50%, 145 days at doubling.** Honest reading: subscribers will not be the problem on FC (1.36 per 1K views); **views are the gate, and the Shorts-ad route is realistically a mid-to-late-2027 target even with strong growth.** At $0.03-$0.20 per 1K views [S] the money is cents-to-dollars until then.

## 6. Versus competitors (Nov 5, newest 30 Shorts each, public counts)
| Channel | Subs | Median | Mean | Max | We are |
|---|---|---|---|---|---|
| **MetaSports FC (us), 16 Shorts, 15 days old** | 151 | **3,150** | 9,337 | 30K | |
| @footballgoat7 (countdown device) | 243K | 44,000 | 114K | 1.1M | 14x smaller |
| @AhmedsGoal (our story model) | 426K | 125,500 | 227K | 1.1M | 40x |
| @Ftblpranz (game/countdown) | 200K | 257,500 | 614K | 2.2M | 82x |
| @TAT_futbol (game/countdown) | 310K | 259,000 | 1.64M | 13M | 82x |
Reading it:
- Our four goalkeeper hits (13-30K) sit **inside the range of the smaller peers' medians** (footballgoat7 44K, Ahmed's Goal 125K is the bar). The premise works; the channel needs **more of it, more often**, not a different edit. [S]
- Ahmed's Goal's weakest recent Shorts are 43K; its top is 1.1M. Their hit rate comes from one repeatable premise class too. [V]
- We cannot compare early trajectory yet: ask again at 60 days. [H]

## 7. Why the gap and what the data says to do
**Hypotheses (ranked):** (1) a single proven premise class the channel has not yet scaled; (2) a 15-day-old channel with no seed audience (the first Shorts got 1-3K); (3) idea supply and fact-checking cost per Short; (4) sequels flop, so each hit costs a new research find; (5) footage quality limits (archive/720p). [S/H]

**Actions (ranked, with tests):**
| # | Action | Test |
|---|---|---|
| 1 | **Build an idea bank of 20+ vetted goalkeeper-odd-device stories**, each with its own new fact, a famous event, real footage and two sources. Pass the copy check first. Order now: S21 Higuita scorpion, S30, S31 (copy check TAKEN, owner's call), S32 (needs a 2nd source). Add 2 vetted ideas a day. | Keep the 70% premise share; judge at 72 h; target at least 3 of every 5 over 10K |
| 2 | **Protect the first-of-a-pattern rule**: no sequel of a trick we have shown; one new mechanism per Short (sock, bottle, subbed on, dance, gloves). | Subs per 1K views at or above 1.0 |
| 3 | **Test two goalkeeper Shorts with an action-first opener** (instead of title-first) to see if the 3-second drop shrinks | 4 Shorts, % viewed and the first-4 s curve |
| 4 | **Keep non-goalkeeper stories to experiments (30%)** and change one variable each (e.g., a global-star club story with a hard number payoff) | each judged at 72 h against 3.1K |
| 5 | **Finish the repetition test:** S26 retention Nov 7 vs S28 and S25 siblings; if S26 is 85%+ % viewed, remove the "repeat" worry and relax the guard | check Nov 7 |
| 6 | **Edits from the Dyson study** (counting number on the payoff, hold the payoff number 3 s) | 3 Shorts |
| 7 | **Footage:** download 1080p (`height<=1080`) when disk permits; prefer official federation, UEFA/FIFA uploads | QA blow-up warning gone |
| 8 | **Crosspost** the same file to TikTok/Instagram; consider the 60 s+ cut only when near 10K followers (TikTok rewards) | followers |
| 9 | **Weekly Studio export** (Monday) so "stayed to watch" exists for FC | owner |

**Targets:** 7-day average 20K views a day by Dec 5; 500 subs by Dec 20; at least 3 of every 5 goalkeeper Shorts over 10K; subs per 1K at or above 1.0; 1,000 subs by late Feb 2027; 3M views in a rolling 90 days by about May-June 2027.

## 8. Risks
- Idea supply (the single premise is a mine that can run dry); each Short needs a sourced new fact (accuracy risk if rushed).
- Copyright/Content ID on broadcast footage; keep official and archive sources.
- Policy: Feb 1, 2027 terms; the Shorts pay floor; AI disclosure rules (answer "No" for narrated real footage, per our policy note).
- n is tiny (6 goalkeeper Shorts): one miss would not kill the premise, but five misses in a row would.

## 9. Files
`Research Notes/Studio exports/api FC/channel_daily 2026-11-05.csv`, `daily 2026-11-05.csv`, `retention 2026-11-05.csv`; `Research Notes/_competitors_nov5.json`; `Research Notes/FC Clip Repetition Study (Nov 4, 2026).md`; `Research Notes/Studio Analytics Review (Nov 4, 2026).md`; `Soccer Channel/Lessons Learned.md`, `Playbook.md`, `Idea Bank.md`, `Outcome Log.md`; `Research Notes/Topic and Script Reset (Nov 2026).md`.
