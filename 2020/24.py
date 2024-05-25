import util
import itertools
import re


def build_black_grid(data: str):
    tiles = set()
    for line in data.splitlines():
        path = re.findall(r'se|sw|ne|nw|e|w', line)
        dest = myutil.dest_of_hex_walk(path)
        if dest in tiles:
            tiles.remove(dest)
        else:
            tiles.add(dest)
    return tiles


def p1(data: str):
    return len(build_black_grid(data))


def p2(data: str):
    tiles = build_black_grid(data)

    def gen_next(g):
        ng = set()
        rx, ry, rz = list(map(lambda r: range(r[0] - 1, r[1] + 2), myutil.range_of_grid_3(g)))
        for p in itertools.product(rx, ry, rz):
            blacks = sum(nb in g for nb in myutil.hex_neighbors_without_ns(*p))
            if p in g and not (blacks == 0 or blacks > 2):
                ng.add(p)
            if p not in g and blacks == 2:
                ng.add(p)
        return ng

    for i in range(100):
        tiles = gen_next(tiles)
    return len(tiles)
