"""Render a colour cheatsheet PNG for every Rosin theme.

Usage:  python tools/cheatsheet.py   (writes images/cheatsheets/*.png and images/preview.png)
Needs Pillow, plus DejaVu Sans Mono and Inter (falls back to DejaVu Sans).
"""
import os, sys, runpy
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'images', 'cheatsheets')
os.makedirs(OUT, exist_ok=True)

sys.argv = ['gen.py']
G = runpy.run_path(os.path.join(HERE, 'gen.py'))
REPORT, NEW, mix = G['REPORT'], G['NEW'], G['mix']

S = 2  # render scale
def F(path, size):
    try:
        return ImageFont.truetype(path, size * S)
    except OSError:
        return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', size * S)
DJ = '/usr/share/fonts/truetype/dejavu/'
INTER = '/usr/share/fonts/opentype/inter/'
MONO = {(False, False): F(DJ + 'DejaVuSansMono.ttf', 15), (True, False): F(DJ + 'DejaVuSansMono-Bold.ttf', 15),
        (False, True): F(DJ + 'DejaVuSansMono-Oblique.ttf', 15), (True, True): F(DJ + 'DejaVuSansMono-BoldOblique.ttf', 15)}
MONO_S = F(DJ + 'DejaVuSansMono.ttf', 12)
CODE = {k: ImageFont.truetype(v.path, 16 * S) for k, v in MONO.items()}
H1 = F(INTER + 'Inter-SemiBold.otf', 34)
H2 = F(INTER + 'Inter-SemiBold.otf', 13)
LBL = F(INTER + 'Inter-Medium.otf', 15)
SUB = F(INTER + 'Inter-Regular.otf', 15)

