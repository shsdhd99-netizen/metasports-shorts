# One-shot resume (register with schtasks, see "HANDOFF - Nov 4 resume 1-30 PM.md"). Starts a FRESH claude session on this repo.
$ErrorActionPreference = 'Continue'
$repo = 'C:\Users\Admin\Documents\metasports-shorts'
$log  = Join-Path $repo 'Research Notes\Resume Last Run.txt'
$exe  = 'C:\Users\Admin\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
function Write-Log($m) { Add-Content -Path $log -Value ('{0:yyyy-MM-dd HH:mm:ss} {1}' -f (Get-Date), $m) }
Set-Location $repo
if (-not (Test-Path $exe)) { $exe = (Get-Command claude -ErrorAction SilentlyContinue).Source }
if (-not $exe) { Write-Log 'FAILED: claude not found'; exit 1 }
git pull --no-rebase origin main-329h3w 2>&1 | Out-Null
Write-Log 'starting fresh session'
$prompt = 'You are Account 1 on the owner PC terminal. Read "HANDOFF - Account 1 START HERE (Nov 4).md" in the repo root and carry out its section 3 (the 1:30 PM start-up list) autonomously in order, then its section 4 loop. BUILDER.txt is cloud: do NOT build Shorts here unless the handoff says the cloud failed. Commit small, push, update Research Notes/STATE.md and append STATUS lines to Research Notes/Daily Log.md. The weekly limit reset at 1 PM ET; if you cannot read usage, read Research Notes/USAGE.txt and say what you assumed. Stop at weekly 99 percent or any hard limit.'
& $exe --permission-mode acceptEdits -p $prompt *>> $log
Write-Log ('session ended, exit {0}' -f $LASTEXITCODE)
