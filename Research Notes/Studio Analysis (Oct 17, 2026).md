# Studio Analysis, Oct 17, 2026 (export Sep 19 to Oct 17, owner upload)

**Files:** `Research Notes/Studio exports/Content 2026-09-19 to 2026-10-17/` (`Table data.csv`, `Chart data.csv`, `Totals.csv`). The column names are kept exactly as exported.
**Method script:** reproducible from the CSVs: log10 views, median and MAD, Spearman rank correlation. Same approach as audit §13.
**Labels:** **[V]** = read directly from the export. **[I]** = my inference. **[T]** = a test, not yet proven.

## 1. Validation

| Check | Result |
|---|---|
| Rows | 102 videos plus a Total row. No duplicate IDs. |
| Period | Sep 19 to Oct 17, 2026. The Oct 14 export covered Sep 16 to Oct 14, so the two windows overlap by 26 days. |
| Totals | 179,938 views; 683.6 watch hours; average view duration 0:24; average % viewed 99.15; **stayed to watch 73.32%**; 70 subscribers. The rows sum to 179,830: 108 views sit in rows Studio leaves blank. |
| Blank rows | 21 old-era videos have no views or retention in this window. Only their thumbnail impressions are filled. |
| Units | Duration is in seconds; average view duration is h:mm:ss; the percentages are 0-100+; watch time is in hours. |
| Columns this export has | Views, Duration, Average view duration, Average percentage viewed (%), **Stayed to watch (%)**, Watch time, Subscribers, Thumbnail impressions/CTR |
| Columns missing vs Oct 14 | **Engaged views** and **Returning / Casual / Regular / New viewers**. So engaged-ratio and audience-mix can't be updated. The Oct 14 values stay in audit §13. |
| `Chart data.csv` | Daily **average view duration** for 5 *old-era* videos (Jason Williams, WNBA, court, $0 tickets, copy machine). Most days read 0:00. **It says nothing about the new Shorts and is not used.** |
| `Totals.csv` | Channel average view duration per day: 0:23-0:25 Oct 9-14, then **0:20-0:21 Oct 15-16**. These are the days #44 (86.7% viewed) and #21 (81%) were posted, and they pull the average down. |
| IDs | All 29 new-era rows (Oct 3 onward) match `Posted Tracker (Oct 15, 2026).csv` or a new post (#42 Ro0oa2VLlqA, #46 WWOX4wV-F6g). Publish dates agree. |

**Conflicts with the Oct 14 export** (same video, both windows):
- Views on Shorts older than about 7 days are **unchanged to within 1-3%**: #22 31,831 → 31,832; #03 26,986 → 26,985; #19 20,567 → 21,119. This confirms that views are final after week 1 (audit §13).
- **#39 is the one real change:**
  - views went from 1,983 to 8,592 (about 1 day old → 4.5 days)
  - stayed rose from 70.8% to 77.0%
  
  So "stayed" is not fixed in the first day. It moves as the feed shows the Short to wider audiences.
- **#29:** stayed went from 55.6% to 59.0% (1,451 → 1,903 views).
- Nothing else moved more than 3 points.

## 2. The new-era table (29 Shorts, Oct 3-17; age at Oct 17)

**How it's sorted:** by views.
- **z** = how far a Short's log10 views sit from the new-era median (3,974), in robust standard deviations (1.4826 × MAD; MAD = 0.294 in log10).
- **Tier key:**
  - **E** = exceptional
  - **A** = consistently above
  - **O** = ordinary
  - **U** = under
  - **P** = provisional (under 3 days old)

| Tier | # | Short (ID) | Age d | Dur s | Views | z | Stayed % | Avg % viewed | Subs |
|---|---|---|---|---|---|---|---|---|---|
| E | #22 | Two Men Wear Six (74hpWW4j5AM) | 13.5 | 26 | 31,832 | +2.1 | 82.4 | 115.5 | 7 |
| E | #03 | Wemby vote (9FLigGnYiXE) | 14.5 | 24 | 26,985 | +1.9 | 80.2 | 104.0 | **16** |
| E | #19 | Flagg height (V8EoO4g7s_k) | 11.5 | 22 | 21,119 | +1.7 | 74.0 | 101.8 | 6 |
| A | #23 | LeBron vs son (21CMU55yJTE) | 6.5 | 27 | 10,403 | +1.0 | 76.1 | 104.1 | **13** |
| A | #39 | Oldest triple-double (hde8nIE1J4Y) | 4.5 | 23 | 8,592 | +0.8 | 77.0 | 113.3 | 2 |
| A, P | #44 | $8M rookie carries bags (p1lVXskwifQ) | 2.5 | 21 | 7,812 | +0.7 | 69.7 | 86.7 | 3 |
| A, P | **#42** | **Most missed shots (Ro0oa2VLlqA)** | **1.5** | 24 | **6,262** | +0.45 | **84.3 (channel record)** | 95.4 | 7 |
| A | #41 | Taller than Wemby (Wn80c_nRQ9I) | 3.5 | 24 | 6,259 | +0.45 | 74.9 | 84.1 | 2 |
| O | #17 | Flopping (iaRj9O1g-uA) | 9.5 | 29 | 6,753 | +0.5 | 70.9 | 81.3 | 3 |
| O | #15 | Adams GTA (Jbo4jxfz0yw) | 11.5 | 23 | 5,982 | +0.4 | 66.2 | 94.9 | 1 |
| O | #24 | Bronny spot (AwmPdOf5cqc) | 12.5 | 29 | 5,747 | +0.4 | 68.4 | 97.1 | 1 |
| O | #34 | 2007 picks (Ctm9TiDMl4k) | 5.5 | 22 | 5,620 | +0.35 | 60.4 | 98.3 | 0 |
| O | #40 re-upload | Jokic pass (FYsYrJ2fJbo) | 2.5 | 24 | 4,163 | +0.05 | 79.4 | 91.5 | 3 |
| O | #01 | 92% pay cut (1hxiFdH0ddA) | 8.5 | 24 | 3,974 | 0.0 | 74.5 | 109.4 | 5 |
| U | #35 | Wemby rugby | 8.5 | 26 | 2,914 | -0.3 | 61.3 | 78.7 | 1 |
| U | #18 | Helicopter | 13.5 | 27 | 2,912 | -0.3 | 66.6 | 89.2 | 1 |
| U | #16 | Giannis Vice City | 10.5 | 26 | 2,902 | -0.3 | 65.9 | 80.3 | 1 |
| U | #12 | Duren $87M | 14.5 | 33 | 2,855 | -0.3 | 69.4 | 71.1 | 1 |
| U | cup | NBA Final doesn't count | 12.5 | 23 | 2,338 | -0.5 | 51.5 | 72.7 | 0 |
| U | #25 | Bronny better | 11.5 | 25 | 1,949 | -0.7 | 63.6 | 68.4 | 0 |
| U | #29 | Underhand | 5.5 | 24 | 1,903 | -0.7 | 59.0 | 94.9 | 0 |
| U | #13 | Kawhi picks | 9.5 | 23 | 1,882 | -0.75 | 50.0 | 91.8 | 2 |
| U | #21 | Jokic by Christmas | 2.5 | 26 | 1,796 | -0.8 | 63.7 | 81.0 | 2 |
| U | #20 | Bad Boys | 7.5 | 27 | 1,643 | -0.9 | 47.8 | 64.7 | 0 |
| U | #14 | Four stars | 10.5 | 24 | 1,616 | -0.9 | 63.1 | 115.3 | 1 |
| U | #40 original | Jokic pass (mqpMv7EH7b8) | 3.5 | 22 | 1,515 | -1.0 | **81.0** | 97.4 | 0 |
| U, P | #46 | LeBron fourth team (WWOX4wV-F6g) | 0.5 | 22 | 1,331 | -1.1 | **49.8** | 81.9 | 1 |
| (out) | #25r | Bronny repost | 4.5 | 25 | 196 | | 63.2 | 79.0 | 0 |
| (out) | #11 | Jordan last shot | 13.5 | 25 | 39 | | 56.3 | 64.4 | 0 |

**Age normalization:**
- Views stop growing after about 5-7 days (section 1), so Shorts 7+ days old are final.
- For the young ones, the fair comparison is **views at the same age**, from the daily public checks in the Outcome Log plus this export:

| Short | about 1 day | about 1.5 days | about 2.5 days | about 3.5-4.5 days |
|---|---|---|---|---|
| #44 | 4,300 | 6,700 | 7,812 | |
| **#42** | 3,100 | **6,262** | | |
| #39 | 1,983 | (about 5K) | 7,500 | 8,592 |
| #41 | 1,700 | 2,300 | 5,300 | 6,259 |
| #40 re-upload | 797 | 2,700 | 4,163 | |
| #21 | 1,200 | 1,500 | 1,796 | |
| #40 original | 752 | 1,200 | 1,400 | 1,515 |
| #46 | 1,331 at 0.5 day | | | |

**[V] At the same age, #42 (6.3K at 1.5 days) and #44 (6.7K) are the two fastest starts since #22/#03.** #42 also has the highest stayed % the channel has recorded.

## 3. What moves with views (Spearman, new era, 1.5+ days old, 500+ views, n=26) [V]

| Measure vs views | rho now (n=26) | rho Oct 14 (n=20) |
|---|---|---|
| **Stayed to watch (%)** | **+0.63** | +0.77 |
| Subscribers (an outcome, not a cause) | +0.74 | |
| Average % viewed | +0.44 | +0.51 |
| Words per minute (n=19 with a script on file) | +0.40 | |
| Days since publish | +0.09 | +0.27 |
| Duration (21-33 s) | -0.06 | -0.05 |

**Readings:**
- **[V] Stayed is still the strongest single correlate, but weaker with more data (0.77 → 0.63).**
  - The new counter-example is **#40**: one video, two uploads, 81.0% and 79.4% stayed, 1,515 vs 4,163 views.
  - **Same file, same retention, 2.7x the views.** So a high stayed % is necessary, not sufficient. Distribution luck (the first test audience, posting hour, the hashtags "#nba" vs "#nba #basketball") is real and outside our control.
  - **Retention is the part we can control.**
- **[V] Every Short at 74%+ stayed got 3,974+ views** (9 of 9, excluding the #40 original).
- **[V] Every Short under 60% stayed got under 2,400 views** (4 of 4: Bad Boys, Kawhi, cup final, #46 provisional).
- **[V] Length still does nothing in the 21-33 s range** (-0.06).
- **[I] Words per minute +0.40 is confounded:**
  - #22, the fastest script (292 wpm), is the biggest hit
  - Bad Boys, the slowest (210 wpm), is near the bottom
  
  Faster scripts are also the tighter, one-measure scripts. Don't speed up the voice because of this.
- **Average % viewed and stayed disagree on some Shorts:**
  - **#14:** 115% viewed but 63% stayed (1.6K). Rule nuance: the few who stayed rewatched.
  - **#44:** 87% viewed but 70% stayed (7.8K). Famous name: many stayed, and fewer finished.
  
  [I] Stayed decides reach, average % viewed decides little. **The first 2 seconds matter more than the last 5.**

## 4. Outlier comparisons

### Positive: #42 "Who Has Missed The Most Shots In NBA History?" (Ro0oa2VLlqA), Oct 16, 24 s, 6,262 views at 1.5 days, **84.3% stayed** (record), 95.4% viewed, 7 subs
- **Premise:** the all-time scorer is also the all-time misser. A paradox about the most famous name in the sport.
- **Hook (line 1):** "LeBron James has missed more shots than anyone in NBA history."
  - One sentence, an absolute ("more than anyone"), a famous name, a mild insult that viewers want to dispute. Clear by about 2.7 s.
- **First visual:** LeBron shoots a three that **falls short** (an airball). The picture proves the claim in frame 1. Kept silent, with no rim sound.
- **Structure:**
  1. claim
  2. number (15,541)
  3. contrast ("And he's the all-time leading scorer")
  4. the old record (Kobe)
  5. a human tie-in (passed it the night he first played with his son)
  6. the viewer's question out loud ("So is he a worse shooter? No.")
  7. proof (51% vs 45%)
  8. payoff: one number (31,502 attempts)
- **Narration:** Alex, one take, about 82 words. Numbers are spoken in full.
- **Visuals:**
  - 12 shots in about 23 s (one every 1.9 s)
  - every shot shows the player the line names
  - **words over footage** for the numbers (LEBRON 50.7% / KOBE 44.7% / 31,502 / Kareem 28,307), with no cards
- **Music:** the v3 render had a Yuke instrumental bed with a dip on "No." (`_v3/music.json`). **Which variant the owner uploaded is not recorded.** Ask before treating music as a factor.
- **Explanation [I]:** it combines every high-stay ingredient: a famous name, an absolute claim, a paradox, a question by 8 s, a number-sized answer, and footage that proves line 1.
- **Replicate:**
  - an "insult or paradox" about an all-time great, answered in his favour
  - frame 1 that shows the claim happening
  - a spoken question then "No."
- **Don't copy:** LeBron-on-LeBron. He is now in 7 of our last 12 Shorts (#23, #24, #01, #18, #36, #42, #46). #46 (LeBron, 49.8%) suggests the name alone does not carry.

### Positive: #44 "$8M rookie carries bags" (p1lVXskwifQ), Oct 15, 21 s, 7,812 at 2.5 days, 69.7% stayed, 86.7% viewed
- **Premise:** a status contradiction (rich, famous, still hazed), with a human answer.
- **Hook:** "Cooper Flagg's teammates still make him carry the bags." A visible, funny act about a famous young name.
- **Explanation [I]:** the topic is human and visual. Stayed is only middling, so the reach came from topic appeal (Flagg + money + hazing) more than the opening.
- **Weak spot:** 86.7% viewed. The middle (Macao, Rookie of the Year) is a list of status items, and viewers leave before the quote.
- **Replicate:** the contradiction of a famous person doing a humble thing.
- **Don't copy:** the list of three status facts in the middle.

### Positive: #39 "Oldest triple-double" (hde8nIE1J4Y), Oct 13, 23 s, 8,592 at 4.5 days, 77.0% stayed, 113% viewed
- **Late climber:** 1,983 on day 1, then 4x by day 4.
- **Hook:** "The oldest triple-double in NBA history lasted twenty-two years." A record with a time twist.
- **Replicate:** a record that lasted an absurd length, and a curious unit (years, not points).

### Positive (control, 7+ days): #22 Six (31.8K, 82.4%), #03 Wemby vote (27.0K, 80.2%, 16 subs), #19 Flagg height (21.1K, 74.0%)
These are covered in audit §5-6. The shared pattern is unchanged:
- one visible object or name
- a paradox
- one measure
- the answer as the end

### Negative: #46 "Can LeBron Win A Title With A Fourth Team?" (WWOX4wV-F6g), Oct 17, 22 s, 1,331 at 0.5 day, **49.8% stayed** (provisional)
- **Hook:** "Only four players ever…" (stat-first, per the Oct 15 critic).
- **Title:** a yes/no future question.
- **First visual:** LeBron's face. The QA flagged LeBron's face on screen for 57% of the runtime.
- **Explanation [I]:**
  - The claim is about a list ("only four players"), not a visible thing.
  - The question can't be answered today, so there is no payoff.
  - It's the third LeBron Short in four days.
  - The Oct 15 critic already called it the weakest visually.
- **Caveat:** under 1 day. Stayed rose 6 points on #39 between day 1 and day 4.
- **Don't repeat:**
  - future-hypothetical premises ("can he win…")
  - a list-of-players opening
  - the same star three times in a week

### Negative: #20 Bad Boys (47.8% stayed), #13 Kawhi (50.0%), cup final (51.5%)
Covered in audit §5: they open on a number with no stakes ("Ninety-two point nine."), a list of penalties, or a rule nobody asked about. **Unchanged.**

### Negative (instructive): #40 original (mqpMv7EH7b8): 81.0% stayed, 1,515 views
Strong retention and weak reach. The same file got 4,163 views as a re-upload a day later. **Outcome: we don't re-upload as a tactic** (it splits views and risks a reused-content flag). We note that one post's reach is noisy, and judge formulas on several posts, never one.

## 5. Channel-wide patterns (correlation, n=26; causation unproven) [I]

| Factor | What the data says |
|---|---|
| **Topic** | Famous names with a **visible** object or act (a jersey number, a vote, a height, carrying bags, missing shots) beat rule and contract topics (Bad Boys, Kawhi, cup final, Duren, four stars: all under 3K). |
| **Hook** | One absolute, curious claim about a famous name, in one sentence ("only", "more than anyone", "still", "never… until"). Openers that start on a number, list or rule sit under 60% stayed. |
| **Emotion** | Surprise, plus a human or flattering answer: LeBron isn't a worse shooter; Flagg sneaks by; father and son. The two biggest subscriber earners (#03 16, #23 13) end on legacy or family. |
| **Subject speed** | Every winner states the subject inside about 3 s. #13 took 6.1 s and #12 took 4.4 s. |
| **Casual clarity** | Winners need no prior knowledge (who wears 6? how tall is he?). Losers need cap rules, CBA penalties or Cup format. |
| **Length** | No effect in 21-33 s (rho -0.06). |
| **WPM** | +0.40, confounded with script tightness (section 3). |
| **Footage variety** | #42 v3 changes shot every 1.9 s, with no card. The card-heavy builds (#13, #20, #29: early cards) are all under 2K. The footage/card choice is confounded with topic, but the direction agrees with competitor practice (section 4 of the competitor breakdown). |
| **Graphics vs footage** | Cards in the first 4 s: every case is under 2K (#13, #29). Words over footage (#42, #36 v4) is the replacement. |
| **Captions** | Constant across the era (house style), so they can't be tested from this data. |
| **Music** | Not recorded per post. We can't attribute anything to it. **Action:** log music yes/no in `UPLOAD.md` and the Outcome Log for every post from now. |
| **Ending** | Answer endings: every Short over 6K. Question endings: #12 and #18, about 2.9K each, and #46 asks a future question. |
| **Timing** | Posting hour isn't in the export. The #40 split suggests reach is noisy day to day. |

## 6. Prioritized findings

**Works best (strong evidence, several posts):**
1. A famous name plus an absolute, visible claim in line 1: #22, #03, #19, #42, #44, #39 (all over 6K).
2. Stayed 74%+ (9 of 9 got about 4K or more).
3. Ending on the answer, ideally a flattering or human one.

**Works poorly (strong evidence):**
1. Openings with a number, list or rule (5 of 5 under 2.4K).
2. Rule, contract or penalty topics needing context (Kawhi, Bad Boys, cup final, Duren, four stars).
3. Question endings and future hypotheticals (#12, #18, #46).

**Strongest evidence:**
- Stayed vs views (rho +0.63 to +0.77 across two exports, with a clear high/low split).
- Views are final after about 7 days (two exports agree).

**Uncertain:**
- music (not logged)
- the voice change (Alex since #42/#44/#46: too few posts)
- wpm
- posting hour
- whether words over footage beats cards (only #42 and #36 v4 use it, and #36 v4 isn't posted)

**Change now:**
1. **Never open on a list or a hypothetical.** The line-1 claim must be something you can **see** in frame 1.
2. **Rotate the star.** No more than 1 LeBron Short in any 4 posts. LeBron was in 3 of the 5 posts Oct 13-17.
3. **Log music, voice and posting hour per post** (Outcome Log columns added today).
4. Treat #44's middle as the warning: **no list of three status facts.** Every line after the hook must move toward the answer.

**Test in the four new Shorts:**
- **T1:** footage-only (zero cards; words over footage only for the one key number) vs the old card builds. Measure: stayed.
- **T2:** the "insult answered in his favour" structure (#42's) on a non-LeBron star.
- **T3:** a visible-object hook (#22's) on a fresh object.
- **T4:** music logged on every post, with a no-music twin kept, so a later comparison is possible.
