import math
from collections import deque
from functools import cache

import networkx as nx

import myutil


def p1(data: str):
    pos = set()
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c.isalpha():
                pos.add((c, (i, j)))
    non_stop = {3, 5, 7, 9}
    hallways = set((1, x) for x in list(range(1, 12)) if x not in non_stop)
    all_pos = [p for _, p in pos] + [p for p in hallways]
    print(all_pos)
    goals = {'A': [[2, 3], [3, 3]], 'B': [[2, 5], [3, 5]], 'C': [[2, 7], [3, 7]], 'D': [[2, 9], [3, 9]]}
    print(hallways)
    seen = set()

    def dfs(n_pos):
        if n_pos in seen:
            return math.inf
        rd = {v: k for k, v in n_pos}
        print(rd)
        unplaced = {}
        for letter, goal in goals.items():
            bottom = tuple(goal[1])
            up = tuple(goal[0])
            if bottom not in rd or rd[bottom] != letter:
                unplaced[letter] = goal
            else:
                if up not in rd or rd[up] != letter:
                    unplaced[letter] = [goal[0]]
        if not unplaced:
            return 0
        print(unplaced)
        spaces = [p for p in all_pos if p not in rd]
        def can_reach(source,dest):

        for letter, p in n_pos:
            if letter not in unplaced:
                continue
            if not any(nb in rd for nb in myutil.neighbors_2d_4(*p)):
                bottom = tuple(goals[letter][1])
                up = tuple(goals[letter][0])
                if p == bottom:
                    continue
                if p in hallways:
                    if bottom not in rd:


    return dfs(pos)


print(p1("""#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""))
