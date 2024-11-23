import sys

import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]
g = nx.DiGraph()
for line in lines:
    if '->' in line:
        cells = line.replace(',', '').split()
        for c in cells[3:]:  g.add_edge(cells[0], c);
print(next(nx.topological_sort(g)))
