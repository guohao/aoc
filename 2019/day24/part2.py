import itertools
import math

import sys

data = sys.stdin.read().strip()

N = 5
gs = {
    0: {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)},
}
for _ in range(200):
    ngs = {}
    gs[min(gs.keys()) - 1] = {(i, j): '.' for i, j in itertools.product(range(N), repeat=2)}
    gs[max(gs.keys()) + 1] = {(i, j): '.' for i, j in itertools.product(range(N), repeat=2)}
    for t in sorted(gs.keys()):
        g = gs[t]
        ng = {}
        for i, j in itertools.product(range(N), repeat=2):
            if (i, j) == (2, 2):
                continue
            bc = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = i + dx, j + dy
                if nb == (2, 2):
                    if t - 1 in gs:
                        ig = gs[t - 1]
                        if dx == 0 and dy == -1:
                            bc += sum(1 for x in range(N) if ig[x, N - 1] == '#')
                        elif dx == 0 and dy == 1:
                            bc += sum(1 for x in range(N) if ig[x, 0] == '#')
                        elif dx == 1 and dy == 0:
                            bc += sum(1 for x in range(N) if ig[0, x] == '#')
                        elif dx == -1 and dy == 0:
                            bc += sum(1 for x in range(N) if ig[N - 1, x] == '#')
                elif nb in g:
                    if g[nb] == '#':
                        bc += 1
                else:
                    if t + 1 in gs:
                        og = gs[t + 1]
                        if dx == 0 and dy == -1:
                            bc += int(og[2, 1] == '#')
                        elif dx == 0 and dy == 1:
                            bc += int(og[2, 3] == '#')
                        elif dx == 1 and dy == 0:
                            bc += int(og[3, 2] == '#')
                        elif dx == -1 and dy == 0:
                            bc += int(og[1, 2] == '#')
            if (g[i, j] == '#' and bc == 1) or (g[i, j] == '.' and bc in (1, 2)):
                ng[i, j] = '#'
            else:
                ng[i, j] = '.'
        ngs[t] = ng
    gs = ngs

print(sum(x == '#' for v in gs.values() for x in v.values()))
