import itertools
import sys
from collections import Counter

N = 1000000000
G = {(i, j): c for i, line in enumerate(sys.stdin.readlines()) for j, c in enumerate(line.strip())}

X = max([x for x, _ in G.keys()]) + 1
Y = max([y for _, y in G.keys()]) + 1


def gen(g):
    ng = {}
    for i, j in g:
        c = Counter()
        for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
            k = i + dx, j + dy
            if k in g:
                c[g[k]] += 1
        c[g[i, j]] -= 1
        match g[i, j]:
            case '.':
                if c['|'] >= 3:
                    ng[i, j] = '|'
            case '|':
                if c['#'] >= 3:
                    ng[i, j] = '#'
            case '#':
                if not (c['#'] >= 1 and c['|'] >= 1):
                    ng[i, j] = '.'
        if (i, j) not in ng:
            ng[i, j] = g[i, j]
    return ng


t = 0
seen = {}
while t < N:
    key = tuple(G.values())
    if key in seen:
        t += (N - t) // (t - seen[key]) * (t - seen[key])
    else:
        seen[key] = t
    G = gen(G)
    t += 1

print(sum(v == '|' for v in G.values()) * sum(v == '#' for v in G.values()))
