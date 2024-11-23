import sys
from functools import cache

import networkx as nx

lines = [line.strip() for line in sys.stdin.readlines()]
g = nx.DiGraph()
for line in lines:
    cells = line.replace(',', '').split()
    g.add_node(cells[0], v=int(cells[1][1:-1]))
    if '->' in line:
        for c in cells[3:]: g.add_edge(cells[0], c);


@cache
def tw(n: str) -> int:
    return nw(n) + sum(map(tw, g[n]))


def nw(n: str) -> int:
    return nx.get_node_attributes(g, 'v')[n]


def need_to_be(es: int, root: str) -> int:
    if len(set(map(tw, g[root]))) == 1:
        return es - tw(root) + nw(root)
    ue = (es - nw(root)) // len(g[root])
    for up in g[root]:
        if ue != tw(up):
            return need_to_be(ue, up)


def solve():
    bottom = next(nx.topological_sort(g))
    vs = list(g[bottom].keys())
    for i, v in enumerate(vs):
        l, m, r = [tw(vs[(i + j) % len(vs)]) for j in range(-1, 2)]
        if l == r != m:
            print(need_to_be(l, v))
            break


solve()
