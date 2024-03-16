import re
from collections import deque
from functools import cache


def build_g(data: str):
    G = {}
    for line in data.splitlines():
        d = {}
        for cell in line.split(', '):
            l, r = cell.split('=')
            rg = list(map(int, re.findall(r'\d+', r)))
            d[l] = rg
        for x in range(d['x'][0], d['x'][-1] + 1):
            for y in range(d['y'][0], d['y'][-1] + 1):
                G[x, y] = '#'
    return G


def solve(data: str):
    G = build_g(data)
    min_y = min(y for _, y in G)
    max_y = max(y for _, y in G)
    min_x = min(x for x, _ in G)
    max_x = max(x for x, _ in G)

    def g_print():
        for j in range(min_y, max_y + 1):
            line = ''
            for i in range(min_x - 3, max_x + 1):
                if (i, j) in G:
                    if G[i, j] == '|':
                        line += '+'
                    else:
                        line += G[i, j]
                else:
                    line += '0'
            line += f'   {j} '
            print(line)
        print('----------------------')

    def is_solid(x, y):
        return (x, y) in G and G[x, y] in '~#'

    def drop():
        q = deque()

        def drop_down(x, y) -> bool:
            if y + 1 > max_y:
                return False
            if (x, y + 1) not in G:
                q.append((x, y))
                q.append((x, y + 1))
                return False
            if not is_solid(x, y + 1):
                return False
            return True

        def drop_left(x, y, op):
            if (x + op, y) not in G:
                q.append((x, y))
                q.append((x + op, y))

        def drain_water(x, y):
            xl = x - 1
            while (xl, y) in G and G[xl, y] == '|':
                xl -= 1
            xr = x + 1
            while (xr, y) in G and G[xr, y] == '|':
                xr += 1
            if is_solid(xl, y) and is_solid(xr, y):
                for i in range(xl + 1, xr):
                    G[i, y] = '~'

        q.append((500, 0))
        while q:
            k = q.pop()
            x, y = k
            if is_solid(x, y):
                continue
            if k not in G:
                G[x, y] = '|'
            if not drop_down(x, y):
                continue
            drop_left(x, y, -1)
            drop_left(x, y, 1)
            drain_water(x, y)

    drop()
    return [v for (_, y), v in G.items() if min_y <= y <= max_y]


def p1(data: str):
    return sum(v in '~|' for v in solve(data))


def p2(data: str):
    return sum(v == '~' for v in solve(data))
