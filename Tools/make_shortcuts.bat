@echo off
rem Run ONCE (double-click). Puts three icons on the Desktop: "Claude - Account 1", "Claude - Account 2" (builder) and "Claude - Account 3" (prep + review).
rem Each opens Git Bash in the repo and starts Claude as that account (own login, bypass mode, briefed from the handoff).
set REPO=%USERPROFILE%\Documents\metasports-shorts
set GITBASH=C:\Program Files\Git\git-bash.exe
if not exist "%GITBASH%" set GITBASH=%LOCALAPPDATA%\Programs\Git\git-bash.exe
for %%N in (1 2 3) do (
  > "%USERPROFILE%\Desktop\Claude - Account %%N.bat" (
    echo @echo off
    echo cd /d "%REPO%"
    echo start "" "%GITBASH%" -c "bash Tools/claude_acct.sh %%N; exec bash"
  )
)
echo Done. Three icons are on your Desktop: Claude - Account 1, 2 and 3.
pause
