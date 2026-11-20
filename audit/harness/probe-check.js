// quick self-test: tokenize a file with Sea Salt and print tokens
const { Harness, scanExtensions, readJSON } = require('./harness');
(async () => {
  const [file, themeFile, ...roots] = process.argv.slice(2);
  const env = scanExtensions(roots);
  const h = new Harness(env); const theme = readJSON(themeFile);
  const r = await h.tokenize(file, theme);
  console.log(r.lang, r.scope);
  for (const t of r.tokens.slice(0, 40)) console.log(t.line + 1, JSON.stringify(t.text).padEnd(18), t.fg, (t.style || '-').padEnd(8), t.scopes.slice(1).join(' '));
})().catch(e => { console.error(e); process.exit(1); });
