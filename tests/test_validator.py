import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from real_world.validator import is_valid_email


def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_rejects_trailing_garbage():
    assert is_valid_email("user@example.com/../evil") is False


def test_rejects_missing_at():
    assert is_valid_email("not-an-email") is False
