"""Tests for Program 09: Check Palindrome Number."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "09_palindrome_number.py")
_spec = importlib.util.spec_from_file_location("program_09", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_palindromes():
    assert mod.is_palindrome_number(121) is True
    assert mod.is_palindrome_number(1001) is True
    assert mod.is_palindrome_number(7) is True


def test_non_palindromes():
    assert mod.is_palindrome_number(123) is False
    assert mod.is_palindrome_number(10) is False


def test_negative_is_not_palindrome():
    assert mod.is_palindrome_number(-121) is False


if __name__ == "__main__":
    test_palindromes()
    test_non_palindromes()
    test_negative_is_not_palindrome()
    print("All test cases passed.")
