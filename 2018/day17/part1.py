import re
import sys

sys.setrecursionlimit(10000)

G = {}

for line in sys.stdin.readlines():
    d = {}
    for cell in line.split(', '):
        l, r = cell.split('=')
        d[l] = list(map(int, re.findall(r'\d+', r)))
    for i in range(d['x'][0], d['x'][-1] + 1):
        for j in range(d['y'][0], d['y'][-1] + 1):
            G[i, j] = '#'

MIN_X, MAX_X = min(x for x, _ in G), max(x for x, _ in G)
MIN_Y, MAX_Y = min(y for _, y in G), max(y for _, y in G)

print(MIN_Y, MAX_Y)


def drop(x, y):
    if y > MAX_Y:
        return
    if G.get((x, y), '.') in '~|#':
        return
    if y >= MIN_Y:
        G[x, y] = '|'
    drop(x, y + 1)
    if G.get((x, y + 1), '.') in '~#':
        drop(x - 1, y)
        drop(x + 1, y)
        lx = x - 1
        while G.get((lx, y), '.') == '|':
            lx -= 1
        rx = x + 1
        while G.get((rx, y), '.') == '|':
            rx += 1
        if G.get((rx, y), '.') in '~#' and G.get((lx, y), '.') in '~#':
            for k in range(lx + 1, rx):
                G[k, y] = '~'


drop(500, 0)
print(sum(v in '~|' for v in G.values()))
