import sys

import networkx as nx

data = sys.stdin.read().strip()

g = nx.DiGraph()
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        g.add_node((i, j), v=int(c))
weight = nx.get_node_attributes(g, 'v')
goal = (max(x for x, _ in g), max(y for _, y in g))
for n in g:
    x, y = n
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nb = x + dx, y + dy
        if nb in g:
            g.add_edge(nb, n, v=weight[n])
p = list(nx.shortest_path(g, (0, 0), goal, weight='v'))
print(nx.path_weight(g, p, 'v'))
