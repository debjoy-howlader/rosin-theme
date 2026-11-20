"""Rosin theme generator: role tables per flavour -> full VS Code colour themes.

Usage:  python tools/gen.py            (writes ./themes/*.json next to tools/)
Edit flavours in NEW, UI colour assignments in fill_rules.py, extra token rules in token_rules.py.
The log-level grammar in ./syntaxes and package.json are maintained by hand."""
import json, os, re, sys, colorsys, copy
sys.path.insert(0, os.path.dirname(__file__))
from fill_rules import assign

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, 'base')               # Sweet C 1.0.1 sources
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)
KEYS = json.load(open(os.path.join(BASE, 'vscode-color-keys.json')))['all']

from token_rules import R, extra_rules, extra_semantic, base_edits, e1_rules, e2_rules, semantic_overrides, prune_shadowed

# ---------------------------------------------------------------- colour helpers
def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def hexc(t): return '#%02X%02X%02X' % tuple(max(0, min(255, round(x))) for x in t)
def mix(a, b, t): A, B = rgb(a), rgb(b); return hexc([A[i] + (B[i] - A[i]) * t for i in range(3)])
def lum(h):
    c = [x / 255 for x in rgb(h)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)
def tint(h, L=0.84, S=0.95):
    r, g, b = [x / 255 for x in rgb(h)]
    hh, _, _ = colorsys.rgb_to_hls(r, g, b)
    return hexc([x * 255 for x in colorsys.hls_to_rgb(hh, L, S)])
def lighten(h, t): return mix(h, '#FFFFFF', t)

# ---------------------------------------------------------------- role vocab
SYN_SS = {  # Sweet C Sea Salt hex -> syntax role (base rules only)
    '#7A8696': 'comment', '#AE9B7F': 'doc', '#75CCC4': 'composite', '#75C290': 'string', '#CB8871': 'escape',
    '#E2726B': 'hazard', '#D5C984': 'number', '#AEA581': 'unit', '#E59B5B': 'keyword', '#8A939E': 'quietop',
    '#6F9895': 'scope', '#5EA0CD': 'prim', '#9CADCB': 'qualifier', '#7DABB0': 'member', '#B5A4FF': 'function',
    '#AEA7ED': 'function', '#8D96BE': 'libfn', '#C6CDD4': 'variable', '#C2B7DB': 'param', '#AB81AD': 'directive',
    '#E497CE': 'macro', '#6A727D': 'punct', '#E97074': 'error', '#DEAF97': 'globalvar', '#ADC6A8': 'staticvar',
    '#C0B2FF': 'method',
}
UI_SS = {  # Sweet C Sea Salt hex -> UI role
    '#13171F': 'bg', '#0D1117': 'bgDark', '#1B212A': 'bgWidget', '#1A1E26': 'bgHover', '#262C35': 'border',
    '#C6CDD4': 'fg', '#A4ACB4': 'fgUi', '#79818B': 'fgMuted', '#5A616B': 'fgFaint', '#575E69': 'lineNum',
    '#292E36': 'whitespace', '#20242B': 'indent', '#454D5E': 'indentActive', '#626A75': 'iconInactive',
    '#AEA7ED': 'accent', '#E59B5B': 'warm', '#E97074': 'red', '#75C290': 'green', '#5EA0CD': 'blue', '#E2726B': 'coral',
    '#75CCC4': 'cyan', '#D5C984': 'yellow', '#333A5F': 'selection', '#605EAB': 'button', '#716FC1': 'buttonHover',
    '#47457C': 'badge', '#6F341F': 'debugBg', '#424171': 'remoteBg', '#371112': 'errBg', '#331F04': 'warnBg',
    '#76BD97': 'untracked', '#FFFFFF': 'white', '#000000': 'black', '#7C8799': 'inlay', '#8989A4': 'inlayParam',
    '#709496': 'inlayType', '#8F9FBB': 'br1', '#88AC91': 'br2', '#B392AF': 'br3', '#B8A680': 'br4', '#7CB0AF': 'br5',
    '#BF928D': 'br6', '#1E2229': 'ansiBlack', '#FE8A88': 'bRed', '#86DB9D': 'bGreen', '#EFCD79': 'bYellow',
    '#8ACCFE': 'bBlue', '#BBBDFE': 'bMagenta', '#84E1D9': 'bCyan',
}
HEXRE = re.compile(r'#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?$')

