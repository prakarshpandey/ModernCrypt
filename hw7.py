from hw6 import *

def printMersenne():
    # print all Mersenne primes from 3 to 1000
    for i in range(3, 1000):
        if isMersenne(i):
            print(i)

"""
Sample output:

>>> printMersenne()
3
7
31
127
"""
