with open("8.txt") as f:
	num = ""
	for x in f.readlines():
		num += x.strip()

# largest_n_factor_product : String Nat -> Nat
# finds largest product using n adajecent digits of given number
def largest_n_factor_product(num, length):
	greatest_product = 0
	start_index = 0
	end_index = start_index + length
	while end_index < len(num):
		current_product = 1
		for factor in num[start_index: end_index]:
			current_product *= int(factor)
		if current_product > greatest_product:
			greatest_product = current_product
		else:
			start_index += 1
			end_index += 1
	return greatest_product

print(largest_n_factor_product(num, 13))