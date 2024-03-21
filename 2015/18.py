import itertools


def solve(data: str, corner_stuck_on=False):
    n = 100
    g = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            g[i, j] = c
    if corner_stuck_on:
        for i, j in itertools.product([0, n - 1], [0, n - 1]):
            g[i, j] = '#'

    def next_step():
        ng = {}
        for (i, j), state in g.items():
            n_on = 0
            for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
                if dx == 0 and dy == 0:
                    continue
                if (dx + i, dy + j) in g and g[dx + i, dy + j] == '#':
                    n_on += 1
            if g[i, j] == '#' and n_on in {2, 3} or g[i, j] == '.' and n_on == 3:
                ng[i, j] = '#'
            else:
                ng[i, j] = '.'
        if corner_stuck_on:
            for i, j in itertools.product([0, n - 1], [0, n - 1]):
                ng[i, j] = '#'
        return ng

    for _ in range(100):
        g = next_step()
    return list(g.values()).count('#')


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, True)
