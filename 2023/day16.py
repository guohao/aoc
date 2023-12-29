from collections import deque

from helper import *

data = raw_data(2023, 16)

lines = data.strip().split('\n')
N = len(lines)
M = len(lines[0])
g = grid(data)


# print(g)

def bfs(entrypoint):
    path = set()
    dq = deque()
    dq.append(entrypoint)
    while dq:
        source, current = dq.popleft()
        if current not in g:
            continue
        if (source, current) in path:
            continue
        path.add((source, current))

        # print(source, current, g[current])
        diff = (current[0] - source[0], current[1] - source[1])
        match g[current]:
            case '.':
                dq.append((current, (current[0] + diff[0], current[1] + diff[1])))
            case '/':
                dq.append((current, (current[0] - diff[1], current[1] - diff[0])))
            case '\\':
                dq.append((current, (current[0] + diff[1], current[1] + diff[0])))
            case '|':
                if diff[1] == 0:
                    dq.append((current, (current[0] + diff[0], current[1])))
                else:
                    dq.append((current, (current[0] + 1, current[1])))
                    dq.append((current, (current[0] - 1, current[1])))
            case '-':
                if diff[0] == 0:
                    dq.append((current, (current[0], current[1] + diff[1])))
                else:
                    dq.append((current, (current[0], current[1] + 1)))
                    dq.append((current, (current[0], current[1] - 1)))

    visited = set()
    for source, target in path:
        if source in g:
            visited.add(source)
        if target in g:
            visited.add(target)
    return len(visited)


print(bfs(((0, -1), (0, 0))))
eps = []
for i in range(N):
    eps.append(((i, -1), (i, 0)))
    eps.append(((i, M), (i, M - 1)))
for j in range(M):
    eps.append(((-1, j), (0, j)))
    eps.append(((N, j), (N - 1, j)))
print(max(bfs(ep) for ep in eps))
