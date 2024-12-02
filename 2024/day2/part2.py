import sys
import re
from itertools import combinations

import sys

ls = [line.strip() for line in sys.stdin.readlines()]

t = 0
for line in ls:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    for c in combinations(nums, len(nums) - 1):
        c = list(c)
        if c == sorted(c) or c == sorted(c, reverse=True):
            for i in range(1, len(c)):
                if not (1 <= abs(c[i] - c[i - 1]) <= 3):
                    break
            else:
                t += 1
                break

print(t)
