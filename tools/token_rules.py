"""Extra token and semantic rules layered on top of the Sweet C base rules.
Colours come from a role table `p` (see gen.py), so every flavour stays consistent."""

def R(name, scopes, fg=None, style=None):
    s = {}
    if fg: s['foreground'] = fg
    if style is not None: s['fontStyle'] = style
    return {'name': name, 'scope': scopes, 'settings': s}

# E1 (audit edit phase 1): scopes removed from the Sweet C base rules. Each entry names the base rule and why.
BASE_REMOVALS = {
    'Members / keys / properties': ['punctuation.definition.begin.bracket.square', 'punctuation.definition.end.bracket.square',  # CP: every [ ] took the member colour
                                    'support.variable.magic'],                                                                    # CP: Python dunders took the member colour
    'Composite-type keywords & user types (turquoise)': ['storage.type.struct', 'storage.type.union', 'storage.type.enum', 'storage.type.class',
                                    'storage.type.namespace', 'storage.type.template', 'storage.type.template.argument'],         # P1
    'Macro names & macro parameters': ['variable.parameter.preprocessor'],                                                        # P6
    'Keywords & control flow (amber)': ['keyword.other.operator.overload'],                                                       # CP: operator names are functions
    'Markup': ['markup.inline.raw'],                                                                                              # P15
    'Links': ['string.other.link'],                                                                                               # P15
}
BASE_DROP = ['volatile (C++ only; C grammar has no scope for it)']                                                                # P16: volatile is a qualifier

def base_edits(tokens):
    out = []
    for r in tokens:
        if r.get('name') in BASE_DROP:
            continue
        rm = BASE_REMOVALS.get(r.get('name'))
        if rm:
            r = dict(r, scope=[x for x in (r['scope'] if isinstance(r['scope'], list) else [r['scope']]) if x not in rm])
        out.append(r)
    return out

def e1_rules(p):
    """Rules added in edit phase E1 (audit report A1). Appended last so they win ties."""
    return [
        R('E1 Rust declaration keywords (storage.type.rust innermost)', ['storage.type.rust'], p['keyword'], ''),
        R('E1 Rust primitive types', ['entity.name.type.numeric.rust', 'entity.name.type.primitive.rust'], p['prim'], ''),
        R('E1 Rust numeric suffix (7u8)', ['constant.numeric entity.name.type.numeric.rust'], p['unit'], ''),
        R('E1 Rust format placeholders {}', ['meta.interpolation.rust punctuation.definition.interpolation.rust', 'meta.interpolation.rust'], p['hazard'], ''),
        R('E1 C/C++ inline asm keyword', ['storage.type.asm'], p['keyword'], ''),
        R('E1 C++ template and typename keywords (P1)', ['storage.type.template', 'storage.type.template.argument'], p['keyword'], ''),
        R('E1 C++ operator-overload names', ['keyword.other.operator.overload'], p['function'], ''),
        R('E1 C++ template parameter names', ['entity.name.type.template'], p['typeparam'], 'italic'),
        R('E1 this (same as self: parameter)', ['variable.language.this'], p['param'], 'italic'),
        R('E1 Doc-comment delimiters', ['comment.block.documentation punctuation.definition.comment', 'comment.line.documentation punctuation.definition.comment'], p['doc'], 'italic'),
        R('E1 Python decorator names that are builtins', ['meta.function.decorator support.type.python', 'meta.function.decorator support.function'], p['directive'], ''),
        R('E1 Kconfig keywords', ['variable.language.kconfig', 'storage.modifier.kconfig', 'storage.type.kconfig'], p['keyword'], ''),
        R('E1 Devicetree node names (this grammar)', ['entity.name.function.dts'], p['composite'], ''),
        R('E1 Devicetree labels (this grammar)', ['entity.name.type.dts'], p['function'], 'italic'),
        R('E1 ARM registers', ['storage.register.arm'], p['hazard'], ''),
        R('E1 ARM label definitions', ['routine.arm'], p['function'], 'italic'),  # variable.named.arm covers every identifier: left plain
        R('E1 Make variable delimiters $( ) take the variable colour', ['string.interpolated.makefile punctuation.definition.variable.makefile'], p['globalvar'], ''),
        R('E1 Make assignment operators', ['punctuation.separator.key-value.makefile'], p['quietop'], ''),
        R('E1 Make .PHONY and special targets', ['support.function.target.PHONY.makefile', 'support.function.target'], p['keyword'], ''),
        R('E1 CMake variable delimiters ${ } take the variable colour', ['variable.other.cmake punctuation.section.variable', 'punctuation.section.variable.begin.cmake', 'punctuation.section.variable.end.cmake'], p['globalvar'], ''),
        R('E1 CMake keyword arguments (PRIVATE VERSION)', ['support.type.property.cmake'], p['qualifier'], 'italic'),
        R('E1 CMake bracket arguments', ['variable.parameter.cmake'], p['string'], ''),
        R('E1 Shell && and ||', ['punctuation.separator.statement.and.shell', 'punctuation.separator.statement.or.shell'], p['keyword'], ''),
        R('E1 Git commit subject', ['meta.scope.subject.git-commit'], p['keyword'], ''),
        R('E1 Markdown inline code', ['markup.inline.raw'], p['string'], ''),
        R('E1 Markdown link text reads as body text (P15)', ['string.other.link.title.markdown', 'string.other.link.description.markdown', 'string.other.link.description.title.markdown'], p['variable'], ''),
    ]

