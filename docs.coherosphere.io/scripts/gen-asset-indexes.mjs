// scripts/gen-asset-indexes.mjs
import { promises as fs } from 'node:fs';
import path from 'node:path';

const ROOT_STATIC = path.resolve(process.cwd(), 'static/assets');
const ASSETS_SRC  = path.resolve(process.cwd(), '../assets'); // repo_root/assets
const OUT_DIR     = path.join(ROOT_STATIC, 'indexes');        // <- KORREKT: /static/assets/indexes

const toPosix = p => p.split(path.sep).join('/');

async function ensureDir(p){ await fs.mkdir(p,{recursive:true}); }

async function listRecursive(dir, {allowExts}) {
  const out = [];
  async function walk(abs, rel='') {
    const entries = await fs.readdir(abs, {withFileTypes:true});
    for (const e of entries) {
      if (e.name.startsWith('.')) continue;              // ignoriere .DS_Store etc.
      const absChild = path.join(abs, e.name);
      const relChild = path.join(rel, e.name);
      if (e.isDirectory()) await walk(absChild, relChild);
      else if (allowExts.includes(path.extname(e.name).toLowerCase())) out.push(toPosix(relChild));
    }
  }
  await walk(dir);
  out.sort((a,b)=>a.localeCompare(b));
  return out;
}

async function writeJSON(name, data) {
  await ensureDir(OUT_DIR);
  const file = path.join(OUT_DIR, name);
  await fs.writeFile(file, JSON.stringify(data, null, 2), 'utf8');
  console.log(`✓ Wrote ${toPosix(path.relative(process.cwd(), file))} (${data.length} entries)`);
}

async function indexDiagrams() {
  const dir = path.join(ASSETS_SRC, 'diagrams');
  try { await fs.access(dir); }
  catch { return writeJSON('diagrams.json', []); }
  const files = await listRecursive(dir, {allowExts:['.mmd','.svg','.png']});
  await writeJSON('diagrams.json', files);
}

async function indexSpecs() {
  const targets = [
    ['specs/openapi',           'specs_openapi.json',         ['.yaml','.yml']],
    ['specs/events',            'specs_events.json',          ['.json','.md']],
    ['specs/events_cloudevents','specs_events_cloudevents.json',['.json']],
    ['specs/cors',              'specs_cors.json',            ['.json','.md']],
  ];
  for (const [folder, outName, exts] of targets) {
    const dir = path.join(ASSETS_SRC, folder);
    try { await fs.access(dir); 
      const files = await listRecursive(dir, {allowExts: exts});
      await writeJSON(outName, files);
    } catch { await writeJSON(outName, []); }
  }
}

(async () => {
  await ensureDir(OUT_DIR);
  await Promise.all([indexDiagrams(), indexSpecs()]);
})().catch(err => { console.error(err); process.exit(1); });