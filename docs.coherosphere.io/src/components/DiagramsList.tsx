import React, {useEffect, useMemo, useState} from 'react';
import Mermaid from '@theme/Mermaid';

type DiagramsIndex = string[]; // e.g. ["C1_system/C1_Stakeholders.mmd", "…/file.png"]

function isImg(p: string) { return p.endsWith('.png') || p.endsWith('.svg'); }
function isMmd(p: string) { return p.endsWith('.mmd'); }

export default function DiagramsList() {
  const [files, setFiles] = useState<string[]>([]);
  const [selected, setSelected] = useState<string | null>(null);
  const [mmdCode, setMmdCode] = useState<string>('');
  const [loading, setLoading] = useState(false);

  // load index
  useEffect(() => {
    fetch('/assets/indexes/diagrams.json')
      .then(r => r.json())
      .then((arr: DiagramsIndex) => {
        const sorted = [...arr].sort((a,b)=>a.localeCompare(b));
        setFiles(sorted);
        if (!selected && sorted.length) setSelected(sorted[0]);
      })
      .catch(() => setFiles([]));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // fetch mermaid source when needed
  useEffect(() => {
    if (!selected || !isMmd(selected)) { setMmdCode(''); return; }
    setLoading(true);
    fetch(`/assets/diagrams/${selected}`)
      .then(r => r.text())
      .then(txt => setMmdCode(txt))
      .finally(() => setLoading(false));
  }, [selected]);

  const groups = useMemo(() => {
    const map = new Map<string, string[]>();
    for (const f of files) {
      const dir = f.includes('/') ? f.split('/')[0] : '(root)';
      if (!map.has(dir)) map.set(dir, []);
      map.get(dir)!.push(f);
    }
    return Array.from(map.entries()).sort((a,b)=>a[0].localeCompare(b[0]));
  }, [files]);

  const assetUrl = selected ? `/assets/diagrams/${selected}` : '';
  const downloadName = selected?.split('/').pop() ?? 'diagram';

  return (
    <div style={{display: 'grid', gridTemplateColumns: 'minmax(260px, 380px) 1fr', gap: '1.25rem'}}>
      {/* LEFT: list */}
      <aside style={{borderRight: '1px solid var(--ifm-toc-border-color)', paddingRight: '1rem', maxHeight: '70vh', overflow: 'auto'}}>
        {groups.map(([dir, items]) => (
          <div key={dir} style={{marginBottom: '1rem'}}>
            <div style={{fontWeight: 600, opacity: .85, margin: '.3rem 0 .4rem'}}>{dir}</div>
            <ul style={{listStyle: 'disc', paddingLeft: '1.1rem', margin: 0}}>
              {items.map(p => (
                <li key={p} style={{margin: '.2rem 0'}}>
                  <button
                    onClick={() => setSelected(p)}
                    style={{
                      background: 'transparent', border: 0, padding: 0, cursor: 'pointer',
                      color: 'var(--ifm-link-color)', textDecoration: selected===p ? 'underline' : 'none'
                    }}
                    title={p}
                  >
                    {p.split('/').slice(1).join('/')}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        ))}
        {!files.length && <p>No diagrams found.</p>}
      </aside>

      {/* RIGHT: preview */}
      <section>
        {!selected && <p>Select a diagram…</p>}
        {selected && (
          <>
            <div style={{display:'flex', alignItems:'baseline', gap:'.75rem', marginBottom:'.75rem'}}>
              <h2 style={{margin:0, fontSize:'1.05rem'}}>{selected}</h2>
              <a href={assetUrl} target="_blank" rel="noreferrer">Open</a>
              <a href={assetUrl} download={downloadName}>Download</a>
            </div>

            <div style={{
              border:'1px solid var(--ifm-toc-border-color)',
              borderRadius:'8px',
              padding:'1rem',
              background:'var(--ifm-pre-background)',
              maxHeight:'70vh',
              overflow:'auto'
            }}>
              {isImg(selected) && (
                // Renders inline (keeps header/sidebar)
                <img src={assetUrl} alt={selected} style={{maxWidth:'100%'}} />
              )}

              {isMmd(selected) && (
                loading ? <p>Loading…</p> : <Mermaid value={mmdCode} />
              )}
            </div>
          </>
        )}
      </section>
    </div>
  );
}