# Tools, scoring and QA: how the system works now (Nov 7, 2026)

Owner, Nov 7: "go more in depth with the tools, scoring, and the qa for everything ... automatically make your own queue ... automatically update shorts hubs ... always update roadmap".
This page is the map. Every tool runs from the repo root and costs zero Claude credits unless it says so. The rules themselves are THE RULES (Nov 7) in `MetaSports - Playbook.md`.

## 1. The daily loop (who runs what)
| When | Step | Tool | Output |
|---|---|---|---|
| 3:43 AM ET | Research: last night's moments, competitors, soccer stories | daily research routine | `Research Notes/Daily Research/<date>.md` |
| 4:41 AM ET | NBA build for the slot the queue gives | NBA build routine → daily-run skill | a DRAFT + card + Hub card + Post task |
| 5:39 AM ET | FC build for the slot the queue gives | FC build routine → daily-run skill | same |
| 6:30 AM / PM ET | Upload READY drafts as private + publishAt | PC: `schedule_ready.py --go` | Scheduled Uploads.csv |
| 6:07 PM ET | Numbers, lab, QA sweep, queue, Hubs, roadmap | stats routine | everything in sections 2-6 |
| Sunday | Weekly review + rule check | `weekly_review.py`, `lab.py study` | rules fixed or dropped |

## 2. Scoring: how a Short gets a number before and after it goes out
**Before (`python Tools/lab.py predict --folder F`):**
- The predicted views at 72 h are the channel median times one factor per feature that the data backs.
- **The features:**
  - NBA: family/kid/rookie topic, 25 s or less, line 1 of 11 words or fewer, 15 shots or fewer, posted before 10 AM, a Why/How/What title, record list, countdown.
  - FC: famous shootout story, and similar.
- **Each factor's size:** the ratio of median views with vs without the feature, shrunk toward 1x by its sample size (`n / (n + 6)`). It's applied relative to how common the feature is, and a feature needs 4+ Shorts on each side to count at all.
- **The score:** 0-100 = 50 + 25 x log2(predicted / channel median). So 50 is a typical Short, 75 is about 2x, and 25 is about half.
- **Example:** S38 Bounou scores 77 (shootout story, 1.97x). #99 Luka scores 45 (no family angle, and a 12-word line 1).

**How good the scorer is:**
- Every day the lab predicts each past Short from all the others (a leave-one-out backtest), and prints the rank correlation in the study.
- **Nov 7:**
  - NBA: rank correlation 0.29 (n=52). Its top third beat the median 59% of the time, its bottom third 35%. A useful filter, not a crystal ball.
  - FC: can't be backtested yet (only 4 mature shootout Shorts). It fixes itself as S25-S29 mature.
- Under 0.2 means "trust topic judgement over the number".

**After: the tests (`python Tools/lab.py score`):**
- **Score** = the chance a Short from arm B beats a Short from arm A (50 = no difference). **p** = a permutation test.
- A test decides at 6+ per arm with p 0.2 or less (score 70+ or 30-). At 12 per arm with no winner it closes as NO DIFFERENCE.
- The metric is views at 72 h, read 5-8 days after go-live, because the API runs about 2 days behind. Avg % viewed is shown next to it.

**The parts of a Short (`python Tools/lab.py study --part topic|script|edit|package|length`):**
- Every feature split, with medians, n, score, p and a plain read ("likely real", "maybe", "no sign", "too few").
- The **Rule check** says whether each rule is still SUPPORTED, NOT SHOWN yet or AGAINST, and whether each scrapped rule still shows no effect.

## 3. QA: the layers, in the order a Short meets them
| Stage | Tool | Fails (blocks) | Warns |
|---|---|---|---|
| Idea | `idea_gauge.py`, `copy_check.py`, `build_gate.py` | gauge under 80%, TAKEN, no slot, a test lane without a variable (a live lab lane test counts) | |
| Script | `script_lint.py`, `lab.py predict` | | line 1 over 11 words, readability, CTA/question ending; predicted under 35 = filler |
| Pre-cut | `precut_lint.py` | shot 1 under 2 s | repeated source ranges |
| Picture | `edit_lint.py` (inside qa_short) | | same angle 3x in the hook, tiny hook subject, a cited scorebug cropped out |
| Retention gate | `qa_short.py --full` (now runs on the DRAFT itself; it was silently skipped before Nov 7) | no action in the first 3 s, a filler first word, dead air, black, frozen or flat frames, broken render, quote lip sync, unverified or missing clips, loudness | NBA outside 18-27 s, payoff held under 1.8 s, time-bound words, absolute-claim words, a number shown twice |
| Portions | `qa_portions.py` | no 2 source links, voice issues, true peak over -1 dB, a dark frame 1, placeholder title, title over 100 characters, no tags at all, tags over 490 characters, no QA PASS line | short tag list, voice CHECK, no cover |
| Final | `qa_final.py` → SHIP / FIX / HOLD + QA score (100 - 30 per FAIL - 4 per WARN) | not 1080x1920, over 59.5 s, black first or last frame, unverified sources; **new Nov 7:** title already live, a slot clash (6 h or a 4th post), "last night" over 30 h before the slot | card arms don't match the build; predicted score under 35; slot in the past |
| On YouTube | `qa_sweep.py` (daily) | video missing; placeholder or wrong title; not private with publishAt at the planned slot; two uploads with one title | under 3 tags; slot passed but still private |

