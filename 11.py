# -*- coding: utf-8 -*-

#In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
#The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

grid = [];

with open("11.txt") as file:
    for line in file:
        row = [int(num) for num in line.split(" ")];
        grid.append(row);

max_product = 1788696
products = []

def check_max_product(x, y, left, right, up, down, up_right, up_left, down_right, down_left):
    if left:
        product = grid[x][y] * grid[x-1][y] * grid[x-2][y] * grid[x-3][y]
        if product > max_product: products.append(product) 
    if right:
        product = grid[x][y] * grid[x+1][y] * grid[x+2][y] * grid[x+3][y]
        if product > max_product: products.append(product)
    if up:
        product = grid[x][y] * grid[x][y-1] * grid[x][y-2] * grid[x][y-3]
        if product > max_product: products.append(product)
    if down:
        product = grid[x][y] * grid[x][y+1] * grid[x][y+2] * grid[x][y+3]
        if product > max_product: products.append(product)
    if up_right:
        product = grid[x][y] * grid[x+1][y-1] * grid[x+2][y-2] * grid[x+3][y-3]
        if product > max_product: products.append(product)
    if up_left:
        product = grid[x][y] * grid[x-1][y-1] * grid[x-2][y-2] * grid[x-3][y-3]
        if product > max_product: products.append(product)
    if down_right:
        product = grid[x][y] * grid[x+1][y+1] * grid[x+2][y+2] * grid[x+3][y+3]
        if product > max_product: products.append(product)
    if down_left:
        product = grid[x][y] * grid[x-1][y+1] * grid[x-2][y+2] * grid[x-3][y+3]
        if product > max_product: products.append(product)

for y in range(20):
    for x in range(20):
        # checking all directions by default
        left = True;
        right = True;
        up = True;
        down = True;
        up_right = True;
        up_left = True;
        down_right = True;
        down_left = True;

        # ignoring directions that don't include 4 numbers in a row
        if y - 3 < 0:
            up = False
            up_right = False
            up_left = False
        if y + 3 > 19:
            down = False
            down_right = False
            down_left = False
        if x - 3 < 0:
            left = False
            down_left = False
            up_left = False
        if x + 3 > 19:
            right = False
            up_right = False
            down_right = False

        check_max_product(x, y, left, right, up, down, up_right, up_left, down_right, down_left)

print(max(products))
