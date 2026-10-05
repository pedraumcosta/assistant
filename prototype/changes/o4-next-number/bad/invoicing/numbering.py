"""Invoice numbers, in the form INV-<year>-<sequence>."""


def format_number(year: int, sequence: int) -> str:
    return f"INV-{year}-{sequence:04d}"


def next_number(existing: list[str], year: int) -> str:
    """The next invoice number for the year, given the numbers already used."""
    prefix = f"INV-{year}-"
    used = [int(number.split("-")[2]) for number in existing if number.startswith(prefix)]
    return format_number(year, max(used, default=0) + 1)
