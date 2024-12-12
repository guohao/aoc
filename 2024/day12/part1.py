import sys
from collections import defaultdict

import math

ls = [l.strip() for l in sys.stdin.readlines()]
g = defaultdict(str) | {(i, j): c for i, line in enumerate(ls) for j, c in enumerate(line)}
seen = set()


def dfs(c):
    if c in seen:
        return 0, 0
    seen.add(c)
    x, y = c
    a, p = 1, 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nb = x + dx, y + dy
        if g[nb] == g[c]:
            a0, p0 = dfs(nb)
            a += a0
            p += p0
        else:
            p += 1
    return a, p


print(sum(math.prod(dfs(k)) for k in g.copy()))
