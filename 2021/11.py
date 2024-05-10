import itertools

import myutil


def p1(data: str):
    g = myutil.d2ig(data)
    ans = 0
    for _ in range(100):
        flashed = set()
        g = {k: v + 1 for k, v in g.items()}
        while any(v > 9 and k not in flashed for k, v in g.items()):
            for n in g:
                if g[n] > 9 and n not in flashed:
                    for nb in myutil.neighbors_2d_8(*n):
                        if nb in g:
                            g[nb] += 1
                    flashed.add(n)
        for n in flashed:
            g[n] = 0
        ans += len(flashed)
    return ans


def p2(data: str):
    g = myutil.d2ig(data)
    for t in itertools.count(1):
        print(t)
        flashed = set()
        g = {k: v + 1 for k, v in g.items()}
        while any(v > 9 and k not in flashed for k, v in g.items()):
            for n in g:
                if g[n] > 9 and n not in flashed:
                    for nb in myutil.neighbors_2d_8(*n):
                        if nb in g:
                            g[nb] += 1
                    flashed.add(n)
        for n in flashed:
            g[n] = 0
        if len(flashed) == len(g):
            return t
