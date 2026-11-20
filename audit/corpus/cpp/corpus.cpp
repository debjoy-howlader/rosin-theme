//@ cpp.pp.directive directive #include
#include <stdint.h>
#include <sys/types.h>
#include <pthread.h>

//@ cpp.ns.kw keyword namespace
//@ cpp.ns.name namespace hal
namespace hal {

//@ cpp.kw.template keyword template
//@ cpp.kw.typename keyword typename
//@ cpp.tparam.decl typeparam T
template <typename T>
//@ cpp.kw.concept keyword concept
//@ cpp.concept.name composite Small
//@ cpp.kw.sizeof keyword sizeof
concept Small = sizeof(T) <= 4;

//@ cpp.class.kw keyword class
//@ cpp.class.name composite Led
//@ cpp.qual.final qualifier final
class Led final {
//@ cpp.access qualifier public
public:
    //@ cpp.ctor.decl function Led
    //@ cpp.ref.declarator hazard &
    //@ cpp.qual.explicit qualifier explicit
    explicit Led(uint8_t pin, const char &tag) : pin_(pin) {}
    //@ cpp.dtor.decl function ~Led
    ~Led() = default;
    //@ cpp.qual.virtual qualifier virtual
    //@ cpp.method.decl method/T:function on
    //@ cpp.type.void prim void
    virtual void on() {}
    //@ cpp.qual.constexpr qualifier constexpr
    //@ cpp.attr.std directive nodiscard
    //@ cpp.type.auto keyword auto
    [[nodiscard]] constexpr auto pin() const { return pin_; }
    //@ cpp.op.overload.decl function operator==
    bool operator==(const Led &o) const = default;
    //@ cpp.rvalue.declarator hazard &&
    void take(Led &&other);
//@ cpp.access.private qualifier private
private:
    //@ cpp.member.decl member pin_
    uint8_t pin_;
    //@ cpp.member.static.decl staticvar/T:member count
    static inline int count = 0;
};

//@ cpp.kw.struct keyword struct
//@ cpp.struct.name composite Regs
struct Regs { volatile uint32_t ctrl; };

//@ cpp.kw.enumclass keyword enum
//@ cpp.enum.name composite Mode
enum class Mode : uint8_t { Off, On };

//@ cpp.udl.op.decl function operator""
//@ cpp.udl.suffix.decl function _ms
constexpr unsigned long long operator""_ms(unsigned long long v) { return v; }

}  // namespace hal

//@ cpp.kw.using keyword using
//@ cpp.alias.name composite Pin
using Pin = uint8_t;

int main() {
    using hal::operator""_ms;
    //@ cpp.ns.use namespace hal
    //@ cpp.scope.op namespace ::
    //@ cpp.class.use composite Led
    hal::Led led(2, 'x');
    //@ cpp.method.call method/T:function on
    led.on();
    //@ cpp.kw.auto keyword auto
    //@ cpp.lambda.capture.ref hazard &
    //@ cpp.lambda.param param x
    auto twice = [&](int x) { return x * 2; };
    //@ cpp.lambda.call variable/T:function twice
    twice(3);
    //@ cpp.kw.nullptr number nullptr
    hal::Led *p = nullptr;
    //@ cpp.kw.new keyword new
    p = new hal::Led(3, 'y');
    //@ cpp.kw.delete keyword delete
    delete p;
    //@ cpp.cast.static keyword static_cast
    int n = static_cast<int>(led.pin());
    //@ cpp.enum.member.use number On
    //@ cpp.enum.type.use composite Mode#2
    hal::Mode m = hal::Mode::On;
    //@ cpp.udl.literal number ~250
    //@ cpp.udl.suffix unit ~_ms
    auto t = 250_ms;
    //@ cpp.rawstring string ~raw
    const char *s = R"(raw\n text)";
    //@ cpp.kw.if.constexpr keyword if
    //@ cpp.kw.constexpr.if qualifier constexpr
    if constexpr (sizeof(int) == 4) { n++; }
    //@ cpp.kw.return keyword return
    return n + (m == hal::Mode::Off) + (int)t + (s != nullptr);
}

