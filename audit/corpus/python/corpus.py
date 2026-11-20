#@ py.comment comment comment
# comment
#@ py.kw.import keyword import
#@ py.module namespace os
import os
#@ py.kw.from keyword from
#@ py.module.dotted namespace dataclasses
#@ py.import.name libfn/T:directive dataclass
from dataclasses import dataclass

#@ py.const.upper number MAX_PINS
MAX_PINS = 0x1F


#@ py.decorator.at directive @
#@ py.decorator.name directive dataclass
@dataclass
#@ py.kw.class keyword class
#@ py.class.name composite Pin
#@ py.class.base prim object
class Pin(object):
    #@ py.docstring doc Docstring
    """Docstring for Pin."""

    #@ py.field.decl member/T:variable number
    #@ py.typehint.builtin prim int
    number: int = 0

    #@ py.kw.def keyword def
    #@ py.dunder.decl method __post_init__
    #@ py.self.param param self
    def __post_init__(self) -> None:
        #@ py.self.use param self
        #@ py.attr.use member number
        self.number &= MAX_PINS

    #@ py.decorator.builtin directive classmethod
    @classmethod
    #@ py.method.decl method/T:function make
    #@ py.cls.param param cls
    #@ py.param.decl param n
    def make(cls, n: int) -> "Pin":
        #@ py.cls.use param cls
        return cls(n)


#@ py.kw.async keyword async
#@ py.fn.decl function blink
#@ py.param.default param times
async def blink(pin: Pin, times: int = 3, *args, **kwargs) -> str:
    #@ py.kw.await keyword await
    await sleep(0.1)
    #@ py.fstring string pin
    #@ py.fstring.brace hazard {
    #@ py.fstring.spec hazard ~02X
    label = f"pin {pin.number:02X}"
    #@ py.percent.format hazard %d
    old = "pin %d" % pin.number
    #@ py.escape escape \n
    #@ py.raw.string escape ~\d
    raw = r"\d+\n" + "\n"
    #@ py.bytes string ~bytes
    b = b"bytes"
    #@ py.fn.builtin libfn print
    print(label, old, raw, b, len(args))
    #@ py.op.shift hazard <<
    #@ py.op.bitor hazard |
    mask = 1 << pin.number | 0x80
    #@ py.op.walrus quietop :=
    if (n := mask) > 0:
        #@ py.kw.return keyword return
        return label
    #@ py.const.none number None
    return None


#@ py.fn.sleep function sleep
async def sleep(s): ...


def classify(v):
    #@ py.kw.match keyword match
    match v:
        #@ py.kw.case keyword case
        case 0:
            #@ py.bool number True
            return True
        case _:
            #@ py.lambda keyword lambda
            #@ py.lambda.param param x
            f = lambda x: x * 2
            #@ py.fn.call variable/T:function f
            #@ py.method.call method/T:function make
            return f(Pin.make(v).number)


#@ py.kw.with keyword with
#@ py.fn.builtin.open libfn open
with open(os.devnull) as fh:
    #@ py.method.lib method write
    fh.write("x")


# ---- coverage additions ----
#@ py.typecomment comment type
x = []  # type: list[int]
#@ py.number.bin number ~0b1010
#@ py.number.oct number ~0o17
#@ py.number.imag unit ~j
nums = [0b1010, 0o17, 1.5, 2j]
#@ py.dict.brace punct {
#@ py.dict.colon punct :
d = {"k": 1}
#@ py.slice.colon punct :
s = nums[1:2]
#@ py.op.not keyword not
#@ py.op.in keyword in
#@ py.op.is keyword is
ok = 1 not in nums and d is not None
#@ py.unpack.star quietop *
#@ py.kwarg param sep
print(*nums, sep=", ")
#@ py.kw.try keyword try
try:
    #@ py.exception.builtin prim ValueError
    #@ py.kw.raise keyword raise
    raise ValueError("bad")
#@ py.kw.except keyword except
except ValueError as err:
    pass
#@ py.kw.global keyword global
global x
#@ py.string.multi string multi
m = """multi
line"""
#@ py.rawbytes string ~raw
rb = rb"raw\d"
import re
#@ py.regex.group hazard ~(?P<
p = re.compile(r"(?P<name>\w+)(?=x)")
#@ py.metaclass.builtin prim type
class Meta(type):
    #@ py.magic.call method __init__
    def __init__(cls, *a): super().__init__(*a)
#@ py.inherit.comma punct ,
class Both(Pin, Meta): pass
def gen():
    #@ py.kw.yield keyword yield
    yield 1
def outer():
    v = 0
    def inner():
        #@ py.kw.nonlocal keyword nonlocal
        nonlocal v
#@ py.line.continuation escape \
total = 1 + \
    2
#@ py.number.plain number 123
n2 = 123
def doc_raw():
    #@ py.docstring.raw doc Raw
    r"""Raw docstring \d."""
def doc_single():
    '''Single-quoted docstring.'''
#@ py.bytes.multi string multi
bm = b"""multi
bytes"""
rm = r"""raw
multi"""
rbm = rb'''raw
bytes'''
#@ py.format.brace hazard {}
fmt = "{} {}".format(1, 2)
#@ py.metaclass.kw param metaclass
class WithMeta(object, metaclass=Meta): pass
#@ py.posonly.sep quietop /
def pos(a, /, b): pass
#@ py.matmul quietop @
mm = nums @ nums
#@ py.typeignore comment ignore
z = 1  # type: ignore
#@ py.codetag comment TODO
# TODO: owner styles this with a separate extension


# ---- pass 1b coverage additions ----
#@ py.raw.single string ~path
rs1 = r'path'
#@ py.raw.bytes string ~bin
rb1 = rb'bin'
#@ py.raw.multi string ~multi
rm1 = r"""multi"""
def doc_single():
    #@ py.docstring.single doc Single
    '''Single-quoted docstring.'''
#@ py.class.kwarg param flag
class Flagged(object, flag=1):
    pass
