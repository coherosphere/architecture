import path from 'node:path';
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'coherosphere Architecture',
  tagline: 'C1–C4 · DDD · Specs',
  favicon: 'img/favicon.ico',

  url: 'https://docs.coherosphere.io',
  baseUrl: '/',

  // GitHub pages deployment info
  organizationName: 'coherosphere',
  projectName: 'architecture',

  onBrokenLinks: 'throw',
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          { from: ['/docs/intro'], to: '/manifest' },
        ],
      },
    ],
  ],

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: path.resolve(__dirname, '../assets/docs'),
          routeBasePath: '/', 
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl:
            'https://github.com/coherosphere/architecture/edit/main/docs.coherosphere.io/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/social-card.png',
    colorMode: { respectPrefersColorScheme: true },

    navbar: {
      title: 'coherosphere',
      logo: { alt: 'coherosphere', src: 'img/logo.svg' },
      items: [
        {
          label: 'Architecture',
          position: 'left',
          items: [
            { to: '/architecture/overview', label: 'Overview' },
            { to: '/architecture/diagrams', label: 'Diagrams' },
          ],
        },
        {
          label: 'Design',
          position: 'left',
          items: [
            { to: '/architecture/ai-build-guide', label: 'AI Build Guide' },
            { to: '/architecture/specs', label: 'API & Specs' },
          ],
        },
        {
          label: 'Governance',
          position: 'left',
          items: [
            { to: '/manifest/manifest', label: 'Vision & Principles' },
            { to: '/architecture/event-schema-catalog', label: 'Event Schemas' },
          ],
        },
        {
          label: 'Audit',
          position: 'left',
          items: [
            { to: '/audit/status', label: 'Status' },
            { to: '/audit/glossary', label: 'Glossary' },
          ],
        },

        { type: 'search', position: 'right' },
        { href: 'https://github.com/coherosphere/architecture', label: 'GitHub', position: 'right' },
        { type: 'localeDropdown', position: 'right' },
        { type: 'themeToggle', position: 'right' }, // wenn Plugin aktiv
      ],
    },
  },
};

    footer: {
  style: 'dark',
  links: [
    {
      title: 'Architecture',
      items: [
        { label: 'Manifest', to: '/manifest' },
        { label: 'Status Report', to: '/architecture_status' },
        { label: 'AI Build Guide', to: '/ai_guide' },
      ],
    },
    {
      title: 'Resources',
      items: [
        { label: 'Specs', to: '/specs' },
        { label: 'Diagrams', to: '/diagrams' },
        { label: 'Governance', to: '/param_governance' },
      ],
    },
    {
      title: 'Connect',
      items: [
        { label: 'Website ↗', href: 'https://coherosphere.com' },
        { label: 'GitHub ↗', href: 'https://github.com/coherosphere' },
      ],
    },
  ],
  copyright: `
    <div style="font-size:0.9rem;opacity:.9;margin-top:0.5rem">
      © ${new Date().getFullYear()} coherosphere · Open Knowledge Framework  
      <br/>
      <span style="opacity:.7;">made with resonance ⚡</span>
    </div>
  `,
},

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
