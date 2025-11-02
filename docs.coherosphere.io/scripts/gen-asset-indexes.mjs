// Build-time generator: creates JSON & HTML indexes for assets we copy to /static/assets
import { promises as fs } from 'node:fs';
import path from 'node:path';

const STATIC_ROOT = path.resolve(process.cwd(), 'static/assets');
const INDEX_DIR   = path.join(STATIC_ROOT, 'indexes'); // where JSON manifests live

const TARGETS = [
  { base: 'specs/openapi', title: 'OpenAPI Specs',   exts: ['.yaml', '.yml'] , json: 'specs-openapi.json' },
  { base: 'specs/events',  title: 'Event Schemas',   exts: ['.json', '.md']   , json: 'specs-events.json' },
  { base: 'diagrams',      title: 'Architecture Diagrams', exts: ['.mmd','.md','.png','.svg','.jpg','.jpeg','.webp'], json: 'diagrams.json' },
];

async function exists(p) {
  try { await fs.access(p); return true; } catch { return false; }
}

async function listFiles(rootAbs, allowExts) {
  const out = [];
  async function walk(dir, rel='') {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    for (const e of entries) {
      const full = path.join(dir, e.name);
      const relPath = path.join(rel, e.name);
      if (e.isDirectory()) await walk(full, relPath);
      else if (allowExts.includes(path.extname(e.name))) {
        out.push(relPath.replaceAll('\\','/'));
      }
    }
  }
  await walk(rootAbs);
  out.sort();
  return out;
}

function htmlIndex(title, files, baseHref) {
  const items = files.map(f => `<li><a href="./${f}">${f}</a></li>`).join('\n') || '<li><em>No files found</em></li>';
  const crumbUp = baseHref.split('/').filter(Boolean).length > 1 ? '../' : '/';
  return `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<title>${title} — Coherosphere</title>
<style>
body{font-family:ui-sans-serif,system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem;color:#e5e7eb;background:#0b0e13}
a{color:#86c5ff;text-decoration:none} a:hover{text-decoration:underline}
h1{margin:0 0 1rem;font-size:1.6rem} ul{line-height:1.6}
.breadcrumbs{margin-bottom:1rem;opacity:.7}
code{background:#111827;padding:.15rem .35rem;border-radius:.35rem}
footer{margin-top:2rem;opacity:.6;font-size:.9rem}
</style></head>
<body>
<div class="breadcrumbs"><a href="${crumbUp}">/assets</a> / <code>${baseHref}</code></div>
<h1>${title}</h1>
<ul>${items}</ul>
<footer>Generated at build time • Coherosphere</footer>
</body></html>`;
}

async function main() {
  await fs.mkdir(INDEX_DIR, { recursive: true });

  for (const t of TARGETS) {
    const abs = path.join(STATIC_ROOT, t.base);
    const ok = await exists(abs);
    if (!ok) continue;

    const files = await listFiles(abs, t.exts);
    const jsonPath = path.join(INDEX_DIR, t.json);
    await fs.writeFile(jsonPath, JSON.stringify(files, null, 2), 'utf8');

    const html = htmlIndex(t.title, files, `/assets/${t.base}/`);
    await fs.writeFile(path.join(abs, 'index.html'), html, 'utf8');

    console.log(`✓ Indexed ${files.length} files in ${t.base}`);
  }
}

main().catch(e => { console.error(e); process.exit(1); });
