import itertools
import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
rows = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]
columns = list(itertools.chain.from_iterable(zip(*rows)))
for i in range(0, len(columns), 3):
    nums = sorted(columns[i:i + 3])
    t += sum(nums[:2]) > nums[2]
print(t)
