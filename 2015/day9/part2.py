import itertools
import math

import networkx as nx

g = nx.Graph()
while True:
    line = input()
    if not line:
        break
    f, t, d = line.split()[0::2]
    g.add_edge(f, t, weight=int(d))

max_cost = -math.inf
for path in itertools.permutations(g.nodes):
    max_cost = max(max_cost, nx.path_weight(g, list(path), weight='weight'))
print(max_cost)
