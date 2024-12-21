import math
import sys
from functools import cache

import re

import networkx as nx

ls = [l.strip() for l in sys.stdin.readlines()]
dc = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ['#', 0, 'A']
]
g = {(i, j): str(c) for i, line in enumerate(dc) for j, c in enumerate(line)}

rg = {v: k for k, v in g.items()}
G = nx.Graph()
for i in range(len(dc)):
    for j in range(len(dc[i])):
        if g[i, j] == '#':
            continue
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nb = i + dx, j + dy
            if nb in g and g[nb] != '#':
                G.add_edge((i, j), nb)
cc = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
]
CG = nx.Graph()
cg = {(i, j): str(c) for i, line in enumerate(cc) for j, c in enumerate(line)}
rcg = {v: k for k, v in cg.items()}
for i in range(len(cc)):
    for j in range(len(cc[i])):
        if cg[i, j] == '#':
            continue
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nb = i + dx, j + dy
            if nb in cg and cg[nb] != '#':
                CG.add_edge((i, j), nb)


def decode(_G, prev_steps):
    steps = []
    for i in range(1, len(prev_steps)):
        start = prev_steps[i - 1]
        target = prev_steps[i]
        one_step_choices = []
        for path in nx.all_shortest_paths(_G, start, target):
            cur_seq = []
            for j in range(1, len(path)):
                diff = (path[j][0] - path[j - 1][0], path[j][1] - path[j - 1][1])
                D = {
                    (1, 0): 'v',
                    (-1, 0): '^',
                    (0, 1): '>',
                    (0, -1): '<'
                }
                cur_seq.append(D[diff])
            cur_seq.append('A')
            one_step_choices.append(''.join(cur_seq))
        min_len = min(len(x) for x in one_step_choices)
        steps.append([x for x in one_step_choices if len(x) == min_len])
    return steps


@cache
def dfs(turn: int, picked: str):
    cost = 0
    if turn == 1:
        for step in decode(CG, [rcg[c] for c in 'A' + picked]):
            cost += min(len(a) for a in step)
    else:
        for steps in decode(CG, [rcg[c] for c in 'A' + picked]):
            min_cost = math.inf
            for pick in steps:
                min_cost = min(min_cost, dfs(turn - 1, pick))
            cost += min_cost
    return cost


N = 25
t = 0
for line in ls:
    _min_cost = 0
    for step in decode(G, [rg[c] for c in 'A' + line]):
        _min_cost += min(dfs(N, choice) for choice in step)
    n = list(map(int, re.findall(r'-?\d+', line)))[0]
    t += _min_cost * n
print(t)
