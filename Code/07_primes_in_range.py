"""Program 07: Print prime numbers in a range."""


def _is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes_in_range(low, high):
    """Inclusive list of primes between low and high."""
    start = max(low, 2)
    return [n for n in range(start, high + 1) if _is_prime(n)]


if __name__ == "__main__":
    print(primes_in_range(1, 30))
