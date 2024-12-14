import itertools
import re
import sys


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


data = sys.stdin.read().strip()


def build_black_grid(data: str):
    tiles = set()
    for line in data.splitlines():
        path = re.findall(r'se|sw|ne|nw|e|w', line)
        dest = dest_of_hex_walk(path)
        if dest in tiles:
            tiles.remove(dest)
        else:
            tiles.add(dest)
    return tiles


tiles = build_black_grid(data)


def range_of_grid_3(g):
    rx = min(x for x, _, _ in g), max(x for x, _, _ in g)
    ry = min(y for _, y, _ in g), max(y for _, y, _ in g)
    rz = min(z for _, _, z in g), max(z for _, _, z in g)
    return rx, ry, rz


def hex_neighbors_without_ns(x, y, z):
    directions = {'e': (1, -1, 0), 'w': (-1, 1, 0),
                  'ne': (1, 0, -1), 'sw': (-1, 0, 1),
                  'nw': (0, 1, -1), 'se': (0, -1, 1)}
    for dx, dy, dz in directions.values():
        yield x + dx, y + dy, z + dz


def gen_next(g):
    ng = set()
    rx, ry, rz = list(map(lambda r: range(r[0] - 1, r[1] + 2), range_of_grid_3(g)))
    for p in itertools.product(rx, ry, rz):
        blacks = sum(nb in g for nb in hex_neighbors_without_ns(*p))
        if p in g and not (blacks == 0 or blacks > 2):
            ng.add(p)
        if p not in g and blacks == 2:
            ng.add(p)
    return ng


for i in range(100):
    tiles = gen_next(tiles)
print(len(tiles))
