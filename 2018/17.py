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


def p1(data: str):
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
        q.append((500, 0))
        while q:
            k = q.pop()
            x, y = k
            if y > max_y:
                continue
            if is_solid(x, y):
                continue
            if k not in G and y >= min_y:
                G[x, y] = '|'
            if y + 1 > max_y:
                continue
            if (x, y + 1) not in G:
                if y >= min_y:
                    q.append(k)
                q.append((x, y + 1))
                continue
            if not is_solid(x, y + 1):
                continue
            xl = x - 1
            while (xl, y) in G and G[xl, y] == '|':
                xl -= 1
            xr = x + 1
            while (xr, y) in G and G[xr, y] == '|':
                xr += 1
            if is_solid(xl, y) and is_solid(xr, y):
                for i in range(xl + 1, xr):
                    G[i, y] = '~'
                continue
            else:
                if not ((x + 1, y) in G and (x - 1, y) in G):
                    q.append(k)
                if (x + 1, y) not in G:
                    q.append((x + 1, y))
                if (x - 1, y) not in G:
                    q.append((x - 1, y))

    drop()
    return sum(v in '~|' for v in G.values())


data = """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""
print(p1(data))
