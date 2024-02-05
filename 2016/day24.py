import networkx as nx
from helper import *

data = raw_data(2016, 24)
lines = lines(data)

G = nx.Graph()

ntv = []
start = None
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c.isdigit():
            G.add_node((i, j))
            ntv.append((i, j))
            if c == '0':
                start = (i, j)
        if c != '#':
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                np = (i + dx, j + dy)
                if 0 <= np[0] < len(lines) and 0 <= np[1] < len(line) and lines[np[0]][np[1]] != '#':
                    G.add_edge((i, j), (i + dx, j + dy))


def p1():
    def search(unv, v, d):
        if len(unv) == 0:
            return d
        return min(search(unv - {i}, i, d + nx.shortest_path_length(G, source=v, target=i)) for i in unv)

    print(search(set(ntv) - {start}, start, 0))


def p2():
    def search(unv, v, d):
        if len(unv) == 0:
            return d + nx.shortest_path_length(G, source=v, target=start)
        return min(search(unv - {i}, i, d + nx.shortest_path_length(G, source=v, target=i)) for i in unv)

    print(search(set(ntv) - {start}, start, 0))


p1()
p2()
