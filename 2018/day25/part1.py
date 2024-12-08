import re
import sys

import networkx as nx


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def is_same(a, b):
    return sum(abs(a[i] - b[i]) for i in range(4)) <= 3


G = nx.Graph()
for line in sys.stdin.readlines():
    G.add_node(tuple(ints(line)))
for a in G.nodes():
    for b in G.nodes():
        if a == b:
            continue
        if is_same(a,b):
            G.add_edge(a,b)
print(len(list(nx.connected_components(G))))
