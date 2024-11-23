import itertools
import sys
import networkx as nx

g = nx.Graph()
lines = [line.strip() for line in sys.stdin.readlines()]
nodes = {}

d2p = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        nodes[i, j] = lines[i][j]
        if lines[i][j].isnumeric():
            d2p[int(lines[i][j])] = i, j

for n in nodes:
    if nodes[n] == '#':
        continue
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = n[0] + i, n[1] + j
        if nb in nodes and nodes[nb] != '#':
            g.add_edge(n, nb, w=1)

sg = nx.Graph()
target_nodes = list(d2p.values())
for i, u in enumerate(target_nodes):
    for v in target_nodes[i + 1:]:
        if nx.has_path(g, u, v):
            shortest_path_length = nx.shortest_path_length(g, u, v, weight="weight")
            sg.add_edge(u, v, weight=shortest_path_length)

start = d2p[0]
del d2p[0]
ans = min(
    nx.path_weight(sg, [start] + list(c) + [start], weight='weight') for c in itertools.permutations(d2p.values()))
print(ans)
