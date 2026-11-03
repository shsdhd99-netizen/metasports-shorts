# Unattended daily run for ONE channel (nba or fc). Register one task per channel, e.g. (owner, once):
#   schtasks /create /sc daily /st 06:45 /tn "MetaSports daily nba" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\Admin\Documents\metasports-shorts\Tools\run_daily.ps1 nba" /f
#   schtasks /create /sc daily /st 07:30 /tn "MetaSports daily fc"  /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\Admin\Documents\metasports-shorts\Tools\run_daily.ps1 fc" /f
# Safety: preflight first (a BLOCKER writes one STATUS line and stops); BUILDER.txt must say pc; lock file stops two runs overlapping;
# the session itself obeys the daily-run skill (never posts; weekly over 90% means zero-credit steps only; stops at 99%).
param([Parameter(Mandatory=$true)][ValidateSet('nba','fc')][string]$Channel)
$ErrorActionPreference = 'Continue'
$repo = 'C:\Users\Admin\Documents\metasports-shorts'
$log  = Join-Path $repo "Research Notes\Daily Run $Channel Last.txt"
$lock = Join-Path $repo "Research Notes\.run_daily.lock"
function Write-Log($m) { Add-Content -Path $log -Value ('{0:yyyy-MM-dd HH:mm:ss} {1}' -f (Get-Date), $m) }
Set-Location $repo
if (Test-Path $lock) {
  $old = Get-Content $lock -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($old -match '^\d+$' -and (Get-Process -Id ([int]$old) -ErrorAction SilentlyContinue)) { Write-Log "another run is active (pid $old); exit"; exit 0 }
}
Set-Content -Path $lock -Value $PID
try {
  git pull --no-rebase origin main-329h3w 2>&1 | Out-Null
  $pf = & python Tools\preflight.py --quiet 2>&1 | Select-Object -Last 1
  Write-Log "preflight: $pf"
  $mode = if ($pf -match 'BLOCKED') { 'zero-credit steps only, because preflight is BLOCKED' } else { 'a normal daily run' }
  $builder = (Get-Content "Research Notes\BUILDER.txt" -ErrorAction SilentlyContinue | Select-Object -First 1)
  if ($builder -ne 'pc') { $mode = 'zero-credit steps only, because BUILDER.txt is not pc' }
  $exe = 'C:\Users\Admin\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
  if (-not (Test-Path $exe)) { $exe = (Get-Command claude -ErrorAction SilentlyContinue).Source }
  $prompt = "Run the daily-run skill (.claude/skills/daily-run/SKILL.md) for channel '$Channel' as $mode. Read Research Notes/USAGE.txt, STATE.md and Preflight.md first. Never post or schedule outside Tools/yt_schedule.py guard rails. Commit small, push at the end, update STATE.md and append a STATUS line to Research Notes/Daily Log.md."
  Write-Log "starting claude ($mode)"
  & $exe --permission-mode acceptEdits -p $prompt *>> $log
  Write-Log ("claude ended, exit {0}" -f $LASTEXITCODE)
} finally { Remove-Item $lock -ErrorAction SilentlyContinue }
