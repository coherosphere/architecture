// docs.coherosphere.io/scripts/gen-asset-indexes.mjs
import { promises as fs } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(process.cwd(), 'static/assets/specs');
const TARGETS = [
  { dir: 'openapi', title: 'OpenAPI Specs' , exts: ['.yaml', '.yml'] },
  { dir: 'events',  title: 'Event Schemas', exts: ['.json', '.md'] },
];

// simple recursive lister
async function listFiles(dir, allowExts) {
  const out = [];
  async function walk(p, rel = '') {
    const entries = await fs.readdir(p, { withFileTypes: true });
    for (const e of entries) {
      const full = path.join(p, e.name);
      const relPath = path.join(rel, e.name);
      if (e.isDirectory()) await walk(full, relPath);
      else if (allowExts.includes(path.extname(e.name))) out.push(relPath);
    }
  }
  await walk(dir);
  out.sort();
  return out;
}

function htmlIndex(title, files, baseHref) {
  const items = files.map(f => `<li><a href="./${f}">${f}</a></li>`).join('\n');
  const up = baseHref.split('/').filter(Boolean).length > 1 ? '../' : '/';
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>${title} — Coherosphere</title>
<style>
body{font-family:ui-sans-serif,system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem;color:#e5e7eb;background:#0b0e13}
a{color:#86c5ff;text-decoration:none} a:hover{text-decoration:underline}
h1{margin:0 0 1rem 0;font-size:1.6rem}
ul{line-height:1.6}
.breadcrumbs{margin-bottom:1rem;opacity:.7}
code{background:#111827;padding:.15rem .35rem;border-radius:.35rem}
footer{margin-top:2rem;opacity:.6;font-size:.9rem}
</style>
</head>
<body>
<div class="breadcrumbs"><a href="${up}">/assets</a> / <code>${baseHref}</code></div>
<h1>${title}</h1>
<ul>
${items || '<li><em>No files found</em></li>'}
</ul>
<footer>Generated at build time • Coherosphere</footer>
</body>
</html>`;
}

async function main() {
  for (const t of TARGETS) {
    const dir = path.join(ROOT, t.dir);
    const exists = await fs.access(dir).then(()=>true).catch(()=>false);
    if (!exists) continue;
    const files = await listFiles(dir, t.exts);
    const html = htmlIndex(t.title, files, `/assets/specs/${t.dir}/`);
    await fs.writeFile(path.join(dir, 'index.html'), html, 'utf8');
    console.log(`✓ Wrote index.html for ${t.dir} (${files.length} items)`);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
