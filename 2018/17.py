import re
import sys

sys.setrecursionlimit(10000)


def solve(data: str):
    G = {}

    def build_g():
        for line in data.splitlines():
            d = {}
            for cell in line.split(', '):
                l, r = cell.split('=')
                rg = list(map(int, re.findall(r'\d+', r)))
                d[l] = rg
            for x in range(d['x'][0], d['x'][-1] + 1):
                for y in range(d['y'][0], d['y'][-1] + 1):
                    G[x, y] = '#'

    build_g()
    min_y = min(y for _, y in G)
    max_y = max(y for _, y in G)

    def is_solid(x, y):
        return (x, y) in G and G[x, y] in '~#'

    def drop(x, y):
        if (x, y) in G:
            return
        G[x, y] = '|'
        if y > max_y:
            return
        drop(x, y + 1)
        if not is_solid(x, y + 1):
            return
        drop(x - 1, y)
        drop(x + 1, y)
        xl = x - 1
        while (xl, y) in G and G[xl, y] == '|':
            xl -= 1
        xr = x + 1
        while (xr, y) in G and G[xr, y] == '|':
            xr += 1
        if is_solid(xl, y) and is_solid(xr, y):
            for i in range(xl + 1, xr):
                G[i, y] = '~'

    drop(500, 0)
    return [v for (_, y), v in G.items() if min_y <= y <= max_y]


def p1(data: str):
    return sum(v in '~|' for v in solve(data))


def p2(data: str):
    return sum(v == '~' for v in solve(data))
