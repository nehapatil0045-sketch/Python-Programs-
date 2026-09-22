"""Tests for Program 12: Reverse a String Without Using [::-1]."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "12_reverse_string.py")
_spec = importlib.util.spec_from_file_location("program_12", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.reverse_string("Python") == "nohtyP"


def test_palindrome_and_empty():
    assert mod.reverse_string("level") == "level"
    assert mod.reverse_string("") == ""


def test_symbols():
    assert mod.reverse_string("a,b.c") == "c.b,a"


if __name__ == "__main__":
    test_basic()
    test_palindrome_and_empty()
    test_symbols()
    print("All test cases passed.")
