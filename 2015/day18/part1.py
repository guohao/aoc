import itertools

g = {}
N = 100
for i in range(N):
    for j, c in enumerate(input()):
        g[i, j] = c

for _ in range(N):
    n = {}
    for i, j in itertools.product(range(N), repeat=2):
        ons = 0
        for di, dj in itertools.product(range(-1, 2), repeat=2):
            if di == dj == 0:
                continue
            if (i + di, j + dj) in g and g[i + di, j + dj] == '#':
                ons += 1
        if g[i, j] == '#':
            n[i, j] = '#' if ons in {2, 3} else '.'
        else:
            n[i, j] = '#' if ons == 3 else '.'
    # print(n)
    g = n
print(list(g.values()).count('#'))
