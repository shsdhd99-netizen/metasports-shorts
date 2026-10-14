# Posted Video Audit (Oct 14, 2026): why some Shorts worked and others didn't

**What this file is:** the canonical review of every posted MetaSports Short, with dated metrics and their limits.
- It feeds the Rules Audit (`Research Notes/Rules Audit (Oct 14, 2026).md`) and the Playbook's Creative System.
- It extends, and does not replace, the history analysis in `Winning Formula v2 (Oct 13, 2026).md`.

**Evidence tiers:**
- **[V]** verified today from data or files
- **[R]** reported (the owner's Studio screenshots, older notes)
- **[I]** inference
- **[H]** hypothesis, not proven

I can't hear audio. Every judgment about the voice here comes from scripts, transcripts and measurements.

**Data file (one row per Short, all 102):** `Research Notes/Posted Shorts - metrics (Oct 14, 2026).csv`
- id, URL, title, era, publish time, length
- public views (Oct 14)
- analytics views and engaged views
- average % viewed, average view duration
- likes, comments, shares, subs gained
- for our builds: the first sentence, words, pace, shots, frame 1 and the first card time

## 1. Sources, dates and what is missing
| Data | Source | Date / window |
|---|---|---|
| Public views, all 102 Shorts | yt-dlp channel list (free) | Oct 14, 10:45 UTC [V] |
| Exact publish times, exact counts for 27 Shorts | vidIQ `get_videos_by_ids` | Oct 14 [V] |
| Per-video analytics: views, engaged views, avg % viewed, AVD, likes, comments, shares, subs gained | vidIQ → YouTube Analytics (owned channel) | Nov 1 2025-Oct 13 2026 [V] |
| Retention curves (watch ratio + YouTube's relative retention, per 1% of the video) | vidIQ `audience_retention` | same window [V]. Fetched: #22, #03, #19, #23, #12, Curry, Giannis, Chris Paul, LeBron 23rd season, old Flagg. #29 returned no data (too few views) |
| Channel views per day | vidIQ | Sep 25-Oct 11 (Oct 12-13 not yet in the API) [V] |
| Traffic sources | vidIQ | Oct 1-13 [V] |
| Transcripts, old era | yt-dlp (saved Oct 13: Curry, Giannis, old underhand) and vidIQ (today: Chris Paul, LeBron, old Flagg) [V] | |
| First frames, old era | YouTube `frame0` images [V] | |
| Scripts, word timings, shot lists, exports, new era | our production folders [V] | |
| Stayed-to-watch % | the owner's Studio screenshots: #03 Wemby 79.5%, #12 Duren 63.0% [R] | Oct 5 |

**Missing, and why** (none of this was invented):
- **Studio-only metrics:** impressions, feed CTR, and per-video "viewed vs swiped away" / "stayed to watch". The YouTube Analytics API (via vidIQ) does not return them for Shorts. They exist only in Studio screenshots, and we have them for 2 Shorts.
- **Old-era production details:** voice, settings, editor, music. Those Shorts were made on the PC (Nov 2025-Feb 2026), and their files are not in the cloud copy. The two eras may have used different voices; that is unknown.
- **Analytics lag:** analytics trail public counts by 1-2 days. Example: #23 shows 2,651 in analytics vs 9,429 public. So views come from public counts, and ratios come from analytics for posts 3+ days old.
- **Engaged views as a swipe measure:** I tested engaged/views as a stand-in for "swiped away" and **rejected it**. In the old era it runs *against* views (Spearman −0.38), because replays add views without adding engaged views. It is not a swipe measure.
- **vidIQ credits used today:** 75 (145 → 70; renews Nov 5).

## 2. The big picture: the era effect is the largest thing in the data
- **Old era** (Nov 2025-Feb 2026, 80 Shorts incl. 8 off-niche memes): median **29.8K** views, middle half 24-34K. [V]
- **New era** (Oct 3-14, 2026, 22 posts incl. 1 re-post): median **2.8K**. Only 3 reached the old band, and all three were posted Oct 3-6: #22 31.8K, #03 27.0K, #19 20.6K. [V]
- **Channel views per day:** [V]

  | Day | Views |
  |---|---|
  | Oct 3 | 24.2K |
  | Oct 4 | **37.2K** (peak) |
  | Oct 5 | 8.2K |
  | Oct 6 | 19.9K (#19 day) |
  | Oct 7 | 6.9K |
  | Oct 8 | 8.1K |
  | Oct 9 | 10.3K |
  | Oct 10 | 4.5K |
  | Oct 11 | 4.75K |

- **94.5% of views come from the Shorts feed** (117K of about 124K, Oct 1-13). Search is 3.9%, channel pages 0.3%, subscribers' feed 0.3%. **The feed's first-second test decides almost everything; titles and tags barely matter for reach.** [V]
- **Posting rate:** 16 posts in Oct 3-9 (2-3 a day), then 1-2 a day. [V]
- **Causes these data can't separate:** [I]
  1. Channel state after a 215-day gap. The feed may test a returning channel generously, then cut back.
  2. Posting 2-3 a day.
  3. A production change between eras (voice and editor unknown, see section 1).
  4. Topic and execution.

  The winners' Oct 3-6 dates fit cause 1 or 2. But Oct 3-6 also produced losers (#12 2.9K, #18 2.8K, the Cup post 2.3K, #25 1.9K), so the date alone doesn't explain it.
- **Plateau:** views stop growing after about 2 days (e.g. #22 29K→31.8K from Oct 5 to Oct 13). #23 was still growing at day 2.5 (6.5K→9.4K). [V]

## 3. What moves with views (Spearman rank correlation; correlation is not cause)
| Measure | New era (n=17, posts 1.6+ days old) | Old era (n=80) | Reading |
|---|---|---|---|
| Average % viewed | **+0.52** | **+0.45** | Retention moves with reach in both eras [V]. Old era: Shorts at 40K+ median 109.9% viewed, 20-40K 107.5%, under 20K 98.7% |
| Average view duration | +0.46 | +0.17 | |
| Narration pace (wpm) | **+0.50** (n=16) | n/a | Faster reads go with more views. #22 ran at 292 wpm. [V corr; H cause] |
| Like rate | +0.02 | −0.16 | Likes don't predict reach. The new era has 2× the like rate (median 1.77% vs 0.88%) at a tenth of the views [V] |
| Subs per 1K views | +0.11 | −0.07 | No relation [V] |
| Length | n/a | −0.13 | No length effect within 18-33 s [V] |
| Card before 4 s | median 1.9K with an early card (n=5: #15, #34, #25, #13, #29) vs 3.9K without (n=13) | n/a | Weak support, and confounded: stat-heavy topics use cards [V counts; H cause] |

## 4. Retention curves (10 Shorts)
**How to read the columns:**
- **Start:** the watch ratio in the first 1%. Above 1 means replays and loops.
- **Relative 10%:** YouTube's comparison with similar-length videos, at 10% of the runtime.
- **Lowest relative:** the lowest point, and where it falls.

| Short | Views | Start | Relative 10% | Lowest relative (where) | End ratio | Notes |
|---|---|---|---|---|---|---|
| #22 Six (Oct 4) | 31.8K | **1.83** | **0.82** | 0.77 (start) | 0.83 | climbs all the way; no cliff |
| #03 Wemby vote (Oct 3) | 27.0K | 1.74 | 0.70 | 0.69 (19%) | 0.77 | |
| #19 Flagg (Oct 6) | 20.6K | 1.74 | 0.72 | 0.71 (22%) | 0.78 | |
| #23 Father vs son (Oct 11) | 9.4K | 1.63 | 0.69 | 0.65 (25%) | 0.67 | |
| #12 Duren (Oct 3) | 2.9K | **1.44** | **0.46** | **0.41 (23%)** | 0.47 | **cliff at 13-17% (4.3-5.6 s)**: ratio 1.17→0.99. A contract explanation follows the hook |
| Curry Kobes (Nov 16 2025) | 30.8K | 1.83 | 0.83 | 0.77 (start) | 0.94 | |
| Giannis game ball (Nov 17) | 28.3K | 1.79 | 0.70 | 0.70 | 0.68 | |
| Chris Paul ending (Nov 23) | 28.4K | 1.75 | 0.68 | 0.65 (21%) | 0.69 | |
| LeBron 23rd season (Nov 20) | **5.3K** | 1.76 | 0.62 | 0.62 (16%) | 0.81 | **good retention, low reach** |
| Old Flagg "scaring defenders" (Nov 22) | 4.9K | **1.56** | 0.66 | 0.61 (31%) | **0.42** | the end falls 0.59→0.43 on "make sure you subscribe" |

**Readings:**
- **[V] (n=10):** every Short at 20K+ starts at 1.74 or higher, with relative 10% of 0.68 or higher. Both curves that start below 1.6 (#12, old Flagg) got under 5K.
- **[I]:** so a weak first few seconds goes with low reach. But a strong one does not guarantee reach: LeBron 23rd held viewers as well as the winners and still got 5.3K. **Retention is necessary, not sufficient.** The rest is the feed's first test, which the API can't show.
- **[V] CTA endings:** the subscribe line costs end-of-video watchers: old Flagg −27% in its last 4%, Curry −12% at its CTA. Chris Paul has no CTA and also dips (−14%, end of narration). So the CTA effect is unclear (TEST). No evidence says the CTA helps.

## 5. Side by side: strongest vs weakest

### A. Our builds (new era, Oct 3-14; production was the same, so differences are topic and execution)
| | #22 Six | #03 Wemby vote | #19 Flagg | #20 Bad Boys | #13 Kawhi | #29 Underhand | #12 Duren |
|---|---|---|---|---|---|---|---|
| Views (age) | 31.8K (9.7 d) | 27.0K (10.7 d) | 20.6K (7.9 d) | 1.6K (3.8 d) | 1.9K (6.0 d) | 1.5K (1.6 d) | 2.9K (10.5 d) |
| Avg % viewed | 115.6 | 104.0 | 102.8 | 65.2 | 91.9 | n/a | 71.1 |
| First line | "Only two NBA players are still allowed to wear number six." | "Every Defensive Player of the Year in NBA history had at least one voter who picked somebody else." | "An Instagram account said Cooper Flagg grew two inches this summer." | "Ninety-two point nine." | "The NBA took five first-round picks from the Clippers, fined them $30 million, and..." | "Knicks center Mitchell Robinson made twenty-nine percent of his playoff free throws." | "Jalen Duren just walked away from eighty-seven million dollars, and a reported weight clause..." |
| Clear by | 2.1 s | 4.1 s | 2.7 s | after 1.0 s the number still means nothing | 6.1 s | 3.2 s, but about a role player | 4.4 s |
| Frame 1 | a #6 jersey | Wemby blocking | Flagg full body, a person beside him for scale, the "6-8 to 6-11?" pill | a scuffle | a Kawhi dunk | Robinson standing; a dark "29%" card at 1.4 s | a Duren dunk |
| Shape | one measure (who may wear 6), ends on the answer | one record and one number, ends on legacy | one measure (his height, 5 conflicting numbers), ends in his own voice: "I'm 6-10" | a number puzzle; 4 cards in the back half | 4 cards from 2.0 s; a transaction log | 6 numbers on 5 measures | contract terms; ends "Smart, or a mistake?" |
| Ending | answers | answers | answers (his own voice) | answers | answers | doesn't answer ("Thanks, but no thanks") | **question** |

**What separates them [I], each reading backed by a curve or count above:**
- **Winners:**
  - name a **visible object** with a **paradox** in about 2-3 s
  - **stay on one measure**
  - **end on an answer**
- **Losers do at least one of these:**
  - open on a number or name with no stakes (#20, #29)
  - start with dense context (#13 needs 6 s; #12 has a contract cliff at 4-6 s)
  - show a card early (#13, #29)
  - end on a question (#12, #18: both about 2.8K)
- **Topic still matters:**
  - #14 (rule nuance) had the **highest** retention of the batch (115.3%) and got 1.6K.
  - #23 had a so-so retention curve and a top like rate (2.9-3.4%) and reached 9.4K.

### B. Same production, same week (Nov 15-23, 2025): the old-era control for topic
| | Curry Kobes | Giannis game ball | Chris Paul ending | LeBron 23rd season | Old Flagg |
|---|---|---|---|---|---|
| Views | 30.8K | 28.3K | 28.4K | **5.3K** | **4.9K** |
| Avg % viewed / like rate | 123.0% / 1.12% | 107.4% / 2.38% | 98.4% / 1.48% | **116.8%** / 0.76% | 100.2% / 1.59% |
| First line | "Stephen Curry just pulled one of the wildest sneaker moves the NBA has ever seen." | "Giannis just saved a rookie's first NBA memory." | "Chris Paul is proof that even legends don't get the ending they deserve." | "LeBron James is about to break NBA history. Tonight, he... becomes the first player ever to play 23 seasons." | "Cooper Flagg might be the biggest problem the NBA didn't prepare for." |
| Frame 1 | Curry in a hoodie, pregame | the referee holding the ball | Paul (#3) walking away | LeBron's back, "23 JAMES" | a wide game shot; Flagg is tiny |
| Story | a visible moment, a hidden reason (Under Armour executives watching) | a visible moment, a kind reason | an emotional arc (every run ended in injury) | the most-covered fact of that night, delivered as news | generic hype; no specific fact |
| Ending | "...subscribe" CTA | a moment line | "every kid will still want to be Chris [Paul]" | "...make sure you subscribe" | "...make sure you subscribe" |

**Reading:**
- **[I] Topic and specificity, not retention, separate this week's hits from its misses.** LeBron's curve matched the winners'. His fact was the night's most-covered headline: it carried no surprise, and anyone could post it.
- **[I]** The old Flagg Short had no fact at all. Its retention was the weakest of the five, with a start ratio of 1.56.
- **[V]** The three hits each pair a visible moment with a reason or feeling the viewer doesn't already have.

## 6. The ten questions, for the Shorts that teach the most
Format per Short: **1-3 s** what the viewer gets · **Hook** · **Frame 1** · **Context** · **Escalation** · **Payoff** · **Ending** · **Craft** · **Evidence** · **Action**.

- **#22 Six (31.8K, 115.6%):**
  - 1-3 s: "only two can wear 6", a rule paradox. The hook is specific, surprising and checkable.
  - Frame 1: a #6 jersey, which matches the hook.
  - Context: fast (Russell retired 6; the two are grandfathered).
  - Escalation: who are the two?
  - Payoff: the answer.
  - Ending: answers.
  - Craft: 292 wpm, no cards.
  - Evidence: best curve on the channel (starts 1.83, no cliff) [V].
  - Action: **repeat** the shape: a visible object, a rule paradox, one measure.
- **#03 Wemby vote (27.0K):**
  - 1-3 s: "every DPOY had a voter who picked someone else". The paradox is clear by 4.1 s, a slower hook than #22's.
  - Frame 1: Wemby blocking (the subject).
  - Payoff: the unanimous vote.
  - Ending: Jordan, the Admiral and a 22-year-old (a legacy close).
  - Evidence: 79.5% stayed [R]; curve starts 1.74 [V].
  - Action: **repeat** record paradoxes on stars. **Test** hooks under 3 s.
- **#19 Flagg height (20.6K):**
  - Frame 1: Flagg full length, with a person for scale and the "6-8 to 6-11?" pill.
  - Escalation: five conflicting numbers.
  - Payoff: his own voice, "I'm 6-10".
  - Evidence: curve starts 1.74 [V]. The pill is the only on-screen premise line ever posted (n=1).
  - Action: **repeat** "a number you can see" plus the subject's own voice at the end. **Test** a premise pill on frame 1 (the owner's no-headline rule; see Rules Audit).
- **#23 Father vs son (9.4K, best like rate):**
  - 1-3 s: "a father and son had never played in the same NBA game, until..."
  - Frame 1: LeBron beside "JAMES JR. 9".
  - Payoff: LeBron vs LeBron Jr.
  - Ending: loops to the opening image.
  - Evidence: still growing at 2.5 days; curve starts 1.63 (middling).
  - Action: **repeat** family and emotional stakes on the channel's top names. The emotion drives likes; the curve says the middle sagged.
- **#17 Flopping (6.7K):** went up with a title we didn't write, which misstates the fact ("Did The NBA Just BAN Flopping?").
  - Hook: the true fact (a technical since 2023-24).
  - Avg % viewed 81.3: viewers who expected a "ban" left.
  - Action: **stop** changing titles away from the script's fact. **[I]** A title that over-promises costs retention.
- **#20 Bad Boys (1.6K, 65.2%, the lowest):**
  - 1-3 s: "Ninety-two point nine." A number with no subject, so nothing to understand at second 1.
  - Context: long.
  - Cards: 4 in the last 10 s.
  - Action: **stop** naked-number openings.
- **#13 Kawhi (1.9K):**
  - The hook is a 6-second compound sentence, with a card at 2.0 s.
  - Action: **stop** compound hooks. One fact first.
- **#29 Underhand (1.5K):** the old-era Short on the same topic did 73K.
  - The new one opens on a niche player's stat, puts a card at 1.4 s and spans 6 numbers.
  - Action: **stop** re-telling an old winner's topic through a lesser angle. If re-telling, keep the winner's opening shape.
- **#12 Duren (2.9K, 71.1%):**
  - Contract terms cliff at 4-6 s [V curve]; 63.0% stayed [R].
  - Ends on a question.
  - Action: **stop** contract explainers and question endings.
- **#14 Four stars (1.6K, 115.3%):**
  - Excellent retention, low reach: the topic was too niche for the feed.
  - Action: **test** whether high-retention niche rule Shorts grow with better titles or frame 1. The more likely fix is a bigger name.
- **#11 Jordan push-off (38 views):** reach collapsed in hour 1. The cause is unknown: a Studio restriction is possible, since the free check flags it.
  - Action: the owner checks Studio > Content for a claim (open since Oct 5).
- **#25 Bronny re-post (193 at 0.9 days):** an identical re-upload gets nothing.
  - Action: **stop** re-posting identical files.
- **#39 Oldest triple-double (2.2K at 11 h):** posted Oct 13, 23:49 UTC.
  - Read at 48 h. Age-matched: #03 had 20.6K at 10 h; #29 had 1.0K at 21 h.

## 7. The named historical examples (verified)
- **Curry: Under Armour → Nike Kobes.** "Fans Noticed Something Strange on Curry…" (`daIsE50TcoQ`, Nov 16 2025).
  - Numbers: 30.8K, 123.0% viewed, AVD 34 s on 28 s, 345 likes.
  - Normal old-era reach, not a breakout. Best retention start of the old set (1.83). [V]
  - Why it worked [I]: a visible, surprising object (Kobes on Curry's feet) and a hidden twist (Under Armour executives in the arena).
- **Giannis giving a game ball to a rookie.** "Why Giannis Took The Ball From The Refs" (`pr-JQuzAUxY`, Nov 17 2025).
  - Numbers: 28.3K, 107.4%, **2.38% like rate** (2nd of 71 old-era Shorts).
  - Kindness drives likes, not extra reach. [V]
- **Wembanyama:**
  - Old era: "Is It Possible To Dunk Without Jumping?" 55.8K; "Wemby makes everything look small" 31.7K; "The NBA Has Never Seen This Before" 25.9K; "Wemby Just Broke Basketball" 21.5K; "Why Everyone Is Scared of Wemby" 18.2K; "Rudy Gobert Crossed the Line" 14.8K.
  - New era: #03 27.0K, #35 rugby 2.9K.
  - **[I]:** Wemby works when there's a visible feat or a record paradox. The rugby Short (an off-court curiosity, a 3.8 s hook) did not.
- **LeBron's 23rd season and Cooper Flagg:**
  - "LeBron Just Broke NBA History Tonight" (Nov 20 2025): 5.3K. Retention was excellent, so the low reach was topic saturation plus a "tonight" news frame [I].
  - The old Flagg Short (Nov 22 2025): 4.9K, generic hype.
  - The new Flagg #19: 20.6K, built on a specific visible number.
  - **The same player, Flagg, went 4.9K → 20.6K when the Short moved from hype to a checkable, visible fact** (n=1 pair, different eras) [V counts; I cause].
- **Chris Paul's retirement.** "Chris Paul Didn't Deserve This Ending 😢" (`7CniAq-eKaU`, Nov 23 2025).
  - Numbers: 28.4K, 98.4%, an emotional arc, no CTA.
  - The emotional "legend's ending" frame worked at normal reach [V].

## 8. Topic appeal vs execution
- **Topic** sets the ceiling. Within one week and one production style, generic or over-covered topics got about 5K and specific visible stories got about 30K (section 5B) [V counts, I cause].
- **Execution** decides whether the topic reaches that ceiling:
  - #29 vs the old underhand Short: same topic, 1.5K vs 73K.
  - Flagg: 4.9K vs 20.6K.
  - The new-era winners share the shape, a visible object + a paradox + one measure + an answering ending [I, n=3].
- **Distribution state** (section 2) caps everything after Oct 6. That is the biggest unknown. Two posts a day against one a day is the cheapest test of it (Rules Audit, Test 1).
- **What we cannot attribute to the voice:** every new-era post used the same clone voice, winners and losers alike, so voice explains none of the new-era spread [V]. The old era's voice is unknown [V].

## 9. Repeat / change / test / stop (carried into the Rules Audit)
- **Repeat:**
  - a visible object + a paradox in the first 2-3 s
  - one measure
  - an answering ending, ideally in the subject's own voice
  - big names with a specific, checkable twist
  - ~~fast narration (about 250-290 wpm)~~ **Revised Oct 14 (section 10):** our own old hits measured 182-212 wpm and the new posts already run 224-250. Keep 200-265: don't drag, don't rush.
- **Change:**
  - **Titles:** go up exactly as written; no over-promising (the #17 lesson).
  - **Hooks:** one fact per sentence; no compound hooks.
- **Test:**
  - posting rate (1 vs 2 a day)
  - a premise pill on frame 1 (#19)
  - the red ring (#40 vs #41)
  - CTA vs no CTA
  - a cold open with no narration in the first 0.5 s, for visual moments
- **Stop:**
  - naked-number or niche-player openings
  - cards before 4 s
  - contract explainers
  - question endings
  - identical re-posts
  - re-telling old winners through lesser angles
  - "tonight/news" framing of the night's most-covered fact


## 10. Old videos as creative references: what they did, what we do now (added Oct 14, 2026, owner request)
**Sources:**
- Five old Shorts watched scene by scene by vidIQ (4 hits + 1 weak control). Reports: `Posted Video Audit - old-video watch reports (Oct 14, 2026).md`.
- Narration pace measured from timed YouTube transcripts of 3 old Shorts.
- Our 20 new-era builds, from our own files (`Posted Shorts - metrics (Oct 14, 2026).csv`).

**Limits:**
- I watched none of the old videos myself (YouTube blocks the cloud). vidIQ's descriptions are AI-written.
- n = 4 hits and 1 control: patterns here are **[S] small-n or [H]**, never proof.
- The two eras also differ in distribution (section 2). Nothing below claims a technique caused views.

| Dimension | Old hits (4) | Old control (1, 4.9K) | New builds (20) | Reading |
|---|---|---|---|---|
| **Music** | a quiet bed in 4/4 (trap/hip-hop; cinematic for Kobe), about -18 to -20 dB under the voice; swells or cut-outs at the payoff | yes (trap) | **none** (no-music rule, Oct 5) | Music was the old **house standard**, present in hits and the miss alike [S, 5/5]. It is not what separated winners. Bring it back as the default (owner request), quiet, with payoff moves. Effect on views: unknown, tracked as a cohort in the Outcome Log |
| **Proof on screen** | the broadcast's own scorebug and banners **kept** and circled (Luka: clock 1.5 and score 126-125; Kobe: 96-86, "60 POINTS") | Google age panel at 22 s | scorebugs **cropped** (after #39's wrong-opponent bug); proof on our own cards | When the footage IS the exact game, the scorebug is evidence: keep it and circle it. Crop it only when the shot is a stand-in [S, 2/4 hits] |
| **Red circles** | 2/4 (FT tricks: 3 circles; Luka: 3) on the exact detail **at the moment it's named** | none | only #40's frame-1 ring (test pending) | Use circles on the detail being named, anywhere in the video, not only frame 1 [H]. Pointer test continues |
| **Exact-moment B-roll** | Luka 8/11 shots, Kobe 11/13, Bronny mostly name-matched; only 2-3 generic cutaways | a montage of generic highlights | mixed: stand-ins under specific lines (#39), archive press conferences | The hits **showed the thing being said**. Exact-moment footage first; generic only for a "what if" line [S] |
| **First frame** | the subject doing the thing (Luka shooting the FT; a Wemby dunk over Bronny; Kobe's face; a circled shoe) + the hook line at once | Flagg driving (generic) | mostly the subject; some cards/archive | Same rule as Creative System v3 checklist #1; confirmed [S] |
| **Hook form** | **3/4 a question** (but only 1 of the 12 voiced old scripts in §11 opened with one: 4/16 overall) ("Why would Luka miss a free throw on purpose?"), 1 a statement with a turn ("wasn't supposed to end like this") | a vague hype claim | **0/20 questions**: all statements/paradoxes | Not proof that questions win: our two best new Shorts (#22 31.8K, #03 27K) were statements. **TEST** a concrete question hook vs a statement on comparable topics [H] |
| **Escalation** | 3 examples, the craziest last ("it gets crazier"); Kobe counts up 51, 53, 56, 60 | none (montage) | a single fact, then the explanation | Build to the payoff with a count-up or escalating examples where the story has them [S] |
| **Ending** | a punch line or answer: "That's next level awareness", "LeBron's... son." (0.4 s pause, black card, music cut), "for the last time" | **subscribe call-to-action** | an answering ending (v3) | Keep answering endings. **New device:** a beat of silence or music cut before the last word [H] |
| **Pace (measured)** | 182-212 wpm (3 old Shorts, timed transcripts). **Corrected in §11:** 12 more voiced old scripts ran 206-252 wpm, median 220 | n/a | 210-292 wpm, median 243 | Slightly faster than the old median. Guideline 200-265 |
| **Shot length** | 1.4-2.3 s average; the payoff shot held longest (3.5 s in the FT Short) | 1.8 s | about 1.25 s | Slightly slower cutting, with **the payoff shot held**, is the old pattern [S]. Don't cut the payoff short |
| **Captions** | heavy ALL CAPS, 1-4 words, key words coloured (yellow/red) or black-on-white | neon green | Montserrat ALL CAPS, red/green key words | Similar. Not a difference worth changing |
| **Sound effects** | 3/4 used 3-5 (whoosh on circles, rim clank on misses, sub boom on hook, riser into payoff); Kobe used **game crowd sound** instead | 6 | 2-3 per Short | Similar count. **New:** natural game sound (crowd, rim, buzzer) under emotional/big moments [H] |
| **Length** | 16-29 s | 27 s | 15-28 s | No difference |

**What the old hits did better (bring back):**
1. A music bed, with the payoff marked by the music: a swell, a cut, or silence.
2. Kept broadcast scorebugs and banners as proof, circled when named.
3. Exact-moment footage under nearly every line.
4. Escalation to the payoff.
5. A held payoff shot.
6. One beat of silence before the final word.

**What they did worse (avoid):**
- the control's montage of generic highlights
- hype claims with no checkable fact
- a subscribe call-to-action ending
- the FT Short's 17 s with no answer (it worked as a list of absurd moments, not a story)

**What we already do better:**
- fact-checked claims with sources
- no CTA
- an answering ending as standard
- no stand-ins with the wrong scorebug (after #39)

**Topic vs execution:** the control (old Flagg, 4.9K) shared every production technique with the hits, while new Flagg (a visible height number, no music) did 20.6K. So topic and angle still dominate; the techniques above are craft, not reach guarantees [S].

**Applied Oct 14:**
- **Music:** library and mixing (`Library/Music Guide.md`); music versions of #40, #41 and #21 (the originals are kept).
- **Proof and circles:** the scorebug-as-proof and circle-on-the-named-detail rules are in Creative System v3 (§5).
- **Rules Audit:** the pace guideline was moved to 200-265 wpm in `qa_short.py`.
- **Tests:** the question-hook and silence-before-the-last-word tests are pre-registered in the Outcome Log.


## 11. Old scripts and old delivery, measured (added Oct 14, 2026, night)
**New evidence:** the narration of 12 of our old Shorts, exactly as voiced.
- The owner's own recordings were the training samples of the clone "pham v2". Full text and per-Short numbers: `Library/Reference Videos - old Shorts transcripts.md`.
- 10 of the 12 match a title with views; 2 are unconfirmed.
- It covers our biggest old Short (Bronny 1v1, 65K) and a flop from the same week (3 Plays Bronny Starter, 5K).

**1. The voice is not what changed.** [V]
- **Same voice:** the clone's current output matches the old narration at 0.93-0.95 (Resemblyzer speaker similarity), and the old recordings match each other at 0.99. Other voices score 0.60-0.72 against ours.
- **Same flat number delivery:** old numbers -1.3 to +0.8 dB vs other words (median about -0.2); ours -0.4 to +0.2.
- **Pace close:** old 206-252 wpm (median 220), new median 243.
- So the voice explains neither the old hits nor the new flops. The earlier claim (§10, from vidIQ's descriptions) that old hits "stressed every number" is not supported by the measured audio.

**2. The scripts did change.** [V counts; effect on views S/H]

| Feature | Old (12 voiced) | New (20 posted) |
|---|---|---|
| Median sentence length | **14.8 words** (flowing story) | **9.4 words** (staccato fact chain) |
| "First… second… third" or "Then it gets crazier" escalation | 5/12 | 2/20 |
| "It isn't X, it's Y" reframe ending | 2/12 (+ the 79K Bronny Short in §10: 3 hits) | 0/20 |
| Personality asides ("So considerate." "Literally office equipment." "It's wild.") | most scripts | rare |
| Opening question | 1/12 | 0/20 |
| First sentence ends | median 3.1 s | median 2.9 s |

- Within the old set, shorter sentences went with more views (rho -0.48, n=10); within the new set there's no link (+0.19, n=20). So sentence length alone isn't the lever.
- The difference is the **storytelling voice**: the old scripts sound like a person telling a friend something wild, with a reaction, a twist ("but not this time, because…") and a reframe. The new ones list facts.
- Topic and distribution still dominate (§2, §8). This is a craft difference to test, not a proven cause.

**3. Opening hooks: statements, not questions.**
- Old openers were bold claims: "Kyle Korver once got traded for a copy machine." / "This is why the WNBA is a joke." / "See, most rookies stay quiet, but Quentin Post did the exact opposite."
- Questions: 4 of 16 old Shorts we can read, counting vidIQ's 4. Q1 stays a test, not a direction.

**4. CoachClank** (the owner's reference; details in `Library/Sound Library.md`):
- Their TikToks use "original sound - CoachClank": their own mix, not a platform sound.
- Their narrator is a different voice from ours (0.74) and isn't in the top 400 ElevenLabs library voices (best 0.78).
- Narration 265-309 wpm (Round 9), with a tonal bed sitting only about 3-5 dB under the voice in the rare gaps (n tiny).

**Use it:**
- **Script direction (Creative System v3 §3/§5):**
  - write like telling a friend: one reaction aside, a twist connector ("then it gets crazier", "but not this time, because…")
  - escalation where the story has steps
  - a reframe ending ("The question isn't X, it's Y") when the story supports it
- **Pre-registered tests** (Outcome Log): R1 "story voice" script vs fact-chain script; R2 reframe ending.
