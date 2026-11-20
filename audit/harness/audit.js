// Run the audit: markers -> observations -> verdicts, for mode T and any mode S dumps present.
// usage: node audit.js <corpusDir> <outJson> [--dumps <dir>]... [--ext-root <dir>]... [--themes <dir>] [--only <relfile>]
'use strict';
const fs = require('fs'), path = require('path');
const { Harness, applySemantic, rankRules, scanExtensions, readJSON } = require('./harness');
const sem = require('./semantic');

const args = process.argv.slice(2); const opt = { dumps: [], ext: [], only: [] };
const pos = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--dumps') opt.dumps.push(args[++i]); else if (args[i] === '--ext-root') opt.ext.push(args[++i]);
  else if (args[i] === '--themes') opt.themes = args[++i]; else if (args[i] === '--only') opt.only.push(args[++i]);
  else if (args[i] === '--spec') opt.spec = args[++i]; else if (args[i] === '--exclude-ext') (opt.excl ||= []).push(args[++i]); else pos.push(args[i]);
}
const [corpus, outFile] = pos;
const ROOT = path.resolve(__dirname, '..', '..');
const spec = readJSON(opt.spec || path.join(ROOT, 'audit/role-spec/v1.json'));
const FL = spec.flavours;
const themes = Object.fromEntries(FL.map(n => [n, readJSON(path.join(opt.themes || path.join(ROOT, 'themes'), 'rosin-' + n.toLowerCase().replace(/ /g, '-') + '.json'))]));
const roleHex = (role, fl) => (spec.roles[role] && spec.roles[role].hex[fl] || '').toUpperCase();
const rolesOf = (hex, fl) => Object.keys(spec.roles).filter(r => roleHex(r, fl) === (hex || '').toUpperCase());

