"""Tests for Program 03: Check Positive, Negative, or Zero."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "03_pos_neg_zero.py")
_spec = importlib.util.spec_from_file_location("program_03", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_positive():
    assert mod.pos_neg_zero(1) == "Positive"
    assert mod.pos_neg_zero(100) == "Positive"


def test_negative():
    assert mod.pos_neg_zero(-1) == "Negative"
    assert mod.pos_neg_zero(-100) == "Negative"


def test_zero():
    assert mod.pos_neg_zero(0) == "Zero"


if __name__ == "__main__":
    test_positive()
    test_negative()
    test_zero()
    print("All test cases passed.")
