import sys

ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}


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

    xr = min(x for x, y in g), max(x for x, y in g)
    yr = min(y for x, y in g), max(y for x, y in g)
    tilt(lambda p: [(i, p[1]) for i in range(p[0])])
    tilt(lambda p: [(p[0], i) for i in range(p[1])])
    tilt(lambda p: [(i, p[1]) for i in range(xr[1], p[0], -1)])
    tilt(lambda p: [(p[0], i) for i in range(yr[1], p[1], -1)])
    return sum(xr[1] + 1 - x for (x, _), v in g.items() if v == 'O'), tuple(g.items())


grid = tuple(g.items())
seen = {}
i = 0
goal = 1000000000
while i < goal:
    if grid in seen:
        goal = goal - (goal - i) // (i - seen[grid]) * (i - seen[grid])
    seen[grid] = i
    load, grid = spin(grid)
    i += 1
print(load)
