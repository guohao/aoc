import sys
import re
import networkx as nx

g = nx.Graph()

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
nodes = {}
X = Y = 0
for line in lines[2:]:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    if nums[-1] > 95:
        continue
    nodes[nums[0], nums[1]] = nums[-4:]
    X = max(X, nums[0])
    Y = max(Y, nums[1])

cap = max(x[2] for x in nodes.values())
start = None
for p in nodes:
    if nodes[p][2] == cap:
        start = p
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nb = p[0] + i, p[1] + j
        if nb in nodes:
            g.add_edge(p, nb)
stl = nx.shortest_path_length(g, start, (0, 0))
ltr = nx.shortest_path_length(g, (0, 0), (X, 0))
print(stl + (ltr - 1) * 5 + ltr)
