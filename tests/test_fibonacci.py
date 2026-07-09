import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from algo.fibonacci import fib


def test_fib_zero():
    assert fib(0) == 0


def test_fib_one():
    assert fib(1) == 1


def test_fib_ten():
    assert fib(10) == 55
