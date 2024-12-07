import sys

exp = 1000000
ls = sys.stdin.read().splitlines()
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
X_MIN, X_MAX = min(x for x, y in g), max(x for x, y in g)
Y_MIN, Y_MAX = min(y for x, y in g), max(y for x, y in g)
empty_cols = set(y for (_, y), v in g.items() if all(g[x, y] == '.' for x in range(X_MIN, X_MAX + 1)))
empty_rows = set(x for (x, _), v in g.items() if all(g[x, y] == '.' for y in range(X_MIN, X_MAX + 1)))
ans = 0
gs = [p for p, c in g.items() if c == '#']
for i in range(len(gs)):
    x0, y0 = gs[i]
    for j in range(i + 1, len(gs)):
        x1, y1 = gs[j]
        ecc = set(range(min(x0, x1), max(x0, x1) + 1)) & empty_rows
        erc = [y for y in range(min(y0, y1), max(y0, y1) + 1) if y in empty_cols]
        ans += abs(x1 - x0) + abs(y1 - y0) + len(ecc) * (exp - 1) + len(erc) * (exp - 1)
print(ans)
