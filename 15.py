import time

t0 = time.time()

length = 21 # number of potential points is the number of cells on an edge + 1 

arr = [[0]*length for i in range(length+1)]

# can only go right or down --> only one possible path towards bottom right corner when on right or bottom edge
# filling right and bottom edge with 1s (except for bottom right corner)
for i in range(length-1):
    arr[i][length-1] = 1
    arr[length-1][i] = 1

# calculating number of paths at each point from bottom to top, traversing from right to left
for col in range(length-2, -1, -1):
    for row in range(length-2, -1, -1):
        arr[col][row] = arr[col+1][row] + arr[col][row+1]

print(arr[0][0])

t1 = time.time();
print(f"{(t1-t0)*1000} milliseconds")