def e2_rules(p):
    """Rules added in edit phase E2 (audit report A2). Appended after E1."""
    return [
        R('E2 C++ extern linkage', ['storage.type.extern.cpp'], p['qualifier'], ''),
        R('E2 C++ keywords the grammar scopes as types or operators (decltype noexcept requires)', ['keyword.other.decltype.cpp', 'storage.type.decltype.cpp', 'keyword.operator.noexcept.cpp', 'variable.other.unknown.requires.cpp'], p['keyword'], ''),
        R('E2 Python global / nonlocal', ['storage.modifier.declaration.python'], p['keyword'], ''),
        R('E2 C __VA_ARGS__ is a macro parameter', ['entity.name.other.preprocessor.macro.predefined.probably.VA_ARGS'], p['param'], 'italic'),
        R('E2 Words inside inline-asm strings stay string', ['meta.embedded.assembly.c variable.named.arm', 'meta.embedded.assembly.cpp variable.named.arm'], p['string'], ''),
        R('E2 C/C++ standard attributes [[nodiscard]]', ['support.other.attribute entity.other.attribute'], p['directive'], ''),
        R('E2 C++ string encoding prefix u8 L u U', ['meta.encoding.cpp'], p['string'], ''),
        R('E2 C++ user-defined literal suffixes', ['keyword.other.suffix.literal.user-defined'], p['unit'], ''),
        R('E2 Linker script section and region names', ['section.output.prepart.ld variable.other.ld', 'section.output.postpart.ld variable.other.ld', 'section.discard.ld variable.other.ld'], p['composite'], ''),
        R('E2 Linker script symbols in expressions', ['expression.ld variable.other.ld'], p['globalvar'], ''),
        R('E2 Diff file-header markers --- +++ ***', ['meta.diff.header punctuation.definition.from-file.diff', 'meta.diff.header punctuation.definition.to-file.diff'], p['comment'], 'italic'),
        R('E2 Diff "Only in" lines', ['meta.diff.only-in'], p['comment'], 'italic'),
        R('E2 Diff hunk-range markers @@', ['meta.diff.range punctuation.definition.range.diff'], p['directive'], ''),
        R('E2 Devicetree label references &label', ['variable.name.dts'], p['function'], ''),
        R('E2 Python line continuation backslash', ['punctuation.separator.continuation.line.python'], p['escape'], ''),
        R('E2 Python imaginary suffix j', ['storage.type.imaginary.number.python'], p['unit'], ''),
        R('E2 Regex escapes keep the escape colour inside raw strings', ['string.regexp support.other.escape.special.regexp', 'string.regexp constant.character.escape'], p['escape'], ''),
        R('E2 Python raw-string body reads as string', ['string.regexp.quoted.single.python', 'string.regexp.quoted.double.python', 'string.regexp.quoted.multi.python'], p['string'], ''),
        R('E2 Shell $\'...\' and <( ) delimiters', ['string.quoted.single.dollar.shell punctuation.definition.string', 'string.interpolated.process-substitution.shell punctuation.definition.string'], p['string'], ''),
        R('E2 ARM memory and register-list brackets', ['storage.memaddress.arm', 'storage.stack.arm'], p['punct'], ''),
        R('E2 CMake generator-expression delimiters $< >', ['punctuation.definition.generator-expression.begin.cmake', 'punctuation.definition.generator-expression.end.cmake'], p['hazard'], ''),
        R('E2 YAML document markers --- ...', ['entity.other.document.begin.yaml', 'entity.other.document.end.yaml'], p['punct'], ''),
        R('E2 YAML merge key <<', ['keyword.operator.yaml'], p['member'], ''),
        R('E2 YAML list dash (same as list bullets)', ['punctuation.definition.block.sequence.item.yaml'], p['keyword'], ''),
        R('E2 C++ class member declarations', ['meta.body.class.cpp variable.other.declare.cpp', 'meta.body.struct.cpp variable.other.declare.cpp'], p['member'], ''),
        R('E2 Git status words in commit comments (new file, deleted)', ['comment.line.number-sign.git-commit markup.deleted.git-commit', 'comment.line.number-sign.git-commit markup.inserted.git-commit', 'comment.line.number-sign.git-commit markup.changed.git-commit'], p['keyword'], ''),
        R('E2 Make prerequisites are targets', ['meta.scope.prerequisites.makefile'], p['function'], ''),
        R('E2 Python dunder methods (def __init__, __post_init__)', ['meta.function.python support.function.magic.python', 'meta.function.python support.variable.magic.python'], p['method'], ''),
        R('E2 Python metaclass= keyword argument', ['support.type.metaclass.python'], p['param'], 'italic'),
        R('E2 Rust macro_rules!', ['entity.name.function.macro.rules.rust'], p['keyword'], ''),
        R('E2 Rust Option / Result variants (Some None Ok Err)', ['entity.name.type.option.rust', 'entity.name.type.result.rust'], p['number'], ''),
        R('E2 Rust float exponent', ['constant.numeric keyword.operator.exponent.rust', 'constant.numeric keyword.operator.exponent.sign.rust'], p['unit'], ''),
        R('E2 Rust path separator :: (same as C++)', ['keyword.operator.namespace.rust'], p['namespace'], ''),
        R('E2 Rust static and super keywords', ['storage.modifier.rust', 'variable.language.super.rust'], p['keyword'], ''),
        R('E2 Shell =~ operator', ['keyword.operator.logical.regex.shell'], p['quietop'], ''),
        R('E2 Shell alias keyword', ['storage.type.alias.shell'], p['keyword'], ''),
        R('E2 C++ qualified namespace names (a::b in namespace, alias, using)', ['entity.name.scope-resolution.namespace.block.cpp', 'entity.name.scope-resolution.namespace.alias.cpp', 'entity.name.scope-resolution.namespace.using.cpp'], p['namespace'], ''),
        R('E2 C++ owner type of an out-of-line definition (Led::get, Led::operator==)', ['entity.name.scope-resolution.function.definition.cpp', 'entity.name.scope-resolution.operator.cpp', 'entity.name.scope-resolution.operator-overload.cpp'], p['composite'], ''),
        R('E2 Shell for-loop variable', ['variable.other.for.shell'], p['globalvar'], ''),
        R('E2 C/C++ exponent sign belongs to the exponent (same as Rust)', ['keyword.operator.plus.exponent', 'keyword.operator.minus.exponent'], p['unit'], ''),
        R('E2 C++ digit separator 1\'000 stays in the number', ['punctuation.separator.constant.numeric'], p['number'], ''),
        R('E2 Rust macro metavariables $name take one colour (P8)', ['meta.macro.metavariable.rust keyword.operator.macro.dollar.rust', 'variable.other.metavariable.name.rust'], p['param'], 'italic'),
        R('E2 Rust macro fragment specifiers (expr ty ident)', ['variable.other.metavariable.specifier.rust'], p['keyword'], ''),
        R('E2 Shell alias names', ['meta.expression.assignment.alias.shell variable.other.assignment.shell'], p['function'], ''),
    ]

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
        R('Type-declaring keywords (class interface type enum namespace)', ['storage.type.class', 'storage.type.interface', 'storage.type.type', 'storage.type.enum', 'storage.type.namespace', 'storage.type.struct', 'storage.type.union', 'storage.type.trait', 'storage.type.module', 'keyword.declaration.struct', 'keyword.declaration.enum', 'keyword.declaration.trait', 'keyword.declaration.type', 'keyword.declaration.impl', 'keyword.other.struct', 'keyword.other.enum', 'keyword.other.trait', 'keyword.other.type', 'keyword.other.impl'], p['keyword'], ''),  # E1: P1
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
        # E1: rust-analyzer const/static items, Pylance modifiers
        'const': p['number'], 'static': p['staticvar'],
        '*.decorator': p['directive'], 'function.decorator': p['directive'], 'class.decorator': p['directive'], 'function.decorator.builtin': p['directive'], 'class.decorator.builtin': p['directive'], 'magicFunction': p['method'], 'magicFunction.builtin': p['method'], 'function.builtin': p['libfn'], 'variable.classMember': p['member'], 'class.builtin': p['prim'],
        # E2
        'type.deduced': p['keyword'], 'class.constructorOrDestructor': p['function'], 'stringLiteral': p['unit'], 'numberLiteral': p['unit'], 'customLiteral': p['unit'],
        'tomlArrayKey': p['member'], 'concept': p['composite'], 'enum.defaultLibrary': p['prim'], 'struct.defaultLibrary': p['prim'], 'function.library': p['libfn'], 'function.decorator.library': p['directive'], 'class.decorator.library': p['directive'],
        # Generic
        'regexp': p['escape'],
        'comment.documentation': {'foreground': p['doc'], 'italic': True},
    }



