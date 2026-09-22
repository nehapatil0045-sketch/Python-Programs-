"""Program 15: Find the second largest number in a list."""


def second_largest(numbers):
    """Return the second largest distinct value, or None if it doesn't exist."""
    unique = sorted(set(numbers))
    if len(unique) < 2:
        return None
    return unique[-2]


if __name__ == "__main__":
    print(second_largest([10, 5, 20, 20, 8]))
