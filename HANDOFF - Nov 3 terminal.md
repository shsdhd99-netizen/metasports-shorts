# Handoff, Tue Nov 3 2026 (desktop session -> owner's Claude terminal)

Branch `main-329h3w`. First: `git pull --no-rebase origin main-329h3w`. Then read `AUTOMATION TO-DO (Nov 3).md` (the plan) and this file.
Rules unchanged: never publish, schedule outside `yt_schedule.py`'s guard rails, or open YouTube Studio; never print/commit keys;
Shorts under 59.5 s; no promo ending. Commit small and often; commits end with the Co-Authored-By line used in this repo's history.

## Owner's instruction (Nov 3)
Finish the automation to-do list autonomously in the terminal and use usage up to **99% weekly** (the 50% ceiling in `C:\Users\Admin\AGENTS.md`
is raised for this run only). Weekly was 96% at 4 PM ET and resets **Wed Nov 4, 1 PM ET**; the 5-hour window is separate.

## Order of work (stop at the first hard limit; everything is committed as you go)
1. **Zero-credit PC items first** (to-do items 5, 6, 7): Task Scheduler entries for `Tools/daily_analytics.bat` (7 PM daily) and a
   ready-draft scheduler wrapper around `Tools/yt_schedule.py`; a usage-guard note in `.claude/skills/daily-run/SKILL.md`
   (weekly over 90%: write one "skipped, low usage" line, do zero-credit steps only).
2. **Learning loop** (item 8): `Research Notes/Experiments.csv` + `Tools/learn.py` -> `Research Notes/Learned Weights.md`, backfilled
   from `Research Notes/Posted Tracker*.csv`, `Outcome Log.md`, `Research Notes/Watch Reports/*.json`. Show n on every row; n<5 = guess.
3. **Hook rule** (item 10), **soccer research finish** (item 9), **editing fixes as opt-in `assemble.py` features** (item 11).
4. Then daily-run reads `Learned Weights.md` (item 15: 70/30 rule, pause a lane after 3 flops).
Not for the terminal: items 1-4 (owner), 13 (account 1 after the reset), 16 (Sunday review).

## Owner-run before starting
- `chmod 600 /c/Users/Admin/.config/watch/.env` (the /watch hook warned the file is world-readable).
- Terminal sessions can't read usage automatically: use `/usage` in the terminal (or the status line) after each chunk of work.

## Left untracked on purpose
Production `clips/`, `voice_raw.mp3`, `_voice_*` folders and `.url` files under `Productions/` are working files; do not commit them.
