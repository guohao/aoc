goal = int(input())
x = y = nx = ny = 0
dx, dy = 1, 0
g = {}
for i in range(goal):
    x, y = nx, ny
    g[x, y] = i + 1
    nx, ny = x - dy, y + dx
    if (nx, ny) not in g:
        dx, dy = -dy, dx
    else:
        nx, ny = x + dx, y + dy

print(abs(x) + abs(y))
