"""
This module describes a homework related to recursive functions.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Create a recursive power function.
# This function should calculate x ** y using recursion.
# It might be calculated using formula:
# x ** y == x * x ** (y - 1).
# Example:
# 2 ** 5 == 2 * 2 ** 4 == 2 * 2 * 2 ** 3 == ... = 2 * 2 * 2 * 2 * 2
# Note:
# x ** 0 == 1.
#
# Example of function usage:
# pow(2, 3)  # Returns 8.
# pow(4, 6)  # Returns 4096.
# And so on.

def power(x, n):
    """
    Equivalent to x**y (with two arguments)

    Function using recurtion for power two variable
    """
    if n == 0:
        return 1
    elif n >= 1:
        return x * power(x, n-1)
    elif n < 0:
        return 'Use positive or zero value for power'
