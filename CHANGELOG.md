# Changelog

## 1.1.0

Colour audit: every colour role was checked token by token in 20 languages, with and without their language servers (cpptools, clangd, rust-analyzer, Pylance, Even Better TOML), and the theme rules were adjusted so each role shows the same colour wherever the grammar or server allows it. Where it can't, the exception is now documented.

**Colour changes**
- Keywords that introduce a type (`struct`, `class`, `enum`, `trait`, `namespace`, `typedef`, `type`) use the keyword colour; built-in and standard-library types (`size_t`, Rust `String` / `Result`) use the primitive-type colour.
- Number prefixes, suffixes and exponents (`0x`, `UL`, `1e-3`, `_ms`, Rust `u8`) use the new unit colour in C, C++, Rust and Python.
- Enum members and Rust `Some` / `None` / `Ok` / `Err` use the number / constant colour.
- C and C++: qualified namespaces (`outer::inner`), owners in out-of-line definitions (`Led::get`), class members, `decltype` / `noexcept` / `requires`, `extern`, user-defined literals, digit separators, `u8` strings and inline-assembly strings.
- Rust: `macro_rules!`, macro variables (`$x`), `static`, `super`, raw strings and `::` paths.
- Python: `global` / `nonlocal`, raw and multi-line strings, line continuations, dunder methods, imaginary literals and `metaclass`.
- Shell, Makefile, CMake, YAML, TOML, diff, git commit, ARM assembly, linker script, devicetree and Kconfig: smaller fixes to variables, labels, operators, document markers and special targets.
- With clangd: deduced types (`auto`), constructors and destructors, concepts and file-scope `static` variables. With Pylance: library decorators.
- ESP-IDF verbose (`V`) log lines have their own colour instead of sharing the debug colour.

**Documentation**
- README: new "What each colour means" table and a "Language support" section. For each language it lists the extensions to install, how many checked tokens show as designed, and every known exception, per setup (nothing installed, cpptools, clangd and so on). The tagline now says each colour keeps one meaning across languages, with the exceptions documented.
- The full limits register and the audit (test files, reports, tooling) are in `audit/`. They are not shipped in the extension.

**Known limit**
- With rust-analyzer 0.3.3121 on Rust 1.93.1, `println!` and `write!` are unresolved and show in the error style. This comes from rust-analyzer, not the theme.

**Internal**
- Duplicate theme rules were removed. There is no visible change.

## 1.0.2

- README & package: Minor update to Litrature and Description

## 1.0.1

- README: Marketplace install and `.vsix` download buttons.
- Releases on GitHub now include the `.vsix`.

## 1.0.0

- First release with six flavours: Sea Salt, Black Cherry, Matcha, Espresso, Licorice (stealth) and OLED.
- Every themeable VS Code UI colour is set (about 970 keys).
- Consistent colour roles across C, C++, Rust, Python, JS/TS, Go, shell, PowerShell, Make, CMake, TOML, INI, YAML, HTML/CSS, SQL, Lua, assembly, devicetree, linker scripts, diff and git.
- Log-level colouring, including ESP-IDF and Zephyr formats.
