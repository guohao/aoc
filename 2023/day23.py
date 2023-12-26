import sys
from collections import defaultdict

from helper import *
from heapq import *

sys.setrecursionlimit(1000000)

data = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""
data = raw_data(2023, 23)
lines = lines(data)
start = (0, lines[0].index('.'))
goal = (len(lines) - 1, lines[-1].index('.'))
g = {(i, j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}


def neighbors(p, ignore_direction=False):
    if g[p] == '#':
        return
    if g[p] == '.' or ignore_direction:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = p[0] + dx, p[1] + dy
            np = (nx, ny)
            if np in g and g[np] != '#':
                yield np
    else:
        dx, dy = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[g[p]]
        nx, ny = p[0] + dx, p[1] + dy
        np = (nx, ny)
        if np in g and g[np] != '#':
            yield np


def transitive_closure(ignore_direction=False):
    adjacency = defaultdict(set)
    weight = defaultdict(int)
    for v in g:
        v_neighbors = list(neighbors(v, ignore_direction))
        if len(v_neighbors) == 2:
        for neighbor in v_neighbors :
            adjacency[v].add(neighbor)
            weight[v, neighbor] = 1
    while True:
        vertex_to_remove = set()
        in_edges = defaultdict(set)
        out_edges = defaultdict(set)
        for v in g:
            for neighbor in adjacency[v]:
                out_edges[v].add(neighbor)
                in_edges[neighbor].add(v)

        for v in g:
            if in_edges[v] == out_edges[v] and len(in_edges) == 2:
                vertex_to_remove.add(v)

        for v in vertex_to_remove:
            predecessor, successor = in_edges[v].pop(), out_edges[v].pop()
            adjacency[predecessor].remove(v)
            adjacency[v].remove(successor)
            adjacency[predecessor].add(successor)

        if not vertex_to_remove:
            break
    return adjacency, weight


def dfs(p, path, adjacency, weight):
    if p not in adjacency or p in path:
        return 0
    ret = 0
    if p == goal:
        path.append(p)
        for i in range(len(path) - 1):
            ret += weight[path[i], path[i + 1]]
        return ret
    path = path.copy()
    path.append(p)
    for neighbor in adjacency[p]:
        ret = max(ret, dfs(neighbor, path, adjacency, weight))
    return ret


def solve(ignore_direction=False):
    adj, wt = transitive_closure(ignore_direction)
    print(dfs(start, [], adj, wt))


solve(False)
solve(True)
