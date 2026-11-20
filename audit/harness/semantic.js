// Port of VS Code's semantic token styling (commit 8a14f0cc1b):
//  platform/theme/common/tokenClassificationRegistry.ts  (types, defaults, parseTokenSelector.match)
//  workbench/services/themes/common/colorThemeData.ts    (getTokenStyle, resolveScopes, nameMatcher, getScopeMatcher)
//  workbench/services/themes/common/textMateScopeMatcher.ts (createMatchers)
'use strict';

// ---------- textMateScopeMatcher.ts (verbatim logic) ----------
function createMatchers(selector, matchesName, results) {
  const tokenizer = newTokenizer(selector);
  let token = tokenizer.next();
  while (token !== null) {
    let priority = 0;
    if (token.length === 2 && token.charAt(1) === ':') { priority = token.charAt(0) === 'R' ? 1 : -1; token = tokenizer.next(); }
    const matcher = parseConjunction();
    if (matcher) results.push({ matcher, priority });
    if (token !== ',') break;
    token = tokenizer.next();
  }
  function parseOperand() {
    if (token === '-') { token = tokenizer.next(); const e = parseOperand(); if (!e) return null; return i => (e(i) < 0 ? 0 : -1); }
    if (token === '(') { token = tokenizer.next(); const e = parseInnerExpression(); if (token === ')') token = tokenizer.next(); return e; }
    if (isIdentifier(token)) { const ids = []; do { ids.push(token); token = tokenizer.next(); } while (isIdentifier(token)); return i => matchesName(ids, i); }
    return null;
  }
  function parseConjunction() {
    let m = parseOperand(); if (!m) return null; const ms = [];
    while (m) { ms.push(m); m = parseOperand(); }
    return i => { let min = ms[0](i); for (let k = 1; min >= 0 && k < ms.length; k++) min = Math.min(min, ms[k](i)); return min; };
  }
  function parseInnerExpression() {
    let m = parseConjunction(); if (!m) return null; const ms = [];
    while (m) { ms.push(m); if (token === '|' || token === ',') { do { token = tokenizer.next(); } while (token === '|' || token === ','); } else break; m = parseConjunction(); }
    return i => { let max = ms[0](i); for (let k = 1; k < ms.length; k++) max = Math.max(max, ms[k](i)); return max; };
  }
}
function isIdentifier(t) { return !!t && !!t.match(/[\w\.:]+/); }
function newTokenizer(input) { const re = /([LR]:|[\w\.:][\w\.:\-]*|[\,\|\-\(\)])/g; let m = re.exec(input); return { next: () => { if (!m) return null; const r = m[0]; m = re.exec(input); return r; } }; }

// ---------- colorThemeData.ts ----------
function scopesAreMatching(a, b) { if (!a) return false; if (a === b) return true; const n = b.length; return a.length > n && a.substr(0, n) === b && a[n] === '.'; }
function nameMatcher(ids, scopes) {
  if (scopes.length < ids.length) return -1;
  let score;
  const every = ids.every(id => { for (let i = scopes.length - 1; i >= 0; i--) if (scopesAreMatching(scopes[i], id)) { score = (i + 1) * 0x10000 + id.length; return true; } return false; });
  return every && score !== undefined ? score : -1;
}
function getScopeMatcher(rule) {
  const rs = rule.scope; if (!rs || !rule.settings) return () => -1;
  const ms = []; (Array.isArray(rs) ? rs : [rs]).forEach(s => createMatchers(s, nameMatcher, ms));
  if (!ms.length) return () => -1;
  return scope => { let max = ms[0].matcher(scope); for (let i = 1; i < ms.length; i++) max = Math.max(max, ms[i].matcher(scope)); return max; };
}

