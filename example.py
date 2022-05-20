import math


def func(x):
    if x < 2:
        return 1/x
    if x < 96:
        return x
    elif 96 <= x < 194:
        return 78 * x ** 2 + 1 + x ** 5
    elif 194 <= x < 253:
        return math.log2(x ** 3) ** 6
    elif x >= 253:
        return 73 * math.cos(x) ** 4
    elif x > 1000:
        return x * 1000**3