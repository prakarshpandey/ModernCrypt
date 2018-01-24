"""
Prakarsh Pandey, Harvey Mudd College
Homework 1:
Problem Statement:
Design a program that calculates and outputs the least common multiple of two
integers a and b, a, b >= 3. The program would ask the user to enter a and b
from the keyboard, i.e., the solution needs to be of a general nature.
In this HW, I want you to present 2 versions of the solution: first, do not use
the logical operator AND. Second, do not use the logical operator OR
"""
import sys
# Solution 2. Does not use the logical AND operator
def lcm_no_or(a, b):
    b_init = b
    a_init = a
    if b > a:
        return lcm_no_or(b, a)
    elif b == a:
        return a
    else:
        # set initial value for lcm
        lcm = b
        while True:
            # keep adding b_init to lcm and b until they are equal to a
            lcm += b_init
            b += b_init
            # in this case we know what the lcm condition is
            if lcm == a and lcm == b:
                return a
            elif b > a:
                a += a_init

# Solution 1. Does not use the logical OR operator
def lcm_no_and(a, b):
    b_init = b
    a_init = a
    if b > a:
        return lcm_no_or(b, a)
    elif b == a:
        return a
    else:
        # set initial value for lcm
        lcm = b
        while True:
            # keep adding b_init to lcm and b until they are equal to a
            lcm += b_init
            b += b_init
            # apply DeMorgan's Law to remove the logical AND
            # in this case we know what the lcm condition is
            if not(not lcm == a or not lcm == b):
                return a
            elif b > a:
                a += a_init
def main():
    print("Please enter two integers a and b")
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print("You did not enter an int. Exiting")
        sys.exit()
    if a < 3 or b < 3:
        print("a and b have to be greater than 3. Exiting")
        sys.exit()
    else:
        print("The least common multiple of", a, "and", b, "is", lcm_no_or(a, b))

# make the main method run automatically when the program is run
if __name__ == "__main__":
    main()

"""
Sample Outputs:
Please enter two integers a and b
3
4
The least common multiple of 3 and 4 is 12

Please enter two integers a and b
34509
12315
The least common multiple of 34509 and 12315 is 141659445

Please enter two integers a and b
True
You did not enter an int. Exiting
"""
