from functools import cache

from util import *


def p1(data: str):
    g = grid_of(data)
    for p in g:
        if g[p] == 'O':
            for i in range(p[0]):
                if g[i, p[1]] == '.' and not any(g[k, p[1]] == '#' for k in range(i, p[0])):
                    g[i, p[1]] = 'O'
                    g[p] = '.'
                    break

    xr, _ = range_of_grid_2(g)
    max_load = xr[1] + 1

    return sum(max_load - x for (x, _), v in g.items() if v == 'O')


def p2(data: str):
    def spin(gt):
        g = dict(gt)

        def op():
            for p in g:
                if g[p] == 'O':
                    yield p

        def tilt(tsf):
            for a in op():
                ts = tsf(a)
                for i, b in enumerate(ts):
                    if g[b] == '.' and not any(g[ts[ib]] == '#' for ib in range(i, len(ts))):
                        g[b] = 'O'
                        g[a] = '.'
                        break

        xr, yr = range_of_grid_2(g)
        tilt(lambda p: [(i, p[1]) for i in range(p[0])])
        tilt(lambda p: [(p[0], i) for i in range(p[1])])
        tilt(lambda p: [(i, p[1]) for i in range(xr[1], p[0], -1)])
        tilt(lambda p: [(p[0], i) for i in range(yr[1], p[1], -1)])
        return sum(xr[1] + 1 - x for (x, _), v in g.items() if v == 'O'), tuple(g.items())

    grid = tuple(grid_of(data).items())
    seen = {}
    i = 0
    goal = 1000000000
    while i < goal:
        if grid in seen:
            goal = goal - (goal - i) // (i - seen[grid]) * (i - seen[grid])
        seen[grid] = i
        load, grid = spin(grid)
        i += 1
    return load
