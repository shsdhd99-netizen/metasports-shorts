# Routines and skills map (Nov 6, 2026): every routine, every skill, who runs it, and whether it is healthy

Built from the Windows task list (checked live Nov 6: all 8 MetaSports tasks last result 0), `~/.claude/scheduled-tasks`, `CLAUDE.md`, the cloud status file `Team/status/CLOUD.md`, the repo and global skills, and the keyword counts in your own Claude prompt history (most used: research 32, to-do 22, upload 14, handoff 13, FC 11, post 9, voice 9, Hub 8, thumbnail 8, QA 7).

## 1. Automatic routines (nothing for you to do)
| Time ET | Routine | Runs on | Health Nov 6 | If it fails |
|---|---|---|---|---|
| 3:20 AM | `MetaSports analytics` (pull + push CSVs) | PC task | ok, but **wake-to-run is OFF**, so a sleeping PC misses it | needs the admin fix (`fix_task_wake.ps1`, to-do step) |
| 3:43 AM | Daily research (ideas, sources) | cloud (Account 1) | ok per CLOUD status | research files stop appearing in `Research Notes/Daily Research/` |
| 3:17 / 4:23 AM | NBA and FC cloud build routines | cloud | **blocked on YouTube keys** (the PC covers them) | PC gap-fill |
| 6:25 AM and PM | `MetaSports wake` (wakes the PC) | PC task | ok | everything after it is late |
| 6:30 AM and 6:30 PM | `schedule ready` (uploads QA-passed drafts as private + publishAt, commits) | PC task | ok | check `Schedule Ready Log.md` |
| 6:45 AM | `gapfill nba` (builds the 3:30 PM moment if the gate passes) | PC task, Account 1 | ok | the gap stays open (skipped) |
| 7:30 AM | `gapfill fc` | PC task | ok | same |
| 9:00 AM | `automation review` (writes `Automation Check.md`) | PC task | ok | no daily audit |
| 6:08 PM | Daily stats | cloud | ok per CLOUD status | stale numbers |
| any | `state.py` health page (titles, preflight, gaps, reminders) | on demand and from `schedule_ready.bat` | new | read the AUTO block of `STATE.md` |

## 2. Your personal routines (outside MetaSports; they must keep working)
| Routine | Where | What it needs | Status |
|---|---|---|---|
| `ai-reels-weekly-pipeline` (review new Instagram reels, update AI-Reels-KB) | Claude desktop scheduled task | **Claude in Chrome connected** and your logged-in Brave session | **at risk: the extension shows "no browsers connected"** until it is signed in as biggbknuts123@gmail.com |
| `scholarship-deadline-reminders` (daily ledger check, phone push) | Claude desktop scheduled task + artifact | the artifact and push notifications | not touched by the MetaSports work; keep the desktop app logged in |

## 3. Your manual routines (the autopilot reminds, it does not do these)
| When | Routine | Time | Where |
|---|---|---|---|
| Every Monday | Studio > Content > Shorts export for BOTH channels (the "stayed to watch" numbers) | 30 s each | save into `Research Notes/Studio exports/` |
| Daily | glance at `STATE.md` (Needs attention) and `TEAM BOARD.md` | 1 min | repo |
| After a Short goes live | pin the comment (the API cannot pin) | 1 min each | YouTube app |
| Sunday | Sunday review: top 3 and bottom 3, one rule kept, one dropped | 20 min | `Lessons Learned` |
| Dec 3 / Jan 31 | Dreamina cancel / accept YouTube terms | 2 min | `Reminders.csv` |

## 4. Skills, in the order a Short uses them (each is a real skill or tool in the repo)
| Step | Skill / tool | Used by |
|---|---|---|
| research | `daily-run` section C, `content-principles`, cloud research, `copy_check.py`, `idea_gauge.py`, `idea_triage.py`, `build_gate.py` | cloud + gap-fill |
| script | `nba-short` (NBA), `story-short` (FC), `script_lint.py` | builder |
| voice | `voiceover` -> `voice_take.py`, `tighten_voice.py` | builder |
| footage and cut | `cloud-short` (X, team sites, archive), `broll.py`, `cut_list.py`, `precut_lint.py` | builder |
| edit | `assemble` -> `assemble.py` (captions, SFX, loudness), `overlay.py` (counting numbers) | builder |
| cover | `thumbnail` -> `thumb.py --shape short` (one cover per Short) | builder |
| title and tags | `titles`, `tags_fit.py`, `UPLOAD.md` (title, empty description, tags to 490, pinned comment) | builder |
| QA | `qa_short.py --full`, `edit_lint.py`, `deflash.py`, `shot_strip.py`, then LOOK at frames | builder |
| upload | `yt_schedule.py` via `schedule_ready.py` (guards: no placeholder titles, no duplicate Short, QA line) | PC timers |
| Hub and Post task | `daily-run` section E (artifact cards + tasks) | builder with the right account |
| social | `crosspost.py` (TikTok/Instagram captions) | after each upload |
| learn | `learn.py`, `test_log.py`, `qa_audit.py` + `QA Changelog.md`, `Outcome Log.md` | daily |
| weekly | `channel-check` (public health check), `channel_totals.py` (monetization lines) | Monday |
| handoff | `handoff.sh`, `team.py status` | before every stop |
| client | `client-avatar-video`, `max_site_deploy.py` | Max only |

## 5. Sunday-night preflight (before the autopilot week)
`python Tools/preflight.py`; ElevenLabs characters (67K until the Nov 19 reset); disk above 8 GB; PC set to wake (admin fix); `python Tools/state.py` shows "Needs attention: nothing"; `python Tools/title_audit.py` clean; both old "unknown" videos deleted in Studio; Chrome extension connected (for the AI-reels routine).
