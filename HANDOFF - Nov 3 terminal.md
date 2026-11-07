# Handoff, Tue Nov 3 2026 (desktop session -> owner's Claude terminal)

Branch `main-329h3w`. First: `git pull --no-rebase origin main-329h3w`. Then read `AUTOMATION TO-DO (Nov 3).md` (the plan) and this file.
Rules unchanged: never publish, schedule outside `yt_schedule.py`'s guard rails, or open YouTube Studio; never print/commit keys;
Shorts under 59.5 s; no promo ending. Commit small and often; commits end with the Co-Authored-By line used in this repo's history.

## Owner's instruction (Nov 3)
Finish the automation to-do list autonomously in the terminal and use usage up to **99% weekly** (the 50% ceiling in `C:\Users\Admin\AGENTS.md`
is raised for this run only). Weekly was 96% at 4 PM ET and resets **Wed Nov 4, 1 PM ET**; the 5-hour window is separate.

## Read first (corrections)
The to-do file's correction note applies: the cloud runs did continue (Nov 2 median 16,250, up); Nov 3 builds were skipped only because the
cloud lost its voice key. The PC has `Tools/.env`, so build and voice here. **One builder only:** read `Research Notes/Automation Options
(Nov 3, 2026).md` and check the newest `STATUS:` lines in the Daily Log before building a Short, so the terminal and the cloud don't both build.

## Order of work (stop at the first hard limit; everything is committed as you go)
1. **Zero-credit PC items first** (to-do items 6, 7; item 5 is already done): a ready-draft scheduler wrapper around
   `Tools/yt_schedule.py` (Task Scheduler entry, same guard rails); a usage-guard note in `.claude/skills/daily-run/SKILL.md`
   (weekly over 90%: write one "skipped, low usage" line, do zero-credit steps only).
2. **Learning loop** (item 8): `Research Notes/Experiments.csv` + `Tools/learn.py` -> `Research Notes/Learned Weights.md`, backfilled
   from `Research Notes/Posted Tracker*.csv`, `Outcome Log.md`, `Research Notes/Watch Reports/*.json`. Show n on every row; n<5 = guess.
3. **Hook rule** (item 10), **soccer research finish** (item 9), **editing fixes as opt-in `assemble.py` features** (item 11).
4. Then daily-run reads `Learned Weights.md` (item 15: 70/30 rule, pause a lane after 3 flops).
Not for the terminal: items 1-4 (owner), 13 (account 1 after the reset), 16 (Sunday review).

## Terminal setup (checked on the PC, Nov 3 5 PM ET)
Already installed and working: Claude Code 2.1.316, git 2.55, Python 3.12.10, ffmpeg 8.1, yt-dlp 2026.08.19, node 24, gh 2.96.
`Tools/.env` already holds the keys (ELEVENLABS_API_KEY/VOICE_ID, GEMINI_API_KEY, YT_CLIENT_ID/SECRET, YT_REFRESH_TOKEN(_FC),
YT_UPLOAD_TOKEN(_FC)); never print it. The Windows task "MetaSports analytics" already runs `Tools\daily_analytics.bat` daily at 3:20 AM
(to-do item 5 is DONE). "ClaudeUsageKillSwitch" is a past one-time task (no next run), not active.

**Shortcut (Nov 3):** pasting multi-word commands into Git Bash garbled them (`^[[200~` bracketed-paste characters, branch `main-329h3w~`).
Type this instead of steps 2-5: `bash Tools/terminal_start.sh` (after `cd /c/Users/Admin/Documents/metasports-shorts`). To fix pasting:
`bind 'set enable-bracketed-paste off'`. Pasting the prompt into `claude` itself is fine.

1. Open **Git Bash** (or Windows Terminal with a Git Bash tab). The repo scripts are bash and Python.
2. `cd /c/Users/Admin/Documents/metasports-shorts`
3. `git status -sb`. If `Research Notes/Watch Reports/index.csv` shows modified, run `git restore "Research Notes/Watch Reports/index.csv"`
   (it is regenerated). Then `git pull --no-rebase origin main-329h3w`. Do not commit the untracked `clips/`, `voice_raw.mp3`, `_voice_*`.
4. `chmod 600 /c/Users/Admin/.config/watch/.env` (the /watch hook warns the file is world-readable).
5. Key check, prints no secrets: `python Tools/voiceover.py --check` (shows characters used of the plan) and `bash Tools/cloud_setup.sh`
   (should say `gemini: set`; `key: MISSING` is expected here because the key lives in `Tools/.env`, not the shell).
6. Keep the PC awake: the "ClaudeDesktopStayAwake" task exists. For a long run also run once in an admin PowerShell:
   `powercfg /change standby-timeout-ac 0` (undo later with the old value; it changes a system setting, so it is the owner's call).
7. Start: `claude --permission-mode acceptEdits`. The first time it asks to run python, git, ffmpeg or yt-dlp, choose "always allow"
   so an unattended run doesn't stall on prompts. `--dangerously-skip-permissions` would also work but removes the guard rails; the
   upload tokens are in `Tools/.env`, so the owner decides that, not the agent.
8. Paste: *Read "HANDOFF - Nov 3 terminal.md" and "AUTOMATION TO-DO (Nov 3).md" and carry out the handoff autonomously, in its order. Commit small after each item. Check `/usage` after each item and stop, writing a STATUS line, when weekly reaches 99% or a limit hits.*
9. Usage: terminals can't read it automatically. `/usage` shows it. Weekly resets Wed Nov 4, 1 PM ET. After a 5-hour limit,
   `claude --continue` resumes the same session.
10. One builder: before building a Short, read the newest `STATUS:` lines in `Research Notes/Daily Log.md` and
    `Research Notes/Automation Options (Nov 3, 2026).md`. Do not build what the cloud run already built.
11. Finish: `git pull --no-rebase` then `git push origin main-329h3w`, and append a STATUS line to `Research Notes/Daily Log.md`.

## Not-yet-done owner items (from the Automation Options note)
Cloud environment keys (ELEVENLABS_API_KEY, GEMINI_API_KEY, YT_* tokens) so the cloud builds stop skipping; "Publish app" on the Google
OAuth consent screen (or tokens die after 7 days); say option B or C in chat; pick ONE builder (cloud or PC) and pause the other's builds.

## Left untracked on purpose
Production `clips/`, `voice_raw.mp3`, `_voice_*` folders and `.url` files under `Productions/` are working files; do not commit them.
