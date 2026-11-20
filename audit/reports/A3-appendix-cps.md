# A3 appendix: change proposals

One proposal per distinguishing selector. Each needs its what-if run (predicted moves) at the start of the edit phase; the selector shown is the evidence, the final rule may be narrower (language suffix, parent scope).

| CP | Sev | Mode | Lang | Selector | Now | Should be | Components |
|---|---|---|---|---|---|---|---|
| CP-A3-001 | 2 | clangd/cpptools/T | cpp | `storage.type.built-in.primitive.cpp` | prim|typeparam | keyword | `cpp.kw.auto`, `cpp.type.auto` |
| CP-A3-002 | 2 | clangd/cpptools | c | `entity.name.function.c` | function | keyword | `c.kw.static_assert.macro`, `c.kw.typeof` |
| CP-A3-003 | 2 | clangd/cpptools/T | cpp | `punctuation.section.attribute.begin.cpp` | punct | keyword | `cpp.kw.alignas` |
| CP-A3-004 | 2 | cpptools | cpp | `semantic memberOperatorOverload.` | libfn | function | `cpp.op.overload.decl`, `cpp.scope.opover.def` |
| CP-A3-005 | 3 | rust | rust | `semantic unresolvedReference.` | error | macro | `rs.macro.call`, `rs.macro.call.println` |
| CP-A3-006 | 3 | clangd/cpptools | c | `(no scope)` | variable | comment | `c.pp.inactive.else` |
| CP-A3-007 | 3 | clangd/cpptools | c | `meta.block.c` | variable | qualifier | `c.kw.noreturn` |
| CP-A3-008 | 2 | clangd/T | c | `meta.function-call.c` | variable | function | `c.asm.goto.label` |
| CP-A3-009 | 2 | cpptools/T | cpp | `keyword.operator.arithmetic.cpp` | quietop | hazard | `cpp.op.deref` |
| CP-A3-010 | 3 | rust/T | rust | `keyword.operator.logical.rust` | keyword | quietop | `rs.closure.pipe` |
| CP-A3-011 | 3 | T | shell | `string.quoted.single.dollar.shell` | string | escape | `sh.escape.hex`, `sh.escape.octal` |
| CP-A3-012 | 3 | cpptools | cpp | `semantic function.` | function | variable | `cpp.lambda.call` |
| CP-A3-013 | 2 | cpptools | cpp | `semantic method.static` | method | function | `cpp.scope.static.call` |
| CP-A3-014 | 2 | rust | rust | `semantic operator.mutable` | quietop | hazard | `rs.op.bitxor` |
| CP-A3-015 | 3 | T | asm | `(no scope)` | variable | directive | `asm.equ` |
| CP-A3-016 | 3 | T | c | `constant.language.c` | number | macro | `c.macro.use.stdlib` |
| CP-A3-017 | 2 | clangd | c | `keyword.operator.c` | quietop | hazard | `c.ptr.declarator` |
| CP-A3-018 | 3 | T | c | `meta.conditional.case.c` | variable | number | `c.enum.member.use` |
| CP-A3-019 | 3 | T | cmake | `(no scope)` | variable | globalvar | `cm.var.name` |
| CP-A3-020 | 3 | T | config | `meta.block-mapping.yaml` | variable | punct | `yaml.explicit.key` |
| CP-A3-021 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | composite | `cpp.enum.type.use` |
| CP-A3-022 | 2 | T | cpp | `entity.name.scope-resolution.cpp` | variable | function | `cpp.scope.dtor.def` |
| CP-A3-023 | 3 | T | cpp | `entity.name.scope-resolution.cpp` | variable | namespace | `cpp.ns.use` |
| CP-A3-024 | 2 | T | cpp | `meta.head.struct.cpp` | variable | composite | `cpp.class.base.use` |
| CP-A3-025 | 3 | T | cpp | `variable.other.unknown.On.cpp` | variable | number | `cpp.enum.member.use` |
| CP-A3-026 | 2 | T | cpp | `variable.other.unknown.Small.cpp` | variable | composite | `cpp.concept.name` |
| CP-A3-027 | 3 | T | cpp | `variable.other.unknown.count.cpp` | variable | staticvar | `cpp.member.static.decl` |
| CP-A3-028 | 2 | T | ld | `variable.other.ld` | variable | hazard | `ld.location.counter` |
| CP-A3-029 | 3 | T | ld | `variable.other.ld` | variable | qualifier | `ld.region.attr` |
| CP-A3-030 | 3 | T | make | `(no scope)` | variable | member | `mk.recipe.flag` |
| CP-A3-031 | 2 | T | markdown | `meta.paragraph.markdown` | variable | function | `md.setext1` |
| CP-A3-032 | 3 | T | python | `meta.attribute.python` | variable | member | `py.attr.use` |
| CP-A3-033 | 3 | T | python | `meta.function-call.generic.python` | function | method | `py.method.lib` |
| CP-A3-034 | 3 | T | rust | `(no scope)` | variable | member | `rs.field.use` |
| CP-A3-035 | 3 | T | rust | `comment.line.double-slash.rust` | comment | doc | `rs.doc.inner` |
| CP-A3-036 | 3 | T | rust | `entity.name.type.rust` | composite|doctag | directive | `rs.attr.derive.item` |
| CP-A3-037 | 2 | T | rust | `keyword.operator.assignment.rust` | quietop | hazard | `rs.op.bitxor` |
| CP-A3-038 | 3 | T | rust | `meta.use.rust` | variable | namespace | `rs.ns.module` |
| CP-A3-039 | 3 | T | rust | `variable.other.rust` | variable | param | `rs.param.decl` |
| CP-A3-040 | 3 | T | shell | `(no scope)` | unmapped: | quietop | `sh.tilde` |
| CP-A3-041 | 3 | T | shell | `keyword.operator.logical.shell` | keyword | member | `sh.flag.test` |
