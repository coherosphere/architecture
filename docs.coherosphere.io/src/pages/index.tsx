import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

export default function Home() {
  return (
    <Layout
      title="Coherosphere Architecture"
      description="Unified documentation hub for architecture, specs, and governance."
    >
      <main className={styles.main}>
        {/* ── Hero ───────────────────────────────────────────── */}
        <section className={styles.hero}>
          <h1 className={styles.title}>architectural documentation Hub</h1>
          <p className={styles.subtitle}>
            Explore the architectural structure, specifications, and governance principles
            of the coherosphere framework.
          </p>
        </section>

        {/* ── Overview Grid ──────────────────────────────────── */}
        <section className={styles.gridSection}>
          <h2 className={styles.sectionTitle}>Core Documentation</h2>
          <div className="cs-grid cs-grid--cols-2">
            <div className="cs-item">
              <h3><Link to="/architecture_todo">Architecture Todo</Link></h3>
              <p>Active development goals and next steps across modules.</p>
            </div>
            <div className="cs-item">
              <h3><Link to="/architecture_status">Status Report</Link></h3>
              <p>Current maturity, completed milestones, and open threads.</p>
            </div>
            <div className="cs-item">
              <h3><Link to="/ai_guide">AI Build Guide</Link></h3>
              <p>Instructions for building, training, and deploying Coherosphere AI components.</p>
            </div>
            <div className="cs-item">
              <h3><Link to="/manifest">Manifest</Link></h3>
              <p>The philosophical and structural foundation of the Coherosphere.</p>
            </div>
          </div>
        </section>

        {/* ── Specs ─────────────────────────────────────────── */}
        <section className={styles.gridSection}>
          <h2 className={styles.sectionTitle}>Specifications</h2>
          <div className="cs-grid cs-grid--cols-2">
            <div className="cs-item">
              <h3><Link to="/specs">All Specs</Link></h3>
              <p>Browse OpenAPI and Event schema specifications.</p>
            </div>
            <div className="cs-item">
              <h3><Link to="/param_governance">Parameter Governance SOP</Link></h3>
              <p>Procedures for versioning, validation, and rollback of system parameters.</p>
            </div>
            <div className="cs-item">
              <h3><Link to="/slo_table">SLO Table</Link></h3>
              <p>Defined reliability and service-level objectives across components.</p>
            </div>
          </div>
        </section>

        {/* ── Diagrams ───────────────────────────────────────── */}
        <section className={styles.gridSection}>
          <h2 className={styles.sectionTitle}>Visual Architecture</h2>
          <div className="cs-grid cs-grid--cols-2">
            <div className="cs-item">
              <h3><Link to="/diagrams">All Diagrams</Link></h3>
              <p>Explore C1–C4 architecture diagrams and systemic overviews.</p>
            </div>
          </div>
        </section>

        {/* ── Meta Section ───────────────────────────────────── */}
        <section className={styles.meta}>
          <p>
            All content is part of the <strong>coherosphere architecture repository</strong>.<br />
            Licensed under <Link to="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</Link>.
          </p>
          <p>
            View source on{' '}
            <Link href="https://github.com/coherosphere/architecture">GitHub</Link>.
          </p>
        </section>
      </main>
    </Layout>
  );
}