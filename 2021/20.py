import itertools
from functools import cache

import util


def solve(data: str, t):
    parts = data.split('\n\n')
    iea = parts[0].replace('\n', '')
    assert len(iea) == 512
    g = myutil.d2g(parts[1])

    @cache
    def st(ix, iy, it):
        if it == 0:
            return v(ix, iy)
        bs = ''.join(
            str(int(st(ix + kx, iy + ky, it - 1) == '#')) for kx, ky in itertools.product(range(-1, 2), repeat=2))
        return iea[int(bs, 2)]

    def v(ix, iy):
        if (ix, iy) in g:
            return g[ix, iy]
        return '.'

    (min_x, max_x), (min_y, max_y) = myutil.range_of_grid_2(g)
    ans = 0
    for i in range(min_x - 2 * t, max_x + 2 * t):
        for j in range(min_y - 2 * t, max_y + 2 * t):
            if st(i, j, t) == '#':
                ans += 1
    return ans


def p1(data: str):
    return solve(data, 2)


def p2(data: str):
    return solve(data, 50)
