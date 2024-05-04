import itertools
import re
from collections import defaultdict, Counter


def p1(data: str):
    directions = {'e': (1, -1, 0), 'w': (-1, 1, 0),
                  'ne': (1, 0, -1), 'sw': (-1, 0, 1),
                  'nw': (0, 1, -1), 'se': (0, -1, 1)}

    def move_hex(moves):
        x, y, z = 0, 0, 0
        for move in moves:
            dx, dy, dz = directions[move]
            x, y, z = x + dx, y + dy, z + dz
        return x, y, z

    tiles = defaultdict(int)
    for line in data.splitlines():
        p = move_hex(re.findall(r'se|sw|ne|nw|e|w', line))
        tiles[p] = 1 - tiles[p]
    return sum(tiles.values())


def p2(data: str):
    directions = {'e': (1, -1, 0), 'w': (-1, 1, 0),
                  'ne': (1, 0, -1), 'sw': (-1, 0, 1),
                  'nw': (0, 1, -1), 'se': (0, -1, 1)}

    def move_hex(moves):
        x, y, z = 0, 0, 0
        for move in moves:
            dx, dy, dz = directions[move]
            x, y, z = x + dx, y + dy, z + dz
        return x, y, z

    tiles = {}
    for line in data.splitlines():
        p = move_hex(re.findall(r'se|sw|ne|nw|e|w', line))
        if p in tiles:
            del tiles[p]
        else:
            tiles[p] = 1
    for i in range(100):
        nt = {}
        nx = range(min(x for x, _, _ in tiles) - 1, max(x for x, _, _ in tiles) + 2)
        ny = range(min(y for _, y, _ in tiles) - 1, max(y for _, y, _ in tiles) + 2)
        nz = range(min(z for _, _, z in tiles) - 1, max(z for _, _, z in tiles) + 2)
        for p in itertools.product(nx, ny, nz):
            blacks = 0
            for dx, dy, dz in directions.values():
                nb = p[0] + dx, p[1] + dy, p[2] + dz
                if nb in tiles and tiles[nb]:
                    blacks += 1
            prev = int(p in tiles)
            if prev:
                nt[p] = 1
            if prev == 1 and (blacks == 0 or blacks > 2):
                del nt[p]
            if prev == 0 and blacks == 2:
                nt[p] = 1
        tiles = nt
    return sum(tiles.values())
