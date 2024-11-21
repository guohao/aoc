import itertools
import math

import networkx as nx

g = nx.Graph()

import sys
lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    f, t, d = line.split()[0::2]
    g.add_edge(f, t, weight=int(d))

min_cost = math.inf
for path in itertools.permutations(g.nodes):
    min_cost = min(min_cost, nx.path_weight(g, list(path), weight='weight'))
print(min_cost)
