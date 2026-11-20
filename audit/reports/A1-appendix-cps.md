# A1 appendix: change proposals

One proposal per distinguishing selector. Each needs its what-if run (predicted moves) at the start of the edit phase; the selector shown is the evidence, the final rule may be narrower (language suffix, parent scope).

Severity here is computed from how many corpus components a selector affects. A1 §5 raises the ones that hit very common constructs (square brackets, Rust type keywords and primitives) regardless of count.

| CP | Sev | Mode | Lang | Selector | Now | Should be | Components |
|---|---|---|---|---|---|---|---|
| CP-A1-001 | 2 | clangd/cpptools/T | cpp | `storage.type.class.cpp` | composite|doctag | keyword | `cpp.class.kw`, `cpp.kw.class.fwd` |
| CP-A1-002 | 3 | clangd/cpptools/T | cpp | `storage.type.extern.cpp` | prim|typeparam | qualifier | `cpp.extern.block`, `cpp.kw.extern.c` |
| CP-A1-003 | 2 | clangd/cpptools/T | cpp | `storage.type.struct.cpp` | composite|doctag | keyword | `cpp.kw.struct`, `cpp.struct.fwd` |
| CP-A1-004 | 1 | T | rust | `storage.type.rust` | prim|typeparam | keyword | `rs.kw.enum`, `rs.kw.let`, `rs.kw.mod`, `rs.kw.struct`, `rs.kw.trait`, `rs.kw.type` |
| CP-A1-005 | 2 | clangd/cpptools/T | cpp | `keyword.other.operator.overload.cpp` | keyword | function | `cpp.op.conversion`, `cpp.op.new.overload` |
| CP-A1-006 | 2 | clangd/cpptools/T | cpp | `storage.type.built-in.primitive.cpp` | prim|typeparam | keyword | `cpp.kw.auto`, `cpp.type.auto` |
| CP-A1-007 | 1 | T | asm | `storage.register.arm` | variable | hazard | `asm.pc`, `asm.register`, `asm.register.sp`, `asm.writeback` |
| CP-A1-008 | 2 | clangd/cpptools | c | `entity.name.function.c` | function | keyword | `c.kw.static_assert.macro`, `c.kw.typeof` |
| CP-A1-009 | 2 | cpptools/T | cpp | `storage.type.decltype.cpp` | prim|typeparam | keyword | `cpp.decltype.auto`, `cpp.kw.decltype` |
| CP-A1-010 | 2 | Pylance/T | python | `storage.modifier.declaration.python` | qualifier | keyword | `py.kw.global`, `py.kw.nonlocal` |
| CP-A1-011 | 1 | clangd | cpp | `semantic type.deduced.defaultLibrary.globalScope` | prim|typeparam | keyword | `cpp.decltype.auto`, `cpp.kw.decltype`, `cpp.type.auto` |
| CP-A1-012 | 1 | Pylance | python | `semantic class.builtin` | composite|doctag | prim | `py.class.base`, `py.exception.builtin`, `py.metaclass.builtin` |
| CP-A1-013 | 3 | clangd/cpptools/T | c | `entity.name.other.preprocessor.macro.predefined.probably.VA_ARGS.c` | macro | param | `c.macro.va_args` |
| CP-A1-014 | 3 | clangd/cpptools/T | c | `punctuation.definition.begin.bracket.square.c` | member | punct | `c.array.decl.size` |
| CP-A1-015 | 3 | clangd/cpptools/T | c | `punctuation.definition.comment.begin.documentation.c` | comment | doc | `c.doc.block` |
| CP-A1-016 | 2 | clangd/cpptools/T | c | `storage.type.asm.c` | prim|typeparam | keyword | `c.kw.asm` |
| CP-A1-017 | 2 | clangd/cpptools/T | c | `storage.type.enum.c` | composite|doctag | keyword | `c.type.enum.kw` |
| CP-A1-018 | 2 | clangd/cpptools/T | c | `storage.type.struct.c` | composite|doctag | keyword | `c.type.struct.kw` |
| CP-A1-019 | 2 | clangd/cpptools/T | c | `storage.type.union.c` | composite|doctag | keyword | `c.type.union.kw` |
| CP-A1-020 | 3 | clangd/cpptools/T | c | `variable.named.arm` | variable | string | `c.asm.operand.constraint` |
| CP-A1-021 | 3 | clangd/cpptools/T | c | `variable.parameter.preprocessor.c` | macro | param | `c.macro.param.def` |
| CP-A1-022 | 3 | clangd/cpptools/T | cpp | `entity.other.attribute.nodiscard.cpp` | variable | directive | `cpp.attr.std` |
| CP-A1-023 | 2 | clangd/cpptools/T | cpp | `keyword.operator.noexcept.cpp` | quietop | keyword | `cpp.noexcept.op` |
| CP-A1-024 | 3 | clangd/cpptools/T | cpp | `meta.encoding.cpp` | punct | string | `cpp.char.u8` |
| CP-A1-025 | 2 | clangd/cpptools/T | cpp | `punctuation.section.attribute.begin.cpp` | punct | keyword | `cpp.kw.alignas` |
| CP-A1-026 | 2 | clangd/cpptools/T | cpp | `storage.type.enum.cpp` | composite|doctag | keyword | `cpp.kw.enumclass` |
| CP-A1-027 | 2 | clangd/cpptools/T | cpp | `storage.type.namespace.alias.cpp` | composite|doctag | keyword | `cpp.ns.alias.kw` |
| CP-A1-028 | 2 | clangd/cpptools/T | cpp | `storage.type.namespace.definition.cpp` | composite|doctag | keyword | `cpp.ns.kw` |
| CP-A1-029 | 2 | clangd/cpptools/T | cpp | `storage.type.template.argument.typename.cpp` | composite|doctag | keyword | `cpp.kw.typename` |
| CP-A1-030 | 2 | clangd/cpptools/T | cpp | `storage.type.template.cpp` | composite|doctag | keyword | `cpp.kw.template` |
| CP-A1-031 | 2 | clangd/cpptools/T | cpp | `storage.type.union.cpp` | composite|doctag | keyword | `cpp.union.kw` |
| CP-A1-032 | 3 | clangd/cpptools/T | cpp | `variable.language.this.cpp` | hazard | param | `cpp.this.use` |
| CP-A1-033 | 2 | clangd/cpptools/T | cpp | `variable.other.unknown.requires.cpp` | variable | keyword | `cpp.kw.requires` |
| CP-A1-034 | 3 | clangd/cpptools/T | cpp | `variable.parameter.preprocessor.cpp` | macro | param | `cpp.macro.param` |
| CP-A1-035 | 1 | T | ld | `variable.other.ld` | variable | composite | `ld.discard`, `ld.region.use`, `ld.section.name` |
| CP-A1-036 | 1 | T | make | `punctuation.separator.key-value.makefile` | punct | quietop | `mk.assign.append`, `mk.assign.cond`, `mk.assign.op` |
| CP-A1-037 | 2 | clangd | cpp | `semantic class.declaration.definition.constructorOrDestructor.classScope` | composite|doctag | function | `cpp.ctor.decl`, `cpp.scope.ctor.def` |
| CP-A1-038 | 2 | cpptools | cpp | `semantic memberOperatorOverload.` | libfn | function | `cpp.op.overload.decl`, `cpp.scope.opover.def` |
| CP-A1-039 | 3 | cpptools | cpp | `semantic stringLiteral.` | function | unit | `cpp.udl.char`, `cpp.udl.string` |
| CP-A1-040 | 3 | Pylance | python | `semantic function.builtin` | function | libfn | `py.fn.builtin`, `py.fn.builtin.open` |
| CP-A1-041 | 3 | Pylance | python | `semantic magicFunction.declaration` | function | method | `py.dunder.decl`, `py.magic.call` |
| CP-A1-042 | 3 | rust | rust | `semantic unresolvedReference.` | error | macro | `rs.macro.call`, `rs.macro.call.println` |
| CP-A1-043 | 3 | clangd/cpptools | c | `(no scope)` | variable | comment | `c.pp.inactive.else` |
| CP-A1-044 | 3 | clangd/cpptools | c | `meta.block.c` | variable | qualifier | `c.kw.noreturn` |
| CP-A1-045 | 2 | clangd/T | c | `meta.function-call.c` | variable | function | `c.asm.goto.label` |
| CP-A1-046 | 3 | T | cmake | `support.type.property.cmake` | member | qualifier | `cm.kwarg`, `cm.kwarg.public` |
| CP-A1-047 | 2 | cpptools/T | cpp | `keyword.operator.arithmetic.cpp` | quietop | hazard | `cpp.op.deref` |
| CP-A1-048 | 3 | clangd/T | cpp | `keyword.other.suffix.literal.user-defined.character.cpp` | keyword | unit | `cpp.udl.char` |
| CP-A1-049 | 3 | clangd/T | cpp | `keyword.other.suffix.literal.user-defined.string.cpp` | keyword | unit | `cpp.udl.string` |
| CP-A1-050 | 3 | T | diff | `punctuation.definition.from-file.diff` | punct | comment | `diff.ctx.from`, `diff.from` |
| CP-A1-051 | 2 | T | dts | `entity.name.function.dts` | function | composite | `dts.node.name`, `dts.node.unit` |
| CP-A1-052 | 2 | T | dts | `variable.name.dts` | member | function | `dts.phandle`, `dts.ref.node` |
| CP-A1-053 | 2 | T | kconfig | `variable.language.kconfig` | hazard | keyword | `kc.config`, `kc.menu` |
| CP-A1-054 | 3 | T | markdown | `string.other.link.title.markdown` | composite|doctag | variable | `md.link.text`, `md.ref.link` |
| CP-A1-055 | 3 | Pylance/T | python | `punctuation.separator.continuation.line.python` | punct | escape | `py.line.continuation` |
| CP-A1-056 | 2 | Pylance/T | python | `storage.type.class.python` | composite|doctag | keyword | `py.kw.class` |
| CP-A1-057 | 3 | Pylance/T | python | `storage.type.imaginary.number.python` | prim|typeparam | unit | `py.number.imag` |
| CP-A1-058 | 3 | Pylance/T | python | `string.regexp.quoted.single.python` | escape | string | `py.rawbytes` |
| CP-A1-059 | 3 | Pylance/T | python | `support.other.escape.special.regexp` | escape | string | `py.raw.string` |
| CP-A1-060 | 2 | T | rust | `entity.name.type.numeric.rust` | composite|doctag | prim | `rs.type.prim`, `rs.type.prim.u8` |
| CP-A1-061 | 3 | rust/T | rust | `keyword.operator.logical.rust` | keyword | quietop | `rs.closure.pipe` |
| CP-A1-062 | 3 | T | shell | `punctuation.definition.string.begin.shell` | punct | string | `sh.ansi.string`, `sh.procsubst` |
| CP-A1-063 | 3 | T | shell | `string.quoted.single.dollar.shell` | string | escape | `sh.escape.hex`, `sh.escape.octal` |
| CP-A1-064 | 3 | clangd | c | `semantic variable.declaration.definition.fileScope` | globalvar | staticvar | `c.var.static.file` |
| CP-A1-065 | 3 | clangd | c | `semantic variable.fileScope` | globalvar | staticvar | `c.var.static.use` |
| CP-A1-066 | 3 | EvenBetterTOML | config | `semantic tomlArrayKey.` | variable | member | `toml.key.dotted` |
| CP-A1-067 | 2 | clangd | cpp | `semantic class.declaration.definition.constructorOrDestructor.globalScope` | composite|doctag | function | `cpp.dtor.decl` |
| CP-A1-068 | 2 | clangd | cpp | `semantic concept.declaration.globalScope` | variable | composite | `cpp.concept.name` |
| CP-A1-069 | 3 | cpptools | cpp | `semantic function.` | function | variable | `cpp.lambda.call` |
| CP-A1-070 | 2 | cpptools | cpp | `semantic method.static` | method | function | `cpp.scope.static.call` |
| CP-A1-071 | 3 | clangd | cpp | `semantic variable.declaration.definition.globalScope` | globalvar | unit | `cpp.number.suffix.float` |
| CP-A1-072 | 3 | cpptools | cpp | `semantic variable.global` | globalvar | unit | `cpp.number.suffix.float` |
| CP-A1-073 | 3 | Pylance | python | `semantic class.decorator.builtin` | composite|doctag | directive | `py.decorator.builtin` |
| CP-A1-074 | 2 | Pylance | python | `semantic class.typeHint.builtin` | composite|doctag | prim | `py.typehint.builtin` |
| CP-A1-075 | 3 | Pylance | python | `semantic function.decorator.library` | function | directive | `py.decorator.name` |
| CP-A1-076 | 3 | Pylance | python | `semantic function.library` | function | directive | `py.import.name` |
| CP-A1-077 | 3 | Pylance | python | `semantic variable.classMember` | variable | member | `py.attr.use` |
| CP-A1-078 | 3 | Pylance | python | `semantic variable.declaration.classMember` | variable | member | `py.field.decl` |
| CP-A1-079 | 3 | rust | rust | `semantic const.constant.public` | variable | number | `rs.const.use` |
| CP-A1-080 | 3 | rust | rust | `semantic const.declaration.constant.public` | variable | number | `rs.const.decl` |
| CP-A1-081 | 2 | rust | rust | `semantic enum.defaultLibrary.library` | composite|doctag | prim | `rs.kw.result` |
| CP-A1-082 | 2 | rust | rust | `semantic function.static.defaultLibrary.associated.constant.library` | libfn | function | `rs.assocfn.call` |
| CP-A1-083 | 2 | rust | rust | `semantic operator.mutable` | quietop | hazard | `rs.op.bitxor` |
| CP-A1-084 | 3 | rust | rust | `semantic static.declaration.mutable.public.unsafe` | variable | staticvar | `rs.static.decl` |
| CP-A1-085 | 3 | T | asm | `(no scope)` | variable | directive | `asm.equ` |
| CP-A1-086 | 2 | T | asm | `routine.arm` | variable | function | `asm.label.def` |
| CP-A1-087 | 3 | T | asm | `storage.memaddress.arm` | variable | punct | `asm.mem.bracket` |
| CP-A1-088 | 3 | T | asm | `storage.stack.arm` | variable | punct | `asm.reglist.brace` |
| CP-A1-089 | 3 | T | c | `constant.language.c` | number | macro | `c.macro.use.stdlib` |
| CP-A1-090 | 2 | clangd | c | `keyword.operator.c` | quietop | hazard | `c.ptr.declarator` |
| CP-A1-091 | 3 | T | c | `meta.conditional.case.c` | variable | number | `c.enum.member.use` |
| CP-A1-092 | 3 | T | cmake | `(no scope)` | variable | globalvar | `cm.var.name` |
| CP-A1-093 | 2 | T | cmake | `punctuation.definition.generator-expression.begin.cmake` | punct | hazard | `cm.genex.open` |
| CP-A1-094 | 3 | T | cmake | `variable.parameter.cmake` | param | string | `cm.bracket.arg` |
| CP-A1-095 | 3 | T | config | `entity.other.document.begin.yaml` | variable | punct | `yaml.doc.begin` |
| CP-A1-096 | 3 | T | config | `entity.other.document.end.yaml` | variable | punct | `yaml.doc.end` |
| CP-A1-097 | 3 | T | config | `keyword.operator.yaml` | quietop | member | `yaml.merge.key` |
| CP-A1-098 | 3 | T | config | `meta.block-mapping.yaml` | variable | punct | `yaml.explicit.key` |
| CP-A1-099 | 2 | T | config | `punctuation.definition.block.sequence.item.yaml` | punct | keyword | `yaml.list.dash` |
| CP-A1-100 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | composite | `cpp.enum.type.use` |
| CP-A1-101 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | function | `cpp.scope.dtor.def` |
| CP-A1-102 | 3 | T | cpp | `entity.name.scope-resolution.cpp` | variable | namespace | `cpp.ns.use` |
| CP-A1-103 | 3 | T | cpp | `entity.name.type.template.cpp` | composite|doctag | typeparam | `cpp.tparam.decl` |
| CP-A1-104 | 2 | T | cpp | `meta.head.struct.cpp` | variable | composite | `cpp.class.base.use` |
| CP-A1-105 | 3 | T | cpp | `variable.other.declare.cpp` | variable | member | `cpp.member.decl` |
| CP-A1-106 | 3 | T | cpp | `variable.other.unknown.On.cpp` | variable | number | `cpp.enum.member.use` |
| CP-A1-107 | 2 | T | cpp | `variable.other.unknown.Small.cpp` | variable | composite | `cpp.concept.name` |
| CP-A1-108 | 3 | T | cpp | `variable.other.unknown.count.cpp` | variable | staticvar | `cpp.member.static.decl` |
| CP-A1-109 | 3 | T | cpp | `variable.other.unknown.fl.cpp` | variable | unit | `cpp.number.suffix.float` |
| CP-A1-110 | 3 | T | diff | `meta.diff.only-in` | variable | comment | `diff.onlyin` |
| CP-A1-111 | 3 | T | diff | `punctuation.definition.range.diff` | punct | directive | `diff.range` |
| CP-A1-112 | 3 | T | diff | `punctuation.definition.to-file.diff` | punct | comment | `diff.to` |
| CP-A1-113 | 2 | T | dts | `entity.name.type.dts` | composite|doctag | function | `dts.label.def` |
| CP-A1-114 | 2 | T | git | `markup.deleted.git-commit` | error | keyword | `git.filetype.deleted` |
| CP-A1-115 | 2 | T | git | `markup.inserted.git-commit` | string | keyword | `git.filetype.new` |
| CP-A1-116 | 2 | T | git | `meta.scope.subject.git-commit` | variable | keyword | `git.subject` |
| CP-A1-117 | 3 | T | ld | `variable.other.ld` | variable | globalvar | `ld.symbol.def` |
| CP-A1-118 | 2 | T | ld | `variable.other.ld` | variable | hazard | `ld.location.counter` |
| CP-A1-119 | 3 | T | ld | `variable.other.ld` | variable | qualifier | `ld.region.attr` |
| CP-A1-120 | 3 | T | make | `(no scope)` | variable | member | `mk.recipe.flag` |
| CP-A1-121 | 2 | T | make | `meta.scope.prerequisites.makefile` | variable | function | `mk.prereq` |
| CP-A1-122 | 2 | T | make | `support.function.target.PHONY.makefile` | libfn | keyword | `mk.phony` |
| CP-A1-123 | 3 | T | markdown | `markup.inline.raw.string.markdown` | number | string | `md.code.inline` |
| CP-A1-124 | 2 | T | markdown | `meta.paragraph.markdown` | variable | function | `md.setext1` |
| CP-A1-125 | 2 | T | markdown | `storage.type.class.cpp` | composite|doctag | keyword | `md.fence.cpp.keyword` |
| CP-A1-126 | 3 | T | python | `meta.attribute.python` | variable | member | `py.attr.use` |
| CP-A1-127 | 3 | T | python | `meta.function-call.generic.python` | function | method | `py.method.lib` |
| CP-A1-128 | 3 | T | python | `support.function.magic.python` | libfn | method | `py.magic.call` |
| CP-A1-129 | 3 | T | python | `support.type.metaclass.python` | prim|typeparam | param | `py.metaclass.kw` |
| CP-A1-130 | 3 | T | python | `support.type.python` | prim|typeparam | directive | `py.decorator.builtin` |
| CP-A1-131 | 3 | T | python | `support.variable.magic.python` | member | method | `py.dunder.decl` |
| CP-A1-132 | 3 | T | rust | `(no scope)` | variable | member | `rs.field.use` |
| CP-A1-133 | 3 | T | rust | `comment.line.double-slash.rust` | comment | doc | `rs.doc.inner` |
| CP-A1-134 | 2 | T | rust | `entity.name.function.macro.rules.rust` | macro | keyword | `rs.macro.rules` |
| CP-A1-135 | 3 | T | rust | `entity.name.type.numeric.rust` | composite|doctag | unit | `rs.number.suffix` |
| CP-A1-136 | 3 | T | rust | `entity.name.type.option.rust` | composite|doctag | number | `rs.option.some` |
| CP-A1-137 | 2 | T | rust | `entity.name.type.primitive.rust` | composite|doctag | prim | `rs.type.str` |
| CP-A1-138 | 3 | T | rust | `entity.name.type.rust` | composite|doctag | directive | `rs.attr.derive.item` |
| CP-A1-139 | 2 | T | rust | `entity.name.type.rust` | composite|doctag | prim | `rs.kw.result` |
| CP-A1-140 | 2 | T | rust | `keyword.operator.assignment.rust` | quietop | hazard | `rs.op.bitxor` |
| CP-A1-141 | 3 | T | rust | `keyword.operator.exponent.rust` | quietop | unit | `rs.number.exp` |
| CP-A1-142 | 3 | T | rust | `keyword.operator.exponent.sign.rust` | quietop | unit | `rs.number.exp.sign` |
| CP-A1-143 | 3 | T | rust | `keyword.operator.namespace.rust` | quietop | namespace | `rs.scope.op` |
| CP-A1-144 | 3 | T | rust | `meta.use.rust` | variable | namespace | `rs.ns.module` |
| CP-A1-145 | 2 | T | rust | `punctuation.definition.interpolation.rust` | punct | hazard | `rs.format.spec` |
| CP-A1-146 | 2 | T | rust | `storage.modifier.rust` | qualifier | keyword | `rs.kw.static` |
| CP-A1-147 | 2 | T | rust | `variable.language.super.rust` | hazard | keyword | `rs.kw.super` |
| CP-A1-148 | 3 | T | rust | `variable.other.rust` | variable | param | `rs.param.decl` |
| CP-A1-149 | 3 | T | shell | `(no scope)` | unmapped: | quietop | `sh.tilde` |
| CP-A1-150 | 3 | T | shell | `keyword.operator.logical.regex.shell` | keyword | quietop | `sh.regex.match` |
| CP-A1-151 | 3 | T | shell | `keyword.operator.logical.shell` | keyword | member | `sh.flag.test` |
| CP-A1-152 | 2 | T | shell | `punctuation.separator.statement.and.shell` | punct | keyword | `sh.op.and` |
| CP-A1-153 | 2 | T | shell | `storage.type.alias.shell` | prim|typeparam | keyword | `sh.alias.kw` |
| CP-A1-154 | 2 | T | shell | `variable.other.assignment.shell` | globalvar | function | `sh.alias.name` |
