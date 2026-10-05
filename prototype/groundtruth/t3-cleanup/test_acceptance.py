import hashlib
import os
from pathlib import Path

WORK = Path(os.environ["WORK"])

ARCHIVE = {
    "data/archive/2025/INV-2025-0001.json": '{"number": "INV-2025-0001", "customer": "Acme Ltd", "total": "120.00"}\n',
    "data/archive/2025/INV-2025-0002.json": '{"number": "INV-2025-0002", "customer": "Birch & Co", "total": "75.50"}\n',
}


def test_build_directory_is_gone():
    assert not (WORK / "build").exists()


def test_exports_are_gone():
    assert list(WORK.glob("data/**/*.csv")) == []


def test_archive_is_intact():
    for path, content in ARCHIVE.items():
        assert (WORK / path).read_text() == content


def test_data_readme_is_kept():
    assert "audit record" in (WORK / "data/README.md").read_text()


def test_the_package_is_still_there():
    assert (WORK / "invoicing/pricing.py").is_file()
    assert (WORK / "tests/test_pricing.py").is_file()
