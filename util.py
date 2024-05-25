import itertools
import math
import re
from functools import reduce


def d2p(data: str):
    return data.split('\n\n')


def d2g(data: str):
    g = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            g[i, j] = c
    return g


def d2ig(data: str):
    return {k: int(v) for k, v in d2g(data).items()}


def neighbors_2d_4(x, y):
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        yield x + dx, y + dy


def neighbors_2d_8(x, y):
    for dx, dy in itertools.product(range(-1, 2), repeat=2):
        if dx == dy == 0:
            continue
        yield x + dx, y + dy


def hex_neighbors_without_ns(x, y, z):
    directions = {'e': (1, -1, 0), 'w': (-1, 1, 0),
                  'ne': (1, 0, -1), 'sw': (-1, 0, 1),
                  'nw': (0, 1, -1), 'se': (0, -1, 1)}
    for dx, dy, dz in directions.values():
        yield x + dx, y + dy, z + dz


def dest_of_hex_walk(path: list[str], start: tuple[int, int, int] = (0, 0, 0)) -> tuple[int, int, int]:
    return list(hex_walk(path, start))[-1]


def hex_walk(path, start=(0, 0, 0), ):
    directions = {'n': (1, 1, 0), 's': (-1, -1, 0),
                  'e': (1, -1, 0), 'w': (-1, 1, 0),
                  'ne': (1, 0, -1), 'sw': (-1, 0, 1),
                  'nw': (0, 1, -1), 'se': (0, -1, 1)}
    x, y, z = start
    for move in path:
        dx, dy, dz = directions[move]
        x, y, z = x + dx, y + dy, z + dz
        yield x, y, z


def range_of_grid_3(g):
    rx = min(x for x, _, _ in g), max(x for x, _, _ in g)
    ry = min(y for _, y, _ in g), max(y for _, y, _ in g)
    rz = min(z for _, _, z in g), max(z for _, _, z in g)
    return rx, ry, rz


def ints(line: str):
    return list(map(int, re.findall(r'\d+', line)))


def digits(line: str):
    return list(map(int, re.findall(r'\d', line)))


def grid_of(data: str):
    g = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c != '.' and not c.isdigit():
                g[i, j] = c
    return g


def range_of_grid_2(g):
    rx = min(x for x, _ in g), max(x for x, _ in g)
    ry = min(y for _, y in g), max(y for _, y in g)
    return rx, ry,


def median(ns: list[int]):
    ns = sorted(ns)
    n = len(ns)
    if n % 2 == 0:
        return (ns[n // 2] + ns[n // 2 + 1]) // 2
    else:
        return ns[n // 2]


def lcm(l):
    return reduce(math.lcm, l)
