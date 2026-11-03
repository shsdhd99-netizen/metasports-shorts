# ACCOUNT 1: START HERE (written Tue Nov 3, 2026, about 10:30 PM ET; first used Wed Nov 4, 1:30 PM ET by the scheduled task "MetaSports terminal resume")

You are the Claude account signed in on the owner's Windows PC terminal (the owner calls it account 2; the other account is 'account 1'/Account 2 branch in older files: the account that owns the cloud routines is the one this terminal uses, so RemoteTrigger works from here). Your job at 1:30 PM Wed is to START the automation on this account and CHECK that every part works (section 3A), then keep it healthy. You are on the owner's Windows PC, in the repo `C:\Users\Admin\Documents\metasports-shorts` (Git Bash or PowerShell), branch `main-329h3w`, remote `shsdhd99-netizen/metasports-shorts`.
Roles: **cloud routines build** (BUILDER=cloud); **you** (PC terminal, Account 1) run the zero-credit chores, merge Account 2, fix what the cloud cannot do (YouTube-only footage, scheduling),
review the results and improve the system. The owner is away most of the time: act, do not ask, except for the owner-only list in section 6.

## 0. Rules that never change
Never publish, never open YouTube Studio, schedule only through `Tools/yt_schedule.py` guard rails (private + publishAt; slot 20 min to 30 days away; never re-upload a file; DRAFT file names only)
and only as section 7 allows. Never print, commit or paste keys (`Tools/.env`). Shorts under 59.5 s, no promo ending, no stat without a source, at most 2 posts a day per channel 6+ hours apart,
never delete and re-upload a Short. No mass-delete by name or glob (exact ids only). Commits end with `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
Do not commit `clips/`, `src/`, `voice_raw.mp3`, `_voice_*`, `.url`, or any file over about 20 MB (the push fails; DRAFT mp4s are 90+ MB).
Auto mode blocks creating persistent scheduled tasks and similar: ask the owner to run a script (like `Tools/register_tasks.ps1`); do not work around it.

## 1. What exists (all committed)
| Need | Where |
|---|---|
| One-page index | `EVERYTHING - index (Nov 3 night).md` |
| Cloud rules (both accounts and both routines read this first) | `CLOUD DAILY RULES.md` |
| Who builds, cloud/PC split, PC request queue | `Research Notes/BUILDER.txt`, `BUILDER.md`, `PC Requests.md` |
| Live status, claims, usage | `Research Notes/STATE.md`, `USAGE.txt`, `Preflight.md` |
| Health check (keys, tokens, credit, disk, tasks) | `python Tools/preflight.py` |
| Learning loop | `python Tools/learn.py all --fetch` -> `Research Notes/Experiments.csv`, `Learned Weights.md` |
| Ready-draft scheduler (dry run default, `--go` uploads) | `Tools/schedule_ready.py` and `.bat` (timers registered) |
| Opt-in editing upgrades | `Tools/edit_upgrade.py` (+ `Productions/MetaSports/2026-11-03 DEMO - editing upgrade 73`) |
| Hook lint | `Tools/script_lint.py` flags a line 1 of 12+ words |
| PC fallback runner per channel | `Tools/run_daily.ps1 nba|fc` (not registered; fallback only) |
| Skills | `.claude/skills/daily-run` (0a usage guard, 0b builder, learned weights), `story-short`, `cloud-short`, `assemble`, `voiceover` |
| Longer lists | `HANDOFF - Nov 4 resume 1-30 PM.md`, `HANDOFF - Nov 3 terminal.md`, `AUTOMATION TO-DO (Nov 3).md`, `Research Notes/Improvement Backlog.md` |

## 2. Registered on this PC (verified Nov 3, about 10:30 PM)
`MetaSports analytics` daily 3:20 AM (commits CSVs) | `MetaSports schedule ready AM` 6:30 AM and `PM` 6:30 PM | `MetaSports terminal resume` once, Wed Nov 4 1:30 PM (this session) | `ClaudeDesktopStayAwake`.
Cloud routines (enabled Nov 3, environment `env_016GURtEd17FS3mEXiKSjfM6`, repo attached, prompts point at `CLOUD DAILY RULES.md`): NBA `trig_01PUCBRzwuJ1j1r3Y53GdfoY` 3:17 AM ET,
FC `trig_011nY5arZZHcgKkWQvcBkNKc` 4:23 AM ET. The owner said the cloud keys were pasted; that cannot be verified from the PC. Verify with the routine logs (section 3, step 3).

## 3A. 1:30 PM MISSION: start the automation and prove it works (owner, Nov 3: "the start at 1:30pm should be to start automation on this account and check to see if everything works")
Write every result into `Research Notes/Automation Check.md` as a table (check, result PASS/FAIL, evidence, fix) and a STATUS line in the Daily Log. Do these in order, then continue with section 3:
1. **Local:** `python Tools/preflight.py`; the four tasks exist and last ran (`Get-ScheduledTask MetaSports* | Get-ScheduledTaskInfo`): `MetaSports analytics` LastRunTime Nov 4 3:20 AM and a commit "Daily analytics pull" in `git log`; `MetaSports schedule ready AM` ran 6:30 AM (`Research Notes/Schedule Ready Last Run.txt`, `Schedule Ready Log.md`).
2. **Cloud routines, morning runs:** with RemoteTrigger (`select:RemoteTrigger` via ToolSearch) `get` both triggers (enabled true, next_run_at tomorrow), `list_runs`, `get_run_log` of the 3:17 and 4:23 AM sessions: repo cloned, preflight line, keys present, Short built or script-only, push succeeded, STATUS line in the Daily Log.
3. **Start it now:** if a morning run failed or skipped only for a fixable reason (keys now present, repo attached), fire `RemoteTrigger run` for the NBA trigger, then the FC trigger (one at a time; wait for the first to finish; they spend the cloud account's credits, so run each at most once today and log the session ids). If the keys are still missing, do NOT fire; tell the owner exactly what to paste.
4. **End-to-end proof of one Short:** after a cloud run finishes, confirm: pushed commit with a new Short folder, `qa_short` PASS line in its UPLOAD.md or notes, `Experiments.csv` row added (`python Tools/learn.py all`), Hub card (if the run had Hub access), and `python Tools/schedule_ready.py` (dry run) lists it or explains why not (two DRAFT files, slot, HOLD).
5. **Scheduler proof:** run `python Tools/yt_schedule.py` in its dry run on one eligible DRAFT (no `--go`) and confirm it parses title, tags and slot; confirm `Research Notes/Scheduled Uploads.csv` has no duplicates for the same sha.
6. **Account 2 branch / shared editing:** `git fetch origin` and confirm both branches and the cloud commits are visible; confirm a `CLAIM` line round-trips in `STATE.md`.
7. **Write the verdict:** `AUTOMATION CHECK: PASS` or a numbered list of what is broken, owner-only items first. Then start the loop (section 4).

## 3. 1:30 PM start-up list (in order; commit small; write a STATUS line after each step)
1. `cd /c/Users/Admin/Documents/metasports-shorts && git restore "Research Notes/Watch Reports/index.csv" 2>/dev/null; git pull --no-rebase origin main-329h3w`. Read the tail of
   `Research Notes/Daily Log.md`, `STATE.md`, `USAGE.txt`. The weekly reset was 1 PM ET, so usage should be near 0%; ceiling for runs is 99% (owner). A terminal cannot read `/usage`; if
   `USAGE.txt` was not updated after Nov 3, assume under 20% and write that assumption.
2. `python Tools/preflight.py` (writes `Preflight.md`). Fix any BLOCKER first: dead token (tell the owner to run `python Tools/yt_auth.py --channel nba|fc`); low voice credit (log it);
   disk under 5 GB (list the largest finished Shorts' `src/` and `clips/`, delete only exact folders the owner approved).
3. **Did the cloud run this morning?** Use the RemoteTrigger tool (ToolSearch "select:RemoteTrigger"): `list_runs` for both trigger ids, then `get_run_log` for the newest session of each.
   Look for: repo cloned, keys present, a Short built or "script only", pushed to `main-329h3w` (`git log origin/main-329h3w --since=yesterday`), no 403 on push, STATUS lines in the Daily Log.
   If the cloud had no keys or could not push, write exactly what failed in `STATE.md` and tell the owner what to fix. Set `BUILDER.txt` to `pc` ONLY if you will build today yourself (say so in `STATE.md`).
4. `python Tools/learn.py all --fetch`; commit `Experiments.csv` and `Learned Weights.md`.
5. `python Tools/schedule_ready.py` (dry run). Do NOT run `--go` yourself unless section 7 allows. The AM/PM timers run `--go` on their own, so make sure no unwanted DRAFT is eligible:
   a card containing `HOLD` is skipped; add `HOLD` to any card that failed QA or a fact check.
6. **Merge Account 2:** `git fetch origin account2 && git merge --no-edit origin/account2` (skip if the branch is missing), read `Research Notes/Account 2/Queue.md`; put a `built` Short on the Hub and
   task list per `daily-run` setup step 5 (the Hub asset store is 1 GB and was full on Oct 15; check before uploading; delete only exact ids the owner approved).
7. **PC requests:** read `Research Notes/PC Requests.md`. For each open line download the clip with `yt-dlp` into that Short's `src/`, cut with `Tools/broll.py`, mark the line DONE. Files over 20 MB are not
   pushed: commit only the small cut clip, or say where the source is.
8. S29 hygiene: its DRAFT mp4s are 97 MB each and need a re-encode under 20 MB before the Hub (`ffmpeg -i in.mp4 -c:v libx264 -crf 28 -b:a 96k out.mp4`, then `qa_short`).
   S29 is built (QA PASS), slot Sat Nov 7 12:00 PM ET, A/B arm not chosen (two DRAFTs, so the scheduler skips it).

## 4. The loop after the start-up list (until usage 99% or a hard limit; always write a STATUS line)
- Hourly: pull, `preflight --quiet`, read new Daily Log lines from the cloud, fix breakage (section 8).
- Zero-credit work from `Research Notes/Improvement Backlog.md`, top first.
- If the cloud failed twice in a row: set `BUILDER.txt` to `pc`, write why in `STATE.md`, and run `powershell -File Tools\run_daily.ps1 nba` then `fc` (preflight, builder guard, lock).
- Sunday: the weekly review (`AUTOMATION TO-DO (Nov 3).md` item 16): read `Learned Weights.md`, retire rules the data contradicts, one line in `Research Notes/Lessons Learned (running log).md`.

## 5. If you must build a Short on the PC (cloud failed)
Follow `CLOUD DAILY RULES.md` plus: voice with `python Tools/voice_take.py --script <script> --takes 3 -- --speed 1.15` (1.2 gave 48.9 s on a 192-word script and 1.1 gave 58.5 s; the story profile needs
50-59.9 s; `retake_sentence.py --folder F --at <sec>` repairs one failed word for about 25 characters). YouTube footage is allowed on the PC
(`yt-dlp -f "bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720]"`). Then `fill_len.py . 0.15` (the 0.15 s pad prevents a 0.28 s picture/sound gap), `cut_list.py --force` and `--verified` after LOOKING at
`_check/sheet.jpg`, `assemble.py --engine ffmpeg --caption-style ahmed [--no-music]`, `qa_short.py --full`. Avoid the last 5 s of FIFA highlight uploads (a green end card gives a flat-frame FIX).
S29 is the worked example: `Soccer Channel/Productions/2026-11-07 S29 The Goalkeeper Who Says Spain Were Scared Of A Shootout/`.

## 6. Owner-only items still open (list once per day in `STATE.md`; never nag in a loop)
1. Confirm the cloud keys are in the environment; "Publish app" on the Google OAuth consent screen (upload tokens made Nov 1 die about Nov 8 otherwise; preflight shows REJECTED when it happens).
2. Choose the A/B arm per Short (two DRAFT files means the scheduler skips). Suggested default: no-music.
3. Monday: the two YouTube Studio exports (Shorts tab) for "Stayed to watch" into `Research Notes/Studio exports/`.
4. Pin the comment in the YouTube app after each goes live (the API cannot).
5. `chmod 600 /c/Users/Admin/.config/watch/.env` (hook warning every session).
6. Free disk on C: (27 GB free of 931 GB). The owner decides what goes; list candidates in `STATE.md`.
7. Decide cloud vs PC permanently after two clean weeks, and option B to C (section 7).

## 7. How full automation ramps (do not skip steps)
- **Now (option B-with-timers):** the cloud builds drafts; the owner can approve on the Hub; the PC timers run `schedule_ready.py --go`, which schedules ANY eligible DRAFT privately with `publishAt`
  (passing QA line, UPLOAD.md, parsable slot at least 2 h away, exactly one DRAFT file, no `HOLD`). The owner can delete it in the YouTube app before it goes public. That is option C-lite: watch the
  scheduled list every day; if a bad file slips through, tell the owner the same day and tighten the rule (add a fact-check line requirement, or require `approved: true` on the Hub card).
- **After two clean weeks** (no QA miss, no fact correction, no copyright claim): option C, autopilot with a 12-24 h veto window.
- **Never** option D (post within hours of news with no check).

## 8. Failure playbook
| Symptom | Fix |
|---|---|
| Cloud push 403 | repo not attached to the environment: owner action; log in `STATE.md` |
| "no voice key" in a cloud log | keys not in the environment: owner reruns `Tools/copy_cloud_env.ps1` and pastes |
| Voice check REDO on one word | `retake_sentence.py --folder F --at <sec>` |
| QA flat green frame at a cut | footage hit an end card; move `at` earlier |
| QA picture and sound differ | `fill_len.py . 0.15`, then `cut_list.py --force` |
| QA same footage twice | change `at` to a different play; a replay needs `"replay": true` |
| `schedule_ready` REFUSED | read the line: slot under 20 min, or file already scheduled (never re-upload) |
| Token REJECTED | `python Tools/yt_auth.py --channel nba|fc`; the owner clicks Allow |
| Push fails (big file) | `git reset --mixed HEAD~1`, unstage the mp4, keep it local |
| Two accounts edit one folder | the `CLAIM` line in `STATE.md` decides; the later one yields |

## 9. Numbers to remember
ElevenLabs 69,040 characters left of 121,224 (resets Nov 18); a Short uses 1.2K-4K. NBA median about 6.7K views (n=27); FC median about 2.8K (n=10); FC goalkeeper/story lane 5.4x (n=3, a guess).
Hook: line 1 of 12+ words engaged 0.490 vs 0.557 under 12 (n=21). Judge a Short only after 72 h. n under 5 is a guess.
