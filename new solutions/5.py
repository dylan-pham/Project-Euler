# smallest_divisible_numnber : Nat Nat -> Nat
# finds smallest positive number that is divisible by all numbers in given range
def smallest_divisible_numnber(start, stop):
	current_value = stop
	i = start
	while (i <= stop):
		if (current_value % i) == 0:
			i += 1
		else:
			current_value += stop
			i = 11
	return current_value

print(smallest_divisible_numnber(1,20))