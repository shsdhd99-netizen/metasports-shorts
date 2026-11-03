# Everything, one page (Tue Nov 3, 2026, 10 PM ET)
## Owner: three things, about 5 minutes
1. `! powershell -ExecutionPolicy Bypass -File Tools\copy_cloud_env.ps1`, then paste the 9 variables into the cloud environment `env_016GURtEd17FS3mEXiKSjfM6` settings (claude.ai > Claude Code > environment variables). Without it the cloud only writes scripts.
2. `! powershell -ExecutionPolicy Bypass -File Tools\register_tasks.ps1` (schedule-ready 6:30 AM and 6:30 PM, and the Wed 1:30 PM resume). Claude's auto mode blocks creating persistent tasks, even with your OK.
3. "Publish app" on the Google OAuth consent screen (or the upload tokens die about Nov 8). Optional: ask Claude to do it in Chrome with you signed in.
## State
Builder = cloud (`Research Notes/BUILDER.txt`). Routines enabled: NBA 3:17 AM ET `trig_01PUCBRzwuJ1j1r3Y53GdfoY`, FC 4:23 AM ET `trig_011nY5arZZHcgKkWQvcBkNKc`, both read `CLOUD DAILY RULES.md`. Usage: weekly about 2% used (`USAGE.txt`); resets Wed 1 PM ET. Preflight OK (`python Tools/preflight.py`).
## Built today
Scheduler wrapper (`schedule_ready.py`), usage + builder guards, learning loop (`learn.py`, `Experiments.csv`, `Learned Weights.md`), hook rule + lint, story-short topic rule, `edit_upgrade.py` + #73 DEMO (QA PASS), S29 FC Short (QA PASS, local DRAFTs), `preflight.py`, `run_daily.ps1`, cloud rules, PC request queue, Account 1 handoff.
## Where to read
`HANDOFF - Account 1 (Nov 3 night).md` (account switch), `HANDOFF - Nov 4 resume 1-30 PM.md` (tomorrow + improvement list), `CLOUD DAILY RULES.md`, `Research Notes/STATE.md`, `Research Notes/Preflight.md`, `Research Notes/Learned Weights.md`, `Research Notes/Daily Log.md` (tail).
## Known limits
Disk 27 GB free on C:. S29 DRAFT mp4s are 97 MB (local only; Hub needs under 20 MB). `schedule_ready.py` skips folders with two DRAFT files (A/B arm is your call). Data is thin: fill `lane` in `Experiments.csv` every build.
