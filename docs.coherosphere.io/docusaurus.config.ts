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
      logo: {
        alt: 'Coherosphere Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/architecture_todo', label: 'Todo', position: 'left' },
        { to: '/ai_guide', label: 'AI Build', position: 'left' },
        { to: '/manifest', label: 'Manifest', position: 'left' },
        { to: '/diagrams', label: 'Diagrams', position: 'left' },
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
            { label: 'Manifest', to: '/manifest' },
            { label: 'Status Report', to: '/architecture_status' },
          ],
        },
        {
          title: 'Specs',
          items: [{ label: 'Specs Overview', to: '/specs' }],
        },
        {
          title: 'More',
          items: [
            { label: 'Coherosphere.com', href: 'https://coherosphere.com' },
            { label: 'GitHub', href: 'https://github.com/coherosphere/architecture' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} coherosphere — CC BY 4.0`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;