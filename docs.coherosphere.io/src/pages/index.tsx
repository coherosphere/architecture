import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';

export default function Home() {
  return (
    <Layout title="Coherosphere Architecture" description="C1–C4 · DDD · Specs">
      <main style={{maxWidth: 880, margin: '0 auto', padding: '3rem 1rem'}}>
        <h1 style={{marginBottom: '1rem'}}>Coherosphere Architecture</h1>
        <p style={{opacity:.85, marginBottom:'2rem'}}>C1–C4 · DDD · Specs</p>
        <ul style={{lineHeight:1.8}}>
          <li><Link to="/architecture_todo">Status</Link></li>
          <li><Link to="/ai_guide">AI Build Guide</Link></li>
          <li><Link to="/manifest">Manifest</Link></li>
          <li><Link to="/diagrams">Diagrams</Link></li>
          <li><Link to="/specs">Specs</Link></li>
        </ul>
      </main>
    </Layout>
  );
}
