import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    t += max(nums) - min(nums)
print(t)
