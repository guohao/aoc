import math
import re
import networkx as nx
import sys

data = sys.stdin.read().strip()

G = nx.DiGraph()
for line in data.splitlines():
    f, t = line.split(' => ')
    tc, tn = t.split()
    tc = int(tc)
    for cell in f.split(', '):
        fc, fn = cell.split()
        fc = int(fc)
        G.add_edge(tn, fn, cost=(fc, tc))

needs = {'FUEL': 1}
for tn in nx.topological_sort(G):
    need = needs[tn]
    for fn in G.successors(tn):
        fc, tc = G.get_edge_data(tn, fn)['cost']
        if fn not in needs:
            needs[fn] = 0
        needs[fn] += need / tc * fc
print(int(1000000000000 // needs['ORE']))
