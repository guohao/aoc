import itertools
import math

import sys

pkgs = []
for line in sys.stdin.readlines():
    line = line.strip()
    pkgs.append(int(line))

group_weight = sum(pkgs) // 3

for i in range(1, len(pkgs)):
    ans = math.inf
    for c in itertools.combinations(pkgs, i):
        if sum(c) == group_weight:
            ans = min(ans, math.prod(c))
    if ans != math.inf:
        print(ans)
        break
