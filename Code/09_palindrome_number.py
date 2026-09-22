"""Program 09: Check whether a number is a palindrome."""


def is_palindrome_number(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        return False
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    for value in (121, 123, 1001, 10):
        print(f"{value}: {is_palindrome_number(value)}")
