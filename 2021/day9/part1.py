import sys

lines = [l.strip() for l in sys.stdin.readlines()]

g = {(i, j): c for i, line in enumerate(lines) for j, c in line}
ans = 0
for (x, y) in g:
    m = True
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = x + dx, y + dy
        if nb not in g or g[nb] <= g[x, y]:
            m = False
            break
    if m:
        ans += g[x, y] + 1
print(ans)
