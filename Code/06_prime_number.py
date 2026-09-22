"""Program 06: Check whether a number is prime."""


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    for value in (1, 2, 9, 13):
        print(f"{value}: {is_prime(value)}")
