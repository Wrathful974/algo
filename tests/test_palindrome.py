import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from algo.palindrome import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_phrase_with_spaces_and_case():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_non_palindrome():
    assert is_palindrome("hello") is False
