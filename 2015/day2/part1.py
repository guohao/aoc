import math
import sys
from itertools import combinations

t = 0
lines = sys.stdin.readlines()
for line in lines:
    nums = map(int, line.split('x'))
    p = list(map(math.prod, combinations(nums, 2)))
    t += min(p) + sum(p) * 2
print(t)
