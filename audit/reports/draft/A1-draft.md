# Audit report A1 — pass 1, first measurement (draft)

20 Nov 2026 · Rosin 1.0.2 (HEAD `ea3c738` + uncommitted README/package/CHANGELOG edits) · Role Spec v1

**Status: incomplete, not yet valid as evidence.** Every component in the corpus is measured, and the harness has matched
VS Code's inspector on 12 of 12 tokens read so far. Four things are still missing before this pass counts under the protocol:

1. **Coverage** is below 100% for every grammar (table in §2). The corpus needs more constructs before the claim is backed.
2. **Calibration** stopped at 12 of 54 tokens because Windows locked the screen. Licorice and mode T on the extension grammars aren't calibrated yet.
3. **Rust mode S** is invalid: rust-analyzer sampled before it finished, so `println!` and `write!` show as unresolved. A rerun with a 90 s minimum wait is queued.
4. **Design questions** (§7) decide the expected role for 78 components. Their verdicts below are provisional.

No theme file was changed during this audit.

## 1. Environment snapshot

| Item | Value |
|---|---|
| OS | Windows (device "lappy"), x64 |
| VS Code | 1.147.0, commit 8a14f0cc1b, user setup |
| Audit copy | isolated `--user-data-dir` and `--extensions-dir` in `Desktop\test-code\rosin-audit-env`; your profiles and Settings Sync untouched |
| Rosin | loaded from source with `--extensionDevelopmentPath`; source and committed `themes/*.json` verified identical to `gen.py` output |
| Colour settings | `editor.semanticHighlighting.enabled: true`, `C_Cpp.enhancedColorization: enabled`, no colour customisations |
| Servers (mode S) | cpptools 1.35.6 (GCC IntelliSense mode), clangd 23.1.0 via vscode-clangd 0.6.0, rust-analyzer 0.3.3121, Pylance 2026.4.1, Even Better TOML 0.21.2 |
| Grammars from extensions | CMake Tools 1.25.10 (CMake), Even Better TOML (TOML), ESP-IDF 2.3.0 (Kconfig), ARM 1.7.4 (`dan-c-underwood.arm`), LinkerScript 1.0.4, DeviceTree 0.1.1 |
| No semantic tokens sent | Red Hat YAML 2.0.0, Bash IDE 1.43.2, Makefile Tools 0.12.17, CMake Tools, DeviceTree, ESP-IDF (Kconfig), LinkerScript, ARM; built-in JSON, INI, Markdown, Log, Diff, Git |
| Harness | `vscode-textmate` 9.3.2 and `vscode-oniguruma` 1.7.0 extracted from this VS Code install; semantic resolution ported from VS Code at the same commit |

Mode T for Python means without Pylance, because Pylance replaces the Python grammar with its own.
For TOML, CMake, Kconfig, assembly, linker scripts and devicetree, the grammar extension is required, so mode T means "grammar only".

## 2. Coverage

Scope names a file's grammar can emit (including grammars it includes) against the names the corpus produced.
Markdown's figure counts every embedded grammar, so it isn't meaningful yet; it will be reported for Markdown's own grammar.

| Corpus file | Grammar | Scope names produced |
|---|---|---|
| c/corpus.c | source.c | 108 / 207 (52%) |
| cpp/corpus.cpp | source.cpp | 163 / 549 (30%) |
| rust/corpus.rs | source.rust | 71 / 98 (72%) |
| python/corpus.py | source.python (MagicPython) | 77 / 179 (43%) |
| shell/corpus.sh | source.shell | 77 / 165 (47%) |
| make/Makefile | source.makefile | 19 / 24 (79%) |
| cmake/CMakeLists.txt | source.cmake | 27 / 37 (73%) |
| config/corpus.json | source.json | 20 / 30 (67%) |
| config/corpus.yaml | source.yaml | 25 / 64 (39%) |
| config/corpus.toml | source.toml | 22 / 38 (58%) |
| config/corpus.ini | source.ini | 6 / 14 (43%) |
| logs/corpus.log | text.log + Rosin injection | 15 / 23 (65%) |
| diff/corpus.diff | source.diff | 13 / 27 (48%) |
| git/COMMIT_EDITMSG | text.git-commit | 4 / 43 (9%) |
| asm/corpus.S | source.arm | 11 / 27 (41%) |
| ld/corpus.ld | source.ld | 10 / 19 (53%) |
| dts/corpus.dts | source.dts | 13 / 19 (68%) |
| kconfig/Kconfig | source.kconfig | 6 / 10 (60%) |

