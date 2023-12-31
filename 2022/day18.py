import functools
import sys
from collections import deque

from helper import *

data = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

data = raw_data(2022, 18)
lines = lines(data)

cubes = [nums(line) for line in lines]
ans = 6 * len(cubes)
for i, a in enumerate(cubes):
    for b in cubes[:i]:
        if sum(abs(a[k] - b[k]) for k in range(3)) == 1:
            ans -= 2
print(ans)

lower_bound = [min(c[i] - 1 for c in cubes) for i in range(3)]
upper_bound = [max(c[i] + 1 for c in cubes) for i in range(3)]

ans2 = 0
dq = deque()
dq.append(lower_bound)
seen = set()
while dq:
    v = dq.popleft()
    if v in cubes:
        ans2 += 1
        continue
    if tuple(v) not in seen:
        seen.add(tuple(v))
        for i, j in itertools.product(range(0, 3), (-1, 1)):
            nv = v.copy()
            nv[i] += j
            if all(lower_bound[i] <= nv[i] <= upper_bound[i] for i in range(3)):
                dq.append(nv)

print(ans2)
