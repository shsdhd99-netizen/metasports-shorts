@echo off
REM MetaSports daily analytics (read-only). Pulls YouTube Analytics for the last 30 days of uploads, writes
REM "Research Notes\Studio exports\api\daily <date>.csv" + "retention <date>.csv", and pushes them so the cloud routine can read them.
REM One-time setup: see Tools Guide.md, "YouTube Analytics API" (auth), then schedule this file:
REM   schtasks /create /sc daily /st 09:00 /tn "MetaSports analytics" /tr "\"%~f0\""
cd /d "%~dp0.."
git pull --rebase --autostash
python Tools\yt_analytics.py daily > "Research Notes\Studio exports\api\last_run.txt" 2>&1
git add "Research Notes/Studio exports/api"
git commit -m "Daily analytics pull (API, read-only)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push
