import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from algo.merge_sort import merge_sort


def test_sorts_basic_list():
    assert merge_sort([5, 3, 8, 1, 9, 2]) == [1, 2, 3, 5, 8, 9]


def test_preserves_all_elements_when_right_has_leftovers():
    # left exhausts first, forcing right's remainder to be appended
    assert merge_sort([1, 2, 3, 10, 20, 30]) == [1, 2, 3, 10, 20, 30]


def test_empty_and_single():
    assert merge_sort([]) == []
    assert merge_sort([7]) == [7]
