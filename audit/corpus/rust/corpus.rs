//@ rs.doc.inner doc Corpus
//! Corpus for the Rosin audit.
//@ rs.attr.inner directive allow
#![allow(dead_code, unused)]

//@ rs.kw.use keyword use
//@ rs.ns.crate namespace std
//@ rs.scope.op namespace ::
//@ rs.ns.module namespace fmt
use std::fmt;

//@ rs.kw.mod keyword mod
//@ rs.mod.name namespace regs
mod regs {
    //@ rs.qual.pub qualifier pub
    //@ rs.const.decl number/T:variable CTRL
    //@ rs.type.prim prim usize
    pub const CTRL: usize = 0x4000_0000;
    //@ rs.kw.static keyword static
    //@ rs.qual.mut qualifier mut
    //@ rs.static.decl staticvar/T:variable TICKS
    pub static mut TICKS: u32 = 0;
}

//@ rs.doc.outer doc Debounced
/// Debounced input pin.
//@ rs.attr.outer directive derive
//@ rs.attr.derive.item directive Debug
#[derive(Debug, Clone)]
//@ rs.kw.struct keyword struct
//@ rs.struct.name composite Pin
//@ rs.lifetime.decl typeparam 'a
//@ rs.tparam.decl typeparam T
pub struct Pin<'a, T> {
    //@ rs.field.decl member id
    //@ rs.type.prim.u8 prim u8
    id: u8,
    //@ rs.ref.lifetime hazard &
    //@ rs.lifetime.use typeparam 'a
    //@ rs.type.str prim str
    name: &'a str,
    //@ rs.tparam.use typeparam T
    extra: T,
}

//@ rs.kw.enum keyword enum
//@ rs.enum.name composite Level
enum Level {
    //@ rs.enum.variant.decl number Low
    Low,
    High,
}

//@ rs.kw.trait keyword trait
//@ rs.trait.name composite Toggle
trait Toggle {
    //@ rs.kw.fn keyword fn
    //@ rs.method.decl method/T:function toggle
    //@ rs.self.ref hazard &
    //@ rs.qual.mut.self qualifier mut
    //@ rs.self.param param self
    fn toggle(&mut self);
}

//@ rs.kw.impl keyword impl
//@ rs.kw.for keyword for
//@ rs.selfty composite Pin
impl<'a, T> Toggle for Pin<'a, T> {
    fn toggle(&mut self) {
        //@ rs.self.use param self
        //@ rs.field.use member id
        //@ rs.op.bitxor hazard ^=
        self.id ^= 1;
    }
}

//@ rs.kw.impl.trait.fmt namespace fmt
impl<'a, T> fmt::Display for Pin<'a, T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        //@ rs.macro.call macro write
        //@ rs.format.spec hazard {}
        write!(f, "pin {}", self.id)
    }
}

//@ rs.macro.rules keyword macro_rules
//@ rs.macro.rules.name macro reg
macro_rules! reg {
    //@ rs.macro.metavar param $addr
    //@ rs.macro.fragment keyword expr
    ($addr:expr) => { $addr as *mut u32 };
}

//@ rs.qual.unsafe hazard unsafe
//@ rs.fn.decl function poke
//@ rs.param.decl param addr
unsafe fn poke(addr: usize, v: u32) {
    //@ rs.rawptr hazard *
    //@ rs.kw.as keyword as
    let p = addr as *mut u32;
    //@ rs.deref hazard *
    *p = v;
}