def sheet(name, r):
    ui, syn = r['ui'], r['syn']
    style = NEW.get(name, {}).get('style', {})
    kw_bold = 'bold' in style.get('Keywords & control flow (amber)', '')
    ct_bold = 'bold' in style.get('Compile-time keywords (typedef sizeof alignof)', '')

    # role: (label, example, colour, bold, italic, underline)
    def row(label, ex, col, b=False, i=False, u=False): return (label, ex, col, b, i, u)
    left = [
        ('STRUCTURE', [
            row('Keyword / control flow', 'if  for  return  match', syn['keyword'], kw_bold),
            row('Compile-time keyword', 'sizeof  typedef', syn['keyword'], ct_bold, True),
            row('Qualifier', 'const  static  extern', syn['qualifier'], False, True),
            row('Function', 'led_set()  uart_init()', syn['function']),
            row('Method', '.write()  .push()', syn['method']),
            row('Library / builtin function', 'printf  memcpy', syn['libfn']),
            row('Macro', 'LED_PIN  MAX()  println!', syn['macro'], True),
            row('Preprocessor / attribute', '#include  #[derive]  @dec', syn['directive']),
            row('Namespace / module', 'std  core::ptr', syn['scope']),
        ]),
        ('TYPES', [
            row('Primitive / library type', 'int  uint8_t  u32  bool', syn['prim']),
            row('User type / type keyword', 'struct  led_t  trait', syn['composite']),
        ]),
        ('DATA', [
            row('Variable', 'count  buf', syn['variable']),
            row('Parameter / self', 'len  self', syn['param'], False, True),
            row('Member / key / CLI flag', '.pin  name:  --baud', syn['member']),
            row('Global / config variable', 'g_ticks  $(CC)  ${VAR}', syn['globalvar']),
            row('Static variable', 's_state', syn['staticvar']),
        ]),
    ]
    right = [
        ('LITERALS', [
            row('Number / constant / enum', '42  0xFF  true  IDLE', syn['number']),
            row('String', '"hello"  <stdint.h>', syn['string']),
            row('Escape / entity', '\\n  \\t  &amp;', syn['escape']),
            row('Format specifier', '%d  %02X  {:#04x}', syn['hazard'], True),
        ]),
        ('ATTENTION', [
            row('Hazard: pointer / bits / unsafe', '*  &  ->  <<  |=  r0', syn['hazard'], True),
            row('Error / invalid', 'invalid_token', syn['error'], False, False, True),
        ]),
        ('QUIET', [
            row('Operator', '=  +  ==  <', syn['quietop']),
            row('Punctuation', ';  ,  {  }', syn['punct']),
            row('Comment', '// note to self', syn['comment'], False, True),
            row('Doc comment', '/// returns length', syn['doc'], False, True),
        ]),
        ('LOGS & DIFFS', [
            row('Log error / warning', 'ERROR', syn['error'], True),
            row('', 'WARN', syn['warning'], True),
            row('Log info / debug', 'INFO', syn['string']),
            row('', 'DEBUG', syn['libfn']),
            row('Diff added / removed', '+ added', ui['green']),
            row('', '- removed', ui['red']),
        ]),
    ]

    W, PAD, GAP, RH = 1500, 56, 36, 34
    COLW = (W - 2 * PAD - GAP) // 2
    def col_h(c): return sum(40 + RH * len(rows) + 12 for _, rows in c)
    code = sample(syn, kw_bold, ct_bold)
    H = 150 + max(col_h(left), col_h(right)) + 26 + 50 + len(code) * 28 + 56
    img = Image.new('RGB', (W * S, H * S), ui['bgDark'])
    d = ImageDraw.Draw(img)
    X = lambda v: v * S

    # header
    d.text((X(PAD), X(44)), f'Rosin · {name}', font=H1, fill=ui['fg'])
    d.text((X(PAD), X(92)), 'What each colour means', font=SUB, fill=ui['fgMuted'])
    sw = [('editor', ui['bg']), ('panels', ui['bgDark']), ('widgets', ui['bgWidget']), ('selection', ui['selection']), ('accent', ui['accent'])]
    x = W - PAD
    for lbl, c in reversed(sw):
        w = 96; x -= w
        d.rounded_rectangle((X(x + 10), X(46), X(x + w), X(78)), radius=X(6), fill=c, outline=ui['border'], width=S)
        d.text((X(x + 10), X(86)), lbl, font=MONO_S, fill=ui['fgMuted'])
        d.text((X(x + 10), X(102)), c, font=MONO_S, fill=ui['fgFaint'])

    PANEL_H = max(col_h(left), col_h(right))
    def draw_col(cols, px):
        y = 150
        d.rounded_rectangle((X(px), X(y - 14), X(px + COLW), X(y + PANEL_H - 4)), radius=X(10), fill=ui['bg'])
        x0 = px + 22
        for sec, rows in cols:
            d.text((X(x0), X(y + 4)), sec, font=H2, fill=ui['fgMuted'])
            y += 40
            for label, ex, colr, b, it, u in rows:
                cy = y + RH / 2
                d.ellipse((X(x0), X(cy - 7), X(x0 + 14), X(cy + 7)), fill=colr)
                if label:
                    d.text((X(x0 + 26), X(cy)), label, font=LBL, fill=ui['fgUi'], anchor='lm')
                fnt = MONO[(b, it)]
                d.text((X(x0 + 280), X(cy)), ex, font=fnt, fill=colr, anchor='lm')
                if u:
                    w = fnt.getlength(ex) / S
                    d.line((X(x0 + 280), X(cy + 10), X(x0 + 280 + w), X(cy + 10)), fill=colr, width=S)
                d.text((X(px + COLW - 22), X(cy)), colr, font=MONO_S, fill=ui['fgFaint'], anchor='rm')
                y += RH
            y += 12
    draw_col(left, PAD)
    draw_col(right, PAD + COLW + GAP)

    # sample editor
    y0 = 150 + PANEL_H + 26
    x0 = PAD
    d.rounded_rectangle((X(x0), X(y0), X(W - PAD), X(y0 + 50 + len(code) * 28)), radius=X(10), fill=ui['bg'], outline=ui['border'], width=S)
    d.text((X(x0 + 20), X(y0 + 14)), 'sample.c', font=MONO_S, fill=ui['fgMuted'])
    yy = y0 + 42
    for i, line in enumerate(code, 1):
        if i == 9:
            d.rectangle((X(x0 + 1), X(yy - 2), X(W - PAD - 1), X(yy + 26)), fill=ui['bgHover'])
        d.text((X(x0 + 44), X(yy + 12)), str(i), font=CODE[(False, False)], fill=ui['lineNum'], anchor='rm')
        cx = x0 + 70
        for text, colr, b, it in line:
            f = CODE[(b, it)]
            d.text((X(cx), X(yy + 12)), text, font=f, fill=colr, anchor='lm')
            cx += f.getlength(text) / S
        yy += 28
    return img

def sample(s, kw_bold, ct_bold):
    def t(x, k, b=False, i=False): return (x, s[k] if k in s else k, b, i)
    K = lambda x: t(x, 'keyword', kw_bold)
    P = lambda x: t(x, 'punct'); SP = (' ', s['variable'], False, False)
    return [
        [t('#include', 'directive'), SP, t('<stdint.h>', 'string')],
        [t('#define', 'directive'), SP, t('LED_PIN', 'macro', True), SP, t('13', 'number')],
        [],
        [t('/** Toggle the LED. ', 'doc', False, True), t('@param', 'composite', False, True), t(' on  new state */', 'doc', False, True)],
        [t('static', 'qualifier', False, True), SP, t('uint32_t', 'prim'), SP, t('g_ticks', 'globalvar'), SP, t('=', 'quietop'), SP, t('0', 'number'), P(';')],
        [t('typedef', 'keyword', ct_bold, True), SP, t('struct', 'composite'), SP, P('{'), SP, t('uint8_t', 'prim'), SP, t('pin', 'member'), P(';'), SP, P('}'), SP, t('led_t', 'composite'), P(';')],
        [],
        [t('void', 'prim'), SP, t('led_set', 'function'), P('('), t('led_t', 'composite'), SP, t('*', 'hazard', True), t('led', 'param', False, True), P(','), SP, t('bool', 'prim'), SP, t('on', 'param', False, True), P(')'), SP, P('{')],
        [t('    // debounce the button before toggling', 'comment', False, True)],
        [t('    ', 'variable'), K('if'), SP, P('('), t('on', 'param', False, True), P(')'), SP, t('*', 'hazard', True), t('ODR', 'variable'), SP, t('|=', 'hazard'), SP, t('1', 'number'), t('u', 'unit'), SP, t('<<', 'hazard'), SP, t('led', 'param', False, True), t('->', 'hazard', True), t('pin', 'member'), P(';')],
        [t('    ', 'variable'), t('printf', 'libfn'), P('('), t('"led ', 'string'), t('%d', 'hazard', True), t('\\n', 'escape'), t('"', 'string'), P(','), SP, t('led', 'param', False, True), t('->', 'hazard', True), t('pin', 'member'), P(')'), P(';')],
        [t('    ', 'variable'), K('return'), P(';')],
        [P('}')],
    ]

