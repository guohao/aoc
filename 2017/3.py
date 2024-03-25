import itertools


def p1(data: str):
    n = int(data)
    x, y = 0, 0
    dx, dy = 1, 0
    g = set()
    for _ in range(1, n):
        x, y = x + dx, y + dy
        g.add((x, y))
        if (x - dy, y + dx) not in g:
            dx, dy = -dy, dx

    return abs(x) + abs(y)


def p2(data: str):
    n = int(data)
    x, y = 0, 0
    dx, dy = 1, 0
    g = {}

    def sum_of_nb(i, j):
        ans = 0
        for x0, y0 in itertools.product(range(-1, 2), range(-1, 2)):
            p = (i + x0, j + y0)
            if p in g:
                ans += g[p]
        return ans

    g[0, 0] = 1
    for _ in range(1, n):
        x, y = x + dx, y + dy
        g[x, y] = sum_of_nb(x, y)
        if g[x, y] > n:
            return g[x, y]
        if (x - dy, y + dx) not in g:
            dx, dy = -dy, dx
