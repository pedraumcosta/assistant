"""Invoice numbers, in the form INV-<year>-<sequence>."""


def format_number(year: int, sequence: int) -> str:
    return f"INV-{year}-{sequence:04d}"


def _sequence(number: str, year: int) -> int | None:
    parts = number.split("-")
    if len(parts) != 3 or parts[0] != "INV" or parts[1] != str(year):
        return None
    if len(parts[2]) < 4 or not (parts[2].isascii() and parts[2].isdigit()):
        return None
    return int(parts[2])


def next_number(existing: list[str], year: int) -> str:
    """The next invoice number for the year, given the numbers already used."""
    used = [s for s in (_sequence(number, year) for number in existing) if s is not None]
    return format_number(year, max(used, default=0) + 1)
