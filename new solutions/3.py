import math

# largest_prime_factor : Num -> Num
# returns the largest prime factor of a given number
def largest_prime_factor(num):
	_max = 0
	for i in range(1, int(math.sqrt(num))+1, 2):
		if (num % i) == 0 and is_prime(i):
			_max = i
	return _max

# is_prime: Num -> Boolean
# determines if given number is prime
def is_prime(num):
	for i in range(2, num-1):
		if (num % i) == 0:
			return False
	return True

print(largest_prime_factor(600851475143))