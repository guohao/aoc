import heapq
import sys
from heapq import heappop, heappush, heapify

import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]

g = nx.DiGraph()
for line in lines:
    a = ord(line.split()[1]) - ord('A') + 61
    b = ord(line.split()[-3]) - ord('A') + 61
    g.add_edge(a, b)

indegree = {v: d for v, d in g.in_degree() if d > 0}
zero_indegree = [v for v, d in g.in_degree() if d == 0]
heapify(zero_indegree)

workers = []

t = 0
while indegree:
    while not zero_indegree or len(workers) == 5:
        t, node = heapq.heappop(workers)
        for child in g[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                heapq.heappush(zero_indegree, child)
                del indegree[child]
    node = heapq.heappop(zero_indegree)
    heapq.heappush(workers, (t + node, node))

worker = heapq.heappop(workers)
print(worker[0])
