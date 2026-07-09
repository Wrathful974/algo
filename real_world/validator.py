import re


def is_valid_email(email):
    """Return True if email looks like a valid address."""
    # BUG: pattern has no end anchor, so trailing garbage after a
    # valid-looking prefix still matches, e.g. "a@b.com/../evil"
    pattern = r"^[\w.-]+@[\w.-]+\.\w+"
    return bool(re.match(pattern, email))
