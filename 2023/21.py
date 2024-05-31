from util import *


def p1(data: str):
    g = d2g(data)
    s = [k for k, v in g.items() if v == 'S'][0]
    tv = [s]
    for _ in range(64):
        nv = set()
        for n in tv:
            for nb in neighbors_2d_4(*n):
                if nb in g and g[nb] != '#':
                    nv.add(nb)
        tv = nv
    return len(tv)


def p2(data: str):
    g = d2g(data)
    H = int(math.sqrt(len(g)))
    s = [k for k, v in g.items() if v == 'S'][0]
    tv = {s}
    const_num = [0, 0]
    ax = [0, 0, 0]
    steps = 26501365
    for i in range(1, steps):
        nv = set()
        for n in tv:
            for nb in neighbors_2d_4(*n):
                wrap = nb[0] % H, nb[1] % H
                if wrap in g and g[wrap] != '#':
                    nv.add(nb)
        tv = nv
        if i % H == steps % H:
            ax[i // H] = len(tv) + const_num[i % 2]
            if ax[2] != 0:
                break
    n = steps // H
    a = (ax[2] + ax[0] - 2 * ax[1]) / 2
    b = ax[1] - ax[0] - a
    c = ax[0]
    return int(a * n ** 2 + b * n + c)
