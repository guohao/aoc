import sys
import re
import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]
g = nx.Graph()
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    for b in nums[1:]:
        g.add_edge(nums[0], b)

print(len(nx.node_connected_component(g,0)))