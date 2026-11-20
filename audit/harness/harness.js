// Rosin audit harness: resolves the final colour and font style of every token in a corpus file,
// in mode T (TextMate only, via vscode-textmate's tokenizeLine2 exactly as VS Code does) and
// mode S (semantic tokens from a probe dump, resolved by the port in semantic.js, layered on mode T).
'use strict';
const fs = require('fs'), path = require('path');
const MODS = process.env.VSC_MODULES || path.join(process.env.HOME, 'w/h/vsc_modules');
const vsctm = require(path.join(MODS, 'vscode-textmate'));
const onig = require(path.join(MODS, 'vscode-oniguruma'));
const { scanExtensions, languageOf, readJSON } = require('./vscode-env');
const sem = require('./semantic');

let onigLib;
async function onigLoad() {
  if (!onigLib) {
    const wasm = fs.readFileSync(path.join(MODS, 'vscode-oniguruma/release/onig.wasm')).buffer;
    await onig.loadWASM(wasm);
    onigLib = { createOnigScanner: s => new onig.OnigScanner(s), createOnigString: s => new onig.OnigString(s) };
  }
  return onigLib;
}

const FS = { 1: 'italic', 2: 'bold', 4: 'underline', 8: 'strikethrough' };
function decodeStyle(n) { return Object.entries(FS).filter(([b]) => n & +b).map(([, s]) => s).sort().join(' '); }

class Harness {
  constructor(env) { this.env = env; this.registries = {}; }
  async registry(theme) {
    // One registry per harness (grammars compile once); the theme is swapped with setTheme, as VS Code does on a theme change.
    const env = this.env;
    if (!this.R) {
      const reg = new vsctm.Registry({
        onigLib: onigLoad(),
        loadGrammar: async scopeName => {
          const g = env.grammars[scopeName]; if (!g) return null;
          return vsctm.parseRawGrammar(fs.readFileSync(g.path, 'utf8'), g.path);
        },
        getInjections: scopeName => env.injections[scopeName],
      });
      this.R = { reg, grammars: {}, theme: null };
    }
    if (this.R.theme !== theme) { this.R.reg.setTheme({ name: theme.name, settings: sem.themeRules(theme) }); this.R.colorMap = this.R.reg.getColorMap(); this.R.theme = theme; }
    return this.R;
  }
  async tokenize(file, theme, scopeOverride) {
    const R = await this.registry(theme);
    const lang = languageOf(this.env, file);
    const scope = scopeOverride || (lang && lang.scope);
    if (!scope) throw new Error('no grammar for ' + file);
    const grammar = R.grammars[scope] ||= await R.reg.loadGrammar(scope);
    if (!grammar) throw new Error('grammar failed to load: ' + scope);
    const lines = fs.readFileSync(file, 'utf8').replace(/^﻿/, '').split(/\r?\n/);
    let st1 = vsctm.INITIAL, st2 = vsctm.INITIAL; const out = [];
    lines.forEach((text, ln) => {
      const r1 = grammar.tokenizeLine(text, st1), r2 = grammar.tokenizeLine2(text, st2);
      st1 = r1.ruleStack; st2 = r2.ruleStack;
      const enc = r2.tokens;
      for (const t of r1.tokens) {
        let m = 0; for (let i = 0; i < enc.length; i += 2) { if (enc[i] <= t.startIndex) m = enc[i + 1]; else break; }
        const fg = R.colorMap[(m & 0x00ff8000) >>> 15], style = decodeStyle((m & 0x00007800) >>> 11);
        const end = Math.min(t.endIndex, text.length);
        if (end > t.startIndex) out.push({ line: ln, start: t.startIndex, end, text: text.slice(t.startIndex, end), scopes: t.scopes, fg: fg && fg.toUpperCase(), style });
      }
    });
    return { lang: lang && lang.id, scope, lines, tokens: out };
  }
}

/** Layer semantic tokens (probe dump for one file) over mode-T tokens: returns per-character-run results. */
function applySemantic(tmTokens, semTokens, resolver, language) {
  const res = [];
  for (const t of tmTokens) {
    // split the TM token at semantic token boundaries on the same line
    const cuts = new Set([t.start, t.end]);
    const sts = semTokens.filter(s => s.line === t.line && s.start < t.end && s.start + s.length > t.start);
    for (const s of sts) { cuts.add(Math.max(t.start, s.start)); cuts.add(Math.min(t.end, s.start + s.length)); }
    const pts = [...cuts].sort((a, b) => a - b);
    for (let i = 0; i < pts.length - 1; i++) {
      const a = pts[i], b = pts[i + 1];
      const s = sts.find(x => x.start <= a && x.start + x.length >= b);
      const piece = { ...t, start: a, end: b, text: t.text.slice(a - t.start, b - t.start), tmFg: t.fg, tmStyle: t.style };
      if (s) {
        const { style, src } = resolver.tokenStyle(s.type, s.modifiers, language);
        piece.semantic = { type: s.type, modifiers: s.modifiers, src };
        if (style.foreground) piece.fg = style.foreground.toUpperCase().slice(0, 7);
        const set = new Set(t.style ? t.style.split(' ') : []);
        for (const p of ['bold', 'italic', 'underline', 'strikethrough']) if (style[p] !== undefined) style[p] ? set.add(p) : set.delete(p);
        piece.style = [...set].sort().join(' ');
      }
      res.push(piece);
    }
  }
  return res;
}

/** Rank every theme TextMate rule that matches a token's scope stack (for runner-up analysis). */
function rankRules(theme, scopes) {
  const rules = sem.themeRules(theme).slice(1);
  const out = [];
  rules.forEach((r, i) => { const s = sem.getScopeMatcher(r)(scopes); if (s >= 0) out.push({ idx: i, name: r.name, score: s, fg: r.settings.foreground, fontStyle: r.settings.fontStyle }); });
  return out.sort((a, b) => b.score - a.score || b.idx - a.idx);
}

module.exports = { Harness, applySemantic, rankRules, scanExtensions, readJSON };
