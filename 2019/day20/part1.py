import sys

import networkx as nx

data = sys.stdin.read()

g = {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}
l2p = {}
G = nx.Graph()
for (i, j), c in g.items():
    if c != '.':
        continue
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nb = i + dx, j + dy
        if nb not in g or g[nb] == '#':
            continue
        if g[nb] == '.':
            G.add_edge(nb, (i, j))
        else:
            nb2 = i + dx * 2, j + dy * 2
            pair = ''.join(sorted([g[nb], g[nb2]]))
            print(pair, i, j)
            if pair in l2p:
                G.add_edge(l2p[pair], (i, j))
            else:
                l2p[pair] = (i, j)
print(nx.shortest_path_length(G, l2p['AA'], l2p['ZZ']))
