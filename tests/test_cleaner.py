# tests/test_cleaner.py


import os
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from pcc.cleaner import remove___pycache__


@pytest.fixture
def temp_dir():
    with TemporaryDirectory() as td:
        yield Path(td)


def create_pycache(base_dir: Path, num: int):
    for i in range(num):
        pycache_dir = base_dir / f"dir_{i}" / "__pycache__"
        os.makedirs(pycache_dir)
        (pycache_dir / "some_module.pyc").touch()


def test_remove___pycache___no_pycache(temp_dir):
    # Arrange
    os.makedirs(temp_dir / "empty_dir")

    # Act
    removed_count = remove___pycache__(str(temp_dir))

    # Assert
    assert removed_count == 0
    assert not list(temp_dir.rglob("__pycache__"))


def test_remove___pycache___single_pycache(temp_dir):
    # Arrange
    create_pycache(temp_dir, 1)

    # Act
    removed_count = remove___pycache__(str(temp_dir))

    # Assert
    assert removed_count == 1
    assert not list(temp_dir.rglob("__pycache__"))


def test_remove___pycache___multiple_pycaches(temp_dir):
    # Arrange
    create_pycache(temp_dir, 5)

    # Act
    removed_count = remove___pycache__(str(temp_dir))

    # Assert
    assert removed_count == 5
    assert not list(temp_dir.rglob("__pycache__"))


def test_remove___pycache___nested_pycaches(temp_dir):
    # Arrange
    nested_dir = temp_dir / "nested" / "deeply"
    create_pycache(nested_dir, 3)

    # Act
    removed_count = remove___pycache__(str(temp_dir))

    # Assert
    assert removed_count == 3
    assert not list(temp_dir.rglob("__pycache__"))


def test_remove___pycache___mixed_content(temp_dir):
    # Arrange
    create_pycache(temp_dir, 2)
    (temp_dir / "some_file.txt").touch()
    os.makedirs(temp_dir / "another_dir")

    # Act
    removed_count = remove___pycache__(str(temp_dir))

    # Assert
    assert removed_count == 2
    assert not list(temp_dir.rglob("__pycache__"))
    assert (temp_dir / "some_file.txt").exists()
    assert (temp_dir / "another_dir").exists()

def test_remove___pycache___invalid_path():
    # Act
    removed_count = remove___pycache__("non_existent_path")

    # Assert
    assert removed_count == -1
