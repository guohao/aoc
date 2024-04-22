import itertools
import math


def p1(data: str):
    N = 5
    g = {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}
    seen = set()
    for t in itertools.count():
        snapshot = tuple(g.values())
        if snapshot in seen:
            ans = 0
            base = 0
            for i, j in itertools.product(range(N), repeat=2):
                if g[i, j] == '#':
                    ans += math.pow(2, base)
                base += 1
            return int(ans)
        seen.add(snapshot)
        ng = {}
        for i, j in itertools.product(range(N), repeat=2):
            bc = 0
            ec = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nb = i + dx, j + dy
                if nb in g:
                    if g[nb] == '#':
                        bc += 1
                    else:
                        ec += 1
            if (g[i, j] == '#' and bc == 1) or (g[i, j] == '.' and bc in (1, 2)):
                ng[i, j] = '#'
            else:
                ng[i, j] = '.'
        g = ng


def p2(data: str):
    N = 5
    gs = {
        0: {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)},
    }
    for _ in range(200):
        ng = {min(gs.keys()) - 1: {(i, j): '.' for i, j in itertools.product(range(N), repeat=2)},
              max(gs.keys()) + 1: {(i, j): '.' for i, j in itertools.product(range(N), repeat=2)}}

        for t in sorted(gs.keys()):
            g = gs[t]
            for i, j in itertools.product(range(N), repeat=2):
                bc = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nb = i + dx, j + dy
                    if nb == (2, 2):
                        ig = gs[t - 1]
                        if dx == 0 and dy == -1:
                            bc += sum(1 for x in range(N) if ig[x, N - 1] == '#')
                        elif dx == 0 and dy == 1:
                            bc += sum(1 for x in range(N) if ig[x, 0] == '#')
                        elif dx == 1 and dy == 0:
                            bc += sum(1 for x in range(N) if ig[0, x] == '#')
                        elif dx == -1 and dy == 0:
                            bc += sum(1 for x in range(N) if ig[N - 1, x] == '#')
                    elif nb in g:
                        if g[nb] == '#':
                            bc += 1
                    else:
                        og = gs[t + 1]
                        if dx == 0 and dy == -1:
                            bc += int(og[1, 2] == '#')
                        elif dx == 0 and dy == 1:
                            bc += int(og[3, 2] == '#')
                        elif dx == 1 and dy == 0:
                            bc += int(og[2, 1] == '#')
                        elif dx == -1 and dy == 0:
                            bc += int(og[2, 3] == '#')
                if (g[i, j] == '#' and bc == 1) or (g[i, j] == '.' and bc in (1, 2)):
                    ng[i, j] = '#'
                else:
                    ng[i, j] = '.'
        g = ng
