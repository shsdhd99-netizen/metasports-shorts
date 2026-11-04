# One-time fix (owner, Nov 3): the PC slept through the 3:20 AM analytics run on Nov 3 ("1 missed run").
# These four tasks were registered from an administrator window, so only an administrator can change them.
# HOW: right-click Windows PowerShell > Run as administrator, then paste:
#   powershell -ExecutionPolicy Bypass -File "C:\Users\Admin\Documents\metasports-shorts\Tools\fix_task_wake.ps1"
# It turns on, for every "MetaSports*" task: wake the computer to run it, run it as soon as possible after a missed start,
# and run on battery. Nothing else changes (same times, same actions).
Get-ScheduledTask -TaskName "MetaSports*" | ForEach-Object {
  $s = $_.Settings
  $s.WakeToRun = $true; $s.StartWhenAvailable = $true
  $s.DisallowStartIfOnBatteries = $false; $s.StopIfGoingOnBatteries = $false
  Set-ScheduledTask -TaskName $_.TaskName -Settings $s | Out-Null
  "{0}: wake {1}, catch up {2}" -f $_.TaskName, $s.WakeToRun, $s.StartWhenAvailable
}
Read-Host "Done. Press Enter to close"
