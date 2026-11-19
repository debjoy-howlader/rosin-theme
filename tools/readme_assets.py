"""Build the README assets: images/preview.png, colour swatches and the colour tables.

Usage:  python tools/readme_assets.py
Writes images/preview.png and images/swatches/*.png, and rewrites the block between
<!-- colours:start --> and <!-- colours:end --> in README.md.
Needs Pillow, plus DejaVu Sans Mono and Inter (falls back to DejaVu Sans).
"""
import os, sys, runpy
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMAGES = os.path.join(ROOT, 'images')

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

def role_rows(name, r):
    """(meaning, example, hex) rows for one flavour's README table."""
    ui, syn = r['ui'], r['syn']
    return [
        ('Editor background', '', ui['bg']),
        ('Panels / sidebar', '', ui['bgDark']),
        ('Selection', '', ui['selection']),
        ('UI accent', '', ui['accent']),
        ('Text / variable', '`count` `buf`', syn['variable']),
        ('Keyword / control flow', '`if` `for` `return`', syn['keyword']),
        ('Qualifier', '`const` `static` `extern`', syn['qualifier']),
        ('Function', '`led_set()`', syn['function']),
        ('Method', '`.write()`', syn['method']),
        ('Library / builtin function', '`printf` `memcpy`', syn['libfn']),
        ('Macro (bold)', '`LED_PIN` `println!`', syn['macro']),
        ('Preprocessor / attribute', '`#include` `#[derive]`', syn['directive']),
        ('Namespace / module', '`std` `core::ptr`', syn['scope']),
        ('Primitive type', '`int` `uint8_t` `u32`', syn['prim']),
        ('User type / type keyword', '`struct` `led_t` `trait`', syn['composite']),
        ('Parameter / self (italic)', '`len` `self`', syn['param']),
        ('Member / key / CLI flag', '`.pin` `name:` `--baud`', syn['member']),
        ('Global / config variable', '`g_ticks` `$(CC)`', syn['globalvar']),
        ('Static variable', '`s_state`', syn['staticvar']),
        ('Number / constant / enum', '`42` `0xFF` `true`', syn['number']),
        ('String', '`"hello"`', syn['string']),
        ('Escape', '`\\n` `&amp;`', syn['escape']),
        ('Hazard: pointer / bits / format', '`*` `->` `<<` `%d`', syn['hazard']),
        ('Operator', '`=` `+` `==`', syn['quietop']),
        ('Punctuation', '`;` `,` `{}`', syn['punct']),
        ('Comment (italic)', '`// note`', syn['comment']),
        ('Doc comment (italic)', '`/// returns`', syn['doc']),
        ('Error / log error', '`ERROR`', syn['error']),
        ('Warning / log warning', '`WARN`', syn['warning']),
        ('Diff added / removed', '`+` / `-`', ui['green'] + ' ' + ui['red']),
    ]

def swatch(hexc, size=18):
    """Small rounded swatch with a neutral outline so dark colours stay visible on any page."""
    path = os.path.join(IMAGES, 'swatches', hexc.lstrip('#').lower() + '.png')
    if not os.path.exists(path):
        k = 4
        im = Image.new('RGBA', (size * k, size * k), (0, 0, 0, 0))
        ImageDraw.Draw(im).rounded_rectangle((k, k, size * k - k - 1, size * k - k - 1), radius=4 * k,
                                             fill=hexc, outline='#7F7F7F', width=k)
        im.resize((size, size), Image.LANCZOS).save(path, optimize=True)
    return f'![{hexc}](images/swatches/{hexc.lstrip("#").lower()}.png)'

def tables():
    out = []
    for name, r in REPORT.items():
        out += [f'### Rosin · {name}', '', '| | Meaning | Example | Hex |', '|:-:|---|---|---|']
        for meaning, ex, hx in role_rows(name, r):
            hexes = hx.split()
            sw = ' '.join(swatch(h) for h in hexes)
            out.append(f'| {sw} | {meaning} | {ex} | {" ".join("`" + h + "`" for h in hexes)} |')
        out.append('')
    return '\n'.join(out)

if __name__ == '__main__':
    os.makedirs(os.path.join(IMAGES, 'swatches'), exist_ok=True)
    for f in os.listdir(os.path.join(IMAGES, 'swatches')):
        os.remove(os.path.join(IMAGES, 'swatches', f))
    wins = [window(n, r) for n, r in REPORT.items()]
    cols, gap, pad = 3, 22 * S, 28 * S
    ww, wh = wins[0].size
    rows = (len(wins) + cols - 1) // cols
    canvas = Image.new('RGB', (pad * 2 + cols * ww + (cols - 1) * gap, pad * 2 + rows * wh + (rows - 1) * gap), '#0A0C10')
    for i, wimg in enumerate(wins):
        m = Image.new('L', wimg.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, ww - 1, wh - 1), radius=10 * S, fill=255)
        canvas.paste(wimg, (pad + (i % cols) * (ww + gap), pad + (i // cols) * (wh + gap)), m)
    canvas.save(os.path.join(IMAGES, 'preview.png'), optimize=True)
    md = tables()
    readme = os.path.join(ROOT, 'README.md')
    text = open(readme, encoding='utf-8').read()
    a, b = text.index('<!-- colours:start -->'), text.index('<!-- colours:end -->')
    text = text[:a] + '<!-- colours:start -->\n' + md + '\n' + text[b:]
    open(readme, 'w', encoding='utf-8').write(text)
    print('preview, %d swatches, README tables updated' % len(os.listdir(os.path.join(IMAGES, 'swatches'))))
