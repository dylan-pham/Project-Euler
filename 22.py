import time

t0 = time.time()
# ------------------------------

names = []
char_vals = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
}
_sum = 0

with open("22.txt") as file:
    for word in file.read().split(","):
        names.append(word[1:-1])

names.sort()

for name in names:
    name_value = 0

    for char in name:
        name_value += char_vals[char]

    _sum += name_value * (names.index(name) + 1)

print(_sum)

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
