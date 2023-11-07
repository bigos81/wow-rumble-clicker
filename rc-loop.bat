echo off > null
cls
:loop
echo %DATE% %TIME% starting quests >> log.txt
rc-quest.py
echo quests done, exitcode: %ERRORLEVEL% >> log.txt
echo %DATE% %TIME% starting pvp >> log.txt
rc-pvp.py
echo pvp done, exitcode: %ERRORLEVEL% >> log.txt
goto loop