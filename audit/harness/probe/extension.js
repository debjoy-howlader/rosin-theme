// Dev-only probe for the Rosin audit. If the workspace has .rosin-probe.json, it opens each listed file,
// waits for the semantic token provider to settle, and writes legend + decoded tokens + diagnostics to JSON.
// It never changes any setting or file outside the dump folder named in the request.
const vscode = require('vscode'), fs = require('fs'), path = require('path');
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function tokensFor(uri) {
  let legend, toks;
  try { legend = await vscode.commands.executeCommand('vscode.provideDocumentSemanticTokensLegend', uri); } catch (e) { legend = undefined; }
  try { toks = await vscode.commands.executeCommand('vscode.provideDocumentSemanticTokens', uri); } catch (e) { toks = undefined; }
  let kind = 'document';
  if (!toks || !toks.data || toks.data.length === 0) {
    try {
      const doc = await vscode.workspace.openTextDocument(uri);
      const range = new vscode.Range(0, 0, doc.lineCount, 0);
      const rl = await vscode.commands.executeCommand('vscode.provideDocumentRangeSemanticTokensLegend', uri, range);
      const rt = await vscode.commands.executeCommand('vscode.provideDocumentRangeSemanticTokens', uri, range);
      if (rt && rt.data && rt.data.length) { legend = rl || legend; toks = rt; kind = 'range'; }
    } catch (e) { /* no range provider */ }
  }
  const out = [];
  if (legend && toks && toks.data) {
    const d = toks.data; let line = 0, ch = 0;
    for (let i = 0; i < d.length; i += 5) {
      line += d[i]; ch = d[i] === 0 ? ch + d[i + 1] : d[i + 1];
      const mods = []; for (let b = 0; b < legend.tokenModifiers.length; b++) if (d[i + 4] & (1 << b)) mods.push(legend.tokenModifiers[b]);
      out.push({ line, start: ch, length: d[i + 2], type: legend.tokenTypes[d[i + 3]], modifiers: mods });
    }
  }
  return { legend: legend ? { tokenTypes: legend.tokenTypes, tokenModifiers: legend.tokenModifiers } : null, kind, tokens: out };
}

async function run(reqFile, root) {
  const req = JSON.parse(fs.readFileSync(reqFile, 'utf8'));
  const outDir = path.join(root, req.out); fs.mkdirSync(outDir, { recursive: true });
  const log = m => fs.appendFileSync(path.join(outDir, '_probe.log'), new Date().toISOString() + ' ' + m + '\n');
  const exts = vscode.extensions.all.filter(e => !e.packageJSON.isBuiltin).map(e => e.id + '@' + e.packageJSON.version);
  const cfg = vscode.workspace.getConfiguration();
  fs.writeFileSync(path.join(outDir, '_env.json'), JSON.stringify({
    vscode: vscode.version, extensions: exts, theme: cfg.get('workbench.colorTheme'),
    semanticHighlighting: cfg.get('editor.semanticHighlighting.enabled'), request: req
  }, null, 1));
  log('start ' + req.label);
  for (const rel of req.files) {
    const uri = vscode.Uri.file(path.join(root, rel));
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc, { preview: false });
    // wait until the provider returns the same token count twice in a row (server finished indexing)
    let last = -1, same = 0, res, t0 = Date.now();
    while (Date.now() - t0 < (req.timeoutMs || 90000)) {
      await sleep(req.pollMs || 2500);
      res = await tokensFor(uri);
      const n = res.tokens.length;
      // no legend yet: keep polling for legendWaitMs (default 10 s, the old behaviour) before concluding the server offers no semantic provider
      if (!res.legend && Date.now() - t0 > (req.legendWaitMs || 10000)) break;
      if (Date.now() - t0 < (req.minWaitMs || 0)) { last = n; continue; }
      // stability only counts once the server has offered a legend; without one the legendWaitMs rule above decides
      if (res.legend && n === last && (n > 0 || Date.now() - t0 > (req.emptyOkAfterMs || 20000))) { if (++same >= 2) break; } else same = 0;
      last = n;
    }
    const diags = vscode.languages.getDiagnostics(uri).map(d => ({ line: d.range.start.line, sev: d.severity, msg: d.message, source: d.source, code: typeof d.code === 'object' ? d.code.value : d.code }));
    res.languageId = doc.languageId; res.file = rel; res.diagnostics = diags; res.waitedMs = Date.now() - t0;
    fs.writeFileSync(path.join(outDir, rel.replace(/[\\/]/g, '__') + '.json'), JSON.stringify(res));
    log(`${rel} lang=${doc.languageId} tokens=${res.tokens.length} kind=${res.kind} diags=${diags.length} waited=${res.waitedMs}`);
  }
  log('done');
  fs.writeFileSync(path.join(outDir, '_done'), new Date().toISOString());
  if (req.quit) { await sleep(1000); vscode.commands.executeCommand('workbench.action.quit'); }
}

