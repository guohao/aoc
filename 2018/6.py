from collections import deque


def md(i, j, node):
    return abs(node[0] - i) + abs(node[1] - j)


def sum_md(i, j, nodes):
    return sum(md(i, j, node) for node in nodes)



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
    min_x = min(x[0] for x in nodes)
    max_x = max(x[0] for x in nodes)
    min_y = min(x[1] for x in nodes)
    max_y = max(x[1] for x in nodes)
    max_distance = 10000
    start = ((max_x + min_x) // 2, (max_y + min_y) // 2)
    assert sum_md(*start, nodes) < max_distance
    visited = set()
    q = deque()
    q.append(start)
    while q:
        i, j = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = dx + i, dy + j
            if sum_md(ni, nj, nodes) < max_distance:
                q.append((ni, nj))
    return len(visited)
