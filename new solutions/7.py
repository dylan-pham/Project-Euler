import math

# is_prime: Num -> Boolean
# determines if given number is prime using sieve of Eratosthenes
def is_prime(n):
	if n == 1:
		return False
	else:
		if n < 4:
			return True
		else:
			if (n % 2) == 0:
				return False
			else:
				if n < 9:
					return True
				else:
					if (n % 3) == 0:
						return False
					else:
						ceiling = math.floor(n**0.5)
						current = 5
						while current <= ceiling:
							if (n % current) == 0:
								return False
							if (n % (current+2)) == 0:
								return False
							current += 6
	return True

# find_xth_prime : Num -> Nat
def find_xth_prime(x):
	num = 3
	num_primes = 1
	while num_primes != x:
		if is_prime(num):
			num_primes += 1
		num += 1
	return num-1

print(find_xth_prime(10001))