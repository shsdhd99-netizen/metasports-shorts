# Handoff (auto), Fri Nov 06 2026, 09:25 UTC, written by account: app account 1 (cloud FC routine)

Read this first, then `Research Notes/Daily Log.md` (newest entries) before building anything, so two sessions never build the same Short.

## Note from the last session
FC Nov 6: blocked at preflight (YT secrets missing in cloud env), no FC gap to Nov 8; lessons/weights updated. Next: build only when a gap opens and preflight passes

## Keys on this machine (presence only)
- ELEVENLABS_API_KEY: set
- GEMINI_API_KEY: set
- YT_CLIENT_ID: MISSING
- YT_REFRESH_TOKEN: MISSING
- YT_REFRESH_TOKEN_FC: MISSING
- YT_UPLOAD_TOKEN: MISSING
- YT_UPLOAD_TOKEN_FC: MISSING
- NETLIFY_AUTH_TOKEN: MISSING
- HEYGEN_API_KEY: MISSING

## Newest STATUS lines (Daily Log)
- STATUS: PC account 1 NBA gap-fill, Nov 5: filled Fri Nov 6 3:30 PM ET by scheduling the already-built #95 (Lendeborg peer pressure; QA PASS re-run, private + publishAt via schedule_ready). No new build, no credits spent.
- STATUS: blocked, no build. BUILDER.txt = `cloud`; voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). `next_gap.py fc`: NO GAP in 54 h. No credits spent.
- STATUS: blocked, no build. Voice and Gemini keys set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment), so no credits spent (CLOUD DAILY RULES step 4). Next NBA gap: Sat Nov 7 3:30 PM ET, in range of the PC gap-fill (6:45 AM ET). Same block as Nov 5: this routine's session needs the four YouTube secrets to ever build.
- STATUS: blocked, no build. BUILDER.txt = `cloud`; `cloud_setup.sh`: voice key set, Gemini set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this environment). Rule 4: script/notes only, no credits. Also `next_gap.py fc`: NO GAP in the next 54 h (FC covered through Sun Nov 8 by S09/S29; S31, S32, S30, S21, S22, S36 already scripted for Nov 8-13), so no new script either. The Nov 4 run's notification reached this session only today (not run separately).
- STATUS: blocked, no build. `cloud_setup.sh`: voice key set, Gemini set; `preflight.py --quiet`: BLOCKED (YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC missing in this session's environment). Per CLOUD DAILY RULES step 4: no credits spent. Next NBA gap (`next_gap.py`): Fri Nov 6 3:30 PM ET; #96 Porzingis and #97 Warriors streak scripts already exist for it, and the PC gap-fill (6:45 AM ET) covers it. Wed Nov 4's run in this session stopped at the weekly usage limit during research (nothing committed).

## Last 15 commits (any account)
- Nov 06 09:25 FC cloud run Nov 6: blocked (YT secrets missing), no FC gap; S25 23K at 72 h; lessons, weights, log, STATE
- Nov 06 08:45 Daily research Nov 6: competitor outliers
- Nov 06 08:44 Daily research Nov 6: Klay blocks Steph, Warriors 6 straight, Como 9-1
- Nov 06 08:19 NBA cloud routine Nov 6: STATUS blocked (YouTube tokens missing in this environment), no build
- Nov 05 18:30 Schedule ready drafts (script)
- Nov 05 23:10 Daily stats Nov 5
- Nov 05 15:04 What-matters-vs-wait research, project charter, advisor memo, duplicate-upload guard, short watcher
- Nov 05 13:08 S27 re-uploaded with proper title (no-music file); parse_card reads soccer H1 titles; read-back check; title_audit
- Nov 05 13:05 yt_schedule: refuse placeholder titles (unknown/untitled/none)
- Nov 05 11:17 Test-and-learn policy (FC not limited to goalkeepers), posting plan and alternating test, idea triage, QA audit + pre-cut lint, autopilot test mode
- Nov 05 11:13 Max: friend prices
- Nov 05 10:59 Build gate, posting cadence review, efficiency review
- Nov 05 10:40 Merge remote-tracking branch 'origin/main-329h3w' into main-329h3w
- Nov 05 10:40 README, reminders, state reminders
- Nov 05 10:39 Apply case-study findings: paused-shape gate in idea_gauge, test-arm rotation, daily rules

## Uncommitted here
     M "HANDOFF - latest.md"
