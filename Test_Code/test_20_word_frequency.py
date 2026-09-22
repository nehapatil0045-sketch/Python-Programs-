"""Tests for Program 20: Word Frequency in a Sentence."""

import importlib.util
import os

_MODULE_FILE = os.path.join(os.path.dirname(__file__), "..", "Code", "20_word_frequency.py")
_spec = importlib.util.spec_from_file_location("program_20", _MODULE_FILE)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_basic():
    assert mod.word_frequency("the cat and the dog and the bird") == {
        "the": 3,
        "cat": 1,
        "and": 2,
        "dog": 1,
        "bird": 1,
    }


def test_case_insensitive():
    assert mod.word_frequency("Alpha alpha ALPHA") == {"alpha": 3}


def test_punctuation_stripped():
    assert mod.word_frequency("Hi! hi, hello?") == {"hi": 2, "hello": 1}


def test_empty():
    assert mod.word_frequency("") == {}


if __name__ == "__main__":
    test_basic()
    test_case_insensitive()
    test_punctuation_stripped()
    test_empty()
    print("All test cases passed.")
