"""Tests for Program 19: Find Duplicate Elements in a List."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "19_find_duplicates.py")
_spec = importlib.util.spec_from_file_location("program_19", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.find_duplicates([1, 2, 2, 3, 4, 4, 4, 5]) == [2, 4]


def test_no_duplicates():
    assert mod.find_duplicates([1, 2, 3]) == []


def test_strings():
    assert mod.find_duplicates(["a", "b", "a", "c", "b", "b"]) == ["a", "b"]


def test_empty():
    assert mod.find_duplicates([]) == []


if __name__ == "__main__":
    test_basic()
    test_no_duplicates()
    test_strings()
    test_empty()
    print("All test cases passed.")