Server legends, token types seen / declared: cpptools C 8/23, C++ 11/23 · clangd C 11/20, C++ 15/20 · rust-analyzer 33/58 · Pylance 11/29 · Even Better TOML 2/2.
The missing names are listed per file in `A1-coverage.json`; they are the to-do list for the corpus.

## 3. Calibration

12 of 54 planned tokens read in the inspector, all in Sea Salt: **12 match, 0 mismatch**, colour and font style.
They cover TextMate-only tokens, cpptools semantic overrides (including the `global` modifier), rust-analyzer `keyword.unsafe` with bold,
and doc-comment tags. Not yet covered: Licorice, mode T on extension grammars, injections, Pylance. Readings: `calibration-observed.json`.

## 4. Results

549 components across 18 files. Counts before design answers, so the `?Qn` entries count against whatever the provisional expectation was.

| Mode | EXACT | FALLBACK | PLAIN | WRONG |
|---|---|---|---|---|
| T (all files) | 368 | 14 | 63 | 104 |
| S cpptools (C, C++) | 137 | – | 1 | 33 |
| S clangd (C, C++) | 136 | – | 3 | 32 |
| S rust-analyzer | invalid, rerun | | | |
| S Pylance + Even Better TOML | see appendix | | | |

Full table: `A1-appendix-verdicts.md`.

## 5. Findings with a fix (change proposals)

Each CP edits a source file under `tools/`, never `themes/*.json`. Predicted moves (the what-if run) are computed at the start of the edit phase and listed in the edit log.
Severity: 1 wrong meaning on a common construct · 2 split between modes · 3 wrong meaning on a rare construct · 4 style only.

| CP | Sev | Finding | Cause (from the inspector/scopes) | Proposed change |
|---|---|---|---|---|
| CP-A1-01 | 1 | Every `[` `]` in C (and other grammars using `bracket.square`) shows the **member** colour | Members rule lists `punctuation.definition.begin/end.bracket.square` | Remove both selectors from the Members rule; TOML/INI table brackets keep their own rule |
| CP-A1-02 | 1 | Python dunder methods (`__post_init__`) show **member** | Members rule lists `support.variable.magic` | Remove it; dunders fall to the function/method rules |
| CP-A1-03 | 1 | Rust `struct` `enum` `trait` and `let` `mod` show the **primitive-type** colour in mode T | Innermost scope `storage.type.rust` matches "Primitive types" and beats `keyword.declaration.*` | Descendant selectors such as `keyword.declaration.struct storage.type.rust`, final role per P1 |
| CP-A1-04 | 1 | Rust `u8` `usize` `str` show the **user-type** colour in mode T; suffix `7u8` too | Scopes `entity.name.type.numeric/primitive.rust` match the user-type rule | Map them to primitive; `constant.numeric entity.name.type.numeric` to unit |
| CP-A1-05 | 1 | Rust `const` and `static` items show plain text in mode S | rust-analyzer sends token types `const` and `static` (subtypes of variable); Rosin has no rule | `const` → number, `static` → static variable |
| CP-A1-06 | 2 | Python decorators show function/class colour in mode S; builtins (`print`, `open`) show user-function colour; class attributes plain | Pylance modifiers `decorator`, `builtin`, `classMember` have no rules | `*.decorator` → directive, `function.builtin` → library function, `variable.classMember` → member |
| CP-A1-07 | 3 | C `__asm__` shows primitive-type colour | `storage.type.asm.c` matches "Primitive types" | `storage.type.asm` → keyword |
| CP-A1-08 | 2 | C++ template parameter `T` shows user-type colour in mode T | `entity.name.type.template.cpp` matches the user-type rule | `entity.name.type.template` → type parameter (cpptools sends plain `type` for it: limit candidate L-07) |
| CP-A1-09 | 1 | Kconfig `config` `menu` show **hazard**; `default` `depends` `help` `range` and the type `int` show qualifier | ESP-IDF grammar uses `variable.language.kconfig` and `storage.modifier.kconfig`; Rosin maps `variable.language` to hazard | `source.kconfig`-scoped rules, roles per P11 and P12 |
| CP-A1-10 | 1 | Devicetree node names show function-italic, labels show user-type | This grammar uses `entity.name.function.dts` for nodes and `entity.name.type.dts` for labels, the reverse of Rosin's rules | Swap the two dts rules |
| CP-A1-11 | 1 | ARM labels, registers, symbol references and `[` plain | This grammar uses `routine.arm`, `storage.register.arm`, `variable.named.arm`, `storage.memaddress.arm`, none of which Rosin covers | `source.arm` rules: labels → function, registers → hazard, symbol refs per P12 |
| CP-A1-12 | 2 | Linker script: numbers, section names, symbols plain; region `FLASH` keyword colour in its definition | Grammar scopes regions as `support.function.builtin.ld` there and `variable.other.ld` elsewhere; numbers unscoped | Rules for what the grammar does scope; the rest goes to limits after a full scope check |
| CP-A1-13 | 3 | Git commit subject plain | Grammar scope is `meta.scope.subject.git-commit`; Rosin targets `markup.heading` inside the message | Add `meta.scope.subject.git-commit` |
| CP-A1-14 | 1 | CMake keyword arguments (`VERSION`, `PRIVATE`) show **member**; bracket arguments show parameter-italic | cmake-tools grammar uses `support.type.property.cmake` for keyword arguments and `variable.parameter.cmake` for bracket arguments | Map `support.type.property.cmake` to qualifier; bracket arguments per P10 |
| CP-A1-15 | 3 | Make `.PHONY` shows library-function colour | `support.function.target.PHONY.makefile` matches the library-function rule | Role per P11 |
| CP-A1-16 | 2 | Rust format placeholders `{}` `{name}` show punctuation in mode T | `punctuation.definition.interpolation.rust` inside `meta.interpolation.rust` | `meta.interpolation.rust` → hazard, matching C `%d`; mode S result after the rerun |
| CP-A1-17 | 4 | C `/**` delimiter shows comment colour while the doc text shows doc colour | `punctuation.definition.comment` rule beats the doc rule on the delimiter | Doc-comment delimiters → doc |
| CP-A1-18 | 1 | Make `$(CC)`, CMake `${BOARD}`: delimiters punctuation, name config-variable; shell `${PORT}` is config-variable throughout | Make/CMake grammars scope the delimiters as punctuation | Make the sigil and braces take the config-variable colour everywhere (P9) |
| CP-A1-19 | 3 | Shell `[[` punctuation, `&&` punctuation, test flag `-f` keyword | Shell grammar scopes them as `punctuation.definition.logical-expression`, `punctuation.separator.statement.and`, `keyword.operator.logical` | Per P8/P9 |

