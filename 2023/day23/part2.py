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
g = {k for k, v in g.items() if v != '#'}
start = (0, [c for _, c in g if (0, c) in g][0])
R = len(ls)
goal = (R - 1, [c for _, c in g if (R - 1, c) in g][0])


def nb4(_x, _y):
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        yield _x + dx, _y + dy


seen = set()
adj = {p: {q: 1 for q in nb4(*p) if q in g} for p in g}
while True:
    for p, qs in adj.items():
        if len(qs) != 2:
            continue
        q1, q2 = qs
        adj[q1][q2] = adj[p][q1] + adj[p][q2]
        adj[q2][q1] = adj[p][q1] + adj[p][q2]
        del adj[p], adj[q1][p], adj[q2][p]
        break
    else:
        break


def dfs(p):
    if p == goal:
        return 0
    seen.add(p)
    ans = float("-inf")
    for nb, d in adj[p].items():
        if nb in seen:
            continue
        ans = max(d + dfs(nb), ans)
    seen.remove(p)
    print(ans)


print(dfs(start))
