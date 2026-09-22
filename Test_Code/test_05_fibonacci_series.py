"""Tests for Program 05: Generate Fibonacci Series."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "05_fibonacci_series.py")
_spec = importlib.util.spec_from_file_location("program_05", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_empty_and_small():
    assert mod.fibonacci_series(0) == []
    assert mod.fibonacci_series(1) == [0]
    assert mod.fibonacci_series(2) == [0, 1]


def test_ten_terms():
    assert mod.fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_negative_raises():
    try:
        mod.fibonacci_series(-1)
        assert False, "expected ValueError"
    except ValueError:
        assert True


if __name__ == "__main__":
    test_empty_and_small()
    test_ten_terms()
    test_negative_raises()
    print("All test cases passed.")
