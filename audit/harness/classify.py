"""Classify every non-EXACT result (protocol §Classifying findings).
Limit proof, computed: another component of a different expected role has the identical scope stack (mode T)
or the identical semantic type+modifiers with the same grammar stack (mode S). Otherwise the case is fixable by a rule."""
import json, sys, collections
T = json.load(open(sys.argv[1])); S = json.load(open(sys.argv[2])); out = sys.argv[3]
LIVE = {'python/corpus.py': 'S-Pylance', 'config/corpus.toml': 'S-EvenBetterTOML'}
def rows(data):
    return [x for x in data if not x.get('summary') and not x.get('error')]
def lang(f): return f.split('/')[0] if not f.startswith('config') else f.split('.')[-1]
recs = []
for x in rows(T):
    o = x['modes']['T']; recs.append(dict(x=x, mode='T', o=o))
for x in rows(S):
    for m, o in x['modes'].items():
        if m == 'T': continue
        if m == 'S-servers':
            if x['file'] not in LIVE: continue
            m = LIVE[x['file']]
        recs.append(dict(x=x, mode=m, o=o))
def key(r):
    o = r['o']; sc = tuple((o.get('scopes') or [])[1:])
    if r['mode'] == 'T': return (r['mode'], r['x']['file'].split('/')[0], sc)
    sem = o.get('semantic'); s = (sem['type'], tuple(sorted(sem['modifiers']))) if sem else None
    return (r['mode'], r['x']['file'].split('/')[0], s if s else ('tm',) + sc)
groups = collections.defaultdict(list)
for r in recs: groups[key(r)].append(r)
findings = []
for r in recs:
    o = r['o']; ex = r['x']['expect']
    if o['v'] in ('EXACT', 'FALLBACK'): continue
    k = key(r); peers = [p for p in groups[k] if p['x']['expect']['role'] != ex['role'] and p is not r]
    if o.get('mixed'):
        cause = 'split token'; kind = 'fix'; proof = 'grammar splits the token into pieces with different colours'
    elif peers:
        cause = 'grammar can\'t tell' if r['mode'] == 'T' or not o.get('semantic') else 'server can\'t tell'
        kind = 'limit'; p = peers[0]['x']
        proof = f"same {'scope stack' if cause.startswith('grammar') else 'semantic type and modifiers'} as `{p['component']}` (expected {p['expect']['role']})"
    else:
        kind = 'fix'
        if r['mode'] != 'T' and o.get('semantic'):
            src = (o['semantic'].get('fgFrom') or {}); cause = 'semantic rule missing or wrong' ; proof = f"semantic {o['semantic']['type']}.{'.'.join(o['semantic']['modifiers'])} styled via {src.get('kind')}:{src.get('sel')}"
        elif o['v'] == 'PLAIN':
            cause = 'missing rule'; proof = 'scope stack is unique to this component but no Rosin rule matches it'
        else:
            cause = 'rule too broad or rule loses'; proof = 'winning rule: ' + ((o.get('rules') or ['?'])[0])
    findings.append(dict(file=r['x']['file'], component=r['x']['component'], token=r['x']['token'], mode=r['mode'], expect=ex['role'],
                         verdict=o['v'], actual=o['actual'], style=o['style'], kind=kind, cause=cause, proof=proof,
                         scopes=' '.join((o.get('scopes') or [])[1:]), semantic=o.get('semantic') and f"{o['semantic']['type']}.{'.'.join(o['semantic']['modifiers'])}"))
json.dump(findings, open(out, 'w'), indent=1)
c = collections.Counter((f['mode'] if f['mode'] == 'T' else 'S', f['kind'], f['cause']) for f in findings)
for k, v in sorted(c.items()): print(k, v)
print('total non-EXACT', len(findings))
