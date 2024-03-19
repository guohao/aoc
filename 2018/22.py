import itertools
import re
import networkx as nx


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def build_g(depth, target):
    g = {}
    X, Y = target[0] + 100, target[1] + 100
    for i in range(1, X + 1):
        g[i, 0] = (depth + (i * 16807)) % 20183
    for j in range(1, Y + 1):
        g[0, j] = (depth + (j * 48271)) % 20183
    g[0, 0] = depth % 20183
    g[target] = depth % 20183
    for j in range(1, Y + 1):
        for i in range(1, X + 1):
            if (i, j) == target:
                continue
            g[i, j] = (depth + (g[i - 1, j] * g[i, j - 1])) % 20183
    return {k: v % 3 for k, v in g.items()}


def p1(data: str):
    lines = data.splitlines()
    depth = ints(lines[0])[0]
    target = tuple(ints(lines[1]))
    g = build_g(depth, target)
    return sum(v for k, v in g.items() if k[0] <= target[0] and k[1] <= target[1])


def p2(data: str):
    lines = data.splitlines()
    depth = ints(lines[0])[0]
    target = tuple(ints(lines[1]))
    g = build_g(depth, (target[0], target[1]))
    G = nx.Graph()

    for x, y in g:
        k0 = (x, y)
        # 1 torch
        # 2 cg
        # 0 neither
        ta, tb = list({0, 1, 2} - {g[k0]})
        G.add_edge((k0, ta), (k0, tb), weight=7)
        for i, j in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            k1 = (x + i, y + j)
            if k1 not in g:
                continue
            for common in list({ta, tb}.intersection(list({0, 1, 2} - {g[k1]}))):
                G.add_edge((k0, common), (k1, common), weight=1)

    path = nx.shortest_path(G, ((0, 0), 1), (target, 1), 'weight')
    return nx.path_weight(G, path, 'weight')
