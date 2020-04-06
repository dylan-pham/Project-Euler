# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

num = 600851475143

def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False

    return True;

def get_primes(num):
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            print(i)

print(get_primes(num)) #6857
