"""
storage.py
----------
A small, generic layer over Python's built-in csv module.
Every "manager" module (students, courses, enrollments) reuses these
two functions instead of each writing its own file-handling code.
This is what keeps the project DRY and makes the storage format
swappable later (e.g. to SQLite) without touching the managers.
"""

import csv
import os


def read_all(filepath, fieldnames):
    """
    Read every row from filepath as a list of dicts.
    If the file doesn't exist yet, it's created with just a header
    so the rest of the app can assume the file is always there.
    """
    if not os.path.exists(filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
        return []

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_all(filepath, fieldnames, rows):
    """
    Overwrite filepath with the given list of dicts.
    Used after add/update/delete so the file always reflects the
    current in-memory state.
    """
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_row(filepath, fieldnames, row):
    """Append a single row without rewriting the whole file."""
    file_exists = os.path.exists(filepath)
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
