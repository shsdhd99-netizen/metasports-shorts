# FC Clip Repetition Study (Nov 4, 2026)

**Question (owner's hypothesis):** repeating clips inside a Short drops retention. **Tested, not assumed.** Method code: `Tools/fc_reuse.py` (measures) and `Tools/fc_study.py` (join + stats; rerun to reproduce). Data: `cuts.json` + `shots.json` per Short folder; outcomes from `Research Notes/Studio exports/api FC/daily 2026-11-04.csv` (avg % viewed, subs) and `Content 2026-10-07 to 2026-11-04 FC/Table data.csv` (views, subs; S20's % viewed derived from watch time); curves from `api FC/retention 2026-11-04.csv` (13 of the 15 Shorts have curves; S20 and S25 do not).

## Verdict
**Not supported at n = 15.** Clip reuse is not associated with lower % viewed or lower views. The Shorts with the most reuse (S17 subbed-on goalkeepers: 10 overlapping source ranges, 90% of runtime from one source file; S01 sock: 3) are two of the four biggest winners, and the best Short by retention (S05 water bottle, 96%) has none; low performers S06, S07, S02 also have none. Every correlation with views is mildly positive, with 95% bootstrap intervals that all include 0. What separates winners from losers in this data is topic shape (a goalkeeper doing something odd), not editing reuse [S, consistent with `Studio Analytics Review (Nov 4, 2026).md`].

Evidence tiers: **[V]** measured and the effect holds with n stated; **[S]** seen in the data, small n; **[H]** guess.
- [V] No detectable negative effect of reuse on % viewed in these 15 Shorts: Spearman(unexcused overlaps, % viewed) = +0.21, 95% CI [-0.23, +0.79]. With n = 15 a real small effect of either sign cannot be ruled out.
- [S] Retention drops happen in the first 3 to 10 seconds in every curve (the hook), where repeated shots almost never occur (a repeat needs an earlier use first). Windows that contain a repeated-shot start lose LESS on average (2.8 pt, n = 20 windows) than windows that do not (5.1 pt, n = 227); that is mostly the position effect, not a benefit of repeating.
- [H] A viewer who sees the same moment twice may leave; this data cannot show it because the repeated moments in the winners are replays of the key action (S17 replays the sub-on and the save).
- Limits: the measure counts the same source file with overlapping time ranges (cuts.json). It cannot see the same moment arriving from two different files (a broadcast and a highlight reel); the picture-level check (2 fps difference hash) covers that partly. Single-source share is high for most Shorts because they cut one long match video.

## Table (n = 15 Shorts with outcomes)
| Short | views | avg % viewed | subs | shots | mean shot s | overlapping pairs (unexcused) | min gap s | max one-source share | consecutive same-source | visual repeats (of frames) |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | 30,401 | 93% | 87 | 42 | 1.43 | 3 (3) | 15.4 | 0.64 | 20 | 6 of 119 |
| S02 | 1,820 | 82% | 4 | 48 | 1.33 | 0 (0) | None | 0.52 | 19 | 0 of 126 |
| S03 | 15,554 | 83% | 11 | 58 | 1.22 | 2 (2) | 0.0 | 0.25 | 28 | 1 of 141 |
| S04 | 1,965 | 72% | 0 | 40 | 1.45 | 1 (1) | 0.0 | 0.20 | 15 | 1 of 116 |
| S05 | 29,206 | 96% | 8 | 40 | 1.79 | 0 (0) | None | 0.12 | 11 | 0 of 119 |
| S06 | 2,051 | 64% | 1 | 38 | 1.58 | 0 (0) | None | 0.70 | 24 | 9 of 125 |
| S07 | 2,512 | 79% | 2 | 35 | 1.60 | 0 (0) | None | 0.13 | 10 | 0 of 110 |
| S08 | 3,279 | 74% | 4 | 25 | 2.12 | 8 (4) | 0.0 | 0.35 | 11 | 4 of 106 |
| S15 | 1,146 | 68% | 3 | 28 | 1.89 | 3 (1) | 2.5 | 0.36 | 13 | 0 of 105 |
| S16 | 3,116 | 67% | 1 | 30 | 1.93 | 1 (0) | 4.4 | 0.19 | 3 | 0 of 115 |
| S17 | 23,583 | 87% | 36 | 26 | 2.15 | 11 (10) | 0.0 | 0.90 | 21 | 3 of 104 |
| S18 | 2,923 | 73% | 3 | 32 | 1.62 | 5 (3) | 6.8 | 0.37 | 14 | 2 of 104 |
| S19 | 3,342 | 64% | 4 | 32 | 1.78 | 1 (1) | 3.2 | 0.57 | 30 | 5 of 112 |
| S20 | 1,012 | 35% | 0 | 37 | 1.54 | 1 (0) | 51.8 | 0.16 | 3 | 1 of 113 |
| S25 | 5,318 | 59% | 1 | 49 | 1.10 | 2 (1) | 0.0 | 0.86 | 44 | 1 of 108 |