const MARK = /^\s*(?:\/\/|#|--|;|%|<!--|\/\*)\s*@\s+(\S+)\s+(\S+)\s+(\S+)/;
function parseMarkers(lines) {
  const out = []; let pending = [];
  lines.forEach((l, i) => {
    const m = l.match(MARK);
    if (m) { pending.push({ component: m[1], expect: m[2], token: m[3], markerLine: i }); return; }
    if (pending.length && l.trim() !== '') { for (const p of pending) out.push({ ...p, line: i }); pending = []; }
  });
  return out;
}
function parseExpect(e) { // role[?Qn][/T:role]
  const [main, t] = e.split('/T:'); const [role, q] = main.split('?');
  return { role, question: q || null, fallbackT: t || null };
}
function locate(lines, mk) {
  let [tok, nth] = mk.token.split(/#(?=\d+$)/); nth = +(nth || 1);
  const text = lines[mk.line]; let idx = -1, from = 0;
  const raw = tok.startsWith('~'); if (raw) tok = tok.slice(1);
  const word = !raw && /^\w+$/.test(tok);
  for (let k = 0; k < nth; k++) {
    if (word) { const re = new RegExp('(?<![A-Za-z_0-9])' + tok + '(?![A-Za-z_0-9])', 'g'); re.lastIndex = from; const m = re.exec(text); idx = m ? m.index : -1; }
    else idx = text.indexOf(tok, from);
    if (idx < 0) break; from = idx + 1; }
  return idx < 0 ? null : { start: idx, end: idx + tok.length, text: tok };
}
function observe(tokens, line, span) {
  const parts = tokens.filter(t => t.line === line && t.start < span.end && t.end > span.start);
  const fgs = [...new Set(parts.map(p => p.fg))], styles = [...new Set(parts.map(p => p.style || ''))];
  return { fg: fgs.length === 1 ? fgs[0] : fgs.join('+'), style: styles.join('+'), mixed: fgs.length > 1 || styles.length > 1, parts };
}
function verdict(ex, obsByFl, mode) {
  const want = mode === 'T' && ex.fallbackT ? [ex.role, ex.fallbackT] : [ex.role];
  const per = {};
  for (const fl of FL) {
    const o = obsByFl[fl]; const roles = rolesOf(o.fg, fl);
    per[fl] = roles;
  }
  const hit = r => FL.every(fl => per[fl].includes(r));
  if (hit(ex.role)) return { v: 'EXACT', actual: ex.role };
  if (mode === 'T' && ex.fallbackT && hit(ex.fallbackT)) return { v: 'FALLBACK', actual: ex.fallbackT };
  // which single role explains all flavours?
  const cand = Object.keys(spec.roles).filter(hit);
  const plain = FL.every(fl => (obsByFl[fl].fg || '') === (themes[fl].colors['editor.foreground'] || '').toUpperCase().slice(0, 7));
  if (plain && ex.role !== 'variable') return { v: 'PLAIN', actual: 'variable' };
  return { v: 'WRONG', actual: cand.length ? cand.join('|') : 'unmapped:' + obsByFl['Sea Salt'].fg };
}

(async () => {
  const env = scanExtensions([path.join(process.env.VSC_BUILTIN), ...opt.ext], { exclude: opt.excl || [] });
  const h = new Harness(env);
  const reg = sem.defaultRegistry(); sem.addContributions(reg, env.semantic);
  const resolvers = Object.fromEntries(FL.map(n => [n, new sem.Resolver(themes[n], reg)]));
  const files = []; (function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) { if (!/^(\.|sysroot|include|target)/.test(f)) walk(p); } else if ((/^corpus\.|^Makefile$|^CMakeLists\.txt$|^Kconfig$|^COMMIT_EDITMSG$/.test(f)) && !/\.anchors$/.test(f)) files.push(p); } })(corpus);
  const results = [];
  for (const file of files) {
    const rel = path.relative(corpus, file).replace(/\\/g, '/');
    if (opt.only.length && !opt.only.includes(rel)) continue;
    const tm = {}; let lines, info;
    try { for (const fl of FL) { const r = await h.tokenize(file, themes[fl]); tm[fl] = r.tokens; lines = r.lines; info = r; } } catch (e) { results.push({ file: rel, summary: true, error: String(e.message) }); continue; }
    let markers = parseMarkers(lines);
    if (fs.existsSync(file + '.anchors')) for (const l of fs.readFileSync(file + '.anchors', 'utf8').split(/\r?\n/)) {
      const m = l.match(/^\s*@\s+(\S+)\s+(\S+)\s+(\S+)\s+L(\d+)/); if (m) markers.push({ component: m[1], expect: m[2], token: m[3], line: +m[4] - 1 });
    }
    const modes = { T: tm };
    for (const d of opt.dumps) {
      const dumpFile = path.join(d, rel.replace(/\//g, '__') + '.json');
      if (!fs.existsSync(dumpFile)) continue;
      const dump = readJSON(dumpFile); const label = 'S-' + path.basename(d);
      modes[label] = Object.fromEntries(FL.map(fl => [fl, applySemantic(tm[fl], dump.tokens, resolvers[fl], dump.languageId)]));
      modes[label]._legend = dump.legend; modes[label]._diags = dump.diagnostics; modes[label]._count = dump.tokens.length;
    }
    for (const mk of markers) {
      const ex = parseExpect(mk.expect); const span = locate(lines, mk);
      const row = { file: rel, lang: info.lang, component: mk.component, token: mk.token, line: mk.line + 1, expect: ex, modes: {} };
      if (!span) { row.error = 'token not found on target line'; results.push(row); continue; }
      for (const [mode, byFl] of Object.entries(modes)) {
        const obs = Object.fromEntries(FL.map(fl => [fl, observe(byFl[fl], mk.line, span)]));
        const p0 = obs['Sea Salt'].parts[0] || {};
        const vd = verdict(ex, obs, mode === 'T' ? 'T' : 'S');
        row.modes[mode] = { ...vd, fg: obs['Sea Salt'].fg, style: obs['Sea Salt'].style, mixed: obs['Sea Salt'].mixed,
          scopes: p0.scopes, semantic: p0.semantic ? { type: p0.semantic.type, modifiers: p0.semantic.modifiers, fgFrom: p0.semantic.src.foreground } : undefined,
          rules: mode === 'T' && p0.scopes ? rankRules(themes['Sea Salt'], p0.scopes).slice(0, 3).map(r => r.name + ' ' + r.fg) : undefined,
          byFlavour: Object.fromEntries(FL.map(fl => [fl, obs[fl].fg + (obs[fl].style ? ' ' + obs[fl].style : '')])) };
      }
      results.push(row);
    }
    results.push({ file: rel, summary: true, modes: Object.fromEntries(Object.entries(modes).map(([m, v]) => [m, { tokens: v._count, diags: v._diags && v._diags.length }])) });
  }
  fs.writeFileSync(outFile, JSON.stringify(results, null, 1));
  // console summary
  for (const r of results) {
    if (r.summary) { console.log('##', r.file, JSON.stringify(r.modes)); continue; }
    if (r.error) { console.log('!!', r.component, r.token, r.error); continue; }
    const cells = Object.entries(r.modes).map(([m, o]) => `${m}:${o.v}${o.v === 'EXACT' ? '' : '(' + o.actual + ')'}${o.mixed ? '*' : ''} ${o.fg} ${o.style || ''}`.trim());
    console.log(r.component.padEnd(26), JSON.stringify(r.token).padEnd(14), (r.expect.role + (r.expect.question ? '?' + r.expect.question : '')).padEnd(14), cells.join(' | '));
  }
})().catch(e => { console.error(e); process.exit(1); });
