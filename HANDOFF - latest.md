# Handoff (auto), Sat Nov 07 2026, 15:36 UTC, written by account: app account 1 (cloud)

Read this first, then `Research Notes/Daily Log.md` (newest entries) before building anything, so two sessions never build the same Short.

## Note from the last session
Efficiency pass done: build.py, pre-voice gate, shared anchors, espn_clip, tool_check, quieter footage QA. Next: builders use build.py; S38/S43 need UPLOAD.md + voice on the PC.

## Team board (who is doing what; full board: `TEAM BOARD.md`, protocol: `TEAM HANDOFF.md`)
| Account | Role | Now | Next | Done today | Unread | Updated |
|---|---|---|---|---|---|---|
| **A1** | Builder | - | next: watch the 7:30 results | 2 | 11 | Sat Nov 7, 7:31 AM ET |
| **A2** | Builder (backup) | - | - | 0 | 9 | never |
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
- NETLIFY_AUTH_TOKEN: MISSING
- HEYGEN_API_KEY: MISSING

## Newest STATUS lines (Daily Log)
- STATUS: PC account 1 NBA gap-fill, Nov 5: filled Fri Nov 6 3:30 PM ET by scheduling the already-built #95 (Lendeborg peer pressure; QA PASS re-run, private + publishAt via schedule_ready). No new build, no credits spent.
- STATUS: built and ran. Scoring: `lab.py predict` (shrunk feature effects, 0-100, leave-one-out backtest: NBA rho 0.29, FC too few). QA: qa_final now runs qa_short on the DRAFT (was silently skipped: no final.mp4 anywhere), plus never-twice, slot clash, stale wording, arm match, prediction and a QA score; `qa_sweep.py` (QA Board: 1 SHIP, 5 HOLD; all 11 scheduled uploads match YouTube). Auto queue: `queue_rank.py` v2 plans 7 days (Sun 7:15 AM NBA is EMPTY: nothing NBA is prepped; FC Mon has S38 + S43 to build by Sun 4 PM / 10 PM). Hubs: `hub_sync.py` applied 79 writes (results refreshed, Lendeborg marked posted, 12 missing posted cards added, UP NEXT cards). Roadmap: `roadmap.py` LIVE STATUS (NBA 650 subs, 1K ~Jan 17; FC 183, 500 ~Jan 5). Marked #93, #96, #97 `**Queue:** no`. Guide: `Research Notes/Tools, Scoring and QA (Nov 7, 2026).md`. Stats routine prompt now runs lab, QA sweep, queue, Hub sync and roadmap daily.
- STATUS: owner approved all of the Theory Ranking. Rules rewritten (Playbook THE RULES Nov 7, Soccer Playbook v3; old text archived), QA fixed (tags and pinned comment never FAIL; 35%/cut-count/shot-length/b-roll lints removed; NBA length warn 18-27 s; payoff-held warn), and the lab built: `Tools/lab.py` measures 84 Shorts, scores 6 live tests (3 per channel) daily, studies any part (`--part edit` etc.) and re-checks every rule. First Rule check: line 1 <=11 words, NBA family lane and NBA <=25 s SUPPORTED; pace >230 wpm overruled (not a rule); NBA morning posts flagged REVISIT. Prompts of the NBA build, FC build and stats routines updated. Record: `Research Notes/Rule Changes Applied (Nov 7, 2026).md`.
- STATUS: blocked, no build. Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). `next_gap.py fc`: NO GAP in 54 h. The skill's "no gap: prep the next two ideas" is already met (S21, S22, S36 scripted past the scheduled S31/S32/S30), so nothing new written. No credits spent.
- STATUS: blocked, no build (3rd day). Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment); no credits spent. Next NBA gap: Sat Nov 7 3:30 PM ET, in range of the PC gap-fill (6:45 AM ET).

## Last 15 commits (any account)
- Nov 07 15:36 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 15:35 Efficiency pass: build.py, pre-voice gate, shared anchors, ESPN clips, tool check
- Nov 07 15:11 Handoff (auto) from app account 1 (cloud)
- Nov 07 15:11 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 15:11 Scoring, QA, auto queue, Hub sync and roadmap (Nov 7, owner request)
- Nov 07 14:50 Handoff (auto) from app account 1 (cloud)
- Nov 07 14:50 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 14:50 Rules rewrite + the lab (owner approved all, Nov 7): R1-R15 applied, scrapped lints removed, Tools/lab.py auto-assigns, logs and scores tests and studies every part
- Nov 07 14:29 [CLOUD Research + scheduled runs] team: message to ALL
- Nov 07 14:29 Theory ranking + rules challenge (Nov 7): all research notes ranked add/test/scrap, every video part ranked, 15 rule fixes proposed; fresh API pulls
- Nov 07 09:00 Automation check (script)
- Nov 07 07:31 FC gap Mon Nov 9 12:00: skipped, S21 gauge 36%
- Nov 07 07:31 Handoff (auto) from PC account 1
- Nov 07 07:31 [A1 Builder] team: done: FC Mon Nov 9 12:00 S21 Higuita build
- Nov 07 07:31 [A1 Builder] team: claim: FC Mon Nov 9 12:00 S21 Higuita build

## Uncommitted here
     M "HANDOFF - latest.md"
