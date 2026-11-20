"""Build the limits register from the final audit (A5 verdicts) + A4 findings + reviewed limits.
One entry per (file, component, mode) that is not EXACT. Every entry must get a reason; unassigned ones abort.
usage: python3 register.py <reportsDir> <out.json>"""
import json, sys, os, collections
R = sys.argv[1]; out = sys.argv[2]
rows = lambda p: [x for x in json.load(open(os.path.join(R, p))) if not x.get('summary') and not x.get('error')]
T, S = rows('A5-T.json'), rows('A5-S.json')
F = {(f['file'], f['component'], f['mode']): f for f in json.load(open(os.path.join(R, 'A4-findings.json')))}
RL = json.load(open(os.path.join(R, 'A4-reviewed-limits.json')))
REV = {}
for e in RL['entries']:
    for c in e['components']:
        for m in e['modes']: REV[(c, m)] = e
LIVE = {'python/corpus.py': 'S-Pylance', 'config/corpus.toml': 'S-EvenBetterTOML'}
SPLIT = json.load(open(os.path.join(R, '..', 'register', 'split-reviewed.json')))
OVR = json.load(open(os.path.join(R, '..', 'register', 'evidence-overrides.json')))
reg, missing = [], []
seen = set()
for src in (T, S):
    for x in src:
        for m, o in x['modes'].items():
            if o['v'] == 'EXACT': continue
            mode = m
            if m == 'S-servers':
                if x['file'] not in LIVE: continue          # no server for this file: identical to mode T
                mode = LIVE[x['file']]
            k = (x['file'], x['component'], mode)
            if k in seen: continue
            seen.add(k)
            e = dict(file=x['file'], lang=x['lang'], component=x['component'], token=x['token'], line=x['line'], mode=mode,
                     expect=x['expect']['role'], verdict=o['v'], actual=o.get('actual'), scopes=' '.join(o.get('scopes', [])[1:]))
            f = F.get((x['file'], x['component'], 'S-Pylance' if mode == 'S-Pylance' else mode))
            if o['v'] == 'FALLBACK':
                e.update(reason='NEEDS-SERVER', evidence=f"declared fallback: without a language server this shows as {o.get('actual')}")
            elif f and f['kind'] == 'limit':
                e.update(reason='SS' if f['cause'] == "grammar can't tell" else 'SV', evidence=f['proof'], computed=True)
            elif f and f['cause'] == 'split token':
                s = SPLIT.get(x['component'])
                if not s: missing.append(k); continue
                e.update(reason=s['reason'], evidence=s['evidence'])
            elif (x['component'], mode) in REV:
                r = REV[(x['component'], mode)]; e.update(reason=r['reason'], evidence=r['evidence'], cp=r['cp'])
            else:
                missing.append(k); continue
            if f"{x['component']}|{mode}" in OVR: e['evidence'] = OVR[f"{x['component']}|{mode}"]; e.pop('computed', None); e['override'] = True
            reg.append(e)
if missing:
    print('UNASSIGNED', len(missing)); [print(' ', m) for m in missing]; sys.exit(1)
json.dump(dict(reasons=dict(RL['reasons'], **{'NEEDS-SERVER': 'only a language server can tell this role; the grammar alone gives the declared fallback colour',
                                              'DESIGN': 'deliberate: a multi-part token is coloured part by part as the meaning table says (not a limit)',
                                              'SPLIT': 'the grammar splits the token into parts with different scopes; the parts are coloured as designed or the split itself is the limit'}),
               entries=reg), open(out, 'w'), indent=1)
print(len(reg), collections.Counter(e['reason'] for e in reg))
