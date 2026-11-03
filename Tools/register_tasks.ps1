# ONE-TIME, run by the owner (Claude's auto mode blocks creating persistent tasks):   ! powershell -ExecutionPolicy Bypass -File Tools\register_tasks.ps1
# Registers: schedule-ready AM/PM timers (private + publishAt uploads via yt_schedule.py guard rails), the Wed Nov 4 1:30 PM terminal resume.
# Run it again any time; /f overwrites. Remove later with: schtasks /delete /tn "<name>" /f
$repo = Split-Path $PSScriptRoot -Parent
$bat  = Join-Path $PSScriptRoot 'schedule_ready.bat'
$res  = Join-Path $PSScriptRoot 'resume_terminal.ps1'
schtasks /create /sc daily /st 06:30 /tn "MetaSports schedule ready AM" /tr "`"$bat`"" /f
schtasks /create /sc daily /st 18:30 /tn "MetaSports schedule ready PM" /tr "`"$bat`"" /f
schtasks /create /sc once /sd 11/04/2026 /st 13:30 /tn "MetaSports terminal resume" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$res`"" /f
Get-ScheduledTask | Where-Object { $_.TaskName -like 'MetaSports*' } | ForEach-Object { '{0} | next {1}' -f $_.TaskName, (Get-ScheduledTaskInfo $_).NextRunTime }
