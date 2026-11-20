<p align="center">
  <img src="images/icon.png" width="96" alt="Rosin icon">
</p>

<h1 align="center">Rosin</h1>

<p align="center">Calm, low-glare dark themes for VS Code, where each colour keeps one meaning across languages.</p>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=debjoy-howlader.rosin-theme"><img src="https://img.shields.io/badge/VS%20Marketplace-Install-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="Install from the VS Marketplace"></a>
  <a href="https://github.com/debjoy-howlader/rosin-theme/releases/latest"><img src="https://img.shields.io/badge/Download-.vsix-C9732F?style=for-the-badge&logo=github&logoColor=white" alt="Download the .vsix"></a>
  <a href="https://github.com/debjoy-howlader/rosin-theme"><img src="https://img.shields.io/badge/GitHub-rosin--theme-24292f?style=for-the-badge&logo=github&logoColor=white" alt="View on GitHub"></a>
</p>

![Rosin flavours](images/preview.png)

## Flavours

- Rosin · Sea Salt
- Rosin · Black Cherry
- Rosin · Matcha
- Rosin · Espresso
- Rosin · Licorice
- Rosin · OLED

## Highlights

- **One meaning per colour.** A function is the function colour in C, Rust, Python, Makefiles and linker scripts alike. Where a grammar or language server can't tell two roles apart, the exception is listed under [Language support](#language-support).
- **Built for semantic highlighting.** Tuned for C/C++ IntelliSense and clangd, rust-analyzer and Pylance. With a language server running, globals, statics, parameters, methods and library calls each get their own colour.
- **Toolchains as well as languages.** Makefiles, CMake, shell, PowerShell, TOML, INI, YAML, Dockerfiles, diffs and git get the same care. Assembly, linker-script and devicetree grammars get it too, when an extension provides them.
- **Readable logs.** In `.log` files, errors, warnings, info and debug lines each get their own colour. ESP-IDF style (`E (512) tag:`) and Zephyr style (`<err>`) levels are recognised, along with panic and fault messages.
- **Contrast checked.** Body text is above WCAG AA in every flavour, while comments and punctuation are deliberately quieter.

## What each colour means

