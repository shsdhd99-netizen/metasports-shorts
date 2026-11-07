<!-- AUTO:STATUS -->
## LIVE STATUS (auto, Sat Nov 07, 10:11 AM ET; `python Tools/roadmap.py` rewrites this block daily)

The plan below it is history (Sep 2026). What runs the channels now: THE RULES (Nov 7) in `MetaSports - Playbook.md`, the auto queue (`Research Notes/Auto Queue.md`), the lab (`Research Notes/Lab/Scoreboard.md`) and the QA board (`Research Notes/QA Board.md`).

### MetaSports (NBA) (data to 2026-11-04)

| Now | |
|---|---|
| Subscribers | 650 (+5.0 a day, 28-day average) |
| Views a day | 23,416 (7-day) vs 15,041 (28-day): up 56% |
| Views, last 90 days | 518,353 |

| Milestone | Needs | Now | Reached at today's pace (7-day) |
|---|---|---|---|
| 500 subscribers | 500 | 650 | reached |
| 1,000 subscribers | 1,000 | 650 | Jan 17, 2027 |
| Fan funding (3M Shorts views / 90 days) | 33,333 a day | 23,416 a day (70%) | needs 1.4x the current pace |
| Partner Program today (10M / 90 days) | 111,111 a day | 23,416 a day (21%) | needs 4.7x the current pace |
| New applicants from Feb 1, 2027 (20M / 90 days) | 222,222 a day | 23,416 a day (11%) | needs 9.5x the current pace |

### MetaSports FC (data to 2026-11-04)

| Now | |
|---|---|
| Subscribers | 183 (+5.4 a day, 28-day average) |
| Views a day | 8,249 (7-day) vs 5,119 (28-day): up 61% |
| Views, last 90 days | 143,331 |

| Milestone | Needs | Now | Reached at today's pace (7-day) |
|---|---|---|---|
| 500 subscribers | 500 | 183 | Jan 05, 2027 |
| 1,000 subscribers | 1,000 | 183 | Apr 09, 2027 |
| Fan funding (3M Shorts views / 90 days) | 33,333 a day | 8,249 a day (25%) | needs 4.0x the current pace |
| Partner Program today (10M / 90 days) | 111,111 a day | 8,249 a day (7%) | needs 13.5x the current pace |
| New applicants from Feb 1, 2027 (20M / 90 days) | 222,222 a day | 8,249 a day (4%) | needs 26.9x the current pace |

### The next 7 days (auto queue)

| Slot (ET) | Ch | What | Short | Score |
|---|---|---|---|---|
| Sat Nov 07 03:30 PM | nba | PINNED | Luka Has Scored 40 In Six Of His Last Seven Games | 45 |
| Sun Nov 08 07:15 AM | nba | EMPTY | - | - |
| Sun Nov 08 03:30 PM | nba | MOMENT | last night's best moment | - |
| Sun Nov 08 12:00 PM | fc | ON YOUTUBE | The player who moved two Coca-Cola bottles at the Euros | - |
| Mon Nov 09 07:15 AM | nba | IDEA | List 1: who has missed the most free throws in NBA hist | 46 |
| Mon Nov 09 12:00 PM | fc | BUILD | The Goalkeeper Who Beat A Team That Practised 1000 Pena | 77 |
| Mon Nov 09 06:00 PM | fc | BUILD | The Goalkeeper Who Found Out Chelsea's Secret Penalty P | 77 |
| Tue Nov 10 07:15 AM | nba | IDEA | Curry passes DeRozan (16th all-time scoring), when it h | 46 |
| Tue Nov 10 03:30 PM | nba | MOMENT | last night's best moment | - |
| Tue Nov 10 12:00 PM | fc | BUILD | The Baby Messi Bathed Beat Him In A World Cup Final | 43 |
| Wed Nov 11 07:15 AM | nba | ON YOUTUBE | The NBA Legend Who Made Up An Insult 😳 #nba | - |
| Wed Nov 11 12:00 PM | fc | BUILD (filler) | The Hull City Fan Who Walked Home From Chile | 43 |
| Wed Nov 11 06:00 PM | fc | BUILD (filler) | The Goalkeeper Who Saved A Shot With A Scorpion Kick | 43 |
| Thu Nov 12 07:15 AM | nba | IDEA | LeBron passes Kidd for 3rd all-time assists, when it ha | 46 |
| Thu Nov 12 03:30 PM | nba | MOMENT | last night's best moment | - |
| Thu Nov 12 12:00 PM | fc | BUILD (filler) | The Goalkeeper Who Scored More Goals Than Most Strikers | 43 |
| Fri Nov 13 07:15 AM | nba | IDEA | Lendeborg Part 3 after a 30+ game | 46 |
| Fri Nov 13 12:00 PM | fc | BUILD (filler) | The Goalkeeper Who Got The Penalty Rules Changed | 43 |
| Fri Nov 13 06:00 PM | fc | EMPTY | - | - |

