import itertools
import sys
from functools import cache

t = 50
parts = sys.stdin.read().split('\n\n')
iea = parts[0].replace('\n', '')
g = {(i, j): c for i, line in enumerate(parts[1].splitlines()) for j, c in enumerate(line.strip())}


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


min_x, max_x = min(x for x, y in g), max(x for x, y in g)
min_y, max_y = min(y for x, y in g), max(y for x, y in g)
ans = 0
for i in range(min_x - 2 * t, max_x + 2 * t):
    for j in range(min_y - 2 * t, max_y + 2 * t):
        if st(i, j, t) == '#':
            ans += 1
print(ans)
