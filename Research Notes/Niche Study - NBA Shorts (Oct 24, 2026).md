# Niche Study: what makes NBA Shorts go viral (Oct 24, 2026)

**The question:** what actually makes NBA Shorts travel, with evidence, and where our current rules are wrong.

**Data used:**
- Public Shorts listings (title + views) for 16 NBA channels: 2,772 Shorts after skipping each channel's 5 newest. Pulled today with yt-dlp.
- vidIQ public stats pages for 28-day views.
- Official YouTube help pages and blog posts.
- Press interviews.
- Our own Ahmed's Basketball CSV (1,175 Shorts).
- Our Studio exports.

**Tiers:**
- **[V]** verified data: computed here, or stated on an official page.
- **[S]** several credible sources, or our own earlier measurements.
- **[H]** a single source, anecdotal, or my inference.

---

## Top 7 findings

### 1. The topic and title explain little. The first seconds and the footage decide most of it.
**What:** the same concept, under the same title, swings 5x or more from one post to the next. Ahmed's Basketball shows it best.

**Evidence:**
- **The Ahmed CSV:** 133 concepts were posted 2 or more times (554 Shorts).
  - **70% of the spread in (log) views sits *within* the same concept.**
  - The best airing of a concept typically gets 5x the views of the worst. 30% of concepts show a gap of 10x or more.
  - Example: "NBA players who had no chance of going pro but still did" was posted 5 times and got 45K, 1.4M, 48K, 42K and 4.1M. [V]
- **Our channel (38 Shorts, Oct 3-21, Studio):**
  - Every Short with 10K+ views had 74%+ stayed to watch.
  - Stayed vs views: Spearman 0.69.
  - But #40 held 81% and got only 1.6K (its re-upload got 6.7K). [V]

**What we should do:**
- Treat stayed % (74%+) as the gate a Short must pass, not as a guarantee.
- When a strong concept flops once, re-cut its first 3 seconds and frame 1 and post it again. Don't drop the concept.
- Spend effort on the opening clip, not on title wording.

### 2. Repeated templates decay, then collapse. Our one-format strategy is our biggest risk.
**What:** every NBA channel that ran one winning template over and over saw it fade. In one case the template went from 23M to near zero.

**Evidence:**
- **Mike Korzemba**, "He Played Dirty, So [Star] Ended His Career": 17 entries.
  - The early entries got 23M (Giannis), 18M (Curry), 13M (Luka), 9.7M (Jordan) and 5.0M (Jokic).
  - **The 6 most recent got 8K-49K.**
  - The channel now gets 1.28M views per 28 days and gained 0 subscribers (vidIQ, Oct 23).
- **REBOUND**, "CAUGHT CHEATING": 42M → 7.7M → 12M → 10M → 2.7M → 2.1M → 1.2M → **184K for "#4"**.
- **Rebound Rewind**, "LeBron James is so Old": 5.3M → 3.3M → 1.4M → 1.4M.
- **Ahmed's network:** a repeat airing of a concept gets about 0.7x the first (n=102 concepts, Oct 23 study). [V]
- **Our own format runs, in posting order:**

  | # | Stayed | Views |
  |---|---|---|
  | #42 | 86.9% | 19-25K |
  | #48 | 83.3% | 22K |
  | #64 | 72.6% | 9.8K |
  | #52 | 59.1% | 3.5K |

  This is confounded: #64 and #52 also changed frame 1 and the star. [V numbers, H cause]
- **YouTube, Jul 16, 2026:** template content that is "very generic and don't really have a narrative arc" can cost a channel its monetization (Matt Halprin, TechCrunch). The policy page says the substance of each video should vary. [V]

**What we should do:**
- Keep THE #42 FORMAT, but as one of 3-4 rotating formats, at most about 1 post in 3.
- Rewrite the fixed lines every time ("So is he a worse shooter? No." must not repeat word for word).
- **Retire any format after 3 posts in a row below the channel median.**

### 3. The 1M+ tier in NBA Shorts is visible moments, not stat paradoxes.
**What:** the channels with the most 1M+ Shorts explain one strange clip the viewer can see. Our stat paradoxes top out around 20-25K.

**Evidence:**
- **CoachClank** (145K subs, 1.12B lifetime views, 8.9M in the last 28 days):
  - Last 295 Shorts: median 419K; **34% reached 1M+**; the top 10% have a median of 9.15M.
  - Its biggest hits are all one visible oddity: "6'8 vs 7'9" (33M), "He Didn't Have To Do That" (24M), "He Was Playing By Himself" (21M), "Only Steph Curry Would Notice This" (15M). [V]
  - In 9 of its top 11 transcripts, line 1 points at the clip: "This has to be the funniest way to end a game", "When a player is falling out of bounds, they usually…" [S, n=11]
- **Our own top 5 of all time** (55-80K) were also visible oddities: free-throw tricks, underhand free throws, a dunk without jumping. Caveat: that era was about 30K across the board. [V]

**What we should do:**
- Add a second lead lane: **"one clip, one oddity"**, 20-35 s.
  - Frame 1 is the moment itself.
  - Line 1 points at it ("This is why…", or "When X happens, players usually Y. He didn't.").
- **Footage gate:** the clip must look strange with the sound off.

### 4. Rules are not the problem; paperwork is.
**What:** rule-breaking you can see is one of the best-performing themes in the niche. Rules that live on paper lose.