//@ rs.fn.main function main
//@ rs.kw.result prim/T:composite Result
fn main() -> Result<(), String> {
    //@ rs.kw.let keyword let
    //@ rs.var.local variable name
    //@ rs.string string pin
    let name = "pin";
    //@ rs.struct.lit composite Pin
    //@ rs.number.int number ~7
    //@ rs.number.suffix unit ~u8
    let mut pin = Pin { id: 7u8, name, extra: 'c' };
    //@ rs.method.call method/T:function toggle
    pin.toggle();
    //@ rs.borrow.mut hazard &
    let r = &mut pin;
    //@ rs.closure.param param x
    //@ rs.closure.pipe quietop |
    let twice = |x: u32| x * 2;
    //@ rs.closure.call variable/T:function twice
    let n = twice(3);
    //@ rs.kw.unsafe.block hazard unsafe
    //@ rs.fn.call function poke
    //@ rs.const.use number/T:variable CTRL
    unsafe { poke(regs::CTRL, n) };
    //@ rs.kw.match keyword match
    //@ rs.enum.variant.use number Low
    //@ rs.arrow.fat quietop =>
    let lvl = match n { 0 => Level::Low, _ => Level::High };
    //@ rs.label.decl function 'outer
    'outer: loop {
        //@ rs.kw.break keyword break
        //@ rs.label.use function 'outer
        break 'outer;
    }
    //@ rs.rawstring string ~raw#2
    let raw = r#"raw "quoted""#;
    //@ rs.bytestring string ~bytes#2
    let bytes = b"bytes";
    //@ rs.char string ~c'
    let c = 'c';
    //@ rs.option.some number Some
    //@ rs.kw.if keyword if
    if let Some(x) = Some(1) { let _ = x; }
    //@ rs.type.string prim/T:composite String
    //@ rs.assocfn.call libfn/T:function new
    let s: String = String::new();
    //@ rs.macro.call.println macro println
    //@ rs.format.named hazard {name}
    println!("{name} {:?} {}", r.id, s.len());
    //@ rs.op.try quietop ?
    let v: u8 = "5".parse::<u8>().map_err(|e| e.to_string())?;
    //@ rs.bool number true
    let ok = true;
    //@ rs.kw.return keyword return
    return Ok(());
}

// ---- coverage additions ----
//@ rs.doc.block doc Block
/** Block doc comment */
//@ rs.comment.block comment block
/* block comment */
//@ rs.kw.crate keyword crate
use crate::regs as r2;
//@ rs.kw.super keyword super
mod inner { use super::Level; }
//@ rs.kw.type keyword type
//@ rs.typealias.decl composite Word
type Word = u32;
//@ rs.number.bin number ~1010
//@ rs.number.oct number ~17
//@ rs.number.exp unit ~e
//@ rs.number.exp.sign unit ~-
//@ rs.number.sep number ~1_000
const NUMS: [f64; 4] = [0b1010 as f64, 0o17 as f64, 1.5e-3, 1_000.0];
fn more(v: &[u8], s: &str) -> bool {
    //@ rs.escape escape \n
    //@ rs.escape.unicode escape ~\u{1F600}
    //@ rs.escape.byte escape ~\x41
    let e = "\n\u{1F600}\x41";
    //@ rs.op.range quietop ..
    //@ rs.op.cmp quietop ==
    let t = &v[1..] == &v[..1];
    //@ rs.op.subpattern quietop @
    //@ rs.op.range.inclusive quietop ..=
    let k = match v.len() { n @ 1..=3 => n, _ => 0 };
    //@ rs.brackets punct [
    let a = [1, 2];
    //@ rs.borrow.ref hazard &
    let b = &a;
    //@ rs.kw.ref keyword ref
    let ref c = a;
    //@ rs.kw.dyn keyword dyn
    let d: Box<dyn Fn()> = Box::new(|| {});
    //@ rs.kw.async keyword async
    //@ rs.kw.move keyword move
    let _ = async move { 0 };
    //@ rs.macro.metavar.ty keyword ty
    macro_rules! m { ($t:ty) => { let _: $t; }; }
    //@ rs.method.lib libfn/T:function len
    s.len() > 0 && t
}
//@ rs.generic.where keyword where
fn gen<T>(x: T) -> T where T: Clone { x.clone() }

// ---- pass 1b coverage additions ----
//@ rs.borrow.mut2 hazard &
fn bm(v: &mut i32) -> i32 { let r = &mut *v; *r }
