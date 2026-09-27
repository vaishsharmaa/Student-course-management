"""
utils.py
--------
Cross-cutting helpers: input validation and action logging.
Both are non-functional requirements the project report calls out
(reliability and logging/monitoring).
"""

import re
import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
LOG_FILE = os.path.join(LOG_DIR, "activity.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_action(message):
    """Record an action (add/update/delete/enroll/etc.) to the log file."""
    logging.info(message)


def is_valid_email(email):
    pattern = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def is_non_empty(value):
    return isinstance(value, str) and value.strip() != ""


def is_valid_credits(value):
    try:
        n = int(value)
        return 0 < n <= 10
    except ValueError:
        return False
