#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:02:30 2024

@author: ccrowe
"""

import re

# Define the pattern
pattern = r"mul\((\d+),(\d+)\)"

# Sample string
text = open("./real.py","r").read()
print(text)

pieces = []
spl = re.split(r"don't\(\)", text)
first = spl[0]
# first is always a do
pieces.append(first)
spl = spl[1:]
for dnt in spl:
    enable = False
    do = re.split(r"do\(\)", dnt)
    for d in do:
        if enable is True:
            print(f"Enabled: {dnt}")
            pieces.append(d)
        else:
            print(f"Did not consider: {d}")
        # enabled after the first do
        enable = True

text = "".join(pieces)

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print("Matches found:", matches)


product = 0
for match in matches:
    num1, num2 = match
    product += int(num1)*int(num2)
print(f"Product: {product}")
