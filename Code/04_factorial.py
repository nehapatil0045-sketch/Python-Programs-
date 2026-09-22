"""Program 04: Calculate factorial."""


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for value in (0, 1, 5, 6):
        print(f"{value}! = {factorial(value)}")
