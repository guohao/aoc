import networkx as nx
from helper import *

data = raw_data(2023, 23)
lines = lines(data)

g: nx.DiGraph = nx.DiGraph()
start = (0, lines[0].index("."))
goal = (len(lines[0]) - 1, lines[-1].index("."))
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] != "#":
                g.add_edge((r, c), (nr, nc), weight=1)

while [1 for n, nbrsdict in g.adjacency() if len(nbrsdict) == 2]:
    for n, nbrsdict in g.adjacency():
        if len(nbrsdict) == 2:
            a, b = nbrsdict.items()
            g.remove_edge(a[0], n)
            g.remove_edge(b[0], n)
            g.remove_edge(n, a[0])
            g.remove_edge(n, b[0])

            g.add_edge(a[0], b[0],
                       weight=a[1]['weight'] + b[1]['weight'])
            g.add_edge(b[0], a[0],
                       weight=a[1]['weight'] + b[1]['weight'])

ans = 0
for p in nx.all_simple_paths(g, start, goal):
    dis = 0
    for i in range(len(p) - 1):
        dis += g.get_edge_data(p[i], p[i + 1])['weight']
    ans = max(ans, dis)

print(ans)
