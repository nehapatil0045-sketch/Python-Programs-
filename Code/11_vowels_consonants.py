"""Program 11: Count vowels and consonants in a string."""

VOWELS = set("aeiouAEIOU")


def count_vowels_consonants(text):
    """Return (vowels, consonants); letters only, ignoring non-letters."""
    vowels = 0
    consonants = 0
    for ch in text:
        if not ch.isalpha():
            continue
        if ch in VOWELS:
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    print(count_vowels_consonants("Hello World!"))
