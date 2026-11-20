"""Write the per-language support section of README.md and the full limits register.

Usage:  python tools/readme_languages.py
Reads   audit/register/limits-register.json   (built by audit/harness/register.py from the final audit)
        audit/reports/A5-T.json, A5-S.json     (token counts per language and mode)
Writes  the block between <!-- languages:start --> and <!-- languages:end --> in README.md
        audit/register/limits-register.md
"""
import os, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AUD = os.path.join(ROOT, 'audit')
REGISTER_LINK = 'audit/register/limits-register.md'
TESTED_VSCODE = '1.147.0'

ROLE = dict(variable='text', keyword='keyword', qualifier='qualifier', function='function', method='method',
            libfn='library function', macro='macro', directive='preprocessor / attribute', namespace='namespace',
            scope='namespace', prim='primitive type', typeparam='primitive type', composite='user type',
            doctag='user type', param='parameter', member='member / key', globalvar='global / config variable',
            staticvar='static variable', number='number / constant', unit='unit', string='string', escape='escape',
            hazard='hazard', quietop='operator', punct='punctuation', comment='comment', doc='doc comment',
            error='error', warning='warning', info='info')

def ext(name, ident, version):
    return f'{name} (`{ident}`) {version}'

# One entry per README section. modes: harness mode -> label used in the text.
LANGS = [
    dict(title='C and C++', langs=['c', 'cpp'], grammar='built in',
         recommended=[ext('C/C++', 'ms-vscode.cpptools', '1.35.6'),
                      ext('clangd', 'llvm-vs-code-extensions.vscode-clangd', '0.6.0') + ' with clangd 23.1.0'],
         modes={'S-cpptools': 'cpptools', 'S-clangd': 'clangd'},
         note='Use one server or the other. clangd tells more roles apart: library functions, deduced types, concepts '
              'and file-scope statics. The two servers label a few tokens differently, so those tokens change colour '
              'when you switch. The servers were tested with `"C_Cpp.enhancedColorization": "enabled"` (the default).'),
    dict(title='Rust', langs=['rust'], grammar='built in',
         recommended=[ext('rust-analyzer', 'rust-lang.rust-analyzer', '0.3.3121')], modes={'S-rust': 'rust-analyzer'},
         note='rust-analyzer could not resolve standard-library macros such as `println!` and `write!` on '
              'Rust 1.93.1. Rosin shows unresolved names in the error style (red, bold, underlined), so these calls '
              'look like errors. This is a toolchain problem, not a theme rule; it goes away when rust-analyzer can '
              'resolve the standard library.'),
    dict(title='Python', langs=['python'], grammar='built in',
         recommended=[ext('Pylance', 'ms-python.vscode-pylance', '2026.4.1') + ', with ' + ext('Python', 'ms-python.python', '2026.10.0')],
         modes={'S-Pylance': 'Pylance'},
         note='Pylance brings its own grammar as well as semantic tokens, so "without a language server" here means '
              'without Pylance.'),
    dict(title='Shell (bash)', langs=['shellscript'], grammar='built in', recommended=[], modes={},
         note='Tested with ' + ext('Bash IDE', 'mads-hartmann.bash-ide-vscode', '1.43.2') + ' installed. It provides no '
              'semantic tokens, so colours are the same with or without it.'),
    dict(title='Makefiles', langs=['makefile'], grammar='built in', recommended=[], modes={},
         note='Tested with ' + ext('Makefile Tools', 'ms-vscode.makefile-tools', '0.12.17') + ' installed; it does not change colours.'),
    dict(title='CMake', langs=['cmake'], grammar=ext('CMake Tools', 'ms-vscode.cmake-tools', '1.25.10'), recommended=[], modes={},
         note='VS Code has no built-in CMake grammar. Other CMake grammar extensions were not tested.'),
    dict(title='JSON and JSONC', langs=['json', 'jsonc'], grammar='built in', recommended=[], modes={}),
    dict(title='YAML', langs=['yaml'], grammar='built in', recommended=[], modes={},
         note='Tested with ' + ext('YAML', 'redhat.vscode-yaml', '2.0.0') + ' installed. It provides no semantic tokens.'),
    dict(title='TOML', langs=['toml'], grammar=ext('Even Better TOML', 'tamasfe.even-better-toml', '0.21.2'),
         recommended=[], modes={'S-EvenBetterTOML': 'Even Better TOML'},
         note='The same extension provides the grammar and the semantic tokens.'),
    dict(title='INI', langs=['ini'], grammar='built in', recommended=[], modes={}),
    dict(title='Markdown', langs=['markdown'], grammar='built in', recommended=[], modes={},
         note='Fenced code blocks use the grammar of their language, so the sections for those languages apply.'),
    dict(title='Log files', langs=['log'], grammar='built in, plus Rosin\'s own log-level grammar', recommended=[], modes={},
         note='Rosin recognises ESP-IDF style (`E (512) tag:`) and Zephyr style (`<err>`) levels, panic and fault messages.'),
    dict(title='Diffs and git commit messages', langs=['diff', 'git-commit'], grammar='built in', recommended=[], modes={}),
    dict(title='ARM assembly', langs=['arm'], grammar=ext('Arm Assembly', 'dan-c-underwood.arm', '1.7.4'), recommended=[], modes={}),
    dict(title='Linker scripts', langs=['linkerscript'], grammar=ext('LinkerScript', 'ZixuanWang.linkerscript', '1.0.4'), recommended=[], modes={}),
    dict(title='Devicetree', langs=['dts'], grammar=ext('DeviceTree', 'plorefice.devicetree', '0.1.1'), recommended=[], modes={}),
    dict(title='Kconfig', langs=['kconfig'], grammar=ext('ESP-IDF', 'espressif.esp-idf-extension', '2.3.0'), recommended=[], modes={},
         note='The ESP-IDF extension provides the Kconfig grammar.'),
]

