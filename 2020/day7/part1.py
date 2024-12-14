import re

import networkx as nx

import sys

data = sys.stdin.read().strip()

G = nx.DiGraph()
for line in data.splitlines():
    bags = re.findall(r'\w+ \w+ bag', line)
    for bag in bags[1:]:
        G.add_edge(bags[0], bag)
ans = 0
for n in G.nodes:
    if n == "shiny gold bag":
        continue
    if nx.has_path(G, n, "shiny gold bag"):
        ans += 1
print(ans)
