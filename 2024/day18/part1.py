import re
import sys

import networkx as nx

G = nx.grid_2d_graph(71, 71)
for line in sys.stdin.readlines()[:1024]:
    G.remove_node(tuple(map(int, re.findall(r'-?\d+', line))))
print(nx.shortest_path_length(G, (0, 0), (70, 70)))
