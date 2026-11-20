import json, sys, collections
F = json.load(open(sys.argv[1])); out = sys.argv[2]
g = collections.defaultdict(list)
for f in F:
    if f['kind'] != 'limit': continue
    g[(f['mode'], f['file'].split('/')[0], f['cause'], f['proof'].split('(expected')[0])].append(f)
L = ['# A1 appendix: limits with proof', '', 'Computed proof: the component has exactly the same scope stack (grammar) or semantic type and modifiers (server) '
     'as a component with a different expected role, so no theme rule can colour both correctly.', '',
     '| Mode | Lang | Cause | Components | Shares its tokens with |', '|---|---|---|---|---|']
for (mode, lang, cause, proof), fs in sorted(g.items()):
    comps = ', '.join(f"`{f['component']}` ({f['expect']}→{f['actual']})" for f in fs[:5]) + (f' +{len(fs) - 5}' if len(fs) > 5 else '')
    L.append(f"| {mode.replace('S-', 'S ')} | {lang} | {cause} | {comps} | {proof.replace('same scope stack as ', '').replace('same semantic type and modifiers as ', '')} |")
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n'); print(len(g), 'limit groups')
