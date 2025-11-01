#!/usr/bin/env python3
import json, re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "assets" / "specs" / "events"
DST  = ROOT / "assets" / "specs" / "events_cloudevents"
DST.mkdir(parents=True, exist_ok=True)

evt_rx = re.compile(r"^DDD-EVT-(\d+)\.json$", re.IGNORECASE)

from typing import Optional

def cloudevent_schema(evt_id: str, base_id: str, title: Optional[str]):
    # CloudEvents-Wrapper; Daten bleiben im bestehenden Schema via $ref
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://coherosphere.dev/schemas/events/cloudevents/{evt_id}.json",
        "title": f"{title or evt_id} (CloudEvents)",
        "type": "object",
        "required": ["specversion", "id", "source", "type", "time", "data"],
        "additionalProperties": False,
        "properties": {
            "specversion": {"type": "string", "const": "1.0"},
            "id":         {"type": "string", "description": "Event UUID"},
            "source":     {"type": "string", "format": "uri"},
            "type":       {"type": "string", "const": f"coherosphere.events.{evt_id}"},
            "subject":    {"type": "string"},
            "time":       {"type": "string", "format": "date-time"},
            "datacontenttype": {"type": "string", "const": "application/json"},
            # Wichtig: data verweist auf das bestehende Event-Schema
            "data": {"$ref": base_id}
        },
        # nützliche Meta
        "x-coherosphere": {
            "eventId": evt_id,
            "version": "1.0.0",
            "generatedAt": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "linkToBaseSchema": base_id
        }
    }

index = []
for p in sorted(SRC.glob("DDD-EVT-*.json")):
    if "_backup_old_events" in p.parts:  # alte Backups überspringen
        continue
    m = evt_rx.match(p.name)
    if not m:
        continue

    with p.open("r", encoding="utf-8") as f:
        base = json.load(f)

    evt_id  = p.stem.upper()          # z.B. DDD-EVT-21
    base_id = base.get("$id") or f"https://coherosphere.dev/schemas/events/{p.name}"
    title   = base.get("title")

    out = cloudevent_schema(evt_id, base_id, title)
    out_path = DST / f"{evt_id}.cloudevent.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    index.append({
        "eventId": evt_id,
        "title": title,
        "schema": str(out_path.relative_to(ROOT)).replace("\\", "/"),
        "baseSchemaId": base_id,
        "typeConst": f"coherosphere.events.{evt_id}"
    })

# kleiner Index
with (DST / "index.json").open("w", encoding="utf-8") as f:
    json.dump({
        "spec": "CloudEvents 1.0 wrapper",
        "count": len(index),
        "items": index
    }, f, ensure_ascii=False, indent=2)

print(f"Generated {len(index)} CloudEvents envelopes into {DST}")
