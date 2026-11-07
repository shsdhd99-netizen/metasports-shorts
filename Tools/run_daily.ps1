# PC safety net for ONE channel (nba or fc): builds ONLY when the next 54 h of slots has a gap nobody filled (Nov 3 rewrite).
# The cloud routines run first (3:17-5:39 AM ET); this runs after them (NBA 6:45 AM, FC 7:30 AM) and fills only what they left open,
# so cloud and PC never build the same slot. Registered tasks: "MetaSports gapfill nba" / "MetaSports gapfill fc".
# Safety: preflight first (BLOCKED = zero-credit steps only); Tools/next_gap.py decides if there is anything to build; a lock file stops
# two runs overlapping; Claude runs as PC account 1 (CLAUDE_CONFIG_DIR, like Tools/claude_acct.sh) in the owner's bypass mode, because
# acceptEdits denies every shell command in an unattended run. The skill itself never posts; scheduling stays with schedule_ready's guard rails.
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
  $gap = & python Tools\next_gap.py $Channel 2>&1 | Select-Object -Last 1
  Write-Log "gap check: $gap"
  if ($gap -notmatch '^GAP') { Write-Log 'nothing to build (every slot in the next 54 h is covered); Claude not started'; exit 0 }
  if ($pf -match 'BLOCKED') { Write-Log 'gap found but preflight is BLOCKED; Claude not started (fix the blocker in Preflight.md)'; exit 0 }
  $env:CLAUDE_CONFIG_DIR = "$env:USERPROFILE\.claude-account1"
  $exe = 'C:\Users\Admin\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
  if (-not (Test-Path $exe)) { $exe = (Get-Command claude -ErrorAction SilentlyContinue).Source }
  $target = if ($gap -match '^GAP') { " Build ONE Short for this open slot: $gap (it was left open by the cloud runs). Claim the folder in STATE.md first; if a claim or a new DRAFT for that slot appeared after the pull, build nothing." } else { '' }
  $prompt = "You are PC account 1, running unattended (the owner may be asleep). Run the daily-run skill (.claude/skills/daily-run/SKILL.md) for channel '$Channel' as $mode.$target Read Research Notes/USAGE.txt, STATE.md and Preflight.md first. Never post or schedule outside Tools/yt_schedule.py guard rails. Commit small, push at the end, update STATE.md and append a STATUS line to Research Notes/Daily Log.md."
  Write-Log "starting claude ($mode)"
  & $exe --dangerously-skip-permissions -p $prompt *>> $log
  Write-Log ("claude ended, exit {0}" -f $LASTEXITCODE)
} finally { Remove-Item $lock -ErrorAction SilentlyContinue }