**Evidence:**
- **Across 13 channels**, titles about rules, bans, "caught", cheating or "illegal" average **1.42x** each channel's own local median (n=79). That theme beats the channel median on 5 of 7 channels, and 41% of these Shorts reach 2x or more. [V]
- **The winners:**
  - REBOUND "NBA Players CAUGHT CHEATING.." (42M) and "3 NBA Rules You Didn't Know Exist.." (36M)
  - HoopFlix "BANNED Food In The NBA" (8.5M)
  - Chaz NBA "Jokic knew a rule that the ref didn't" (2.1M)
  - CoachClank "The Unwritten Triple Double Rule" (6.5M)
- **The losers are policy and procedure:**
  - Rebound Rewind "New NBA Rule for the Upcoming Season!" (0.23x)
  - NBA Facts "Why did the NBA ban masks?" (0.14x)
  - CoachClank "NBA's New Secret Rule" (0.31x)
  - our #53, the bet ban (2.8K), and #45, the Game 4 credit question (3.8K)
- **Our own #22** "Only two can wear six" (31.8K, 82.4%) is a rule premise, and **#03** (DPOY voters, 26K, 80.2%) is a vote technicality. [V]

**What we should do:**
- Replace "no rule/policy topics" with **"no paperwork rules"**.
- A famous player visibly breaking a rule, or a banned object you can see, is allowed and is high-ceiling.
- Betting, scheduling, voting procedure and stat credit stay out unless a famous name and a hard paradox carry them (as #22 and #03 did).

### 5. 20-30 s is unproven. The biggest NBA story channel does best at 31-45 s.
**What:** our length rule rests on no test. The strongest outside data points longer.

**Evidence:**
- **CoachClank, 431 Shorts with exact durations (our Sep 27 pull):**

  | Length | 2025 median (n) | 2026 median (n) |
  |---|---|---|
  | 20 s or less | 738K (115) | 301K (123) |
  | 21-30 s | 279K (46) | 666K (74) |
  | **31-45 s** | **1.43M (27)** | **999K (17)** |

  31-45 s is the best band in both years. Caveat: bigger stories run longer. [S]
- **Our 38 Shorts:** no relation inside 20-33 s (rho -0.12 with views, -0.02 with stayed). **We have never posted a 35-45 s NBA Short.** [V]
- **Other studies disagree:**
  - quso.ai, 108K mostly small-creator Shorts: views peak at 11-20 s and fall after 30 s. [S, vendor data]
  - Paddy Galloway, 5,400 Shorts in 2023: longer did better. [S]
- **A hard limit:** a Short over 60 s with any active Content ID claim is blocked worldwide. [V official]

**What we should do:**
- Let length follow the story.
- Run 5 paired tests: a 35-45 s version with 2 turns against our 22-28 s cut.
- **Cap every NBA Short at 58 s**, because NBA footage can be claimed.

### 6. The AI voice is not what hurts us. Templates and reused clips are the real risks.
**What:** no evidence shows AI-voiced NBA Shorts are suppressed or earn less.

**Evidence:**
- **The biggest narrated channels use AI voices:**
  - CoachClank uses a fast AI voice. It has 1.12B views, and 0 of its 180 top comments mention the voice (Playbook). [S]
  - Ahmed's network is narrated in the same machine style. [S]
- **YouTube's monetization policy page does not mention AI voice at all.** [V]
- **The disclosure page:** "Disclosing AI content alone won't limit a video's audience or impact its eligibility to earn money." Disclosure is required only when a real person is shown saying something they didn't say. [V]
- **What is demonetized:**
  - template content with little variation (Jul 2026); [V]
  - clips reused without added commentary. [V]
- **What is allowed:** YouTube's policy explicitly lists "Replays of a sports tournament where you explain the moves a competitor did to succeed." [V]
- **Copyright claims:**
  - A claim on a Short under 60 s doesn't block it. [V]
  - Non-music claims don't cut the Shorts revenue-pool share: "No other category of third-party content will be credited." [V]

**What we should do:**
- Keep Alex. Don't pay for a human voice.
- Spend the effort on real commentary and variety.
- Never clone a real announcer. NBC's AI Jim Fagan voice was made with his family's permission.

### 7. From Feb 1, 2027, Shorts pay nothing below about 111K views a day. Only hits get us there.
**What:** we need 10M qualified Shorts views every 90 days to earn from Shorts at all.

**Evidence:**
- **YouTube Blog, Aug 10, 2026:** from Feb 1, 2027, creators need "10 million qualified Shorts views over the last 90 days" to share in Shorts revenue. [V]
- **Where we are:** about 17.3K a day (Oct 17-23), roughly 1.6M public views per 90 days, under a sixth of the floor. Qualified views run lower still. [V]
- **What the floor takes:**
  - Twenty-five 20K hits a month don't reach it.
  - A handful of 1M+ Shorts do.
  - Already covered in `Monetization Research (Oct 23, 2026).md`.

**What we should do:**
- Make "share of Shorts at 100K+" the headline metric alongside stayed %.
- Point the formats at a 1M+ ceiling: findings 3 and 4.
- Use the #42 format to keep the floor up, not to clear the 10M bar.

---

## Where our rules are wrong or unproven

| Our rule | Verdict | Evidence | Change |
|---|---|---|---|
| **THE #42 FORMAT as the lead format** | **Works now, with high decay risk** | 2 of 4 posts at 83%+ stayed (#42, #48); then 72.6% and 59.1%. Every outside single-template series decayed (finding 2) [V] | One of 3-4 rotating formats, about 1 in 3 posts; retire after 3 misses in a row |
| Fixed lines ("So is he a worse shooter? No.") | **Risky** | YouTube's template clarification of Jul 2026 [V]; Korzemba's identical-title series collapsed [V] | Same beats, new words every time |
| **20-30 s** | **Unproven** | CoachClank's best band is 31-45 s in both 2025 and 2026 [S]. Our own data has no length signal and no posts over 33 s [V] | Paired tests at 35-45 s; cap at 58 s |
| AI voice (Alex) | **Fine** | Finding 6 [V policy, S reception] | Keep |
| **~225 wpm** | **Unproven, and our own numbers disagree** | #42 ran at about 195 wpm, by its own spec. CoachClank runs 265-309 wpm, Ahmed 258-274 [S] | Log wpm for every post; test 195 vs 250 |
| **No music** | **Unproven, and possibly contradicted** | The #42 v3 render had a Yuke instrumental, and nobody logged which file was uploaded (`THE 42 FORMAT.md`). Ahmed uses a quiet bed about 20 dB under the voice [V]. No study shows music raises or lowers views [S] | Test a royalty-free bed, which does *not* cut pay (Q2 below); log music yes/no on every post |
| Words and numbers over real footage; captions burned in | **Supported** | Every big narrated NBA channel burns captions in: CoachClank, Ahmed, REBOUND, Hoop Facts [S] | Keep |
| **A new shot every ~1.5 s** | **Contradicted** | #42 had a 2.0 s median shot and "read better" than our 1.2-1.9 s builds (`THE 42 FORMAT.md`). Competitors run 1.9-2.8 s (Round 9) [S] | 2.0 s median; hold the opening play for its first 5 s |
| **Frame 1 = a sharp close-up of the star** | **Contradicted by our own data** | #42 opened on the airball (86.9%); #64 on Wemby's face (72.6%); #52 on a soft close-up (59.1%). Both the format spec and the Oct 23 Diagnosis say "frame 1 shows the bad thing, not a face." CoachClank hits open on the moment [S] | Frame 1 = the thing line 1 is about, happening, and sharp |
| **Titles "Why [Star] … 😳 #nba"** | **Unproven** | Pooled across 13 channels: question titles 0.88x (n=329), "Why" 0.95x (n=69), star named 0.96x (n=813), emoji 1.00x. On CoachClank, titles naming a star have a 260K median, against 568K without [V]. Shorts titles are a small factor | Test "He/This" titles without the name against named ones; don't treat titles as a lever |
| Flop: rule/policy topics | **Too broad** | Finding 4 [V] | Ban paperwork rules only |
| Flop: future questions | **Supported** | Ours: #46 50%, #21 64% [V]. Rebound Rewind "Will Cade Cunningham win ANY NBA Award this season?!" 0.36x [V] | Keep |
| Flop: news a day late | **Supported (n=1 ours)** | #63 57.6%, 1.4K [V]. News titles on Rebound Rewind sit at about half its evergreen median (Q4) [V] | Keep: same day or not at all |
| Flop: soft black-and-white frame 1 | **Plausible, n=1** | #52 [V]; also confounded with a weaker star | Keep as a QA check |
| **Stayed % as the main metric** | **Necessary, not sufficient** | 10K+ needs 74%+ [V], but #40 held 81% and got 1.6K | Add share of Shorts at 100K+ |

**Big things we aren't doing at all:**
1. **The "one clip, one oddity" explainer** (CoachClank's lane, finding 3). It's in our skills (`nba-short`) but it isn't a lead format.
2. **Transgression and conflict stories:**
   - caught cheating, banned, illegal (finding 4);
   - "he played dirty, so [star] got even" revenge arcs: 5-23M for Korzemba's first 6.
3. **A format rotation and retirement rule** (finding 2).
4. **Re-cutting and reposting winning concepts with a new opening.** Ahmed reposts concepts constantly, and his 4.1M and 4.6M hits were repeat airings.
5. **Any length test above 33 s** (finding 5).
6. **A music A/B test.** We dropped music on Oct 14 by owner decision, without data.
7. **Rankings with a hard measure** ("Every NBA Team's Tallest Player Ever", "The best NBA player at every age"):
   - Rebound Rewind: 869K, 542K, 448K against a 190K median;
   - pooled number-list starts: 1.17x, above the median on 6 of 6 channels;
   - record and stat titles: 1.63x (n=63). [V]

---

## The specific questions

### Q1. Do AI-voiced NBA Shorts get suppressed or monetized less?
**No evidence of either.**
- The largest narrated NBA Shorts channels run fast AI voices (finding 6).
- YouTube's policy pages don't name AI voice as a problem. Disclosure "won't limit a video's audience." [V]
- YouTube's Rene Ritchie says the recommendation system doesn't factor in monetization status, and AI content alone isn't a disqualifier (vidIQ episode summary, Mar 30, 2026). [H, summary only]
- Shorts pay by share of engaged views, so the voice can't change the rate per view. [V]

**The real risks are at channel level:**
- template or mass-produced content: "a channel with too much of these content types will not be able to monetize" (Halprin, Jul 2026); [V]
- clips without commentary (reused content). [V]

**Audience reception:**
- 0 of 180 top CoachClank comments mention the voice. [S]
- Reddit (our usual source for creator complaints) was unreachable from this server, so I have no first-hand creator reports.

### Q2. Is music better or worse for narrated NBA Shorts?
**Nobody has measured it.**
- **Views:** no independent study compares Shorts with and without music. OpusClip's 13.5M-clip study found music in only 1.9% of clips and reported no effect. [S]
- **What the big channels do:**
  - Ahmed's network: a quiet bed about 20 dB under the voice. [V]
  - CoachClank: not verified by ear.
  - Courtside, Score 81 and Chaz NBA (no narration): run game audio or music. [S/H]
  - Our old-era hits all had beds, but so did the weak control (Music Guide). [S]
- **Money [V official]:**
  - Only "content made available or claimed by YouTube's music industry partners" cuts the pool share: one track halves it.
  - A royalty-free bed that isn't partner music (an ElevenLabs Music bed, Mixkit) does **not** cut it.
  - A commercial song from the Shorts library does.
- **Verdict:** "no music" is a reasonable default for pay, not a proven retention rule.
- **Test:** 5 paired posts, the same cut with and without a royalty-free bed at -20 dB, dipped under the turn. Compare stayed % at 48 h.

### Q3. Is 20-30 s right, or do 45-60 s story Shorts win now?
**Neither is proven for us.**
- CoachClank's best band is 31-45 s. [S]
- Ahmed runs 60-105 s, but his NBA channel is fading:
  - median 102K over his last 300 posts, against 159K all-time (CSV); [V]
  - 1% of his last 295 reached 1M, against 5.8% all-time. [V]
- Our soccer story S01 (60 s) got 30K with 80.4% stayed. The other two, at 64-71 s, held 56-65%. [V, n=3, soccer]

**Best evidence-based plan:** a 35-45 s band for stories with two turns, 20-28 s for single-paradox Shorts, never over 58 s.

### Q4. Same-night news or evergreen: which is the better engine?
**Evergreen is the steadier engine. News works only as a fresh moment with a timeless angle.**
- **Rebound Rewind** (the one big channel that switched to news recaps this month):

  | Rebound Rewind Shorts | n | Median views |
  |---|---|---|
  | **News / timely titles** | 26 | **133.5K** |
  | Evergreen titles | 88 | 245K |
  | Debate questions | 31 | 189K |

  Its "NBA Day 2 Recap" and "Opener Recap" posts sit at 105-161K, against a 190K channel median. Those two are only days old, but the older news posts in the n=26 group trail too ("Ben Simmons Returns" 149K, "The Clippers are DOOMED" 89K). [V]
- **Score 81:** went from current-game edits (median about 25-32K) to legend and nostalgia edits; its last 25 posts have a 569K median.
  - Within its newest 100, nostalgia titles get a 340K median against 65K for current ones.
  - Confounded by season timing. [V numbers, H cause]
- **CoachClank, the counter-example:** it uses *this season's* clips, but frames each one as a timeless oddity. Legend titles there get a 95K median against 536K. [V]
- **Ours:** #58 (same-day news plus a number gap) at 23K is our best recent post, but #63 (a day late) got 1.4K. [V]
- **Verdict:** keep news as a second engine. It must be the same day, about a household name, with a number paradox. The best mix is last night's clip with an evergreen question.

### Q5. Which hook types dominate?
**Hooks that point at something on screen and promise a specific answer. The type of sentence matters less.**

**CoachClank's top 11 line 1s [S]:**

| Hook type | Count | Example |
|---|---|---|
| "This" plus a claim about the clip | 5 | "This is why people think LeBron is selfish" |
| A norm, then the break | 2 | "When a player is close to a triple double, their teammates usually…" |
| A concrete question about the clip | 2 | "Why did this player miss this free throw on purpose?" (10.5M) |
| A reputation claim | 1 | "Kobe Bryant was known for not respecting his teammates" |
| A scene | 1 | |

**Its bottom 4:**
- hypothetical or speculative questions ("Have you ever wondered…", "Fans are wondering…");
- a vague line ("This video shows you how good NBA offenses are");
- a withheld payoff.

**At title level, pooled across 13 channels (n=2,772) [V]:**

| Title shape | Lift (x own local median) | Channels above median |
|---|---|---|
| Starts with a number list | 1.17x | 6 of 6 |
| Starts "This/These/The" | 1.05x | 6 of 9 |
| Question titles | 0.88x | 2 of 12 |

**Our #42 accusation hook is a reputation-clash claim.** That fits the winning shape.

### Q6. Copyright on NBA footage: what creators and the league say
- **The NBA's stated line:**
  - "highlights are marketing" (Adam Silver, 2015-16);
  - the NBA told Awful Announcing it didn't launch the FreeDawkins takedown. [S]
- **NBA Playmakers (BBTV):** a league-backed creator network since 2016. Golden Hoops' founder: "In 2017, I signed with NBA Playmakers, which allowed me to monetize my NBA videos on YouTube." I couldn't confirm that it still runs in 2026. [H]
- **A sports-business analysis:** many creators accept the claim and use the clips for audience growth. [H]
- **For us:** under 60 s, a claim can't block a Short, and a non-music claim doesn't cut the pool. [V]

---

## The Ahmed's Basketball CSV: top quartile vs bottom quartile

**Method:**
- 1,170 Shorts (the 5 under 10 days old are dropped).
- Views are lifetime totals, so newer Shorts are undercounted. I scored each Short as **its views ÷ the median of the 101 Shorts around it in upload order** (an age adjustment).
- **Quartiles on that score:**
  - top quartile: 2.02x or more; n=293; raw median 555K;
  - bottom quartile: 0.56x or less; n=293; raw median 60K.
- The base rate is 25% in each. Raw medians are shown too; where they disagree, the age-adjusted number is the one to trust.
- Script: `/tmp/claude-0/-home-user-metasports-shorts/fd2d646b-e100-5ee6-a7bb-3b5b53e3f69a/scratchpad/scripts/ahmed_q.py`.

**Topics and title shapes most over-represented in the TOP quartile [V]:**

| Feature | n | Raw median | Age-adj. median | % top Q | % bottom Q |
|---|---|---|---|---|---|
| NBA 2K / shoes / brands | 15 | 173K | 2.37x | **60%** | 7% |
| Jersey / numbers / iconic | 11 | 226K | 1.08x | 45% | 9% |
| "…look fake but are 100% real" | 21 | 270K | 1.08x | 43% | 24% |
| Legends / GOAT / Hall of Fame | 16 | 258.5K | 1.51x | 38% | 19% |
| Relationships (friends, childhood hero, family) | 27 | 173K | 1.30x | 37% | 22% |
| Draft / picks | 59 | 228K | 1.10x | 34% | **14%** |
| Trades / free agency | 65 | 197K | 1.31x | 34% | 22% |
| "Almost / nearly / before they were" | 58 | 186.5K | **1.38x** | 33% | **16%** |
| Rivalry / hated / betrayed | 52 | 206K | 1.33x | 33% | 15% |
| Opens "Players who/that" | 80 | 236K | 1.10x | 34% | 22% |
| College / high school / scouted (tiny n) | 8 | 831.5K | 5.22x | 62% | 12% |

**Most over-represented in the BOTTOM quartile [V]:**

| Feature | n | Raw median | Age-adj. median | % top Q | % bottom Q |
|---|---|---|---|---|---|
| Injury / tragedy / sad | 24 | 106.5K | 1.00x | 21% | **46%** |
| Coaches / refs / owners / GMs / fans | 58 | 110K | **0.73x** | 17% | **38%** |
| Retirement / comeback | 23 | 187K | 1.20x | 30% | 35% |
| Money / contracts | 64 | 90K | 0.88x | **14%** | 31% |
| Contrast word in title (but/still/anyway) | 170 | 132K | 0.97x | 26% | 32% |
| Question titles | 17 | 119K | 0.96x | 18% | 29% |
| "Episode N" series tag | 129 | 176K | 0.87x | 24% | 29% |
| "Craziest / strangest / weird" | 83 | 144K | 0.83x | 18% | 27% |
| "In NBA history" | 226 | 164.5K | 0.86x | 19% | 25% |

**No effect once age is controlled (all within ±5 points of 25%):**
- CAPS words (n=570)
- a digit (n=162)
- title length: 6-8 words (n=492) against 12+ (n=142)
- the "Basketball players" opener: 77K raw, but **0.99x adjusted**, so its low raw median is an age artifact.
- Earlier notes called money "0.58x". Adjusted it is 0.88x: still weak, but less extreme.

**What this means for us:**
- **Topics to favour:** draft, "almost", rivalry, brands/2K, iconic numbers, legends.
- **Topics to avoid:** tragedy, injuries, money, owners/coaches/refs.
- **Biggest lesson:** a concept can be posted again with a better opening. Most of the spread is within a concept (finding 1).
- **Ahmed is fading on NBA:** a 102K median over his last 300 posts, and uploads cut from 84-86 a month (Jul-Aug) to 29 in September and 10 so far in October. The monthly counts use the interpolated dates from `analysis_output.txt`, so they are approximate. He is not a model to copy wholesale. [V]

---

## Per-channel notes (12 NBA Shorts channels that aren't official league or team accounts)

**How to read this:**
- Subs and 28-day views: vidIQ public pages (Oct 23-24).
- Shorts medians: today's listing (newest 5 skipped).
- Voice, music and length were **not heard or measured today** (YouTube watch pages are bot-blocked here). Where they're given, they come from our Oct 4-15 measurements (Round 3/5/9, Competitor Script Breakdown) or are marked as inferred.

| Channel | Subs | Views, last 28 d | Shorts median (n) | Top 10% median | 1M+ share | Format |
|---|---|---|---|---|---|---|
| **Score 81** | 296K | **50.3M** (+19K subs) | 36.5K (196); **last 25: 569K** | 1.7M | 9% | music edits of moments, no narration [H, from titles] |
| **Chaz NBA** | 665K | 35.7M | 145K (276) | 882K | 4% | raw funny or candid clips + caption title |
| **Golden Hoops** | 2.24M | 12.4M | 45K (275); last 50: 22.5K | 906K | 5% | mixed edits and news; NBA Playmakers partner |
| **Courtside Films** | 809K | 11.0M | 285K (187) | 5.2M | 26% | Top-10 countdowns, high school; no voice |
| **CoachClank** | 145K | 8.9M | **419K (295)** | **9.15M** | **34%** | one-clip oddity explainer, AI voice |
| **Rebound Rewind** | 236K | 6.7M | 190K (295) | 1.0M | 5% (80% hit 100K+) | rankings/explainers, now daily recaps |
| **Ahmed's Basketball** | 121K | 4.1M | 100K (295) | 578K | 1% | list title, one story, 60-105 s |
| **HoopFlix** | 843K | 3.25M | 161.5K (178) | 5.75M | 16% | "3 …" lists, banned/expensive/LeBron |
| **Mike Korzemba** | 1.86M | 1.28M (0 subs) | 49K (131); last 50: 18.5K | 5.05M | 21% | revenge narratives (series burned out) |
| **Hoop Facts** | 51K | 0.59M | 37K (233) | 685.5K | 3% | stat rankings and facts |
| **Hoops Lore** | 16.3K | n/a | 42K (62) | 1.6M | n/a | reposted podcast/interview clips |
| **REBOUND** | 3.36M | n/a (no vidIQ page) | 972K (54; Shorts dated 2022-23) | 20M | n/a | narrated "3 …" rule/ban lists |
| *MetaSports (us)* | about 600 | about 0.5M (17.3K a day) | about 3.5-4.6K | | 0% | #42 format and news paradoxes |

**Also seen, but not core benchmarks:**
- NBA Facts (33K subs; a French-origin facts channel; 58K median)
- B Story (266K; Korean-language)
- THE NBA STORYTELLER (64.8K subs but a 2.5K Shorts median)
- bball explained, Nick Smith NBA, Med (almost no Shorts)

**Shorts views barely become subscribers in this niche:**

| Channel | Subs gained | Views (28 d) | Subs per 1,000 views |
|---|---|---|---|
| CoachClank | 1K | 8.9M | 0.11 |
| Ahmed's | 1K | 4.1M | 0.24 |
| Score 81 | 19K | 50M | 0.38 |
| **Us** (Oct 17-23) | 47 | 120.8K | **0.39**, already at par [V] |

### CoachClank
- **Format:**
  - one real-game clip explained;
  - fast AI voice, 265-309 wpm;
  - small white sentence-case captions, 3-4 words, centred;
  - 16:9 footage on a blurred 9:16 background.
  - 12-35 s; best band 31-45 s. [S]
- **Titles and cadence:**
  - 2-6 words (mean 5.4), often "He…/This…" plus an emoji, no hashtag;
  - about 6 a week (Oct 4 measurement).
- **Top vs weak:**
  - **Top:** a visible on-court oddity, a size gap or an "IQ" play.
  - **Weak:** wholesome fan or mascot stunts, celebrity stunts ("She Tried Picking Up Shaq", 8.1K), abstract claims ("Why Steph Curry Is the Hardest Person to Guard", 13K), banned shoes or haircuts with nothing to see, speculative questions. [V titles, S transcripts]
- **Still working:** the last 50 posts have a 386.5K median.

### Score 81 (the current momentum leader)
- **Numbers:** 50.3M views and +19K subs in 28 days.
- **The shift:** its median jumped from about 25-32K (positions 75-200) to 569K over its last 25 posts. The playoff-news edits went ("Cavs Eliminated PISTONS", 5K). Legend and nostalgia edits came in:
  - "Kobe Gives Dirk His Respect" 1.8M
  - "MJ Was One Of One" 1.4M
  - "All-Star Game NOW vs THEN" 1.0M
  - plus "They Made Wemby The Villain" 15M [V]
- **Format:** 3-6 word emotive titles plus an emoji. The format is inferred as music edits without narration; I didn't watch it. [H]
- **Lesson:** emotion and nostalgia with no words can out-reach any narrated channel right now.
- **Not for us to copy directly:** edits without commentary carry reused-content risk for monetization.

### Chaz NBA
- **Format:** candid star moments (warm-ups, bench, mic'd up) with a caption-style title ("LeBron James really faked a fist bump and laughed when he fell", 2.4M).
- **Scale:** 4,550 videos, about 1.5 a day over its lifetime; 66% of Shorts reach 100K, but only 4% reach 1M.
- **Weak:** stat lines ("Scottie had 25 BOARDS", 28K) and injury news ("JOKIC OUT 4+ WEEKS", 20K). [V]

### Rebound Rewind
- **Format:**
  - animated explainers and rankings, about 67 s; [S]
  - the title is the only caption, and spoken words aren't captioned (Round 9 watch);
  - every title carries "#nba".
- **Top:** "LeBron James is so Old…" (5.3M), "NBA Players who NEVER:" (4.8M), "The best NBA Player from Youngest to Oldest" (3.3M).
- **Bottom:** "New NBA Rule for the Upcoming Season!", MVP opinions, hecklers.
- **Its October recaps underperform** its evergreen posts (Q4). [V]

### Ahmed's Basketball
See the CSV section above.
- **Format:**
  - the title read aloud as line 1, then "Back in [year]…";
  - one story behind a plural list title;
  - about 258-274 wpm;
  - a quiet music bed;
  - small white captions;
  - archive footage plus AI images;
  - 60-105 s (median 70). [V/S]
- **Fading on NBA** (102K median over his last 300 posts); uploads cut sharply in Sep-Oct 2026. [V]

### HoopFlix
- **Format:** "3 …" lists and provocative LeBron claims: "Most Expensive Shoes NBA Players Wore In Games" (14M), "LeBron James was almost KILLED" (8.6M), "BANNED Food In The NBA" (8.5M), "The NBA is LYING About LeBron James" (7.6M).
- **Weak:** "this season" lists, lawsuits, fan reactions (7-20K).
- **Volume:** 308 videos in 13 years. Few posts, high ceiling. [V]

### Mike Korzemba
- **Format:** revenge arcs ("He Played Dirty, So Giannis ENDED His Career", 23M) and "The Only Teammate Kobe Bryant Never Forgave" (10M).
- **The warning:**
  - the series was repeated about 17 times until it died (finding 2);
  - the latest upload was Oct 2;
  - 0 subs gained in the last 28 days. [V]
- **Voice:** a long-form personality, so probably his own voice on Shorts. Unverified. [H]

### REBOUND
- **Format:**
  - narrated "3 …" lists about rules, bans and cheating, with ALL-CAPS words plus "..";
  - one-word captions with a green highlight;
  - top Shorts about 53 s, the rest about 35 s. [S, Oct 4]
- **Activity:** its Shorts date from 2022-23, so it is not active on Shorts now. Still the clearest proof of the transgression theme (42M, 36M). [V]
- **Founder:** Dillon Baheri, 2016 (Greenlight Group page). [H]

### Courtside Films
- **Format:** countdown compilations ("TOP 10 BACKBOARD SHATTERING DUNKS OF ALL-TIME!", 41M), high-school stars; no narration, only a rank label; about 65-75 s; game audio or music. [S]
- **Volume:** 6,967 videos. 26% of its Shorts reach 1M.
- **Weak:** generic repeats ("Top 10 NBA Dunks EVER!", 45K) and unknown high-school players. [V]

### Golden Hoops
- **Who:** Valdemar Dahl, since 2011.
- **What he says:**
  - "consistency is key";
  - he has posted daily since 2019;
  - "I know a lot of my viewers like it when I cover last night's events";
  - he monetized through NBA Playmakers. (Tubefilter, 2022) [S]
- **Now:** Shorts are weak. A 45K median and 22.5K over the last 50 posts, with one 11M tabloid outlier. [V]

### Hoop Facts
- **Format:** stat rankings; ALL-CAPS captions with yellow on the key number; 15-62 s, with no length effect. [S]
- **Top:** Shaq memes (3.1M) and hard-measure rankings ("Highest Career 3pt% In NBA History", 1.8M; "The NBA's Worst Stats!", 1.3M).
- **Bottom:** niche or vague titles ("NBA's All-Time Lane Violations Leaders!", 4.7K; "This Story is HILARIOUS!", 1.9K). [V]

### Hoops Lore
- **Format:** reposted podcast clips with long question-plus-emoji titles.
- **Top:** famous-name fight and locker-room stories ("Iman Shumpert details the fight between Carmelo Anthony and Kevin Garnett", 9.4M).
- **Bottom:** current role players' feelings (7-15K).
- **Not a model:** it's the reused-content shape YouTube targets. [V/S]

**What the top Shorts share across channels:**
- a concrete event you can see (a play, a fight, a cheat, a size gap), or a ranking on a hard measure;
- conflict or transgression;
- a legend or household name *in the video*, even when the title hides the name.

**What the weak ones share:**
- feelings and abstractions;
- policy;
- speculation or the future;
- injury and tragedy news;
- money;
- owners, coaches and refs (unless they're caught cheating);
- a sequel after the 3rd entry;
- empty adjectives ("disrespectful", "savage", "crazy") with no object.

---

## How this was done, and what I couldn't reach
- **Channel data:**
  - `yt-dlp --flat-playlist` on each channel's `/shorts` tab (up to 300 newest, titles and views only) and on YouTube channel search.
  - Scripts and raw data: `/tmp/claude-0/-home-user-metasports-shorts/fd2d646b-e100-5ee6-a7bb-3b5b53e3f69a/scratchpad/` (`chans/*.jsonl`, `scripts/pooled.py`, `scripts/chstats.py`, `scripts/ahmed_q.py`, `scripts/ahmed_dupes.py`).
- **Pooled title analysis:** each Short's views ÷ the median of the 41 Shorts around it on the same channel (n=2,772, 13 channels).
- **Not reachable:**
  - Per-video pages (duration, transcripts, upload dates): YouTube's bot check, plus 403/429 errors.
  - Reddit (old.reddit.com and reddit.com): 403, and WebFetch is blocked.
  - Social Blade: 403.
  - Third-party transcript sites: Cloudflare.
  - So there are **no first-hand Reddit or X creator reports** in this study. The "creators say" evidence is limited to Tubefilter interviews (Golden Hoops, Korzemba), YouTube's own creator talks, and our earlier transcript work.
- **Caveats:**
  - Lifetime views favour older Shorts. vidIQ figures are rounded public counts.
  - Listings show only what each channel still has public. Deleted flops are invisible (survivorship bias).
  - Every title-level pattern is a correlation, not a cause.

---

## Sources

**Official YouTube:**
- Channel monetization policies (reused, inauthentic/templated, sports-replay example): https://support.google.com/youtube/answer/1311392
- Shorts monetization (music = partner content; non-music claims not credited; over 1 min with claims blocked): https://support.google.com/youtube/answer/12504220
- Three-minute Shorts and Content ID blocking: https://support.google.com/youtube/answer/15424877
- Altered or synthetic content disclosure ("won't limit a video's audience"): https://support.google.com/youtube/answer/14328491
- YouTube Blog, Aug 10, 2026, YPP changes from Feb 1, 2027: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- Todd Sherman and Jenny Hoyos, Shorts deep dive: https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/

**Press and interviews:**
- TechCrunch, Jul 20, 2026, inauthentic-content clarification (Halprin): https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- NetInfluencer, Halprin's three categories: https://www.netinfluencer.com/youtube-trust-and-safety-chief-details-three-categories-of-content-barred-from-monetization/
- Search Engine Journal, 2027 payout rules: https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/
- Search Engine Journal, Todd Sherman on the Shorts algorithm (2023): https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/
- TechCrunch, Shorts series feature (Sep 23, 2026): https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/
- Tubefilter, Golden Hoops / Valdemar Dahl (2022): https://www.tubefilter.com/2022/02/03/youtube-millionaires-golden-hoops/amp/
- Tubefilter, Mike Korzemba profile: https://www.tubefilter.com/?p=165547
- NBA and BBTV, Playmakers launch (2016): https://pr.nba.com/nba-broadbandtv-playmakers
- Sports Illustrated, NBA highlight channels (2016): https://www.si.com/extra-mustard/2016/02/09/nba-highlight-videos-clips-youtube-legality
- Awful Announcing, FreeDawkins: https://awfulannouncing.com/nba/freedawkins-youtube-channel-nba-videos-vanish.html
- SVG, NBC's AI Jim Fagan voice (made with family consent): https://www.sportsvideo.org/2025/05/06/nbc-sports-to-feature-ai-generated-voice-of-former-narrator-jim-fagan-in-its-upcoming-nba-coverage-and-promotion/
- Flippa, a sold NBA Shorts channel (@DBall1, 113K subs, 350M views; slug only): https://flippa.com/12057981
- Sportsepreneur, creators accepting claims: https://sportsepreneur.com/how-youtubers-are-monetizing-sports-content-without-owning-it/

**Studies:**
- Paddy Galloway, 5,400 Shorts / 3.3B views: https://threadreaderapp.com/thread/1646898356419981315.html
- quso.ai, 108K Shorts, length vs median views: https://quso.ai/research/youtube-shorts-length
- OpusClip, 13.5M clips: https://www.opus.pro/research/how-to-go-viral-youtube-shorts

**Channel stats (vidIQ, Oct 23-24, 2026):**
- CoachClank: https://vidiq.com/youtube-stats/channel/UC7Nw5ntgYhrUnws0zJCUyTA
- Ahmed's Basketball: https://vidiq.com/youtube-stats/channel/UCtfUw7OHpsgOpVro_atMmUg
- Score 81: https://vidiq.com/youtube-stats/channel/UCxwQAQ2j6sIoHYHFMF2CI_A
- Chaz NBA: https://vidiq.com/youtube-stats/channel/UChgDp_uE5PVqnpdV05xKOOA
- Golden Hoops: https://vidiq.com/youtube-stats/channel/UCoDfZzwJNFJ2lVgF41tUX0A
- Courtside Films: https://vidiq.com/youtube-stats/channel/UCQPp7FYJUkw0Xk2Pr-6irOA
- Rebound Rewind: https://vidiq.com/youtube-stats/channel/UCt8McXkBAcops8ZdFj2LnVQ
- HoopFlix: https://vidiq.com/youtube-stats/channel/UC1Wt-vBY7SOjROTUMJHsp5Q
- Mike Korzemba: https://vidiq.com/youtube-stats/channel/UCp3dgMf1OUP2XqOpyOY2bzQ
- Hoop Facts: https://vidiq.com/youtube-stats/channel/UCFEwO714Se45wz5NMnYw4ag

**Shorts tabs pulled:**
- https://www.youtube.com/@CoachClank/shorts
- https://www.youtube.com/@AhmedsBasketball/shorts
- `youtube.com/channel/<id>/shorts` for the channel IDs above, plus:
  - REBOUND UCVepIJedg6BMQeSgjPY4e6A
  - Hoops Lore UCwdOA-ZRZ9Ihpo6Wfar5wbQ
  - NBA Facts UCLLjYvvXf8BHZd6kwUhTAtg
  - B Story UC-2uQeZQoX6OJwZ5mswZReA

**Internal:**
- `Library/THE 42 FORMAT.md`
- `Research Notes/NBA Diagnosis (Oct 23, 2026).md`
- `Research Notes/Studio Export Read (Oct 24, 2026).md`
- `Research Notes/NBA Viral Topics + Ahmed Basketball (Oct 23, 2026).md`
- `Research Notes/Ahmed Network Data (Oct 21, 2026)/AhmedsBasketball_shorts.csv`
- `Research Notes/Round 3 - Deeper Findings.md` (CoachClank lengths)
- `Research Notes/Round 5 - Competitor Formulas (Oct 4, 2026).md`
- `Research Notes/Round 9 - Competitor Shorts Watched (Oct 5, 2026).md`
- `Research Notes/Competitor Script Breakdown (Oct 15, 2026)/`
- `Research Notes/Monetization Research (Oct 23, 2026).md`
- `Library/Music Guide.md`
- `MetaSports - Playbook.md`
