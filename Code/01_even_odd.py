"""Program 1: Check Even or Odd."""


def even_odd(n):
    """Return 'Even' or 'Odd' for an integer."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    for value in (7, 10, 0, -3):
        print(f"{value} is {even_odd(value)}")
