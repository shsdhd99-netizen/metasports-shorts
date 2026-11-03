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
$prompt = 'Read "HANDOFF - Nov 4 resume 1-30 PM.md", "HANDOFF - Nov 3 terminal.md" and "AUTOMATION TO-DO (Nov 3).md" and carry out section 2 of the Nov 4 handoff autonomously, in order. Commit small after each item. The weekly limit reset at 1 PM ET, so usage is low: if you cannot read /usage, assume under 50% and write that assumption in the STATUS line. Stop at weekly 99% or any hard limit and write a STATUS line in Research Notes/Daily Log.md. Push at the end.'
& $exe --permission-mode acceptEdits -p $prompt *>> $log
Write-Log ('session ended, exit {0}' -f $LASTEXITCODE)
