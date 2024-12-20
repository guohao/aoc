import math
import sys

import networkx as nx

ls = [l.strip() for l in sys.stdin.readlines()]
N = len(ls)
M = len(ls[0])
g = {(i, j): c for i, line in enumerate(ls) for j, c in enumerate(line)}
start = next(x for x in g if g[x] == 'S')
target = next(x for x in g if g[x] == 'E')
G = nx.grid_2d_graph(N, M)
for i, j in g:
    if g[i, j] == '#':
        G.remove_node((i, j))
m = nx.shortest_path_length(G, start, target)
start_dis = nx.single_source_dijkstra_path_length(G, start)
end_dis = nx.single_source_dijkstra_path_length(G, target)

t = 0
NG = nx.grid_2d_graph(N, M)
for s in start_dis:
    if g[s] == '#':
        continue
    cheats = nx.single_source_dijkstra_path_length(NG, s, cutoff=20)
    for ce, step in cheats.items():
        if g[ce] == '#':
            continue
        save = m - start_dis[s] - end_dis.get(ce, math.inf) - step
        if save >= 100:
            t += 1
print(t)