Every flavour uses the same roles. The [Colours](#colours) tables give each flavour's hex values.

| Meaning | What gets it | Examples |
|---|---|---|
| Text / variable | Local variables, and anything the grammar or server leaves unclassified | `count` `buf` |
| Keyword | Control flow, declarations, keywords that introduce a type, build-language keywords | `if` `return` `struct` `fn` `ifeq` |
| Qualifier | Storage and type qualifiers, CMake keyword arguments | `const` `static` `extern` `volatile` `PRIVATE` |
| Function | Functions you define or call; labels (italic) ¹ | `led_set()` |
| Method | Methods and member functions ¹ | `.write()` `__init__` |
| Library function | Standard-library and built-in functions ¹ | `print` `echo` `$(wildcard …)` `printf` |
| Macro (bold) | Preprocessor macros and macro calls | `LED_PIN` `BIT(n)` `__FILE__` |
| Preprocessor / attribute | Directives, attributes, decorators | `#include` `#[derive]` `@dataclass` |
| Namespace / module | Namespaces, modules and the `::` between them | `std` `core::ptr` |
| Primitive type | Built-in and standard-library types | `int` `u32` `str` `String` ¹ |
| User type | Types you define | `led_t` `Led` |
| Parameter (italic) | Parameters, `self`, `this`, macro parameters | `len` `self` `$x` |
| Member / key / flag | Fields, config keys, command-line flags | `.pin` `name:` `--baud` |
| Global / config variable | Global variables ¹, build and environment variables, linker symbols | `g_ticks` `$(CC)` `${BOARD}` `_etext` |
| Static variable | File- and function-scope statics ¹ | `s_state` |
| Number / constant / enum | Numbers, booleans, null values, enum members | `42` `true` `None` `Some` |
| Unit | Number base prefixes, suffixes and exponents; literal suffixes | `0x` `UL` `e-3` `_ms` |
| String | Strings and unquoted config values | `"hello"` |
| Escape | Escape sequences and entities | `\n` `&amp;` |
| Hazard | Pointers, bit operations, format specifiers | `*p` `->` `<<` `%d` |
| Operator | Assignment, arithmetic and comparison operators | `=` `+` `==` |
| Punctuation | Separators, brackets, string quotes | `;` `,` `{}` |
| Comment (italic) | Comments | `// note` |
| Doc comment (italic) | Documentation comments | `/// returns` |
| Error / warning | Log levels, unresolved names | `ERROR` `WARN` |
| Diff added / removed | Diff lines | `+` / `-` |

¹ In some languages only a language server can tell these apart from an ordinary function, variable or type. The sections under [Language support](#language-support) say which, and what you see without one.

## Colours

<!-- colours:start -->
### Rosin · Sea Salt

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#13171F](images/swatches/13171f.png) | Editor background |  | `#13171F` |
| ![#0D1117](images/swatches/0d1117.png) | Panels / sidebar |  | `#0D1117` |
| ![#333A5F](images/swatches/333a5f.png) | Selection |  | `#333A5F` |
| ![#AEA7ED](images/swatches/aea7ed.png) | UI accent |  | `#AEA7ED` |
| ![#C6CDD4](images/swatches/c6cdd4.png) | Text / variable | `count` `buf` | `#C6CDD4` |
| ![#E59B5B](images/swatches/e59b5b.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#E59B5B` |
| ![#9CADCB](images/swatches/9cadcb.png) | Qualifier | `const` `static` `extern` | `#9CADCB` |
| ![#B5A4FF](images/swatches/b5a4ff.png) | Function | `led_set()` | `#B5A4FF` |
| ![#C0B2FF](images/swatches/c0b2ff.png) | Method | `.write()` | `#C0B2FF` |
| ![#8D96BE](images/swatches/8d96be.png) | Library / builtin function | `print` `echo` `printf` | `#8D96BE` |
| ![#E497CE](images/swatches/e497ce.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#E497CE` |
| ![#AB81AD](images/swatches/ab81ad.png) | Preprocessor / attribute | `#include` `#[derive]` | `#AB81AD` |
| ![#6F9895](images/swatches/6f9895.png) | Namespace / module | `std` `core::ptr` | `#6F9895` |
| ![#5EA0CD](images/swatches/5ea0cd.png) | Primitive type | `int` `u32` `str` | `#5EA0CD` |
| ![#75CCC4](images/swatches/75ccc4.png) | User type | `led_t` `Led` | `#75CCC4` |
| ![#C2B7DB](images/swatches/c2b7db.png) | Parameter / self (italic) | `len` `self` | `#C2B7DB` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEAF97](images/swatches/deaf97.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEAF97` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#D5C984](images/swatches/d5c984.png) | Number / constant / enum | `42` `true` `None` | `#D5C984` |
| ![#AEA581](images/swatches/aea581.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#AEA581` |
| ![#75C290](images/swatches/75c290.png) | String | `"hello"` | `#75C290` |
| ![#CB8871](images/swatches/cb8871.png) | Escape | `\n` `&amp;` | `#CB8871` |
| ![#E2726B](images/swatches/e2726b.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#E2726B` |
| ![#8A939E](images/swatches/8a939e.png) | Operator | `=` `+` `==` | `#8A939E` |
| ![#6A727D](images/swatches/6a727d.png) | Punctuation | `;` `,` `{}` | `#6A727D` |
| ![#7A8696](images/swatches/7a8696.png) | Comment (italic) | `// note` | `#7A8696` |
| ![#AE9B7F](images/swatches/ae9b7f.png) | Doc comment (italic) | `/// returns` | `#AE9B7F` |
| ![#E97074](images/swatches/e97074.png) | Error / log error | `ERROR` | `#E97074` |
| ![#E59B5B](images/swatches/e59b5b.png) | Warning / log warning | `WARN` | `#E59B5B` |
| ![#75C290](images/swatches/75c290.png) ![#E97074](images/swatches/e97074.png) | Diff added / removed | `+` / `-` | `#75C290` `#E97074` |

### Rosin · Black Cherry

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#1E131A](images/swatches/1e131a.png) | Editor background |  | `#1E131A` |
| ![#160E13](images/swatches/160e13.png) | Panels / sidebar |  | `#160E13` |
| ![#462D4B](images/swatches/462d4b.png) | Selection |  | `#462D4B` |
| ![#C28DD7](images/swatches/c28dd7.png) | UI accent |  | `#C28DD7` |
| ![#D4C8CF](images/swatches/d4c8cf.png) | Text / variable | `count` `buf` | `#D4C8CF` |
| ![#DB7489](images/swatches/db7489.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#DB7489` |
| ![#A1ABCC](images/swatches/a1abcc.png) | Qualifier | `const` `static` `extern` | `#A1ABCC` |
| ![#DAB663](images/swatches/dab663.png) | Function | `led_set()` | `#DAB663` |
| ![#DCC27B](images/swatches/dcc27b.png) | Method | `.write()` | `#DCC27B` |
| ![#AA966E](images/swatches/aa966e.png) | Library / builtin function | `print` `echo` `printf` | `#AA966E` |
| ![#D297E5](images/swatches/d297e5.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#D297E5` |
| ![#A184BB](images/swatches/a184bb.png) | Preprocessor / attribute | `#include` `#[derive]` | `#A184BB` |
| ![#6F9896](images/swatches/6f9896.png) | Namespace / module | `std` `core::ptr` | `#6F9896` |
| ![#649FCB](images/swatches/649fcb.png) | Primitive type | `int` `u32` `str` | `#649FCB` |
| ![#74CCCB](images/swatches/74cccb.png) | User type | `led_t` `Led` | `#74CCCB` |
| ![#C1B7DC](images/swatches/c1b7dc.png) | Parameter / self (italic) | `len` `self` | `#C1B7DC` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEB49B](images/swatches/deb49b.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEB49B` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#ECB0C6](images/swatches/ecb0c6.png) | Number / constant / enum | `42` `true` `None` | `#ECB0C6` |
| ![#B693A0](images/swatches/b693a0.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#B693A0` |
| ![#79C49C](images/swatches/79c49c.png) | String | `"hello"` | `#79C49C` |
| ![#C89164](images/swatches/c89164.png) | Escape | `\n` `&amp;` | `#C89164` |
| ![#E3814A](images/swatches/e3814a.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#E3814A` |
| ![#9D8C97](images/swatches/9d8c97.png) | Operator | `=` `+` `==` | `#9D8C97` |
| ![#7C6C76](images/swatches/7c6c76.png) | Punctuation | `;` `,` `{}` | `#7C6C76` |
| ![#957D8C](images/swatches/957d8c.png) | Comment (italic) | `// note` | `#957D8C` |
| ![#B39982](images/swatches/b39982.png) | Doc comment (italic) | `/// returns` | `#B39982` |
| ![#E97074](images/swatches/e97074.png) | Error / log error | `ERROR` | `#E97074` |
| ![#DAB663](images/swatches/dab663.png) | Warning / log warning | `WARN` | `#DAB663` |
| ![#79C49C](images/swatches/79c49c.png) ![#E97074](images/swatches/e97074.png) | Diff added / removed | `+` / `-` | `#79C49C` `#E97074` |

### Rosin · Matcha

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#141A17](images/swatches/141a17.png) | Editor background |  | `#141A17` |
| ![#0E1210](images/swatches/0e1210.png) | Panels / sidebar |  | `#0E1210` |
| ![#374831](images/swatches/374831.png) | Selection |  | `#374831` |
| ![#9CC97A](images/swatches/9cc97a.png) | UI accent |  | `#9CC97A` |
| ![#CBD4CB](images/swatches/cbd4cb.png) | Text / variable | `count` `buf` | `#CBD4CB` |
| ![#E8A0AA](images/swatches/e8a0aa.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#E8A0AA` |
| ![#A2B8AE](images/swatches/a2b8ae.png) | Qualifier | `const` `static` `extern` | `#A2B8AE` |
| ![#A8D17E](images/swatches/a8d17e.png) | Function | `led_set()` | `#A8D17E` |
| ![#B8DA92](images/swatches/b8da92.png) | Method | `.write()` | `#B8DA92` |
| ![#93A88C](images/swatches/93a88c.png) | Library / builtin function | `print` `echo` `printf` | `#93A88C` |
| ![#DFA2D6](images/swatches/dfa2d6.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#DFA2D6` |
| ![#B49AC0](images/swatches/b49ac0.png) | Preprocessor / attribute | `#include` `#[derive]` | `#B49AC0` |
| ![#73A08E](images/swatches/73a08e.png) | Namespace / module | `std` `core::ptr` | `#73A08E` |
| ![#7FB8D6](images/swatches/7fb8d6.png) | Primitive type | `int` `u32` `str` | `#7FB8D6` |
| ![#7CCBB4](images/swatches/7ccbb4.png) | User type | `led_t` `Led` | `#7CCBB4` |
| ![#C8BFDA](images/swatches/c8bfda.png) | Parameter / self (italic) | `len` `self` | `#C8BFDA` |
| ![#A3B9C8](images/swatches/a3b9c8.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#A3B9C8` |
| ![#E2C39E](images/swatches/e2c39e.png) | Global / config variable | `g_ticks` `$(CC)` | `#E2C39E` |
| ![#B9D0A8](images/swatches/b9d0a8.png) | Static variable | `s_state` | `#B9D0A8` |
| ![#B9B8EE](images/swatches/b9b8ee.png) | Number / constant / enum | `42` `true` `None` | `#B9B8EE` |
| ![#B9A08A](images/swatches/b9a08a.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#B9A08A` |
| ![#D8C38A](images/swatches/d8c38a.png) | String | `"hello"` | `#D8C38A` |
| ![#D9A274](images/swatches/d9a274.png) | Escape | `\n` `&amp;` | `#D9A274` |
| ![#E57A6E](images/swatches/e57a6e.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#E57A6E` |
| ![#8E9C92](images/swatches/8e9c92.png) | Operator | `=` `+` `==` | `#8E9C92` |
| ![#6C796F](images/swatches/6c796f.png) | Punctuation | `;` `,` `{}` | `#6C796F` |
| ![#7E8D82](images/swatches/7e8d82.png) | Comment (italic) | `// note` | `#7E8D82` |
| ![#AEA382](images/swatches/aea382.png) | Doc comment (italic) | `/// returns` | `#AEA382` |
| ![#EC7A7A](images/swatches/ec7a7a.png) | Error / log error | `ERROR` | `#EC7A7A` |
| ![#E0B070](images/swatches/e0b070.png) | Warning / log warning | `WARN` | `#E0B070` |
| ![#8CCB86](images/swatches/8ccb86.png) ![#EC7A7A](images/swatches/ec7a7a.png) | Diff added / removed | `+` / `-` | `#8CCB86` `#EC7A7A` |

### Rosin · Espresso

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#1B1714](images/swatches/1b1714.png) | Editor background |  | `#1B1714` |
| ![#12100E](images/swatches/12100e.png) | Panels / sidebar |  | `#12100E` |
| ![#4C3B27](images/swatches/4c3b27.png) | Selection |  | `#4C3B27` |
| ![#D9A15E](images/swatches/d9a15e.png) | UI accent |  | `#D9A15E` |
| ![#DDD2C6](images/swatches/ddd2c6.png) | Text / variable | `count` `buf` | `#DDD2C6` |
| ![#DE8C6C](images/swatches/de8c6c.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#DE8C6C` |
| ![#B5ACBA](images/swatches/b5acba.png) | Qualifier | `const` `static` `extern` | `#B5ACBA` |
| ![#E8B565](images/swatches/e8b565.png) | Function | `led_set()` | `#E8B565` |
| ![#EEC47F](images/swatches/eec47f.png) | Method | `.write()` | `#EEC47F` |
| ![#B59D7A](images/swatches/b59d7a.png) | Library / builtin function | `print` `echo` `printf` | `#B59D7A` |
| ![#DA9DC6](images/swatches/da9dc6.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#DA9DC6` |
| ![#BB91AC](images/swatches/bb91ac.png) | Preprocessor / attribute | `#include` `#[derive]` | `#BB91AC` |
| ![#8AA59C](images/swatches/8aa59c.png) | Namespace / module | `std` `core::ptr` | `#8AA59C` |
| ![#8DB2CD](images/swatches/8db2cd.png) | Primitive type | `int` `u32` `str` | `#8DB2CD` |
| ![#86C2B2](images/swatches/86c2b2.png) | User type | `led_t` `Led` | `#86C2B2` |
| ![#CEC0D8](images/swatches/cec0d8.png) | Parameter / self (italic) | `len` `self` | `#CEC0D8` |
| ![#AABAC5](images/swatches/aabac5.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#AABAC5` |
| ![#E7C4A1](images/swatches/e7c4a1.png) | Global / config variable | `g_ticks` `$(CC)` | `#E7C4A1` |
| ![#BDC9A5](images/swatches/bdc9a5.png) | Static variable | `s_state` | `#BDC9A5` |
| ![#C7B5E4](images/swatches/c7b5e4.png) | Number / constant / enum | `42` `true` `None` | `#C7B5E4` |
| ![#BEA18A](images/swatches/bea18a.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#BEA18A` |
| ![#A9C48E](images/swatches/a9c48e.png) | String | `"hello"` | `#A9C48E` |
| ![#D8A26C](images/swatches/d8a26c.png) | Escape | `\n` `&amp;` | `#D8A26C` |
| ![#E3785E](images/swatches/e3785e.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#E3785E` |
| ![#A2968C](images/swatches/a2968c.png) | Operator | `=` `+` `==` | `#A2968C` |
| ![#7C7066](images/swatches/7c7066.png) | Punctuation | `;` `,` `{}` | `#7C7066` |
| ![#918376](images/swatches/918376.png) | Comment (italic) | `// note` | `#918376` |
| ![#B7A487](images/swatches/b7a487.png) | Doc comment (italic) | `/// returns` | `#B7A487` |
| ![#EA7070](images/swatches/ea7070.png) | Error / log error | `ERROR` | `#EA7070` |
| ![#E3C46F](images/swatches/e3c46f.png) | Warning / log warning | `WARN` | `#E3C46F` |
| ![#9AC68C](images/swatches/9ac68c.png) ![#EA7070](images/swatches/ea7070.png) | Diff added / removed | `+` / `-` | `#9AC68C` `#EA7070` |

### Rosin · Licorice

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#121314](images/swatches/121314.png) | Editor background |  | `#121314` |
| ![#0C0D0E](images/swatches/0c0d0e.png) | Panels / sidebar |  | `#0C0D0E` |
| ![#2A3540](images/swatches/2a3540.png) | Selection |  | `#2A3540` |
| ![#94B9DA](images/swatches/94b9da.png) | UI accent |  | `#94B9DA` |
| ![#CACCCE](images/swatches/caccce.png) | Text / variable | `count` `buf` | `#CACCCE` |
| ![#8E9296](images/swatches/8e9296.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#8E9296` |
| ![#868A8E](images/swatches/868a8e.png) | Qualifier | `const` `static` `extern` | `#868A8E` |
| ![#94B9DA](images/swatches/94b9da.png) | Function | `led_set()` | `#94B9DA` |
| ![#A7C6E2](images/swatches/a7c6e2.png) | Method | `.write()` | `#A7C6E2` |
| ![#8FA2B5](images/swatches/8fa2b5.png) | Library / builtin function | `print` `echo` `printf` | `#8FA2B5` |
| ![#E4E6E8](images/swatches/e4e6e8.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#E4E6E8` |
| ![#808488](images/swatches/808488.png) | Preprocessor / attribute | `#include` `#[derive]` | `#808488` |
| ![#7F8387](images/swatches/7f8387.png) | Namespace / module | `std` `core::ptr` | `#7F8387` |
| ![#A6AAAE](images/swatches/a6aaae.png) | Primitive type | `int` `u32` `str` | `#A6AAAE` |
| ![#D6D8DA](images/swatches/d6d8da.png) | User type | `led_t` `Led` | `#D6D8DA` |
| ![#B9BCBF](images/swatches/b9bcbf.png) | Parameter / self (italic) | `len` `self` | `#B9BCBF` |
| ![#B3B6B9](images/swatches/b3b6b9.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#B3B6B9` |
| ![#E8E9EA](images/swatches/e8e9ea.png) | Global / config variable | `g_ticks` `$(CC)` | `#E8E9EA` |
| ![#C0C3C6](images/swatches/c0c3c6.png) | Static variable | `s_state` | `#C0C3C6` |
| ![#DDDFE1](images/swatches/dddfe1.png) | Number / constant / enum | `42` `true` `None` | `#DDDFE1` |
| ![#A3A6A9](images/swatches/a3a6a9.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#A3A6A9` |
| ![#A7BDA2](images/swatches/a7bda2.png) | String | `"hello"` | `#A7BDA2` |
| ![#C3C7CA](images/swatches/c3c7ca.png) | Escape | `\n` `&amp;` | `#C3C7CA` |
| ![#D9827A](images/swatches/d9827a.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#D9827A` |
| ![#8A8E92](images/swatches/8a8e92.png) | Operator | `=` `+` `==` | `#8A8E92` |
| ![#66696D](images/swatches/66696d.png) | Punctuation | `;` `,` `{}` | `#66696D` |
| ![#7A7E82](images/swatches/7a7e82.png) | Comment (italic) | `// note` | `#7A7E82` |
| ![#8F9397](images/swatches/8f9397.png) | Doc comment (italic) | `/// returns` | `#8F9397` |
| ![#D9827A](images/swatches/d9827a.png) | Error / log error | `ERROR` | `#D9827A` |
| ![#C9A66B](images/swatches/c9a66b.png) | Warning / log warning | `WARN` | `#C9A66B` |
| ![#9CB896](images/swatches/9cb896.png) ![#D9827A](images/swatches/d9827a.png) | Diff added / removed | `+` / `-` | `#9CB896` `#D9827A` |

### Rosin · OLED

| | Meaning | Example | Hex |
|:-:|---|---|---|
| ![#000000](images/swatches/000000.png) | Editor background |  | `#000000` |
| ![#000000](images/swatches/000000.png) | Panels / sidebar |  | `#000000` |
| ![#2A2840](images/swatches/2a2840.png) | Selection |  | `#2A2840` |
| ![#AEA7ED](images/swatches/aea7ed.png) | UI accent |  | `#AEA7ED` |
| ![#C6CDD4](images/swatches/c6cdd4.png) | Text / variable | `count` `buf` | `#C6CDD4` |
| ![#E59B5B](images/swatches/e59b5b.png) | Keyword / control flow | `if` `return` `struct` `fn` | `#E59B5B` |
| ![#9CADCB](images/swatches/9cadcb.png) | Qualifier | `const` `static` `extern` | `#9CADCB` |
| ![#B5A4FF](images/swatches/b5a4ff.png) | Function | `led_set()` | `#B5A4FF` |
| ![#C0B2FF](images/swatches/c0b2ff.png) | Method | `.write()` | `#C0B2FF` |
| ![#8D96BE](images/swatches/8d96be.png) | Library / builtin function | `print` `echo` `printf` | `#8D96BE` |
| ![#E497CE](images/swatches/e497ce.png) | Macro (bold) | `LED_PIN` `BIT(n)` | `#E497CE` |
| ![#AB81AD](images/swatches/ab81ad.png) | Preprocessor / attribute | `#include` `#[derive]` | `#AB81AD` |
| ![#6F9895](images/swatches/6f9895.png) | Namespace / module | `std` `core::ptr` | `#6F9895` |
| ![#5EA0CD](images/swatches/5ea0cd.png) | Primitive type | `int` `u32` `str` | `#5EA0CD` |
| ![#75CCC4](images/swatches/75ccc4.png) | User type | `led_t` `Led` | `#75CCC4` |
| ![#C2B7DB](images/swatches/c2b7db.png) | Parameter / self (italic) | `len` `self` | `#C2B7DB` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEAF97](images/swatches/deaf97.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEAF97` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#D5C984](images/swatches/d5c984.png) | Number / constant / enum | `42` `true` `None` | `#D5C984` |
| ![#AEA581](images/swatches/aea581.png) | Unit: number prefix / suffix | `0x` `UL` `_ms` | `#AEA581` |
| ![#75C290](images/swatches/75c290.png) | String | `"hello"` | `#75C290` |
| ![#CB8871](images/swatches/cb8871.png) | Escape | `\n` `&amp;` | `#CB8871` |
| ![#E2726B](images/swatches/e2726b.png) | Hazard: pointer / bits / format | `*` `->` `<<` `%d` | `#E2726B` |
| ![#8A939E](images/swatches/8a939e.png) | Operator | `=` `+` `==` | `#8A939E` |
| ![#6A727D](images/swatches/6a727d.png) | Punctuation | `;` `,` `{}` | `#6A727D` |
| ![#7A8696](images/swatches/7a8696.png) | Comment (italic) | `// note` | `#7A8696` |
| ![#AE9B7F](images/swatches/ae9b7f.png) | Doc comment (italic) | `/// returns` | `#AE9B7F` |
| ![#E97074](images/swatches/e97074.png) | Error / log error | `ERROR` | `#E97074` |
| ![#E59B5B](images/swatches/e59b5b.png) | Warning / log warning | `WARN` | `#E59B5B` |
| ![#75C290](images/swatches/75c290.png) ![#E97074](images/swatches/e97074.png) | Diff added / removed | `+` / `-` | `#75C290` `#E97074` |

<!-- colours:end -->

## Language support

Each language below was checked token by token, with and without its language server. A few constructs can't be coloured by their meaning, because the grammar or the server gives them exactly the same label as something else. Those exceptions are listed per language and per setup: pick the heading that matches the language server you have installed (or none), and that list is complete for it.

<!-- languages:start -->
### C and C++

- **Grammar:** built in.
- **Recommended:** C/C++ (`ms-vscode.cpptools`) 1.35.6; or clangd (`llvm-vs-code-extensions.vscode-clangd`) 0.6.0 with clangd 23.1.0.
- **Checked tokens shown as designed:** 298 of 368 without a language server; 312 of 368 with cpptools; 318 of 368 with clangd.
- Use one server or the other. clangd tells more roles apart: library functions, deduced types, concepts and file-scope statics. The two servers label a few tokens differently, so those tokens change colour when you switch. The servers were tested with `"C_Cpp.enhancedColorization": "enabled"` (the default).

Pick the line that matches what you have installed. Each list is complete for that setup.

<details>
<summary><b>Neither cpptools nor clangd</b>: 70 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `else_branch` | comment | text | the grammar scopes it exactly like `u8_custom` (user type). |
| `fail` | function | text | asm goto label operand gets only meta.function-call.c. |
| `done`, `out`, `retry` | function | text | only a language server can tell. |
| `V` | function | text | the grammar scopes it exactly like `Led2` (user type). |
| `Led2` | function | text | the grammar scopes it exactly like the user type `Led2` elsewhere in the file. |
| `callback` | global / config variable | function | only a language server can tell. |
| `g_ticks`, `callback`, `REG_CTRL`, `fp2` | global / config variable | text | only a language server can tell. |
| `*`, `&`, `~`, `^`, `\|` | hazard | operator | the grammar scopes it exactly like `+` (operator). |
| `*` | hazard | operator | unary `*` (deref) and binary `*` (multiply) share keyword.operator.arithmetic.cpp. |
| `\|=` | hazard | two colours | the C++ grammar scopes `\|` of `\|=` as a bitwise operator and `=` as assignment, so the compound operator is half hazard, half quiet (clangd colours it whole). |
| `static_assert`, `typeof` | keyword | function | the grammar scopes it exactly like `BIT` (macro). |
| `_Static_assert` | keyword | function | the grammar scopes it exactly like `add` (function). |
| `auto` | keyword | primitive type | `auto` has the same scope as `void`, `int` (storage.type.built-in.primitive.cpp). clangd fixes it with type.deduced. |
| `alignas` | keyword | punctuation | `alignas` is scoped as the opening punctuation of an attribute, same as `[[`. |
| `printf`, `memcpy` | library function | function | the grammar scopes it exactly like `BIT` (macro). |
| `BIT` | macro | function | the grammar scopes it exactly like `printf` (library function). |
| `NULL` | macro | number / constant | `NULL` and `true` share constant.language.c. |
| `cb` | member / key | function | only a language server can tell. |
| `v` | member / key | function | the grammar scopes it exactly like `Led2` (function). |
| `v` | member / key | text | `int v = 0;` in a class body has the same scope as an assignment to a local variable. |
| `pin`, `reg`, `flag` | member / key | text | the grammar scopes it exactly like `MODE_OFF` (number / constant). |
| `on`, `get` | method | function | only a language server can tell. |
| `hal` | namespace | text | `hal` in `hal::init()` gets entity.name.scope-resolution.cpp, the scope the grammar also gives enum types, class names and destructor owners. |
| `k_max` | number / constant | text | only a language server can tell. |
| `On` | number / constant | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role. |
| `MODE_ON` | number / constant | text | the grammar scopes it exactly like `...` (punctuation). |
| `MODE_OFF` | number / constant | text | the grammar scopes it exactly like `pin` (member / key). |
| `fp` | parameter | function | only a language server can tell. |
| `n` | parameter | preprocessor / attribute | the grammar scopes it exactly like `##` (preprocessor / attribute). |
| `a` | parameter | text | only a language server can tell. |
| `x` | parameter | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role. |
| `__attribute__` | preprocessor / attribute | function | the grammar scopes it exactly like `add` (function). |
| `...` | punctuation | text | `...` in a parameter list gets only meta.function.definition.parameters. |
| `...` | punctuation | text | the grammar scopes it exactly like `MODE_ON` (number / constant). |
| `_Noreturn` | qualifier | text | the grammar scopes it exactly like `pin` (member / key). |
| `s_count` | static variable | text | only a language server can tell. |
| `count` | static variable | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role. |
| `u8` | string | text | the grammar scopes it exactly like `u8_custom` (user type). |
| `twice` | text | function | only a language server can tell. |
| `led2_t` | user type | primitive type | any name ending in `_t` gets support.type.posix-reserved.cpp, so a user typedef `led2_t` looks like `pid_t`. Servers fix it. |
| `Led2` | user type | text | `Led2::Led2()` is scoped as a qualified call (entity.name.scope-resolution.function.call.cpp), the same as `ns::f()`. |
| `Base` | user type | text | base class name in `struct D : Base` gets only meta.head.struct.cpp. |
| `Mode` | user type | text | entity.name.scope-resolution.cpp covers enum types, namespaces and destructor owners alike. |
| `Small` | user type | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role (clangd fixes it with concept). |
| `Led2`, `Box2` | user type | text | the grammar scopes it exactly like `V` (function). |
| `u8_custom`, `led`, `mode` | user type | text | the grammar scopes it exactly like `s_count` (static variable). |

</details>

<details>
<summary><b>With cpptools</b>: 55 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `else_branch` | comment | text | the grammar scopes it exactly like `u8` (string). |
| `operator` | function | keyword | the server labels it exactly like `new` (keyword). |
| `operator==`, `operator+` | function | library function | cpptools gives operator-overload declarations and overloaded operator uses the same type with no modifiers; uses keep the library-function colour. |
| `f` | function | method | cpptools calls `V::f()` a static method; clangd a function. |
| `Led`, `V`, `Led2` | function | method | the server labels it exactly like `on` (method). |
| `operator""`, `_ms` | function | unit | the server labels it exactly like `250` (number / constant). |
| `V`, `Led2` | function | user type | the server labels it exactly like `T` (primitive type). |
| `*`, `&`, `~`, `^`, `\|` | hazard | operator | the grammar scopes it exactly like `+` (operator). |
| `*` | hazard | operator | unary `*` (deref) and binary `*` (multiply) share keyword.operator.arithmetic.cpp. |
| `\|=` | hazard | two colours | the C++ grammar scopes `\|` of `\|=` as a bitwise operator and `=` as assignment, so the compound operator is half hazard, half quiet (clangd colours it whole). |
| `static_assert`, `typeof` | keyword | function | cpptools and clangd emit no semantic token for `static_assert` / `typeof`; the TextMate fallback is the function-call scope. |
| `_Static_assert` | keyword | function | the grammar scopes it exactly like `__attribute__` (preprocessor / attribute). |
| `auto` | keyword | primitive type | `auto` has the same scope as `void`, `int` (storage.type.built-in.primitive.cpp). clangd fixes it with type.deduced. |
| `alignas` | keyword | punctuation | `alignas` is scoped as the opening punctuation of an attribute, same as `[[`. |
| `printf`, `memcpy` | library function | function | the server labels it exactly like `add` (function). |
| `k_max` | number / constant | global / config variable | the server labels it exactly like `s_count` (static variable). |
| `true` | number / constant | macro | the server labels it exactly like `LED_PIN` (macro). |
| `250` | number / constant | unit | the server labels it exactly like `operator""` (function). |
| `n` | parameter | member / key | the server labels it exactly like `pin_` (member / key). |
| `n` | parameter | preprocessor / attribute | the grammar scopes it exactly like `##` (preprocessor / attribute). |
| `x` | parameter | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role. |
| `x` | parameter | text | the server labels it exactly like `i` (text). |
| `__attribute__` | preprocessor / attribute | function | the grammar scopes it exactly like `_Static_assert` (keyword). |
| `bool` | primitive type | macro | the server labels it exactly like `LED_PIN` (macro). |
| `T` | primitive type | user type | the server labels it exactly like `Led` (user type). |
| `pid_t` | primitive type | user type | the server labels it exactly like `T` (primitive type). |
| `uint8_t`, `size_t`, `pthread_t`, `int8_t`, `uintptr_t`, `ssize_t` | primitive type | user type | the server labels it exactly like `u8_custom` (user type). |
| `...` | punctuation | text | GNU case range `...` gets only meta.conditional.case.c. |
| `...` | punctuation | text | `...` in a parameter list gets only meta.function.definition.parameters. |
| `_Noreturn` | qualifier | text | `_Noreturn` gets only meta.block.c. |
| `s_count` | static variable | global / config variable | the server labels it exactly like `g_ticks` (global / config variable). |
| `u8` | string | text | the grammar scopes it exactly like `else_branch` (comment). |
| `twice` | text | function | cpptools calls a lambda through a variable a function; clangd calls it a variable. |

</details>

<details>
<summary><b>With clangd</b>: 50 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `else_branch` | comment | text | the grammar scopes it exactly like `u8` (string). |
| `fail` | function | text | asm goto label operand gets only meta.function-call.c. |
| `operator==`, `operator+` | function | two colours | clangd marks only the word `operator` as the function; the operator symbols keep the grammar colour. |
| `V`, `Led2` | function | user type | the server labels it exactly like `Led` (user type). |
| `*` | hazard | operator | pointer declarator `*` shares keyword.operator.c with multiply; clangd sends no token for it. |
| `&`, `*`, `\|=`, `~`, `^`, `<<=`, `&=`, `>>=`, `\|` | hazard | operator | the server labels it exactly like `+` (operator). |
| `&`, `\|`, `^`, `~`, `<<`, `\|=`, `*` | hazard | operator | the server labels it exactly like `new` (keyword). |
| `static_assert`, `typeof` | keyword | function | cpptools and clangd emit no semantic token for `static_assert` / `typeof`; the TextMate fallback is the function-call scope. |
| `_Static_assert` | keyword | function | the grammar scopes it exactly like `__attribute__` (preprocessor / attribute). |
| `new`, `delete`, `?`, `&&` | keyword | operator | the server labels it exactly like `&` (hazard). |
| `!`, `?` | keyword | operator | the server labels it exactly like `+` (operator). |
| `auto` | keyword | primitive type | clangd emits no token for `auto` when the deduced type is a lambda (`auto twice = [&](int x) {...}`), so the grammar's primitive-type scope shows; for other deduced types clangd's type.deduced fixes it. |
| `alignas` | keyword | punctuation | `alignas` is scoped as the opening punctuation of an attribute, same as `[[`. |
| `true` | number / constant | macro | the server labels it exactly like `DEBUG` (macro). |
| `n` | parameter | preprocessor / attribute | the grammar scopes it exactly like `##` (preprocessor / attribute). |
| `x` | parameter | text | the grammar puts the name itself in the scope (variable.other.unknown.&lt;name&gt;), so no rule can match the role. |
| `n` | parameter | text | the server labels it exactly like `i` (text). |
| `x` | parameter | text | the server labels it exactly like `twice` (text). |
| `__attribute__` | preprocessor / attribute | function | the grammar scopes it exactly like `_Static_assert` (keyword). |
| `bool` | primitive type | macro | the server labels it exactly like `DEBUG` (macro). |
| `...` | punctuation | text | GNU case range `...` gets only meta.conditional.case.c. |
| `...` | punctuation | text | `...` in a parameter list gets only meta.function.definition.parameters. |
| `_Noreturn` | qualifier | text | `_Noreturn` gets only meta.block.c. |
| `u8` | string | text | the grammar scopes it exactly like `else_branch` (comment). |

</details>

### Rust

- **Grammar:** built in.
- **Recommended:** rust-analyzer (`rust-lang.rust-analyzer`) 0.3.3121.
- **Checked tokens shown as designed:** 93 of 118 without a language server; 102 of 118 with rust-analyzer.
- rust-analyzer could not resolve standard-library macros such as `println!` and `write!` on Rust 1.93.1. Rosin shows unresolved names in the error style (red, bold, underlined), so these calls look like errors. This is a toolchain problem, not a theme rule; it goes away when rust-analyzer can resolve the standard library.

Pick the line that matches what you have installed. Each list is complete for that setup.

<details>
<summary><b>Without rust-analyzer</b>: 25 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `Corpus` | doc comment | comment | `//!` inner doc comments get comment.line.double-slash.rust, same as `//` (grammar source). |
| `'outer` | function | primitive type | the grammar scopes it exactly like `'a` (primitive type). |
| `unsafe` | hazard | keyword | the grammar scopes it exactly like `impl` (keyword). |
| `^=` | hazard | operator | rust-analyzer marks every compound assignment (`+=`, `^=`) operator.mutable; without it `^=` shares keyword.operator.assignment.rust with `=`. |
| `new`, `len` | library function | function | only a language server can tell. |
| `id` | member / key | text | Rust field access is unscoped (rust-analyzer fixes it). |
| `id` | member / key | text | the grammar scopes it exactly like `name` (text). |
| `toggle` | method | function | only a language server can tell. |
| `fmt` | namespace | text | module names in use paths get only meta.use.rust (rust-analyzer fixes it). |
| `Low` | number / constant | user type | the grammar scopes it exactly like `T` (primitive type). |
| `\|` | operator | keyword | closure `\|` shares keyword.operator.logical.rust with `^ \|\| && << >> !` (grammar source). |
| `addr` | parameter | text | parameters, fields and locals share variable.other.rust without rust-analyzer. |
| `x` | parameter | text | the grammar scopes it exactly like `id` (member / key). |
| `Debug` | preprocessor / attribute | user type | entity.name.type.rust covers derive items, user types, std types, generics. |
| `Result`, `String` | primitive type | user type | only a language server can tell. |
| `T` | primitive type | user type | the grammar scopes it exactly like `Low` (number / constant). |
| `TICKS` | static variable | number / constant | the grammar scopes it exactly like `CTRL` (number / constant). |
| `twice` | text | function | only a language server can tell. |

</details>

<details>
<summary><b>With rust-analyzer</b>: 16 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `*` | hazard | keyword | the server labels it exactly like `use` (keyword). |
| `^=` | hazard | operator | rust-analyzer marks every compound assignment (`+=`, `^=`) operator.mutable; without it `^=` shares keyword.operator.assignment.rust with `=`. |
| `&` | hazard | operator | the server labels it exactly like `::` (namespace). |
| `{}`, `{name}` | hazard | string | the server labels it exactly like `pin` (string). |
| `write`, `println` | macro | error | `println!` / `write!` unresolved; Rosin shows unresolvedReference as error. |
| `::` | namespace | operator | the server labels it exactly like `&` (hazard). |
| `\|` | operator | keyword | closure `\|` shares keyword.operator.logical.rust with `^ \|\| && << >> !` (grammar source). |
| `pub`, `mut` | qualifier | keyword | the server labels it exactly like `use` (keyword). |
| `u8`, `e`, `-` | unit | number / constant | the server labels it exactly like `7` (number / constant). |

</details>

### Python

- **Grammar:** built in.
- **Recommended:** Pylance (`ms-python.vscode-pylance`) 2026.4.1, with Python (`ms-python.python`) 2026.10.0.
- **Checked tokens shown as designed:** 83 of 93 without a language server; 92 of 93 with Pylance.
- Pylance brings its own grammar as well as semantic tokens, so "without a language server" here means without Pylance.

Pick the line that matches what you have installed. Each list is complete for that setup.

<details>
<summary><b>Without Pylance</b>: 10 exceptions</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `(?P<` | hazard | two colours | the regex grammar splits a named group opener `(?P<` into punctuation and a group-name scope. |
| `dataclass` | library function | text | the grammar scopes it exactly like `os` (namespace). |
| `number` | member / key | text | attribute access without Pylance gets only meta.attribute.python. |
| `number` | member / key | text | only a language server can tell. |
| `write` | method | function | library method calls and plain calls share meta.function-call.generic.python without Pylance. |
| `make` | method | function | only a language server can tell. |
| `os`, `dataclasses` | namespace | text | the grammar scopes it exactly like `dataclass` (library function). |
| `f` | text | function | only a language server can tell. |

</details>

<details>
<summary><b>With Pylance</b>: 1 exception</summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `(?P<` | hazard | two colours | the regex grammar splits a named group opener `(?P<` into punctuation and a group-name scope. |

</details>

### Shell (bash)

- **Grammar:** built in.
- **Checked tokens shown as designed:** 87 of 98 as tested.
- Tested with Bash IDE (`mads-hartmann.bash-ide-vscode`) 1.43.2 installed. It provides no semantic tokens, so colours are the same with or without it.

<details>
<summary><b>11 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `\x41`, `\033` | escape | string | escapes inside bash $'...' strings are not tokenized. |
| `@` | hazard | operator | the grammar scopes it exactly like `:-` (operator). |
| `@(` | hazard | two colours | the bash grammar does not recognise extglob `@(...)`; `@` is plain text and `(` punctuation. |
| `\|\|` | keyword | operator | the grammar scopes it exactly like `\|` (operator). |
| `-f` | member / key | keyword | `-f` test flags share keyword.operator.logical.shell with `&& == !=` (grammar source). |
| `~` | operator | text | `~` in shell is unscoped. |
| `&>` | operator | two colours | the bash grammar splits `&>` into a background `&` and a redirect `>`. |
| `$[` | punctuation | text | `$[ ]` arithmetic is unscoped. |

</details>

### Makefiles

- **Grammar:** built in.
- **Checked tokens shown as designed:** 24 of 25 as tested.
- Tested with Makefile Tools (`ms-vscode.makefile-tools`) 0.12.17 installed; it does not change colours.

<details>
<summary><b>1 exception</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `-Wall` | member / key | text | Make recipe flags (-Wall) are unscoped. |

</details>

### CMake

- **Grammar:** CMake Tools (`ms-vscode.cmake-tools`) 1.25.10.
- **Checked tokens shown as designed:** 25 of 29 as tested.
- VS Code has no built-in CMake grammar. Other CMake grammar extensions were not tested.

<details>
<summary><b>4 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `add_fw` | function | text | the grammar scopes it exactly like `3.20` (number / constant). |
| `BOARD` | global / config variable | text | CMake variable name in set() is unscoped. |
| `C_STANDARD` | member / key | text | the grammar scopes it exactly like `3.20` (number / constant). |
| `3.20` | number / constant | text | the grammar scopes it exactly like `add_fw` (function). |

</details>

### JSON and JSONC

- **Grammar:** built in.
- **Checked tokens shown as designed:** 16 of 16 as tested.

No exceptions found.

### YAML

- **Grammar:** built in.
- **Checked tokens shown as designed:** 29 of 31 as tested.
- Tested with YAML (`redhat.vscode-yaml`) 2.0.0 installed. It provides no semantic tokens.

<details>
<summary><b>2 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `2026-11-20` | number / constant | string | the grammar scopes it exactly like `esp32` (string). |
| `?` | punctuation | text | YAML explicit-key `?` gets only meta.block-mapping.yaml. |

</details>

### TOML

- **Grammar:** Even Better TOML (`tamasfe.even-better-toml`) 0.21.2.
- **Checked tokens shown as designed:** 24 of 24 without a language server; 24 of 24 with Even Better TOML.
- The same extension provides the grammar and the semantic tokens.

No exceptions found.

### INI

- **Grammar:** built in.
- **Checked tokens shown as designed:** 6 of 9 as tested.

<details>
<summary><b>3 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `-DDEBUG` | member / key | text | the grammar scopes it exactly like `espressif32` (string). |
| `115200` | number / constant | text | the grammar scopes it exactly like `espressif32` (string). |
| `espressif32` | string | text | the grammar scopes it exactly like `115200` (number / constant). |

</details>

### Markdown

- **Grammar:** built in.
- **Checked tokens shown as designed:** 26 of 27 as tested.
- Fenced code blocks use the grammar of their language, so the sections for those languages apply.

<details>
<summary><b>1 exception</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `Setext` | function | text | a setext heading line is a paragraph until the underline on the next line; TextMate cannot look ahead. |

</details>

### Log files

- **Grammar:** built in, plus Rosin's own log-level grammar.
- **Checked tokens shown as designed:** 19 of 22 as tested.
- Rosin recognises ESP-IDF style (`E (512) tag:`) and Zephyr style (`<err>`) levels, panic and fault messages.

<details>
<summary><b>3 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `Traceback`, `ValueError` | error | text | the grammar scopes it exactly like `<` (punctuation). |
| `<` | punctuation | text | the grammar scopes it exactly like `Traceback` (error). |

</details>

### Diffs and git commit messages

- **Grammar:** built in.
- **Checked tokens shown as designed:** 25 of 26 as tested.

<details>
<summary><b>1 exception</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `src/main.c` | string | keyword | the grammar scopes it exactly like `modified` (keyword). |

</details>

### ARM assembly

- **Grammar:** Arm Assembly (`dan-c-underwood.arm`) 1.7.4.
- **Checked tokens shown as designed:** 26 of 31 as tested.

<details>
<summary><b>5 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `main`, `Reset_Handler` | function | text | the grammar scopes it exactly like `_estack` (global / config variable). |
| `_estack`, `STACK` | global / config variable | text | the grammar scopes it exactly like `main` (function). |
| `.equ` | preprocessor / attribute | text | ARM `.equ` directive is unscoped in this grammar. |

</details>

### Linker scripts

- **Grammar:** LinkerScript (`ZixuanWang.linkerscript`) 1.0.4.
- **Checked tokens shown as designed:** 16 of 23 as tested.

<details>
<summary><b>7 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `Reset_Handler` | function | text | the grammar scopes it exactly like `0x08000000` (number / constant). |
| `.` | hazard | text | the location counter `.` is a bare variable.other.ld, the same scope as every other linker-script name. |
| `0x08000000`, `4096` | number / constant | text | the grammar scopes it exactly like `Reset_Handler` (function). |
| `rx` | qualifier | text | memory attributes (rx) and input-section patterns (.text*) share section.input.ld variable.other.ld; a rule was tried in E2 and reverted. |
| `K` | unit | text | the grammar scopes it exactly like `Reset_Handler` (function). |
| `FLASH` | user type | keyword | the grammar scopes it exactly like `KEEP` (keyword). |

</details>

### Devicetree

- **Grammar:** DeviceTree (`plorefice.devicetree`) 0.1.1.
- **Checked tokens shown as designed:** 9 of 15 as tested.

<details>
<summary><b>6 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `\n` | escape | string | the grammar scopes it exactly like `gpio-leds` (string). |
| `GPIO_ACTIVE_HIGH` | macro | number / constant | the grammar scopes it exactly like `13` (number / constant). |
| `compatible`, `#address-cells` | member / key | text | the grammar scopes it exactly like `/dts-v1/` (preprocessor / attribute). |
| `/dts-v1/` | preprocessor / attribute | text | the grammar scopes it exactly like `compatible` (member / key). |
| `[` | punctuation | number / constant | the grammar scopes it exactly like `GPIO_ACTIVE_HIGH` (macro). |

</details>

### Kconfig

- **Grammar:** ESP-IDF (`espressif.esp-idf-extension`) 2.3.0.
- **Checked tokens shown as designed:** 10 of 19 as tested.
- The ESP-IDF extension provides the Kconfig grammar.

<details>
<summary><b>9 exceptions</b></summary>

| Token | Should be | Shown as | Why |
|---|---|---|---|
| `Pin` | comment | text | the grammar scopes it exactly like `BLINK_GPIO` (global / config variable). |
| `\"` | escape | text | the grammar scopes it exactly like `BLINK_GPIO` (global / config variable). |
| `$(` | global / config variable | string | the grammar scopes it exactly like `GPIO` (string). |
| `BLINK_GPIO`, `SOC_GPIO` | global / config variable | text | the grammar scopes it exactly like `48` (number / constant). |
| `48` | number / constant | text | the grammar scopes it exactly like `BLINK_GPIO` (global / config variable). |
| `int`, `string`, `bool` | primitive type | keyword | the grammar scopes it exactly like `range` (keyword). |

</details>

Every exception, with its evidence, is in the [limits register](audit/register/limits-register.md). Tested on VS Code 1.147.0.
<!-- languages:end -->

## Install

1. Open the Extensions view (`Ctrl+Shift+X`) and search for **Rosin**.
2. Install it, then run **Preferences: Color Theme** and pick a **Rosin · …** flavour.

Offline or on a fork of VS Code? Download the `.vsix` from the [latest release](https://github.com/debjoy-howlader/rosin-theme/releases/latest) and run **Extensions: Install from VSIX…**.

### Recommended settings

```jsonc
"editor.semanticHighlighting.enabled": true,
"editor.bracketPairColorization.enabled": true
```

Install the language servers recommended under [Language support](#language-support) for the languages you use. Without them, methods, library functions, globals and statics fall back to the function or text colour in C, C++, Rust and Python.

## Building from source

The theme files are generated. To change a palette, edit the flavour tables in `tools/gen.py`, then run:

```sh
python tools/gen.py             # writes themes/*.json
python tools/readme_assets.py   # redraws the preview, swatches and colour tables (needs Pillow)
python tools/readme_languages.py   # rewrites the Language support section from the audit's limits register
npx @vscode/vsce package        # builds the .vsix
```

To release, bump `version` in `package.json`, add a `CHANGELOG.md` entry, then push a matching tag (`git tag v1.0.2 && git push --tags`). A GitHub Action builds the `.vsix` and attaches it to a new release.

## License

MIT
