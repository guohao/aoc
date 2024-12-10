import itertools
import re
import sys
from collections import deque

lines = [l.strip() for l in sys.stdin.readlines()]

cubes = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

lower_bound = [min(c[i] - 1 for c in cubes) for i in range(3)]
upper_bound = [max(c[i] + 1 for c in cubes) for i in range(3)]

ans = 0
dq = deque()
dq.append(lower_bound)
seen = set()
while dq:
    v = dq.popleft()
    if v in cubes:
        ans += 1
        continue
    if tuple(v) not in seen:
        seen.add(tuple(v))
        for i, j in itertools.product(range(0, 3), (-1, 1)):
            nv = v.copy()
            nv[i] += j
            if all(lower_bound[i] <= nv[i] <= upper_bound[i] for i in range(3)):
                dq.append(nv)

print(ans)
