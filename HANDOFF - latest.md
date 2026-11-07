# Handoff (auto), Sat Nov 07 2026, 03:19 UTC, written by account: app account 1 (CLOUD)

Read this first, then `Research Notes/Daily Log.md` (newest entries) before building anything, so two sessions never build the same Short.

## Note from the last session
Read PC HANDOFF (Nov 7).md: Klay #98 for Sat 7:15 AM, S21 for Mon 12 PM, #79 Sun 7:15; queue_rank no longer offers live Shorts; A3 queue + background jobs listed.

## Team board (who is doing what; full board: `TEAM BOARD.md`, protocol: `TEAM HANDOFF.md`)
| Account | Role | Now | Next | Done today | Unread | Updated |
|---|---|---|---|---|---|---|
| **A1** | Builder | idle: #92 + S30 scheduled for 7:30 PM | next: watch the 7:30 results | 0 | 4 | Fri Nov 6, 1:28 PM ET |
| **A2** | Builder (backup) | - | - | 0 | 3 | never |
| **A3** | Prep + Review | - | - | 0 | 4 | never |
| **CLOUD** | Research + scheduled runs | PC handoff Nov 7 + TikTok review + queue_rank fix | 3:43 AM ET research run | 0 | 1 | Fri Nov 6, 10:19 PM ET |

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
- STATUS: blocked, no build. BUILDER.txt = `cloud`; voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). `next_gap.py fc`: NO GAP in 54 h. No credits spent.
- STATUS: blocked, no build. Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment), so no credits spent (CLOUD DAILY RULES step 4). Next NBA gap: Sat Nov 7 3:30 PM ET, in range of the PC gap-fill (6:45 AM ET). Same block as Nov 5: this routine's session needs the four YouTube secrets to ever build.
- STATUS: blocked, no build. BUILDER.txt = `cloud`; `cloud_setup.sh`: voice key set, Gemini set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). Rule 4: script/notes only, no credits. Also `next_gap.py fc`: NO GAP in the next 54 h (FC covered through Sun Nov 8 by S09/S29; S31, S32, S30, S21, S22, S36 already scripted for Nov 8-13), so no new script either. The Nov 4 run's notification reached this session only today (not run separately).
- STATUS: blocked, no build. `cloud_setup.sh`: voice key set, Gemini set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment). Per CLOUD DAILY RULES step 4: no credits spent. Next NBA gap (`next_gap.py`): Fri Nov 6 3:30 PM ET; #96 Porzingis and #97 Warriors streak scripts already exist for it, and the PC gap-fill (6:45 AM ET) covers it. Wed Nov 4's run in this session stopped at the weekly usage limit during research (nothing committed).

## Last 15 commits (any account)
- Nov 07 03:19 [CLOUD Research + scheduled runs] team: status: PC handoff Nov 7 + TikTok review + queue_rank fix
- Nov 07 03:19 [CLOUD Research + scheduled runs] team: message to A3
- Nov 07 03:19 [CLOUD Research + scheduled runs] team: message to A1
- Nov 07 03:19 [CLOUD] PC handoff Nov 7; TikTok page review; #79 to Sun 7:15 AM; mark 6 live Shorts' cards LIVE so nobody re-fixes them
- Nov 07 03:17 [CLOUD] queue_rank + schedule_ready: never offer or upload a Short that is already live (owner also posts by hand); title match on the newest API daily files of both channels
- Nov 06 18:30 Schedule ready drafts (script)
- Nov 06 23:10 [CLOUD Research + scheduled runs] team: message to BUILDER
- Nov 06 23:10 [CLOUD] Daily stats Nov 6; #92 slot corrected (uploaded for tonight 7:30 PM ET)
- Nov 06 16:43 Handoff (auto) from PC account 1
- Nov 06 16:43 Queue rank refresh
- Nov 06 16:42 Ideas note: pinned official footage candidates for N1 and F1
- Nov 06 16:42 daily-run: PC gap-fill exception; fee settlement for F1/F2
- Nov 06 16:40 Research: 10 NBA + 10 FC ideas rated on the 12-point bar (Nov 6 night)
- Nov 06 16:38 Deep-dive MetaSports case study (monetization math, ops audit, risks, actions)
- Nov 06 16:34 Held Shorts: card titles/tags/slots, source links, fix report

## Uncommitted here
     M "HANDOFF - latest.md"
     M "Research Notes/Preflight.md"
