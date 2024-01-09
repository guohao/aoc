from helper import *

data = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

data = raw_data(2015, 18)


def p1():
    g = {(i, j): c for i, line in enumerate(lines(data)) for j, c in enumerate(line)}
    for _ in range(100):
        ng = {}
        for (x, y), v in g.items():

            ng[x, y] = '.'
            if v == '#':
                if sum((dx + x, dy + y) in g and g[dx + x, dy + y] == '#' for dx, dy in \
                       itertools.product([-1, 0, 1], [-1, 0, 1]) if dx != 0 or dy != 0) in [2, 3]:
                    ng[x, y] = '#'
            else:
                if sum((dx + x, dy + y) in g and g[dx + x, dy + y] == '#' for dx, dy in \
                       itertools.product([-1, 0, 1], [-1, 0, 1]) if dx != 0 or dy != 0) == 3:
                    ng[x, y] = '#'
        g = ng

    print(sum(c == '#' for c in g.values()))


def p2():
    g = {(i, j): c for i, line in enumerate(lines(data)) for j, c in enumerate(line)}
    max_x = max(x for x, _ in g.keys())
    max_y = max(y for _, y in g.keys())

    stay_on = [(0, 0), (0, max_y), (max_x, 0), (max_x, max_y)]
    for p in stay_on:
        g[p] = '#'
    for _ in range(100):
        ng = {}
        for (x, y), v in g.items():
            if (x, y) in stay_on:
                ng[x, y] = '#'
                continue
            ng[x, y] = '.'
            if v == '#':
                if sum((dx + x, dy + y) in g and g[dx + x, dy + y] == '#' for dx, dy in \
                       itertools.product([-1, 0, 1], [-1, 0, 1]) if dx != 0 or dy != 0) in [2, 3]:
                    ng[x, y] = '#'
            else:
                if sum((dx + x, dy + y) in g and g[dx + x, dy + y] == '#' for dx, dy in \
                       itertools.product([-1, 0, 1], [-1, 0, 1]) if dx != 0 or dy != 0) == 3:
                    ng[x, y] = '#'
        g = ng

    print(sum(c == '#' for c in g.values()))


p1()
p2()
