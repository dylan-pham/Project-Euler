sum = 0

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

# ------------------- more efficient solution

def sum_of_multiples(target, divisor):
    n = target // divisor
    return 0.5 * n * (n + 1) * divisor

solution = sum_of_multiples(999, 3) + sum_of_multiples(999, 5) - sum_of_multiples(999, 15)
print(solution)
