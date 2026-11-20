@echo off
rem Read-only: lists the extensions in your normal VS Code profiles for the cleanup comparison.
set C="C:\Users\howla\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
set O=C:\Users\howla\Desktop\test-code\rosin\audit\cleanup
call %C% --list-extensions --show-versions > "%O%\default-profile.txt" 2>&1
call %C% --list-extensions --show-versions --profile WD > "%O%\wd-profile.txt" 2>&1
echo done > "%O%\list.done"
