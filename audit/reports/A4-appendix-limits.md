# A1 appendix: limits with proof

Computed proof: the component has exactly the same scope stack (grammar) or semantic type and modifiers (server) as a component with a different expected role, so no theme rule can colour both correctly.

| Mode | Lang | Cause | Components | Shares its tokens with |
|---|---|---|---|---|
| S clangd | c | grammar can't tell | `c.kw.static_assert` (keyword→function) | `c.attr.gnu`  |
| S clangd | c | grammar can't tell | `c.pp.inactive.else` (comment→variable) | `c.encoding.prefix`  |
| S clangd | c | grammar can't tell | `c.attr.gnu` (directive→function) | `c.kw.static_assert`  |
| S clangd | c | grammar can't tell | `c.encoding.prefix` (string→variable) | `c.pp.inactive.else`  |
| S clangd | c | grammar can't tell | `c.macro.param.use` (param→directive) | `c.pp.paste`  |
| S clangd | c | server can't tell | `c.type.bool` (prim→macro), `c.const.true` (number→macro) | `c.macro.use.cond`  |
| S clangd | c | server can't tell | `c.op.addressof` (hazard→quietop), `c.op.deref` (hazard→quietop), `c.op.bitassign` (hazard→quietop), `c.op.bitnot` (hazard→quietop), `c.op.bitand` (hazard→quietop) +7 | `c.op.arith`  |
| S clangd | cpp | server can't tell | `cpp.scope.dtor.def` (function→composite|doctag), `cpp.ool.dtor.name` (function→composite|doctag) | `cpp.class.use`  |
| S clangd | cpp | server can't tell | `cpp.lambda.capture.init` (param→variable) | `cpp.for.var`  |
| S clangd | cpp | server can't tell | `cpp.op.bitand` (hazard→quietop), `cpp.op.bitor` (hazard→quietop), `cpp.op.xor` (hazard→quietop), `cpp.op.not.bit` (hazard→quietop), `cpp.op.shift` (hazard→quietop) +3 | `cpp.kw.new`  |
| S clangd | cpp | server can't tell | `cpp.lambda.capture.var` (param→variable) | `cpp.lambda.call`  |
| S clangd | cpp | server can't tell | `cpp.kw.new` (keyword→quietop), `cpp.kw.delete` (keyword→quietop), `cpp.op.ternary` (keyword→quietop), `cpp.op.logical` (keyword→quietop), `cpp.kw.new.array` (keyword→quietop) +2 | `cpp.op.bitand`  |
| S cpptools | c | grammar can't tell | `c.kw.static_assert` (keyword→function) | `c.attr.gnu`  |
| S cpptools | c | grammar can't tell | `c.pp.inactive.else` (comment→variable) | `c.encoding.prefix`  |
| S cpptools | c | grammar can't tell | `c.attr.gnu` (directive→function) | `c.kw.static_assert`  |
| S cpptools | c | grammar can't tell | `c.ptr.declarator` (hazard→quietop), `c.op.addressof` (hazard→quietop), `c.op.deref` (hazard→quietop), `c.op.bitnot` (hazard→quietop), `c.op.bitand` (hazard→quietop) +2 | `c.op.arith`  |
| S cpptools | c | grammar can't tell | `c.encoding.prefix` (string→variable) | `c.pp.inactive.else`  |
| S cpptools | c | grammar can't tell | `c.macro.param.use` (param→directive) | `c.pp.paste`  |
| S cpptools | c | server can't tell | `c.fn.lib` (libfn→function), `c.fn.lib2` (libfn→function) | `c.fn.def`  |
| S cpptools | c | server can't tell | `c.type.bool` (prim→macro), `c.const.true` (number→macro) | `c.macro.name.def`  |
| S cpptools | c | server can't tell | `c.type.stdint` (prim→composite|doctag), `c.type.size_t` (prim→composite|doctag), `c.type.pthread` (prim→composite|doctag), `c.type.stdint.2` (prim→composite|doctag), `c.type.uintptr` (prim→composite|doctag) +3 | `c.type.typedef.def`  |
| S cpptools | c | server can't tell | `c.var.static.file` (staticvar→globalvar), `c.var.static.use` (staticvar→globalvar) | `c.var.global`  |
| S cpptools | c | server can't tell | `c.var.const.global` (number→globalvar) | `c.var.static.file`  |
| S cpptools | cpp | server can't tell | `cpp.tparam.decl` (typeparam→composite|doctag) | `cpp.class.name`  |
| S cpptools | cpp | server can't tell | `cpp.lambda.capture.var` (param→variable) | `cpp.for.var`  |
| S cpptools | cpp | server can't tell | `cpp.op.new.overload` (function→keyword) | `cpp.kw.new`  |
| S cpptools | cpp | server can't tell | `cpp.lambda.capture.init` (param→member) | `cpp.member.decl`  |
| S cpptools | cpp | server can't tell | `cpp.ctor.decl` (function→method), `cpp.dtor.decl` (function→method), `cpp.scope.ctor.def` (function→method), `cpp.ool.ctor.name` (function→method) | `cpp.method.decl`  |
| S cpptools | cpp | server can't tell | `cpp.scope.dtor.def` (function→composite|doctag), `cpp.posix.type` (prim→composite|doctag), `cpp.ool.dtor.name` (function→composite|doctag) | `cpp.tparam.decl`  |
| S cpptools | cpp | server can't tell | `cpp.udl.op.decl` (function→unit), `cpp.udl.suffix.decl` (function→unit) | `cpp.udl.literal`  |
| S cpptools | cpp | server can't tell | `cpp.udl.literal` (number→unit) | `cpp.udl.op.decl`  |
| S rust | rust | server can't tell | `rs.scope.op` (namespace→quietop) | `rs.borrow.mut`  |
| S rust | rust | server can't tell | `rs.qual.pub` (qualifier→keyword), `rs.qual.mut` (qualifier→keyword), `rs.qual.mut.self` (qualifier→keyword), `rs.rawptr` (hazard→keyword) | `rs.kw.use`  |
| S rust | rust | server can't tell | `rs.number.suffix` (unit→number), `rs.number.exp` (unit→number), `rs.number.exp.sign` (unit→number) | `rs.number.int`  |
| S rust | rust | server can't tell | `rs.borrow.mut` (hazard→quietop), `rs.borrow.ref` (hazard→quietop) | `rs.scope.op`  |
| S rust | rust | server can't tell | `rs.format.spec` (hazard→string), `rs.format.named` (hazard→string) | `rs.string`  |
| T | asm | grammar can't tell | `asm.symbol.ref` (globalvar→variable), `asm.equ.name` (globalvar→variable) | `asm.call.target`  |
| T | asm | grammar can't tell | `asm.call.target` (function→variable), `asm.label.ref` (function→variable) | `asm.symbol.ref`  |
| T | c | grammar can't tell | `c.enum.member.use` (number→variable) | `c.case.range`  |
| T | c | grammar can't tell | `c.member.decl` (member→variable), `c.member.ptr.decl` (member→variable), `c.member.bitfield` (member→variable), `c.member.designated` (member→variable) | `c.enum.member.decl`  |
| T | c | grammar can't tell | `c.case.range` (punct→variable) | `c.enum.member.use`  |
| T | c | grammar can't tell | `c.attr.gnu` (directive→function), `c.kw.static_assert` (keyword→function) | `c.fn.def`  |
| T | c | grammar can't tell | `c.macro.fn.use` (macro→function) | `c.fn.lib`  |
| T | c | grammar can't tell | `c.fn.lib` (libfn→function), `c.fn.lib2` (libfn→function), `c.kw.static_assert.macro` (keyword→function), `c.kw.typeof` (keyword→function) | `c.macro.fn.use`  |
| T | c | grammar can't tell | `c.enum.member.decl` (number→variable), `c.kw.noreturn` (qualifier→variable) | `c.member.decl`  |
| T | c | grammar can't tell | `c.ptr.declarator` (hazard→quietop), `c.op.addressof` (hazard→quietop), `c.op.deref` (hazard→quietop), `c.op.bitnot` (hazard→quietop), `c.op.bitand` (hazard→quietop) +2 | `c.op.arith`  |
| T | c | grammar can't tell | `c.macro.param.use` (param→directive) | `c.pp.paste`  |
| T | c | grammar can't tell | `c.pp.inactive.else` (comment→variable), `c.encoding.prefix` (string→variable) | `c.type.typedef.def`  |
| T | c | grammar can't tell | `c.type.typedef.def` (composite→variable), `c.type.struct.tag` (composite→variable), `c.type.enum.tag` (composite→variable) | `c.var.static.file`  |
| T | cmake | grammar can't tell | `cm.number` (number→variable) | `cm.fn.def.name`  |
| T | cmake | grammar can't tell | `cm.fn.def.name` (function→variable), `cm.prop` (member→variable) | `cm.number`  |
| T | config | grammar can't tell | `ini.value` (string→variable) | `ini.number`  |
| T | config | grammar can't tell | `ini.number` (number→variable), `ini.flag` (member→variable) | `ini.value`  |
| T | config | grammar can't tell | `yaml.date` (number→string) | `yaml.value.plain`  |
| T | cpp | grammar can't tell | `cpp.ctor.init.member` (member→function) | `cpp.ool.ctor.name`  |
| T | cpp | grammar can't tell | `cpp.scope.dtor.def` (function→variable), `cpp.ool.dtor.name` (function→variable) | `cpp.ool.dtor.owner`  |
| T | cpp | grammar can't tell | `cpp.ool.dtor.owner` (composite→variable), `cpp.tmpl.scope.call` (composite→variable) | `cpp.scope.dtor.def`  |
| T | dts | grammar can't tell | `dts.prop` (member→variable), `dts.prop.hash` (member→variable) | `dts.directive`  |
| T | dts | grammar can't tell | `dts.bracket.square` (punct→number) | `dts.macro`  |
| T | dts | grammar can't tell | `dts.macro` (macro→number) | `dts.number`  |
| T | dts | grammar can't tell | `dts.directive` (directive→variable) | `dts.prop`  |
| T | dts | grammar can't tell | `dts.escape` (escape→string) | `dts.string`  |
| T | git | grammar can't tell | `git.filename` (string→keyword) | `git.filetype.modified`  |
| T | kconfig | grammar can't tell | `kc.symbol.def` (globalvar→variable), `kc.symbol.use` (globalvar→variable) | `kc.number`  |
| T | kconfig | grammar can't tell | `kc.env.var` (globalvar→string) | `kc.prompt`  |
| T | kconfig | grammar can't tell | `kc.type` (prim→keyword), `kc.type.string` (prim→keyword), `kc.type.bool` (prim→keyword) | `kc.range`  |
| T | kconfig | grammar can't tell | `kc.number` (number→variable), `kc.help.text` (comment→variable), `kc.escape` (escape→variable) | `kc.symbol.def`  |
| T | ld | grammar can't tell | `ld.number` (number→variable), `ld.size.suffix` (unit→variable), `ld.number.dec` (number→variable) | `ld.entry.symbol`  |
| T | ld | grammar can't tell | `ld.region.name` (composite→keyword) | `ld.keep.2`  |
| T | ld | grammar can't tell | `ld.entry.symbol` (function→variable) | `ld.number`  |
| T | logs | grammar can't tell | `log.zephyr.bracket` (punct→variable) | `log.traceback`  |
| T | logs | grammar can't tell | `log.traceback` (error→variable), `log.exceptiontype` (error→variable) | `log.zephyr.bracket`  |
| T | python | grammar can't tell | `py.module` (namespace→variable), `py.module.dotted` (namespace→variable) | `py.import.name`  |
| T | python | grammar can't tell | `py.import.name` (libfn→variable) | `py.module`  |
| T | rust | grammar can't tell | `rs.static.decl` (staticvar→number) | `rs.const.decl`  |
| T | rust | grammar can't tell | `rs.tparam.decl` (typeparam→composite|doctag), `rs.tparam.use` (typeparam→composite|doctag) | `rs.enum.variant.decl`  |
| T | rust | grammar can't tell | `rs.closure.param` (param→variable) | `rs.field.decl`  |
| T | rust | grammar can't tell | `rs.qual.unsafe` (hazard→keyword), `rs.kw.unsafe.block` (hazard→keyword) | `rs.kw.impl`  |
| T | rust | grammar can't tell | `rs.label.decl` (function→prim|typeparam), `rs.label.use` (function→prim|typeparam) | `rs.lifetime.decl`  |
| T | rust | grammar can't tell | `rs.enum.variant.decl` (number→composite|doctag), `rs.enum.variant.use` (number→composite|doctag) | `rs.tparam.decl`  |
| T | rust | grammar can't tell | `rs.field.decl` (member→variable) | `rs.var.local`  |
| T | shell | grammar can't tell | `sh.array.at` (hazard→quietop) | `sh.param.op`  |
| T | shell | grammar can't tell | `sh.or.op` (keyword→quietop), `sh.or.sep` (keyword→quietop) | `sh.pipe`  |
