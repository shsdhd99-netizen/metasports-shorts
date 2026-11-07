# Daily automation review, Nov 4-17, 2026 (task "MetaSports automation review", 9:00 AM). Zero credits on a good day.
# Runs Tools/automation_review.py (writes Research Notes/Automation Check.md), commits and pushes it. On a FAIL it starts ONE
# Claude session (PC account 1, bypass mode like the desktop launcher) to diagnose and fix, then log a STATUS line.
$ErrorActionPreference = 'Continue'
$repo = 'C:\Users\Admin\Documents\metasports-shorts'
Set-Location $repo
git pull --no-rebase --autostash origin main-329h3w 2>&1 | Out-Null
$out = & python Tools\automation_review.py 2>&1
$code = $LASTEXITCODE
git add "Research Notes/Automation Check.md" 2>&1 | Out-Null
git commit -m "Automation check (script)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" 2>&1 | Out-Null
git push 2>&1 | Out-Null
if ($code -eq 2) {
  $env:CLAUDE_CONFIG_DIR = "$env:USERPROFILE\.claude-account1"
  $exe = 'C:\Users\Admin\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
  if (-not (Test-Path $exe)) { $exe = (Get-Command claude -ErrorAction SilentlyContinue).Source }
  $fails = ($out | Select-String '^FAIL') -join '; '
  $prompt = "You are PC account 1, running unattended for the daily automation review (Nov 4-17). Today's check FAILED: $fails. Read Research Notes/Automation Check.md (newest block), Research Notes/BUILDER.md and the newest Daily Log entries. Diagnose each FAIL and fix what you can without the owner (never post, never schedule outside Tools/yt_schedule.py guard rails, never print keys). If a fix needs the owner, add one clear task to the owner's task list (artifact https://claude.ai/artifact/Ki1UXnbxsdykE4dy7BwyLT, collection tasks) instead of retrying. Re-run python Tools/automation_review.py at the end. Commit, push, and append a STATUS line to Research Notes/Daily Log.md."
  & $exe --dangerously-skip-permissions -p $prompt *>> "Research Notes\Automation Review Last.txt"
}
