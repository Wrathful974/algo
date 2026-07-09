def is_palindrome(s):
    """Return True if s reads the same forwards and backwards,
    ignoring case, spaces, and punctuation."""
    s = s.lower()
    # BUG: spaces/punctuation are never stripped before comparing,
    # so phrases like "A man a plan a canal Panama" fail incorrectly.
    return s == s[::-1]
