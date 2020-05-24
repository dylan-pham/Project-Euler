import time

t0 = time.time()
# ------------------------------

triangle = []
largest_sum = [] # largest sum at a given point from bottom

with open("18.txt") as file:
    for line in file:
        row = [int(num) for num in line.split(" ")];
        triangle.append(row);
        largest_sum.append([0 for i in range(len(row))])

largest_sum[len(triangle)-1] = triangle[len(triangle)-1]

for row in range(len(largest_sum)-2, -1, -1):
    for col in range(len(largest_sum[row])):
        largest_sum_left = largest_sum[row+1][col]
        largest_sum_right = largest_sum[row+1][col+1]

        largest_sum[row][col] = triangle[row][col] + (largest_sum_left if largest_sum_left > largest_sum_right else largest_sum_right)


print(largest_sum[0][0])

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