def to_ref(val, table, prefix=''):
    a = val[7:] if len(val) == 9 else ''
    role = table.get(val[:7].upper())
    if role is None:
        raise KeyError(f'unmapped {val}')
    return prefix + role + ('@' + a.upper() if a else '')

def templatize(o, table, prefix=''):
    if isinstance(o, str) and HEXRE.match(o):
        return {'$ref': to_ref(o, table, prefix)}
    if isinstance(o, dict):
        return {k: templatize(v, table, prefix) for k, v in o.items()}
    if isinstance(o, list):
        return [templatize(v, table, prefix) for v in o]
    return o

def resolve_ref(ref, ui, syn):
    if ref == 'none':
        return '#00000000'
    r, _, a = ref.partition('@')
    if r.startswith('syn:'):
        h = syn[r[4:]]
    else:
        h = ui[r]
    return h + a

def render(o, ui, syn):
    if isinstance(o, dict) and '$ref' in o:
        return resolve_ref(o['$ref'], ui, syn)
    if isinstance(o, dict):
        return {k: render(v, ui, syn) for k, v in o.items()}
    if isinstance(o, list):
        return [render(v, ui, syn) for v in o]
    return o

# ---------------------------------------------------------------- templates from Sweet C
ss = json.load(open(f'{BASE}/sweet-c-sea-salt.json', encoding='utf-8'))
bc = json.load(open(f'{BASE}/sweet-c-black-cherry.json', encoding='utf-8'))
T_COLORS = templatize(ss['colors'], UI_SS)
T_TOKENS = templatize(ss['tokenColors'], SYN_SS, 'syn:')
T_SEM = templatize(ss['semanticTokenColors'], SYN_SS, 'syn:')
for r in T_TOKENS:   # section headings follow the function colour
    sc = r['scope'][0] if isinstance(r['scope'], list) else r['scope']
    if sc == 'entity.name.section':
        r['settings']['foreground'] = {'$ref': 'syn:function'}

unassigned = []
for k in KEYS:
    if k in T_COLORS:
        continue
    v = assign(k)
    if v is None:
        unassigned.append(k); continue
    T_COLORS[k] = {'$ref': v}
if unassigned:
    print('UNASSIGNED', unassigned)

def extract(theme, table, section_pairs):
    """Read role values for an existing flavour by aligning it with Sea Salt."""
    out = {}
    def walk(a, b):
        if isinstance(a, dict) and '$ref' in a:
            bb = b if isinstance(b, str) else b.get('foreground')
            role = a['$ref'].split('@')[0].replace('syn:', '')
            out.setdefault(role, bb[:7].upper())
        elif isinstance(a, dict):
            for k in a:
                if isinstance(b, str):   # bc has plain string where ss has style object
                    if k == 'foreground': walk(a[k], b)
                elif k in b:
                    walk(a[k], b[k])
        elif isinstance(a, list):
            for x, y in zip(a, b): walk(x, y)
    for t, s in section_pairs:
        walk(t, s)
    return out

def derive_extra_ui(u):
    u.setdefault('bgHover2', mix(u['bgWidget'], u['fg'], 0.05))
    u.setdefault('infoBg', mix(u['blue'], u['bg'], 0.82))
    u.setdefault('errBg2', mix(u['red'], u['bg'], 0.62))
    u.setdefault('warnBg2', mix(u['warm'], u['bg'], 0.62))
    return u

