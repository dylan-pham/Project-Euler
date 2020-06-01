import time

t0 = time.time()
# ------------------------------

sum_amicable_nums = 0
pairs = {} # number : sum of proper divisors of number

def get_sum_divisors(num):
    _sum = 0

    for i in range(1, int(num/2 + 1)):
        if num % i == 0:
            _sum += i

    return _sum

for num in range(1, 10000):
    _sum = get_sum_divisors(num)
    pairs[num] = _sum

    if (_sum in pairs) and (pairs[_sum] == num) and (_sum != num):
        sum_amicable_nums += num 
        sum_amicable_nums += _sum

print(sum_amicable_nums)

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
