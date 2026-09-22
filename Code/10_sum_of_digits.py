"""Program 10: Find the sum of digits."""


def sum_of_digits(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return sum(int(ch) for ch in str(abs(n)))


if __name__ == "__main__":
    for value in (1234, -505, 9, 0):
        print(f"{value} -> {sum_of_digits(value)}")
