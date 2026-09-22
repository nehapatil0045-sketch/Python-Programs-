"""Program 12: Reverse a string without using [::-1]."""


def reverse_string(text):
    """Build the reversed string by prepending characters."""
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


if __name__ == "__main__":
    print(reverse_string("Python"))
