from collections import deque


def p1(data: str):
    G = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == ' ':
                continue
            G[i, j] = c
    ans = ''
    q = deque()
    q.append(((0, min(x for x in range(10000) if (0, x) in G)), (1, 0)))
    while q:
        (x, y), d = q.popleft()
        if G[x, y].isalpha():
            ans += G[x, y]
        nb = x + d[0], y + d[1]
        if nb in G:
            q.append((nb, d))
        else:
            for nd in {(0, 1), (0, -1), (1, 0), (-1, 0)} - {(-d[0], -d[1]), d}:
                nb = x + nd[0], y + nd[1]
                if nb in G:
                    q.append(((x + nd[0], y + nd[1]), nd))
                    break
    return ans


def p2(data: str):
    G = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == ' ':
                continue
            G[i, j] = c
    q = deque()
    q.append(((0, min(x for x in range(10000) if (0, x) in G)), (1, 0)))
    ans = 0
    while q:
        ans += 1
        (x, y), d = q.popleft()
        nb = x + d[0], y + d[1]
        if nb in G:
            q.append((nb, d))
        else:
            for nd in {(0, 1), (0, -1), (1, 0), (-1, 0)} - {(-d[0], -d[1]), d}:
                nb = x + nd[0], y + nd[1]
                if nb in G:
                    q.append((nb, nd))
                    break
    return ans
