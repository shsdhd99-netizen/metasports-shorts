# Handoff for the next terminal session (written Tue Nov 3, 2026, 4:40 PM ET; resume Wed Nov 4, 1:30 PM ET)

Branch `main-329h3w`. First: `git pull --no-rebase origin main-329h3w`. Rules unchanged from `HANDOFF - Nov 3 terminal.md`: never publish,
never schedule outside `yt_schedule.py`'s guard rails, never open YouTube Studio, never print or commit keys, Shorts under 59.5 s, no promo
ending, never delete and re-upload a Short, at most 2 posts a day per channel 6+ hours apart. Commits end with
the Co-Authored-By line for the model actually running (the session states it; do not copy a fixed model name). Do not commit untracked `clips/`, `voice_raw.mp3`, `_voice_*`, `src/`, `.url`.

## 1. What is DONE (all committed and pushed; last commit `64ca199`)
| Item | Result | Where |
|---|---|---|
| 6 Ready-draft scheduler | `Tools/schedule_ready.py` (dry run by default, `--go` uploads) + `Tools/schedule_ready.bat` | NOT on a timer yet (see section 3) |
| 7 Usage guard | daily-run section 0a: weekly over 90% means one "skipped, low usage" line and zero-credit steps only | `.claude/skills/daily-run/SKILL.md` |
| 8 Learning loop | `Tools/learn.py` -> `Research Notes/Experiments.csv` (160 rows), `Research Notes/Learned Weights.md` | `python Tools/learn.py all --fetch` (public views via yt-dlp, no login) |
| 9 Soccer research | already finished by an earlier session; FC Playbook v2 is goalkeeper-first; `story-short` skill now has a Topic rule block | `Soccer Channel/Playbook.md` |
| 10 Hook rule | line 1 of 12+ words engaged 0.490 (n=6) vs 0.557 under 12 (n=15); `script_lint.py` flags it; Playbook rule 3 annotated | |
| 11 Editing fixes | `Tools/edit_upgrade.py` (opt-in: wide hook zoom, scorebug whole, no shot over 3 s) + DEMO re-cut of #73, `qa_short --full` PASS, `edit_lint` clean | `Productions/MetaSports/2026-11-03 DEMO - editing upgrade 73` |
| 15 70/30 + pause rule | daily-run reads `Learned Weights.md` before picking a topic | `.claude/skills/daily-run/SKILL.md` section C |

## 2. What to do at 1:30 PM Wed (the weekly reset is 1 PM ET; check `/usage` first)
Order. Stop and write a `STATUS:` line in `Research Notes/Daily Log.md` at weekly 99% or any hard limit.
1. `git pull --no-rebase origin main-329h3w`; `git restore "Research Notes/Watch Reports/index.csv"` if modified. Read the newest `STATUS:` lines in
   `Research Notes/Daily Log.md` and `Research Notes/Automation Options (Nov 3, 2026).md` (one builder only).
2. Zero credit: `python Tools/learn.py all --fetch` (refresh weights; commit `Experiments.csv` and `Learned Weights.md`), then
   `python Tools/schedule_ready.py` (dry run). Read what it lists; run with `--go` only for folders the owner has not held (a card with `HOLD` is skipped).
3. Item 13: `git fetch origin account2 && git merge --no-edit origin/account2` (skip if the branch is missing), read `Research Notes/Account 2/Queue.md`,
   put any `built` Short on the Hub and task list per the daily-run setup step 5.
4. Item 14: revise S20 (Messi napkin: drop the auction price, end on the napkin; it has a voice and a 31-shot plan but is not rendered), S09 (held:
   open on the odd act "moved two bottles", cut the $4B and $242B), S19 (Rulli, unvoiced) against FC Playbook v2. Voice only if `python Tools/voiceover.py --check` shows credit.
5. NBA and FC daily runs under the weights (daily-run skill). Done when a Short builds with no 403 and no manual rescue.
6. Item 12 (pre-build 6 Shorts, 3 per channel, drafts) only if usage allows after the daily runs.
7. Sunday only (item 16): the weekly review.

## 3. What I need from the owner (in priority order)
1. **Register the scheduler timer** (the classifier blocked me; it is a persistent task that uploads private, scheduled videos). Type in the prompt:
   `! schtasks /create /sc daily /st 06:30 /tn "MetaSports schedule ready AM" /tr "C:\Users\Admin\Documents\metasports-shorts\Tools\schedule_ready.bat" /f`
   and the same with `/st 18:30` and `PM`. Verify with `Get-ScheduledTask *MetaSports*`.
