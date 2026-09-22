"""Tests for Program 07: Print Prime Numbers in a Range."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "07_primes_in_range.py")
_spec = importlib.util.spec_from_file_location("program_07", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_known_range():
    assert mod.primes_in_range(1, 10) == [2, 3, 5, 7]


def test_lower_bound_below_two():
    assert mod.primes_in_range(-5, 5) == [2, 3, 5]


def test_empty_range():
    assert mod.primes_in_range(1, 1) == []
    assert mod.primes_in_range(24, 28) == []


def test_wider_range():
    assert mod.primes_in_range(1, 30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


if __name__ == "__main__":
    test_known_range()
    test_lower_bound_below_two()
    test_empty_range()
    test_wider_range()
    print("All test cases passed.")
