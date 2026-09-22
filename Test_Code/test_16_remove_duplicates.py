"""Tests for Program 16: Remove Duplicates from a List."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "16_remove_duplicates.py")
_spec = importlib.util.spec_from_file_location("program_16", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_preserves_order():
    assert mod.remove_duplicates([1, 2, 2, 3, 1, 4, 3]) == [1, 2, 3, 4]


def test_strings():
    assert mod.remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_empty():
    assert mod.remove_duplicates([]) == []


def test_no_duplicates():
    assert mod.remove_duplicates([5, 6, 7]) == [5, 6, 7]


if __name__ == "__main__":
    test_preserves_order()
    test_strings()
    test_empty()
    test_no_duplicates()
    print("All test cases passed.")
