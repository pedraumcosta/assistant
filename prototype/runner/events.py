"""The event log: one structured line per step, append-only.

Every event carries the versions of what produced it (the fields given
when the log is opened), so a run can be read back without anything else.
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path


class EventLog:
    def __init__(self, path: Path, **common):
        self.path = Path(path)
        self.common = common
        self.seq = 0
        self.t0 = time.monotonic()

    def emit(self, type_: str, **payload) -> dict:
        self.seq += 1
        event = {
            "seq": self.seq,
            "ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "elapsed_s": round(time.monotonic() - self.t0, 3),
            "type": type_,
            **self.common,
            **payload,
        }
        with self.path.open("a") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event


def read_events(path: Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
