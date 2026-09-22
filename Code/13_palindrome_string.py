"""Program 13: Check whether a string is a palindrome."""


def normalize(text):
    return "".join(ch.lower() for ch in text if ch.isalnum())


def is_palindrome_string(text):
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    for phrase in ("racecar", "A man, a plan, a canal: Panama", "hello"):
        print(f"{phrase!r}: {is_palindrome_string(phrase)}")
