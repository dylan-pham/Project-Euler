# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

def is_prime(num): # does not work when num == 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True;

sum = 0

for i in range(2, 2000001):
    if is_prime(i):
        sum += i

print(sum)