# sum_even_fibo_terms : Nat Nat Nat Nat -> Nat
# given previous term, current term, and maximum term value, returns sum of even-valued terms
def sum_even_fibo_terms(prev, current, _max):
	if (current < _max):
		if (current % 2) == 0:
			return current + sum_even_fibo_terms(current, prev + current, _max)
		return sum_even_fibo_terms(current, prev + current, _max)
	return 0

print(sum_even_fibo_terms(1, 2, 4000000))