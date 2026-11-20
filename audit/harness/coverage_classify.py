"""Turn raw coverage into the protocol's numbers: per grammar (files of one grammar combined), reachable names produced,
and every name not produced either listed as missing or marked unreachable with a reason."""
import json, sys, collections, re
raw = json.load(open(sys.argv[1])); out = sys.argv[2]
OWN_SUFFIX = {'source.c': '.c', 'source.cpp': '.cpp', 'source.rust': '.rust', 'source.python': '.python', 'source.shell': '.shell',
  'source.makefile': '.makefile', 'source.cmake': '.cmake', 'source.json': '.json', 'source.json.comments': '.json', 'source.yaml': '.yaml',
  'source.toml': '.toml', 'source.ini': '.ini', 'text.log': '', 'source.diff': '.diff', 'text.git-commit': '', 'source.arm': '.arm',
  'source.ld': '.ld', 'source.dts': '.dts', 'source.kconfig': '.kconfig', 'text.html.markdown': '.markdown'}
FOREIGN = ('.arm', '.regexp', '.python', '.go', '.ruby.shell', '.js', '.diff')
by = collections.defaultdict(lambda: {'files': [], 'reach': set(), 'got': set()})
for f, v in raw['grammar'].items():
    g = by[v['grammar']]; g['files'].append(f)
    g['reach'] |= set(v['missing']) | set(['__produced__%d' % i for i in range(v['produced'])])  # placeholder, replaced below
# recompute exactly from missing lists: produced = reachable - missing ; union across files
by2 = {}
for f, v in raw['grammar'].items():
    g = by2.setdefault(v['grammar'], {'files': [], 'missing_sets': [], 'reachable': v['reachableNames']})
    g['files'].append(f); g['missing_sets'].append(set(v['missing']))
res = {}
for gname, g in by2.items():
    missing = set.intersection(*g['missing_sets'])
    suf = OWN_SUFFIX.get(gname, '')
    cls = {'missing': [], 'unreachable': collections.defaultdict(list)}
    for n in sorted(missing):
        if '.' not in n or ' ' in n: cls['unreachable']['grammar display name, not a scope'].append(n)
        elif n.startswith('invalid.'): cls['unreachable']['error markup for malformed code, styled by the Invalid rule'].append(n)
        elif gname != 'source.diff' and gname != 'text.git-commit' and any(n.endswith(s) for s in FOREIGN) and not n.endswith(suf or '\0'):
            cls['unreachable']['belongs to an embedded grammar, audited in that language'].append(n)
        elif n.startswith('meta.embedded.block.') and n.split('.')[3] not in ('c','cpp','rust','python','shellscript','makefile','cmake','json','jsonc','yaml','toml','ini','diff','log','git_commit','markdown'):
            cls['unreachable']['fenced block for a language outside the audited set'].append(n)
        elif 'mac-classic' in n or 'gtkdoc' in n: cls['unreachable']['legacy Mac/GTK conventions outside the embedded scope'].append(n)
        else: cls['missing'].append(n)
    unr = sum(len(v) for v in cls['unreachable'].values()); reach = g['reachable'] - unr
    prod = g['reachable'] - len(missing)
    res[gname] = {'files': g['files'], 'produced': prod, 'reachable': reach, 'pct': round(100 * prod / reach) if reach else 100,
                  'missing': cls['missing'], 'unreachable': cls['unreachable']}
json.dump({'grammar': res, 'legend': raw['legend']}, open(out, 'w'), indent=1)
for g, v in sorted(res.items(), key=lambda x: x[1]['pct']):
    print(f"{g:22} {v['produced']:4}/{v['reachable']:<4} {v['pct']:3}%  missing {len(v['missing'])}")