## 6. Limit candidates

Each needs its proof attached before it moves to the limits register. Proof shown where already collected.

| ID | Mode | What you see | Cause and proof |
|---|---|---|---|
| L-01 | T, C | `& * ~ ^ |` (address-of, dereference, bitwise) quiet, not hazard | Grammar can't tell: `* / % + - ~ & | ^` all get exactly `keyword.operator.c`. The C++ grammar does separate them. |
| L-02 | S clangd | all operators quiet, including bitwise and `!` `?` `new` `delete` | Server can't tell: clangd sends type `operator` with no kind modifier for all of them; it overrides the grammar's correct C++ bitwise scopes |
| L-03 | T, C/C++ | struct/enum tags, typedef names at definition, members at declaration, enum members, labels plain | Grammar emits no scope for these positions (scope stack ends at `meta.block.c`) |
| L-04 | T, C | function-like macro calls look like function calls; `printf` looks like a user function | `meta.function-call.c entity.name.function.c` for both |
| L-05 | S cpptools | `printf`/`memcpy` user-function colour; file-scope `static` and `const` globals show global-variable colour | cpptools legend has no `defaultLibrary` or `readonly`; it marks `s_count` and `k_max` only as `global` |
| L-06 | S clangd | file-scope `static` variables show global-variable colour | clangd marks them `fileScope` without `static`; Rosin maps `variable.fileScope` to global. Interacts with P-static |
| L-07 | S cpptools | C++ template parameter `T` shows user-type colour | cpptools sends plain `type` |
| L-08 | T, Rust | `unsafe` keyword colour, `//!` comment colour | Grammar scopes `unsafe` as `keyword.other.rust` like `let`, and `//!` as a plain line comment |
| L-09 | S rust-analyzer | `struct` `enum` `trait` `impl` `pub` `mut` all keyword colour; `&` borrow quiet | rust-analyzer sends type `keyword` and `operator` with no distinguishing modifier (legend in `A1-coverage.json`) |
| L-10 | T, YAML/Python/Rust | YAML dates are strings; Rust `static mut TICKS` shows constant colour | Grammar can't tell: `string.unquoted.plain.out.yaml`; `constant.other.caps.rust` comes from the upper-case name |
| L-11 | T, C | `__attribute__` and `_Static_assert` show function colour | Grammar mis-parses them as function declarations (`meta.function.definition.parameters.c entity.name.function.c`) |
| L-12 | T, C | uses of a macro parameter inside the body show directive colour | No scope beyond `meta.preprocessor.macro.c` |
| L-13 | S cpptools/clangd | C `bool` and `true` (from `<stdbool.h>`) show bold macro | Correct per the servers: in C17 they are macros. Becomes a limit or a design call (P-bool) |

