import itertools
import sys

lines = [l.strip() for l in sys.stdin.readlines()]

g = {(i, j): c for i, line in enumerate(lines) for j, c in line}
ans = 0
for t in itertools.count(1):
    print(t)
    flashed = set()
    g = {k: v + 1 for k, v in g.items()}
    while any(v > 9 and k not in flashed for k, v in g.items()):
        for n in g:
            if g[n] > 9 and n not in flashed:
                for dx, dy in itertools.product(range(-1, 2), repeat=2):
                    if dx == dy == 0:
                        continue
                    nb = x + dx, y + dy
                    if nb in g:
                        g[nb] += 1
                flashed.add(n)
    for n in flashed:
        g[n] = 0
    if len(flashed) == len(g):
        print(t)
        exit()
