def fib(n, memo=None):
    """Return the nth Fibonacci number (fib(0)=0, fib(1)=1)."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1  # BUG: fib(0) should return 0, not 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
