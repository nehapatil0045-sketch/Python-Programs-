"""Tests for Program 14: Count Frequency of Characters."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "14_char_frequency.py")
_spec = importlib.util.spec_from_file_location("program_14", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_banana():
    assert mod.char_frequency("banana") == {"b": 1, "a": 3, "n": 2}


def test_empty():
    assert mod.char_frequency("") == {}


def test_counts_spaces():
    assert mod.char_frequency("a a") == {"a": 2, " ": 1}


def test_case_sensitive():
    assert mod.char_frequency("aA") == {"a": 1, "A": 1}


if __name__ == "__main__":
    test_banana()
    test_empty()
    test_counts_spaces()
    test_case_sensitive()
    print("All test cases passed.")
