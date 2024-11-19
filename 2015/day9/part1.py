import itertools
import math

import networkx as nx

g = nx.Graph()
try:
    while True:
        line = input()
        f, t, d = line.split()[0::2]
        g.add_edge(f, t, weight=int(d))
except EOFError:
    pass

min_cost = math.inf
for path in itertools.permutations(g.nodes):
    min_cost = min(min_cost, nx.path_weight(g, list(path), weight='weight'))
print(min_cost)
