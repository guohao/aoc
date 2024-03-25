import itertools
import math

import networkx as nx


def p1(data: str):
    G = nx.Graph()
    targets = []
    start = (-1, -1)
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                continue
            G.add_node((i, j))
            if c.isdigit():
                if c == '0':
                    start = (i, j)
                targets.append((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nb = (dx + i, dy + j)
                if G.has_node(nb):
                    G.add_edge(nb, (i, j))
    G1 = nx.Graph()
    for a in targets:
        for b in targets:
            if a == b:
                continue
            weight = nx.shortest_path_length(G, a, b)
            G1.add_edge(a, b, weight=weight)

    ans = math.inf
    others = set(targets) - {start}
    for perm in itertools.permutations(others):
        path = [start] + list(perm)
        ans = min(ans, nx.path_weight(G1, path, 'weight'))
    return ans


def p2(data: str):
    G = nx.Graph()
    targets = []
    start = (-1, -1)
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                continue
            G.add_node((i, j))
            if c.isdigit():
                if c == '0':
                    start = (i, j)
                targets.append((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nb = (dx + i, dy + j)
                if G.has_node(nb):
                    G.add_edge(nb, (i, j))
    G1 = nx.Graph()
    for a in targets:
        for b in targets:
            if a == b:
                continue
            weight = nx.shortest_path_length(G, a, b)
            G1.add_edge(a, b, weight=weight)

    ans = math.inf
    others = set(targets) - {start}
    for perm in itertools.permutations(others):
        path = [start] + list(perm) + [start]
        ans = min(ans, nx.path_weight(G1, path, 'weight'))
    return ans
