import itertools
import math
import re
import string


def fr(a: list[string], flip, rotate) -> list[string]:
    if flip:
        a = a[::-1]
    for _ in range(rotate):
        a = [''.join(l[::-1]) for l in zip(*a)]
    return a


def reassemble(data: str):
    tiles = {}
    for part in data.strip().split('\n\n'):
        lines = part.splitlines()
        id = re.findall(r'\d+', lines[0])[0]
        tiles[id] = lines[1:]

    N = int(len(tiles) ** 0.5)

    def dfs(placed, i, j):
        pkv = {(px, py): (x, xf, xr) for x, xf, xr, px, py in placed}
        seen = set(x for x, _, _ in pkv.values())
        if len(placed) == len(tiles):
            return pkv
        ava = [x for x in tiles if x not in seen]

        for x, flip, rotate in itertools.product(ava, [0, 1], range(4)):
            t = fr(tiles[x], flip, rotate)
            placeable = True
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nb = di + i, dj + j
                if nb in pkv:
                    nbt, nbf, nbr = pkv[nb]
                    nbt = fr(tiles[nbt], nbf, nbr)
                    if (di, dj) == (0, 1) and list(zip(*nbt))[0] != list(zip(*t))[-1] or (di, dj) == (1, 0) and nbt[
                        0] != t[-1] or (di, dj) == (0, -1) and list(zip(*nbt))[-1] != list(zip(*t))[0] or (di, dj) == (
                            -1, 0) and nbt[-1] != t[0]:
                        placeable = False
                        break
            if placeable and i < N:
                if j == N - 1:
                    ni = i + 1
                    nj = 0
                else:
                    ni = i
                    nj = j + 1
                ans = dfs(placed | {(x, flip, rotate, i, j)}, ni, nj)
                if ans != -1:
                    return ans
        return -1

    return tiles, dfs(frozenset(), 0, 0)


import sys

data = sys.stdin.read().strip()

tiles, pkv = reassemble(data)
N = int(len(tiles) ** 0.5)
print(math.prod(int(pkv[p][0]) for p in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]))
