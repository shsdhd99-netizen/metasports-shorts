# Project: Autopilot Learning Loop (started Nov 5, 2026)

**Goal (owner):** build until the channels run themselves with high retention and millions of views. **Scope of this project:** make the loop that decides what to make, makes it, measures it and learns from it work without a human, and measure whether it beats today's baseline.

**Baseline (Nov 5):** NBA median 7K views per Short, 24K views/day, 0.43 subs per 1K views; FC median 3K, 9.6K views/day, 1.36 subs per 1K. Monetization needs 1,000 subs + 10M Shorts views in 90 days (20M for new applicants from Feb 1, 2027).

**The loop (each day, run by the autopilot; terminal/app sessions only improve tools while `AUTOPILOT_TEST.txt` exists):**
1. Pull data (`yt_analytics.py`, `channel_totals.py`), update lane states (`test_log.py status`).
2. Pick ideas: `idea_triage.py` candidates, gauged (`idea_gauge.py`), copy-checked, passed through `build_gate.py` (open slot, proven lane or one-variable test, 80%+, FRESH).
3. Build only what passes; QA (`precut_lint.py`, `edit_lint.py`, `qa_short.py`); schedule through the guard rails (`yt_schedule.py`, which now refuses placeholder titles and reads back the title).
4. Judge at 72 hours; write the lesson (`test_log.py result`); change one QA check (`QA Changelog.md`).
5. Health: `state.py` (what needs attention), `title_audit.py`.

**Success measures** (read Nov 17 and Dec 3; targets from the case studies): NBA 7-day average 35K views/day and subs per 1K 0.6 by Dec 5; FC 20K/day and subs per 1K at least 1.0; at least 3 of 10 Shorts above 15K (NBA); a second proven FC lane (4 Shorts at 1.5x the median) by Dec 31; 3M Shorts views in a rolling 90 days on NBA by Feb-Mar 2027.

**Experiments running:** posting cadence (alternating 1-vs-2, from Nov 9), lane tests (FC and NBA), length 30-35 s, foreshadow hook, tension-first hook, action-first FC opener.

**Open risks:** voice credits cap volume (121K characters a month); cloud routines blocked on keys (PC autopilot carries the load); data lags 1-2 days; sample sizes are small until about Nov 17; one silent bug can cost a Short (the Nov 1 "unknown" titles), hence the guardrails.

**First 14 days:** see `What Matters vs Wait (Nov 5, 2026).md` (decision calendar). Files: `Test and Learn Policy`, `Posting Plan`, `Efficiency Review`, `QA Changelog`, `Test Log.csv`, `Idea Candidates.md`.
