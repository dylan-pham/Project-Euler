# sum_of_multiples : Num, Num -> Num
# given a number, finds the sum of its multiples below a second given number
def sum_of_multiples(multiple, _max):
	_sum = 0
	for i in range(_max):
		if (i % multiple) == 0:
			_sum += i
	return _sum

print(sum_of_multiples(3, 1000) + sum_of_multiples(5, 1000) - sum_of_multiples(15, 1000))