struct Base { virtual int get() { return 1; } };
//@ cpp.class.base.use composite Base
//@ cpp.qual.override qualifier override
//@ cpp.this.use param this
struct Derived : Base { int get() override { return this->Base::get() + 1; } };

// ---- coverage additions ----
//@ cpp.doc.line doc Line
/// Line doc
//@ cpp.comment.block comment block
/* block */
//@ cpp.pp.define directive define
//@ cpp.macro.def macro SQ
//@ cpp.macro.param param x
#define SQ(x) ((x) * (x))
//@ cpp.pp.undef directive undef
#undef SQ
//@ cpp.pp.pragma directive pragma
#pragma once
//@ cpp.ns.alias.kw keyword namespace
//@ cpp.ns.alias namespace hl
namespace hl = hal;
//@ cpp.using.ns keyword using
using namespace hal;
//@ cpp.kw.typedef keyword typedef
typedef unsigned int u32;
//@ cpp.union.kw keyword union
//@ cpp.union.name composite U
union U { int i; float f; };
//@ cpp.number.bin number ~1010
//@ cpp.number.oct number ~017
//@ cpp.number.suffix.ull unit ~ull
//@ cpp.number.sep number ~1'000
unsigned long long nums2[] = {0b1010ull, 017ull, 1'000ull};
double hexf = 0x1p3;
//@ cpp.number.suffix.float unit ~f#3
float fl = 1.5f;
//@ cpp.escape escape \n
//@ cpp.char.u8 string ~u8"
const char8_t *u8s = u8"text\n";
//@ cpp.kw.decltype keyword decltype
//@ cpp.kw.noexcept qualifier noexcept
decltype(fl) g() noexcept { return 0; }
//@ cpp.kw.static_assert keyword static_assert
static_assert(sizeof(int) == 4);
//@ cpp.kw.requires keyword requires
template <typename T> requires Small<T> void h(T) {}
//@ cpp.kw.alignas keyword alignas
//@ cpp.kw.alignof keyword alignof
struct alignas(8) Al { int a = alignof(int); };
//@ cpp.kw.sizeof.pack keyword sizeof...
template <typename... Ts> int cnt() { return sizeof...(Ts); }
struct Ctl {
    //@ cpp.ctor.default.delete keyword delete
    Ctl(const Ctl &) = delete;
    //@ cpp.qual.virtual.dtor qualifier virtual
    virtual ~Ctl() {}
    //@ cpp.op.conversion function operator
    operator bool() const { return true; }
    //@ cpp.qual.mutable qualifier mutable
    mutable int m;
};
void more(int *p) {
    //@ cpp.op.bitand hazard &
    //@ cpp.op.bitor hazard |
    //@ cpp.op.xor hazard ^
    //@ cpp.op.not.bit hazard ~~
    int x = (1 & 2) | (3 ^ ~4);
    //@ cpp.op.shift hazard <<
    //@ cpp.op.compound.bit hazard |=
    x = x << 1; x |= 2;
    //@ cpp.op.deref hazard *
    //@ cpp.op.addressof hazard &
    x = *p + *&x;
    //@ cpp.op.ternary keyword ?
    //@ cpp.op.logical keyword &&
    x = (x && p) ? 1 : 0;
    //@ cpp.op.decr quietop --
    x--;
    //@ cpp.kw.new.array keyword new
    //@ cpp.kw.delete.array keyword delete
    int *a = new int[4]; delete[] a;
    //@ cpp.kw.goto keyword goto
    //@ cpp.label.use function/T:variable out
    goto out;
    //@ cpp.label.def function/T:variable out
out:
    //@ cpp.lambda.capture.var param x
    //@ cpp.lambda.ret prim int
    auto lam = [x](int y) -> int { return x + y; };
    int vals[] = {1, 2};
    //@ cpp.kw.for.range keyword for
    //@ cpp.range.colon punct :
    for (int v : vals) { x += v; }
    //@ cpp.kw.switch keyword switch
    //@ cpp.kw.case keyword case
    switch (x) { case 1: break; default: break; }
    //@ cpp.kw.try keyword try
    //@ cpp.kw.catch keyword catch
    //@ cpp.kw.throw keyword throw
    try { throw 1; } catch (...) {}
    //@ cpp.cast.reinterpret keyword reinterpret_cast
    auto q = reinterpret_cast<long>(p);
    (void)q;
}
//@ cpp.kw.extern.c qualifier extern
extern "C" void c_fn();
//@ cpp.kw.consteval qualifier consteval
consteval int ce() { return 1; }

// ---- coverage round 2 ----
//@ cpp.pp.include.macro macro HDR
#define HDR <stdint.h>
#include HDR
//@ cpp.pp.line directive line
#line 500
//@ cpp.pp.defined directive defined
#if defined(HDR)
#endif
//@ cpp.predef.macro macro __FILE__
const char *file = __FILE__;
//@ cpp.kw.class.fwd keyword class
class Fwd;
//@ cpp.struct.fwd keyword struct
struct SFwd; union UFwd; enum class EFwd : int;
namespace outer { namespace inner2 { struct V { V(); ~V(); V operator+(const V &) const; static int f(); int prop; }; } }
//@ cpp.scope.ctor.def function V#2
outer::inner2::V::V() {}
//@ cpp.scope.dtor.def function ~V
outer::inner2::V::~V() {}
//@ cpp.scope.opover.def function operator+
outer::inner2::V outer::inner2::V::operator+(const V &) const { return *this; }
//@ cpp.op.new.overload function operator
void *operator new(decltype(sizeof 0) n);
char operator""_c(char c) { return c; }
const char *operator""_s(const char *s, decltype(sizeof 0)) { return s; }
template <typename T> struct Box { T v; T get() const { return v; } };
void more2(int (*fp)(int), outer::inner2::V &obj, int camelCase = 3) {
    //@ cpp.scope.static.call function f
    int r = outer::inner2::V::f();
    //@ cpp.template.call composite Box
    //@ cpp.template.arg prim int
    Box<int> b{1};
    //@ cpp.obj.prop member prop
    r += obj.prop;
    //@ cpp.upper.def macro FOO
    #define FOO() 1
    r += FOO();
    //@ cpp.for.var variable i
    for (int i = 0; i < 2; ++i) {}
    //@ cpp.fnptr.param.call param/T:function fp
    r += fp(2);
    //@ cpp.udl.char unit _c
    //@ cpp.udl.string unit _s
    auto c1 = 'a'_c; auto s1 = "s"_s;
    //@ cpp.posix.type prim pid_t
    pid_t pid; pthread_t th;
    //@ cpp.decltype.auto keyword decltype
    decltype(auto) da = r;
    //@ cpp.noexcept.op keyword noexcept
    bool ne = noexcept(r++);
    //@ cpp.cast.const keyword const_cast
    const int *ci = const_cast<const int *>(&r); (void)ci;
    //@ cpp.delete.array.bracket keyword delete
    int *arr = new int[2]; delete [] arr;
    //@ cpp.lambda.capture.init param n
    auto l2 = [n = 2]() mutable { return n; };
    //@ cpp.lambda.trailing.ret prim long
    auto l3 = []() -> long { return 1; };
}
//@ cpp.extern.block qualifier extern
extern "C" { void c2(); }
//@ cpp.kw.virtual.base qualifier virtual
struct D2 : virtual Base { };
//@ cpp.kw.friend qualifier friend
class Fr { friend class Led; };
//@ cpp.kw.inline.ns qualifier inline
inline namespace v1 {}
//@ cpp.kw.thread_local qualifier thread_local
thread_local int tl;

// ---- pass 1b coverage additions ----
//@ cpp.include.local string corpus_local
#include "corpus_local.h"
//===== banner section =====
//@ cpp.comment.banner comment banner
// banner comment
//@ cpp.doc.bold doc bold
//@ cpp.doc.italic doc italic
/** @brief Doc with \b bold and \e italic words. */
int doxy_target();
//@ cpp.pragma.mark directive mark
#pragma mark Section
//@ cpp.ns.alias.kw keyword namespace
//@ cpp.ns.alias.name namespace hw
//@ cpp.ns.alias.target namespace hal
namespace hw = hal;
//@ cpp.ns.nested.outer namespace outer
//@ cpp.ns.nested.inner namespace inner
namespace outer::inner { int deep; }
//@ cpp.ns.alias.qual namespace outer
namespace oi = outer::inner;
//@ cpp.using.ns.qual namespace outer
using namespace outer::inner;
//@ cpp.type.alias.kw keyword using
//@ cpp.type.alias.name composite Byte
using Byte = uint8_t;
//@ cpp.fwd.class.kw keyword class
//@ cpp.fwd.class.name composite Fwd
class Fwd;
//@ cpp.fwd.enum.kw keyword enum
//@ cpp.fwd.enum.name composite E3
enum class E3 : int;
//@ cpp.fwd.union.kw keyword union
union U2;
//@ cpp.posix.user.type composite led2_t
typedef int led2_t; led2_t lv = 0;
struct Led2 {
    //@ cpp.inline.member qualifier inline
    inline int get() const;
    Led2();
    ~Led2();
    //@ cpp.dtor.delete.kw keyword delete
    Led2(const Led2 &) = delete;
    bool operator==(const Led2 &) const;
    //@ cpp.member.init.decl member v
    int v = 0;
};
//@ cpp.ool.ctor.owner composite Led2
//@ cpp.ool.ctor.name function Led2#2
//@ cpp.ctor.init.member member v
Led2::Led2() : v(1) {}
//@ cpp.ool.dtor.owner composite Led2
//@ cpp.ool.dtor.name function ~Led2
Led2::~Led2() {}
//@ cpp.ool.fn.owner composite Led2
//@ cpp.ool.fn.name method/T:function get
int Led2::get() const { return v; }
//@ cpp.ool.op.owner composite Led2
bool Led2::operator==(const Led2 &) const { return true; }
template <typename T> struct Box2 { static T make() { return T{}; } using type = T; };
//@ cpp.tmpl.scope.call composite Box2
int bx = Box2<int>::make();
//@ cpp.typename.dep keyword typename
template <typename T> typename Box2<T>::type unwrap();
//@ cpp.explicit.inst.kw keyword template
template struct Box2<long>;
//@ cpp.param.class.kw keyword class
//@ cpp.param.class.name composite Fwd
//@ cpp.param.struct.kw keyword struct
//@ cpp.param.enum.kw keyword enum
void elab(class Fwd *a, struct Led2 *b, enum E3 c);
//@ cpp.vararg punct ...
void vfn(int n, ...);
//@ cpp.extern.decl qualifier extern
extern int ext_v;
//@ cpp.alignas.op keyword alignas
alignas(16) char abuf[16];
//@ cpp.requires.expr keyword requires
template <typename T> concept HasGet = requires(T t) { t.get(); };
//@ cpp.static_assert.msg string ~size#2
static_assert(sizeof(int) == 4, "size");
//@ cpp.macro.arg.use param x#2
#define SQ(x) ((x) * (x))
//@ cpp.macro.cont escape \#1
#define TWO(a, b) \
    ((a) + (b))
//@ cpp.raw.regex.quant hazard +
const char *rx = R"regex(a+)regex";
//@ cpp.trailing.arrow punct ->
auto tr() -> int;
//@ cpp.fnptr.var globalvar/T:variable fp2
int (*fp2)(int);
//@ cpp.hexfloat.exp unit ~p
double hf = 0x1p+4 + 1.5e-3;
struct P2 { int a, b; };
P2 std_pair();
int user1b() {
    int arr3[3] = {1, 2, 3};
    //@ cpp.binding.name variable bx1
    auto [bx1, bx2] = std_pair();
    //@ cpp.range.for.var variable el
    for (int el : arr3) { (void)el; }
    //@ cpp.label.def2 function/T:variable retry
retry:
    //@ cpp.goto.kw keyword goto
    if (bx1) goto retry;
    //@ cpp.asm.kw keyword asm
    asm("nop");
    return SQ(2) + TWO(1, 2) + bx2;
}
