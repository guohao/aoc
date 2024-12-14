import networkx as nx

import sys

data = sys.stdin.read().strip()

g = {}
l2p = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '.' or c.isupper():
            g[i, j] = c
G = nx.Graph()
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
                        if pair in l2p:
                            G.add_edge(l2p[pair], p)
                        else:
                            l2p[pair] = p
                        break
print(nx.shortest_path_length(G, l2p['AA'], l2p['ZZ']))
