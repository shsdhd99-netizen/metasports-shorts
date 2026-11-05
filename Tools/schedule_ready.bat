@echo off
REM Schedules ready DRAFTs (private + publishAt, yt_schedule.py guard rails) and commits the log. Zero Claude credits.
REM Register (owner, once; run in a normal terminal):
REM   schtasks /create /sc daily /st 06:30 /tn "MetaSports schedule ready AM" /tr "\"%~f0\""
REM   schtasks /create /sc daily /st 18:30 /tn "MetaSports schedule ready PM" /tr "\"%~f0\""
cd /d "%~dp0.."
git pull --no-rebase --autostash
python Tools\schedule_ready.py --go >> "Research Notes\Schedule Ready Last Run.txt" 2>&1
REM Nov 3: refresh the TikTok/Instagram cross-post queue from what is now on YouTube
python Tools\crosspost.py >> "Research Notes\Schedule Ready Last Run.txt" 2>&1
git add "Research Notes/Scheduled Uploads.csv" "Research Notes/Schedule Ready Log.md" "Research Notes/Crosspost Queue.md"
git commit -m "Schedule ready drafts (script)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
REM Nov 5: the cloud may have pushed meanwhile; .gitattributes merge=union keeps both sides of the log/CSV files, so pull and retry once
git push || (git pull --no-rebase --autostash && git push)
python Tools\state.py >nul 2>&1
