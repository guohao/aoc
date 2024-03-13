import itertools


def p1(data: str):
    gsn = int(data)
    N = 300
    max_acc = 0
    ans = (0, 0)
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            acc = 0
            for a, b in itertools.product(range(x, x + 3), range(y, y + 3)):
                ti = a + 10
                pl = ti * b
                pl += gsn
                pl *= ti
                pl = int('000' + str(pl)[-3]) - 5
                acc += pl
            if acc > max_acc:
                max_acc = acc
                ans = (x, y)
    return str(ans)


def p2(data: str):
    gsn = int(data)
    N = 300
    max_acc = 0
    ans = (0, 0)
    plg = [[0] * (N + 1) for _ in range(N + 1)]

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            ti = x + 10
            pl = ti * y
            pl += gsn
            pl *= ti
            pl = int('000' + str(pl)[-3]) - 5
            plg[x][y] = pl
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            acc = 0
            for s in range(1, N + 1 - max(x, y)):
                acc += sum(plg[x + s - 1][i] for i in range(y, y + s))
                acc += sum(plg[i][y + s - 1] for i in range(x, x + s))
                acc -= plg[x + s - 1][y + s - 1]
                if acc > max_acc:
                    max_acc = acc
                    ans = (x, y, s)
    return str(ans)
