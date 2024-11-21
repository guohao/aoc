import itertools

import sys

g = {}
lines = [line.strip() for line in sys.stdin.readlines()]
N = len(lines)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        g[i, j] = c

for _ in range(N):
    n = {}
    for i, j in itertools.product(range(N), repeat=2):
        ons = 0
        for di, dj in itertools.product(range(-1, 2), repeat=2):
            if di == dj == 0:
                continue
            if (i + di, j + dj) in g and g[i + di, j + dj] == '#':
                ons += 1
        if g[i, j] == '#':
            n[i, j] = '#' if ons in {2, 3} else '.'
        else:
            n[i, j] = '#' if ons == 3 else '.'
    g = n
print(list(g.values()).count('#'))
