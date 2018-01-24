"""
Prakarsh Pandey, Harvey Mudd College
Homework 2:
Problem Statement: Design a program whether the entered integer n; n > 4; is
perfect or not. It also outputs the divisors of the first one.
"""
import sys

"""
Helper method that gets the list of divisors of a number that aren't the number
itself.
"""
def getDivisors(n):
    divisorList = []
    # we only go til n/2 + 1 instead of n because we don't need to
    # iterate through n.
    # this reduces the number of operations needed to be done
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            divisorList += [i]
    return divisorList

"""
Method that checks if a number is a perfect number or not
"""
def isPerfect(n):
    if sum(getDivisors(n)) == n:
        return True
    else:
        return False

def main():
    print("Enter a number to see if it is perfect or not:")
    try:
        n = int(input())
    except ValueError:
        print("Needs to be an integer greater than 4. Exiting.")
        sys.exit()
    if n <= 4:
        print("Needs to be an integer greater than 4. Exiting")
        sys.exit()
    else:
        if isPerfect(n):
            print(n, "is a perfect number. The list of divisors is",
                getDivisors(n))
        else:
            print(n, "is not a perfect number")

# make the main method run automatically when the program is run
if __name__ == "__main__":
    main()

"""
Sample Output:

Enter a number to see if it is perfect or not:
28
28 is a perfect number. The list of divisors is [1, 2, 4, 7, 14]

Enter a number to see if it is perfect or not:
567
567 is not a perfect number

Enter a number to see if it is perfect or not:
asd
Needs to be an integer greater than 4. Exiting.
"""
