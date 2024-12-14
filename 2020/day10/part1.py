from collections import Counter
import sys

import networkx as nx

data = sys.stdin.read().strip()

G = nx.DiGraph()
for a in map(int, data.splitlines()):
    G.add_node(a)
G.add_node(0)
G.add_node(3 + max(G.nodes))
for n in G.nodes:
    for i in range(1, 4):
        if n - i in G:
            G.add_edge(n - i, n)
path = nx.dag_longest_path(G, 0, max(G.nodes))
c = Counter([path[i] - path[i - 1] for i in range(1, len(path))])
print(c[1] * c[3])