`Research Notes/QA Board.md` lists every waiting draft (verdict, QA score, predicted score, the first thing to fix) and every scheduled upload as YouTube actually has it.

**On Nov 7 it found:**
- 5 drafts on HOLD:
  - #65 LeBron-Knicks: 0 source links;
  - #79 buzzer-beaters: no real title;
  - #58 Bronny/Knecht: 1 source link;
  - #61 Paul George: 0 source links;
  - #53 opening tip: no cut plan.
- All 11 real scheduled uploads matched YouTube.

## 4. The auto queue (`python Tools/queue_rank.py [--apply]`)
Every slot of the next 7 days, filled in this order:
- **ON YOUTUBE** (booked);
- **PINNED** (an owner-set slot);
- **READY** (built, SHIP/FIX; paid-for voice goes out unless predicted under 30);
- **BUILD** (recent prep: voice + cut by slot - 20 h);
- **IDEA** (80%+ candidates: research + build by slot - 44 h);
- **MOMENT** (the NBA 3:30 PM morning-after slot);
- **EMPTY**.

**Priority** = predicted score
- \+ 25 for READY;
- \+ 40 for PINNED;
- \+ 8 if it feeds a live lane test that still needs Shorts;
- \- 8 if it repeats the channel's previous lane;
- \- 10 for an IDEA.

**Limits:**
- FC gets at most one new non-shootout premise a week.
- A prepped Short predicted under 40 only fills a slot nothing else wants (shown as "filler").
- Stale news and moments are dropped.
- `**Queue:** no (why)` in a card or notes keeps a folder out (used for #93, #96 and #97 on Nov 7).

`--apply` writes the slot into each READY card, so the PC scheduler books it. Owner-set slots are never moved.

**Output:** `Research Notes/Auto Queue.md` (for people) and `Research Notes/Lab/queue.json` (for the Hub sync and the roadmap).

## 5. The Hubs (`python Tools/hub_sync.py`)
The routine saves each Hub's documents (`.hub_cache/`, git-ignored), the sync works out what changed, and one batch per Hub applies it.

**What it updates:**
- **Live Shorts:** status "posted", the YouTube link, and results (views, avg % watched, stayed % from the Studio export or the API's engaged %, the go-live date, the 72 h views). A real stayed % already on a card is never overwritten.
- **Ready cards:** a slot label ("Scheduled on YouTube: Wed Nov 11, 7:15 AM ET" or "Auto queue: …").
- **Missing cards:** live Shorts with no Hub card get a posted card (Nov 7: #82-#89 and S19, S20, S25, S26 were missing).
- **The ideas list:** "UP NEXT" cards for every slot of the week.
- **Post tasks:** ticked done once the Short is live. Never unticked.
- **Never touched:** rejected, held or skipped cards.

**First run (Nov 7):** 79 writes across both Hubs.

## 6. The roadmap (`python Tools/roadmap.py`)
The LIVE STATUS block at the top of `Roadmap - Next 90 Days.md` is rewritten daily. It shows:
- subscribers and per-day growth;
- views a day (7-day vs 28-day);
- the last-90-day total against 3M / 10M / 20M, with the date each is reached at today's pace;
- the week's queue;
- the live tests;
- the rules the data questions;
- the QA summary.

It also refreshes `channel_daily <date>.csv`, which `state.py` and `weekly_review.py` read.

**Nov 7:**
- NBA: 650 subscribers (1,000 around Jan 17 at today's pace); 23.4K views a day, 70% of the fan-funding pace.
- FC: 183 subscribers (500 around Jan 5).

## 7. What still needs a person
- Approving a Short if you want to (the card's `**Approved:** yes` line plus `schedule_ready.py --require-approved`).
- Pinning comments (optional now).
- The Monday Studio export ("stayed to watch" for both channels: the lab's best metric).
- Answering when the QA board shows a FAIL on YouTube (the system never edits YouTube).