def window(name, r, w=640):
    """A small editor 'window' showing sample.c in one flavour (for the README preview)."""
    ui, syn = r['ui'], r['syn']
    style = NEW.get(name, {}).get('style', {})
    kw_bold = 'bold' in style.get('Keywords & control flow (amber)', '')
    ct_bold = 'bold' in style.get('Compile-time keywords (typedef sizeof alignof)', '')
    code = sample(syn, kw_bold, ct_bold)
    LH, TOP, AB = 23, 74, 40
    h = TOP + len(code) * LH + 22
    im = Image.new('RGB', (w * S, h * S), ui['bg'])
    d = ImageDraw.Draw(im)
    X = lambda v: v * S
    small = {k: ImageFont.truetype(v.path, 13 * S) for k, v in MONO.items()}
    # title bar, tab strip, activity bar
    d.rectangle((0, 0, X(w), X(30)), fill=ui['bgDark'])
    for i, col in enumerate((ui['red'], ui['warm'], ui['green'])):
        d.ellipse((X(14 + i * 18), X(10), X(24 + i * 18), X(20)), fill=col)
    d.text((X(w / 2), X(15)), f'Rosin · {name}', font=F(INTER + 'Inter-SemiBold.otf', 12), fill=ui['fgMuted'], anchor='mm')
    d.rectangle((0, X(30), X(AB), X(h)), fill=ui['bgDark'])
    for i in range(4):
        d.rounded_rectangle((X(12), X(48 + i * 34), X(28), X(64 + i * 34)), radius=X(3),
                            fill=ui['accent'] if i == 0 else ui['iconInactive'])
    d.rectangle((X(AB), X(30), X(w), X(56)), fill=ui['bgDark'])
    d.rectangle((X(AB), X(30), X(AB + 112), X(56)), fill=ui['bg'])
    d.line((X(AB), X(30), X(AB + 112), X(30)), fill=ui['accent'], width=X(2))
    d.text((X(AB + 14), X(43)), 'sample.c', font=F(INTER + 'Inter-Regular.otf', 12), fill=ui['fg'], anchor='lm')
    yy = TOP - 8
    for i, line in enumerate(code, 1):
        if i == 9:
            d.rectangle((X(AB), X(yy - 1), X(w), X(yy + LH - 2)), fill=ui['bgHover'])
        d.text((X(AB + 30), X(yy + LH / 2 - 1)), str(i), font=small[(False, False)], fill=ui['lineNum'], anchor='rm')
        cx = AB + 44
        for text, colr, b, it in line:
            f = small[(b, it)]
            d.text((X(cx), X(yy + LH / 2 - 1)), text, font=f, fill=colr, anchor='lm')
            cx += f.getlength(text) / S
        yy += LH
    return im

if __name__ == '__main__':
    for name, r in REPORT.items():
        img = sheet(name, r)
        fn = os.path.join(OUT, 'rosin-' + name.lower().replace(' ', '-') + '-cheatsheet.png')
        img.save(fn, optimize=True)
        print(fn, img.size)
    wins = [window(n, r) for n, r in REPORT.items()]
    cols, gap, pad = 3, 22 * S, 28 * S
    ww, wh = wins[0].size
    rows = (len(wins) + cols - 1) // cols
    canvas = Image.new('RGB', (pad * 2 + cols * ww + (cols - 1) * gap, pad * 2 + rows * wh + (rows - 1) * gap), '#0A0C10')
    for i, wimg in enumerate(wins):
        m = Image.new('L', wimg.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, ww - 1, wh - 1), radius=10 * S, fill=255)
        canvas.paste(wimg, (pad + (i % cols) * (ww + gap), pad + (i // cols) * (wh + gap)), m)
    pv = os.path.join(ROOT, 'images', 'preview.png')
    canvas.save(pv, optimize=True)
    print(pv, canvas.size)
