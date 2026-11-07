# Theory ranking and rules challenge (Sat Nov 7, 2026, cloud)

> **APPLIED Nov 7 (owner: "approve all").** What changed and where: `Research Notes/Rule Changes Applied (Nov 7, 2026).md`. One proposal was overruled by the new lab the same day: A8 (pace over 230 wpm) is not a rule. The theories in section 1 are now re-checked daily by `python Tools/lab.py auto` (Rule check in `Research Notes/Lab/Study - all (<date>).md`).

Owner: "combine all research notes into theories, rank which ones are most important to add to rules, test, or scrap. then, rank every part of our videos the same way. challenge my current rules aswell to be fixed."

**What I read:**
- the 212 files in `Research Notes/` (the Nov 5 Master Index lists them), plus every study since (Nov 5-7);
- THE RULES in `MetaSports - Playbook.md`, the `Soccer Channel/Playbook.md` rules, the `daily-run` / `story-short` / `nba-short` skills;
- the QA code that actually blocks a Short (`qa_portions.py`, `qa_final.py`, `qa_short.py`, `edit_lint.py`, `precut_lint.py`);
- the stored prompts of the daily builds.

**Data, re-measured today:**
- the YouTube Analytics API pulled this morning (`Studio exports/api*/daily 2026-11-07.csv`), joined to `Shorts Dataset.csv` (stayed %) and `Scheduled Uploads.csv` (which file went up);
- **NBA:** restart-era Shorts only (Sep 25 on) that are 3+ days old: **n=60, median 5,520 views**;
- **FC:** 3+ days old: **n=16, median 3,202**;
- code and the joined table: scratch only; re-run with `shorts_dataset.py` + `learn.py`.

**Tiers:**
- **[V]** measured on our channels with n given, or stated by YouTube;
- **[S]** small sample, or competitors;
- **[H]** a guess.
- Every number here is correlation, not proof. n under 5 is a guess.

## 0. The answer in seven lines
1. **Two things decide our views: the premise, and the first 3 seconds.** Everything else is small or unmeasured. [V]
2. **FC's real hit lane is "a famous penalty shootout + one odd act", not "goalkeepers".** All 6 such Shorts got 8.6K-29K (median 19.6K). The other 10 FC Shorts are all under 3.8K (median 2.3K). [V]
3. **NBA's hit lanes are family/kid/rookie stories (2.5x) and "Who has missed the most ___ in NBA history" lists (2 of 3 at 24-26K).** Rules, history and news explainers sit at 0.4-0.6x. [V]
4. **Short NBA wins:** 25 s or less gets 6.4K vs 2.9K for longer. [V]
5. **Editing micro-rules don't move the numbers.** Cut counts, shot length, the one-source limit, clip counts, captions, cards: each within about 3 points of stayed %, or no data. Keep the cheap ones as house style; stop treating them as gates. [V/S]
6. **Our tests never finish.** The Test Log has 78 rows and every one says "variable: unknown". The music, caption, opener and real-audio tests were never logged, so none can be read. This is the biggest process fix. [V]
7. **Seven of our own rules contradict each other** (tags, FC time, posts per day, cuts in the first 3 s, loop, title shape, pinned comment). Section 3 has one fix for each.

---

## 1. Theories, ranked
Ranked inside each verdict by how much it should move views, times how sure we are.

