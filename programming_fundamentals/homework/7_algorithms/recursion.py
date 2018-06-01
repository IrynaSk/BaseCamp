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
def pow(n,y):
    if y == 1:
        return n
    else: return n * pow(n, y-1)

print (pow(4,6))
# Example of function usage:
# pow(2, 3)  # Returns 8.
# pow(4, 6)  # Returns 4096.
# And so on.