LIVE = {'python/corpus.py': 'S-Pylance', 'config/corpus.toml': 'S-EvenBetterTOML'}

def load_rows(name):
    return [x for x in json.load(open(os.path.join(AUD, 'reports', name), encoding='utf-8'))
            if not x.get('summary') and not x.get('error')]

def norm(actual):
    if not actual or actual == 'unmapped:':
        return 'text'
    if actual.startswith('unmapped:'):
        return 'two colours'
    return ROLE.get(actual.split('|')[0], actual)

def esc(text):
    """Escape < and > outside code spans so names like <name> are not read as HTML tags."""
    parts = text.split('`')
    return '`'.join(p.replace('<', '&lt;').replace('>', '&gt;') if i % 2 == 0 else p for i, p in enumerate(parts))

MODE_NAME = {'T': 'no server', 'S-cpptools': 'cpptools', 'S-clangd': 'clangd', 'S-rust': 'rust-analyzer',
             'S-Pylance': 'Pylance', 'S-EvenBetterTOML': 'Even Better TOML'}

def tok(t):
    if t.startswith('~') and len(t) > 1: t = t[1:]          # corpus marker: raw substring
    if '#' in t[1:] and t.rsplit('#', 1)[1].isdigit(): t = t.rsplit('#', 1)[0]   # corpus marker: nth occurrence
    return '`` ` ``' if t == '`' else f'`{t}`'

