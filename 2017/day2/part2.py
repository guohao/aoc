import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    for a in nums:
        for b in nums:
            if a != b and a % b == 0:
                t += a // b

print(t)
