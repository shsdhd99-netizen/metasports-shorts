# Idea Gauging (Nov 1, 2026): should this Short be made, fixed, or skipped, and what about classic stories?

Owner's point: finding the right idea is what makes a Short viral. This note turns our own results into a pre-production filter (`python Tools/idea_gauge.py`). Evidence tiers: [V] measured on a large sample, [S] small sample, [H] judgement.

## 1. What separated hits from flops (our 132 NBA Shorts, 12 FC Shorts, 4,885 competitor soccer Shorts)
Hits (NBA, 35-80K): "NBA Players Are Doing THIS", "Why Does No One Like Bronny James?", "Why NBA Players Stopped Shooting Underhand", "Is It Possible To Dunk Without Jumping?" (Wemby), "The Most 200 IQ Play" (Luka), "Kobe's Final Game". FC hits (15-30K): the four goalkeeper-in-a-shootout stories.
Flops (sub-3K): "Did The NBA Call Out Four Stars", "How Many Picks Did Kawhi Cost?", "Why Jokic's Best Pass Doesn't Count", "Did Jalen Duren Just Leave $87 Million?", "The NBA Final That Does Not Count", "Jokic Could Break Westbrook's Record By Christmas", "Would Jordan's Last Shot Be a Foul Now?" (45 views), and FC's Zidane, Lewandowski, Coutinho, Hand-of-God Shorts.

Seven things the hits have and the flops lack [S, consistent with the competitor data]:
1. **A thing you can SEE in the first frame** (a note in a sock, a ball, a dunk without a jump), not a rule, a number or a contract.
2. **A lightning-rod name**: Bronny, Steph, Luka, Wemby, LeBron (people already argue about them). Flops feature "neutral" names or the league itself.
3. **A question the viewer can't answer** from the title ("Why does no one like Bronny?"), versus a question the viewer doesn't care about ("Did the NBA call out four stars?").
4. **No context lesson.** Rules, technicalities, picks, and money all need a paragraph.
5. **An arguable ending** (is he overrated?).
6. **Escalation and a reversal** (the FC hits all end by flipping the opening device).
7. **Not a flop shape:** rules/technicality, hypothetical ("would it be called now"), a pure record number, or news phrased "Did X just...?" (the last two clusters are 1.3-2.8K almost every time).

## 2. Classic / old stories: when they work
Our own evidence [S]:
- **Worked:** FC S01 (2006), S03 (2005), S05 (2018): old stories with an object or act nobody had seen, plus real footage. NBA: "Kobe's Final Game" (39K), "Why NBA Players Stopped Shooting Underhand" (73K: a decades-old fact with visible footage and a current question).
- **Flopped:** "Would Jordan's Last Shot Be a Foul Now?" (45 views: a hypothetical), the Rodman story (2.9K: famous, no new angle), "Luka Just Did What Kobe Never Did" (a record number), FC Zidane/Hand-of-God (the viewer already knows the headline).
- **Competitors:** "club history/origins" 1.02x (neutral) and "tragedy/injury" 0.88x: history as a category adds nothing; the unknown detail does.

**Classic-story rule (question j in the gauge):** make it ONLY if (1) most viewers don't know the specific detail, (2) real footage or photos of it exist, and (3) a modern hook is attached (a current player breaking or repeating it, an anniversary, a rule still argued about). Old + famous + no new angle = skip. Old + hypothetical = skip.

## 3. The gauge
Ten questions (a-j), each 0/1/2, weighted (total 50 points): a unknown-answer hook (x3), b lightning-rod subject (x3), c visible oddity (x3), d verified footage (x3), e arguable (x2), f escalation/reversal (x2), g fresh or modern hook (x2), h no context needed (x2), i not a flop shape (x3), j classic-story test (x2).
Verdict: **GO** at 68%+, **FIX** at 50-67% (it prints the three biggest missing points and the fix), **SKIP** below 50%, or SKIP outright when there is no verified footage, no hook and no lightning rod, or a flop shape with nothing visible.
Run it: `python Tools/idea_gauge.py --title "..." --lane nba --answers "a2 b2 c1 d2 e1 f2 g2 h1 i2 j1"`; `--list` prints the questions; `--backtest` re-scores the table below.

## 4. Backtest (in-sample, and biased: read this before trusting it)
I scored these 27 Shorts by judgement AFTER seeing their views, so the result is optimistic by construction. In the table, every Short with 35K+ views scores GO (68-86%) except FC S03 (66%, FIX); every NBA Short under 3K scores SKIP except the Wemby-rugby one (52%, FIX); three FC flops land in FIX (Balotelli derby, Zidane, Hand of God: 56-66%) instead of SKIP. So the filter would not have blocked those three, and it would have blocked the worst NBA ideas. That is useful but it is not a prediction.
**The real test starts now:** every new idea is scored BEFORE work and logged in `Research Notes/Idea Gauge Log.csv` (columns: date, idea, lane, answers, verdict, built?, views at 7 days). After 20 logged ideas, re-fit the weights. Do not trust the cutoffs until then [H].

