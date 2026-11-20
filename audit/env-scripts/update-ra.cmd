@echo off
rem Installs the latest rust-analyzer into the ISOLATED audit copy only.
call "C:\Users\howla\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd" --user-data-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\data" --extensions-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\ext" --install-extension rust-lang.rust-analyzer --force > "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\ra-update.log" 2>&1
call "C:\Users\howla\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd" --user-data-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\data" --extensions-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\ext" --list-extensions --show-versions >> "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\ra-update.log" 2>&1
