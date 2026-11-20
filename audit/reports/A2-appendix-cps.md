# A2 appendix: change proposals

One proposal per distinguishing selector. Each needs its what-if run (predicted moves) at the start of the edit phase; the selector shown is the evidence, the final rule may be narrower (language suffix, parent scope).

| CP | Sev | Mode | Lang | Selector | Now | Should be | Components |
|---|---|---|---|---|---|---|---|
| CP-A2-001 | 3 | clangd/cpptools/T | cpp | `storage.type.extern.cpp` | prim|typeparam | qualifier | `cpp.extern.block`, `cpp.kw.extern.c` |
| CP-A2-002 | 2 | clangd/cpptools/T | cpp | `storage.type.built-in.primitive.cpp` | prim|typeparam | keyword | `cpp.kw.auto`, `cpp.type.auto` |
| CP-A2-003 | 2 | clangd/cpptools | c | `entity.name.function.c` | function | keyword | `c.kw.static_assert.macro`, `c.kw.typeof` |
| CP-A2-004 | 2 | cpptools/T | cpp | `storage.type.decltype.cpp` | prim|typeparam | keyword | `cpp.decltype.auto`, `cpp.kw.decltype` |
| CP-A2-005 | 2 | Pylance/T | python | `storage.modifier.declaration.python` | qualifier | keyword | `py.kw.global`, `py.kw.nonlocal` |
| CP-A2-006 | 1 | clangd | cpp | `semantic type.deduced.defaultLibrary.globalScope` | prim|typeparam | keyword | `cpp.decltype.auto`, `cpp.kw.decltype`, `cpp.type.auto` |
| CP-A2-007 | 3 | clangd/cpptools/T | c | `entity.name.other.preprocessor.macro.predefined.probably.VA_ARGS.c` | macro | param | `c.macro.va_args` |
| CP-A2-008 | 3 | clangd/cpptools/T | c | `variable.named.arm` | variable | string | `c.asm.operand.constraint` |
| CP-A2-009 | 3 | clangd/cpptools/T | cpp | `entity.other.attribute.nodiscard.cpp` | variable | directive | `cpp.attr.std` |
| CP-A2-010 | 2 | clangd/cpptools/T | cpp | `keyword.operator.noexcept.cpp` | quietop | keyword | `cpp.noexcept.op` |
| CP-A2-011 | 3 | clangd/cpptools/T | cpp | `meta.encoding.cpp` | punct | string | `cpp.char.u8` |
| CP-A2-012 | 2 | clangd/cpptools/T | cpp | `punctuation.section.attribute.begin.cpp` | punct | keyword | `cpp.kw.alignas` |
| CP-A2-013 | 2 | clangd/cpptools/T | cpp | `variable.other.unknown.requires.cpp` | variable | keyword | `cpp.kw.requires` |
| CP-A2-014 | 1 | T | ld | `variable.other.ld` | variable | composite | `ld.discard`, `ld.region.use`, `ld.section.name` |
| CP-A2-015 | 2 | clangd | cpp | `semantic class.declaration.definition.constructorOrDestructor.classScope` | composite|doctag | function | `cpp.ctor.decl`, `cpp.scope.ctor.def` |
| CP-A2-016 | 2 | cpptools | cpp | `semantic memberOperatorOverload.` | libfn | function | `cpp.op.overload.decl`, `cpp.scope.opover.def` |
| CP-A2-017 | 3 | cpptools | cpp | `semantic stringLiteral.` | function | unit | `cpp.udl.char`, `cpp.udl.string` |
| CP-A2-018 | 3 | rust | rust | `semantic unresolvedReference.` | error | macro | `rs.macro.call`, `rs.macro.call.println` |
| CP-A2-019 | 3 | clangd/cpptools | c | `(no scope)` | variable | comment | `c.pp.inactive.else` |
| CP-A2-020 | 3 | clangd/cpptools | c | `meta.block.c` | variable | qualifier | `c.kw.noreturn` |
| CP-A2-021 | 2 | clangd/T | c | `meta.function-call.c` | variable | function | `c.asm.goto.label` |
| CP-A2-022 | 2 | cpptools/T | cpp | `keyword.operator.arithmetic.cpp` | quietop | hazard | `cpp.op.deref` |
| CP-A2-023 | 3 | clangd/T | cpp | `keyword.other.suffix.literal.user-defined.character.cpp` | keyword | unit | `cpp.udl.char` |
| CP-A2-024 | 3 | clangd/T | cpp | `keyword.other.suffix.literal.user-defined.string.cpp` | keyword | unit | `cpp.udl.string` |
| CP-A2-025 | 3 | T | diff | `punctuation.definition.from-file.diff` | punct | comment | `diff.ctx.from`, `diff.from` |
| CP-A2-026 | 2 | T | dts | `variable.name.dts` | member | function | `dts.phandle`, `dts.ref.node` |
| CP-A2-027 | 3 | Pylance/T | python | `punctuation.separator.continuation.line.python` | punct | escape | `py.line.continuation` |
| CP-A2-028 | 3 | Pylance/T | python | `storage.type.imaginary.number.python` | prim|typeparam | unit | `py.number.imag` |
| CP-A2-029 | 3 | Pylance/T | python | `string.regexp.quoted.single.python` | escape | string | `py.rawbytes` |
| CP-A2-030 | 3 | Pylance/T | python | `support.other.escape.special.regexp` | escape | string | `py.raw.string` |
| CP-A2-031 | 3 | rust/T | rust | `keyword.operator.logical.rust` | keyword | quietop | `rs.closure.pipe` |
| CP-A2-032 | 3 | T | shell | `punctuation.definition.string.begin.shell` | punct | string | `sh.ansi.string`, `sh.procsubst` |
| CP-A2-033 | 3 | T | shell | `string.quoted.single.dollar.shell` | string | escape | `sh.escape.hex`, `sh.escape.octal` |
| CP-A2-034 | 3 | clangd | c | `semantic variable.declaration.definition.fileScope` | globalvar | staticvar | `c.var.static.file` |
| CP-A2-035 | 3 | clangd | c | `semantic variable.fileScope` | globalvar | staticvar | `c.var.static.use` |
| CP-A2-036 | 3 | EvenBetterTOML | config | `semantic tomlArrayKey.` | variable | member | `toml.key.dotted` |
| CP-A2-037 | 2 | clangd | cpp | `semantic class.declaration.definition.constructorOrDestructor.globalScope` | composite|doctag | function | `cpp.dtor.decl` |
| CP-A2-038 | 2 | clangd | cpp | `semantic concept.declaration.globalScope` | variable | composite | `cpp.concept.name` |
| CP-A2-039 | 3 | cpptools | cpp | `semantic function.` | function | variable | `cpp.lambda.call` |
| CP-A2-040 | 2 | cpptools | cpp | `semantic method.static` | method | function | `cpp.scope.static.call` |
| CP-A2-041 | 3 | clangd | cpp | `semantic variable.declaration.definition.globalScope` | globalvar | unit | `cpp.number.suffix.float` |
| CP-A2-042 | 3 | cpptools | cpp | `semantic variable.global` | globalvar | unit | `cpp.number.suffix.float` |
| CP-A2-043 | 3 | Pylance | python | `semantic function.library` | function | directive | `py.import.name` |
| CP-A2-044 | 2 | rust | rust | `semantic enum.defaultLibrary.library` | composite|doctag | prim | `rs.kw.result` |
| CP-A2-045 | 2 | rust | rust | `semantic function.static.defaultLibrary.associated.constant.library` | libfn | function | `rs.assocfn.call` |
| CP-A2-046 | 2 | rust | rust | `semantic operator.mutable` | quietop | hazard | `rs.op.bitxor` |
| CP-A2-047 | 3 | T | asm | `(no scope)` | variable | directive | `asm.equ` |
| CP-A2-048 | 3 | T | asm | `storage.memaddress.arm` | variable | punct | `asm.mem.bracket` |
| CP-A2-049 | 3 | T | asm | `storage.stack.arm` | variable | punct | `asm.reglist.brace` |
| CP-A2-050 | 3 | T | c | `constant.language.c` | number | macro | `c.macro.use.stdlib` |
| CP-A2-051 | 2 | clangd | c | `keyword.operator.c` | quietop | hazard | `c.ptr.declarator` |
| CP-A2-052 | 3 | T | c | `meta.conditional.case.c` | variable | number | `c.enum.member.use` |
| CP-A2-053 | 3 | T | cmake | `(no scope)` | variable | globalvar | `cm.var.name` |
| CP-A2-054 | 2 | T | cmake | `punctuation.definition.generator-expression.begin.cmake` | punct | hazard | `cm.genex.open` |
| CP-A2-055 | 3 | T | config | `entity.other.document.begin.yaml` | variable | punct | `yaml.doc.begin` |
| CP-A2-056 | 3 | T | config | `entity.other.document.end.yaml` | variable | punct | `yaml.doc.end` |
| CP-A2-057 | 3 | T | config | `keyword.operator.yaml` | quietop | member | `yaml.merge.key` |
| CP-A2-058 | 3 | T | config | `meta.block-mapping.yaml` | variable | punct | `yaml.explicit.key` |
| CP-A2-059 | 2 | T | config | `punctuation.definition.block.sequence.item.yaml` | punct | keyword | `yaml.list.dash` |
| CP-A2-060 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | composite | `cpp.enum.type.use` |
| CP-A2-061 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | function | `cpp.scope.dtor.def` |
| CP-A2-062 | 3 | T | cpp | `entity.name.scope-resolution.cpp` | variable | namespace | `cpp.ns.use` |
| CP-A2-063 | 2 | T | cpp | `meta.head.struct.cpp` | variable | composite | `cpp.class.base.use` |
| CP-A2-064 | 3 | T | cpp | `variable.other.declare.cpp` | variable | member | `cpp.member.decl` |
| CP-A2-065 | 3 | T | cpp | `variable.other.unknown.On.cpp` | variable | number | `cpp.enum.member.use` |
| CP-A2-066 | 2 | T | cpp | `variable.other.unknown.Small.cpp` | variable | composite | `cpp.concept.name` |
| CP-A2-067 | 3 | T | cpp | `variable.other.unknown.count.cpp` | variable | staticvar | `cpp.member.static.decl` |
| CP-A2-068 | 3 | T | cpp | `variable.other.unknown.fl.cpp` | variable | unit | `cpp.number.suffix.float` |
| CP-A2-069 | 3 | T | diff | `meta.diff.only-in` | variable | comment | `diff.onlyin` |
| CP-A2-070 | 3 | T | diff | `punctuation.definition.range.diff` | punct | directive | `diff.range` |
| CP-A2-071 | 3 | T | diff | `punctuation.definition.to-file.diff` | punct | comment | `diff.to` |
| CP-A2-072 | 2 | T | git | `markup.deleted.git-commit` | error | keyword | `git.filetype.deleted` |
| CP-A2-073 | 2 | T | git | `markup.inserted.git-commit` | string | keyword | `git.filetype.new` |
| CP-A2-074 | 3 | T | ld | `variable.other.ld` | variable | globalvar | `ld.symbol.def` |
| CP-A2-075 | 2 | T | ld | `variable.other.ld` | variable | hazard | `ld.location.counter` |
| CP-A2-076 | 3 | T | ld | `variable.other.ld` | variable | qualifier | `ld.region.attr` |
| CP-A2-077 | 3 | T | make | `(no scope)` | variable | member | `mk.recipe.flag` |
| CP-A2-078 | 2 | T | make | `meta.scope.prerequisites.makefile` | variable | function | `mk.prereq` |
| CP-A2-079 | 2 | T | markdown | `meta.paragraph.markdown` | variable | function | `md.setext1` |
| CP-A2-080 | 3 | T | python | `meta.attribute.python` | variable | member | `py.attr.use` |
| CP-A2-081 | 3 | T | python | `meta.function-call.generic.python` | function | method | `py.method.lib` |
| CP-A2-082 | 3 | T | python | `support.function.magic.python` | libfn | method | `py.magic.call` |
| CP-A2-083 | 3 | T | python | `support.type.metaclass.python` | prim|typeparam | param | `py.metaclass.kw` |
| CP-A2-084 | 3 | T | python | `support.variable.magic.python` | variable | method | `py.dunder.decl` |
| CP-A2-085 | 3 | T | rust | `(no scope)` | variable | member | `rs.field.use` |
| CP-A2-086 | 3 | T | rust | `comment.line.double-slash.rust` | comment | doc | `rs.doc.inner` |
| CP-A2-087 | 2 | T | rust | `entity.name.function.macro.rules.rust` | macro | keyword | `rs.macro.rules` |
| CP-A2-088 | 3 | T | rust | `entity.name.type.option.rust` | composite|doctag | number | `rs.option.some` |
| CP-A2-089 | 3 | T | rust | `entity.name.type.rust` | composite|doctag | directive | `rs.attr.derive.item` |
| CP-A2-090 | 2 | T | rust | `entity.name.type.rust` | composite|doctag | prim | `rs.kw.result` |
| CP-A2-091 | 2 | T | rust | `keyword.operator.assignment.rust` | quietop | hazard | `rs.op.bitxor` |
| CP-A2-092 | 3 | T | rust | `keyword.operator.exponent.rust` | quietop | unit | `rs.number.exp` |
| CP-A2-093 | 3 | T | rust | `keyword.operator.exponent.sign.rust` | quietop | unit | `rs.number.exp.sign` |
| CP-A2-094 | 3 | T | rust | `keyword.operator.namespace.rust` | quietop | namespace | `rs.scope.op` |
| CP-A2-095 | 3 | T | rust | `meta.use.rust` | variable | namespace | `rs.ns.module` |
| CP-A2-096 | 2 | T | rust | `storage.modifier.rust` | qualifier | keyword | `rs.kw.static` |
| CP-A2-097 | 2 | T | rust | `variable.language.super.rust` | hazard | keyword | `rs.kw.super` |
| CP-A2-098 | 3 | T | rust | `variable.other.rust` | variable | param | `rs.param.decl` |
| CP-A2-099 | 3 | T | shell | `(no scope)` | unmapped: | quietop | `sh.tilde` |
| CP-A2-100 | 3 | T | shell | `keyword.operator.logical.regex.shell` | keyword | quietop | `sh.regex.match` |
| CP-A2-101 | 3 | T | shell | `keyword.operator.logical.shell` | keyword | member | `sh.flag.test` |
| CP-A2-102 | 2 | T | shell | `storage.type.alias.shell` | prim|typeparam | keyword | `sh.alias.kw` |
| CP-A2-103 | 2 | T | shell | `variable.other.assignment.shell` | globalvar | function | `sh.alias.name` |
