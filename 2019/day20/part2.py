import heapq
from collections import defaultdict

import networkx as nx

import sys

data = sys.stdin.read()

g = {}
X = len(data.splitlines())
Y = len(data.splitlines()[0])
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '.' or c.isupper():
            g[i, j] = c
G = nx.Graph()
outs = {}
ins = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '.':
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nb = (i + dx, j + dy)
                if nb in g and g[nb] == '.':
                    G.add_edge(nb, (i, j))
        elif c.isupper():
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nb = (i + dx, j + dy)
                if nb in g and g[nb].isupper():
                    p = (nb[0] + dx, nb[1] + dy)
                    if p in g:
                        pair = ''.join(sorted(c + data.splitlines()[nb[0]][nb[1]]))
                        if 1 < i - dx < X - 1 and 1 < j - dy < Y - 1:
                            ins[pair] = p
                        else:
                            outs[pair] = p
                        break
trans = {}
for o in ins:
    trans[outs[o]] = (ins[o], -1)
    trans[ins[o]] = (outs[o], 1)
paths = defaultdict(dict)

for a in list(outs.values()) + list(ins.values()):
    for b in list(outs.values()) + list(ins.values()):
        if a == b:
            continue
        if nx.has_path(G, a, b):
            paths[a][b] = nx.shortest_path_length(G, a, b)
            paths[b][a] = paths[a][b]
q = []
heapq.heapify(q)

start = outs['AA']
target = outs['ZZ']

del paths[target]
for p in paths:
    if start in paths[p]:
        del paths[p][start]

q.append((0, 0, start))
while q:
    steps, lvl, node = heapq.heappop(q)
    reaches = paths[node].copy()
    if lvl == 0:
        if target in reaches:
            print(steps + paths[node][target])
            break
        for o in outs.values():
            if o in reaches:
                del reaches[o]
    else:
        if target in reaches:
            del reaches[target]
    steps += 1
    for n in reaches:
        p, diff = trans[n]
        heapq.heappush(q, (steps + reaches[n], lvl + diff, p))
