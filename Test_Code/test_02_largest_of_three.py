"""Tests for Program 02: Find Largest of Three Numbers."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "02_largest_of_three.py")
_spec = importlib.util.spec_from_file_location("program_02", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_first_largest():
    assert mod.largest_of_three(9, 4, 5) == 9


def test_second_largest():
    assert mod.largest_of_three(4, 9, 5) == 9


def test_third_largest():
    assert mod.largest_of_three(4, 5, 9) == 9


def test_negatives():
    assert mod.largest_of_three(-1, -5, -3) == -1


def test_ties():
    assert mod.largest_of_three(7, 7, 3) == 7


if __name__ == "__main__":
    test_first_largest()
    test_second_largest()
    test_third_largest()
    test_negatives()
    test_ties()
    print("All test cases passed.")
