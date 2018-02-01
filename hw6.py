import sys

def isMersenne(n):
    # we will first check if the number is prime
    if not isPrime(n):
        return False
    # We will proceed by incrementing n and seeing if it is a power of 2 or not
    n += 1
    # we will keep dividing by two until we get a number that isn't a power of
    # 2 (not Mersenne) or 1 (Mersenne)
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2
    return True


# Helper function to check if a number is prime or not
def isPrime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def main():
    print("Enter a number to see if it is a Mersenne Prime or not:")
    try:
        n = int(input())
    except ValueError:
        print("Needs to be an integer greater than 2. Exiting.")
        sys.exit()
    if n <= 2:
        print("Needs to be an integer greater than 2. Exiting")
        sys.exit()
    else:
        if isMersenne(n):
            print(n, "is a Mersenne Prime.")
        else:
            print(n, "is not a Mersenne Prime")


"""
Sample Output:

Enter a number to see if it is a Mersenne Prime or not:
3
3 is a Mersenne Prime.

Enter a number to see if it is a Mersenne Prime or not:
127
127 is a Mersenne Prime.

Enter a number to see if it is a Mersenne Prime or not:
1
Needs to be an integer greater than 2. Exiting

Enter a number to see if it is a Mersenne Prime or not:
6
6 is not a Mersenne Prime

Enter a number to see if it is a Mersenne Prime or not:
11
11 is not a Mersenne Prime
"""
