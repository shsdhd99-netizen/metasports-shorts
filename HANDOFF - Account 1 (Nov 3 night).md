# Handoff for ACCOUNT 1 (written Tue Nov 3, 2026, 8:20 PM ET by the terminal session on Admin's PC)

Branch `main-329h3w`. First: `git pull --no-rebase origin main-329h3w`. Then run `python Tools/preflight.py` (zero credits, prints no secrets, writes `Research Notes/Preflight.md`).
Rules unchanged: never publish, never open YouTube Studio, schedule only through `Tools/yt_schedule.py` guard rails, no keys in chat or git, Shorts under 59.5 s, no promo ending,
never delete and re-upload, at most 2 posts a day per channel 6+ hours apart. Commits end with `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
Do not commit untracked `clips/`, `src/`, `voice_raw.mp3`, `_voice_*`, the 97 MB DRAFT mp4s (the push fails).

## 1. State right now
- **Builder:** `Research Notes/BUILDER.txt` = **`cloud`** (owner, Nov 3 night: "build in cloud so both accounts can edit"). Rules for cloud runs, both accounts: `CLOUD DAILY RULES.md`; split of work and the PC request queue: `Research Notes/BUILDER.md`, `Research Notes/PC Requests.md`. The two cloud routines (NBA 3:17 AM ET `trig_01PUCBRzwuJ1j1r3Y53GdfoY`, FC 4:23 AM ET `trig_011nY5arZZHcgKkWQvcBkNKc`, environment `env_016GURtEd17FS3mEXiKSjfM6`) were re-pointed to that file and ENABLED Nov 3 6:15 PM ET. They will write scripts only until the keys are in the cloud environment.
- **Usage:** `Research Notes/USAGE.txt` says weekly about 2% used (owner said 98% left, Nov 3 8:15 PM). The weekly reset is Wed Nov 4, 1 PM ET. Owner ceiling for these runs: 99%.
- **Preflight (8:15 PM):** OK with 6 warnings. ffmpeg, yt-dlp, git, node fine. ElevenLabs 69,040 characters left (resets Nov 18). All four YouTube refresh tokens work. **Disk: 27 GB free on C: (98% full)**; clean old `src/` and `clips/` of finished Shorts before big batches.
- **Scheduled tasks missing (the owner must register, the classifier blocks me):** `MetaSports schedule ready AM/PM` (lines in `Tools/schedule_ready.bat`), `MetaSports daily nba/fc` (see section 4), and the Wed 1:30 PM resume (`Tools/resume_terminal.ps1`, command in `HANDOFF - Nov 4 resume 1-30 PM.md`).

## 2. What got built today (all pushed, last pushed commit `3b59532`)
| Item | Where |
|---|---|
| Ready-draft scheduler (dry run by default) | `Tools/schedule_ready.py` + `.bat` |
| Usage guard + one-builder guard in daily-run | `.claude/skills/daily-run/SKILL.md` sections 0a, 0b |
| Learning loop: `Experiments.csv`, `Learned Weights.md` (n on every row, engaged ratio column) | `python Tools/learn.py all --fetch` |
| Hook rule re-tested (line 1 of 12+ words engaged 0.490 vs 0.557) + lint flag | Playbook rule 3, `script_lint.py` |
| story-short topic rule, daily-run 70/30 + pause-after-3-flops | skills |
| Opt-in editing upgrades + DEMO re-cut of #73 (QA PASS) | `Tools/edit_upgrade.py`, `Productions/MetaSports/2026-11-03 DEMO - editing upgrade 73` |
| **S29 FC built** (both versions QA PASS; local DRAFT mp4s, slot Sat Nov 7 12:00) | `Soccer Channel/Productions/2026-11-07 S29 .../`, `UPLOAD.md` has a known-gaps list |
| Preflight, STATE.md, BUILDER.txt, USAGE.txt | `Tools/preflight.py`, `Research Notes/` |

## 3. What Account 1 should do (order)
1. Pull, preflight, read the tail of `Research Notes/Daily Log.md` and `Research Notes/STATE.md`.
2. Zero credit: `python Tools/learn.py all --fetch` then commit `Experiments.csv` and `Learned Weights.md`; `python Tools/schedule_ready.py` (dry run).
3. After the 1 PM Wed reset (until then it is the old week): merge `account2` (`git fetch origin account2 && git merge --no-edit origin/account2`), read `Research Notes/Account 2/Queue.md`.
4. NBA and FC daily runs under the weights (daily-run skill). FC next scripts-only folders: S31 (baby Messi bathed; copy check TAKEN, owner's call), S32 (Hull fan; the 1998 table line needs a second source), S30. S25-S28 were already voiced by another run; S19/S20 are built.
5. Fill `lane`, `fresh`, `music` in `Experiments.csv` for every new Short at build time. This is what makes the learning loop work.
6. Item 12 (pre-build 6 Shorts as drafts) if credits allow; item 16 Sunday review.

## 4. Full-automation checklist (what is still missing)
1. **Owner:** register the 3-5 scheduled tasks above. For unattended daily runs add two more with the same pattern as `Tools/resume_terminal.ps1` (a script that does `claude -p "<daily-run prompt>" --permission-mode acceptEdits`), one per channel, 06:45 and 07:30 ET. They are written: `Tools/run_daily.ps1 nba|fc` (preflight, BUILDER guard, lock, then `claude -p`); the two `schtasks` lines are in its header.
2. **Owner:** pick ONE builder (cloud or PC); put cloud keys in the environment settings; **Publish app** on the Google OAuth consent screen (tokens made Nov 1 die about Nov 8 otherwise; preflight will catch it).
3. **Owner:** `chmod 600 /c/Users/Admin/.config/watch/.env`; weekly Monday Studio exports ("stayed to watch").
4. **Code gaps I know of:** `schedule_ready.py` cannot choose between a music and a no-music DRAFT (skips); no automatic re-encode under 20 MB for the Hub; no log rotation for `Research Notes/*Last Run.txt`; disk cleanup is manual.
5. **Safety before going autonomous:** run on option B (owner taps Approve) for two clean weeks, then C (autopilot with a veto window), per `Research Notes/Automation Options (Nov 3, 2026).md`.

## 5. Files to read first
`Research Notes/STATE.md`, `Research Notes/Preflight.md`, `Research Notes/Learned Weights.md`, `HANDOFF - Nov 4 resume 1-30 PM.md` (full improvement list), `HANDOFF - Nov 3 terminal.md`, `AUTOMATION TO-DO (Nov 3).md`, `.claude/skills/daily-run/SKILL.md`.

## 6. Added after this handoff (Nov 3, 10 PM ET)
- Cloud is the builder; routines enabled (above). **Owner must put the keys in the cloud environment settings:** run `powershell -File Tools\copy_cloud_env.ps1` (copies the 9 variables to the clipboard, prints names only, clears in 120 s) and paste into the environment variables. Without them the 3:17 and 4:23 AM runs only write scripts.
- Still owner-only: register the PC tasks (analytics already exists; schedule-ready AM/PM; the PC no longer needs daily nba/fc tasks while the cloud builds), "Publish app" on the Google OAuth consent screen, the Monday Studio exports, `chmod 600` on the watch .env.
