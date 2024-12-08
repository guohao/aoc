import sys

sys.setrecursionlimit(10000000)

DIRECTIONS = {
    '>': [(0, 1)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '^': [(-1, 0)],
    '.': [(0, 1),
          (1, 0),
          (0, -1),
          (-1, 0)]
}
ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}

start = (0, [c for _, c in g if g[0, c] == '.'][0])
R = len(ls)
goal = (R - 1, [c for _, c in g if g[R - 1, c] == '.'][0])

seen = set()


def dfs(p):
    if p == goal:
        return 0
    seen.add(p)
    path_len = 0
    for dr, dc in DIRECTIONS[g[p]]:
        nb = dr + p[0], dc + p[1]
        if nb in g and g[nb] != '#' and nb not in seen:
            path_len = max(1 + dfs(nb), path_len)
    seen.remove(p)
    return path_len


print(dfs(start))
