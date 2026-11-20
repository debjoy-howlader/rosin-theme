// What-if / full-corpus diff: every token's final colour and style, baseline themes vs candidate themes,
// mode T (Pylance grammar excluded) and every mode S dump (all grammars). Lists every token that moved.
// usage: node diff.js <corpusDir> <baseThemesDir> <newThemesDir> <out.json>
'use strict';
const fs = require('fs'), path = require('path');
const { Harness, applySemantic, scanExtensions, readJSON } = require('./harness');
const sem = require('./semantic');
const [corpus, baseDir, newDir, out] = process.argv.slice(2);
const FL = ['Sea Salt', 'Black Cherry', 'Matcha', 'Espresso', 'Licorice', 'OLED'];
const fname = n => 'rosin-' + n.toLowerCase().replace(/ /g, '-') + '.json';
const load = d => Object.fromEntries(FL.map(n => [n, readJSON(path.join(d, fname(n)))]));
const B = load(baseDir), N = load(newDir);
for (const n of FL) { B[n].name = 'base ' + n; N[n].name = 'new ' + n; }
const EXT = [process.env.VSC_BUILTIN, path.join(process.env.HOME, 'mnt/test-code/rosin-audit-env/ext'), path.resolve(__dirname, '../..')];
const envT = scanExtensions(EXT, { exclude: ['ms-python.vscode-pylance', 'debjoy-howlader'] });
const envS = scanExtensions(EXT, { exclude: ['debjoy-howlader'] });
const DUMPS = ['cpptools', 'clangd', 'rust', 'servers'].map(d => path.resolve(__dirname, '../dumps', d));
(async () => {
  const hT = new Harness(envT), hS = new Harness(envS);
  const reg = sem.defaultRegistry(); sem.addContributions(reg, envS.semantic);
  const res = { B: Object.fromEntries(FL.map(n => [n, new sem.Resolver(B[n], reg)])), N: Object.fromEntries(FL.map(n => [n, new sem.Resolver(N[n], reg)])) };
  const files = []; (function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) { if (!/^(\.|sysroot|include|target)/.test(f)) walk(p); } else if (/^corpus\.|^Makefile$|^CMakeLists\.txt$|^Kconfig$|^COMMIT_EDITMSG$/.test(f) && !/\.anchors$/.test(f)) files.push(p); } })(corpus);
  const moved = []; let total = 0;
  const cmp = (rel, mode, fl, a, b) => {
    for (let i = 0; i < a.length; i++) {
      total++; const x = a[i], y = b[i];
      if (!y || x.start !== y.start) continue;
      if (x.fg !== y.fg || (x.style || '') !== (y.style || '')) moved.push({ file: rel, mode, flavour: fl, line: x.line + 1, col: x.start, text: x.text, before: `${x.fg} ${x.style || ''}`.trim(), after: `${y.fg} ${y.style || ''}`.trim(), scopes: x.scopes.slice(1).join(' '), semantic: x.semantic && `${x.semantic.type}.${x.semantic.modifiers.join('.')}` });
    }
  };
  for (const file of files) {
    const rel = path.relative(corpus, file).replace(/\\/g, '/');
    for (const fl of FL) {
      const tb = (await hT.tokenize(file, B[fl])).tokens, tn = (await hT.tokenize(file, N[fl])).tokens;
      cmp(rel, 'T', fl, tb, tn);
      const sb = (await hS.tokenize(file, B[fl])).tokens, sn = (await hS.tokenize(file, N[fl])).tokens;
      for (const d of DUMPS) {
        const df = path.join(d, rel.replace(/\//g, '__') + '.json'); if (!fs.existsSync(df)) continue;
        const dump = readJSON(df); if (!dump.tokens.length) continue;
        cmp(rel, 'S-' + path.basename(d), fl, applySemantic(sb, dump.tokens, res.B[fl], dump.languageId), applySemantic(sn, dump.tokens, res.N[fl], dump.languageId));
      }
    }
  }
  fs.writeFileSync(out, JSON.stringify({ total, moved }, null, 1));
  console.log('token-runs compared', total, 'moved', moved.length);
})().catch(e => { console.error(e); process.exit(1); });