async function calibrate(req, root) {
  const items = JSON.parse(fs.readFileSync(path.join(root, req.calibrate), 'utf8'));
  const outDir = path.join(root, req.out); fs.mkdirSync(outDir, { recursive: true });
  const log = m => fs.appendFileSync(path.join(outDir, '_calib.log'), Date.now() + ' ' + m + '\n');
  const cfg = vscode.workspace.getConfiguration();
  // open every file first so language servers can index while we wait
  for (const f of [...new Set(items.map(i => i.file))]) await vscode.window.showTextDocument(await vscode.workspace.openTextDocument(vscode.Uri.file(path.join(root, f))), { preview: false });
  log('warmup'); await sleep(req.warmupMs || 45000);
  const open = {};
  for (const theme of req.themes) {
    await cfg.update('workbench.colorTheme', theme, vscode.ConfigurationTarget.Global); await sleep(2500);
    open.prev = null; await vscode.commands.executeCommand('workbench.action.closeAllEditors');
    for (const it of items) {
      if (theme !== req.themes[0] && !it.licorice) continue;
      const ed = await vscode.window.showTextDocument(await vscode.workspace.openTextDocument(vscode.Uri.file(path.join(root, it.file))), { preview: false });
      const p = new vscode.Position(it.line, it.start);
      ed.selection = new vscode.Selection(p, p);
      ed.revealRange(new vscode.Range(Math.max(0, it.line - 2), 0, it.line, 0), vscode.TextEditorRevealType.AtTop);
      vscode.window.setStatusBarMessage(`CAL ${it.n} ${theme.replace('Rosin · ', '')} ${it.comp}`, req.intervalMs);
      await sleep(400);
      // the inspector is a per-editor toggle that reads the cursor when it opens: close it if this editor has it, then open it fresh
      // one editor group reuses one editor widget, so switching files closes the inspector (model change); same file -> still open
      if (open.prev === it.file) { await vscode.commands.executeCommand('editor.action.inspectTMScopes'); await sleep(250); }
      await vscode.commands.executeCommand('editor.action.inspectTMScopes'); open.prev = it.file;
      log(`step ${it.n} ${theme} ${it.comp}`);
      await sleep(req.intervalMs);
    }
  }
  await cfg.update('workbench.colorTheme', req.themes[0], vscode.ConfigurationTarget.Global);
  log('done'); fs.writeFileSync(path.join(outDir, '_calib_done'), 'x');
  if (req.quit) vscode.commands.executeCommand('workbench.action.quit');
}

exports.activate = async ctx => {
  ctx.subscriptions.push(vscode.commands.registerCommand('rosinProbe.dump', () => {
    const root = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath; if (root) run(path.join(root, '.rosin-probe.json'), root);
  }));
  const root = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (root && fs.existsSync(path.join(root, '.rosin-probe.json'))) {
    const req0 = JSON.parse(fs.readFileSync(path.join(root, '.rosin-probe.json'), 'utf8'));
    if (req0.calibrate) { try { await calibrate(req0, root); } catch (e) { fs.appendFileSync(path.join(root, 'probe-error.log'), String(e && e.stack || e) + '\n'); } return; }
    try { await run(path.join(root, '.rosin-probe.json'), root); } catch (e) { fs.appendFileSync(path.join(root, 'probe-error.log'), String(e && e.stack || e) + '\n'); }
  }
};
exports.deactivate = () => {};
