import sys
from collections import deque


def s_is(grid, ps):
    connected = {}
    x, y = ps
    up = x - 1, y
    down = x + 1, y
    left = x, y - 1
    right = x, y + 1
    connected[up] = up in grid and grid[up] in '7F|'
    connected[down] = down in grid and grid[down] in 'JL|'
    connected[left] = left in grid and grid[left] in 'FL-'
    connected[right] = right in grid and grid[right] in '7J-'
    if connected[up] and connected[down]:
        return '|'
    if connected[left] and connected[right]:
        return '-'
    if connected[up] and connected[right]:
        return 'L'
    if connected[up] and connected[left]:
        return 'J'
    if connected[down] and connected[left]:
        return '7'
    if connected[down] and connected[right]:
        return 'F'


def loop(data: str):
    ls = data.splitlines()
    g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}

    start = [p for p, c in g.items() if c == 'S'][0]
    g[start] = s_is(g, start)
    visited = {}

    q = deque()
    q.append((start, 0))
    while q:
        p, step = q.popleft()
        x, y = p
        if p not in g:
            continue
        if g[p] == '.':
            continue
        if p in visited and visited[p] <= step:
            continue
        visited[p] = step
        next_visits = set()
        match g[p]:
            case '|':
                next_visits.add((x - 1, y))
                next_visits.add((x + 1, y))
            case '-':
                next_visits.add((x, y - 1))
                next_visits.add((x, y + 1))
            case 'L':
                next_visits.add((x - 1, y))
                next_visits.add((x, y + 1))
            case 'J':
                next_visits.add((x - 1, y))
                next_visits.add((x, y - 1))
            case '7':
                next_visits.add((x + 1, y))
                next_visits.add((x, y - 1))
            case 'F':
                next_visits.add((x + 1, y))
                next_visits.add((x, y + 1))
        for nv in next_visits:
            q.append((nv, step + 1))
    return visited


print(max(loop(sys.stdin.read()).values()))
