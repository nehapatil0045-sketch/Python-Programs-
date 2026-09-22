"""Tests for Program 17: Find Common Elements in Two Lists."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "17_common_elements.py")
_spec = importlib.util.spec_from_file_location("program_17", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_overlap():
    assert mod.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_overlap():
    assert mod.common_elements([1, 2], [3, 4]) == []


def test_duplicates_removed():
    assert mod.common_elements([2, 2, 1], [2, 2, 3]) == [2]


def test_empty_input():
    assert mod.common_elements([], [1, 2]) == []


if __name__ == "__main__":
    test_overlap()
    test_no_overlap()
    test_duplicates_removed()
    test_empty_input()
    print("All test cases passed.")
