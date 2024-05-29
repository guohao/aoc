from heapq import *

from util import *


def dfs(data: str, min_step, max_step):
    g = int_grid(data)
    (_, xm), (_, ym) = range_of_grid_2(g)
    goal = xm, ym
    pq = [(0, (0, 0), (0, 0), min_step)]
    visited = set()
    while pq:
        heat_lost, p, d, step = heappop(pq)
        if (p, d, step) in visited:
            continue
        visited.add((p, d, step))
        if p == goal:
            return heat_lost
        for nd in set(ds_4()) - {(-d[0], -d[1])}:
            if d == nd and step == max_step:
                continue
            if d != nd and step < min_step:
                continue
            ns = step + 1 if d == nd else 1
            np = (p[0] + nd[0], p[1] + nd[1])
            if np in g:
                heappush(pq, (heat_lost + g[np], np, nd, ns))


def p1(data: str):
    return dfs(data, 1, 3)


def p2(data: str):
    return dfs(data, 4, 10)
