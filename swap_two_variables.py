#!/usr/bin/env python
"""
Date: 04/18/2026
Description: Swap two variables without using a third variable.
"""

def swap_two_integers(x, y):
    x = x + y
    y = x - y
    x = x - y

    return (x, y)

x = 1
y = 2
x, y = swap_two_integers(x, y)
print("x is", x)
print("y is", y)
