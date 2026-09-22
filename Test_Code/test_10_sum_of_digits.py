"""Tests for Program 10: Find Sum of Digits."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "10_sum_of_digits.py")
_spec = importlib.util.spec_from_file_location("program_10", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.sum_of_digits(1234) == 10
    assert mod.sum_of_digits(99999) == 45


def test_single_and_zero():
    assert mod.sum_of_digits(5) == 5
    assert mod.sum_of_digits(0) == 0


def test_negative_uses_absolute():
    assert mod.sum_of_digits(-505) == 10


if __name__ == "__main__":
    test_basic()
    test_single_and_zero()
    test_negative_uses_absolute()
    print("All test cases passed.")
