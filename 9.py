# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def checkTriangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def checkCombos():
    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(1, 500):
                if a + b + c == 1000:
                    if checkTriangle(a, b, c) == True:
                        return(a * b * c)

print(checkCombos())
# answer = 31875000