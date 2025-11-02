import React, {useEffect, useMemo, useState} from 'react';
import CodeBlock from '@theme/CodeBlock';

// ---------- Helpers ----------
const isYaml = (p: string) => p.endsWith('.yaml') || p.endsWith('.yml');
const isJson = (p: string) => p.endsWith('.json');
const isMd   = (p: string) => p.endsWith('.md') || p.endsWith('.markdown');
const basename = (p: string) => p.split('/').pop() ?? p;

// Normalize an index entry to be relative to its category folder
function normalizeEntry(entry: string, category: string): string {
  let e = entry.trim();
  if (!e) return e;

  // strip leading "./"
  if (e.startsWith('./')) e = e.slice(2);
  // If the entry is absolute with the assets path, strip it
  if (e.startsWith('/assets/specs/')) {
    e = e.replace('/assets/specs/', '');
  }
  // If it still contains the category as the first segment, remove it
  if (e.startsWith(category + '/')) {
    e = e.slice(category.length + 1);
  }
  return e;
}

type IndexList = string[];

function useIndex(urls: string[], category: string) {
  const [list, setList] = useState<string[]>([]);
  useEffect(() => {
    let cancelled = false;
    (async () => {
      for (const u of urls) {
        try {
          const r = await fetch(u);
          if (!r.ok) continue;
          const arr: IndexList = await r.json();
          const norm = arr
            .map(x => normalizeEntry(x, category))
            .filter(Boolean)
            .sort((a,b)=>a.localeCompare(b));
          if (!cancelled) setList(norm);
          break;
        } catch { /* try next */ }
      }
    })();
    return () => { cancelled = true; };
  }, [urls.join('|'), category]);

  return list;
}

// ---------- Component ----------
type CatKey = 'openapi'|'events'|'events_cloudevents'|'cors';

const CATEGORIES: {key: CatKey; label: string; indexUrls: string[]}[] = [
  { key: 'openapi',           label: 'OpenAPI',         indexUrls: ['/assets/indexes/specs-openapi.json','/assets/indexes/openapi.json'] },
  { key: 'events',            label: 'Event Schemas',   indexUrls: ['/assets/indexes/specs-events.json','/assets/indexes/events.json'] },
  { key: 'events_cloudevents',label: 'CloudEvents',     indexUrls: ['/assets/indexes/specs-events_cloudevents.json','/assets/indexes/cloudevents.json'] },
  { key: 'cors',              label: 'CORS Policies',   indexUrls: ['/assets/indexes/specs-cors.json','/assets/indexes/cors.json'] },
];

export default function SpecsList() {
  const [tab, setTab] = useState<CatKey>('openapi');

  // load each category lazily
  const lists = {
    openapi: useIndex(CATEGORIES[0].indexUrls, 'openapi'),
    events:  useIndex(CATEGORIES[1].indexUrls, 'events'),
    events_cloudevents: useIndex(CATEGORIES[2].indexUrls, 'events_cloudevents'),
    cors:    useIndex(CATEGORIES[3].indexUrls, 'cors'),
  };

  const files = lists[tab] || [];

  // selection
  const [selected, setSelected] = useState<string | null>(null);
  useEffect(() => {
    if (files.length && (!selected || !files.includes(selected))) {
      setSelected(files[0]);
    }
    if (!files.length) setSelected(null);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [tab, files.join('|')]);

  // fetch selected content
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    setText('');
    if (!selected) return;
    setLoading(true);
    const url = `/assets/specs/${tab}/${selected}`;
    fetch(url)
      .then(r => r.text())
      .then(t => setText(t))
      .finally(() => setLoading(false));
  }, [selected, tab]);

  // left nav grouping
  const groups = useMemo(() => {
    const map = new Map<string, string[]>();
    for (const f of files) {
      const dir = f.includes('/') ? f.split('/').slice(0,-1).join('/') : '(root)';
      if (!map.has(dir)) map.set(dir, []);
      map.get(dir)!.push(f);
    }
    return Array.from(map.entries()).sort((a,b)=>a[0].localeCompare(b[0]));
  }, [files]);

  const assetUrl = selected ? `/assets/specs/${tab}/${selected}` : '';

  return (
    <div>
      {/* Tabs */}
      <div style={{display:'flex', gap:'0.5rem', margin:'0 0 1rem 0'}}>
        {CATEGORIES.map(c => (
          <button
            key={c.key}
            className={`button button--sm ${tab===c.key ? 'button--primary' : ''}`}
            onClick={() => setTab(c.key)}
          >
            {c.label}
          </button>
        ))}
      </div>

      <div style={{display:'grid', gridTemplateColumns:'minmax(260px, 340px) 1fr', gap:'1.25rem'}}>
        {/* LEFT: grouped list */}
        <aside style={{borderRight:'1px solid var(--ifm-toc-border-color)', paddingRight:'1rem', maxHeight:'70vh', overflow:'auto'}}>
          {groups.length === 0 && <p style={{opacity:.8}}>No specs found.</p>}
          {groups.map(([dir, items]) => (
            <div key={dir} style={{marginBottom:'1rem'}}>
              <div style={{fontWeight:600, opacity:.85, margin:'.3rem 0 .4rem'}}>{dir}</div>
              <ul style={{listStyle:'disc', paddingLeft:'1.1rem', margin:0}}>
                {items.map(p => (
                  <li key={p} style={{margin:'.2rem 0'}}>
                    <button
                      onClick={() => setSelected(p)}
                      style={{
                        background:'transparent',
                        border:0,
                        padding:0,
                        cursor:'pointer',
                        color:'var(--ifm-link-color)',
                        textDecoration:selected===p ? 'underline' : 'none'
                      }}
                      title={p}
                    >
                      {basename(p)}
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </aside>

        {/* RIGHT: inline preview */}
        <section>
          {!selected && <p>Select a file…</p>}
          {selected && (
            <>
              <div style={{display:'flex', alignItems:'baseline', gap:'.75rem', marginBottom:'.75rem'}}>
                <h2 style={{margin:0, fontSize:'1.05rem'}}>{basename(selected)}</h2>
                <a href={assetUrl} target="_blank" rel="noreferrer">Open</a>
                <a href={assetUrl} download={basename(selected)}>Download</a>
              </div>
              <div
                style={{
                  border:'1px solid var(--ifm-toc-border-color)',
                  borderRadius:'8px',
                  padding:'1rem',
                  background:'var(--ifm-pre-background)',
                  maxHeight:'70vh',
                  overflow:'auto'
                }}
              >
                {loading && <p>Loading…</p>}
                {!loading && isYaml(selected) && <CodeBlock language="yaml">{text}</CodeBlock>}
                {!loading && isJson(selected) && (
                  <CodeBlock language="json">
                    {(() => { try { return JSON.stringify(JSON.parse(text), null, 2); } catch { return text; } })()}
                  </CodeBlock>
                )}
                {!loading && isMd(selected) && <CodeBlock language="md">{text}</CodeBlock>}
                {!loading && !(isYaml(selected)||isJson(selected)||isMd(selected)) && (
                  <p>Preview not supported for this type. Use “Open” or “Download”.</p>
                )}
              </div>
            </>
          )}
        </section>
      </div>
    </div>
  );
}