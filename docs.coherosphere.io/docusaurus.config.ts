import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  // ─────────────────────────────────────────────────────────
  // Site basics
  // ─────────────────────────────────────────────────────────
  title: 'Coherosphere Architecture',
  tagline: 'C1–C4 · DDD · Specs',
  favicon: 'img/favicon.ico',

  url: 'https://docs.coherosphere.io',
  baseUrl: '/',

  organizationName: 'coherosphere',
  projectName: 'architecture',

  // Be strict in CI; change to 'warn' locally if needed
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'throw',

  i18n: { defaultLocale: 'en', locales: ['en'] },

  // Serve raw assets directly from the repo (no copying)
  // This makes /assets/** reachable at docs.coherosphere.io/assets/**
  staticDirectories: ['static', '../assets'],

  // Enable Mermaid in Markdown/MDX
  markdown: { mermaid: true },
  themes: ['@docusaurus/theme-mermaid'],

  // ─────────────────────────────────────────────────────────
  // Presets (main docs live in assets/docs)
  // ─────────────────────────────────────────────────────────
  presets: [
    [
      'classic',
      {
        docs: {
          id: 'main',
          path: '../assets/docs',
          routeBasePath: '/',              // docs are the site root
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl: 'https://github.com/coherosphere/architecture/edit/main/docs.coherosphere.io/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') },
      } satisfies Preset.Options,
    ],
  ],

  // ─────────────────────────────────────────────────────────
  // Optional: curated mounts you can use later to add MDX
  // pages that reference raw assets (keeps structure clean).
  // These do nothing unless there are *.md / *.mdx files inside.
  // ─────────────────────────────────────────────────────────
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'diagrams',
        path: '../assets/diagrams',         // keep in assets
        routeBasePath: 'diagrams',          // /diagrams/**
        include: ['**/*.md', '**/*.mdx'],   // only render MD/MDX if you add any
        sidebarPath: false,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'specs',
        path: '../assets/specs',            // keep in assets
        routeBasePath: 'specs',             // /specs/**
        include: ['**/*.md', '**/*.mdx'],   // only render MD/MDX if you add any
        sidebarPath: false,
      },
    ],
  ],

  // ─────────────────────────────────────────────────────────
  // Theme / UI
  // ─────────────────────────────────────────────────────────
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
        {
          label: 'Diagrams',
          position: 'left',
          items: [
            // Raw assets (served via staticDirectories) – no file moves needed
            { to: '/assets/diagrams/overview/C4_Layers_Summary.mmd', label: 'C4 Layers (raw .mmd)' },
            { to: '/assets/diagrams/overview/Architecture_Stack.mmd', label: 'Architecture Stack (raw .mmd)' },
            // If you later add MD/MDX under assets/diagrams, those will appear under /diagrams/**
          ],
        },
        {
          label: 'Specs',
          position: 'left',
          items: [
            { to: '/assets/specs/openapi/C2-11_Gateway.yaml', label: 'Gateway OpenAPI (raw .yaml)' },
            { to: '/assets/specs/events/README.md', label: 'Event Schemas (catalog)' },
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
            { label: 'OpenAPI (raw)', to: '/assets/specs/openapi/' },
            { label: 'Events (JSON Schemas)', to: '/assets/specs/events/' },
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
