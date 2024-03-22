import itertools
import re


def p1(data: str):
    W, H = 50, 6
    g = [['.'] * W for _ in range(H)]

    def extract_rotate(s):
        return list(map(int, re.findall(r'(\d+) by (\d+)', s)[0]))

    for line in data.splitlines():
        if 'rect' in line:
            a, b = list(map(int, re.findall(r'\d+', line)))
            for i in range(b):
                for j in range(a):
                    g[i][j] = '#'
        elif 'row' in line:
            y, b = extract_rotate(line)
            lits = set((i + b) % W for i in range(W) if g[y][i] == '#')
            for i in range(W):
                g[y][i] = '#' if i in lits else '.'
        elif 'column' in line:
            x, b = extract_rotate(line)
            lits = set((i + b) % H for i in range(H) if g[i][x] == '#')
            for i in range(H):
                g[i][x] = '#' if i in lits else '.'
    for i in range(H):
        ll = ''
        for j in range(W):
            ll += g[i][j] if g[i][j] == '#' else ' '
        print(ll)
    return sum(g[i][j] == '#' for (i, j) in itertools.product(range(H), range(W)))
