import sys

g = {}
for i, line in enumerate(sys.stdin.readlines()):
    for j, c in enumerate(line.strip()):
        g[i, j] = int(c)
x_max, y_max = max((x, y) for x, y in g.keys())
ans = 0


def visible():
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if all((i + dx * k, j + dy * k) not in g or g[i + dx * k, j + dy * k] < g[i, j] for k in
               range(1, max(x_max, y_max))):
            return True
    return False


for i in range(x_max + 1):
    for j in range(y_max + 1):
        ans += visible()
print(ans)
