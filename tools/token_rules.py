"""Extra token and semantic rules layered on top of the Sweet C base rules.
Colours come from a role table `p` (see gen.py), so every flavour stays consistent."""

def R(name, scopes, fg=None, style=None):
    s = {}
    if fg: s['foreground'] = fg
    if style is not None: s['fontStyle'] = style
    return {'name': name, 'scope': scopes, 'settings': s}

def extra_rules(p):
    return [
        # ---------- comments ----------
        R('Doc comments (line-style: Rust ///, C++ ///, C# ///)', ['comment.line.documentation', 'comment.line.double-slash.documentation', 'comment.line.triple-slash', 'comment.block.documentation', 'comment.line.doc', 'comment.block.doc'], p['doc'], 'italic'),
        # ---------- Rust ----------
        R('Rust attributes #[..] (same family as C preprocessor)', ['meta.attribute.rust', 'punctuation.definition.attribute.rust', 'meta.attribute.rust entity.name.function.macro.rust'], p['directive'], ''),
        R('Rust lifetimes', ['entity.name.type.lifetime', 'storage.modifier.lifetime', 'punctuation.definition.lifetime'], p['typeparam'], 'italic'),
        R('Rust unsafe (hazard)', ['keyword.other.unsafe', 'storage.modifier.unsafe'], p['hazard'], 'bold'),
        R('Rust borrow & (same as C address-of)', ['keyword.operator.borrow', 'keyword.operator.borrow.and', 'keyword.operator.borrow.rust'], p['hazard'], 'bold'),
        R('Rust self / Python self,cls / Lua self', ['variable.language.self', 'variable.language.self.rust', 'variable.language.self.lua', 'variable.language.special.self', 'variable.language.special.cls'], p['param'], 'italic'),
        R('Macro invocations (Rust println!, Elixir, Julia @)', ['entity.name.function.macro', 'support.macro', 'meta.macro.rust entity.name.function'], p['macro'], 'bold'),
        # ---------- JS / TS / C# / Java declaration keywords ----------
        R('Type-declaring keywords (class interface type enum namespace)', ['storage.type.class', 'storage.type.interface', 'storage.type.type', 'storage.type.enum', 'storage.type.namespace', 'storage.type.struct', 'storage.type.union', 'storage.type.trait', 'storage.type.module', 'keyword.declaration.struct', 'keyword.declaration.enum', 'keyword.declaration.trait', 'keyword.declaration.type', 'keyword.declaration.impl', 'keyword.other.struct', 'keyword.other.enum', 'keyword.other.trait', 'keyword.other.type', 'keyword.other.impl'], p['composite'], ''),
        R('Modules / packages / imports', ['entity.name.type.module', 'entity.name.package', 'entity.name.import', 'entity.name.namespace', 'support.other.namespace', 'entity.name.module'], p['namespace'], ''),
        R('JSX / component tags', ['support.class.component', 'entity.name.tag.tsx support.class', 'entity.name.tag.jsx support.class'], p['composite'], ''),
        R('Regular expressions', ['string.regexp', 'source.regexp'], p['escape'], ''),
        R('Regex operators / classes', ['keyword.operator.quantifier.regexp', 'constant.other.character-class.regexp', 'keyword.control.anchor.regexp', 'punctuation.definition.group.regexp', 'constant.character.character-class.regexp', 'keyword.operator.or.regexp'], p['hazard'], ''),
        # ---------- Shell / PowerShell ----------
        R('Shell plain arguments (not strings)', ['string.unquoted.argument.shell', 'string.unquoted.cmake'], p['variable'], ''),
        R('CLI options / flags (--port -Wall)', ['constant.other.option', 'constant.other.option.dash', 'string.unquoted.argument.shell constant.other.option', 'variable.parameter.option', 'support.constant.option'], p['member'], ''),
        R('Shell function definitions', ['entity.name.function.shell', 'meta.function.shell entity.name.function'], p['function'], ''),
        R('Build/config variables: shell $VAR, Make $(VAR), CMake ${VAR}, env (share C-global colour)', ['variable.other.normal.shell', 'variable.other.bracket.shell', 'variable.other.assignment.shell', 'punctuation.definition.variable.shell', 'variable.other.makefile', 'variable.other.cmake', 'variable.other.env.cmake', 'variable.other.cache.cmake', 'support.type.variable.cmake', 'variable.other.env', 'variable.other.readwrite.powershell', 'support.variable.automatic.powershell', 'variable.other.dockerfile', 'variable.other.env.dockerfile'], p['globalvar'], ''),
        R('Positional / special shell params ($1 $@ $?), Make automatic vars ($@ $< $^)', ['variable.parameter.positional.shell', 'variable.parameter.positional.all.shell', 'variable.language.special.shell', 'variable.language.makefile'], p['hazard'], ''),
        R('Variable sigils ($ in PowerShell)', ['punctuation.definition.variable.powershell'], p['punct'], ''),
        R('Heredoc delimiters', ['keyword.control.heredoc-token.shell', 'punctuation.definition.string.heredoc'], p['directive'], ''),
        # ---------- Make / CMake ----------
        R('Make targets', ['entity.name.function.target.makefile', 'entity.name.function.target'], p['function'], 'bold'),
        R('Make/CMake built-in functions (wildcard, patsubst)', ['support.function.makefile'], p['libfn'], ''),
        R('CMake commands', ['support.function.cmake', 'entity.name.function.cmake', 'support.function.commandProperty.cmake'], p['function'], ''),
        R('CMake keywords (PRIVATE PUBLIC VERSION REQUIRED)', ['keyword.other.cmake'], p['qualifier'], 'italic'),
        R('CMake properties', ['support.type.property.cmake'], p['member'], ''),
        # ---------- TOML / INI / YAML / JSON ----------
        R('TOML / INI table headers', ['support.type.property-name.table.toml', 'support.type.property-name.array.toml', 'punctuation.definition.table.toml', 'punctuation.definition.array.table.toml', 'entity.other.attribute-name.table.toml', 'entity.name.section.group-title.ini', 'punctuation.definition.entity.ini'], p['function'], 'bold'),
        R('Dates & times (TOML/YAML)', ['constant.other.time', 'constant.other.date', 'constant.other.timestamp'], p['number'], ''),
        R('YAML anchors / aliases / tags', ['entity.name.type.anchor.yaml', 'variable.other.alias.yaml', 'punctuation.definition.anchor.yaml', 'punctuation.definition.alias.yaml', 'storage.type.tag-handle.yaml'], p['directive'], ''),
        # ---------- HTML / CSS ----------
        R('HTML entities (&amp;)', ['constant.character.entity', 'punctuation.definition.entity.html'], p['escape'], ''),
        R('Tag brackets < > </ />', ['punctuation.definition.tag'], p['punct'], ''),
        R('CSS class selectors', ['entity.other.attribute-name.class.css', 'entity.other.attribute-name.class.scss', 'entity.other.attribute-name.class.less'], p['composite'], ''),
        R('CSS id selectors', ['entity.other.attribute-name.id.css', 'entity.other.attribute-name.id'], p['keyword'], ''),
        R('CSS pseudo-classes / at-rules', ['entity.other.attribute-name.pseudo-class', 'entity.other.attribute-name.pseudo-element', 'keyword.control.at-rule', 'punctuation.definition.keyword.css'], p['directive'], ''),
        R('CSS property values', ['support.constant.property-value', 'support.constant.font-name', 'support.constant.color'], p['number'], ''),
        R('CSS property names', ['support.type.property-name.css', 'support.type.vendored.property-name', 'meta.property-name'], p['member'], ''),
        # ---------- Assembly (ARM / RISC-V / AVR / x86 grammars) ----------
        R('ASM instructions / mnemonics', ['keyword.opcode', 'keyword.instruction', 'support.function.instruction', 'keyword.other.instruction', 'keyword.control.instruction', 'support.function.mnemonic', 'keyword.other.mnemonic', 'keyword.mnemonic'], p['keyword'], ''),
        R('ASM assembler directives (.section .global .word)', ['support.function.directive', 'storage.type.directive', 'keyword.directive', 'keyword.other.directive', 'meta.directive', 'keyword.control.directive.asm', 'support.function.pseudo', 'keyword.control.assembler'], p['directive'], ''),
        R('ASM registers (r0 sp lr a0 x5)', ['variable.other.register', 'storage.other.register', 'support.variable.register', 'variable.register', 'variable.language.register', 'support.constant.register', 'storage.type.register', 'constant.language.register'], p['hazard'], ''),
        R('ASM labels', ['entity.name.function.label', 'entity.name.label', 'meta.label entity.name', 'entity.name.tag.label'], p['function'], 'italic'),
        R('ASM immediates (#5 $0x18)', ['constant.numeric.immediate', 'punctuation.definition.immediate'], p['number'], ''),
        # ---------- Device tree / linker scripts / Kconfig (extension grammars) ----------
        R('Devicetree nodes', ['entity.name.type.dts', 'entity.name.tag.dts', 'entity.name.type.node'], p['composite'], ''),
        R('Devicetree properties', ['variable.name.dts', 'support.type.property-name.dts', 'entity.other.attribute-name.dts'], p['member'], ''),
        R('Devicetree / Kconfig directives', ['keyword.directive.dts', 'keyword.other.dts', 'keyword.control.kconfig', 'keyword.other.kconfig', 'storage.type.kconfig'], p['directive'], ''),
        R('Devicetree labels & phandles', ['entity.name.function.dts', 'variable.other.phandle', 'entity.name.label.dts'], p['function'], 'italic'),
        R('Linker-script sections & regions', ['entity.name.section.linkerscript', 'entity.name.section.ld', 'entity.name.type.memory-region', 'support.constant.memory-region'], p['composite'], ''),
        R('Linker-script commands (ENTRY KEEP ORIGIN)', ['support.function.linkerscript', 'keyword.other.linkerscript', 'keyword.control.linkerscript', 'support.function.builtin.ld', 'keyword.other.ld'], p['keyword'], ''),
        # ---------- Logs (built-in Log grammar + injected ESP-IDF / Zephyr levels) ----------
        R('Log: error', ['log.error', 'log.exceptiontype'], p['error'], 'bold'),
        R('Log: warning', ['log.warning'], p['warning'], 'bold'),
        R('Log: info', ['log.info'], p['string'], ''),
        R('Log: debug', ['log.debug'], p['libfn'], ''),
        R('Log: verbose / timestamps', ['log.verbose', 'log.date', 'log.timestamp'], p['comment'], ''),
        R('Log: constants / numbers / addresses', ['log.constant'], p['number'], ''),
        R('Log: quoted strings', ['log.string'], p['string'], ''),
        R('Log: exception text', ['log.exception'], p['error'], ''),
        R('Log: ESP-IDF / Zephyr tag', ['log.tag.rosin'], p['member'], ''),
        # ---------- Diff / git ----------
        R('Diff headers', ['meta.diff.header', 'meta.diff.header.from-file', 'meta.diff.header.to-file', 'meta.diff.index'], p['comment'], 'bold'),
        R('Diff hunk ranges @@', ['meta.diff.range', 'meta.diff.range.unified'], p['directive'], ''),
        R('Git commit subject / rebase commands', ['meta.scope.message.git-commit markup.heading', 'support.function.git-rebase', 'keyword.operator.git-rebase'], p['keyword'], ''),
        R('Git SHA', ['constant.sha.git-rebase', 'constant.other.sha'], p['number'], ''),
        # ---------- Markdown polish ----------
        R('Markdown headings', ['markup.heading', 'entity.name.section.markdown', 'punctuation.definition.heading.markdown'], p['function'], 'bold'),
        R('Markdown code fence language', ['fenced_code.block.language', 'markup.fenced_code.block.markdown punctuation.definition'], p['comment'], ''),
        R('Markdown strikethrough', ['markup.strikethrough'], None, 'strikethrough'),
    ]