### A. ADD TO RULES (or keep as a rule, with the evidence now attached)
| # | Theory | Evidence | Tier |
|---|---|---|---|
| A1 | **"Stayed to watch" is the gate; aim for 74%+.** It is decided by frame 1 + line 1. | Stayed vs views, rank correlation **0.75** (NBA n=40). 74%+ stayed: median **10,436** (n=13) vs 3,821 (n=47). YouTube lists "chose to view" first among Shorts ranking signals. 15 of 16 of our steepest retention drops happen in the first 4 s (Full Review). | [V] |
| A2 | **Premise first: the subject beats the edit.** | FC 6.5x for the proven lane. NBA lanes run from 0.4x to 3.6x of median. Edit variables move stayed % by 3 points at most (Script and Retention Study). | [V] |
| A3 | **FC lane = a famous penalty shootout + one odd act, by the keeper OR the takers.** | Shootout Shorts: sock 28.3K, water bottle 29.2K, subbed on 23.7K, danced 15.6K, **England subs 12.0K (no keeper trick)**, gloves 8.6K. All other FC: max 3.8K (n=10). Young ones fit too: S28 Kepa refused to come off before a shootout (24K in ~1 day), but S27, a goalkeeper story with no shootout, got 1.3K at ~2 days. Penalties without one famous shootout moment (S19 Man United "penalty nightmare", 3.8K) don't work. | [V] n=16; [S] for S27/S28 |
| A4 | **NBA: family / kid / rookie stories are the main lane.** | Titles about a dad, son, kid, brother, Bronny, Boozer, a rookie or teammates: **10,460 (n=12) vs 4,142 (n=48)**. Learned Weights: family 3.65x. | [V] |
| A5 | **NBA length 20-25 s.** | 25 s or less: **6,388 (n=44)** vs 2,913 (n=16) over 25 s; same stayed %, so likely replays. 20 s or less is no better (5,431, n=9); Learned Weights has under 20 s at 0.58x. Replays count as views since Mar 31, 2025 [V YouTube]. | [V] |
| A6 | **Line 1 is 11 words or fewer; frame 1 shows it happening.** (Already a rule; keep it.) | 72.6% vs 62.2% stayed (Oct 26, n=25/12). Engaged 0.557 vs 0.490 (Nov 3). | [V] small |
| A7 | **Hold the payoff on screen for the last 2-3 s.** | At 90% of the runtime hits keep 0.88 of the audience, flops 0.65 (20 NBA curves). | [S] |
| A8 | **NBA pace 235-260 wpm** (FC stays about 226-233, Ahmed's 230). | Over 230 wpm: stayed 69.4% vs 63.6%, views 3,974 vs 2,842 (n=19/15). Matches Round 5 (240-290). | [S] |
| A9 | **One new sourced fact per Short, and never retell a bigger channel's story.** (Keep; it's also our defence.) | YouTube's "inauthentic content" policy targets templated, mass-produced output. Copy-check TAKEN stories don't win for us. | [V official] |
| A10 | **Never delete or re-upload a slow Short; judge at 72 h.** (Keep.) | #48 had 25 views on day 0 and 14.6K by day 2. YouTube: re-posting a flop can look like spam. | [V] |
| A11 | **FC is the subscriber engine, NBA the view engine: protect FC's proven-lane supply first.** | Subs per 1K views: FC **1.36** vs NBA 0.43. One FC shootout Short gave 36 subs. | [V] |

### B. TEST (worth a real, logged test), ranked by expected value
Run at most 3 at a time per channel (section 3, R10).

