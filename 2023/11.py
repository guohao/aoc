from util import *


def solve(data: str, expand: int):
    g = grid_of(data)
    xr, yr = range_of_grid_2(g)
    empty_cols = set(y for (_, y), v in g.items() if all(g[x, y] == '.' for x in range(xr[0], xr[1] + 1)))
    empty_rows = set(x for (x, _), v in g.items() if all(g[x, y] == '.' for y in range(yr[0], yr[1] + 1)))
    ans = 0
    gs = [p for p, c in g.items() if c == '#']
    for i in range(len(gs)):
        x0, y0 = gs[i]
        for j in range(i + 1, len(gs)):
            x1, y1 = gs[j]
            ecc = set(range(min(x0, x1), max(x0, x1) + 1)) & empty_rows
            erc = [y for y in range(min(y0, y1), max(y0, y1) + 1) if y in empty_cols]
            ans += abs(x1 - x0) + abs(y1 - y0) + len(ecc) * (expand - 1) + len(erc) * (expand - 1)
    return ans


def p1(data: str):
    return solve(data, 2)


def p2(data: str):
    return solve(data, 1000000)