def extra_semantic(p):
    return {
        # Rust (rust-analyzer)
        'lifetime': {'foreground': p['typeparam'], 'italic': True},
        'selfKeyword': {'foreground': p['param'], 'italic': True},
        'selfTypeKeyword': p['composite'],
        'attribute': p['directive'], 'builtinAttribute': p['directive'], 'derive': p['directive'], 'deriveHelper': p['directive'],
        'formatSpecifier': {'foreground': p['hazard'], 'bold': True},
        'escapeSequence': p['escape'],
        'interface': {'foreground': p['composite'], 'italic': True},
        'typeAlias': p['composite'],
        'builtinType': p['prim'],
        'boolean': p['number'],
        'character': p['string'],
        'toolModule': p['namespace'], 'crateRoot': p['namespace'],
        'keyword.unsafe': {'foreground': p['hazard'], 'bold': True},
        'function.unsafe': {'foreground': p['function'], 'bold': True},
        'method.unsafe': {'foreground': p['method'], 'bold': True},
        'operator.unsafe': {'foreground': p['hazard'], 'bold': True},
        'unresolvedReference': {'foreground': p['error'], 'underline': True},
        'procMacro': {'foreground': p['macro'], 'bold': True},
        # Python (Pylance)
        'selfParameter': {'foreground': p['param'], 'italic': True},
        'clsParameter': {'foreground': p['param'], 'italic': True},
        'module': p['namespace'],
        'decorator': p['directive'],
        'builtinConstant': p['number'],
        # Generic
        'regexp': p['escape'],
        'comment.documentation': {'foreground': p['doc'], 'italic': True},
    }

