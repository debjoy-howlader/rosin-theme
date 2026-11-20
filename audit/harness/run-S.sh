#!/bin/bash
# Mode S: all audit-env extensions (Pylance's grammar included) + every semantic dump.
cd "$(dirname "$0")"
export VSC_BUILTIN="$HOME/mnt/Microsoft VS Code/8a14f0cc1b/resources/app/extensions"
node audit.js ../corpus "${1:-$HOME/w/a1-S.json}" --ext-root $HOME/mnt/test-code/rosin-audit-env/ext --ext-root ../.. --exclude-ext debjoy-howlader \
  --dumps ../dumps/cpptools --dumps ../dumps/clangd --dumps ../dumps/rust --dumps ../dumps/servers
