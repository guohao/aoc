import math


def p1(data: str):
    visited = set()
    ans = math.inf
    for line in data.splitlines():
        x, y = 0, 0
        find_state = len(visited) > 0
        for step in line.strip().split(','):
            directions = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
            d = directions[step[0]]
            step = int(step[1:])
            for _ in range(step):
                x, y = d[0] + x, d[1] + y
                if find_state:
                    if (x, y) in visited:
                        ans = min(abs(x) + abs(y), ans)
                else:
                    visited.add((x, y))
    return ans


def p2(data: str):
    visited = {}
    ans = math.inf
    for line in data.splitlines():
        x, y = 0, 0
        find_state = len(visited) > 0
        sc = 0
        for step in line.strip().split(','):
            directions = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
            d = directions[step[0]]
            step = int(step[1:])
            for _ in range(step):
                sc += 1
                x, y = d[0] + x, d[1] + y
                if find_state:
                    if (x, y) in visited:
                        ans = min(sc + visited[x, y], ans)
                else:
                    if (x, y) not in visited:
                        visited[x, y] = sc
    return ans
