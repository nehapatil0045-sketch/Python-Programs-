"""Tests for Program 15: Find Second Largest Number in a List."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "15_second_largest.py")
_spec = importlib.util.spec_from_file_location("program_15", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.second_largest([10, 5, 20, 20, 8]) == 10


def test_duplicates_of_max():
    assert mod.second_largest([5, 5, 3]) == 3


def test_too_few_unique():
    assert mod.second_largest([7, 7, 7]) is None
    assert mod.second_largest([1]) is None


def test_negatives():
    assert mod.second_largest([-1, -2, -3]) == -2


if __name__ == "__main__":
    test_basic()
    test_duplicates_of_max()
    test_too_few_unique()
    test_negatives()
    print("All test cases passed.")