# existing flavours: role values read back from their Sweet C files
ROLE = {}
ss_ui = extract(ss, UI_SS, [({k: v for k, v in T_COLORS.items() if k in ss['colors']}, ss['colors'])])
ss_syn = extract(ss, SYN_SS, [(T_TOKENS, ss['tokenColors']), (T_SEM, ss['semanticTokenColors'])])
bc_ui = extract(bc, UI_SS, [({k: v for k, v in T_COLORS.items() if k in bc['colors']}, bc['colors'])])
bc_syn = extract(bc, SYN_SS, [(T_TOKENS, bc['tokenColors']), (T_SEM, bc['semanticTokenColors'])])
ss_syn['function'] = '#B5A4FF'      # 1.0.1 change
ROLE['Sea Salt'] = (derive_extra_ui(ss_ui), ss_syn)
ROLE['Black Cherry'] = (derive_extra_ui(bc_ui), bc_syn)

# ---------------------------------------------------------------- new flavours
def derive_ui(s, syn):
    bg, fg = s['bg'], s['fg']
    u = dict(
        bg=bg, bgDark=s.get('bgDark', mix(bg, '#000000', 0.32)), bgWidget=mix(bg, fg, 0.055), bgHover=mix(bg, fg, 0.03),
        border=mix(bg, fg, 0.10), fg=fg, fgUi=mix(fg, bg, 0.15), fgMuted=mix(fg, bg, 0.40), fgFaint=mix(fg, bg, 0.60),
        lineNum=mix(fg, bg, 0.61), whitespace=mix(bg, fg, 0.09), indent=mix(bg, fg, 0.055), indentActive=mix(bg, fg, 0.22),
        iconInactive=mix(fg, bg, 0.55), accent=s['accent'], warm=s['warm'], red=s['red'], green=s['green'], blue=s['blue'],
        coral=s['coral'], cyan=s['cyan'], yellow=s['yellow'], selection=mix(bg, s['accent'], 0.26),
        button=mix(s['accent'], bg, 0.50), buttonHover=mix(s['accent'], bg, 0.40), badge=mix(s['accent'], bg, 0.62),
        debugBg=mix(s['warm'], bg, 0.62), remoteBg=mix(s['accent'], bg, 0.66), errBg=mix(s['red'], bg, 0.82),
        warnBg=mix(s['warm'], bg, 0.84), untracked=s['green'], white='#FFFFFF', black='#000000',
        inlay=mix(fg, bg, 0.38), inlayParam=mix(syn['param'], bg, 0.30), inlayType=mix(syn['composite'], bg, 0.35),
        ansiBlack=mix(bg, fg, 0.05),
    )
    for i, k in enumerate(s.get('brackets', ['function', 'string', 'macro', 'number', 'composite', 'hazard']), 1):
        u[f'br{i}'] = mix(syn[k] if k in syn else k, fg, 0.30)
    for k, base in (('bRed', 'red'), ('bGreen', 'green'), ('bYellow', 'yellow'), ('bBlue', 'blue'), ('bMagenta', 'accent'), ('bCyan', 'cyan')):
        u[k] = lighten(u[base], 0.25)
    u.update(s.get('ui_over', {}))
    return derive_extra_ui(u)

def syn_extra(syn, ui):
    syn = dict(syn)
    syn.setdefault('warning', ui['warm']); syn.setdefault('info', ui['blue'])
    syn.setdefault('typeparam', syn['prim']); syn.setdefault('namespace', syn['scope']); syn.setdefault('doctag', syn['composite'])
    return syn

