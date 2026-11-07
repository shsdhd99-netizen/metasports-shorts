# Handoff (auto), Sat Nov 07 2026, 11:06 EST, written by account: PC account 2

Read this first, then `Research Notes/Daily Log.md` (newest entries) before building anything, so two sessions never build the same Short.

## Note from the last session
A2 was moved to the owner's private side project; no MetaSports build. #99 Luka (Sat 3:30 PM) still NOT scheduled: dry run OK, local qa_final HOLD only because cloud clips are missing on the PC; BUILDER told.

## Team board (who is doing what; full board: `TEAM BOARD.md`, protocol: `TEAM HANDOFF.md`)
| Account | Role | Now | Next | Done today | Unread | Updated |
|---|---|---|---|---|---|---|
| **A1** | Builder | - | next: watch the 7:30 results | 2 | 12 | Sat Nov 7, 7:31 AM ET |
| **A2** | Builder (backup) | owner's private side project (not MetaSports) | free for builds | 1 | 0 | Sat Nov 7, 11:05 AM ET |
| **A3** | Prep + Review | - | - | 0 | 9 | never |
| **CLOUD** | Research + scheduled runs | - | 3:43 AM ET research run | 1 | 0 | Sat Nov 7, 5:10 AM ET |

- nothing claimed

## Keys on this machine (presence only)
- ELEVENLABS_API_KEY: set
- GEMINI_API_KEY: set
- YT_CLIENT_ID: set
- YT_REFRESH_TOKEN: set
- YT_REFRESH_TOKEN_FC: set
- YT_UPLOAD_TOKEN: set
- YT_UPLOAD_TOKEN_FC: set
- NETLIFY_AUTH_TOKEN: set
- HEYGEN_API_KEY: MISSING

## Newest STATUS lines (Daily Log)
- STATUS: PC account 1 NBA gap-fill, Nov 5: filled Fri Nov 6 3:30 PM ET by scheduling the already-built #95 (Lendeborg peer pressure; QA PASS re-run, private + publishAt via schedule_ready). No new build, no credits spent.
- STATUS: built and ran. Scoring: `lab.py predict` (shrunk feature effects, 0-100, leave-one-out backtest: NBA rho 0.29, FC too few). QA: qa_final now runs qa_short on the DRAFT (was silently skipped: no final.mp4 anywhere), plus never-twice, slot clash, stale wording, arm match, prediction and a QA score; `qa_sweep.py` (QA Board: 1 SHIP, 5 HOLD; all 11 scheduled uploads match YouTube). Auto queue: `queue_rank.py` v2 plans 7 days (Sun 7:15 AM NBA is EMPTY: nothing NBA is prepped; FC Mon has S38 + S43 to build by Sun 4 PM / 10 PM). Hubs: `hub_sync.py` applied 79 writes (results refreshed, Lendeborg marked posted, 12 missing posted cards added, UP NEXT cards). Roadmap: `roadmap.py` LIVE STATUS (NBA 650 subs, 1K ~Jan 17; FC 183, 500 ~Jan 5). Marked #93, #96, #97 `**Queue:** no`. Guide: `Research Notes/Tools, Scoring and QA (Nov 7, 2026).md`. Stats routine prompt now runs lab, QA sweep, queue, Hub sync and roadmap daily.
- STATUS: owner approved all of the Theory Ranking. Rules rewritten (Playbook THE RULES Nov 7, Soccer Playbook v3; old text archived), QA fixed (tags and pinned comment never FAIL; 35%/cut-count/shot-length/b-roll lints removed; NBA length warn 18-27 s; payoff-held warn), and the lab built: `Tools/lab.py` measures 84 Shorts, scores 6 live tests (3 per channel) daily, studies any part (`--part edit` etc.) and re-checks every rule. First Rule check: line 1 <=11 words, NBA family lane and NBA <=25 s SUPPORTED; pace >230 wpm overruled (not a rule); NBA morning posts flagged REVISIT. Prompts of the NBA build, FC build and stats routines updated. Record: `Research Notes/Rule Changes Applied (Nov 7, 2026).md`.
- STATUS: blocked, no build. Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). `next_gap.py fc`: NO GAP in 54 h. The skill's "no gap: prep the next two ideas" is already met (S21, S22, S36 scripted past the scheduled S31/S32/S30), so nothing new written. No credits spent.
- STATUS: blocked, no build (3rd day). Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment); no credits spent. Next NBA gap: Sat Nov 7 3:30 PM ET, in range of the PC gap-fill (6:45 AM ET).

## Last 15 commits (any account)
- Nov 07 11:05 [A2 Builder (backup)] team: read 9 message(s)
- Nov 07 11:05 [A2 Builder (backup)] team: status: owner's private side project (not MetaSports)
- Nov 07 10:57 [A2 Builder (backup)] team: message to BUILDER
- Nov 07 10:57 [A2 Builder (backup)] team: done: #99 Luka schedule for Sat 3:30 PM
- Nov 07 10:56 [A2 Builder (backup)] team: claim: #99 Luka schedule for Sat 3:30 PM
- Nov 07 10:55 [A2 Builder (backup)] Handoff (auto) from PC account 2 (start)
- Nov 07 10:55 [A2 Builder (backup)] team: status: starting a session
- Nov 07 15:36 Handoff (auto) from app account 1 (cloud)
- Nov 07 15:36 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 15:35 Efficiency pass: build.py, pre-voice gate, shared anchors, ESPN clips, tool check
- Nov 07 15:11 Handoff (auto) from app account 1 (cloud)
- Nov 07 15:11 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 15:11 Scoring, QA, auto queue, Hub sync and roadmap (Nov 7, owner request)
- Nov 07 14:50 Handoff (auto) from app account 1 (cloud)
- Nov 07 14:50 [CLOUD Research + scheduled runs] team: message to ALL

## Uncommitted here
     M "HANDOFF - latest.md"
     M "Productions/MetaSports/2026-11-07 99 Luka Scored 53 For His Sixth 40 In Seven/qa_final.json"
     M "Research Notes/QA Final Log.csv"
    ?? "Productions/MetaSports/2026-10-29 77 Did Bronny Actually Get Better/qa_final.json"
    ?? "Productions/MetaSports/2026-10-29 78 Rodman Skipped A Finals Practice To Go Wrestling/qa_final.json"
    ?? "Productions/MetaSports/2026-10-31 80 The Warriors Flipped The Exact Same Score/DRAFT - awaiting approval - The Lakers Led By 23 And Lost By 17 (no music).mp4"
    ?? "Productions/MetaSports/2026-10-31 80 The Warriors Flipped The Exact Same Score/qa_final.json"
    ?? "Productions/MetaSports/2026-11-03 85 Jokic Only Wanted To Go Home/_voice_pretighten/"
    ?? "Productions/MetaSports/2026-11-03 85 Jokic Only Wanted To Go Home/_voice_prev/"
    ?? "Productions/MetaSports/2026-11-03 85 Jokic Only Wanted To Go Home/clips/"
    ?? "Productions/MetaSports/2026-11-03 85 Jokic Only Wanted To Go Home/voice_raw.mp3"
    ?? "Productions/MetaSports/2026-11-03 87 Draymond Triple Double With Four Points/_voice_pretighten/"
    ?? "Productions/MetaSports/2026-11-03 87 Draymond Triple Double With Four Points/clips/"
    ?? "Productions/MetaSports/2026-11-03 87 Draymond Triple Double With Four Points/voice_raw.mp3"
    ?? "Productions/MetaSports/2026-11-03 DEMO - editing upgrade 73/_render.json"