def main():
    reg = json.load(open(os.path.join(AUD, 'register', 'limits-register.json'), encoding='utf-8'))
    E = reg['entries']
    T, S = load_rows('A5-T.json'), load_rows('A5-S.json')
    token_of = {(x['file'], x['component']): x['token'] for x in T}
    role_of = {(x['file'], x['component']): x['expect']['role'] for x in T}

    # token counts per language and mode, counting deliberate multi-colour tokens as designed
    design = {(e['file'], e['component'], e['mode']) for e in E if e['reason'] == 'DESIGN'}
    counts = collections.defaultdict(lambda: collections.Counter())
    for x in S:
        for m, o in x['modes'].items():
            if m == 'S-servers':
                if x['file'] not in LIVE: continue
                m = LIVE[x['file']]
            counts[(x['lang'], m)]['n'] += 1
            if o['v'] == 'EXACT' or (x['file'], x['component'], m) in design:
                counts[(x['lang'], m)]['ok'] += 1

    def why(e):
        if e['reason'] == 'NEEDS-SERVER':
            return 'only a language server can tell'
        if e['reason'] == 'ID':
            extra = e['evidence'][e['evidence'].find('('):].rstrip('.') if '(' in e['evidence'] else ''
            return ('the grammar puts the name itself in the scope (variable.other.unknown.<name>), so no rule can match the role'
                    + (' ' + extra if extra else ''))
        if e.get('computed'):
            ref = e['evidence'].split('`')[1]
            other = (e['file'], ref)
            what = 'the grammar scopes it' if e['reason'] == 'SS' else 'the server labels it'
            rt, rr = token_of.get(other, ref), ROLE.get(role_of.get(other, ''), 'another role')
            if tok(rt) == tok(e['token']):
                return f'{what} exactly like the {rr} {tok(rt)} elsewhere in the file'
            return f'{what} exactly like {tok(rt)} ({rr})'
        return e['evidence'].rstrip('.')

    md = []
    for L in LANGS:
        ents = [e for e in E if e['lang'] in L['langs'] and e['reason'] != 'DESIGN']
        allmodes = ['T'] + list(L['modes'])
        md += [f'### {L["title"]}', '']
        md.append(f'- **Grammar:** {L["grammar"]}.')
        if L['recommended']:
            md.append('- **Recommended:** ' + '; or '.join(L['recommended']) + '.')
        cnt = []
        for m in allmodes:
            c = collections.Counter()
            for lg in L['langs']: c.update(counts[(lg, m)])
            if c['n']:
                label = 'without a language server' if m == 'T' and L['modes'] else ('as tested' if m == 'T' else 'with ' + L['modes'][m])
                cnt.append(f'{c["ok"]} of {c["n"]} {label}')
        md.append('- **Checked tokens shown as designed:** ' + '; '.join(cnt) + '.')
        if L.get('note'):
            md.append('- ' + L['note'])
        md.append('')
        if not ents:
            md += ['No exceptions found.', '']
            continue
        def table(es):
            """Rows grouped by (should be, shown as, why); one table for one setup."""
            g = collections.defaultdict(list)
            for e in es:
                g[(e['expect'], norm(e['actual']), why(e))].append(e['token'])
            out = ['| Token | Should be | Shown as | Why |', '|---|---|---|---|']
            for (exp, act, w), toks in sorted(g.items(), key=lambda kv: (ROLE.get(kv[0][0], kv[0][0]), kv[0][1], kv[0][2])):
                ts = ', '.join(dict.fromkeys(tok(t).replace('|', '\\|') for t in toks))
                out.append(f'| {ts} | {ROLE.get(exp, exp)} | {act} | {esc(w).replace("|", chr(92) + "|")}. |')
            return out, sum(len(v) for v in g.values())

        def block_for(label, es):
            rows, n = table(es)
            if not es:
                return [f'**{label}:** no exceptions found.', '']
            count = f'{n} exception{"s" if n != 1 else ""}'
            head = f'<b>{count}</b>' if label == 'Exceptions' else f'<b>{label}</b>: {count}'
            return ['<details>', f'<summary>{head}</summary>', ''] + rows + ['', '</details>', '']

        if L['modes']:
            names = list(L['modes'].values())
            none = 'Neither ' + ' nor '.join(names) if len(names) > 1 else 'Without ' + names[0]
            md.append('Pick the line that matches what you have installed. Each list is complete for that setup.')
            md.append('')
            for m, label in [('T', none)] + [(m, 'With ' + n) for m, n in L['modes'].items()]:
                md += block_for(label, [e for e in ents if e['mode'] == m])
        else:
            md += block_for('Exceptions', ents)

    md.append(f'Every exception, with its evidence, is in the [limits register]({REGISTER_LINK}). '
              f'Tested on VS Code {TESTED_VSCODE}.')

    block = '\n'.join(md)
    readme = os.path.join(ROOT, 'README.md')
    raw = open(readme, 'rb').read().decode('utf-8')
    crlf = '\r\n' in raw
    text = raw.replace('\r\n', '\n')
    a, b = text.index('<!-- languages:start -->'), text.index('<!-- languages:end -->')
    text = text[:a] + '<!-- languages:start -->\n' + block + '\n' + text[b:]
    open(readme, 'wb').write((text.replace('\n', '\r\n') if crlf else text).encode('utf-8'))

    # full register
    R = ['# Rosin limits register', '',
         'Generated by `tools/readme_languages.py` from `limits-register.json`, which `audit/harness/register.py` builds '
         'from the final audit (`audit/reports/A5-*.json`). One row per checked token and mode where the colour is not the '
         'one the meaning table gives. The Mode column is the language server installed (\"no server\" is the grammar alone).', '',
         '## Reason codes', '', '| Code | Meaning |', '|---|---|']
    R += [f'| {k} | {v} |' for k, v in reg['reasons'].items()]
    R += ['', 'DESIGN rows are not exceptions: the token is coloured part by part on purpose. They are listed for completeness.', '']
    for L in LANGS:
        ents = sorted((e for e in E if e['lang'] in L['langs']), key=lambda e: (e['file'], e['line'], e['component'], e['mode']))
        R += [f'## {L["title"]}', '']
        if not ents:
            R += ['No exceptions.', '']; continue
        R += ['| File:line | Token | Mode | Expected | Shown | Reason | Evidence |', '|---|---|---|---|---|---|---|']
        for e in ents:
            ev = esc(e['evidence']).replace('|', '\\|')
            R.append(f'| {e["file"]}:{e["line"]} | {tok(e["token"]).replace("|", chr(92) + "|")} | {MODE_NAME.get(e["mode"], e["mode"])} | {ROLE.get(e["expect"], e["expect"])} '
                     f'| {norm(e["actual"])} | {e["reason"]} | {ev} |')
        R.append('')
    open(os.path.join(AUD, 'register', 'limits-register.md'), 'w', encoding='utf-8').write('\n'.join(R))
    print('README languages block:', len(md), 'lines; register:', len(E), 'entries')

if __name__ == '__main__':
    main()