NEW = {
    'Matcha': dict(
        bg='#141A17', fg='#CBD4CB', accent='#9CC97A', warm='#E0B070', red='#EC7A7A', green='#8CCB86', blue='#7FB2DB',
        coral='#E57A6E', cyan='#7CCBB4', yellow='#D8C38A',
        syn=dict(comment='#7E8D82', doc='#AEA382', string='#D8C38A', escape='#D9A274', hazard='#E57A6E', number='#B9B8EE',
                 unit='#B9A08A', keyword='#E8A0AA', quietop='#8E9C92', scope='#73A08E', prim='#7FB8D6', composite='#7CCBB4',
                 qualifier='#A2B8AE', member='#A3B9C8', function='#A8D17E', method='#B8DA92', libfn='#93A88C',
                 variable='#CBD4CB', param='#C8BFDA', directive='#B49AC0', macro='#DFA2D6', punct='#6C796F', error='#EC7A7A',
                 globalvar='#E2C39E', staticvar='#B9D0A8')),
    'Espresso': dict(
        bg='#1B1714', fg='#DDD2C6', accent='#D9A15E', warm='#E3C46F', red='#EA7070', green='#9AC68C', blue='#88B0D4',
        coral='#E3785E', cyan='#86C2B2', yellow='#E3CB88',
        syn=dict(comment='#918376', doc='#B7A487', string='#A9C48E', escape='#D8A26C', hazard='#E3785E', number='#C7B5E4',
                 unit='#BEA18A', keyword='#DE8C6C', quietop='#A2968C', scope='#8AA59C', prim='#8DB2CD', composite='#86C2B2',
                 qualifier='#B5ACBA', member='#AABAC5', function='#E8B565', method='#EEC47F', libfn='#B59D7A',
                 variable='#DDD2C6', param='#CEC0D8', directive='#BB91AC', macro='#DA9DC6', punct='#7C7066', error='#EA7070',
                 globalvar='#E7C4A1', staticvar='#BDC9A5')),
    'Licorice': dict(   # stealth: greys + three quiet accents (steel, sage, coral)
        bg='#121314', fg='#CACCCE', accent='#94B9DA', warm='#C9A66B', red='#D9827A', green='#9CB896', blue='#94B9DA',
        coral='#D9827A', cyan='#A9C4C8', yellow='#C9C2A0',
        brackets=['#9DA1A5', '#B4B7BA', '#94B9DA', '#8A8E92', '#C3C6C9', '#A7ABAF'],
        syn=dict(comment='#7A7E82', doc='#8F9397', string='#A7BDA2', escape='#C3C7CA', hazard='#D9827A', number='#DDDFE1',
                 unit='#A3A6A9', keyword='#8E9296', quietop='#8A8E92', scope='#7F8387', prim='#A6AAAE', composite='#D6D8DA',
                 qualifier='#868A8E', member='#B3B6B9', function='#94B9DA', method='#A7C6E2', libfn='#8FA2B5',
                 variable='#CACCCE', param='#B9BCBF', directive='#808488', macro='#E4E6E8', punct='#66696D', error='#D9827A',
                 globalvar='#E8E9EA', staticvar='#C0C3C6'),
        style={'Keywords & control flow (amber)': 'bold', 'Compile-time keywords (typedef sizeof alignof)': 'bold italic',
               # E1: rules that now carry the keyword colour keep Licorice's bold keywords
               'Type-declaring keywords (class interface type enum namespace)': 'bold', 'E1 Rust declaration keywords (storage.type.rust innermost)': 'bold',
               'E1 C/C++ inline asm keyword': 'bold', 'E1 C++ template and typename keywords (P1)': 'bold', 'E1 Kconfig keywords': 'bold', 'E1 Make .PHONY and special targets': 'bold',
               'E1 Shell && and ||': 'bold', 'E1 Git commit subject': 'bold',
               # E2 keyword-coloured rules
               'E2 C++ keywords the grammar scopes as types or operators (decltype noexcept requires)': 'bold', 'E2 Python global / nonlocal': 'bold', 'E2 YAML list dash (same as list bullets)': 'bold',
               'E2 Git status words in commit comments (new file, deleted)': 'bold', 'E2 Rust macro_rules!': 'bold', 'E2 Rust static and super keywords': 'bold', 'E2 Shell alias keyword': 'bold', 'E2 Rust macro fragment specifiers (expr ty ident)': 'bold'},
        ui_over=dict(button='#3E5468', buttonHover='#4A6379', badge='#2E3A46', selection='#2A3540')),
}

