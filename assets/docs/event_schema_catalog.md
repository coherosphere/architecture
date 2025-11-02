---
id: event_schema_catalog
slug: /event_schema_catalog
title: Event Schema Catalog
sidebar_label: Event Schema Catalog
---


# Event Schema Catalog

Objective: Enumerate and describe all Coherosphere event schemas (DDD-EVT-xx) across domains.
Note: Defines schema versions, validation criteria, and event flow alignment within the distributed system.
Acts as the registry for event-driven interoperability and data consistency.

---

> Conventions:  
> - `specversion: "1.0"`  
> - `type`: `coh.<domain>.<eventName>.v<major>` (semantic major)  
> - `source`: URI-like producer identifier (e.g., `coh://C2-02/ledger`)  
> - `id`: ULID (monotonic, lexicographically sortable)  
> - `time`: RFC3339 UTC  
> - `datacontenttype`: `application/json; charset=utf-8`  
> - **IDs:** ULID, namespaced: `C2-XX:...` when crossing services
> - **PII:** Personal data must be encrypted or excluded; use PoCI claims or hashed IDs.

---

## Index

- C2-02 PoC: `ContributionSubmitted.v1`, `CPUpdated.v1`
- C2-08 Ethics: `AlignmentChecked.v1`, `AttestationIssued.v1`
- C2-01 Resonance: `ResonanceUpdated.v1`
- C2-07 Metrics: `KPIUpdated.v1`, `SRIComputed.v1`
- C2-03 Governance: `ProposalCreated.v1`, `VoteCast.v1`, `DecisionRecorded.v1`, `PolicyChanged.v1`
- C2-04 Treasury: `FundingAllocated.v1`, `RoundOpened.v1`, `RoundClosed.v1`, `StreamCreated.v1`
- C2-06 Hubs: `ProjectCreated.v1`, `MilestoneReported.v1`, `SyncMerged.v1`
- C2-10 Security: `IncidentOpened.v1`, `TransparencyReportPublished.v1`

---

## Shared JSON Schema Fragments

```json
{
  "$id": "https://coherosphere.com/schemas/common.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "title": "Common Fragments",
  "definitions": {
    "ULID": { "type": "string", "pattern": "^[0-9A-HJKMNP-TV-Z]{26}$" },
    "ID": { "type": "string" },
    "Money": {
      "type": "object",
      "properties": { "amount": { "type": "number" }, "currency": { "type": "string", "minLength": 3, "maxLength": 12 } },
      "required": ["amount", "currency"],
      "additionalProperties": false
    },
    "Did": { "type": "string", "pattern": "^did:[a-z0-9]+:.+" }
  }
}
```

---

## Example: PoC — ContributionSubmitted.v1

**type**: `coh.poc.ContributionSubmitted.v1`  
**source**: `coh://C2-02/ingest`

### JSON Schema
```json
{
  "$id": "https://coherosphere.com/schemas/poc/ContributionSubmitted.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "contributionId": { "$ref": "../common.json#/$defs/ID" },
    "memberId":       { "$ref": "../common.json#/$defs/ID" },
    "projectId":      { "type": ["string","null"] },
    "uri":            { "type": "string", "format": "uri" },
    "refs":           { "type": "array", "items": { "type": "string" }, "default": [] },
    "ingestedAt":     { "type": "string", "format": "date-time" }
  },
  "required": ["contributionId","memberId","uri","ingestedAt"],
  "additionalProperties": true
}
```

### CloudEvent Example
```json
{
  "specversion": "1.0",
  "type": "coh.poc.ContributionSubmitted.v1",
  "source": "coh://C2-02/ingest",
  "id": "01J9X9FJ0Z7D4T0E9R86Z0J3V5",
  "time": "2025-10-31T10:15:00Z",
  "datacontenttype": "application/json; charset=utf-8",
  "data": {
    "contributionId": "C2-02:ctrb-7f3a",
    "memberId": "C2-05:mem-21ab",
    "projectId": "C2-06:proj-9c0d",
    "uri": "ipfs://bafy.../artifact.json",
    "refs": ["https://github.com/..."],
    "ingestedAt": "2025-10-31T10:14:58Z"
  }
}
```

---

## Ethics — AlignmentChecked.v1

**type**: `coh.ethics.AlignmentChecked.v1`  
**source**: `coh://C2-08/evaluator`

```json
{
  "$id": "https://coherosphere.com/schemas/ethics/AlignmentChecked.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "subjectId": { "$ref": "../common.json#/$defs/ID" },
    "rubricId":  { "type": "string" },
    "alignment": { "type": "number", "minimum": 0, "maximum": 1 },
    "explain":   { "type": "string" },
    "version":   { "type": "string" }
  },
  "required": ["subjectId","rubricId","alignment","version"],
  "additionalProperties": false
}
```

