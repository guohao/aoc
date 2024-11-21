import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    nums = sorted(list(map(int, re.findall(r'-?\d+', line))))
    t += sum(nums[:2]) > nums[2]
print(t)