## 7. Design questions

78 components wait on a design answer. They reduce to these principles. My recommendation is first; nothing below is applied until you approve.

| P | Question | Components | Recommendation |
|---|---|---|---|
| P1 | Do type-introducing keywords (`struct` `enum` `class` `union` `trait` `impl` `namespace` `template` `typename` `mod`) share the user-type colour, or are they keywords? | Q15, Q25, Q37, Rust kw | **Keywords.** rust-analyzer sends them all as `keyword`, so the user-type choice can't hold in Rust mode S (L-09); keyword is consistent everywhere |
| P2 | Is `uint8_t` / `size_t` / `int` in a Python hint / `String` / `Result` / `object` a primitive or a user type? | Q7, Q29, Q31, Q38 | **Built-in or standard-library types are primitive, everything else user type.** clangd marks them `defaultLibrary`; cpptools can't (limit) |
| P3 | What colour is a call through a variable (function pointer, lambda, closure)? | Q12 | **What the server says** (variable / global); function colour in mode T is a declared fallback |
| P4 | Do attributes and decorators across C, C++, Rust and Python share the directive colour, including the name inside (`packed`, `nodiscard`, `Debug`)? | Q13, Q36 | **Yes, directive** |
| P5 | Enum members and variants (`MODE_ON`, `Low`, `Some`, `None`) | Q24 | **Number/constant colour** (servers agree); mode T user-type colour for Rust variants is a fix or limit |
| P6 | Macro parameters and macro_rules metavariables | Q2 | **Parameter colour (italic)**, not macro |
| P7 | Assignment-like and flow operators: Make `:=` `?=` `+=`, Rust `=>` `?`, closure `|`, shell redirects `>` `2>&1`, `:-`, CMake `STREQUAL`, YAML `<<` | Q22, Q23, Q30, Q41, Q44, Q51, Q55, Q61 | **Quiet operator** |
| P8 | Expansion delimiters: `$(` `${` `$<` backtick `[[`, JSON key quotes, Zephyr `<` `>` | Q47, Q49, Q50, Q59, Q81 | **Variable expansions take the colour of what they wrap**: Make `$(VAR)` and CMake `${VAR}` config variable like shell `${VAR}`, genex `$<…>` hazard, JSON key quotes member. Shell command substitution `$(…)`, backticks and `[[` stay punctuation |
| P9 | Unquoted values: YAML plain scalars, INI values, CMake bare numbers and bracket arguments | Q54, Q58, Q60 | **String**, numbers **number** where the grammar can tell |
| P10 | Build-language keywords: Make `ifeq` `include` `define` `.PHONY`, Kconfig `config` `menu` `depends` `default` `help` `range`, linker `MEMORY` `SECTIONS` `ORIGIN` `ALIGN` | Q45, Q70, Q72, Q75 | **Keyword.** C `#if` stays directive because it is preprocessing; these are the build language's own statements |
| P11 | Symbols defined in build and link files: Kconfig symbols, linker symbols (`_etext`), assembly symbol references, CMake variable names in `set()` | Q48, Q68, Q76 | **Config variable**, the same as C globals and Make variables |
| P12 | Labels: C `goto` labels, Rust loop labels | Q11 | **Function, italic** (as the servers' `label` rule already does); plain in mode T is a declared fallback |
| P13 | `this` (hazard today) vs Rust/Python `self` (parameter today) | Q16 | **Parameter colour for both** |
| P14 | Upper-case constants by convention (`MAX_PINS`) | — | **Number/constant**: the grammar (`constant.other.caps`) and Pylance (`readonly`) already agree |
| P15 | Markdown: inline code number-coloured, link text user-type-coloured, bold/italic text body colour | Q65, Q66, Q67 | **Inline code string, link text body, URL user-type, bold/italic body colour** |
| P16 | Smaller ones: C++ ctor/dtor (Q18) → function; operator overload names (Q17) → function; `volatile` (Q8) → qualifier in both C and C++; `auto` (Q19) → keyword; number exponent and literal suffixes (Q14) → unit; C `#`, `##`, `defined` (Q3, Q4) → directive; `#error` text (Q5) → string; `#if 0` code (Q6) → comment; Python `cls`/`class` (Q37) per P1 | | as listed |

## 8. What happens next

1. You answer §7 (or accept the recommendations). The Role Map is then frozen and verdicts recomputed.
2. Unlock the PC: I finish calibration (Licorice, extension grammars, Pylance) and rerun rust-analyzer with the long wait.
3. I extend the corpus to 100% of reachable scope names and legend entries, then measure again. That run is the valid pass 1, and its report replaces this draft.
4. Fix CPs then go to the edit phase; design CPs wait for you.
