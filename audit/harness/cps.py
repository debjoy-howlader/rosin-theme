"""Group fixable findings into change proposals: one CP per (mode family, language, distinguishing selector, expected role).
The selector is the innermost scope (mode T) or the semantic type+modifiers (mode S)."""
import json, sys, collections
F = json.load(open(sys.argv[1])); out_json, out_md = sys.argv[2], sys.argv[3]
SEV = lambda n, ex: 1 if n >= 3 else (2 if ex in ('hazard', 'keyword', 'function', 'composite', 'prim') else 3)
g = collections.defaultdict(list)
for f in F:
    if f['kind'] != 'fix' or f['cause'] == 'split token': continue
    fam = 'T' if (f['mode'] == 'T' or not f['semantic']) else 'S'
    if fam == 'S' and f['semantic']: sel = 'semantic ' + f['semantic']
    else: sel = (f['scopes'].split() or ['(no scope)'])[-1]
    g[(fam, f['file'].split('/')[0], sel, f['expect'])].append(f)
cps = []
for i, ((fam, lang, sel, ex), fs) in enumerate(sorted(g.items(), key=lambda kv: (-len(kv[1]), kv[0])), 1):
    actual = collections.Counter(f['actual'] for f in fs).most_common(1)[0][0]
    cps.append(dict(id=f'CP-{__import__("os").environ.get("CP_PASS","A1")}-{i:03d}', mode=fam, lang=lang, selector=sel, expect=ex, now=actual, n=len({f['component'] for f in fs}), sev=SEV(len({f['component'] for f in fs}), ex),
                    cause=collections.Counter(f['cause'] for f in fs).most_common(1)[0][0], kind='fix',
                    components=sorted({f['component'] for f in fs}), modes=sorted({f['mode'] for f in fs})))
json.dump(cps, open(out_json, 'w'), indent=1)
L = ['# '+__import__('os').environ.get('CP_PASS','A1')+' appendix: change proposals', '', 'One proposal per distinguishing selector. Each needs its what-if run (predicted moves) at the start of the edit phase; '
     'the selector shown is the evidence, the final rule may be narrower (language suffix, parent scope).', '',
     '| CP | Sev | Mode | Lang | Selector | Now | Should be | Components |', '|---|---|---|---|---|---|---|---|']
for c in cps:
    comps = ', '.join(f'`{x}`' for x in c['components'][:6]) + (f' +{len(c["components"]) - 6}' if len(c['components']) > 6 else '')
    L.append(f"| {c['id']} | {c['sev']} | {'/'.join(m.replace('S-', '') for m in c['modes'])} | {c['lang']} | `{c['selector']}` | {c['now']} | {c['expect']} | {comps} |")
open(out_md, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(len(cps), 'CPs;', collections.Counter(c['sev'] for c in cps))