CloudEvent:
```json
{
  "specversion": "1.0",
  "type": "coh.ethics.AlignmentChecked.v1",
  "source": "coh://C2-08/evaluator",
  "id": "01J9XA9MAM5X5Q4HJR9EW53K2H",
  "time": "2025-10-31T10:16:40Z",
  "datacontenttype": "application/json",
  "data": {
    "subjectId": "C2-02:ctrb-7f3a",
    "rubricId": "eth.v3",
    "alignment": 0.82,
    "explain": "Meets criteria A,B; minor issues with C.",
    "version": "3.0.0"
  }
}
```

---

## Resonance — ResonanceUpdated.v1

**type**: `coh.resonance.ResonanceUpdated.v1`  
**source**: `coh://C2-01/engine`

Data schema:
```json
{
  "$id": "https://coherosphere.com/schemas/resonance/ResonanceUpdated.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "targetType": { "type": "string", "enum": ["contribution","project","hub","system"] },
    "targetId":   { "$ref": "../common.json#/$defs/ID" },
    "r":          { "type": "number" },
    "i":          { "type": "number" },
    "a":          { "type": "number" },
    "lambda":     { "type": "number" },
    "at":         { "type": "string", "format": "date-time" }
  },
  "required": ["targetType","targetId","r","i","a","lambda","at"],
  "additionalProperties": false
}
```

---

## Metrics — KPIUpdated.v1 / SRIComputed.v1

- `coh.metrics.KPIUpdated.v1` — generic KPI rollups  
- `coh.metrics.SRIComputed.v1` — system resonance index snapshot

```json
{
  "$id": "https://coherosphere.com/schemas/metrics/SRIComputed.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "sri":     { "type": "number" },
    "window":  { "type": "string", "enum": ["1h","24h","7d","30d"] },
    "basis":   { "type": "string", "enum": ["events","projects","hubs"] },
    "at":      { "type": "string", "format": "date-time" }
  },
  "required": ["sri","window","basis","at"],
  "additionalProperties": false
}
```

---

## Governance — ProposalCreated / VoteCast / DecisionRecorded / PolicyChanged

Types:
- `coh.gov.ProposalCreated.v1`
- `coh.gov.VoteCast.v1`
- `coh.gov.DecisionRecorded.v1`
- `coh.gov.PolicyChanged.v1`

**Example** `DecisionRecorded`:
```json
{
  "$id": "https://coherosphere.com/schemas/gov/DecisionRecorded.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "proposalId": { "$ref": "../common.json#/$defs/ID" },
    "outcome":    { "type": "string", "enum": ["Approved","Rejected","NoQuorum"] },
    "quorum":     { "type": "number" },
    "threshold":  { "type": "number" },
    "talliedAt":  { "type": "string", "format": "date-time" }
  },
  "required": ["proposalId","outcome","quorum","threshold","talliedAt"],
  "additionalProperties": false
}
```

---

## Treasury — FundingAllocated / RoundOpened / RoundClosed / StreamCreated

Types:
- `coh.treasury.FundingAllocated.v1`
- `coh.treasury.RoundOpened.v1`
- `coh.treasury.RoundClosed.v1`
- `coh.treasury.StreamCreated.v1`

**Example** `FundingAllocated`:
```json
{
  "$id": "https://coherosphere.com/schemas/treasury/FundingAllocated.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "projectId": { "$ref": "../common.json#/$defs/ID" },
    "amount":    { "$ref": "../common.json#/$defs/Money" },
    "roundId":   { "$ref": "../common.json#/$defs/ID" },
    "at":        { "type": "string", "format": "date-time" }
  },
  "required": ["projectId","amount","roundId","at"],
  "additionalProperties": false
}
```

---

## Security — IncidentOpened / TransparencyReportPublished

Types:
- `coh.security.IncidentOpened.v1`
- `coh.security.TransparencyReportPublished.v1`

**Example** `TransparencyReportPublished`:
```json
{
  "$id": "https://coherosphere.com/schemas/security/TransparencyReportPublished.v1.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "reportId":  { "$ref": "../common.json#/$defs/ID" },
    "hash":      { "type": "string" },
    "uri":       { "type": "string", "format": "uri" },
    "at":        { "type": "string", "format": "date-time" }
  },
  "required": ["reportId","hash","uri","at"],
  "additionalProperties": false
}
```

---

## Validation & Tooling

- JSON Schema: 2020-12  
- Event envelope: CloudEvents 1.0 (binary or structured)  
- Suggested checks: `$schema` presence, required fields, enum coverage, RFC3339 timestamps, ULID shape  
- CI: validate with `ajv`, `spectral`, or custom pipeline

---

**Prepared by:** the coherosphere collective 