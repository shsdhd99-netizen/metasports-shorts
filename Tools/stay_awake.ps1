# Keeps the PC awake for N minutes (default 15). Used by the task "MetaSports wake", which wakes the PC 5 minutes before the
# timers that were registered as administrator (analytics 3:20 AM, schedule ready 6:30 AM / 6:30 PM, terminal resume Wed 1:30 PM)
# and therefore can't be given "wake the computer" without an admin prompt (Nov 3). Nothing else happens.
param([int]$Minutes = 15)
Add-Type -Namespace Win32 -Name Power -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint esFlags);'
$ES_CONTINUOUS = [uint32]2147483648; $ES_SYSTEM_REQUIRED = [uint32]1
[Win32.Power]::SetThreadExecutionState($ES_CONTINUOUS -bor $ES_SYSTEM_REQUIRED) | Out-Null
Start-Sleep -Seconds ($Minutes * 60)
[Win32.Power]::SetThreadExecutionState($ES_CONTINUOUS) | Out-Null
