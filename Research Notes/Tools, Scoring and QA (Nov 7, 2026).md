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
| Script (pre-voice gate, Nov 7) | `script_lint.py` (exit 1 on FIX), `lab.py predict` | NBA outside about 16-28 s or FC outside 185-240 words / over 59.5 s at 234 wpm, line 1 over 11 words, a filler first word, a question/CTA last line, a bare "3-0" | NBA outside 20-25 s, FC that may pass 59.5 s on a slow take, "last night", readability; predicted under 35 = filler |
| Pre-cut | `precut_lint.py` (times shots from the anchors) | shot 1 under 2 s, an anchor not in words.json, no action shot in the first 3 s, overlay text reaching the caption band, window past the source end, no `why` | an anchor pinned mid-sentence while a later copy starts a phrase, overlays too fast to read, a shot over 6 s, repeated source ranges |
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

## 7. Building fast (Nov 7 efficiency pass: `python Tools/build.py`)
Owner, Nov 7: "make processes more efficient, faster, and easier". The Nov 5 Efficiency Review found the time goes to re-cut loops and
footage hunting, so the fixes target those.

| Stage | Command | What it runs, and where it stops |
|---|---|---|
| Where am I? | `build.py status F` | a checklist (script, 2+ sources, UPLOAD.md, voice, cut plan, clips, verified, DRAFT, SHIP) and the next command |
| Footage | `espn_clip.py clips --date YYYYMMDD --team LAL [--find luka]`, then `espn_clip.py get <ids> --folder F` | a game's ESPN clips by id; 1080p into `src/` with a `.url` sidecar, so sources.csv fills itself |
| Voice | `build.py voice F` | the pre-voice gate (stops on FIX: no credits spent), voice_take, tighten_voice, the predicted score, the voice length vs the channel window |
| Cut | `build.py cut F`, LOOK at the sheet, `build.py cut F --verified` | precut_lint (stops on FIX), cut_list (fills `len` from the anchors; no fill_len step), sources.csv links, the contact sheet |
| Render | `build.py render F` | assemble by channel (NBA no music; FC + music while `fc-music` runs), the DRAFT names, cover.jpg, qa_final, `_hub/s.mp4` + `_hub/prev.mp4` |

Tested on a copy of #99 Luka: cut plan to SHIP + Hub files in 89 s, with no hand steps. On the same Short the old way took a hand
`fill_len` run, a re-cut for the "Last" anchor, and a hand patch of sources.csv that set every row to one ESPN link (now fixed: 6 different clips).

**Health:** `python Tools/tool_check.py` compiles all 111 tools on the running Python and runs the self-tests and read-only smoke runs
(about 3 s). Run it on Sundays and after editing a tool: the Python 3.11 break in `test_log.py` had silently switched off build_gate's lane check.

## 8. What still needs a person
- Approving a Short if you want to (the card's `**Approved:** yes` line plus `schedule_ready.py --require-approved`).
- Pinning comments (optional now).
- The Monday Studio export ("stayed to watch" for both channels: the lab's best metric).
- Answering when the QA board shows a FAIL on YouTube (the system never edits YouTube).
