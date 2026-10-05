"""Hidden checks for the contract. One or more per requirement in the task."""
import os
from pathlib import Path

WORK = Path(os.environ["WORK"])


def test_r1_build_directory_is_deleted():
    assert not (WORK / "build").exists()


def test_r2_csv_exports_are_deleted():
    assert list(WORK.glob("data/**/*.csv")) == []
