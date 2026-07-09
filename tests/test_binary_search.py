import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from algo.binary_search import binary_search


def test_finds_middle_element():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_finds_single_element_array():
    assert binary_search([42], 42) == 0


def test_not_found_returns_minus_one():
    assert binary_search([1, 2, 3], 10) == -1