Columns: overlapping pairs = pairs of shots with the same source file and overlapping time range, unexcused count (shots marked `replay: true` are excused) in brackets; min gap = shortest time between the two uses; max one-source share = share of runtime on one source file; consecutive same-source = back-to-back shots from the same file (mostly different moments of one match); visual repeats = sampled frames (2 fps) matching an earlier frame 3 s or more before, out of frames sampled.

## Correlations (Spearman, 95% bootstrap CI, 4000 resamples, n = 15)
```
spearman(n_unexcused, pct) = +0.21  95% bootstrap CI [-0.23, +0.79]
spearman(n_unexcused, views) = +0.46  95% bootstrap CI [-0.04, +0.80]
spearman(n_unexcused, subs1k) = +0.37  95% bootstrap CI [-0.04, +0.78]
spearman(overlap_pairs, pct) = +0.13  95% bootstrap CI [-0.40, +0.66]
spearman(overlap_pairs, views) = +0.42  95% bootstrap CI [-0.22, +0.73]
spearman(overlap_pairs, subs1k) = +0.39  95% bootstrap CI [-0.12, +0.74]
spearman(max_src_share, pct) = -0.10  95% bootstrap CI [-0.69, +0.55]
spearman(max_src_share, views) = +0.25  95% bootstrap CI [-0.35, +0.75]
spearman(max_src_share, subs1k) = +0.44  95% bootstrap CI [-0.12, +0.81]
spearman(consec_same, pct) = -0.02  95% bootstrap CI [-0.63, +0.59]
spearman(consec_same, views) = +0.39  95% bootstrap CI [-0.10, +0.72]
spearman(consec_same, subs1k) = +0.17  95% bootstrap CI [-0.41, +0.62]
spearman(mean_shot, pct) = +0.11  95% bootstrap CI [-0.50, +0.63]
spearman(mean_shot, views) = +0.07  95% bootstrap CI [-0.45, +0.67]
spearman(mean_shot, subs1k) = +0.25  95% bootstrap CI [-0.29, +0.76]
spearman(vis, pct) = -0.18  95% bootstrap CI [-0.60, +0.49]
spearman(vis, views) = +0.26  95% bootstrap CI [-0.24, +0.75]
spearman(vis, subs1k) = +0.17  95% bootstrap CI [-0.37, +0.70]
```

