import sys
from collections import deque
from itertools import count

import networkx as nx

g = nx.Graph()
lines = sys.stdin.readlines()
nodes = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != ' ':
            nodes[i, j] = lines[i][j]
for n in nodes:
    if nodes[n].isalpha():
        continue
    nbs = []
    if nodes[n] == '+':
        nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    elif nodes[n] == '|':
        nbs = [(0, 1), (0, -1)]
    else:
        nbs = [(1, 0), (-1, 0)]
    for i, j in nbs:
        nb = n[0] + i, n[1] + j
        if nb in nodes:
            g.add_edge(n, nb)

start = (0, 0)
for j in count():
    if (0, j) in nodes:
        start = 0, j
        break
q = deque([start])
ans = 0
d = (1, 0)
while q:
    ans += 1
    u = q.popleft()
    for nd in [d, (-d[1], d[0]), (d[1], -d[0])]:
        v = u[0] + nd[0], u[1] + nd[1]
        if v in nodes:
            q.append(v)
            d = nd
            break

print(ans)
