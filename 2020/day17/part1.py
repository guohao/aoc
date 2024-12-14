import itertools

import sys

data = sys.stdin.read().strip()

g = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '#':
            g[i, j, 0] = c
for t in range(6):
    ng = {}
    for k in range(min(z for _, _, z in g) - 1, max(z for _, _, z in g) + 2):
        for i in range(min(x for x, _, _ in g) - 1, max(x for x, _, _ in g) + 2):
            for j in range(min(y for _, y, _ in g) - 1, max(y for _, y, _ in g) + 2):

                c = 0
                for dx, dy, dz in itertools.product(range(-1, 2), repeat=3):
                    if dx == dy == dz == 0:
                        continue
                    nb = i + dx, j + dy, k + dz
                    if nb in g and g[nb] == '#':
                        c += 1
                if (i, j, k) in g and g[i, j, k] == '#' and c in (2, 3):
                    ng[i, j, k] = '#'
                if ((i, j, k) not in g or g[i, j, k] == '.') and c == 3:
                    ng[i, j, k] = '#'
    g = ng
print(list(g.values()).count('#'))
