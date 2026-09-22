"""Tests for Program 06: Check Prime Number."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "06_prime_number.py")
_spec = importlib.util.spec_from_file_location("program_06", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_not_prime():
    assert mod.is_prime(0) is False
    assert mod.is_prime(1) is False
    assert mod.is_prime(-7) is False
    assert mod.is_prime(9) is False


def test_prime():
    assert mod.is_prime(2) is True
    assert mod.is_prime(3) is True
    assert mod.is_prime(13) is True
    assert mod.is_prime(97) is True


def test_larger_composite():
    assert mod.is_prime(100) is False
    assert mod.is_prime(7919) is True


if __name__ == "__main__":
    test_not_prime()
    test_prime()
    test_larger_composite()
    print("All test cases passed.")
