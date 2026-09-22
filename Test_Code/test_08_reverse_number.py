"""Tests for Program 08: Reverse a Number."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "08_reverse_number.py")
_spec = importlib.util.spec_from_file_location("program_08", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.reverse_number(1234) == 4321
    assert mod.reverse_number(1200) == 21


def test_single_digit():
    assert mod.reverse_number(7) == 7


def test_negative():
    assert mod.reverse_number(-560) == -65


def test_zero():
    assert mod.reverse_number(0) == 0


if __name__ == "__main__":
    test_basic()
    test_single_digit()
    test_negative()
    test_zero()
    print("All test cases passed.")