NEW.update({
    'OLED': dict(   # Sea Salt syntax on pure black
        bg='#000000', bgDark='#000000', fg='#C6CDD4', accent='#AEA7ED', warm='#E59B5B', red='#E97074', green='#75C290',
        blue='#5EA0CD', coral='#E2726B', cyan='#75CCC4', yellow='#D5C984',
        syn={k: v for k, v in ROLE['Sea Salt'][1].items() if k in ('comment','doc','string','escape','hazard','number','unit','keyword','quietop','scope','prim','composite','qualifier','member','function','method','libfn','variable','param','directive','macro','punct','error','globalvar','staticvar')},
        ui_over=dict(bgWidget='#0D0E10', bgHover='#0B0C0E', border='#1C1F25', indent='#14161A', whitespace='#1E2126',
                     ansiBlack='#15171A', button='#4E4C93', buttonHover='#5D5BA8', badge='#33325A', selection='#2A2840')),
})

def LABEL(n): return f'Rosin · {n}'
def FILE(n): return 'rosin-' + n.lower().replace(' ', '-') + '.json'

def fill_syn(syn, fg, bg):
    syn = dict(syn)
    syn.setdefault('method', mix(syn['function'], fg, 0.15))
    syn.setdefault('libfn', mix(syn['function'], bg, 0.22))
    syn.setdefault('doc', mix(syn['comment'], fg, 0.25))
    syn.setdefault('unit', mix(syn['number'], bg, 0.22))
    syn.setdefault('quietop', mix(fg, bg, 0.35))
    syn.setdefault('punct', mix(fg, bg, 0.50))
    syn.setdefault('staticvar', mix(syn['string'], fg, 0.35))
    syn.setdefault('globalvar', mix(syn['number'], fg, 0.25))
    syn.setdefault('escape', syn['hazard'])
    syn.setdefault('error', syn['hazard'])
    syn.setdefault('qualifier', mix(syn['keyword'], fg, 0.35))
    syn.setdefault('scope', mix(syn['composite'], bg, 0.25))
    syn.setdefault('param', mix(fg, syn['keyword'], 0.15))
    syn.setdefault('variable', fg)
    return syn

for name, s in list(NEW.items()):
    s['syn'] = fill_syn(s['syn'], s['fg'], s['bg'])
    ui = derive_ui(s, s['syn'])
    ROLE[name] = (ui, s['syn'])

# ---------------------------------------------------------------- build
def tag_rules(ui, syn):
    # TODO/FIXME highlighting is left to dedicated extensions; Python's built-in
    # codetag scope is pinned to the plain comment style so it doesn't pick up keyword colour.
    return [R('Python code tags render as plain comments', ['keyword.codetag.notation.python'], syn['comment'], 'italic')], ()

report = {}
REPORT = {}
SHADOWED = {}
os.makedirs(f'{OUT}/themes', exist_ok=True)
for name, (ui, syn0) in ROLE.items():
    syn = syn_extra(syn0, ui)
    colors = render(T_COLORS, ui, syn)
    colors = {k: v for k, v in colors.items()}
    tokens = render(T_TOKENS, ui, syn)
    style = NEW.get(name, {}).get('style', {})
    tokens = base_edits(tokens)
    extras = extra_rules(syn) + e1_rules(syn) + e2_rules(syn)
    for r in tokens + extras:
        if r.get('name') in style:
            r['settings']['fontStyle'] = style[r['name']]
    tags, tagcols = tag_rules(ui, syn)
    sem = render(T_SEM, ui, syn)
    for k, v in extra_semantic(syn).items():
        sem.setdefault(k, v)
    sem.update(semantic_overrides(syn))
    pruned, shadowed = prune_shadowed(tokens + extras + tags)
    SHADOWED[name] = shadowed
    theme = {
        '$schema': 'vscode://schemas/color-theme',
        'name': LABEL(name), 'type': 'dark', 'semanticHighlighting': True,
        'semanticTokenColors': sem, 'colors': colors, 'tokenColors': pruned,
    }
    fn = FILE(name)
    json.dump(theme, open(f'{OUT}/themes/{fn}', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    report[name] = dict(file=fn, ui=ui, syn=syn, tags=tagcols, ncolors=len(colors))
    REPORT[name] = report[name]

print({k: (v['file'], v['ncolors'], v['tags']) for k, v in report.items()})
