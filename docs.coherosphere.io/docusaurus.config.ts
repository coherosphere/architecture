import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';


const config: Config = {
  // ── Site basics ───────────────────────────────────────────
  title: 'Coherosphere Architecture',
  tagline: 'C1–C4 · DDD · Specs',
  favicon: 'img/favicon.ico',

  url: 'https://docs.coherosphere.io',
  baseUrl: '/',

  // GitHub repo info (für Edit-Links etc.)
  organizationName: 'coherosphere',
  projectName: 'architecture',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // ── Enable Mermaid ────────────────────────────────────────
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  // ── Presets ───────────────────────────────────────────────
  presets: [
    [
      'classic',
      {
        docs: {
          // Wir verwenden die bereits vorhandenen Markdown-Dokumente im Repo:
          path: '../assets/docs',
          routeBasePath: '/', // Docs sind die Startseite
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl: 'https://github.com/coherosphere/architecture/edit/main/docs/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false, // kein Blog
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      } satisfies Preset.Options,
    ],
  ],

  // ── Theme / UI ────────────────────────────────────────────
  themeConfig: {
    image: 'img/social-card.png',
    colorMode: { respectPrefersColorScheme: true },
    navbar: {
      title: 'Coherosphere',
      logo: { alt: 'Coherosphere', src: 'img/logo.svg' },
      items: [
        // Beispiele: passe Ziele an deine Dateien in assets/docs an
        { to: '/', label: 'Docs', position: 'left' },
        { to: '/ARCHITECTURE_TODO_v4.3', label: 'Status (v4.3)', position: 'left' },
        { to: '/AI_BUILD_GUIDE_v4', label: 'AI Build Guide', position: 'left' },
        {
          label: 'Diagrams',
          position: 'left',
          items: [
            { to: '/diagrams/overview/C4_Layers_Summary', label: 'C4 Layers Summary' },
            { to: '/diagrams/overview/Architecture_Stack', label: 'Architecture Stack' },
          ],
        },
        {
          href: 'https://github.com/coherosphere/architecture',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Architecture',
          items: [
            { label: 'Manifest', to: '/Manifest' },
            { label: 'Status Report', to: '/ARCHITECTURE_STATUS_REPORT_v4' },
          ],
        },
        {
          title: 'Specs',
          items: [
            { label: 'OpenAPI', to: '/specs/openapi/README' },
            { label: 'Events (JSON Schemas)', to: '/specs/events/README' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Coherosphere.com', href: 'https://coherosphere.com' },
            { label: 'GitHub', href: 'https://github.com/coherosphere/architecture' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Coherosphere — CC BY 4.0`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;