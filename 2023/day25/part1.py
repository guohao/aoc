import itertools
import sys

import networkx as nx

graph = nx.DiGraph()
for line in sys.stdin.readlines():
    left, right = line.split(':')
    for y in right.split():
        graph.add_edge(left, y, capacity=1)
        graph.add_edge(y, left, capacity=1)

for a, b in itertools.combinations(graph.nodes, 2):
    cut_c, (left, right) = nx.minimum_cut(graph, a, b)
    if cut_c == 3:
        print(len(left) * len(right))
        break
