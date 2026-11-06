@echo off
rem Run ONCE (double-click). Puts three labelled icons on the Desktop:
rem   "Claude A1 - Builder", "Claude A2 - Builder backup", "Claude A3 - Prep and Review"
rem Each opens Git Bash in the repo and starts Claude as that account (own login, bypass mode, briefed from the handoff + team inbox).
rem A1 or A2 builds (never both at once); A3 can run at the same time as either.
set REPO=%USERPROFILE%\Documents\metasports-shorts
set GITBASH=C:\Program Files\Git\git-bash.exe
if not exist "%GITBASH%" set GITBASH=%LOCALAPPDATA%\Programs\Git\git-bash.exe
del "%USERPROFILE%\Desktop\Claude - Account 1.bat" "%USERPROFILE%\Desktop\Claude - Account 2.bat" "%USERPROFILE%\Desktop\Claude - Account 3.bat" 2>nul
call :make 1 "Claude A1 - Builder"
call :make 2 "Claude A2 - Builder backup"
call :make 3 "Claude A3 - Prep and Review"
echo Done. Three labelled icons are on your Desktop: A1 Builder, A2 Builder backup, A3 Prep and Review.
pause
goto :eof

:make
> "%USERPROFILE%\Desktop\%~2.bat" (
  echo @echo off
  echo cd /d "%REPO%"
  echo start "" "%GITBASH%" -c "bash Tools/claude_acct.sh %1; exec bash"
)
goto :eof
