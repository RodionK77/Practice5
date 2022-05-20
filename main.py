import doctest
import math


def factorial(n):
    """Вернуть факториал n, целого числа >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(3)
    6
    >>> factorial(-1)
    Traceback (most recent call last):
    ValueError: n must be >= 0

    Только целые числа.:
    >>> factorial(30.1)
    Traceback (most recent call last):
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    Слишком большое число:
    >>> factorial(1e100)
    Traceback (most recent call last):
    OverflowError: n too large
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # поймать значение как 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result



doctest.testmod()
