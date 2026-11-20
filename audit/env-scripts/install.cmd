@echo off
rem Installs the audit's extensions into the ISOLATED audit copy only (own data + extensions folders).
set C="C:\Users\howla\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
set D=--user-data-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\data" --extensions-dir "C:\Users\howla\Desktop\test-code\rosin-audit-env\ext"
echo %date% %time% start > "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\install.log"
for %%X in (ms-vscode.cpptools@1.35.6 llvm-vs-code-extensions.vscode-clangd rust-lang.rust-analyzer@0.3.3121 ms-python.python@2026.10.0 ms-python.vscode-pylance@2026.4.1 ms-vscode.cmake-tools@1.25.10 tamasfe.even-better-toml@0.21.2 espressif.esp-idf-extension@2.3.0 dan-c-underwood.arm zixuanwang.linkerscript plorefice.devicetree mads-hartmann.bash-ide-vscode redhat.vscode-yaml ms-vscode.makefile-tools) do (
  echo === %%X >> "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\install.log"
  call %C% %D% --install-extension %%X --force >> "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\install.log" 2>&1
)
call %C% %D% --list-extensions --show-versions > "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\installed.txt" 2>&1
echo %date% %time% done >> "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\install.log"
