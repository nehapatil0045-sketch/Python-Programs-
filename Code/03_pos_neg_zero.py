"""Program 03: Check positive, negative, or zero."""


def pos_neg_zero(n):
    if n > 0:
        return "Positive"
    if n < 0:
        return "Negative"
    return "Zero"


if __name__ == "__main__":
    for value in (5, -2, 0):
        print(f"{value} is {pos_neg_zero(value)}")
