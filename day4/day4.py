#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:35:10 2024

@author: ccrowe
"""

import time

start_time = time.time()

s = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

arr = []

spl = s.split("\n")
for line in spl:
    row = [x for x in line]
    arr.append(row)

print(arr)

directions = [
# up 
[-1,0],
# up-right 
[-1, 1],
# right
[0,1],
# down-right 
[1, 1],
# down 
[1, 0],
# down-left 
[1,-1],
# left 
[0,-1],
# up-lef 
[-1, -1]
    ]

import copy
# answer = copy.deepcopy(arr)

count = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        item = arr[row][col]
        if item == "X":
            for direction in directions:
                r, c = row, col
                building = []
                for letter in ["M","A","S"]:
                    r += direction[0]
                    c += direction[1]
                    if r < 0 or r >= len(arr):
                        break
                    if c < 0 or c >= len(arr[0]):
                        break
                    if arr[r][c] == letter:
                        building.append(arr[r][c])
                        if letter == "S" and "".join(building) == "MAS":
                            count += 1

#print(f"Count: {count}")

option1 = [[-1, 1],
# up right
[1, -1]]
# down left

option2 = [[-1,-1],
# up left
[1, 1]]
# down right

def is_valid_position(r, c, rows, cols):
    """Check if a position is within array bounds."""
    return 0 <= r < rows and 0 <= c < cols

# Look for MAS and MAS crossed
count = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        item = arr[row][col]
        if item == "A":
            o1r = row + option1[0][0]
            o1c = col + option1[0][1]
            o1r2 = row + option1[1][0]
            o1c2 = col + option1[1][1]
            if (is_valid_position(o1r, o1c, len(arr), len(arr[0])) and
    is_valid_position(o1r2, o1c2, len(arr), len(arr[0]))):
                if (arr[o1r][o1c] == "M" and arr[o1r2][o1c2] == "S") or (arr[o1r][o1c] == "S" and arr[o1r2][o1c2] == "M"):
                    o2r = row + option2[0][0]
                    o2c = col + option2[0][1]
                    o2r2 = row + option2[1][0]
                    o2c2 = col + option2[1][1]
                    if (is_valid_position(o2r, o2c, len(arr), len(arr[0])) and
            is_valid_position(o2r2, o2c2, len(arr), len(arr[0]))):
                        if (arr[o2r][o2c] == "M" and arr[o2r2][o2c2] == "S") or (arr[o2r][o2c] == "S" and arr[o2r2][o2c2] == "M"):
                            count += 1

print(f"Count: {count}")

end_time = time.time()
print(f"Runtime: {end_time - start_time:.6f} seconds")