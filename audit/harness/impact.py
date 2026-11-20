"""Impact set for an edit phase: components the next audit must confirm, each with the reason it is in the set."""
import json, sys, re, collections
T = json.load(open(sys.argv[1])); S = json.load(open(sys.argv[2])); D = json.load(open(sys.argv[3])); CPS = json.load(open(sys.argv[4]))
edited_rules = set(sys.argv[6].split('|')); edited_sem = set(sys.argv[7].split('|')); out = sys.argv[5]
rows = lambda X: [x for x in X if not x.get('summary') and not x.get('error')]
imp = collections.defaultdict(set)
# moved tokens -> components whose marker covers them
moved = collections.defaultdict(list)
for m in D['moved']: moved[(m['file'], m['line'])].append(m)
for x in rows(T):
    k = (x['file'], x['component'])
    if any(True for _ in moved.get((x['file'], x['line']), [])):
        # the marker's token covers a moved run?
        tok = x['token'].lstrip('~').split('#')[0]
        if any(tok and (tok in mm['text'] or mm['text'].strip() in tok) and mm['text'].strip() for mm in moved[(x['file'], x['line'])]): imp[k].add('colour or style moved in the what-if')
    rules = [r.rsplit(' #', 1)[0] for r in (x['modes']['T'].get('rules') or [])]
    if rules and rules[0] in edited_rules: imp[k].add('winning rule edited: ' + rules[0])
    if any(r in edited_rules for r in rules[1:]): imp[k].add('coupled: an edited rule is a runner-up')
for x in rows(S):
    for m, o in x['modes'].items():
        sem = o.get('semantic')
        if sem and sem.get('fgFrom') and (sem['fgFrom'].get('sel') in edited_sem or sem['type'] in edited_sem or any(s.split('.')[-1] in sem['modifiers'] for s in edited_sem if s.startswith('*.'))):
            imp[(x['file'], x['component'])].add('semantic rule edited: ' + str(sem['type']))
for c in CPS:
    for comp in c['components']:
        for x in rows(T):
            if x['component'] == comp: imp[(x['file'], comp)].add('CP target ' + c['id'])
json.dump([{'file': f, 'component': c, 'reasons': sorted(r)} for (f, c), r in sorted(imp.items())], open(out, 'w'), indent=1)
print(len(imp), 'components in the impact set')
