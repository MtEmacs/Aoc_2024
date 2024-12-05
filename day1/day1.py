
import pandas as pd

first = []
second = []

with open("day1_input.txt", "r") as file:
    # Read the lines and process them
    for line in file:
        # Split the line into numbers and convert them to integers
        numbers = list(map(int, line.split()))
        first.append(numbers[0])
        second.append(numbers[1])

# Print the processed data
first.sort()
second.sort()

product = 0
for left in first:
    count = second.count(left)
    product += count * left
    

print(f"Answer: {product}")
