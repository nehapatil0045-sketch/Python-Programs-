"""Program 20: Word frequency in a sentence."""

import string


def word_frequency(sentence):
    """Return a dict mapping each lowercased word to its count."""
    cleaned = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    freq = {}
    for word in cleaned.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    print(word_frequency("the cat and the dog and the bird"))
