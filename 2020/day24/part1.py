import re


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


import sys
data = sys.stdin.read().strip()
print(len(build_black_grid(data)))

