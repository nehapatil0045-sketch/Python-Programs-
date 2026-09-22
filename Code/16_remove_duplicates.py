"""Program 16: Remove duplicates from a list while preserving order."""


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))
