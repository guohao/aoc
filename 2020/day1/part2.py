import math
import sys
from itertools import combinations

nums = set([int(line.strip()) for line in sys.stdin.readlines()])
t = 0
for c in combinations(nums, 3):
    if sum(c) == 2020:
        print(math.prod(c))
        break
