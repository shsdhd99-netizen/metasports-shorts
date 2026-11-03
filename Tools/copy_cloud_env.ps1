# Copies the keys the CLOUD environment needs from Tools\.env to your clipboard (nothing is printed). Then paste them into
# claude.ai > Settings > Claude Code (cloud environment) > environment variables for env_016GURtEd17FS3mEXiKSjfM6, one NAME=value per line.
# Clear the clipboard afterwards (this script does it after 120 s). Names only are shown here.
$names = 'ELEVENLABS_API_KEY','ELEVENLABS_VOICE_ID','GEMINI_API_KEY','YT_CLIENT_ID','YT_CLIENT_SECRET','YT_REFRESH_TOKEN','YT_REFRESH_TOKEN_FC','YT_UPLOAD_TOKEN','YT_UPLOAD_TOKEN_FC'
$env_ = Join-Path $PSScriptRoot '.env'
$lines = Get-Content $env_ | Where-Object { $_ -match '^\s*([A-Z0-9_]+)\s*=' -and $names -contains $Matches[1] }
$lines -join "`r`n" | Set-Clipboard
Write-Host ("Copied {0} variables to the clipboard: {1}" -f $lines.Count, (($lines | ForEach-Object { ($_ -split '=')[0] }) -join ', '))
Write-Host "Paste them into the cloud environment settings now. The clipboard clears in 120 s."
Start-Sleep -Seconds 120
Set-Clipboard -Value ' '