// ---------- tokenClassificationRegistry.ts ----------
class Registry {
  constructor() { this.types = {}; this.defaults = []; }
  registerTokenType(id, superType) { this.types[id] = { id, superType }; }
  hierarchy(t) { const h = [t]; let x = this.types[t]; while (x && x.superType) { h.push(x.superType); x = this.types[x.superType]; } return h; }
  parseSelector(str, language) {
    let [s, lang] = str.split(':'); if (lang === undefined) lang = language;
    const parts = s.split('.'); const type = parts[0], modifiers = parts.slice(1);
    if (!type) return { match: () => -1, id: '$invalid' };
    return {
      str, match: (t, mods, l) => {
        let score = 0;
        if (lang !== undefined) { if (lang !== l) return -1; score += 10; }
        if (type !== '*') { const lv = this.hierarchy(t).indexOf(type); if (lv === -1) return -1; score += 100 - lv; }
        for (const m of modifiers) if (mods.indexOf(m) === -1) return -1;
        return score + modifiers.length * 100;
      }
    };
  }
  registerDefault(sel, scopesToProbe, source) { this.defaults.push({ selector: this.parseSelector(sel.split(':')[0], sel.split(':')[1]), scopesToProbe, source }); }
}
function defaultRegistry() {
  const r = new Registry();
  const T = (id, probe = [], sup) => { r.registerTokenType(id, sup); if (probe) r.registerDefault(id, probe, 'vscode'); };
  T('comment', [['comment']]); T('string', [['string']]); T('keyword', [['keyword.control']]); T('number', [['constant.numeric']]);
  T('regexp', [['constant.regexp']]); T('operator', [['keyword.operator']]); T('namespace', [['entity.name.namespace']]);
  T('type', [['entity.name.type'], ['support.type']]); T('struct', [['entity.name.type.struct']]); T('class', [['entity.name.type.class'], ['support.class']]);
  T('interface', [['entity.name.type.interface']]); T('enum', [['entity.name.type.enum']]); T('typeParameter', [['entity.name.type.parameter']]);
  T('function', [['entity.name.function'], ['support.function']]); T('member', [], 'method'); T('method', [['entity.name.function.member'], ['support.function']]);
  T('macro', [['entity.name.function.preprocessor']]); T('variable', [['variable.other.readwrite'], ['entity.name.variable']]);
  T('parameter', [['variable.parameter']]); T('property', [['variable.other.property']]); T('enumMember', [['variable.other.enummember']]);
  T('event', [['variable.other.event']]); T('decorator', [['entity.name.decorator'], ['entity.name.function']]); r.registerTokenType('label');
  const D = (s, p) => r.registerDefault(s, p, 'vscode');
  D('variable.readonly', [['variable.other.constant']]); D('property.readonly', [['variable.other.constant.property']]);
  D('type.defaultLibrary', [['support.type']]); D('class.defaultLibrary', [['support.class']]); D('interface.defaultLibrary', [['support.class']]);
  D('variable.defaultLibrary', [['support.variable'], ['support.other.variable']]); D('variable.defaultLibrary.readonly', [['support.constant']]);
  D('property.defaultLibrary', [['support.variable.property']]); D('property.defaultLibrary.readonly', [['support.constant.property']]);
  D('function.defaultLibrary', [['support.function']]); D('member.defaultLibrary', [['support.function']]);
  return r;
}
/** add extension contributions (tokenClassificationExtensionPoint.ts) */
function addContributions(r, sem) {
  for (const t of sem.types) r.registerTokenType(t.id, t.superType);
  for (const s of sem.scopes) for (const [sel, scopes] of Object.entries(s.scopes || {}))
    r.defaults.push({ selector: r.parseSelector(sel, s.language), scopesToProbe: scopes.map(x => x.split(' ')), source: s.ext });
}

