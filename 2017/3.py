import itertools
from collections import defaultdict


def p1(data):
    steps = int(data)
    x, y = -1, 0
    d = (1, 0)
    v = set()
    for _ in range(steps):
        x, y = x + d[0], y + d[1]
        v.add((x, y))
        if (x - d[1], y + d[0]) not in v:
            d = (-d[1], d[0])
    return abs(x) + abs(y)


def p2(data):
    steps = int(data)
    x, y = 0, 0
    d = (1, 0)
    v = defaultdict(int)
    v[(0, 0)] = 1
    for _ in itertools.count():
        x, y = x + d[0], y + d[1]
        v[(x, y)] = sum([v[(x + dx, y + dy)] for dx, dy in itertools.product(list(range(-1, 2)), repeat=2)])
        if v[(x, y)] > steps:
            return v[(x, y)]
        if v[(x - d[1], y + d[0])] == 0:
            d = (-d[1], d[0])
