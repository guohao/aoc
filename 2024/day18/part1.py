import itertools
import re
import sys

import networkx as nx

G = nx.Graph()
for i, j in itertools.product(range(71), repeat=2):
    k = i, j
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nbx, nby = i + dx, j + dy
        if 0 <= nbx <= 70 and 0 <= nby <= 70:
            G.add_edge(k, (nbx, nby))
for line in sys.stdin.readlines()[:1024]:
    x, y = list(map(int, re.findall(r'-?\d+', line)))
    G.remove_node((x, y))
print(nx.shortest_path_length(G, (0, 0), (70, 70)))
