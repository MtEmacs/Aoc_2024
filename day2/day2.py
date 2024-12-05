
import pandas as pd
from typing import List


lines = []
with open("test_input", "r") as file:
    # Read the lines and process them
    for line in file:
        numbers = list(map(int, line.split()))
        lines.append(numbers)


line = lines[0]
prev = line[0] - 1

def is_increasing(numbers: List[int]) -> bool:
    prev = numbers[0]
    for x in numbers[1:]:
        if x <= prev:
            return False
        prev = x
    return True

def is_decreasing(numbers: List[int]) -> bool:
    prev = numbers[0]
    for x in numbers[1:]:
        if x >= prev:
            return False
        prev = x
    return True


def biggest_diff(numbers: List[int]) -> int:
    diff = 0
    prev = numbers[0]
    for x in numbers[1:]:
        diff = max(diff, abs(x - prev))
        prev = x
    return diff

correct = 0
for line in lines:
    if is_increasing(line) or is_decreasing(line) and biggest_diff(line) <= 3:
        correct += 1
        print(biggest_diff(line))
        print(line)
print(f"Correct: {correct}")
