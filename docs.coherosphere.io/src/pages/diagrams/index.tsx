import React, { useEffect, useState } from 'react';
import Layout from '@theme/Layout';

export default function DiagramsPage() {
  const [files, setFiles] = useState<string[]>([]);

  useEffect(() => {
    fetch('/assets/indexes/diagrams.json').then(r=>r.json()).then(setFiles).catch(()=>setFiles([]));
  }, []);

  return (
    <Layout title="All Diagrams" description="Architecture Diagrams">
      <main style={{ maxWidth: '900px', margin: '0 auto', padding: '2rem' }}>
        <h1>All Diagrams</h1>
        {files.length ? (
          <ul>{files.map(f => <li key={f}><a href={`/assets/diagrams/${f}`} target="_blank" rel="noreferrer">{f}</a></li>)}</ul>
        ) : (
          <p>No diagrams found.</p>
        )}
      </main>
    </Layout>
  );
}
