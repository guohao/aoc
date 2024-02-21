def p1(n):
    v = {}
    x, y = 0, 0
    d = (1, 0)
    for i in range(n - 1):
        v[x, y] = i + 1
        x = x + d[0]
        y = y + d[1]
        if d == (1, 0):
            if (x, y + 1) not in v:
                d = (0, 1)
        elif d == (0, 1):
            if (x - 1, y) not in v:
                d = (-1, 0)
        elif d == (-1, 0):
            if (x, y - 1) not in v:
                d = (0, -1)
        else:
            if (x + 1, y) not in v:
                d = (1, 0)
    # print(v)
    return abs(x) + abs(y)


def p2(n):
    v = {}
    x, y = 0, 0
    d = (1, 0)
    v[0, 0] = 1
    while True:
        x = x + d[0]
        y = y + d[1]
        v[x, y] = sum(v.get((x + i, y + j), 0) for i in range(-1, 2) for j in range(-1, 2))
        if v[x, y] > n:
            return v[x, y]
        if d == (1, 0):
            if (x, y + 1) not in v:
                d = (0, 1)
        elif d == (0, 1):
            if (x - 1, y) not in v:
                d = (-1, 0)
        elif d == (-1, 0):
            if (x, y - 1) not in v:
                d = (0, -1)
        else:
            if (x + 1, y) not in v:
                d = (1, 0)


print(p1(277678))
print(p2(277678))
