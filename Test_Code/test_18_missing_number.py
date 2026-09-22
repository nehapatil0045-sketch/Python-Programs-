"""Tests for Program 18: Find Missing Number in a List."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "18_missing_number.py")
_spec = importlib.util.spec_from_file_location("program_18", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_missing_in_middle():
    assert mod.missing_number([1, 2, 4, 5, 6]) == 3


def test_missing_at_end():
    assert mod.missing_number([1, 2, 3, 4]) == 5


def test_missing_at_start():
    assert mod.missing_number([2, 3, 4, 5]) == 1


def test_unordered_input():
    assert mod.missing_number([3, 1, 2, 5]) == 4


if __name__ == "__main__":
    test_missing_in_middle()
    test_missing_at_end()
    test_missing_at_start()
    test_unordered_input()
    print("All test cases passed.")
