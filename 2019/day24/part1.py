import itertools
import math

import sys

data = sys.stdin.read().strip()

N = 5
g = {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}
seen = set()
for t in itertools.count():
    snapshot = tuple(g.values())
    if snapshot in seen:
        ans = 0
        base = 0
        for i, j in itertools.product(range(N), repeat=2):
            if g[i, j] == '#':
                ans += math.pow(2, base)
            base += 1
        print(int(ans))
        break
    seen.add(snapshot)
    ng = {}
    for i, j in itertools.product(range(N), repeat=2):
        bc = 0
        ec = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nb = i + dx, j + dy
            if nb in g:
                if g[nb] == '#':
                    bc += 1
                else:
                    ec += 1
        if (g[i, j] == '#' and bc == 1) or (g[i, j] == '.' and bc in (1, 2)):
            ng[i, j] = '#'
        else:
            ng[i, j] = '.'
    g = ng