Held by QA: Why You Can't Bet On The Opening Tip 😳 (FOOTAGE: no cuts.json / cuts_plan.json); Why The Lakers Kept Bronny Over Knecht 😳 (SCRIPT: notes.md has 1 source link(s); every Short needs at ); Paul George Broke A Celtics Record And L (SCRIPT: notes.md has 0 source link(s); every Short needs at ); LeBron Just Answered A Knicks Fan 😳 (SCRIPT: notes.md has 0 source link(s); every Short needs at ); Two Buzzer-Beaters From 40 And 50 Feet (PACKAGE: title missing or a placeholder; 7 tags, 83 characte)

### Live tests (the lab scores them daily)

| Test | Question | A | B | Score | p | Avg % | Status | Next |
|---|---|---|---|---|---|---|---|---|
| `nba-lists` | Are record lists a hit lane we can repeat? | every other NBA Short: 5,629 (n=49) | 'Who has ___ the most in NBA history?' list: 23,952 (n=3) | 78 | 0.12 | 98% vs 96% | **RUNNING** | needs 3 more (+11 waiting for 72 h) |
| `nba-opener` | Do Why/How/What/Who titles get more views? | title opens on a name or noun: - (n=0) | title opens with Why/How/What/Who: - (n=0) | - | - | - | **RUNNING** | needs 6 more (+2 waiting for 72 h) |
| `nba-cadence` | Does a second post on the same day cost views per post? | a 1-post day: - (n=0) | a 2+-post day: - (n=0) | - | - | - | **RUNNING** | needs 8 more (+2 waiting for 72 h) |
| `fc-premise` | Can a new premise (a star's relative, kept his promise, one-mistake chain, bargain scouting, fans beat the club) match our shootout Shorts? | penalty-shootout Shorts: 24,230 (n=4) | a new non-shootout premise: - (n=0) | - | - | - | **RUNNING** | needs 5 more (+5 waiting for 72 h) |
| `fc-opener` | Does opening on the action keep more viewers than reading the title first? | title-first (the spoken title is line 1): - (n=0) | action-first (the title on screen only; line 1 is the first story sentence): - (n=0) | - | - | - | **RUNNING** | needs 6 more |
| `fc-music` | Does the quiet music bed help? | no music: 1,085 (n=1) | quiet music bed: 3,337 (n=1) | 100 | - | 71% vs 64% | **RUNNING** | needs 5 more (+7 waiting for 72 h) |


### Rules the data questions (fixed or dropped on Sunday)

- C6 scrapped: posting before 10 AM ET (nba): **REVISIT: it may matter**

### QA

- Waiting drafts: 1 SHIP, 0 FIX, 5 HOLD (see `Research Notes/QA Board.md`).
- On YouTube: 2 upload(s) with a FAIL. ; 

<!-- /AUTO:STATUS -->


# Roadmap: Next 90 Days (Sep 28 → Dec 27, 2026)

*Round 3. It's built from:*
- *your real numbers*
- *CoachClank's growth curve*
- *the 2026-27 NBA calendar*
- *YouTube's current rules*

*Check it every Sunday with `/channel-check`.*

## MetaSports

**Where you start:**
- 469 subs, 80 Shorts, ~30K median views.
- Your last upload was **Feb 23, about 7 months ago**. After a break that long, YouTube re-tests the channel, so the first 1–2 weeks can look slow.
- That's normal. Don't change the recipe while it happens.

**The money lines (they explain the checkpoints below):**

| Milestone | YouTube requires | What that means for you |
|---|---|---|
| **Fan funding** (memberships, Super Thanks) | 500 subs + 3M Shorts views in 90 days | ~33K views a day. Daily posting at your old 30K level lands *just* under; 2 a day clears it |
| **Shorts ad money** (YPP) | 1K subs + 10M Shorts views in 90 days | ~110K views a day, e.g. 2 a day at a 55K median. **For new applicants from Feb 1, 2027 the bar doubles to 20M**, so reaching it before then is the stretch goal |

### Phase 1: Restart (Sep 28 → Oct 19)
- **1 Short a day, posted between 6 and 11 AM ET.** That's CoachClank's best window in both years; afternoons are his worst.
  - Batch 2 #1–10 are dated for this window; `/nba-short` fills the gaps.
  - Make evergreen stories the night before and schedule them for 8 AM.
- **Every upload follows the new rules:**
  - a 4–7 word title, with no hashtags; questions are welcome
  - 22–40 seconds for stories (90–170 words) and 15–25 for quick moments
    - CoachClank's 31–45s Shorts have the best median.
    - His 8 biggest of 2026 ran 22–34s.
  - the moment on screen from frame 1
  - an argument ending plus a pinned question
- **Preseason is slow news.** It's the best time for evergreen "rule-weird" and "what happened to…" stories.
- **Checkpoint (Oct 19):** the median of your last 10 is 30K+, and at least one Short hit 100K+.
  - Under 10K? That's the re-test. Keep posting 14 more days before you change anything.

### Phase 2: Season surge (Oct 20 → Nov 30)
- **Opening night is Tue Oct 20.** From then on, run the daily loop:
  1. `/nba-short` in the morning.
  2. Pick last night's best moment.
  3. Post by 11 AM ET. Being first is the whole game.
- **Add a 2nd Short only when you have two strong stories.** CoachClank's 2-a-day days were weaker in 2025 and only slightly better in 2026. His 3-a-day days always flopped.
- **Watch the length data.** 30–45s is CoachClank's best bucket in both years (1.43M and 999K medians).
  - Your three Shorts over 30s flopped, but that's only 3, and one was a fight clip.
  - `/channel-check` will show within 2 weeks whether 30–45s works for you too.
- **Every WINNER (2× your normal) gets a follow-up within 48 hours:** same player, same rule, or "part 2".
- **Checkpoint (Nov 30):** median 50K+, 3+ Shorts at 250K+, 500 subs. Apply for fan funding once you pass 3M views in 90 days.

### Phase 3: NBA Cup & Christmas (Dec 1 → Dec 27)
- **The NBA Cup final is Fri Dec 11** in Indianapolis.
- **Christmas Day** is the biggest regular-season audience. Have 3 stories written by Dec 20.
- **Checkpoint (Dec 27):** one 1M-view Short and a 100K median. That's the pace for 10M in 90 days before Feb 1.

### Bank ideas now for later
- **Trade deadline, Thu Feb 11, 2027.** "Who won the trade?" is the easiest argument ending in the sport.
- **All-Star weekend, Feb 19–21**, in Phoenix.

### Decision rules

| If… | Then… |
|---|---|
| A Short hits 2× your normal | Post a follow-up within 48 hours |
| 5 in a row land under half your normal | Check the basics: copy-checked? scene opener? argument ending? Then post an iconic "what happened to…" story |
| A Short gets almost no views | In YouTube Studio, look for a copyright claim or an age restriction (`/channel-check` flags these) |
| You miss a day | Post the next day. Never go dark for a week again |
| A whole month is bad | That's normal. CoachClank's monthly median swung from 87K to 1.05M this year. Judge by 4-week medians and keep posting |

## Commentary

**Where you start:** no channel yet, and the 5 lane questions aren't answered. Everything below waits on those answers, because your lane *is* the channel.

### Phase 0: This week
1. Type `/commentary-script`. It asks the 5 questions and saves your answers to `Commentary - My Lane.md`.
2. Create the channel. The Garbage Time avatar and banner are in `Brand Images`, or pick your own name.
3. Record a 60-second mic test over gameplay and listen back on your phone.

### Phase 1: Launch sprint (days 1–30)
- **2 videos a week minimum, 3 if you can, 6–10 minutes each.** This is the 30-day sprint in the Commentary playbook.
- **Expect 15–30 videos before your first breakout.**
  - Pauly Walnuts reached his first 100K-view video at video #14, on day 19.
  - Random Hero Gaming, posting about once a week, got there at video #16, on day 103.
  - Avery Yapps got there at video #32, on day 72.
  - Puckout, posting about once a week, needed 28 videos and 194 days just to reach 10K.
  - It's the number of videos more than the calendar. The faster you reach video #30, the sooner your breakout comes.
- **Every breakout was personal:**
  - PW quit his job.
  - Random Hero Gaming described single life after 30.
  - Avery explained why he ghosted old friends.
  - Puckout defended his generation.

  Make every 3rd video a "Why I ___" confession or a life-stage story.
- **Package every video:**
  - The title uses a breakout pattern (`/titles`).
  - It gets 3 thumbnails in Test & Compare (`/thumbnail`).
- **After 48 hours, write down 2 numbers from YouTube Studio:**
  - click-through rate
  - % still watching at 30 seconds

### Phase 2: Double down (days 31–60)
- **Your best video gets a Part 2 within 7 days.** That pattern is behind most peer breakouts.
- **Make one "Why I ___" confession video.**
- **Cut the best 30–45 seconds of each video into a Short.**
- **Comment genuinely on 5 peer videos a week.** Once you have 5 videos up, pitch one small peer (under 10K subs) on a collab.

### Phase 3: Weekly rhythm (days 61–90)
- **1 long video a week, plus 2–3 Shorts cut from it.** Go 12–20 minutes when the story earns it.
- **Checkpoints:**
  - **Fan funding:** 500 subs + 3,000 watch hours.
  - **Ad money (YPP):** 1K subs + 4,000 hours today. It's 8,000 hours for anyone applying from Feb 1, 2027, so plan on 8,000.

## Your week (both channels)

| When | MetaSports | Commentary |
|---|---|---|
| Every day (20–30 min) | `/nba-short` → `/voiceover` → drop clips → `/assemble` → post | — |
| Tue & Fri | — | record + edit |
| Wed & Sat | — | post, with 3 thumbnails in Test & Compare |
| Sunday | `/channel-check` | check click-through + 30-second retention, pick next week's 2 topics |

*Sources: NBA dates from NBC's [2026-27 key dates](https://www.nbcnewyork.com/nba/nba-key-dates-2026-27-opening-night-trade-deadline-finals/6535379/). YouTube thresholds and title data are in `Research Notes/Sources.md` and `Tools/data/title_patterns.md`.*