2. **Register the 1:30 PM resume** (same reason, I cannot create persistent tasks): 
   `! schtasks /create /sc once /sd 11/04/2026 /st 13:30 /tn "MetaSports terminal resume" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\Admin\Documents\metasports-shorts\Tools\resume_terminal.ps1" /f`
   The script starts a fresh `claude -p` session on this repo with the prompt "read HANDOFF - Nov 4 resume 1-30 PM.md and carry it out". It uses
   `--permission-mode acceptEdits`, so the first python/git/ffmpeg prompts must already be "always allowed" (or add allow rules in `.claude/settings.local.json`).
   The PC must be awake (task "ClaudeDesktopStayAwake" exists).
3. **Say which builder is the only one**: cloud or this PC. Both building is the main duplicate risk. Until you say, I only build what is not in the Daily Log.
4. **Cloud environment keys** (ELEVENLABS_API_KEY, GEMINI_API_KEY, YT_* tokens) so cloud builds stop skipping; **Publish app** on the Google OAuth consent
   screen or upload tokens die after 7 days (they were made Nov 1, so about Nov 8).
5. **Usage number**: this session cannot read `/usage`. Tell me the weekly % at the start of each session.
6. **Monday exports**: the two Studio exports (Shorts tab) for "Stayed to watch". No API for it.
7. `chmod 600 /c/Users/Admin/.config/watch/.env` (the /watch hook warns every session).

## 4. What can improve (my honest list)
- **The data is too thin to steer yet.** Only 27 NBA and 10 FC Shorts are mature with a lane or views since Oct 14; most rows have no `lane`. Every run must fill `lane`
  (and `fresh`, `music`) in `Experiments.csv` at build time, or `learn.py` stays a guess machine. The first real finding needs about 5 Shorts per lane.
- **Views are public counts, not retention.** Engaged ratio exists for only about 45 Shorts and `learn.py` does not use it yet. Next step: add `engaged_ratio` as a second
  outcome column in the report (the hook study showed it can separate openings when views cannot), and a 72-hour stamp so a Short is judged once, at day 3.
- **Hook rule is one measure.** "Withhold the result in line 1" looks like the difference (#75 0.615 vs #76/Barkley/SGA) but n is too small. Run ONE test: next two
  fresh stories, one tension-first and one result-first, same lane, same length.
- **Editing upgrade tradeoff.** Whole-frame shots keep the scorebug but make the player small (see the DEMO contact sheet). The better fix is a closer second angle,
  which needs another source. Caption position off the players (captions.py) and the escalating counter are still not built.
- **`schedule_ready.py` limits.** It skips a folder with two DRAFT files (music vs no music), so it will not schedule A/B pairs. Decide a rule (for example the
  `no music` arm unless the card names the arm) and add it; today those need a human. Card slots are parsed from free text, so a typo means a silent skip: the
  log lists skips only on dry runs. A `--go` run writes one line to `Research Notes/Schedule Ready Log.md`.
- **Account-switch safety.** All state is in the repo, which is good. Missing: a single `STATE.md` that the daily run updates (last slot used per channel, builder in charge,
  weekly % last seen) so a different account does not have to read three logs.
- **Duplicate-builder guard.** There is no lock. A plain file `Research Notes/BUILDER.txt` ("cloud" or "pc", set by the owner) that both daily runs read first would remove the risk.
- **Usage guard has no number.** It trusts a human-supplied %. A tiny `Research Notes/USAGE.txt` the owner updates (or that the desktop app writes) would let a headless run obey it.
- **Cost of a failed morning.** Nov 3 builds were skipped for a lost voice key. The usage guard and a "no key" skip both exist now; add the key check to the top of the PC resume script
  (`python Tools/voiceover.py --check`) so it fails in 5 seconds instead of mid-build.

## 5. Files to read first
`HANDOFF - Nov 3 terminal.md` (rules, setup, owner items), `AUTOMATION TO-DO (Nov 3).md` (plan), `Research Notes/Learned Weights.md` (what the data says),
`Research Notes/Automation Options (Nov 3, 2026).md` (builder choice), `.claude/skills/daily-run/SKILL.md` (the run), `Research Notes/Daily Log.md` (tail: STATUS lines).
