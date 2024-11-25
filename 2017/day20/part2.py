import re
import sys
from collections import defaultdict
from functools import reduce

lines = [line.strip() for line in sys.stdin.readlines()]
ps = []
for line in lines:
    ps.append(list(map(int, re.findall(r'-?\d+', line))))

ans = 0
for k in range(1000):
    nps = []
    collisions = defaultdict(list)
    for i in range(len(ps)):
        p, v, a = ps[i][:3], ps[i][3:6], ps[i][6:]
        v = [v[j] + a[j] for j in range(3)]
        p = [p[j] + v[j] for j in range(3)]
        ps[i] = p + v + a
        collisions[tuple(p)].append(i)
    td = reduce(lambda a, b: a + b, [v for v in collisions.values() if len(v) > 1], [])
    ps = [ps[i] for i in range(len(ps)) if i not in td]
    ans = len(ps)
print(ans)
