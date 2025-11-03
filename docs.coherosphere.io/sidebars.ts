import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: 'Architecture Overview',
      collapsible: true,
      collapsed: false,
      items: [
        'manifest',
        'diagrams/diagrams',
        'diagram_color',
      ],
    },
    {
      type: 'category',
      label: 'Design & Modelling',
      collapsible: true,
      collapsed: true,
      items: [
        'ai_guide',
        'slo_table',
        'param_governance',
        'specs/specs',
      ],
    },
    {
      type: 'category',
      label: 'Governance & Processes',
      collapsible: true,
      collapsed: true,
      items: [
        'event_schema_catalog',
        'manifest',
        'architecture_todo',
      ],
    },
    {
      type: 'category',
      label: 'Audit & Reference',
      collapsible: true,
      collapsed: true,
      items: [
        'architecture_status',
        'audit/glossary',
      ],
    },
  ],
};

export default sidebars;
