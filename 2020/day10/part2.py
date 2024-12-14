from collections import defaultdict
import sys

import networkx as nx

data = sys.stdin.read().strip()

G = nx.DiGraph()
for a in map(int, data.splitlines()):
    G.add_node(a)
G.add_node(0)
G.add_node(3 + max(G.nodes))
for n in G.nodes:
    for i in range(1, 4):
        if n - i in G:
            G.add_edge(n - i, n)
dp = defaultdict(int)
dp[0] = 1
for i in sorted(G.nodes)[1:]:
    for succ in G.predecessors(i):
        dp[i] += dp[succ]
print(dp[max(dp.keys())])
