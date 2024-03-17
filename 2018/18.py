import itertools
from collections import Counter


def solve(data: str, n):
    G = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            G[i, j] = c
    X = max([x for x, _ in G.keys()]) + 1
    Y = max([y for _, y in G.keys()]) + 1

    m = 0
    seen = {}
    while m < n:
        ck = tuple(G.values())
        if ck in seen:
            m += (n - m) // (m - seen[ck]) * (m - seen[ck])
        else:
            seen[ck] = m
        ng = {}
        for i in range(X):
            for j in range(Y):
                c = Counter()
                for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
                    k = i + dx, j + dy
                    if k in G:
                        c[G[k]] += 1
                c[G[i, j]] -= 1

                match G[i, j]:
                    case '.':
                        if c['|'] >= 3:
                            ng[i, j] = '|'
                    case '|':
                        if c['#'] >= 3:
                            ng[i, j] = '#'
                    case '#':
                        if not (c['#'] >= 1 and c['|'] >= 1):
                            ng[i, j] = '.'
                    case _:
                        assert False
                if (i, j) not in ng:
                    ng[i, j] = G[i, j]
        G = ng
        m += 1
    return sum(v == '|' for v in G.values()) * sum(v == '#' for v in G.values())


def p1(data):
    return solve(data, 10)


def p2(data):
    return solve(data, 1000000000)
