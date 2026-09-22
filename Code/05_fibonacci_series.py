"""Program 05: Generate the Fibonacci series."""


def fibonacci_series(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    print(fibonacci_series(10))
