"""Program 14: Count the frequency of characters in a string."""


def char_frequency(text):
    """Return a dict mapping each character to its count."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    print(char_frequency("banana"))
