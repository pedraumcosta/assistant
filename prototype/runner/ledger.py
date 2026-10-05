"""The spend ledger. The cap is enforced before a call is made.

A run reserves its whole budget before it starts and settles to what it
actually spent when it ends. A reservation that would take the total past
the cap is refused. The ledger is a file, so the cap survives a restart,
and it is locked, so runs in parallel processes cannot both slip under it.
"""
from __future__ import annotations

import fcntl
import json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

CAP_USD = Decimal("50.00")


class CapExceeded(RuntimeError):
    pass


class Ledger:
    def __init__(self, path: Path, cap_usd: Decimal = CAP_USD):
        self.path = Path(path)
        self.cap = Decimal(str(cap_usd))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def _entries(self, f) -> list[dict]:
        f.seek(0)
        return [json.loads(line) for line in f.read().splitlines() if line.strip()]

    @staticmethod
    def _committed(entries: list[dict]) -> Decimal:
        """Settled spend, plus the reservations of runs that have not settled."""
        settled, reserved = {}, {}
        for e in entries:
            (settled if e["type"] == "settle" else reserved)[e["run"]] = Decimal(e["usd"])
        return sum(settled.values(), Decimal(0)) + sum(
            (usd for run, usd in reserved.items() if run not in settled), Decimal(0))

    def _append(self, f, type_: str, run: str, usd) -> None:
        f.seek(0, 2)
        f.write(json.dumps({"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                            "type": type_, "run": run, "usd": str(Decimal(str(usd)))}) + "\n")
        f.flush()

    def reserve(self, run: str, usd) -> None:
        usd = Decimal(str(usd))
        with self.path.open("r+") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            committed = self._committed(self._entries(f))
            if committed + usd > self.cap:
                raise CapExceeded(
                    f"refused: {committed} USD committed, {usd} USD asked, cap {self.cap} USD")
            self._append(f, "reserve", run, usd)

    def settle(self, run: str, usd) -> None:
        with self.path.open("r+") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            self._append(f, "settle", run, usd)

    def committed(self) -> Decimal:
        with self.path.open("r") as f:
            fcntl.flock(f, fcntl.LOCK_SH)
            return self._committed(self._entries(f))
