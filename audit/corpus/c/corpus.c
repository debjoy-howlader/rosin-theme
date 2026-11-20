//@ c.comment.line comment //
// line comment: a plain remark
//@ c.comment.block comment /*
/* block comment */
//@ c.doc.block doc /**
//@ c.doc.tag doctag @brief
//@ c.doc.body doc Doc
/** @brief Doc comment with a Doxygen tag. */
//@ c.pp.directive directive #include
//@ c.pp.header.system string stdint.h
#include <stdint.h>
//@ c.pp.header.local string board.h
#include "board.h"
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <pthread.h>

//@ c.pp.define directive define
//@ c.macro.name.def macro LED_PIN
//@ c.number.int number 2
#define LED_PIN 2
//@ c.macro.fn.def macro BIT
//@ c.macro.param.def param n
//@ c.number.suffix unit ~UL
//@ c.op.shift hazard <<
//@ c.macro.param.use param n#2
#define BIT(n) (1UL << (n))
//@ c.pp.stringize directive #
#define STR(x) #x
//@ c.pp.paste directive ##
#define CAT(a, b) a##b
//@ c.pp.if directive #if
//@ c.pp.defined directive defined
//@ c.macro.use.cond macro DEBUG
//@ c.op.logical keyword &&
#if defined(DEBUG) && DEBUG > 1
//@ c.pp.error.msg string debug
#error "debug builds need a log level"
#endif
//@ c.pp.pragma directive pragma
#pragma pack(1)
#if 0
//@ c.pp.inactive comment dead_code
int dead_code = 1;
#endif

//@ c.kw.typedef keyword typedef
//@ c.type.prim prim unsigned
//@ c.type.typedef.def composite u8_custom
typedef unsigned char u8_custom;

//@ c.type.struct.kw keyword struct
//@ c.type.struct.tag composite led
typedef struct led {
    //@ c.type.stdint prim uint8_t
    //@ c.member.decl member pin
    uint8_t pin;
    //@ c.qual.volatile qualifier volatile
    //@ c.ptr.declarator hazard *
    //@ c.member.ptr.decl member reg
    volatile uint32_t *reg;
    //@ c.member.bitfield member flag
    //@ c.number.bitwidth number 1
    unsigned flag : 1;
//@ c.type.typedef.def2 composite led_t
} led_t;

//@ c.type.enum.kw keyword enum
//@ c.type.enum.tag composite mode
//@ c.enum.member.decl number MODE_OFF
enum mode { MODE_OFF, MODE_ON = 1 };

//@ c.type.union.kw keyword union
//@ c.array.decl.size punct [
union reg_u { uint32_t word; uint8_t bytes[4]; };

//@ c.qual.static qualifier static
//@ c.var.static.file staticvar/T:variable s_count
static int s_count = 0;
//@ c.var.global globalvar/T:variable g_ticks
int g_ticks;
//@ c.qual.const qualifier const
//@ c.var.const.global number/T:variable k_max
const int k_max = 10;
//@ c.qual.extern qualifier extern
extern int g_ext;

//@ c.qual.inline qualifier inline
//@ c.fn.def function add
//@ c.param.decl param a
//@ c.kw.return keyword return
//@ c.param.use param/T:variable a#2
//@ c.op.arith quietop +
static inline int add(int a, int b) { return a + b; }

//@ c.type.void prim void
//@ c.fnptr.name globalvar/T:variable callback
//@ c.macro.use.stdlib macro NULL
void (*callback)(int) = NULL;

int main(void) {
    //@ c.type.char prim char
    //@ c.var.local variable buf
    //@ c.string string hi
    //@ c.escape escape \n
    char buf[16] = "hi\n";
    //@ c.char.literal string A
    char c = 'A';
    //@ c.number.float number 1.5
    //@ c.number.exponent unit ~e
    //@ c.number.suffix.f unit ~f#3
    float f = 1.5e3f;
    //@ c.number.hexfloat number 1.8
    double h = 0x1.8p1;
    //@ c.number.hex.prefix unit ~0x
    unsigned long ul = 0x2AUL;
    //@ c.type.bool prim bool
    //@ c.const.true number true
    bool ok = true;
    //@ c.member.designated member pin
    //@ c.op.addressof hazard &
    //@ c.var.global.use globalvar/T:variable REG_CTRL
    led_t led = { .pin = LED_PIN, .reg = &REG_CTRL };
    led_t *p = &led;
    //@ c.op.arrow hazard ->
    //@ c.member.use member pin
    p->pin = 3;
    //@ c.op.dot quietop .
    //@ c.member.use.dot member flag
    led.flag = 1;
    //@ c.op.deref hazard *
    //@ c.op.bitassign hazard |=
    //@ c.macro.fn.use macro BIT
    *p->reg |= BIT(3);
    //@ c.cast.type prim int#2
    int x = (int)f;
    //@ c.type.size_t prim size_t
    //@ c.kw.sizeof keyword sizeof
    size_t n = sizeof(buf);
    //@ c.op.bitnot hazard ~~
    //@ c.op.bitand hazard &
    //@ c.op.xor hazard ^
    x = ~x & 0xFF ^ 1;
    //@ c.op.shift.assign hazard <<=
    x <<= 2;
    //@ c.kw.if keyword if
    //@ c.op.compare quietop >
    //@ c.op.not keyword !
    //@ c.kw.else keyword else
    if (x > 0 && !ok) { x = 0; } else { x = 1; }
    //@ c.kw.for keyword for
    //@ c.op.incr quietop ++
    //@ c.kw.continue keyword continue
    for (int i = 0; i < 4; i++) { continue; }
    //@ c.kw.switch keyword switch
    //@ c.kw.case keyword case
    //@ c.enum.member.use number MODE_ON
    //@ c.kw.break keyword break
    switch (x) { case MODE_ON: break; default: break; }
    //@ c.kw.goto keyword goto
    //@ c.label.use function/T:variable done
    goto done;
    //@ c.op.ternary keyword ?
    int y = x ? 1 : 2;
    //@ c.fn.lib libfn printf
    //@ c.format.spec hazard %d
    printf("%d items %s\n", x, buf);
    //@ c.fn.lib2 libfn memcpy
    memcpy(buf, "ab", 2);
    //@ c.fn.call function add
    add(1, 2);
    //@ c.fnptr.call globalvar/T:function callback
    callback(y);
    //@ c.var.static.use staticvar/T:variable s_count
    s_count++;
//@ c.label.def function/T:variable done
done:
    //@ c.kw.asm keyword __asm__
    __asm__ volatile ("nop");
    //@ c.number.zero number 0
    return 0;
}

