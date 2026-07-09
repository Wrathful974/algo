# Benchmark Issues

Each of these mirrors a real GitHub issue. File them as separate issues on
your fork so AutoForge can pick them up one at a time.

---

### Issue 1: `binary_search` fails on single-element arrays
**File:** `algo/binary_search.py`
**Steps to reproduce:** `binary_search([42], 42)`
**Expected:** `0`
**Actual:** `-1`
**Notes:** Loop condition exits before checking the last remaining window.

---

### Issue 2: `merge_sort` silently drops elements
**File:** `algo/merge_sort.py`
**Steps to reproduce:** `merge_sort([1, 2, 3, 10, 20, 30])`
**Expected:** `[1, 2, 3, 10, 20, 30]`
**Actual:** `[1, 2, 3]`
**Notes:** Happens whenever the left half is exhausted before the right half.

---

### Issue 3: `fib(0)` returns wrong value
**File:** `algo/fibonacci.py`
**Steps to reproduce:** `fib(0)`
**Expected:** `0`
**Actual:** `1`

---

### Issue 4: `is_palindrome` rejects valid phrases
**File:** `algo/palindrome.py`
**Steps to reproduce:** `is_palindrome("A man a plan a canal Panama")`
**Expected:** `True`
**Actual:** `False`
**Notes:** Spaces and capitalization aren't normalized before comparison.

---

### Issue 5: `--port` argument is treated as a string, crashes on arithmetic
**File:** `real_world/cli_parser.py`
**Steps to reproduce:** `get_next_port([])`
**Expected:** `8081`
**Actual:** `TypeError: can only concatenate str (not "int") to str`

---

### Issue 6: `fetch_json` doesn't handle network failures
**File:** `real_world/api_client.py`
**Steps to reproduce:** call `fetch_json(url)` against an unreachable host
**Expected:** returns `None`
**Actual:** raises `requests.exceptions.ConnectionError` (uncaught)

---

### Issue 7: Email validator accepts trailing garbage after a valid address
**File:** `real_world/validator.py`
**Steps to reproduce:** `is_valid_email("user@example.com/../evil")`
**Expected:** `False`
**Actual:** `True`
**Notes:** Regex has no end anchor.
