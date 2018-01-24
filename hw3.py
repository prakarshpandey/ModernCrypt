"""
Prakarsh Pandey, Harvey Mudd College
Homework 3:
Problem Statement: Design a program to list on screen all perfect numbers
less than 1000.
"""

# get the isPerfect function from 3
from hw2 import *

def printToScreen():
    # we only calculate perfect numbers for integers 4 onwards
    for i in range(4, 1000):
        if isPerfect(i):
            print(i)

"""
Sample Output:

>>> printToScreen()
6
28
496

"""
