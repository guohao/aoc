import sys

lines = [l.strip() for l in sys.stdin.readlines()]

g = {(i, j): int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}
ans = 0
for x, y in g:
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = x + dx, y + dy
        if nb in g and g[nb] <= g[x, y]:
            break
    else:
        ans += g[x, y] + 1
print(ans)
