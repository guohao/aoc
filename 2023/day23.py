import sys
from collections import defaultdict

from helper import *

sys.setrecursionlimit(1000000)


def neighbors(p, ignore_direction=False):
    if g[p] == '.' or ignore_direction:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = p[0] + dx, p[1] + dy
            np = (nx, ny)
            if np in g:
                yield np
    else:
        dx, dy = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[g[p]]
        nx, ny = p[0] + dx, p[1] + dy
        np = (nx, ny)
        if np in g:
            yield np


def transitive_closure(ignore_direction=False):
    adjacency = defaultdict(dict)
    for v in g:
        for neighbor in list(neighbors(v, ignore_direction)):
            adjacency[v][neighbor] = 1
    while True:
        change = False
        for v in g:
            if v not in adjacency:
                continue
            nbs = adjacency[v]
            if not ignore_direction:
                nbs = [nb for nb in nbs if g[nb] == '.']
            if len(nbs) == 2:
                change = True
                a, b = nbs
                adjacency[a][b] = adjacency[a][v] + adjacency[v][b]
                adjacency[b][a] = adjacency[b][v] + adjacency[v][a]
                del adjacency[b][v]
                del adjacency[a][v]
                del adjacency[v]
        if not change:
            break
    return adjacency


def dfs(p, path, adjacency):
    if p not in adjacency or p in path:
        return 0
    ret = 0
    if p == goal:
        path.append(p)
        for i in range(len(path) - 1):
            ret += adjacency[path[i]][path[i + 1]]
        return ret
    path = path.copy()
    path.append(p)
    for neighbor in adjacency[p].keys():
        ret = max(ret, dfs(neighbor, path, adjacency))
    return ret


def solve(ignore_direction=False):
    adj = transitive_closure(ignore_direction)
    print(dfs(start, [], adj))


data = raw_data(2023, 23)
lines = lines(data)
start = (0, lines[0].index('.'))
goal = (len(lines) - 1, lines[-1].index('.'))
g = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] != '#'}
solve(False)
solve(True)
