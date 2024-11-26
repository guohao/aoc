import sys

import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]
g = nx.DiGraph()
for line in lines:
    a = line.split()[1]
    b = line.split()[-3]
    g.add_edge(a,b)
print(''.join(nx.lexicographical_topological_sort(g)))
