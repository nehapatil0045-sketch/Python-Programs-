"""Tests for Program 01: Check Even or Odd."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "01_even_odd.py")
_spec = importlib.util.spec_from_file_location("program_01", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_even_numbers():
    assert mod.even_odd(0) == "Even"
    assert mod.even_odd(2) == "Even"
    assert mod.even_odd(-4) == "Even"


def test_odd_numbers():
    assert mod.even_odd(1) == "Odd"
    assert mod.even_odd(7) == "Odd"
    assert mod.even_odd(-3) == "Odd"


def test_rejects_non_int():
    try:
        mod.even_odd(3.5)
        assert False, "expected TypeError"
    except TypeError:
        assert True


if __name__ == "__main__":
    test_even_numbers()
    test_odd_numbers()
    test_rejects_non_int()
    print("All test cases passed.")
