# Improvement review, 2026-10-31 (Account 2)

**Data:** private YouTube Analytics pulls dated 10-31 (`Studio exports/api` = NBA, `api FC` = soccer), plus the Oct 29 What's Working Now, both Lessons Learned logs, the 10-31 competitor review, and scripts/notes in `Productions/`. No API was called for this review.

**Samples:** NBA 43 Shorts with views (age 3-27 days; 4 Shorts under 3 days have no numbers). NBA retention curves exist for only **19** of them (Oct 17-28 posts); the rest returned empty. FC 9 Shorts, all with curves.

**Tags:** [V] measured here. [S] seen on 3+ Shorts, topic confounded. [H] hypothesis, fewer than 3 or no control.

**Read these first (caveats that apply everywhere):**
- **Avg % viewed is not "watched to the end".** 14 of 43 NBA Shorts are over 100% (loops). It rewards a clean loop and a short length.
- **Noise is large.** The same Short (Jokic's best pass) got 1.7K and then 6.8K as a re-upload a day later; "Did Bronny Actually Get Better" got 197 and 1,950. One identical-content pair can differ 4-10x, so small view gaps are not evidence.
- **Topic and age confound everything.** 8 Shorts hold 44% of all NBA views.
- **The curve's first bins (1% to 3%) are 0.2-0.7 s on a NBA Short and 1.2-2 s on a 60 s FC Short.** Values above 1.0 are replays.

---

## 1. Retention findings

**NBA, 19 curves [V, n=19, rank correlation with avg % viewed]:**

| Part of the curve | vs avg % viewed | vs views |
|---|---|---|
| Start-of-Short watch ratio at 1% (how often the opening is watched/replayed) | +0.78 | +0.62 |
| YouTube's relative retention at 3% | +0.71 | +0.53 |
| Hold from 10% to 50% of runtime | **+0.74** | +0.19 |
| Hold from 50% to 95% | +0.40 | +0.67 |
| Loss from 1% to 10% | -0.38 | -0.56 (artefact: more replays at the start means a bigger apparent fall) |

- **Early drops are small and similar on NBA.** Every curve keeps 76-89% of its 1% audience by the 10% mark, and nothing predicts views there. What separates 95%+ Shorts from sub-90% Shorts is the **middle** (10% to 50%: median 0.70 vs 0.65, worst cases 0.53-0.59) and the **start replay** (1.77 vs 1.47).
- **Highest start replay and best avg %:** Chuck test (1.86), Haliburton alley-oop (1.83), Wemby 1-for-13 (1.80), Lakers/Bronny (1.78), Steve Kerr lookalike (1.77), Kid free throws (1.77). Each opens on a visible human moment or a named person doing the strange thing.
- **Lowest start replay and worst mid-hold:** Game 4 "who actually won" (1.46, mid 0.53), Caitlin Clark (1.42, mid 0.59, 29 s), "NBA just banned this bet" (1.54, mid 0.59, 27 s), All Three Williamses (1.39).
- **Formats above 95% avg viewed (n=20 of 43):** story moments, "most X in NBA history" lists, oddities, Bronny/LeBron news. **Below 80% (n=8):** the Oct 3-6 batch of legality/hypothetical explainers (Bad Boys defense 64.6%, Jordan foul 75%, NBA Final that doesn't count 72.6%, "Did Bronny actually get better" twice, 68% and 79%), plus Rugby (78.5%) and Caitlin Clark (77%). Not a lane finding: "Jokic's pass doesn't count" is a rule Short at 98-100% twice.

**FC, the 2-3% drop [V, n=9]:**
- Loss from 1% to 3%: goalkeeper trio **-17%** (S01 1.74 to 1.45, S05 1.81 to 1.51, S03 1.63 to 1.35) vs **-8 to -15%** for the six others.
- It is not a line-1 problem. 3% of runtime is 1.8 s (S01, 60 s), 1.8 s (S05), 2.1 s (S03). In all three the voice has said only "Goalkeepers who hid a..." and the first shot (1.9 s, 2.4 s, 2.2 s) has not yet cut. The title card is on screen with line 1 [V from `title_caption.txt`/`shots.json`]. So the loss happens on frame 1 plus the first 3-4 words.
- **It reflects wider reach, not a worse start.** The trio's start replay is highest (1.63-1.81 vs 1.31-1.59) and their YouTube relative retention at 3% is **the best on the channel** (0.84, 0.74, 0.80 vs 0.52-0.69). They shed the uninterested audience early and then hold: 10% to 50% retained 0.86/0.72/0.81 vs 0.60-0.73, and 50% to 95% about 0.83 vs 0.55-0.66.
- Conclusion: do not rewrite line 1 to fix the 2-3% drop. What the goalkeeper stories do right is the middle and the end.

## 2. Length vs retention vs views

- **NBA avg % viewed falls with length (rank correlation -0.43, n=43).** At 22 s or less: median 99.3% (n=15). 23-25 s: 94.8% (n=16). 26 s or more: 83.1% (n=12).
- **Views do not follow length (-0.13).** Median views at 22 s or less 5.6K, 23-25 s 4.5K, 26 s or more 2.9K: the gap is within the noise.
- **Subscribers lean the other way [H, n too small]:** 6.3 subs per 10K views at 26 s or more vs 3.0 at 22 s or less. Driven by two Shorts (Lakers/Bronny, 19 subs at 29 s; LeBron vs his son, 13 at 27 s).
- **FC:** the 52-59 s Shorts average 64-80% viewed; the 60 s goalkeeper Shorts 93-97%; 71 s S03 83%. Length is confounded with topic [S, Oct 30 log already says so].

## 3. Title patterns (NBA, age 3+ days)

| Pattern | n | Median views | Median avg % viewed | Verdict |
|---|---|---|---|---|
| Question | 18 | 5.6K | 93.4 | **n too small / topic-driven** (three record-list questions alone are 25.6K, 23.9K, 5.6K) |
| Statement | 25 | 3.2K | 94.7 | same |
| Has hashtag | 28 | 5.6K | 96.4 | confounded: the 15 without are mostly Oct 4-9 posts |
| 8+ words | 17 | 5.6K | 88.0 | n too small |
| 6 words or fewer | 16 | 5.0K | 93.4 | n too small |
| Title length 30 chars or fewer / 31-40 / over 40 | 11 / 20 / 12 | 4.3K / 2.9K / 6.8K | 91.7 / 94.8 / 96.9 | no trend (rank correlation with views +0.16) |
| "Who/How many ... most" | 3 | 23.9K | 95.9 | only pattern with 3 supports, see change 3 |

- **Emoji:** all 43 NBA titles carry one (😳 most often), so there is no baseline: **cannot be assessed.** The competitor review has the same gap.
- **Avg % viewed is flat across every title pattern (88-97).** Titles move who clicks in, not who stays. Do not spend time on title shape beyond the record-list pattern.

## 4. Engaged ratio under 0.5 (NBA, 11 Shorts)

Luka 1963 (.492), SGA streak (.495), Lost Most Games (.493), Steve Kerr lookalike (.495), Chuck test (.455), underhand (.473), 2007 picks (.484), Bad Boys (.465), Kawhi picks (.442), NBA Final (.497), Jordan foul (.444).
- **Honest result: no shared trait with 3+ clean support.** The whole range is narrow (0.44-0.60, median 0.546), and the Shorts under 0.5 have normal avg % viewed (median 94.6%) but fewer views (2.3K vs 5.7K) and a lower like rate (11 vs 16 per 1K).
- Two partial leads [S, confounded]: **6 of the 11 come from the Oct 3-5 script batch** (Kawhi, 2007 picks, Bad Boys, Jordan, NBA Final, underhand), written before the Oct 14 rules; and **7 of 11 open on a statistic or an institution (the NBA, the league, "Only 9,100 seats", "Ninety-two point nine") with no visible moment in the first sentence.** But Luka and SGA open on a number and still sit at .49. So treat "number-first, no scene" as the lead to test, not a finding.
- Engaged ratio is a weak predictor on its own: rank correlation with views +0.28.

## 5. FC: why does only one goalkeeper Short convert subscribers?

- **The claim is really "one Short".** Subs: **S01 sock 86**, S03 danced 11, S05 water bottle 7; the six others 0-4 each. S01 is 74% of the channel's 117. Per 10K views: S01 30.5, S03 7.1, S05 2.5; non-goalkeepers range 0 to 29.5 (Coutinho 3 subs on 1.0K views).
- **Retention does not explain it.** S01 and S05 have nearly identical curves (relative retention at 3%: 0.84/0.80; at 10%: 0.80/0.74; avg viewed 96.8% and 92.9%; engaged ratio .553 and .557) yet 86 vs 7 subs.
- **Like rate separates them [V]:** S01 26.5 likes per 1K views; S05 **5.6** (lowest on the channel); S03 9.9; the others 12-21.
- **Candidate causes [all H, none controllable from this data]:**
  1. **Ending.** S01 ends on a hard, shareable number ("bought for one million euros... a page from a hotel notepad"). S05 was cut to 60 s and ends on "the note reportedly just said, feel on the day". S03 ends on "played just twelve games".
  2. **Repeat topic.** S05 reuses S01's hook ("cheat sheet") four days later; viewers who liked S01 may already be subscribed.
  3. **First Short on a new channel.** S01 launched the channel (Oct 21, 9:27 pm), so it may have collected every early subscriber. Cannot separate this from 1 and 2 without "viewed vs subscribed" by traffic source.
- **What is safe to say:** the goalkeeper-shootout stories earn views (3 of 3 over 15K; 0 of 6 others over 3K) but conversion is **not** a goalkeeper trait, it is an S01 trait.

---

## Top 5 changes, ranked by expected impact

1. **Judge and design the first second by start replay, not by the 2-3% drop.** Evidence: start replay vs views +0.62, vs avg % +0.78 (n=19); best Shorts open on a visible moment or a named person doing the strange thing; FC's 2-3% drop is wider reach, not a flaw. Action: add the 1% watch ratio to the daily check (aim 1.7+ on NBA); keep the shot-1 rules (2 s or more, shows line 1 happening). [S]
2. **Fix the middle, cap NBA at 24 s.** Evidence: hold from 10% to 50% is the best curve predictor of avg % (+0.74); the worst middles (0.53-0.59) are 22-29 s rule/news Shorts that explain before showing; avg % falls with length (-0.43, n=43). Action: a new visual fact or turn by 8-10 s, then cut any sentence that does not add one. Trade-off: subs per view are higher at 26 s or more, so test it (see below). [S]
3. **Make "Who has the most/least X in NBA history" the default NBA lane.** Evidence: #42 25.6K, #48 23.9K, #52 5.6K (n=3, median 23.9K vs 4.3K channel median); they top the view ranking. Confounder: LeBron and Harden are huge names, #52 is the weakest, and the supply of fresh records is finite. [S]
4. **Put a hard, concrete number as the last line and protect it when trimming to 60 s.** Evidence: S01 vs S05 (86 vs 7 subs, 26.5 vs 5.6 likes per 1K, same retention). One pair only, so [H]; but trimming S05 to fit moved its end from a hard fact to a vague note, and the log already says hits end on a twist (64% vs 52%).
5. **On FC, build the next batch on "a trick the viewer can see in a famous shootout" and test the rest sparingly.** Evidence: 3 of 3 trick-in-shootout Shorts 15.5K-28K; 0 of 6 non-trick stories above 3.0K, despite bigger names (Zidane, Maradona, Coutinho), and their middles are weaker (10% to 50% retained 0.60-0.73 vs 0.72-0.86). Open test: S17 Krul (judge Nov 2). [S]

## Stop doing

- **Reading 24 h counts** (FC breakouts come on day 2-3, and one identical re-upload gave 4x).
- **Opening on a bare statistic or institution with no scene** (the Oct 3-5 batch pattern) until the test below says it is fine. [H]
- **NBA cuts of 26 s or more without a moving clip carrying the middle.** [S]
- **Rewriting line 1 to "fix" the FC 2-3% drop.**
- **Second Shorts reusing a hit's hook within a week** (S05 after S01), until the repeat-topic question is answered. [H]
- **Re-uploading the same Short** to chase views (one pair, but it burns a slot).
- **Claiming anything about emoji or title shape**: no variation, no baseline.

## What to test next (one A/B each, 72 h reads)

- **NBA length and middle:** the two queued record-list Shorts (#51 most turnovers ever, #55 most turnovers in a season). Cut one to 20-22 s, the other to 27-29 s with a mid-point extra fact. Same posting hour, different days. Read avg % viewed, views, subs per 10K.
- **NBA opener:** pair one number-first opener against one scene-first opener (a visible moment in the first sentence) on the same lane, e.g. #54 vs #55. Read start replay and engaged ratio.
- **FC:** S17 Krul (a save, no trick) vs S21 Higuita (a visible trick), the already-planned pair. Added read: likes per 1K and subs per 10K, not only views.
- **Title (one test, matched pair):** question vs statement on two record-list Shorts, same hour. Read views and avg % viewed together.

## What data we still lack

- **Stayed to watch / swiped** per Short (last export Oct 24, Studio only): the strongest known predictor (Spearman +0.77) and a better gate than avg %.
- **Retention curves for 24 of 43 NBA Shorts** (the API returned empty for Oct 4-17 posts) and for FC S16-S18.
- **Viewed vs subscribed and traffic source** (Shorts feed vs browse vs search) per Short, to settle the S01 question.
- **Frame-1 content per Short** in a table (face, scene, number, text), so first-frame effects can be counted rather than recalled.
- **Which version was posted (music or no music; real audio or narrated)** for S01-S07 and #70-#75.
- **Post hour** for #40a-#42, #70, #71, S08, S15.
- **A baseline for emoji and hashtags** (titles without them); all current NBA titles have one.
- **72 h snapshots** at a fixed time for every Short, so age is not a confounder.
- **Impressions and click-through** (not applicable to the Shorts feed, but needed if Shorts surface in Browse/Suggested).
