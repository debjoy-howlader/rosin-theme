// Coverage: (1) grammar scope names reachable from each corpus file's grammar vs scopes the corpus produced,
// (2) server legend token types vs types present in the dumps.
'use strict';
const fs = require('fs'), path = require('path');
const { Harness, scanExtensions, readJSON } = require('./harness');
const vsctm = require(path.join(process.env.VSC_MODULES || path.join(process.env.HOME, 'w/h/vsc_modules'), 'vscode-textmate'));
const [corpus, out, ...rest] = process.argv.slice(2);
const roots = [process.env.VSC_BUILTIN, ...rest.filter(a => !a.startsWith('--'))];
const env = scanExtensions(roots, { exclude: ['ms-python.vscode-pylance', 'debjoy-howlader'] });
function names(scope, seen = new Set(), acc = new Set(), root = scope) {
  // Only rules reachable from the grammar's top-level patterns through includes count (dead repository entries don't).
  if (seen.has(scope) || !env.grammars[scope]) return acc; seen.add(scope);
  const g = vsctm.parseRawGrammar(fs.readFileSync(env.grammars[scope].path, 'utf8'), env.grammars[scope].path);
  const repo = g.repository || {}; const visitedRepo = new Set();
  const addName = v => { if (typeof v === 'string' && !v.includes('$')) v.split(/\s+/).forEach(n => n && acc.add(n)); };
  function rule(r, localRepo) {
    if (!r || typeof r !== 'object') return;
    addName(r.name); addName(r.contentName);
    for (const capKey of ['captures', 'beginCaptures', 'endCaptures', 'whileCaptures'])
      if (r[capKey]) for (const c of Object.values(r[capKey])) rule(c, localRepo);
    const lr = r.repository ? { ...localRepo, ...r.repository } : localRepo;
    for (const p of r.patterns || []) {
      if (p.include) {
        const inc = p.include;
        if (inc === '$self' || inc === '$base') continue;
        if (inc.startsWith('#')) { const k = inc.slice(1); if (!visitedRepo.has(k) && lr[k]) { visitedRepo.add(k); rule(lr[k], lr); } }
        else { const sc = inc.split('#')[0]; if (sc.startsWith(root)) names(sc, seen, acc, root); }
      } else rule(p, lr);
    }
  }
  rule({ patterns: g.patterns, repository: repo }, repo);
  if (g.injections) for (const r of Object.values(g.injections)) rule(r, repo);
  for (const inj of env.injections[scope] || []) if (inj.startsWith('rosin.')) names(inj, seen, acc, inj);
  return acc;
}
(async () => {
  const h = new Harness(env); const theme = readJSON(path.resolve(__dirname, '../../themes/rosin-sea-salt.json'));
  const files = []; (function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) { if (!/^(\.|sysroot|include|target)/.test(f)) walk(p); } else if (/^corpus\.|^Makefile$|^CMakeLists\.txt$|^Kconfig$|^COMMIT_EDITMSG$/.test(f) && !/\.anchors$/.test(f)) files.push(p); } })(corpus);
  const res = {};
  for (const f of files) {
    const r = await h.tokenize(f, theme); const own = names(r.scope);
    const seen = new Set(r.tokens.flatMap(t => t.scopes));
    const hit = [...own].filter(n => seen.has(n));
    res[path.relative(corpus, f)] = { grammar: r.scope, reachableNames: own.size, produced: hit.length, pct: own.size ? Math.round(100 * hit.length / own.size) : 100, missing: [...own].filter(n => !seen.has(n)).sort() };
  }
  // legend coverage
  const dumps = path.resolve(__dirname, '../dumps'); const leg = {};
  for (const d of ['cpptools', 'clangd', 'rust', 'servers']) for (const f of fs.readdirSync(path.join(dumps, d)).filter(x => x.endsWith('.json') && !x.startsWith('_'))) {
    const j = readJSON(path.join(dumps, d, f)); if (!j.legend || !j.tokens.length) continue;
    const k = d + ':' + j.languageId; const L = leg[k] ||= { types: j.legend.tokenTypes, mods: j.legend.tokenModifiers, seenT: new Set(), seenM: new Set() };
    j.tokens.forEach(t => { L.seenT.add(t.type); t.modifiers.forEach(m => L.seenM.add(m)); });
  }
  const legOut = Object.fromEntries(Object.entries(leg).map(([k, L]) => [k, { types: `${L.seenT.size}/${new Set(L.types).size}`, mods: `${L.seenM.size}/${new Set(L.mods).size}`, missingTypes: [...new Set(L.types)].filter(t => !L.seenT.has(t)) }]));
  fs.writeFileSync(out, JSON.stringify({ grammar: res, legend: legOut }, null, 1));
  for (const [f, v] of Object.entries(res)) console.log(f.padEnd(26), v.grammar.padEnd(16), `${v.produced}/${v.reachableNames} scope names (${v.pct}%)`);
  for (const [k, v] of Object.entries(legOut)) console.log(k.padEnd(22), 'types', v.types, 'mods', v.mods);
})().catch(e => { console.error(e); process.exit(1); });
