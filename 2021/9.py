import math

import myutil


def p1(data: str):
    ans = 0
    g = myutil.d2ig(data)
    for n in g:
        if all(g[nb] > g[n] for nb in myutil.neighbors_2d_4(*n) if nb in g):
            ans += g[n] + 1
    return ans


def p2(data: str):
    g = myutil.d2ig(data)
    mx = max(x for x, _ in g)
    my = max(y for _, y in g)
    seen = set()
    basins = []

    def bfs(x, y):
        if (x, y) not in g:
            return
        if (x, y) in seen:
            return
        if g[x, y] == 9:
            return
        seen.add((x, y))
        for nx, ny in myutil.neighbors_2d_4(x, y):
            bfs(nx, ny)

    for i in range(mx + 1):
        for j in range(my + 1):
            pre_size = len(seen)
            bfs(i, j)
            basins.append(len(seen) - pre_size)

    return math.prod(sorted(basins)[-3:])
