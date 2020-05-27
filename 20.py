import time

t0 = time.time()
# ------------------------------

# cheap solution

def get_factorial(num):
    return num * get_factorial(num - 1) if num - 1 > 0 else num 

_sum = 0
factorial = str(get_factorial(100))

for i in range(len(factorial)):
    _sum += int(factorial[i])

print(_sum)

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
