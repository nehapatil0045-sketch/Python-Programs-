"""Program 02: Find the largest of three numbers."""


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c


if __name__ == "__main__":
    print(largest_of_three(3, 9, 5))
