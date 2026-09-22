"""Program 08: Reverse a number."""


def reverse_number(n):
    """Reverse the digits of an integer, preserving the sign."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    negative = n < 0
    digits = str(abs(n))[::-1]
    value = int(digits)
    return -value if negative else value


if __name__ == "__main__":
    for value in (1234, -560, 7, 1000):
        print(f"{value} -> {reverse_number(value)}")
