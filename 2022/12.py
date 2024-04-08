from collections import deque


def p1(data: str):
    q = deque()
    g = {}
    start = 0, 0
    goal = 0, 0
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == 'E':
                goal = i, j
                c = 'z'
            if c == 'S':
                start = i, j
                c = 'a'
            g[i, j] = ord(c)
    q.append((start, 0))
    visited = set()
    while q:
        (x, y), s = q.popleft()
        if (x, y) == goal:
            return s
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nb = x + dx, y + dy
            if nb not in g:
                continue
            if g[nb] - g[x, y] <= 1:
                q.append((nb, s + 1))


def p2(data: str):
    q = deque()
    g = {}
    start = 0, 0
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == 'E':
                start = i, j
                c = 'z'
            if c == 'S':
                c = 'a'
            g[i, j] = ord(c)
    q.append((start, 0))
    visited = set()
    while q:
        (x, y), s = q.popleft()
        if g[x, y] == ord('a'):
            return s
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nb = x + dx, y + dy
            if nb not in g:
                continue
            if g[nb] - g[x, y] >= -1:
                q.append((nb, s + 1))
