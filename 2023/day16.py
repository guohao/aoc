from collections import deque

from helper import *

data = raw_data(2023, 16)

lines = data.strip().split('\n')
N = len(lines)
M = len(lines[0])
g = grid_dict(lines)


def f2(x, y, d):
    D = set()
    v = set()
    tv = deque()
    tv.append((x, y, d))
    while tv:
        x, y, d = tv.popleft()
        if x not in range(0, N):
            continue
        if y not in range(0, M):
            continue
        if (x, y, d) in v:
            continue
        v.add((x, y, d))
        D.add((x, y))
        if g[(x, y)] == '.':
            if d == 'N':
                tv.append((x - 1, y, d))
            elif d == 'S':
                tv.append((x + 1, y, d))
            elif d == 'E':
                tv.append((x, y + 1, d))
            else:
                tv.append((x, y - 1, d))
        elif g[(x, y)] == '\\':
            if d == 'E':
                d = 'S'
                tv.append((x + 1, y, d))
            elif d == 'W':
                d = 'N'
                tv.append((x - 1, y, d))
            elif d == 'N':
                d = 'W'
                tv.append((x, y - 1, d))
            else:
                d = 'E'
                tv.append((x, y + 1, d))
        elif g[(x, y)] == '/':
            if d == 'E':
                d = 'N'
                tv.append((x - 1, y, d))
            elif d == 'W':
                d = 'S'
                tv.append((x + 1, y, d))
            elif d == 'N':
                d = 'E'
                tv.append((x, y + 1, d))
            elif d == 'S':
                d = 'W'
                tv.append((x, y - 1, d))
        elif g[(x, y)] == '-':
            if d == 'E':
                tv.append((x, y + 1, d))
            elif d == 'W':
                tv.append((x, y - 1, d))
            elif d == 'N':
                tv.append((x, y - 1, 'W'))
                tv.append((x, y + 1, 'E'))
            elif d == 'S':
                tv.append((x, y - 1, 'W'))
                tv.append((x, y + 1, 'E'))
        elif g[(x, y)] == '|':
            if d == 'N':
                tv.append((x - 1, y, d))
            elif d == 'S':
                tv.append((x + 1, y, d))
            elif d == 'E':
                tv.append((x - 1, y, 'N'))
                tv.append((x + 1, y, 'S'))
            elif d == 'W':
                tv.append((x - 1, y, 'N'))
                tv.append((x + 1, y, 'S'))
    return len(D)


print(f2(0, 0, 'E'))
m = max(f2(i, 0, 'E') for i in range(N))
m = max(m, max(f2(i, M - 1, 'W') for i in range(N)))
m = max(m, max(f2(0, i, 'S') for i in range(M)))
m = max(m, max(f2(N - 1, i, 'N') for i in range(M)))
print(m)