def semantic_overrides(p):
    """Semantic keys that REPLACE a base-theme entry (extra_semantic only adds missing keys)."""
    return {
        # E2: clangd marks file-scope (internal linkage, i.e. static) variables with fileScope; extern globals get globalScope.
        'variable.fileScope': p['staticvar'],
    }


def prune_shadowed(rules):
    """Drop scope selectors that a LATER rule redefines completely.

    In a TextMate theme two rules with the identical scope selector collapse to one: the later rule
    overwrites colour and font style. So the earlier occurrence is dead. It is only removed when the later
    rule sets both foreground and fontStyle (a full overwrite); rules left with no scope are dropped.
    Returns (pruned_rules, removed) where removed lists (rule name, scope) for the report."""
    def scopes(r):
        return r['scope'] if isinstance(r['scope'], list) else [r['scope']]
    def full(r):
        return 'foreground' in r['settings'] and 'fontStyle' in r['settings']
    last = {}
    for i, r in enumerate(rules):
        if 'scope' not in r:
            continue
        if full(r):
            for sc in scopes(r):
                last[sc] = i
    out, removed = [], []
    for i, r in enumerate(rules):
        if 'scope' not in r:
            out.append(r); continue
        keep = [sc for sc in scopes(r) if last.get(sc, i) <= i]
        gone = [sc for sc in scopes(r) if last.get(sc, i) > i]
        removed += [(r.get('name'), sc) for sc in gone]
        if not gone:
            out.append(r)
        elif keep:
            r = dict(r); r['scope'] = keep if isinstance(r['scope'], list) else keep[0]; out.append(r)
    return out, removed
