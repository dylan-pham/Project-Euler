# 4. Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPalindrome(num):
    length = len(num)
    endIndex1 = int(length/2)
    endIndex2 = -(endIndex1 + 1)
    if num[0:endIndex1] == num[-1:endIndex2:-1]:
        return True
    else:
        return False

largestPalindrome = 0
for i in range(999, 99, -1):
    for x in range(999, 99, -1):
        if checkPalindrome(str(i * x)) == True and i * x > largestPalindrome:
            largestPalindrome = i * x

print(largestPalindrome)

# answer = 906609