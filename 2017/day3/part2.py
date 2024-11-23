import itertools

goal = int(input())
x = y = nx = ny = 0
dx, dy = 1, 0
g = {}

for i in itertools.count():
    x, y = nx, ny
    g[x, y] = sum(g.get((p + x, q + y), 0) for p, q in itertools.product(range(-1, 2), repeat=2))
    if g[x, y] > goal:
        print(g[x, y])
        break
    nx, ny = x - dy, y + dx
    if (nx, ny) not in g:
        dx, dy = -dy, dx
    else:
        nx, ny = x + dx, y + dy
