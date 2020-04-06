# 5. Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisor = 20
initialValue = 2520

while True:
    if initialValue % divisor == 0:
        divisor -= 1
        if divisor == 1:
            print(initialValue)
            break
    else:
        initialValue += 20
        divisor = 20
