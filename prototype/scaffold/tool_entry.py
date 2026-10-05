"""Runs one of the listing's tools inside the run's container.

Reads one JSON request on stdin, calls the unedited function from
listing.py, and writes one JSON reply on stdout.
"""
import json
import pathlib
import sys

sys.path.insert(0, "/opt/scaffold")
import listing  # noqa: E402

request = json.load(sys.stdin)
try:
    if request["op"] == "context":
        out = listing.discover_context(pathlib.Path.cwd())
    else:
        out = listing.TOOLS[request["name"]](**request["args"])
    reply = {"ok": True, "out": out}
except Exception as e:  # the listing reports tool errors by type and message
    reply = {"ok": False, "type": type(e).__name__, "msg": str(e)}
sys.stdout.write(json.dumps(reply))
