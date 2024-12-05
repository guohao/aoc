import networkx as nx

import util


def p1(data: str):
    g = nx.DiGraph()
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            g.add_node((i, j), v=int(c))
    weight = nx.get_node_attributes(g, 'v')
    goal = (max(x for x, _ in g), max(y for _, y in g))
    for n in g:
        for nb in myutil.nb4(*n):
            if nb in g:
                g.add_edge(nb, n, v=weight[n])
    p = list(nx.shortest_path(g, (0, 0), goal, weight='v'))
    return nx.path_weight(g, p, 'v')


def p2(data: str):
    N = len(data.splitlines())
    origin_grid = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            origin_grid[i, j] = int(c)
    g = nx.DiGraph()
    for (x, y), weight in origin_grid.items():
        for i in range(5):
            for j in range(5):
                ew = weight + i + j
                if ew > 9:
                    ew -= 9
                g.add_node((x + i * N, y + j * N), v=ew)

    ew = nx.get_node_attributes(g, 'v')
    for n in g:
        for nb in myutil.nb4(*n):
            if nb in g:
                g.add_edge(nb, n, v=ew[n])
    goal = N * 5 - 1, N * 5 - 1
    p = list(nx.shortest_path(g, (0, 0), goal, weight='v'))
    return nx.path_weight(g, p, 'v')

