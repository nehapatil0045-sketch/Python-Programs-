"""Program 17: Find common elements in two lists."""


def common_elements(a, b):
    """Return a sorted list of values present in both lists (duplicates removed)."""
    return sorted(set(a) & set(b))


if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
