import itertools

import sys

data = sys.stdin.read().strip()

g = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '#':
            g[i, j, 0, 0] = c
for t in range(6):
    ng = {}
    rz = range(min(z for _, _, z, _ in g) - 1, max(z for _, _, z, _ in g) + 2)
    rw = range(min(w for _, _, _, w in g) - 1, max(w for _, _, _, w in g) + 2)
    rx = range(min(x for x, _, _, _ in g) - 1, max(x for x, _, _, _ in g) + 2)
    ry = range(min(y for _, y, _, _ in g) - 1, max(y for _, y, _, _ in g) + 2)
    for n in itertools.product(rx, ry, rz, rw):
        c = 0
        x, y, z, w = n
        for dx, dy, dz, dw in itertools.product(range(-1, 2), repeat=4):
            if dx == dy == dz == dw == 0:
                continue
            nb = x + dx, y + dy, z + dz, w + dw
            if nb in g and g[nb] == '#':
                c += 1
        if n in g and g[n] == '#' and c in (2, 3):
            ng[n] = '#'
        if (n not in g or g[n] == '.') and c == 3:
            ng[n] = '#'
    g = ng
print(list(g.values()).count('#'))
