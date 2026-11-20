# Install ledger

Everything the audit adds to the Windows PC, and how it is undone. Cleanup works through this list and then
compares every VS Code profile's extension list with the baseline below.

## Baseline (2026-11-20, before anything was installed)
- VS Code 1.147.0 (commit 8a14f0cc1b), user setup at `%LOCALAPPDATA%\Programs\Microsoft VS Code`
- Default profile: 54 extensions; profile "WD": 35 extensions; profile "Agents" (built-in). Full lists: `audit/reports/A1-environment.md`
- Settings Sync is on and syncs profiles, so the audit does not create a VS Code profile.

## Added
| # | What | Where | Why | Undo |
|---|---|---|---|---|
| 1 | Isolated audit copy of VS Code: own user-data and extensions folders | `Desktop\test-code\rosin-audit-env\` | Keeps every audit extension and setting out of your profiles and Settings Sync | Delete the folder |
| 2 | Extensions installed into #1 only (list in `rosin-audit-env\logs\installed.txt`) | `rosin-audit-env\ext\` | Language servers and grammars under test | Removed with #1 |
| 3 | Probe extension, loaded from source with `--extensionDevelopmentPath` (never installed) | `rosin\audit\harness\probe\` | Records semantic tokens | Nothing to undo |
| 4 | clangd 23.1.0 for Windows, official release zip from github.com/clangd/clangd (sha256 23412a24…c810), unpacked, not installed system-wide | `rosin-audit-env\tools\clangd_23.1.0\` | clangd mode S run; used through the isolated copy's `clangd.path` setting | Removed with #1 |
| 5 | `diag-rust.cmd`, `update-ra.cmd` (read-only toolchain report; reinstall attempt of rust-analyzer into #1, a no-op: 0.3.3121 is the latest) | `rosin-audit-env\` | Diagnose unresolved `println!` | Removed with #1 |

## Cleanup (2026-11-20)
- `Desktop\test-code\rosin-audit-env\` deleted (items 1, 2, 4, 5: isolated VS Code data, the 16 audit-only extensions, clangd 23.1.0, helper scripts). Nothing was installed system-wide; rustup untouched.
- Copies of the scripts, `installed.txt`, `rust-toolchain.txt` and the isolated settings are kept in `audit/env-scripts/`. To re-run the server modes, recreate `Desktop\test-code\rosin-audit-env\`, copy the `.cmd` files back, run `install.cmd`, and unpack clangd 23.1.0 into `rosin-audit-env\tools\` for the clangd mode. The harness (`audit/harness/`) also reads extension grammars from `rosin-audit-env\ext\`, so it needs the reinstall too.
- Removed the empty `audit/corpus/c/.vscode/` and the generated `audit/corpus/.rosin-probe.json`.
- Profile check after cleanup (`audit/cleanup/`, from `code --list-extensions`): default profile 54 extensions, WD 35, the same counts as the baseline. The audit-pinned versions of cpptools, rust-analyzer, Pylance, CMake Tools, Even Better TOML and ESP-IDF that appear in the default profile are your own installs (they were in the 54 before the audit). The WD profile's extension list was last written on 2026-10-27, before the audit.
