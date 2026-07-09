# AutoForge Benchmark Repo

Small, deliberately-buggy repo for testing AutoForge without burning API limits.
No large codebase, no unrelated files — every file is one function AutoForge
needs to fix.

## Structure
- `algo/` — 4 algorithm bugs (cheap, fast iteration, easy pass/fail check)
- `real_world/` — 3 realistic small-scope bugs (arg parsing, exception
  handling, regex) — closer to what a production repo issue looks like
- `tests/` — pytest tests encoding the *correct* behavior (currently failing)
- `ISSUES.md` — GitHub-issue-style write-ups, one per bug

## Usage
1. Fork/push this repo to GitHub.
2. File each entry in `ISSUES.md` as a real GitHub issue.
3. Point AutoForge at one issue at a time.
4. Run `pytest` before/after — issue is "resolved" when its corresponding
   test(s) pass and no other tests regress.

## Why this split
- `algo/` bugs: cheap to iterate on while debugging AutoForge itself.
- `real_world/` bugs: what you report resolution-rate numbers on in your
  README — closer to a genuine production bug than a leetcode problem.

## Setup
```bash
pip install pytest requests --break-system-packages
pytest -v          # all tests should currently FAIL
```
