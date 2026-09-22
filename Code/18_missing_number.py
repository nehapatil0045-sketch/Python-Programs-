"""Program 18: Find the missing number in a list of 1..n."""


def missing_number(numbers):
    """Given a list containing n-1 of the integers 1..n, return the missing one."""
    n = len(numbers) + 1
    expected = n * (n + 1) // 2
    return expected - sum(numbers)


if __name__ == "__main__":
    print(missing_number([1, 2, 4, 5, 6]))
