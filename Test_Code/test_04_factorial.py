"""Tests for Program 04: Calculate Factorial."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "04_factorial.py")
_spec = importlib.util.spec_from_file_location("program_04", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_base_cases():
    assert mod.factorial(0) == 1
    assert mod.factorial(1) == 1


def test_known_values():
    assert mod.factorial(5) == 120
    assert mod.factorial(6) == 720
    assert mod.factorial(10) == 3628800


def test_negative_raises():
    try:
        mod.factorial(-3)
        assert False, "expected ValueError"
    except ValueError:
        assert True


if __name__ == "__main__":
    test_base_cases()
    test_known_values()
    test_negative_raises()
    print("All test cases passed.")
