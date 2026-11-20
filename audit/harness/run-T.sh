#!/bin/bash
# Mode T over the whole corpus: built-in grammars + audit-env extensions + Rosin from source, Pylance excluded (it swaps the Python grammar).
cd "$(dirname "$0")"
export VSC_BUILTIN="$HOME/mnt/Microsoft VS Code/8a14f0cc1b/resources/app/extensions"
node audit.js ../corpus "${1:-$HOME/w/a1-T.json}" --ext-root $HOME/mnt/test-code/rosin-audit-env/ext --ext-root ../.. --exclude-ext ms-python.vscode-pylance --exclude-ext debjoy-howlader
