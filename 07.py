# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

count = 0

def is_prime(num): # does not work when num == 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True;

i = 2
while (count != 10001):
    if is_prime(i):
        count += 1
        print(str(count) + ": " + str(i))
    i += 1