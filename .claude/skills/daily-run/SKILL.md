---
name: daily-run
description: >
  The automatic daily MetaSports run, one channel per run (nba or fc): pull analytics, learn from results, fill an open posting slot with the best
  Short that passes the build gate and full QA, schedule it, log everything, commit and push. Use when a scheduled task says "daily run", or the
  user types /daily-run nba|fc. Argument: nba (MetaSports) or fc (MetaSports FC). Rewritten Nov 6, 2026 (owner approved the cloud proposal);
  every old dated override is kept in `Research Notes/Rule History - daily-run skill before Nov 6 rewrite.md`.
---

# /daily-run nba|fc

Goal (owner): channels that run themselves with high retention and millions of views. A weak Short costs a slot, voice credits and channel signal:
**skipping is the default**; a skipped slot is logged `AUTO: <slot> skipped (best idea rated N)` in `Research Notes/Daily Log.md`.

## 1. Rules that never relax
- Never publish or open YouTube Studio. Scheduling goes only through `Tools/schedule_ready.py` / `yt_schedule.py` (private + publishAt, guard rails in `UPLOAD SCHEDULE.md`). Never delete or re-upload a posted Short (the owner decides).
- Never print, commit or ask for keys. Keys come from the environment (cloud) or `Tools/.env` (PC).
- Never invent a stat; write "missing" and why. Every claim line has a source row; under 60 s (end before 59.5 s); no promo or teaser at the end.
- Max 3 posts per channel per day, 6+ hours apart. No placeholder titles. Work on branch `main-329h3w`, never open or merge a PR; on a rejected push: pull `--no-rebase`, keep both sides of CSV logs, push again, never force.
- THE RULES at the top of `MetaSports - Playbook.md` win over this file; the posting grid is in `UPLOAD SCHEDULE.md` and `Tools/next_gap.py`.

## 2. Who builds what (check first)
- Read `Research Notes/BUILDER.txt` (`pc` or `cloud`) and today's Daily Log: build only if it names where you run and nobody holds a CLAIM for the slot (`Tools/team.py status`). Otherwise do the zero-credit steps and write `STATUS: not the builder`.
- **Exception (the PC safety net):** the PC gap-fill runs (6:45 AM NBA, 7:30 AM FC, `Tools/run_daily.ps1`) tell you "Build ONE Short for this open slot". When `next_gap.py` shows that GAP and nobody holds a claim, build it even if BUILDER.txt says `cloud`: the cloud cannot build without the YouTube keys, and an empty slot costs more than a double check. Claim the slot first (`team.py claim`); if a claim or a new DRAFT for it appeared after the pull, build nothing.
- PC: everything that needs YouTube footage and all renders. Cloud: research, copy-checks, scripts, source tables, cut plans from ESPN/archive.org, and NBA moment builds from ESPN clips only when the PC is offline. No ElevenLabs key: stop at script + notes (never fake a voice).
- Usage guard: weekly usage above 90% (or unreadable) means zero-credit steps only (analytics, `queue_rank.py`, schedule dry run), one STATUS line, exit.
- Setup: `git pull --no-rebase origin main-329h3w`, `bash Tools/cloud_setup.sh` (cloud), read `HANDOFF - latest.md` and the newest 2 Daily Log entries. `AUTOPILOT_TEST.txt` present = interactive terminal sessions do not build; scheduled runs pass `--autopilot`.

## 3. Decision order each run
1. **A paid-for draft is waiting?** `python Tools/queue_rank.py` ranks every waiting Short and gives it a slot (best first, stale moments dropped, weak ones as filler). Run `python Tools/qa_final.py "<folder>"`: SHIP means schedule it (`schedule_ready.py`), HOLD means fix first.
2. **A gap in the next 54 h?** `python Tools/next_gap.py nba|fc`. A gap means build the highest-scoring fresh idea (step 4). No gap: prep the next two ideas (script + sources, no voice) and stop with one log line.
3. A build needs `python Tools/build_gate.py <ch> --shape S --score N --fresh --autopilot` to say BUILD (gauge 80%+, FRESH, proven lane or ONE logged variable, open slot). DO NOT BUILD: log the reasons and stop.