| # | Test | Why | Tier | How |
|---|---|---|---|---|
| B1 | **NBA "Who has ___ the most in NBA history?" as a numbered serial** | Missed shots 25.6K and missed threes 24.0K; "lost the most games" got only 5.6K. Competitors: "Part N" serials break out 34% of the time vs 18%. | [V] n=3, [S] | Lists 1-5 are already in the Two-Week Plan. Copy-check each. Keep "missed" and "embarrassing" angles. |
| B2 | **FC: new premises from competitor breakouts** | Apart from goalkeepers, competitor lanes have the same median; they differ in **hit rate**. Breakouts: a star's relative with a twist (Haaland's dad 91x); "kept his promise" (Mbappe 16M, 628x); a one-mistake butterfly chain (3.7M, 141x); bargain scouting (1.1M, 900x); fans beat the club (45x). | [S] | Keep about half of FC builds on shootouts (S38 Bounou, S43 Van der Sar are ready); test one new premise a week. |
| B3 | **Why/How/What/Who title opener** | Ours: **6,794 (n=21) vs 5,004 (n=39)**, 1.36x. Competitors: 1.41x (n=31 of 528). Costs nothing. | [V] small, [S] | Alternate the opener on NBA; FC keeps "The goalkeeper who..." as the control. |
| B4 | **A natural loop** (the last line or frame flows into frame 1) | Replays count as views [V]. The 3.7M butterfly Short ends mid-sentence into its first line. Hits hold to the end (A7). | [S] | Two NBA + two FC; never add a shot just to loop. |
| B5 | **1 vs 2 posts a day** | Already planned from Nov 9 (Posting Plan). 2-post days did as well per post (4.1K vs 4.2K). | [S] | Keep running; read Nov 17, full read Dec 3. |
| B6 | **FC action-first opener** (the title on screen only, the first story line spoken over the action) | The FC drop happens exactly as the spoken title ends (-28 to -34 points at 1.8-2.4 s). Owner-approved Nov 1, never logged. | [V] curves, [H] fix | The next 2 shootout Shorts. |
| B7 | **Hook + foreshadow** (line 2 says what the ending is about) | Jenny Hoyos, with YouTube's Shorts lead. Our lines 2 are mostly backstory. | [S] | 4 Shorts, logged. |
| B8 | **Count-up numbers on the proof** | Dyson / PureBusiness. #99 Luka is the first one with it (53, 37). | [S] | Log "count-up" on #99 and the next 3; compare avg % viewed. |
| B9 | **Real audio on viral moments** | Owner, Oct 28. n=1 (#92 real-audio version). | [H] | Only on moments with a famous live call; log it. |
| B10 | **Music bed vs none** | Never readable: NBA posted almost all without music, and FC has 2 logged posts per arm (11.9K/3.8K with, 8.6K/1.1K without). | [H] | Run it only if logging is automatic (R9); otherwise drop it (section 3). |
| B11 | **Style v3 script moves** (a misread by 8 s, "what nobody knew" by 15 s, a reason for every "no") | PureBusiness (142K median). Not tried on a posted Short yet. | [S] | S21 Higuita is the test. |
| B12 | **Weekly NBA countdown** ("3 times [star] did X", #3 to #1) | In the Playbook since Oct 26, never run. The TikTok page's one breakout (438K) was a countdown of superstar dunks. | [S] | One a week, a superstar only. |

### C. SCRAP (stop spending time or credits on it)
| # | Theory or habit | Why it goes | Tier |
|---|---|---|---|
| C1 | **NBA rule / ban / history / news-explainer lanes** (Round 4's "rules and bans are the best lane") | Rule 2.8K (n=13), history 2.4K (n=8), news 3.8K (n=4) against a 6.8K median; history titles 1.3K (n=3). The one rule-shaped hit (underhand free throw, 29K) worked as a *curiosity you can watch*. Reframe a rule story that way, or skip it. | [V] |
| C2 | **Editing micro-rules as levers:** "3+ shots in the first 3 s", shot-length targets, "6+ source clips", "at most 35% from one source", the "same source back-to-back" rule | Shots in the first 3 s (2 or fewer vs 3+): stayed 66.7 vs 67.5. Average shot (1.8 s or less vs longer): 66.5 vs 69.7. FC reuse vs % viewed: +0.21. **S17 was 90% one source and got 23.7K.** These cost re-cuts (#99 needed 5 extra clips) and buy nothing. Keep only "shot 1 at least 2 s" and "frame 1 = the promise". | [V/S] |
| C3 | **The pinned "debate question"** | YouTube's Shorts ranking signals don't include comments. Likes and shares per view don't go with views (NBA -0.10 / -0.04, FC -0.35 / -0.17). Keep a pin only as a source line or a "Part 2" pointer. | [V official] |
| C4 | **Title tuning:** emoji, digits, question vs statement, name first, 5-7 words | Ours: question 5.6K vs statement 5.4K; emoji 5.7K vs 4.4K (n=8); digit 5.6K vs 5.4K. Competitors: all about 1.0x (528 Shorts). Only B3 survives. | [V/S] |
| C5 | **"Global names only" / star in the title** | NBA star in the title: 0.88x (n=26). FC: Messi napkin 1.0K; star-named 0.7x. Our FC hits are Lehmann, Krul and Kepa: **a famous moment beats a famous name.** | [V] |
| C6 | **Optimising the posting hour** | YouTube: "not something that we think about optimizing for". Ours: 5-10 AM ET 9.1K (n=14), 10 AM-2 PM 3.8K (n=9), later 5-7K: too small and mixed with topic. Keep a fixed grid; stop moving times. | [V official] |
| C7 | **The NBA 30-35 s length test** (Growth Study) | Our 16 NBA Shorts over 25 s already got 2.9K vs 6.4K. Not worth credits. | [V] |
| C8 | **Caption-style A/B** (CoachClank quiet captions, colour-word) | Inside six competitor channels the top and bottom halves edit alike (n=128). Expected value is low; park it. | [S] |
| C9 | **Script Critic craft scores and title scores** | They predicted views backwards (#40/#41). Already advice only; drop the scores. | [V] |
| C10 | **Custom covers as a reach lever** | The Shorts feed shows no thumbnail. One quick frame is enough; QA already only warns. | [V official] |
| C11 | **Likes/comments/shares bait** (CTAs, "comment below") | No link to views (C3). The owner's no-promo rule already covers it. | [V] |
| C12 | **"Same-day news" as its own NBA lane** | Fresh 5.0K vs evergreen 5.6K; news 0.62x. What works fresh is a *moment you can watch* (9.3K, n=6), not news explained. | [V] |

---

## 2. Every part of a video, ranked
Ranked by how much it moves views on our channels. "Verdict" says what to do with that part.

| Rank | Part | How much it moves views | Verdict | What to do |
|---|---|---|---|---|
| 1 | **Premise / topic** | Huge: FC 6.5x, NBA 0.4-3.6x | RULE | A3, A4; tests B1, B2 |
| 2 | **Frame 1 + line 1** (the first 3 s) | Huge: stayed tracks views at 0.75 | RULE | A1, A6; tests B6, B7 |
| 3 | **Length** | Large on NBA (2.2x) | RULE | NBA 20-25 s; FC 50-59 s (under 59.5) |
| 4 | **The ending** (payoff held, loop) | Medium (hits hold 0.88 vs 0.65) | RULE + TEST | A7; test B4 |
| 5 | **Script shape** (turns, escalation, one new fact per sentence) | Medium, measured only through topic | KEEP | Style v3 test (B11) |
| 6 | **Voice pace** | Small-medium | RULE | NBA 235-260 wpm |
| 7 | **Voice quality** (no glitches, every word said) | Protects; a bad take loses viewers | KEEP gates | voice_take gate stays |
| 8 | **Footage quality** (big, sharp, 3:4 crop, the named person on screen) | Protects | KEEP | rules 2.2 and 2.7 stay |
| 9 | **Proof on the footage** (words, circles, count-ups) | Small, unmeasured | KEEP style | test count-up (B8) |
| 10 | **Replay of the key second** | Unknown, cheap | KEEP default | no gate |
| 11 | **Title** | Small (search, 1.36x opener) | KEEP simple | test B3 |
| 12 | **Music bed** | Unknown (never logged) | TEST or DROP | R9 |
| 13 | **Real audio** | Unknown (n=1) | TEST | B9 |
| 14 | **Cut rhythm, shot counts, source mix** | None measured | SCRAP as gates | C2 |
| 15 | **Caption style** | None measured | KEEP house style | park the A/B (C8) |
| 16 | **Sound effects** | None or negative | KEEP "none decorative" | |
| 17 | **Posts per day** | Unknown | TEST (running) | B5 |
| 18 | **Posting time** | None | FIXED grid | C6, R3 |
| 19 | **Tags** | None measured | AUTO, never blocking | R2 |
| 20 | **Hashtags** | None (0-1) | KEEP 0-1 | |
| 21 | **Description** | None (1.00x) | KEEP empty | |
| 22 | **Pinned comment** | None | OPTIONAL | C3, R5 |
| 23 | **Cover** | None for the feed | WARN only | C10 |
| 24 | **Cross-posting** (TikTok/IG) | TikTok gets 0.1-0.5x of YouTube for story creators | KEEP same file, zero effort | |

---

## 3. Your rules, challenged (with the fix)
**(owner)** = your own rule, so you decide. **(internal)** = a contradiction or a rule I set; I'll fix it as soon as you say yes.

| # | Rule now | Problem | Proposed fix |
|---|---|---|---|
| **R1** (internal) | daily-run skill: "shot 1 at least 2 s, **3+ shots in the first 3 s**" | Contradicts the Playbook ("at most 2 shots in the first 3 s"), and "3+ cuts in 3 s" was REMOVED on Oct 26. With a 2 s first shot it means two cuts inside 1 s. The data shows no effect either way. | Delete it. Keep "shot 1 at least 2 s, frame 1 = the promise". |
| **R2** (owner + internal) | Tags: the daily-build prompts and Hub say **3-8 tags**; the Playbook and skills say **fill to 490** (you, Nov 1); `qa_portions.py` **FAILS** a Short with under 15 tags | Three rules for one box, and the strictest blocks finished Shorts over something with no reach evidence (Posting Study: tags aren't needed). | One rule: `tags_fit.py` fills the box automatically; a short list is a WARN, never a FAIL. Fix the prompts to match. |
| **R3** (owner + internal) | FC time: Soccer Playbook rule 7 and the FC build prompt say **8-9 AM ET**; the live grid (`next_gap.py`, Two-Week Plan) posts at **12 PM** | Two times in force. | Keep 12 PM (the grid slot: Nov 2-4, S29 today and S09 tomorrow go out at 12:00); fix the Playbook and the prompt. |
| **R4** (owner + internal) | Playbook §3: "up to 2 a day, **never 3**"; your Nov 5 rule and the daily-run skill: "up to **3** a day, 6 h apart" | Your newer rule wins, but the Playbook still says the old one. | Playbook to "up to 3, 6+ h apart, only if each is as strong". |
| **R5** (owner) | "Pinned comment: the two-sided argument" (Playbook §3; the build prompts ask for one) | No reach effect (C3). It costs a manual step on every Short. | Optional; when used, a source line or "Part 2". |
| **R6** (internal) | Rule 2.10: "**No forced loop**. End on the payoff." | Half right. Since Mar 2025 replays count as views, and hits hold to the end. | "End on the payoff, held 2-3 s. When it fits naturally, the last frame or line flows into frame 1. Never add a shot to loop." Test B4. |
| **R7** (internal) | Title "**a short statement**" (Playbook §3, Soccer rule 13) | No evidence that statements win; Why/How/What titles do 1.36x for us, 1.41x for competitors. | "Short and searchable (the name + the key word). A statement or a Why/How/What question." |
| **R8** (internal) | Soccer rule 2: "**Global names only**" (from Ahmed's channel) | Our FC hits name Lehmann, Krul, Kepa. Messi napkin got 1.0K. | "A famous **moment** (a World Cup or final shootout), not a famous name." |
| **R9** (owner) | "Render music + no-music for every FC Short; NBA alternates music/no music" | Nobody logged which file went up until `Scheduled Uploads.csv`. NBA ran almost all without music, so the NBA test never happened. Two renders per FC Short cost time for a test we can't read. | Either `schedule_ready.py` writes the arm into `Test Log.csv` automatically and we read 8 per arm; or drop music: NBA no music, FC whichever you prefer, one render. |
| **R10** (internal) | Test and Learn: "every attempt changes ONE variable, logged before building" | All 78 Test Log rows say "unknown". About 10 tests are open at once (opener, captions, music, real audio, foreshadow, length, cadence, Style v3, count-up, lists, countdown). At about 12 posts per arm, none can finish. | At most **3 live tests per channel**. NBA: lists serial (B1), Why/How/What opener (B3), posts per day (B5). FC: new premise a week (B2), action-first opener (B6), music only if auto-logged (B10). `build_gate.py` refuses a TESTING-lane build without a logged variable. |
| **R11** (internal) | QA warnings "one source over 35%", "6+ clips", "same source back-to-back" (`edit_lint`, `precut_lint`) | No effect on our data (C2), and they trigger re-cuts. | Remove them from the lints, or never act on them. |
| **R12** (internal) | NBA length: Playbook "voice 22 s or less"; Learned Weights "under 20 s is BELOW" | Two small samples pointing at the same window. | One target: **20-25 s file length**; QA warns outside 18-27 s. |
| **R13** (internal) | FC lane name "goalkeeper + odd device" | Too narrow and slightly wrong (A3). | "Famous penalty shootout + one odd act (keeper or takers)", one new shootout per Short. |
| **R14** (internal) | NBA lanes: "moments about half; same-day news; weekly countdown" | News sits below; the countdown never ran; family and lists are the measured winners. | NBA mix: family/kid/rookie + last night's moment (the 3:30 PM slot) + lists/record chases; countdown as the one weekly test. |
| **R15** (internal) | "Judge at 72 h, stayed % first" | Stayed % only comes from your Studio export, so the autopilot can't see it. | Same rule, plus the stand-ins written down. **FC:** avg % viewed 85%+ marks a hold (hits 83-96%, flops 64-82%). **NBA:** no API number separates hits from flops (engaged ratio 0.52-0.57 vs 0.49-0.58), so NBA is read on views at 72 h until the Monday export. |

**Owner rules I would keep exactly as they are** (the evidence agrees, or it's purely your call): drafts only, never open Studio; no promo or teaser at the end; no dead air; no cards; never re-upload; empty description; 0-1 hashtags; under 59.5 s (competitor breakouts run 74-76 s, but our broadcast footage makes a Content ID block over 1 minute a real risk).

---

## 4. What I'd change first (if you approve)
1. Fix the seven contradictions: R1, R2, R3, R4, R6, R7, R8. These are text edits plus one QA line (tags FAIL to WARN). No credits.
2. Rename the FC lane (R13) and point FC builds at shootouts: S38 Bounou, then S43 Van der Sar, are ready to voice.
3. Make tests real (R10): 3 per channel, auto-logged, everything else parked.
4. Drop the micro-edit lints (R11) and the 30-35 s test (C7).
5. Monday: your Studio export (stayed % for both channels) re-checks A1, A5 and the FC numbers with the real metric.

## 5. Where each number came from
- **NBA splits:** API daily 2026-11-07 + `Shorts Dataset.csv`, restart era (Sep 25 on), 3+ days old, n=60.
- **FC:** API FC daily 2026-11-07, n=16 aged 3+ days; S27/S28 counts from the Nov 7 FC run's public check.
- **Earlier studies:**
  - Script and Retention Study (Nov 6): pace, edit variables, 20 retention curves, 528 competitor titles;
  - Full Review (Nov 1): first 4 s, CoachClank frames;
  - FC Clip Repetition Study (Nov 4): reuse;
  - Pinned Comments (Nov 7): YouTube's signals, engagement correlations;
  - Posting Study (Oct 26): time, tags, description;
  - Growth Study (Nov 3): Hoyos, YouTube staff;
  - What Matters vs Wait (Nov 5): FC competitor lanes, 4,884 Shorts;
  - Deep Studies (Nov 6): xeysfc, butterfly;
  - TikTok Review (Nov 7);
  - Case Study deep dive (Nov 6): subs per 1K, concentration;
  - Learned Weights (Nov 7) and Test Log.
- **Not measurable today:**
  - stayed % for FC and for NBA after mid-October (needs the Studio export);
  - music, captions, opener and real-audio arms (never logged);
  - the 1-vs-2-a-day test (starts Nov 9).
