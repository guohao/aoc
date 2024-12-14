import re
import sys
import networkx as nx

data = sys.stdin.read().strip()

G = nx.DiGraph()
for line in data.splitlines():
    parent = re.findall(r'\w+ \w+ bag', line)[0]
    children = re.findall(r'\d+ \w+ \w+ bag', line)
    for bag in children:
        if bag == "no other bag":
            continue
        cnt = int(bag.split()[0])
        name = ' '.join(bag.split()[1:])
        G.add_edge(parent, name, v=cnt)


def req(node):
    ans = 0
    for _, t in G.out_edges(node):
        ans += G.get_edge_data(node, t)['v'] * (req(t) + 1)
    return ans


print(req("shiny gold bag"))
