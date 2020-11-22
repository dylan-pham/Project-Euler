# sum_of_squares : Nat -> Nat
# finds sum of squares of numbers from 1 to given upper limit
def sum_of_squares(upper):
	return (upper*(upper+1)/2)**2

# square_of_sum : Nat Nat -> Nat
# finds the square of the sum of the numbers from 1 to given upper limit
def square_of_sum(upper):
	return upper*(upper+1)*(2*upper+1)/6

print(sum_of_squares(100) - square_of_sum(100))