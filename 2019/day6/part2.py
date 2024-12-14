
import sys

import networkx as nx

data = sys.stdin.read().strip()

G = nx.Graph()
for line in data.splitlines():
    a, b = line.split(')')
    G.add_edge(a, b)

print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2)