| Short | Views | Answers (a..j) |
|---|---|---|
| NBA Players Are Doing THIS | 80K | a2 b1 c2 d2 e1 f0 g1 h2 i2 j1 |
| Why Does No One Like Bronny James? | 79K | a2 b2 c0 d1 e2 f0 g2 h2 i2 j1 |
| Why NBA Players Stopped Shooting Underhand | 73K | a2 b1 c2 d2 e1 f1 g1 h2 i1 j2 |
| Bronny James 1v1 With NBA All-Star | 65K | a1 b2 c2 d2 e1 f0 g1 h2 i2 j1 |
| Is It Possible To Dunk Without Jumping? (Wemby) | 55K | a2 b2 c2 d2 e1 f1 g1 h2 i2 j1 |
| The Most 200 IQ Play (Luka) | 53K | a1 b2 c2 d2 e1 f0 g1 h2 i2 j1 |
| The Most Unreal Ending in NBA History: Kobe's Final Game | 39K | a1 b2 c2 d2 e1 f1 g1 h2 i1 j2 |
| Is Bronny James Really This Bad? | 36K | a1 b2 c1 d1 e2 f0 g2 h2 i2 j1 |
| Would Jordan's Last Shot Be a Foul Now? | 45 | a1 b2 c1 d2 e2 f0 g0 h1 i0 j0 |
| Luka Just Did What Kobe Never Did | 1.3K | a1 b2 c0 d1 e1 f0 g2 h1 i0 j1 |
| Did The NBA Call Out Four Stars | 1.6K | a0 b1 c0 d1 e0 f0 g2 h0 i0 j1 |
| How Many Picks Did Kawhi Cost? | 1.8K | a1 b1 c0 d1 e1 f0 g1 h0 i0 j1 |
| Why Jokic's Best Pass Doesn't Count | 1.6K | a1 b1 c1 d1 e0 f0 g1 h0 i0 j1 |
| Did Jalen Duren Just Leave $87 Million? | 2.8K | a1 b0 c0 d1 e0 f0 g2 h0 i0 j1 |
| Jokic Could Break Westbrook's Record By Christmas | 2.6K | a0 b1 c0 d1 e1 f0 g2 h1 i0 j1 |
| Rodman Skipped A Finals Practice To Go Wrestling | 2.9K | a1 b1 c1 d1 e0 f1 g0 h2 i1 j1 |
| The NBA Final That Does Not Count | 2.3K | a1 b0 c0 d1 e0 f0 g1 h0 i0 j1 |
| Why Did Wemby Train With A Rugby Team? | 2.9K | a1 b2 c1 d1 e0 f0 g1 h2 i1 j1 |
| FC S01 Goalkeepers who hid a cheat sheet in a sock | 30K | a2 b1 c2 d2 e1 f2 g0 h2 i2 j2 |
| FC S05 cheat sheet on a water bottle | 29K | a2 b1 c2 d2 e1 f2 g0 h2 i2 j2 |
| FC S17 keeper subbed on just for penalties | 16.6K | a2 b1 c2 d2 e1 f2 g1 h2 i2 j2 |
| FC S03 keepers who danced on the line | 15K | a2 b0 c1 d2 e0 f2 g0 h2 i2 j2 |
| FC S02 trouble the day before a derby | 1.8K | a1 b2 c1 d2 e1 f2 g0 h2 i1 j1 |
| FC S04 sent off in their last game (Zidane) | 2.0K | a0 b2 c1 d2 e2 f1 g0 h2 i1 j0 |
| FC S06 five goals in nine minutes | 2.1K | a1 b2 c0 d2 e0 f1 g0 h1 i0 j1 |
| FC S08 Hand of God shirt | 3.2K | a1 b2 c2 d1 e0 f2 g0 h2 i1 j1 |
| FC S15 Coutinho transfer | 1.1K | a1 b1 c0 d1 e0 f1 g1 h1 i0 j1 |

## 5. How to use it in the daily run
1. Generate 5-8 ideas (Idea Bank, news, the milestone calendar).
2. Gauge each. GO: build. FIX: apply the printed fix and re-gauge once; if it still isn't GO, skip. SKIP: log it and move on, without writing a script.
3. Never gauge after scripting: the sunk cost biases the answers.
4. Log everything, including skips (so the weights can be re-fit and so a skip that later goes viral on someone else's channel teaches us something).
