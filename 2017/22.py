def build_graph(data: str):
    G = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            G[i, j] = c
    X, Y = max(x for x, _ in G.keys()), max(y for _, y in G.keys())
    p = (X // 2, Y // 2)
    return G, p


def p1(data: str):
    G, p = build_graph(data)
    infect_count = 0
    d = (-1, 0)
    for _ in range(10000):
        if p not in G or G[p] == '.':
            d = (-d[1], d[0])
            G[p] = '#'
            infect_count += 1
        else:
            d = (d[1], -d[0])
            G[p] = '.'
        p = (p[0] + d[0], p[1] + d[1])
    return infect_count


def p2(data: str):
    G, p = build_graph(data)
    infect_count = 0
    d = (-1, 0)
    for _ in range(10000000):
        if p not in G or G[p] == '.':
            d = (-d[1], d[0])
            G[p] = 'W'
        elif G[p] == 'W':
            G[p] = '#'
            infect_count += 1
        elif G[p] == '#':
            d = (d[1], -d[0])
            G[p] = 'F'
        elif G[p] == 'F':
            d = (-d[0], -d[1])
            G[p] = '.'
        p = (p[0] + d[0], p[1] + d[1])
    return infect_count
