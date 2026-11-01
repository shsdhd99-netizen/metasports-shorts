# Why the NBA Shorts' views dropped (Oct 26, 2026)

**Owner's question (Oct 26):** "can you see why nba short views are down? i think its editing and bad retention rules in general"

**Short answer: mostly yes.** It isn't the whole niche, and it isn't the channel being dead. Our good Shorts still reach old-era numbers (20-32K). Most new Shorts don't, and they fail at the same place: fewer than 74% of viewers stay past the first seconds. Two of our own editing rules line up with that failure:
- **"3+ cuts in the first 3 s, a new picture every second":** the fast openings hold worse.
- **Evidence cards:** stat and screenshot cards hold worse, most of all in the first 4 s.

Topic choice (Oct 23 diagnosis) still matters too.

**Tiers:** [V] measured · [S] a pattern in a small sample · [H] a guess. All new-era numbers below are from our own Studio export (Oct 17-24) and the posted Shorts' edit files.

## 1. How big is the drop, and is it the whole niche?
| | Old era (Nov 2025-Feb 2026, 80 Shorts) | New era (Oct 3-23 2026, 40 Shorts) |
|---|---|---|
| Median views | **29,000** (public, Oct 14) | **3,900** (Studio window) |
| Average % viewed | 107% | 92% |
| Length | 22.5 s | 24 s |
| Music bed | 5 of 5 we watched | none |

**Not the niche [V, approximate]:** Ahmed's Basketball, a big narrated NBA channel, drew a median of 214K, 142K and 252K a Short in Dec-Feb, and 130K in September 2026 (monthly dates interpolated). That is down about 40%, not 90%.

**Not the channel [V]:** the same channel's new-era hits got old-era numbers:
- #22 "Two Men Can Still Wear Six": 31.8K
- #03 "Nobody Voted Against Wemby": 27K
- #58 "The Lakers Just Saved Bronny": 23K
- #48 "Most Missed Threes": 22K
- #19 "How Tall Is Cooper Flagg": 21K

Our brand-new soccer channel also reached 30K (S01) in October. So 20-30K Shorts are still possible in this feed.

**Where they fail [V]:** "stayed to watch" decides reach:
- stayed vs views: Spearman 0.70 (n=37).
- Shorts that held 74%+ got a median of 8.6K views; those under got 2.9K.
- **Only 13 of 40 new-era Shorts reached 74%.** The median was 69%.
- **All 6 Shorts at 10K+ held 74% or more.**

## 2. What separates the 74%+ Shorts from the rest
These are our 37 posted new-era Shorts whose edit files are in the repo (#45, #46 and #10 aren't). Medians:

| Edit choice | With it | Without it | Tier |
|---|---|---|---|
| **2 or fewer shots in the first 3 s** | **75.0% stayed, 7.8K views** (n=7; exactly 2: 77.6%, 14.9K, n=6) | 3+ shots: 67.5%, 3.1K (n=30) | [V] n=37 |
| **No card anywhere** (stat card, screenshot, article) | **72.6%, 6.1K** (n=17) | any card: 66.1%, 3.4K (n=20) | [V] |
| **No card in the first 4 s** | 72.0%, 5.0K (n=28) | card in the first 4 s: 63.2%, 1.9K (n=9) | [V] |
| **15 shots or fewer** | 75.0%, 6.1K (n=13) | 16+: 66.4%, 3.1K (n=24) | [V] |
| Average shot 1.8 s or longer | 75.0%, 4.2K (n=11) | under 1.8 s: 66.4%, 3.7K (n=26) | [V] |
| Line 1 finished by 3.0 s | 71.1% (n=23) | later: 62.2% (n=14) | [V] |

**Rank correlations (n=37):**
- card share vs views: **-0.40**
- number of shots vs stayed: **-0.44**
- average shot length vs stayed: +0.39

Within the Oct 3-13 builds alone (n=23, same tools and same period), card share vs stayed is **-0.51** and vs views -0.55.

**No link [V]:**
- speaking pace: 0.10
- word count: -0.08
- how many numbers are spoken: 0.15
- length vs stayed: -0.09
- frame 1 a face vs an action shot: 70.6% vs 68.4%

**The old hits looked like our winners, not like our rules** (vidIQ scene reports, Oct 14):
- 7-15 shots at 1.4-2.3 s each
- the real moment on screen, with **red circles on the broadcast's own scorebug and score** as the proof
- no stat cards
- a whoosh or pop at 0 s
- a quiet music bed throughout

**#42 and #48** (84% and 83% stayed) were built the same calm way: 12 shots of about 2 s, one play held through the first 5 s, zero cards, numbers written over the footage.

**Caveats:**
- **Edit choices travel with topics.** Rule and contract stories needed cards and did worse for both reasons; the later builds also had better topics.
- **This is correlation in one channel.** It is strong, consistent and backed by the old hits and by #42, but not an experiment.
- **Music:** every new-era NBA Short had none, so its effect can't be measured here.

## 3. The rules that pushed us the wrong way
| Rule | Where | Verdict |
|---|---|---|
| ">= 3 cuts in the first 3 s", "a new image about every second until 5 s" | `cloud-short` SKILL (first 3 seconds), QA soft check | **Wrong for NBA.** Openings with 2 shots held 77.6% vs 67.5%. Hold the opening moment. |
| "average shot 1.4-1.9 s", "no shot over 3 s" (QA fails a shot over 3.6 s) | SKILL quality formula, QA PACE | **Wrong.** Fewer, longer shots held better. A play needs to run (the old free-throw hit held its payoff 3.5 s). |
| "Evidence cards for any fact line" (`card.py` screenshots) | SKILL section 5 | **Harmful.** Proof goes on the footage (words over the play, or a circle on the scorebug), not on a card. |
| ">= 6 distinct source clips", "<= 35% from one clip" | QA hard gates | **Pushes illustrative filler.** It made us cut away from the one moment the story is about. Demote to a warning. |
| "No sound in the first second" | SKILL, assemble.py | **Untested.** The old hits opened with a whoosh/pop. Leave it as is; it isn't what separates our winners. |
| No music bed (owner, Oct 14) | Music Guide | **Unknown.** All 5 old hits we watched had one, and so do Ahmed's channels. It's the one big difference we can't measure, so it's worth a clean test (section 5). |

## 4. What changes now (applied Oct 26)
- **QA (`Tools/qa_short.py`, NBA profile, not the soccer story format):**
  - **More than 2 shots in the first 3 s is now a warning.** It used to be "fewer than 3".
  - **A card in the first 4 s is now a FAIL.**
  - **A card share over 10% is a warning.**
  - **Shot length:** a shot is "too long" only over 6 s (quotes 6 s). The average-shot guideline is now 1.8-3.0 s.
  - **The 6-clip / 35%-per-clip gates are warnings.**
- **`cloud-short` SKILL:** the first-3-seconds and pace rules are rewritten to match: hold the moment, about 2 s shots, no cards, proof on the footage.
- **#69 (Luka, today's 11 AM slot):** re-cut to the new rules as v2: 2 shots in the first 3 s, 12 shots, no card. v1 stays in the Hub for comparison.

## 5. Tests that need the owner
1. **Music bed, NBA:** the next 6 NBA Shorts alternate a quiet bed (-20 LU, royalty-free, so it doesn't cut pay) against none, both calm-cut. Decide on stayed %. Owner: yes or no?
2. **Topics:** keep to the Oct 23 rules: household star, one visible paradox, no paperwork rules, news under 36 h old.
