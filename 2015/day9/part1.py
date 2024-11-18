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

min_cost = math.inf
for path in itertools.permutations(g.nodes):
    min_cost = min(min_cost, nx.path_weight(g, list(path), weight='weight'))
print(min_cost)