//@ c.attr.gnu directive __attribute__
struct __attribute__((packed)) frame { uint8_t a; };
//@ c.kw.static_assert keyword _Static_assert
_Static_assert(sizeof(struct frame) == 1, "packed");

/* ---- coverage additions (A1 coverage list) ---- */
//@ c.pp.undef directive undef
#undef LED_PIN
//@ c.pp.line directive line
#line 300 "corpus.c"
//@ c.pp.number number 300
#if 300 > 1
//@ c.pp.elif directive elif
#elif 0
int elif_branch;
//@ c.pp.else directive else
#else
//@ c.pp.inactive.else comment else_branch
int else_branch;
#endif
//@ c.macro.variadic.ellipsis punct ...
//@ c.macro.va_args param __VA_ARGS__
#define LOG(fmt, ...) printf(fmt, __VA_ARGS__)
//@ c.pp.continuation escape \
#define LONG_MACRO(x) \
    ((x) + 1)
//@ c.doc.line doc Line
/// Line doc comment
//@ c.doc.markup.bold doc bold
/** \b bold and \e italic words */
//@ c.var.fwd.decl.param param n
int proto(int n, ...);
//@ c.number.binary number ~1010
//@ c.number.binary.prefix unit ~0b
//@ c.number.octal number 017
//@ c.number.exp.sign unit ~p+
static int nums[] = { 0b1010, 017, (int)0x1p+3 };
//@ c.type.pthread prim pthread_t
pthread_t th;
void ops(void) {
    int i = 0;
    //@ c.op.decr quietop --
    //@ c.op.compound.arith quietop +=
    i--; i += 2;
    //@ c.op.compound.bitand hazard &=
    //@ c.op.compound.shr hazard >>=
    i &= 3; i >>= 1;
    //@ c.op.mul quietop *
    i = i * 2;
    //@ c.op.bitor hazard |
    i = i | 4;
    //@ c.escape.unknown error \q
    const char *bad = "\q";
    //@ c.escape.hex escape \x41
    //@ c.escape.octal escape \101
    const char *esc = "\x41\101";
    //@ c.asm.operand.constraint string r
    //@ c.asm.colon punct :
    __asm__ volatile ("mov %0, %0" : "+r"(i));
    //@ c.kw.static_assert.macro keyword static_assert
    static_assert(1, "c11 macro form");
    //@ c.kw.while keyword while
    //@ c.kw.do keyword do
    do { i++; } while (i < 3);
    //@ c.kw.default keyword default
    switch (i) { default: break; }
    //@ c.kw.register qualifier register
    register int r = 0;
    int r2 = r;
    //@ c.kw.restrict qualifier restrict
    int *restrict rp = &r2;
    //@ c.kw.noreturn qualifier _Noreturn
    extern _Noreturn void halt(void);
    //@ c.kw.typeof keyword typeof
    typeof(i) t = 0;
}
//@ c.comment.banner comment ====
// ==== Section ====
//@ c.pragma.mark directive mark
#pragma mark - Helpers
//@ c.pp.number.cond number 2
#if VERSION > 2
#endif
struct dev { void (*cb)(int); };
void more_c(struct dev *d, int arr[static 4]) {
    //@ c.member.fncall member/T:function cb
    d->cb(1);
    //@ c.number.exp.minus unit ~e-
    //@ c.number.exp.plus unit ~e+
    double e1 = 1e-3, e2 = 2e+3, e3 = 0x1p-2;
    //@ c.type.stdint.2 prim int8_t
    //@ c.type.uintptr prim uintptr_t
    int8_t a8; uintptr_t up; intmax_t im;
    //@ c.type.sys prim ssize_t
    ssize_t ss; pthread_mutex_t mu;
#if 0
    //@ c.pp.inactive.inblock comment inblock
    int inblock;
#else
    int live;
#endif
    _Static_assert(1, "in block");
    //@ c.asm.goto.label function fail
    asm goto ("" :::: fail);
fail:
    return;
}

/* ---- pass 1b coverage additions ---- */
/* ===== Banner block ===== */
//@ c.comment.banner comment Banner
// ===== Banner line =====
//@ c.encoding.prefix string u8
const char *enc = u8"x";
//@ c.type.pthread prim pthread_t
//@ c.type.systypes prim ssize_t
pthread_t c_th; ssize_t c_n;
void c1b(int v) {
    //@ c.case.range punct ...
    switch (v) { case 1 ... 3: break; default: break; }
#if 0
    int off;
    //@ c.pp.elif.inblock directive elif
#elif 2 > 1
    int on1;
#else
    int off2;
#endif
}
