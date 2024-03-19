import itertools
import re
import networkx as nx


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def build_g(depth, target):
    g = {}
    X, Y = target
    for i in range(1, X + 1):
        g[i, 0] = (depth + (i * 16807)) % 20183
    for j in range(1, Y + 1):
        g[0, j] = (depth + (j * 48271)) % 20183
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            g[i, j] = (depth + (g[i - 1, j] * g[i, j - 1])) % 20183
    g[target] = depth % 20183
    g[0, 0] = depth % 20183
    return {k: v % 3 for k, v in g.items()}


def p1(data: str):
    lines = data.splitlines()
    depth = ints(lines[0])[0]
    target = tuple(ints(lines[1]))

    g = build_g(depth, target)
    return sum(g.values())


def p2(data: str):
    # lines = data.splitlines()
    # depth = ints(lines[0])[0]
    # target = tuple(ints(lines[1]))
    depth = 510
    target=(10,10)
    g = build_g(depth, target)
    G = nx.Graph()
    for x, y in g:
        k0 = (x, y)
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            k1 = (x + i, y + j)
            if k1 == (0, 0):
                continue
            if k1 not in g:
                continue
            # 0 torch
            # 1 cg
            # 2 neither
            if g[k0] == 0:
                if g[k1] == 0:
                    G.add_edge((k0, 0), (k1, 0), weight=1)
                    G.add_edge((k0, 1), (k1, 1), weight=1)
                    G.add_edge((k0, 0), (k1, 1), weight=8)
                    G.add_edge((k0, 1), (k1, 0), weight=8)
                elif g[k1] == 1:
                    G.add_edge((k0, 0), (k1, 1), weight=8)
                    G.add_edge((k0, 1), (k1, 1), weight=1)
                else:
                    G.add_edge((k0, 0), (k1, 0), weight=1)
                    G.add_edge((k0, 1), (k1, 0), weight=8)
            elif g[k0] == 1:
                if g[k1] == 0:
                    G.add_edge((k0, 1), (k1, 0), weight=8)
                    G.add_edge((k0, 2), (k1, 1), weight=8)
                elif g[k1] == 1:
                    G.add_edge((k0, 1), (k1, 1), weight=1)
                    G.add_edge((k0, 2), (k1, 2), weight=1)
                    G.add_edge((k0, 1), (k1, 2), weight=8)
                    G.add_edge((k0, 2), (k1, 1), weight=8)
                else:
                    G.add_edge((k0, 2), (k1, 2), weight=1)
                    G.add_edge((k0, 1), (k1, 2), weight=8)
            else:
                if g[k1] == 0:
                    G.add_edge((k0, 0), (k1, 0), weight=1)
                    G.add_edge((k0, 2), (k1, 0), weight=8)
                elif g[k1] == 1:
                    G.add_edge((k0, 0), (k1, 2), weight=8)
                    G.add_edge((k0, 2), (k1, 2), weight=1)
                else:
                    G.add_edge((k0, 0), (k1, 0), weight=1)
                    G.add_edge((k0, 2), (k1, 2), weight=1)
                    G.add_edge((k0, 0), (k1, 2), weight=8)
                    G.add_edge((k0, 2), (k1, 0), weight=8)
    path = nx.shortest_path(G, ((0, 0), 0), (target, 0), 'weight')
    return nx.path_weight(G, path, 'weight')
