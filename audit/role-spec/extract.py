"""Freeze the Role Spec and rule inventory from tools/gen.py.
Usage: python audit/role-spec/extract.py <version>   -> audit/role-spec/v<version>.json + .md
Roles = gen.py syntax roles after syn_extra; rules are mapped back to roles by hex across all six flavours."""
import json, os, sys, runpy, tempfile, re, colorsys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ver = sys.argv[1] if len(sys.argv) > 1 else '1'
tmp = tempfile.mkdtemp()
sys.argv = ['gen.py', tmp]
g = runpy.run_path(os.path.join(ROOT, 'tools', 'gen.py'))
FL = list(g['ROLE'])
SYN = {n: g['syn_extra'](g['ROLE'][n][1], g['ROLE'][n][0]) for n in FL}
ROLES = sorted(set().union(*[set(s) for s in SYN.values()]))
themes = {n: json.load(open(os.path.join(tmp, 'themes', g['FILE'](n)), encoding='utf-8')) for n in FL}

def role_of(hexes):
    """roles whose hex equals the rule's colour in every flavour"""
    c = [r for r in ROLES if all(SYN[n].get(r, '').upper() == (hexes[n] or '').upper()[:7] for n in FL)]
    return c
def fg(v): return v if isinstance(v, str) else v.get('foreground')
def style(v):
    if isinstance(v, str): return ''
    if 'fontStyle' in v: return v['fontStyle']
    return ' '.join(k for k in ('bold', 'italic', 'underline', 'strikethrough') if v.get(k))

tm = []
for i, r in enumerate(themes[FL[0]]['tokenColors']):
    hexes = {n: themes[n]['tokenColors'][i]['settings'].get('foreground') for n in FL}
    sc = r['scope'] if isinstance(r['scope'], list) else [s.strip() for s in r['scope'].split(',')]
    tm.append(dict(idx=i, name=r.get('name', ''), scopes=sc, roles=role_of(hexes) if hexes[FL[0]] else ['(none)'],
                   style={n: themes[n]['tokenColors'][i]['settings'].get('fontStyle') for n in FL}))
sem = []
for k in themes[FL[0]]['semanticTokenColors']:
    hexes = {n: fg(themes[n]['semanticTokenColors'][k]) for n in FL}
    sem.append(dict(selector=k, roles=role_of(hexes) if hexes[FL[0]] else ['(none)'],
                    style={n: style(themes[n]['semanticTokenColors'][k]) for n in FL}))
# README meaning labels, from the Sea Salt table
readme = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read()
sec = readme.split('### Rosin · Sea Salt')[1].split('###')[0]
labels = {}
for m in re.finditer(r'^\|[^|]*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*`(#[0-9A-F]{6})`', sec, re.M):
    labels.setdefault(m.group(3), []).append((m.group(1), m.group(2)))
out = dict(version=ver, flavours=FL, roles={})
for r in ROLES:
    hx = {n: SYN[n].get(r) for n in FL}
    out['roles'][r] = dict(hex=hx, readme=labels.get((hx['Sea Salt'] or '').upper(), []),
                           tm_rules=[t['idx'] for t in tm if r in t['roles']],
                           sem_rules=[s['selector'] for s in sem if r in s['roles']])
out['tm_rules'] = tm; out['sem_rules'] = sem
p = os.path.join(ROOT, 'audit', 'role-spec', f'v{ver}.json')
json.dump(out, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
amb = [t for t in tm if len(t['roles']) != 1] + [s for s in sem if len(s['roles']) != 1]
print(f'{len(ROLES)} roles, {len(tm)} TextMate rules, {len(sem)} semantic rules; {len(amb)} rules map to 0 or >1 roles')
for a in amb: print('  AMBIGUOUS', a.get('name') or a.get('selector'), a['roles'])
for r in ROLES:
    o = out['roles'][r]
    print(f"{r:10} SS {o['hex']['Sea Salt']}  tm={len(o['tm_rules']):3} sem={len(o['sem_rules']):2}  README: {'; '.join(l for l,_ in o['readme']) or '-'}")
