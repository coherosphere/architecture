import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Coherosphere Architecture',
  tagline: 'C1–C4 · DDD · Specs',
  favicon: 'img/favicon.ico',

  url: 'https://docs.coherosphere.io',
  baseUrl: '/',

  organizationName: 'coherosphere',
  projectName: 'architecture',

  // Don’t fail the build while we wire pages
  onBrokenLinks: 'warn',

  // v3 syntax still valid; also add v4-style hook to quiet warnings
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },
  themes: ['@docusaurus/theme-mermaid'],

  i18n: { defaultLocale: 'en', locales: ['en'] },

  presets: [
    [
      'classic',
      {
        docs: {
          path: '../assets/docs',          // your Markdown docs
          routeBasePath: '/',              // docs on homepage
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl: 'https://github.com/coherosphere/architecture/edit/main/docs.coherosphere.io/',
          showLastUpdateTime: true,
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') },
      } satisfies Preset.Options,
    ],
  ],

  // Extra docs instances (must use the explicit plugin)
  plugins: [
    // Diagrams section (folder exists, even if no .md yet)
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'diagrams',
        path: '../assets/diagrams',       // <-- fixed (was ../assets/docs/diagrams)
        routeBasePath: '/diagrams',
        sidebarPath: false,
        include: ['**/*.md', '**/*.mdx'], // ignore .mmd files (no pages yet, but OK)
      },
    ],
    // Specs section (serves READMEs under /specs)
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'specs',
        path: '../assets/specs',           // this folder exists
        routeBasePath: '/specs',
        sidebarPath: false,
        include: ['**/README.md', 'README.md', '**/*.md', '**/*.mdx'],
      },
    ],
  ],

  themeConfig: {
    image: 'img/social-card.png',
    colorMode: { respectPrefersColorScheme: true },
    navbar: {
      title: 'Coherosphere',
      logo: { alt: 'Coherosphere', src: 'img/logo.svg' },
      items: [
        { to: '/', label: 'Docs', position: 'left' },
        { to: '/ARCHITECTURE_TODO_v4.3', label: 'Status (v4.3)', position: 'left' },
        { to: '/AI_BUILD_GUIDE_v4', label: 'AI Build Guide', position: 'left' },
        // Link to section roots for now (avoid deep links to non-existent pages)
        { to: '/diagrams', label: 'Diagrams', position: 'left' },
        { to: '/specs', label: 'Specs', position: 'left' },
        { href: 'https://github.com/coherosphere/architecture', label: 'GitHub', position: 'right' },
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
