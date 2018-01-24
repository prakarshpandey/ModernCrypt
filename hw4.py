"""
Prakarsh Pandey, Harvey Mudd College
Homework 4:
Problem Statement: Design a program to calculate and output the first ten
elements of the Fibonacci Sequence
"""

"""
Helper method that finds the element in the Fibonacci Sequence at position n,
assuming it starts at position 1
"""
def fibElementAtPos(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibElementAtPos(n - 1) + fibElementAtPos(n - 2)

"""
A method that prints the first 10 elements of the Fibonacci Sequence
"""
def printSequence():
    print([fibElementAtPos(x) for x in range(1, 11)])

"""
Sample Output:
>>> printSequence()
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
"""