/** Theme wrapper: TextMate rules as VS Code builds them (default rule first, dark default tokens appended). */
function themeRules(theme) {
  const out = [{ settings: { foreground: theme.colors['editor.foreground'], background: theme.colors['editor.background'] } }];
  let info = false;
  for (const r of theme.tokenColors) if (r.scope && r.settings) { if (r.scope === 'token.info-token') info = true; out.push({ scope: r.scope, settings: r.settings, name: r.name }); }
  if (!info) [['token.info-token', '#6796e6'], ['token.warn-token', '#cd9731'], ['token.error-token', '#f44747'], ['token.debug-token', '#b267e6']]
    .forEach(([s, f]) => out.push({ scope: s, settings: { foreground: f }, name: '(VS Code dark default)' }));
  return out;
}
function semanticRules(theme, r) {
  const out = [];
  for (const [sel, v] of Object.entries(theme.semanticTokenColors || {})) {
    let st;
    if (typeof v === 'string') st = { foreground: v };
    else if (v && typeof v === 'object') {
      st = { foreground: v.foreground };
      if (typeof v.fontStyle === 'string') { for (const p of ['bold', 'italic', 'underline', 'strikethrough']) st[p] = v.fontStyle.includes(p); }
      for (const p of ['bold', 'italic', 'underline', 'strikethrough']) if (v[p] !== undefined) st[p] = v[p];
    }
    if (st) out.push({ selector: r.parseSelector(sel), style: st, sel });
  }
  return out;
}
function fontStyleToProps(fs) { if (typeof fs !== 'string') return {}; const o = {}; for (const p of ['bold', 'italic', 'underline', 'strikethrough']) o[p] = fs.includes(p); return o; }

class Resolver {
  constructor(theme, r) {
    this.r = r; this.tm = themeRules(theme).slice(1); this.tmMatchers = this.tm.map(getScopeMatcher); this.sem = semanticRules(theme, r);
  }
  // calibration A1-2: VS Code keeps the grammar's font style when the scope-map rule's fontStyle is an empty string
  resolveScopes(scopes) {
    for (const scope of scopes) {
      let fg, fs, fgS = -1, fsS = -1, fgRule, fsRule;
      for (let i = 0; i < this.tmMatchers.length; i++) {
        const s = this.tmMatchers[i](scope);
        if (s >= 0) { const st = this.tm[i].settings;
          if (s >= fgS && st.foreground) { fg = st.foreground; fgS = s; fgRule = this.tm[i]; }
          if (s >= fsS && typeof st.fontStyle === 'string' && st.fontStyle !== '') { fs = st.fontStyle; fsS = s; fsRule = this.tm[i]; } }
      }
      if (fg !== undefined || fs !== undefined) return { style: { foreground: fg, ...fontStyleToProps(fs) }, fgRule, fsRule, scope };
    }
    return undefined;
  }
  /** returns {style, sources} exactly as getTokenStyle, plus which rule supplied each property */
  tokenStyle(type, modifiers, language) {
    const res = {}, score = { foreground: -1, bold: -1, underline: -1, strikethrough: -1, italic: -1 }, src = {};
    const proc = (ms, style, def) => {
      if (style.foreground && score.foreground <= ms) { score.foreground = ms; res.foreground = style.foreground; src.foreground = def; }
      for (const p of ['bold', 'underline', 'strikethrough', 'italic']) if (style[p] !== undefined && score[p] <= ms) { score[p] = ms; res[p] = style[p]; src[p] = def; }
    };
    for (const rule of this.sem) { const ms = rule.selector.match(type, modifiers, language); if (ms >= 0) proc(ms, rule.style, { kind: 'semanticTokenColors', sel: rule.sel, score: ms }); }
    let undef = false; for (const k in score) { if (score[k] === -1) undef = true; else score[k] = Number.MAX_VALUE; }
    if (undef) for (const d of this.r.defaults) {
      const ms = d.selector.match(type, modifiers, language);
      if (ms >= 0 && d.scopesToProbe) { const st = this.resolveScopes(d.scopesToProbe);
        if (st) proc(ms, st.style, { kind: 'scopeMap', sel: d.selector.str, by: d.source, probe: st.scope.join(' '), rule: st.fgRule && (st.fgRule.name || JSON.stringify(st.fgRule.scope)), score: ms }); }
    }
    return { style: res, src };
  }
}
module.exports = { defaultRegistry, addContributions, Resolver, themeRules, getScopeMatcher, nameMatcher };