## Retention curves vs repeated shots
| Short | biggest drop windows (second marks) | repeated-shot starts inside them | steepest 5% windows holding a repeated shot | share of all windows holding a repeat |
|---|---|---|---|---|
| S01 | 1-4s (-50pt), 4-7s (-16pt), 7-10s (-7pt) | 2 | 0 of 3 | 11% |
| S02 | 1-4s (-34pt), 4-7s (-17pt), 7-10s (-9pt) | 0 | 0 of 3 | 0% |
| S03 | 1-4s (-42pt), 4-8s (-16pt), 8-11s (-7pt) | 2 | 0 of 3 | 11% |
| S04 | 1-3s (-26pt), 3-6s (-14pt), 6-9s (-7pt) | 1 | 0 of 3 | 5% |
| S05 | 1-4s (-55pt), 4-7s (-15pt), 37-40s (-5pt) | 0 | 0 of 3 | 0% |
| S06 | 4-6s (-21pt), 1-4s (-21pt), 6-9s (-10pt) | 0 | 0 of 3 | 0% |
| S07 | 1-3s (-35pt), 3-6s (-17pt), 6-9s (-11pt) | 0 | 0 of 3 | 0% |
| S08 | 1-3s (-21pt), 3-6s (-17pt), 6-8s (-10pt) | 4 | 0 of 3 | 21% |
| S15 | 1-3s (-17pt), 6-8s (-14pt), 3-6s (-12pt) | 1 | 0 of 3 | 5% |
| S16 | 1-3s (-23pt), 3-6s (-13pt), 6-9s (-12pt) | 0 | 0 of 3 | 0% |
| S17 | 1-3s (-37pt), 3-6s (-12pt), 6-9s (-8pt) | 8 | 1 of 3 | 37% |
| S18 | 1-3s (-27pt), 3-6s (-14pt), 6-8s (-11pt) | 3 | 0 of 3 | 11% |
| S19 | 1-3s (-21pt), 3-6s (-20pt), 6-9s (-17pt) | 1 | 0 of 3 | 5% |

mean 5%-window drop: windows with a repeated-shot start 2.8 pt (n=20), without 5.1 pt (n=227)


Reading: the steepest drop windows are in the first 10 s for all 13 curves; in 12 of 13 none of the three steepest windows holds a repeated shot (S17 has one, because it repeats from the start). No curve shows a drop that lines up with a repeated clip beyond the hook.

## What I shipped regardless
Repetition is a known risk and cheap to avoid, so `Tools/edit_lint.py` (runs inside `qa_short.py`) now flags: the same source and time range twice (exception: `replay: true`), one source over 35% of the runtime, and consecutive shots from one source within 3 s. It is advice, not a gate, because the evidence above does not justify blocking posts. `python Tools/edit_lint.py --selftest` proves it flags S26 (36 overlaps) and passes a clean fixture. Rule added to `.claude/skills/story-short/SKILL.md`, `Soccer Channel/Lessons Learned.md` and `CLOUD DAILY RULES.md`.

## Next test (so the question gets an answer)
S26 (36 unexcused overlaps), S27 and S29 are the strongest repeats yet and are recent: compare their % viewed and curves at 7 days against S28 (clean). Rerun `python Tools/fc_study.py` after adding them to the VID map in the script.

## Update Nov 5, 2026 (more testing; `Tools/fc_study.py` reruns all of it)
- **Data-quality fix.** Two rows (S20, S25) had no API value for average % viewed yet, so their % was derived from watch time (S25 came out 59% where Studio showed 92%). Derived and API values are not comparable. **Re-run on API-only rows (n = 13): same answer.** Spearman(unexcused overlaps, % viewed) = +0.19, CI [-0.31, +0.79]; with views +0.51, CI [-0.16, +0.79]. [V] still "no detectable negative effect".
- **Topic control.** Inside the goalkeeper lane only (S01, S03, S05, S17, S25) n = 5: Spearman(overlaps, views) = +0.20, CI [-0.60, +1.00]. Too small to say anything; it is listed only so nobody reads the pooled number as a topic effect. [H]
- **Natural experiment (the strongest repeater).** S26 "Goalkeepers who took their gloves off" has 36 unexcused overlapping source ranges and 88% of its runtime on one source file. Public count Nov 5: **12,967 views about a day after it went public** (Nov 4). Its goalkeeper-lane sibling S25 (1 overlap) read 5,318 views at day 1 in the Studio export and 17,328 on Nov 5. A video with the most repetition we have shipped is tracking in the top half of the channel [S]. Its retention curve is not available yet (the API lags 2 days); **check again Nov 7**: if its average % viewed is under 75% while goalkeeper-lane peers are 83-96%, the hypothesis gets support; if it is 85% or above, it is dead for this channel.
- **What would still change my mind:** a Short whose curve shows a drop at the exact second a repeated clip returns, with the same topic shape and a clean sibling to compare. S26 vs S28 (clean, 1 overlap, 60% on one source) is that pair.
- Not testable with this data: repeats that come from two different files showing the same moment (the dhash visual check flags some, e.g. S06 9 frames, S19 5 frames, but they too do not line up with a worse % viewed).
