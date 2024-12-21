import sys
from collections import deque

import networkx as nx

data = sys.stdin.read().strip()
g = nx.Graph()
for line in data.splitlines():
    l, r = line.split('-')
    g.add_edge(l, r)
ans = 0
q = deque()
q.append(('start',))
while q:
    p = q.popleft()
    if p[-1] == 'end':
        ans += 1
        continue
    curr = p[-1]
    for x in g.neighbors(curr):
        if x.islower() and x in p:
            continue
        q.append(p + (x,))
print(ans)