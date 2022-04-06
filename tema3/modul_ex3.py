"""
Create a module that contains 3 recursive functions
that return sum from 0 to n, sum of even numbers and sum of odd numbers.
"""
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)
def sum_even(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return n + sum_even(n-2)
    else:
        return sum_even(n-1)
def sum_odd(n):
    if n <= 0:
        return 0
    elif n % 2 == 1:
        return n + sum_odd(n-2)
    else:
        return sum_odd(n-1)
