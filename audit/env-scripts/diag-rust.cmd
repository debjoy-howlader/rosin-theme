@echo off
rem Read-only: report the Rust toolchain rust-analyzer will use.
cd /d "C:\Users\howla\Desktop\test-code\rosin\audit\corpus\rust"
(rustup show & echo ---- & rustup component list --installed & echo ---- & rustc --version --verbose & echo ---- & rustc --print sysroot) > "C:\Users\howla\Desktop\test-code\rosin-audit-env\logs\rust-toolchain.txt" 2>&1
