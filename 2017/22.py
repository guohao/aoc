def p1(data: str):
    G = {}
    MI, MJ = 0, 0
    for i, line in enumerate(data.splitlines()):
        MI = max(MI, i)
        for j, c in enumerate(line):
            MJ = max(MJ, j)
            if c == '#':
                G[i, j] = c
    p = MI // 2, MJ // 2
    ans = 0
    d = (-1, 0)
    for _ in range(10000):
        if p not in G:
            d = (-d[1], d[0])
            G[p] = '#'
            ans += 1
        else:
            d = (d[1], -d[0])
            del G[p]
        p = p[0] + d[0], p[1] + d[1]
    return ans


def p2(data: str):
    G = {}
    MI, MJ = 0, 0
    for i, line in enumerate(data.splitlines()):
        MI = max(MI, i)
        for j, c in enumerate(line):
            MJ = max(MJ, j)
            if c == '#':
                G[i, j] = 'I'
    p = MI // 2, MJ // 2
    ans = 0
    d = (-1, 0)
    for _ in range(10000000):
        if p not in G:
            d = (-d[1], d[0])
            G[p] = 'W'
        elif G[p] == 'W':
            ans += 1
            G[p] = 'I'
        elif G[p] == 'I':
            d = (d[1], -d[0])
            G[p] = 'F'
        elif G[p] == 'F':
            d = (-d[0], -d[1])
            del G[p]
        p = p[0] + d[0], p[1] + d[1]
    return ans
