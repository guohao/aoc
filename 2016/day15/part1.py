import itertools
import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
ans = 1
ps = []
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    ps.append((nums[1], nums[-1]))
for i in itertools.count(0):
    if all((i + b + j) % a == 0 for j, (a, b) in enumerate(ps, start=1)):
        print(i)
        break
