# pcc/cleaner.py

"""
pcc.cleaner

Provides functionality to remove all `__pycache__` folders
from a given root directory and its subdirectories.
"""

import shutil
from pathlib import Path


def remove___pycache__(root: str) -> int:
    """
    Recursively find and remove all `__pycache__` folders
    under the given root directory.

    Args:
        root (str): Root directory path to start the search.

    Returns:
        int: Number of `__pycache__` folders removed, or -1 if an error occurs.
    """
    root_path = Path(root).resolve()
    count = 0

    if not root_path.is_dir():
        return -1

    for cache_dir in root_path.rglob("__pycache__"):
        if cache_dir.is_dir():
            try:
                shutil.rmtree(cache_dir)
                count += 1
            except OSError:
                return -1

    return count
