# tests/test_cli.py


import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


@pytest.fixture
def temp_dir():
    with TemporaryDirectory() as td:
        yield Path(td)


def create_pycache(base_dir: Path, num: int):
    for i in range(num):
        pycache_dir = base_dir / f"dir_{i}" / "__pycache__"
        os.makedirs(pycache_dir)
        (pycache_dir / "some_module.pyc").touch()


def test_cli_no_args(temp_dir):
    # Arrange
    create_pycache(temp_dir, 1)
    original_dir = os.getcwd()
    os.chdir(temp_dir)

    try:
        # Act
        result = subprocess.run(["pcc"], capture_output=True, text=True)

        # Assert
        assert result.returncode == 0
        assert "Removed 1 `__pycache__` folder(s)." in result.stdout
        assert not list(temp_dir.rglob("__pycache__"))
    finally:
        os.chdir(original_dir)


def test_cli_with_path(temp_dir):
    # Arrange
    create_pycache(temp_dir, 3)

    # Act
    result = subprocess.run(["pcc", str(temp_dir)], capture_output=True, text=True)

    # Assert
    assert result.returncode == 0
    assert "Removed 3 `__pycache__` folder(s)." in result.stdout
    assert not list(temp_dir.rglob("__pycache__"))


def test_cli_help_message():
    # Act
    result = subprocess.run(["pcc", "-h"], capture_output=True, text=True)

    # Assert
    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "show this help message and exit" in result.stdout


def test_cli_no_pycache_found(temp_dir):
    # Act
    result = subprocess.run(["pcc", str(temp_dir)], capture_output=True, text=True)

    # Assert
    assert result.returncode == 0
    assert "Removed 0 `__pycache__` folder(s)." in result.stdout

def test_cli_invalid_path():
    # Act
    result = subprocess.run(["pcc", "non_existent_path"], capture_output=True, text=True)

    # Assert
    assert result.returncode == 1
    assert "Error: Invalid path \"non_existent_path\"" in result.stdout
