# C4 ↔ DDD Event Schema Alignment Validator

Validates that each `DDD-EVT-XX` referenced in `assets/diagrams/C4_sequences/*.mmd`:
1) Has a schema under `assets/specs/events/DDD-EVT-XX_*.json`
2) Contains a `properties.c4Sequence.enum` including the `C4-YY` for the diagram where it appears
3) Warns on missing CloudEvents envelope fields

## Usage
```bash
python3 c4_schema_alignment/validate_c4_event_schemas.py --repo-root .
# Optional strict mode
python3 c4_schema_alignment/validate_c4_event_schemas.py --repo-root . --fail-on-warn
```

Generated: 2025-11-01T12:22:39.768833Z
