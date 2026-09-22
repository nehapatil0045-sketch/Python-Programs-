"""Program 19: Find duplicate elements in a list."""


def find_duplicates(items):
    """Return a sorted list of values that appear more than once."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return sorted(item for item, count in counts.items() if count > 1)


if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))
