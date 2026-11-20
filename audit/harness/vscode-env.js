// Grammar registry and language map built from VS Code's own extension manifests,
// so tokenisation uses exactly the grammars, injections and embedded languages VS Code loads.
'use strict';
const fs = require('fs'), path = require('path');

function readJSON(p) { return JSON.parse(fs.readFileSync(p, 'utf8').replace(/^﻿/, '')); }

/** dirs: list of extension folders (each containing package.json). Later entries override earlier ones
 *  for the same scopeName, as installed extensions override built-ins in VS Code. */
function scanExtensions(extRoots, { exclude = [] } = {}) {
  const grammars = {}, injections = {}, languages = {}, semantic = { types: [], modifiers: [], scopes: [] }, extsSeen = [];
  for (const root of extRoots) {
    if (!fs.existsSync(root)) continue;
    const names = fs.existsSync(path.join(root, 'package.json')) ? [''] : fs.readdirSync(root).sort();
    for (const name0 of names) {
      const name = name0 || path.basename(root); const dir = path.join(root, name0), pj = path.join(dir, 'package.json');
      if (!fs.existsSync(pj)) continue;
      if (exclude.some(x => name.toLowerCase().startsWith(x.toLowerCase()))) continue;
      let d; try { d = readJSON(pj); } catch { continue; }
      const c = d.contributes || {};
      extsSeen.push(name);
      for (const l of c.languages || []) {
        const L = languages[l.id] ||= { id: l.id, extensions: [], filenames: [] };
        L.extensions.push(...(l.extensions || []).map(e => e.toLowerCase()));
        L.filenames.push(...(l.filenames || []));
      }
      for (const g of c.grammars || []) {
        if (!g.scopeName || !g.path) continue;
        grammars[g.scopeName] = { path: path.join(dir, g.path), language: g.language, embeddedLanguages: g.embeddedLanguages, tokenTypes: g.tokenTypes, ext: name };
        for (const t of g.injectTo || []) (injections[t] ||= []).push(g.scopeName);
        if (g.language && languages[g.language]) languages[g.language].scope = g.scopeName;
        else if (g.language) (languages[g.language] ||= { id: g.language, extensions: [], filenames: [] }).scope = g.scopeName;
      }
      for (const t of c.semanticTokenTypes || []) semantic.types.push({ ...t, ext: name });
      for (const m of c.semanticTokenModifiers || []) semantic.modifiers.push({ ...m, ext: name });
      for (const s of c.semanticTokenScopes || []) semantic.scopes.push({ ...s, ext: name });
    }
  }
  return { grammars, injections, languages, semantic, extsSeen };
}

function languageOf(env, file) {
  // VS Code's order: exact filename (case-insensitive on Windows), then the longest matching extension suffix.
  const base = path.basename(file).toLowerCase();
  let best = null, bestLen = -1;
  for (const L of Object.values(env.languages)) {
    if (!L.scope) continue;
    if (L.filenames.some(f => f.toLowerCase() === base)) return L;
    for (const e of L.extensions) if (base.endsWith(e) && e.length > bestLen) { best = L; bestLen = e.length; }
  }
  return best;
}
module.exports = { scanExtensions, languageOf, readJSON };
