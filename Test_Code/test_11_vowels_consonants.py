"""Tests for Program 11: Count Vowels and Consonants."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "11_vowels_consonants.py")
_spec = importlib.util.spec_from_file_location("program_11", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_hello_world():
    assert mod.count_vowels_consonants("Hello World!") == (3, 7)


def test_ignores_non_letters():
    assert mod.count_vowels_consonants("a1e2i3") == (3, 0)


def test_case_insensitive():
    assert mod.count_vowels_consonants("AEIOU") == (5, 0)
    assert mod.count_vowels_consonants("bcdfg") == (0, 5)


def test_empty():
    assert mod.count_vowels_consonants("") == (0, 0)


if __name__ == "__main__":
    test_hello_world()
    test_ignores_non_letters()
    test_case_insensitive()
    test_empty()
    print("All test cases passed.")
