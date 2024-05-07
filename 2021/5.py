from collections import defaultdict


def p1(data: str):
    g = defaultdict(int)
    for line in data.splitlines():
        l, r = line.split(' -> ')
        x1, y1 = list(map(int, l.split(',')))
        x2, y2 = list(map(int, r.split(',')))
        if x1 == x2 or y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    g[i, j] += 1
    return sum(v >= 2 for v in g.values())


def p2(data: str):
    g = defaultdict(int)
    for line in data.splitlines():
        l, r = line.split(' -> ')
        x1, y1 = list(map(int, l.split(',')))
        x2, y2 = list(map(int, r.split(',')))
        i = x1
        j = y1
        dx = (x2 > x1) - (x2 < x1)
        dy = (y2 > y1) - (y2 < y1)
        while i != (x2 + dx) or j != (y2 + dy):
            g[i, j] += 1
            i += dx
            j += dy
    return sum(v >= 2 for v in g.values())
