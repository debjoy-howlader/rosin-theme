@echo off
rem Rosin audit, mode S run "calib": isolated VS Code, Rosin and the probe loaded from source, corpus folder opened.
copy /Y "C:\Users\howla\Desktop\test-code\rosin\audit\corpus\probe-calib.json" "C:\Users\howla\Desktop\test-code\rosin\audit\corpus\.rosin-probe.json" >nul
start "" "C:\Users\howla\AppData\Local\Programs\Microsoft VS Code\Code.exe" --user-data-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\data" --extensions-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\ext" --extensionDevelopmentPath="C:\Users\howla\Desktop\test-code\rosin" --extensionDevelopmentPath="C:\Users\howla\Desktop\test-code\rosin\audit\harness\probe" --disable-extension llvm-vs-code-extensions.vscode-clangd "C:\Users\howla\Desktop\test-code\rosin\audit\corpus"
