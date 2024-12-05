from typing import List
import time

start_time = time.time()

# Read the file
with open('real', 'r') as file:
    lines = file.readlines()

# Parse the lines
rules = []
pages = []

for line in lines:
    line = line.strip()  # Remove any trailing newlines or spaces
    if '|' in line:  # Check if it's a pair line
        pairs = tuple(map(int, line.split('|')))
        rules.append(pairs)
    elif ',' in line:  # Check if it's a list line
        values = list(map(int, line.split(',')))
        pages.append(values)

# I need to identify a page that should come before what preceeds it
# I need to see if the page should come before all preceeds
# for each preceed, track its dependencies
# track those to see if the latter page is one.

from collections import defaultdict
deps = defaultdict(lambda : set())
for rule in rules:
    before, after = rule
    # list an individual page's dependencies
    deps[after].add(before)

def is_correct(line):
    for index in range(len(line)):
        page = line[index]
        preceeds = line[:index]
        for preceed in preceeds:
            if page in deps[preceed]:
                return False
    return True

def correct_order(line) -> List[int]:
    for index in range(len(line)):
        page = line[index]
        preceeds = line[:index]
        for preceed in preceeds:
            if page in deps[preceed]:
                preceed_index = line.index(preceed)
                line[preceed_index] = page
                line[index] = preceed
                break
    return line

total = 0
for line in pages:
    answer = is_correct(line)
    print(answer, line)
    if not answer:
        while not is_correct(line):
            line = correct_order(line)
        middle = len(line) // 2
        val = line[middle]
        total += val
print(total)
    
    
end_time = time.time()
print(f"Runtime: {end_time - start_time:.6f} seconds")
