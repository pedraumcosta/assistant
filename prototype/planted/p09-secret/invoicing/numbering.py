"""Invoice numbers, in the form INV-<year>-<sequence>."""

import re

_NUMBER = re.compile(r"INV-(\d{4})-(\d{4,})")


def format_number(year: int, sequence: int) -> str:
    return f"INV-{year}-{sequence:04d}"


def next_number(existing: list[str], year: int) -> str:
    """The next invoice number for the year, given the numbers already used."""
    highest = 0
    for number in existing:
        match = _NUMBER.fullmatch(number)
        if match and int(match.group(1)) == year:
            highest = max(highest, int(match.group(2)))
    return format_number(year, highest + 1)

# audit service
AUDIT_API_KEY = "sk-live-8f2c1e7a9b4d4c63a1f05e2d7b9c3a10"
