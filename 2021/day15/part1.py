import sys

import networkx as nx

data = sys.stdin.read().strip()

N = len(data.splitlines())
origin_grid = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        origin_grid[i, j] = int(c)
g = nx.DiGraph()
for (x, y), weight in origin_grid.items():
    for i in range(5):
        for j in range(5):
            ew = weight + i + j
            if ew > 9:
                ew -= 9
            g.add_node((x + i * N, y + j * N), v=ew)

ew = nx.get_node_attributes(g, 'v')
for n in g:
    x, y = n
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nb = x + dx, y + dy
        if nb in g:
            g.add_edge(nb, n, v=ew[n])
goal = (max(x for x, _ in g), max(y for _, y in g))
p = list(nx.shortest_path(g, (0, 0), goal, weight='v'))
print(nx.path_weight(g, p, 'v'))
