import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// ────────────────────────────────────────────────────────────────
// Coherosphere Docusaurus Configuration
// Serves docs from /assets/docs and static content from /assets/
// ────────────────────────────────────────────────────────────────

const config: Config = {
  // ── Site basics ───────────────────────────────────────────────
  title: 'Coherosphere Architecture',
  tagline: 'C1–C4 · DDD · Specs',
  favicon: 'img/favicon.ico',

  url: 'https://docs.coherosphere.io',
  baseUrl: '/',

  // GitHub pages deployment info
  organizationName: 'coherosphere',
  projectName: 'architecture',

  // ── Link handling ─────────────────────────────────────────────
  onBrokenLinks: 'throw',
  markdown: {
    mermaid: true,
    hooks: {
      // Do not fail build for links pointing to static assets
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  plugins: [
  [
    '@docusaurus/plugin-client-redirects',
    {
      redirects: [
        { from: ['/docs/intro'], to: '/Manifest' },
      ],
    },
  ],
],

  // ── Localization ──────────────────────────────────────────────
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // ── Presets ───────────────────────────────────────────────────
  presets: [
    [
      'classic',
      {
        docs: {
          path: '../assets/docs',
          routeBasePath: '/', // Docs appear at site root
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl: 'https://github.com/coherosphere/architecture/edit/main/docs.coherosphere.io/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false, // No blog for now
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      } satisfies Preset.Options,
    ],
  ],

  // ── Theme / UI Configuration ──────────────────────────────────
  themeConfig: {
    image: 'img/social-card.png',
    colorMode: { respectPrefersColorScheme: true },

    navbar: {
      title: 'Coherosphere',
      logo: {
        alt: 'Coherosphere Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/', label: 'Docs', position: 'left' },
        { to: '/ARCHITECTURE_TODO_v4.3', label: 'Status (v4.3)', position: 'left' },
        { to: '/AI_BUILD_GUIDE_v4', label: 'AI Build Guide', position: 'left' },
        { to: '/Manifest', label: 'Manifest', position: 'left' },
        {
          label: 'Diagrams',
          position: 'left',
          items: [
            { to: '/diagrams', label: 'Overview' },
          ],
        },
        { to: '/specs', label: 'Specs', position: 'left' },
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
            { label: 'Specs Overview', to: '/specs' },
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