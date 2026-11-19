<p align="center">
  <img src="images/icon.png" width="96" alt="Rosin icon">
</p>

<h1 align="center">Rosin</h1>

<p align="center">Calm, low-glare dark themes for VS Code, where every colour means the same thing in every language.</p>

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

- **The whole window is themed.** Every colour VS Code lets a theme set (about 970 of them) is set in all six flavours. That covers the editor, panels, terminal, diff and merge views, testing, debugging, notebooks, chat and the settings editor.
- **Built for semantic highlighting.** Tuned for C/C++ IntelliSense and clangd, rust-analyzer and Pylance. Globals, statics, `const` values, parameters and library calls are each distinguishable.
- **Toolchains as well as languages.** Makefiles, CMake, shell, PowerShell, TOML, INI, YAML, Dockerfiles, diffs and git get the same care. Assembly, linker-script and devicetree grammars get it too, when an extension provides them.
- **Readable logs.** In `.log` files, errors, warnings, info and debug lines each get their own colour. ESP-IDF style (`E (512) tag:`) and Zephyr style (`<err>`) levels are recognised, along with panic and fault messages.
- **Contrast checked.** Body text is above WCAG AA in every flavour, while comments and punctuation are deliberately quieter.

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
| ![#E59B5B](images/swatches/e59b5b.png) | Keyword / control flow | `if` `for` `return` | `#E59B5B` |
| ![#9CADCB](images/swatches/9cadcb.png) | Qualifier | `const` `static` `extern` | `#9CADCB` |
| ![#B5A4FF](images/swatches/b5a4ff.png) | Function | `led_set()` | `#B5A4FF` |
| ![#C0B2FF](images/swatches/c0b2ff.png) | Method | `.write()` | `#C0B2FF` |
| ![#8D96BE](images/swatches/8d96be.png) | Library / builtin function | `printf` `memcpy` | `#8D96BE` |
| ![#E497CE](images/swatches/e497ce.png) | Macro (bold) | `LED_PIN` `println!` | `#E497CE` |
| ![#AB81AD](images/swatches/ab81ad.png) | Preprocessor / attribute | `#include` `#[derive]` | `#AB81AD` |
| ![#6F9895](images/swatches/6f9895.png) | Namespace / module | `std` `core::ptr` | `#6F9895` |
| ![#5EA0CD](images/swatches/5ea0cd.png) | Primitive type | `int` `uint8_t` `u32` | `#5EA0CD` |
| ![#75CCC4](images/swatches/75ccc4.png) | User type / type keyword | `struct` `led_t` `trait` | `#75CCC4` |
| ![#C2B7DB](images/swatches/c2b7db.png) | Parameter / self (italic) | `len` `self` | `#C2B7DB` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEAF97](images/swatches/deaf97.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEAF97` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#D5C984](images/swatches/d5c984.png) | Number / constant / enum | `42` `0xFF` `true` | `#D5C984` |
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
| ![#DB7489](images/swatches/db7489.png) | Keyword / control flow | `if` `for` `return` | `#DB7489` |
| ![#A1ABCC](images/swatches/a1abcc.png) | Qualifier | `const` `static` `extern` | `#A1ABCC` |
| ![#DAB663](images/swatches/dab663.png) | Function | `led_set()` | `#DAB663` |
| ![#DCC27B](images/swatches/dcc27b.png) | Method | `.write()` | `#DCC27B` |
| ![#AA966E](images/swatches/aa966e.png) | Library / builtin function | `printf` `memcpy` | `#AA966E` |
| ![#D297E5](images/swatches/d297e5.png) | Macro (bold) | `LED_PIN` `println!` | `#D297E5` |
| ![#A184BB](images/swatches/a184bb.png) | Preprocessor / attribute | `#include` `#[derive]` | `#A184BB` |
| ![#6F9896](images/swatches/6f9896.png) | Namespace / module | `std` `core::ptr` | `#6F9896` |
| ![#649FCB](images/swatches/649fcb.png) | Primitive type | `int` `uint8_t` `u32` | `#649FCB` |
| ![#74CCCB](images/swatches/74cccb.png) | User type / type keyword | `struct` `led_t` `trait` | `#74CCCB` |
| ![#C1B7DC](images/swatches/c1b7dc.png) | Parameter / self (italic) | `len` `self` | `#C1B7DC` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEB49B](images/swatches/deb49b.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEB49B` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#ECB0C6](images/swatches/ecb0c6.png) | Number / constant / enum | `42` `0xFF` `true` | `#ECB0C6` |
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
| ![#E8A0AA](images/swatches/e8a0aa.png) | Keyword / control flow | `if` `for` `return` | `#E8A0AA` |
| ![#A2B8AE](images/swatches/a2b8ae.png) | Qualifier | `const` `static` `extern` | `#A2B8AE` |
| ![#A8D17E](images/swatches/a8d17e.png) | Function | `led_set()` | `#A8D17E` |
| ![#B8DA92](images/swatches/b8da92.png) | Method | `.write()` | `#B8DA92` |
| ![#93A88C](images/swatches/93a88c.png) | Library / builtin function | `printf` `memcpy` | `#93A88C` |
| ![#DFA2D6](images/swatches/dfa2d6.png) | Macro (bold) | `LED_PIN` `println!` | `#DFA2D6` |
| ![#B49AC0](images/swatches/b49ac0.png) | Preprocessor / attribute | `#include` `#[derive]` | `#B49AC0` |
| ![#73A08E](images/swatches/73a08e.png) | Namespace / module | `std` `core::ptr` | `#73A08E` |
| ![#7FB8D6](images/swatches/7fb8d6.png) | Primitive type | `int` `uint8_t` `u32` | `#7FB8D6` |
| ![#7CCBB4](images/swatches/7ccbb4.png) | User type / type keyword | `struct` `led_t` `trait` | `#7CCBB4` |
| ![#C8BFDA](images/swatches/c8bfda.png) | Parameter / self (italic) | `len` `self` | `#C8BFDA` |
| ![#A3B9C8](images/swatches/a3b9c8.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#A3B9C8` |
| ![#E2C39E](images/swatches/e2c39e.png) | Global / config variable | `g_ticks` `$(CC)` | `#E2C39E` |
| ![#B9D0A8](images/swatches/b9d0a8.png) | Static variable | `s_state` | `#B9D0A8` |
| ![#B9B8EE](images/swatches/b9b8ee.png) | Number / constant / enum | `42` `0xFF` `true` | `#B9B8EE` |
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
| ![#DE8C6C](images/swatches/de8c6c.png) | Keyword / control flow | `if` `for` `return` | `#DE8C6C` |
| ![#B5ACBA](images/swatches/b5acba.png) | Qualifier | `const` `static` `extern` | `#B5ACBA` |
| ![#E8B565](images/swatches/e8b565.png) | Function | `led_set()` | `#E8B565` |
| ![#EEC47F](images/swatches/eec47f.png) | Method | `.write()` | `#EEC47F` |
| ![#B59D7A](images/swatches/b59d7a.png) | Library / builtin function | `printf` `memcpy` | `#B59D7A` |
| ![#DA9DC6](images/swatches/da9dc6.png) | Macro (bold) | `LED_PIN` `println!` | `#DA9DC6` |
| ![#BB91AC](images/swatches/bb91ac.png) | Preprocessor / attribute | `#include` `#[derive]` | `#BB91AC` |
| ![#8AA59C](images/swatches/8aa59c.png) | Namespace / module | `std` `core::ptr` | `#8AA59C` |
| ![#8DB2CD](images/swatches/8db2cd.png) | Primitive type | `int` `uint8_t` `u32` | `#8DB2CD` |
| ![#86C2B2](images/swatches/86c2b2.png) | User type / type keyword | `struct` `led_t` `trait` | `#86C2B2` |
| ![#CEC0D8](images/swatches/cec0d8.png) | Parameter / self (italic) | `len` `self` | `#CEC0D8` |
| ![#AABAC5](images/swatches/aabac5.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#AABAC5` |
| ![#E7C4A1](images/swatches/e7c4a1.png) | Global / config variable | `g_ticks` `$(CC)` | `#E7C4A1` |
| ![#BDC9A5](images/swatches/bdc9a5.png) | Static variable | `s_state` | `#BDC9A5` |
| ![#C7B5E4](images/swatches/c7b5e4.png) | Number / constant / enum | `42` `0xFF` `true` | `#C7B5E4` |
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
| ![#8E9296](images/swatches/8e9296.png) | Keyword / control flow | `if` `for` `return` | `#8E9296` |
| ![#868A8E](images/swatches/868a8e.png) | Qualifier | `const` `static` `extern` | `#868A8E` |
| ![#94B9DA](images/swatches/94b9da.png) | Function | `led_set()` | `#94B9DA` |
| ![#A7C6E2](images/swatches/a7c6e2.png) | Method | `.write()` | `#A7C6E2` |
| ![#8FA2B5](images/swatches/8fa2b5.png) | Library / builtin function | `printf` `memcpy` | `#8FA2B5` |
| ![#E4E6E8](images/swatches/e4e6e8.png) | Macro (bold) | `LED_PIN` `println!` | `#E4E6E8` |
| ![#808488](images/swatches/808488.png) | Preprocessor / attribute | `#include` `#[derive]` | `#808488` |
| ![#7F8387](images/swatches/7f8387.png) | Namespace / module | `std` `core::ptr` | `#7F8387` |
| ![#A6AAAE](images/swatches/a6aaae.png) | Primitive type | `int` `uint8_t` `u32` | `#A6AAAE` |
| ![#D6D8DA](images/swatches/d6d8da.png) | User type / type keyword | `struct` `led_t` `trait` | `#D6D8DA` |
| ![#B9BCBF](images/swatches/b9bcbf.png) | Parameter / self (italic) | `len` `self` | `#B9BCBF` |
| ![#B3B6B9](images/swatches/b3b6b9.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#B3B6B9` |
| ![#E8E9EA](images/swatches/e8e9ea.png) | Global / config variable | `g_ticks` `$(CC)` | `#E8E9EA` |
| ![#C0C3C6](images/swatches/c0c3c6.png) | Static variable | `s_state` | `#C0C3C6` |
| ![#DDDFE1](images/swatches/dddfe1.png) | Number / constant / enum | `42` `0xFF` `true` | `#DDDFE1` |
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
| ![#E59B5B](images/swatches/e59b5b.png) | Keyword / control flow | `if` `for` `return` | `#E59B5B` |
| ![#9CADCB](images/swatches/9cadcb.png) | Qualifier | `const` `static` `extern` | `#9CADCB` |
| ![#B5A4FF](images/swatches/b5a4ff.png) | Function | `led_set()` | `#B5A4FF` |
| ![#C0B2FF](images/swatches/c0b2ff.png) | Method | `.write()` | `#C0B2FF` |
| ![#8D96BE](images/swatches/8d96be.png) | Library / builtin function | `printf` `memcpy` | `#8D96BE` |
| ![#E497CE](images/swatches/e497ce.png) | Macro (bold) | `LED_PIN` `println!` | `#E497CE` |
| ![#AB81AD](images/swatches/ab81ad.png) | Preprocessor / attribute | `#include` `#[derive]` | `#AB81AD` |
| ![#6F9895](images/swatches/6f9895.png) | Namespace / module | `std` `core::ptr` | `#6F9895` |
| ![#5EA0CD](images/swatches/5ea0cd.png) | Primitive type | `int` `uint8_t` `u32` | `#5EA0CD` |
| ![#75CCC4](images/swatches/75ccc4.png) | User type / type keyword | `struct` `led_t` `trait` | `#75CCC4` |
| ![#C2B7DB](images/swatches/c2b7db.png) | Parameter / self (italic) | `len` `self` | `#C2B7DB` |
| ![#7DABB0](images/swatches/7dabb0.png) | Member / key / CLI flag | `.pin` `name:` `--baud` | `#7DABB0` |
| ![#DEAF97](images/swatches/deaf97.png) | Global / config variable | `g_ticks` `$(CC)` | `#DEAF97` |
| ![#ADC6A8](images/swatches/adc6a8.png) | Static variable | `s_state` | `#ADC6A8` |
| ![#D5C984](images/swatches/d5c984.png) | Number / constant / enum | `42` `0xFF` `true` | `#D5C984` |
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

## Install

1. Open the Extensions view (`Ctrl+Shift+X`) and search for **Rosin**.
2. Install it, then run **Preferences: Color Theme** and pick a **Rosin · …** flavour.

Offline or on a fork of VS Code? Download the `.vsix` from the [latest release](https://github.com/debjoy-howlader/rosin-theme/releases/latest) and run **Extensions: Install from VSIX…**.

### Recommended settings

```jsonc
"editor.semanticHighlighting.enabled": true,
"editor.bracketPairColorization.enabled": true
```

## Building from source

The theme files are generated. To change a palette, edit the flavour tables in `tools/gen.py`, then run:

```sh
python tools/gen.py             # writes themes/*.json
python tools/readme_assets.py   # redraws the preview, swatches and colour tables (needs Pillow)
npx @vscode/vsce package        # builds the .vsix
```

To release, bump `version` in `package.json`, add a `CHANGELOG.md` entry, then push a matching tag (`git tag v1.0.2 && git push --tags`). A GitHub Action builds the `.vsix` and attaches it to a new release.

## License

MIT
