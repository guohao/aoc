import sys


def nb4(_x, _y):
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        yield _x + dx, _y + dy


ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
s = [k for k, v in g.items() if v == 'S'][0]
tv = [s]
for _ in range(64):
    nv = set()
    for n in tv:
        for nb in nb4(*n):
            if nb in g and g[nb] != '#':
                nv.add(nb)
    tv = nv
print(len(tv))
