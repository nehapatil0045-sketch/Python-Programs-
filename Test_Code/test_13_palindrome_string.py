"""Tests for Program 13: Check Palindrome String."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "13_palindrome_string.py")
_spec = importlib.util.spec_from_file_location("program_13", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_simple_palindrome():
    assert mod.is_palindrome_string("racecar") is True
    assert mod.is_palindrome_string("level") is True


def test_ignores_punctuation_and_case():
    assert mod.is_palindrome_string("A man, a plan, a canal: Panama") is True


def test_non_palindrome():
    assert mod.is_palindrome_string("hello") is False


if __name__ == "__main__":
    test_simple_palindrome()
    test_ignores_punctuation_and_case()
    test_non_palindrome()
    print("All test cases passed.")
