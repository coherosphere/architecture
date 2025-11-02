import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Architecture',
      collapsed: false,
      items: [
        'architecture_todo',              
        'architecture_status',
        'ai_guide',
        'manifest',
        'event_schema_catalog',
        'param_governance',
        'slo_table',
        'diagram_color',       
        'diagrams/diagrams',
        'specs/specs',
      ],
    },
  ],
};

export default sidebars;
