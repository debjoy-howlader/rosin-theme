# R2: limits register and README

**Register.** `audit/harness/register.py` builds `audit/register/limits-register.json` from the final audit (A5 verdicts), the A4 findings, `A4-reviewed-limits.json`, `register/split-reviewed.json` (hand review of split tokens) and `register/evidence-overrides.json` (two corrected evidence texts). One entry per checked token and mode that is not the designed colour: 296 entries. Every entry has a reason; the script stops if one does not. Codes: SS 128, SV 81, NEEDS-SERVER 30, NS 21, DESIGN 16 (deliberate, not a limit), SPLIT 8, ID 6, GE 2, DV 2, ENV 2.

**README.** `tools/readme_languages.py` writes the Language support section (between `<!-- languages:start/end -->`) and `audit/register/limits-register.md`. Per language: grammar source (built in or required extension), recommended servers with tested versions, checked-token counts per mode, notes, and the exceptions grouped by mode set (every mode / without a server / with a given server). Hand-written: tagline narrowed to "each colour keeps one meaning across languages"; new Highlights bullet; new "What each colour means" table; recommended-servers sentence; build command.

**Colour tables** (`tools/readme_assets.py`, now with `--tables-only`, preview untouched): new Unit row; examples changed where the audit showed them wrong in some mode: `uint8_t` (user type with cpptools), `println!` (error with rust-analyzer, E-01), `printf memcpy` (library colour only with clangd), `0xFF` (two colours by design), `struct trait` moved from user type to keyword (P1). Row "User type / type keyword" renamed "User type".

**Packaging.** `.vscodeignore` gains `audit/**` so the audit (dumps, corpus, reports) stays out of the .vsix.

**Line endings.** README.md, CHANGELOG.md and package.json had been converted to CRLF in the working tree with no content change; the generators keep whatever line ending the README has.
