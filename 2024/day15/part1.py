import sys
from collections import defaultdict

parts = sys.stdin.read().split('\n\n')

g = defaultdict(lambda: "#") | {(i, j): c for i, line in enumerate(parts[0].splitlines()) for j, c in enumerate(line)}
x, y = next(n for n in g if g[n] == '@')
for d in parts[1].replace('\n', ''):
    assert g[x, y] == '@'
    dx, dy = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}[d]
    nx, ny = x + dx, y + dy
    while g[nx, ny] == 'O':
        nx, ny = nx + dx, ny + dy
    if g[nx, ny] == '.':
        while (nx, ny) != (x, y):
            g[nx, ny] = g[nx - dx, ny - dy]
            nx, ny = nx - dx, ny - dy
        g[x, y] = '.'
        x, y = x + dx, y + dy
print(sum(p[0] * 100 + p[1] for p in g if g[p] == 'O'))
