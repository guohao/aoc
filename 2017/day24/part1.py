import sys
import re
from collections import defaultdict, deque

import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]
comps = defaultdict(list)
for line in lines:
    a, b = map(int, re.findall(r'-?\d+', line))
    comps[a].append(b)
    comps[b].append(a)

q = deque([(0, frozenset())])
ans = 0
while q:
    u, visited = q.popleft()
    has_next = False
    for v in comps[u]:
        if (u, v) not in visited and (v, u) not in visited:
            q.append((v, visited | {(u, v)}))
            has_next = True
    if not has_next:
        ans = max(ans, sum(sum(x) for x in visited))
print(ans)
