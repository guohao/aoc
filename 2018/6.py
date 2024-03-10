import itertools


def md(i, j, node):
    return abs(node[0] - i) + abs(node[1] - j)


def p1(data: str):
    nodes = [eval('(' + x + ')') for x in data.splitlines()]
    X, Y = max(x[0] for x in nodes), max(x[1] for x in nodes)
    G = {}
    for i in range(X + 10):
        for j in range(Y + 10):
            nearest = sorted(nodes, key=lambda x: md(i, j, x))
            if md(i, j, nearest[0]) == md(i, j, nearest[1]):
                G[i, j] = (-1, -1)
            else:
                G[i, j] = nearest[0]
    ans = 0
    for node in nodes:
        colored = [x for x in G.keys() if G[x] == node]
        if all(0 < x[0] < X + 9 and 0 < x[1] < Y + 9 for x in colored):
            ans = max(ans, len(colored))
    return ans


def p2(data: str):
    nodes = [eval(f'({x})') for x in data.splitlines()]
    MD = 10000
    min_x = min(x[0] - MD for x in nodes)
    max_x = max(x[0] + MD for x in nodes)
    min_y = min(x[1] - MD for x in nodes)
    max_y = max(x[1] + MD for x in nodes)
    ans = 0
    # total = (max_x - min_x + 1) * (max_y - min_x + 1)
    print(min_x, max_x, min_y, max_y)
    for i, j in itertools.product(range(min_x, max_x), range(min_y, max_y)):
        if all(md(i, j, x) < MD for x in nodes):
            ans += 1
    return ans
