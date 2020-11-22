# largest_palindromic_number : Num -> Num
# returns largest possible palindromic number given by product of two factors with given number of digits
def largest_palindromic_number(digits):
	lower = int("1" + "0"*(digits-1))
	upper = int("9"*digits)
	_max = 0
	for i in range(upper, lower+1, -1):
		for j in range(upper, i+1, -1):
			if is_palindromic(str(i*j)) and (i*j > _max):
				_max = i*j
	return _max

# is_palindromic : String -> Boolean
# determines if given string is palindromic
def is_palindromic(x):
	_len = len(x)
	return x[0:_len//2] == x[_len//2+_len%2:_len][::-1]

print(largest_palindromic_number(3))