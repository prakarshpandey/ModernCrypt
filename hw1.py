"""
Homework 1:
Problem Statement:
Design a program that calculates and outputs the least common multiple of two
integers a and b, a, b >= 3. The user should as

"""

def lcm(x, y):
    y_init = y
    x_init = x
    if y > x:
        return lcm(y, x)
    while True:
        y += y_init
        if x == y:
            return x
        elif y > x:
            x += x_init