## 4. Pick and build (only after the gate says BUILD)
- Data first: `python Tools/yt_analytics.py daily` (FC: `--channel fc`), `python Tools/learn.py ingest --fetch` then `report`; read `Research Notes/Learned Weights.md`. About 70% of builds are lanes marked ABOVE; 30% are experiments that change ONE variable (`Tools/next_arm.py`, `Tools/test_log.py`). A lane with 3 flops under the channel median pauses until Sunday.
- Ideas: `Research Notes/Idea Candidates.md` (max 5 per channel; 12-point bar in the Autopilot Schedule) and `Research Requests`; `idea_gauge.py` + `copy_check.py` (FRESH only) before any work; footage must be verified to exist before scripting. Research notes cite every source link.
- NBA: moments from last night (same day or morning after only), family, watchable curiosity, live star chases; no rules/history/news explainers. 20-30 s, `/nba-short` + `/assemble`. FC: `/story-short`, all lanes allowed (goalkeeper-odd-device is the proven lane; others are logged tests), music and no-music files, under 59.5 s.
- Edit evidence (use, do not re-debate): frame 1 shows the promise, line 1 is 11 words or fewer, shot 1 at least 2 s, 3+ shots in the first 3 s, pace 230-260 wpm, payoff held on screen 2-3 s with a loop frame, no decorative SFX or cards, proof on the footage. Package: short statement title, empty description, tags filled to about 490 characters (`tags_fit.py`), pinned-comment question, `cover.jpg` (`thumb.py --shape short`).
- QA: `python Tools/qa_final.py "<folder>"` must say SHIP (it runs qa_portions + `qa_short --full` + file checks); LOOK at frame 1, every overlay and the last frame. The script critic is advice; only a factual error blocks beyond QA.
- Late news is dropped, not posted late.

## 5. Hub, schedule, log
- Write the Short's card on the channel Hub and the "Post: <title>" task (shapes and URLs: `Rule History - daily-run skill before Nov 6 rewrite.md`, section E). Read before writing, pin writes with `if_version`, never untick what the owner ticked, read the `inbox` notes first.
- Schedule through `schedule_ready.py` (dry run first, `--go` only when the owner's rules allow) using the slot `queue_rank.py` assigned. Run `python Tools/crosspost.py` at the end of each build (TikTok/Instagram get the SAME file; captions from `Crosspost Queue.md`).
- Daily Log (`AUTO:` line per slot: filled by whom, on time Y/N), `Tools/state.py`, then `bash Tools/handoff.sh "<where> account <n>" "<one line>"`. Commit and push.

## 6. Learn (every day)
- Judge a Short at 72 h against the channel's last 10 on stayed %, the 90%-of-runtime hold ratio, views and subs gained (`test_log.py result` + one written lesson). A pattern on 3+ Shorts becomes a tiered lesson [V]/[S]/[H] and, if it is a rule, a QA check. Subs come from the first Short of a pattern; repeats earn views only.
- `python Tools/qa_audit.py`, then change ONE QA check and add one line to `Research Notes/QA Changelog.md`. `python Tools/idea_triage.py list`.
- **Look for new tools and skills (owner, Nov 6):** note one repeated manual step in the Daily Log and either script it in `Tools/` or add it to the right skill; list new tools in `Tools/README.md`.
- Sundays: `python Tools/weekly_review.py` (top 3 / bottom 3, one rule to keep, one to drop).

## 7. Report (3-5 plain lines)
What was made or skipped, its slot, QA verdict, what was learned, and anything only the owner can do.

## Read when needed
`Research Notes/Rule History - daily-run skill before Nov 6 rewrite.md` (all old overrides), `Research Notes/Rule Changes Applied (Oct 26, 2026).md`, `Soccer Channel/START HERE.md`, `Soccer Channel/Lessons Learned.md`, `Research Notes/Lessons Learned (running log).md`.
