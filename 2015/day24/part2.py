import itertools
import math

pkgs = []
try:
    while True:
        pkgs.append(int(input()))
except EOFError:
    pass

group_weight = sum(pkgs) // 4

for i in range(1, len(pkgs)):
    ans = math.inf
    for c in itertools.combinations(pkgs, i):
        if sum(c) == group_weight:
            ans = min(ans, math.prod(c))
    if ans != math.inf:
        print(ans)
        break
