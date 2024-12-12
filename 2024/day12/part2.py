import sys
from collections import defaultdict

ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): c for i, line in enumerate(ls) for j, c in enumerate(line)}
seen = set()

inner = defaultdict(set)
outer = defaultdict(set)


def dfs(f, c):
    if c in seen:
        return
    seen.add(c)
    inner[f].add(c)
    x, y = c
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nb = x + dx, y + dy
        if g.get(nb, '') == g[c]:
            dfs(f, nb)
        else:
            outer[f].add(nb)


for k in g:
    dfs(k, k)

t = 0
for k in g:
    c = 0
    for x, y in inner[k]:
        for c0, c1 in [[(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(-1, 0), (0, 1)], [(1, 0), (0, -1)]]:
            if (x + c0[0], y + c0[1]) in outer[k] and (x + c1[0], y + c1[1]) in outer[k]:
                c += 1
            elif (x + c0[0], y + c0[1]) in inner[k] and (x + c1[0], y + c1[1]) in inner[k] and \
                    (x + c0[0] + c1[0], y + c0[1] + c1[1]) in outer[k]:
                c += 1
    t += len(inner[k]) * c

print(t)
