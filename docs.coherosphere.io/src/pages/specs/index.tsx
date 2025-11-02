import React, { useEffect, useState } from 'react';
import Layout from '@theme/Layout';

export default function SpecsPage() {
  const [openapi, setOpenapi] = useState<string[]>([]);
  const [events, setEvents] = useState<string[]>([]);

  useEffect(() => {
    fetch('/assets/indexes/specs-openapi.json').then(r=>r.json()).then(setOpenapi).catch(()=>setOpenapi([]));
    fetch('/assets/indexes/specs-events.json').then(r=>r.json()).then(setEvents).catch(()=>setEvents([]));
  }, []);

  return (
    <Layout title="All Specifications" description="All Coherosphere Specifications">
      <main style={{ maxWidth: '900px', margin: '0 auto', padding: '2rem' }}>
        <h1>All Specifications</h1>

        <h2>OpenAPI Specs</h2>
        <ul>{openapi.map(f => <li key={f}><a href={`/assets/specs/openapi/${f}`} target="_blank" rel="noreferrer">{f}</a></li>)}</ul>

        <h2>Event Schemas</h2>
        <ul>{events.map(f => <li key={f}><a href={`/assets/specs/events/${f}`} target="_blank" rel="noreferrer">{f}</a></li>)}</ul>
      </main>
    </Layout>
  );
}
