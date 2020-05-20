import time

t0 = time.time()
# ------------------------------

nums_to_word_length = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
    11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 0: 0
    }

total = 0

def sum_1_to_20():
    subtotal = 0
    for i in range(1, 21):
        subtotal += nums_to_word_length[i]

    return subtotal

def sum_21_to_99():
    subtotal = 0
    for i in range(21, 100):
        tens = int(str(i)[0]) * 10
        subtotal += nums_to_word_length[tens]

        ones = int(str(i)[1])
        subtotal += nums_to_word_length[ones]
    
    return subtotal

total += sum_1_to_20() * 10 # 1-20, 101-120... 
total += sum_21_to_99() * 10 # 21-99, 121-199...
total += 3 * 99 * 9 # AND

total += 3 * 100 # ONE hundred
total += 3 * 100
total += 5 * 100
total += 4 * 100
total += 4 * 100
total += 3 * 100
total += 5 * 100
total += 5 * 100
total += 4 * 100

total += 7 * 900 # one HUNDRED
total += 11 # ONE THOUSAND

print(total)

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
