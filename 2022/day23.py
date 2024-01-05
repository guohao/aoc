from collections import defaultdict

from helper import *

data = raw_data(2022, 23)

g = {(i, j) for i, line in enumerate(data.strip().splitlines()) for j, c in enumerate(line) if c != '.'}
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

for r in range(1000000000):
    dest = defaultdict(list)
    for x, y in g:
        if sum([(x + i, y + j) in g for i in range(-1, 2) for j in range(-1, 2)]) == 1:
            continue
        np = (x, y)
        for j in range(4):
            dx, dy = DIRECTIONS[(r + j) % 4]
            if dx == 0:
                if all((x + k, y + dy) not in g for k in range(-1, 2)):
                    np = (x, y + dy)
                    break
            else:
                if all((x + dx, y + k) not in g for k in range(-1, 2)):
                    np = (x + dx, y)
                    break
        dest[np].append((x, y))

    dest = {p: v for p, v in dest.items() if len(v) == 1}
    if len(dest) == 0:
        print(r + 1)
        break
    for p, v in dest.items():
        g.remove(v[0])
        g.add(p)
    if r == 9:
        X = max(x for x, _ in g) - min(x for x, _ in g) + 1
        Y = max(y for _, y in g) - min(y for _, y in g) + 1
        print(X * Y - len(g))
