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
1. **The queue decides (Nov 7).** `python Tools/qa_sweep.py` (QA on every waiting draft + a read-back of every scheduled upload), then `python Tools/queue_rank.py --apply`: it plans every slot of the next 7 days in `Research Notes/Auto Queue.md` (ON YOUTUBE / PINNED / READY / BUILD / IDEA / MOMENT / EMPTY) and writes the slot into each READY card so `schedule_ready.py` books it. Build what the queue says for the first open slot: a BUILD folder by its deadline, else the IDEA, else (3:30 PM) last night's moment. HOLD drafts: fix the first problem the QA board names.
2. **A gap in the next 54 h?** `python Tools/next_gap.py nba|fc`. A gap means build the highest-scoring fresh idea (step 4). No gap: prep the next two ideas (script + sources, no voice) and stop with one log line.
3. A build needs `python Tools/build_gate.py <ch> --shape S --score N --fresh --autopilot` to say BUILD (gauge 80%+, FRESH, proven lane or ONE logged variable, open slot). DO NOT BUILD: log the reasons and stop.

## 4. Pick and build (only after the gate says BUILD)
- Data first: `python Tools/yt_analytics.py daily` (FC: `--channel fc`), then `python Tools/lab.py auto`; read `Research Notes/Lab/Scoreboard.md` and the Rule check in the newest `Research Notes/Lab/Study - all (<date>).md`. About 70% of builds come from proven lanes, about 30% from the live lab tests. A lane with 3 flops under the channel median pauses until Sunday (`test_log.py status`).
- **Tests (Nov 7, owner: "auto run and log tests yourself with a score"):** before scripting, run `python Tools/lab.py assign <ch> --folder "<folder>"` and build every arm it prints (it writes the card's `**Arms:**` line and `Research Notes/Lab/plans.csv`). Arms are detected from the files, so follow them exactly; never run more than the 3 live tests per channel in `Research Notes/Lab/tests.json`.
- Ideas: `Research Notes/Idea Candidates.md` (max 5 per channel; 12-point bar in the Autopilot Schedule) and `Research Requests`; `idea_gauge.py` + `copy_check.py` (FRESH only) before any work; footage must be verified to exist before scripting. Research notes cite every source link.
- NBA (Playbook N2): family/kid/rookie stories first, then last night's moment you can watch (morning after only), "Who has ___ the most in NBA history?" lists and live star chases; rules/history/news only reframed as a curiosity you can watch. **20-25 s**, no music, `/nba-short` + `/assemble`. FC (Soccer Playbook F1): **a famous penalty shootout + one odd act** (keeper or takers) is the proven lane, one new premise a week as the `fc-premise` test; `/story-short`, under 59.5 s; render music + no-music only while `fc-music` runs.
- Edit rules (Playbook S1-S3, E1-E7; Nov 7): frame 1 shows the promise, line 1 is 11 words or fewer, shot 1 about 2 s or more, the payoff held on screen 2-3 s, no decorative SFX or cards, proof on the footage. No cut-count, shot-length, clip-count or one-source rules (scrapped Nov 7; the lab re-checks them). Package (P1-P5): a short searchable title (a statement or a Why/How/What question, as `nba-opener` assigns), empty description, tags filled by `tags_fit.py` (a warning, never a blocker), pinned comment optional (a source line or "Part 2"), a quick `cover.jpg`.
- QA: `python Tools/qa_final.py "<folder>"` must say SHIP (qa_portions + `qa_short --full` on the DRAFT + file checks + Nov 7: never-twice, slot clash, stale "last night", test-arm match, the lab's predicted score; QA score 0-100). `python Tools/lab.py predict --folder F` scores a script before voicing (50 = typical; under 35 = filler only). LOOK at frame 1, every overlay and the last frame. The script critic is advice; only a factual error blocks beyond QA.
- Late news is dropped, not posted late.

## 5. Hub, schedule, log
- Write the Short's card on the channel Hub and the "Post: <title>" task (shapes and URLs: `Rule History - daily-run skill before Nov 6 rewrite.md`, section E). Read before writing, pin writes with `if_version`, never untick what the owner ticked, read the `inbox` notes first.
- Schedule through `schedule_ready.py` (dry run first, `--go` only when the owner's rules allow) using the slot `queue_rank.py` assigned. Run `python Tools/crosspost.py` at the end of each build (TikTok/Instagram get the SAME file; captions from `Crosspost Queue.md`).
- **Hubs (Nov 7: kept up to date automatically):** list each Hub's `shorts` and `ideas` collections and the task list's `tasks` (section post) with ArtifactData (`out_dir` `.hub_cache/nba`, `.hub_cache/fc`, `.hub_cache/tasks`), paste each listing's text into `.hub_cache/<kind>/versions.txt`, run `python Tools/hub_sync.py`, then send each `.hub_cache/out/<kind>.json` `writes` as one ArtifactData batch (max 50 per call) to its `url`. It fills results from the API, marks live Shorts posted, labels ready cards with their slot, adds missing posted cards, writes the week's UP NEXT cards and ticks Post tasks once live.
- **Roadmap:** `python Tools/roadmap.py` rewrites the LIVE STATUS block of `Roadmap - Next 90 Days.md` (milestones with dates at today's pace, the week's queue, tests, rule flags, QA).
- Daily Log (`AUTO:` line per slot: filled by whom, on time Y/N), `Tools/state.py`, then `bash Tools/handoff.sh "<where> account <n>" "<one line>"`. Commit and push.

## 6. Learn (every day)
- **Every day: `python Tools/lab.py auto`** (measures every Short, scores the live tests, writes `Research Notes/Lab/Scoreboard.md` and the study). When the Scoreboard shows a DECIDED test: edit the rule it names in `MetaSports - Playbook.md` / `Soccer Channel/Playbook.md` with the date and the score, add a line to `Research Notes/Lab/Decisions.md` if the tool didn't, and say it in the report. The next queued test starts by itself.
- Judge a Short at 72 h (the lab reads it 5-8 days after go-live, the API runs ~2 days behind) on stayed % (Studio export), then views and subs. A pattern on 3+ Shorts becomes a tiered lesson [V]/[S]/[H]; if it should be a rule, it becomes a lab test first (add it to the queue in `tests.json`), and a rule only after it wins.
- `python Tools/qa_audit.py`, then change ONE QA check and add one line to `Research Notes/QA Changelog.md`. `python Tools/idea_triage.py list`.
- **Look for new tools and skills (owner, Nov 6):** note one repeated manual step in the Daily Log and either script it in `Tools/` or add it to the right skill; list new tools in `Tools/README.md`.
- Sundays: `python Tools/weekly_review.py` and `python Tools/lab.py study --part all`. Any rule the Rule check marks **AGAINST** or **REVISIT** is fixed or dropped in the Playbook that day (one dated line each). On demand: `lab.py study --part edit|script|package|topic|length`.

## 7. Report (3-5 plain lines)
What was made or skipped, its slot, QA verdict, what was learned, and anything only the owner can do.

## Read when needed
`Research Notes/Rule History - daily-run skill before Nov 6 rewrite.md` (all old overrides), `Research Notes/Rule Changes Applied (Oct 26, 2026).md`, `Soccer Channel/START HERE.md`, `Soccer Channel/Lessons Learned.md`, `Research Notes/Lessons Learned (running log).md`.
