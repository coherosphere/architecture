import React, { useEffect, useState } from 'react';
import Layout from '@theme/Layout';

export default function EventSchemasPage() {
  const [files, setFiles] = useState<string[]>([]);

  useEffect(() => {
    fetch('/assets/indexes/specs-events.json').then(r=>r.json()).then(setFiles).catch(()=>setFiles([]));
  }, []);

  return (
    <Layout title="Event Schemas" description="All Event Schemas">
      <main style={{ maxWidth: '900px', margin: '0 auto', padding: '2rem' }}>
        <h1>Event Schemas</h1>
        <ul>{files.map(f => <li key={f}><a href={`/assets/specs/events/${f}`} target="_blank" rel="noreferrer">{f}</a></li>)}</ul>
      </main>
    </Layout>
  );
}
