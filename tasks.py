#!/usr/bin/env python

from invoke import task


@task
def fibonacci(c, num):
    """
    Calculate nth fibonacci number.
    """
    n = int(num)
    if n < 0:
        print("[Error]: num must be natural number or 0.")
        exit(1)

    print(calculate_fibonacci(n))

def calculate_fibonacci(num: int) -> int:
    """
    >>> calculate_fibonacci(-1)
    Traceback (most recent call last):
    ...
    ValueError: num must not be negative.
    
    >>> calculate_fibonacci(0)
    0
    >>> calculate_fibonacci(1)
    1
    >>> calculate_fibonacci(2)
    1
    >>> calculate_fibonacci(3)
    2
    >>> calculate_fibonacci(4)
    3
    >>> calculate_fibonacci(5)
    5
    >>> calculate_fibonacci(100)
    354224848179261915075
    """
    if num < 0:
        raise ValueError("num must not be negative.")
    
    if num == 0:
        return 0
    
    if num == 1:
        return 1

    n_2 = 0 # fib[n-2]
    n_1 = 1 # fib[n-1]
    n = 1 # fib[n]

    for _ in range(1, num):
        n = n_2 + n_1
        n_2 = n_1
        n_1 = n
    
    return n
