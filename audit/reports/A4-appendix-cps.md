# A4 appendix: change proposals

One proposal per distinguishing selector. Each needs its what-if run (predicted moves) at the start of the edit phase; the selector shown is the evidence, the final rule may be narrower (language suffix, parent scope).

| CP | Sev | Mode | Lang | Selector | Now | Should be | Components |
|---|---|---|---|---|---|---|---|
| CP-A4-001 | 2 | clangd/cpptools/T | cpp | `storage.type.built-in.primitive.cpp` | prim|typeparam | keyword | `cpp.kw.auto`, `cpp.type.auto` |
| CP-A4-002 | 2 | clangd/cpptools | c | `entity.name.function.c` | function | keyword | `c.kw.static_assert.macro`, `c.kw.typeof` |
| CP-A4-003 | 3 | clangd/cpptools/T | cpp | `meta.function.definition.parameters` | variable | punct | `cpp.vararg` |
| CP-A4-004 | 2 | clangd/cpptools/T | cpp | `punctuation.section.attribute.begin.cpp` | punct | keyword | `cpp.kw.alignas` |
| CP-A4-005 | 3 | clangd/cpptools/T | cpp | `variable.other.unknown.x.cpp` | variable | param | `cpp.macro.arg.use` |
| CP-A4-006 | 2 | cpptools | cpp | `semantic memberOperatorOverload.` | libfn | function | `cpp.op.overload.decl`, `cpp.scope.opover.def` |
| CP-A4-007 | 3 | rust | rust | `semantic unresolvedReference.` | error | macro | `rs.macro.call`, `rs.macro.call.println` |
| CP-A4-008 | 3 | clangd/cpptools | c | `meta.block.c` | variable | qualifier | `c.kw.noreturn` |
| CP-A4-009 | 3 | clangd/cpptools | c | `meta.conditional.case.c` | variable | punct | `c.case.range` |
| CP-A4-010 | 2 | clangd/T | c | `meta.function-call.c` | variable | function | `c.asm.goto.label` |
| CP-A4-011 | 2 | cpptools/T | cpp | `keyword.operator.arithmetic.cpp` | quietop | hazard | `cpp.op.deref` |
| CP-A4-012 | 3 | rust/T | rust | `keyword.operator.logical.rust` | keyword | quietop | `rs.closure.pipe` |
| CP-A4-013 | 3 | T | shell | `(no scope)` | unmapped: | quietop | `sh.tilde`, `sh.tilde.cd` |
| CP-A4-014 | 3 | T | shell | `string.quoted.single.dollar.shell` | string | escape | `sh.escape.hex`, `sh.escape.octal` |
| CP-A4-015 | 3 | cpptools | cpp | `semantic function.` | function | variable | `cpp.lambda.call` |
| CP-A4-016 | 2 | cpptools | cpp | `semantic method.static` | method | function | `cpp.scope.static.call` |
| CP-A4-017 | 2 | rust | rust | `semantic operator.mutable` | quietop | hazard | `rs.op.bitxor` |
| CP-A4-018 | 3 | T | asm | `(no scope)` | variable | directive | `asm.equ` |
| CP-A4-019 | 3 | T | c | `constant.language.c` | number | macro | `c.macro.use.stdlib` |
| CP-A4-020 | 2 | clangd | c | `keyword.operator.c` | quietop | hazard | `c.ptr.declarator` |
| CP-A4-021 | 3 | T | cmake | `(no scope)` | variable | globalvar | `cm.var.name` |
| CP-A4-022 | 3 | T | config | `meta.block-mapping.yaml` | variable | punct | `yaml.explicit.key` |
| CP-A4-023 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | composite | `cpp.enum.type.use` |
| CP-A4-024 | 3 | T | cpp | `entity.name.scope-resolution.cpp` | variable | namespace | `cpp.ns.use` |
| CP-A4-025 | 2 | T | cpp | `entity.name.scope-resolution.function.call.cpp` | variable | composite | `cpp.ool.ctor.owner` |
| CP-A4-026 | 2 | T | cpp | `meta.head.struct.cpp` | variable | composite | `cpp.class.base.use` |
| CP-A4-027 | 2 | T | cpp | `support.type.built-in.posix-reserved.cpp` | prim|typeparam | composite | `cpp.posix.user.type` |
| CP-A4-028 | 3 | T | cpp | `variable.other.assignment.cpp` | variable | member | `cpp.member.init.decl` |
| CP-A4-029 | 3 | T | cpp | `variable.other.unknown.On.cpp` | variable | number | `cpp.enum.member.use` |
| CP-A4-030 | 2 | T | cpp | `variable.other.unknown.Small.cpp` | variable | composite | `cpp.concept.name` |
| CP-A4-031 | 3 | T | cpp | `variable.other.unknown.count.cpp` | variable | staticvar | `cpp.member.static.decl` |
| CP-A4-032 | 2 | T | ld | `variable.other.ld` | variable | hazard | `ld.location.counter` |
| CP-A4-033 | 3 | T | ld | `variable.other.ld` | variable | qualifier | `ld.region.attr` |
| CP-A4-034 | 3 | T | make | `(no scope)` | variable | member | `mk.recipe.flag` |
| CP-A4-035 | 2 | T | markdown | `meta.paragraph.markdown` | variable | function | `md.setext1` |
| CP-A4-036 | 3 | T | python | `meta.attribute.python` | variable | member | `py.attr.use` |
| CP-A4-037 | 3 | T | python | `meta.function-call.generic.python` | function | method | `py.method.lib` |
| CP-A4-038 | 3 | T | rust | `(no scope)` | variable | member | `rs.field.use` |
| CP-A4-039 | 3 | T | rust | `comment.line.double-slash.rust` | comment | doc | `rs.doc.inner` |
| CP-A4-040 | 3 | T | rust | `entity.name.type.rust` | composite|doctag | directive | `rs.attr.derive.item` |
| CP-A4-041 | 2 | T | rust | `keyword.operator.assignment.rust` | quietop | hazard | `rs.op.bitxor` |
| CP-A4-042 | 3 | T | rust | `meta.use.rust` | variable | namespace | `rs.ns.module` |
| CP-A4-043 | 3 | T | rust | `variable.other.rust` | variable | param | `rs.param.decl` |
| CP-A4-044 | 3 | T | shell | `keyword.operator.logical.shell` | keyword | member | `sh.flag.test` |
| CP-A4-045 | 3 | T | shell | `meta.argument.shell` | variable | punct | `sh.arith.single` |
