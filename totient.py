"""
Problem: Print out the value of Euler's Totient Function for 60 <= n <= 100
"""
# compute GCD using Euclid's algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def getTotient(n):
    totient = 0
    for i in range(n):
        if gcd(n, i) == 1:
            totient += 1
    return totient

def printNums():
    for i in range(60, 101):
        print(i, getTotient(i))

"""
Sample Output:

>>> printNums()
60 16
61 60
62 30
63 36
64 32
65 48
66 20
67 66
68 32
69 44
70 24
71 70
72 24
73 72
74 36
75 40
76 36
77 60
78 24
79 78
80 32
81 54
82 40
83 82
84 24
85 64
86 42
87 56
88 40
89 88
90 24
91 72
92 44
93 60
94 46
95 72
96 32
97 96
98 42
99 60
100 40
"""
