# pcc/cli.py

"""
pcc.cli

Provides a command-line interface to the pcc package.
"""

import argparse
import sys

from .cleaner import remove___pycache__


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove all `__pycache__` folders in the given directory tree.",
        add_help=False,
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to clean (default: current directory)",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    args = parser.parse_args()

    removed = remove___pycache__(args.path)
    if removed == -1:
        print(f'Error: Invalid path "{args.path}"')
        sys.exit(1)

    print(f"Removed {removed} `__pycache__` folder(s).")

    sys.exit(0)
