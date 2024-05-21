import math
from collections import deque
from functools import cache

import networkx as nx

import myutil


def p1(data: str):
    pos = []
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c.isalpha():
                pos.append((c, (i, j)))
    non_stop = {3, 5, 7, 9}
    hallways = set((1, x) for x in list(range(1, 12)) if x not in non_stop)
    goals = {'A': [[2, 3], [3, 3]], 'B': [[2, 5], [3, 5]], 'C': [[2, 7], [3, 7]], 'D': [[2, 9], [3, 9]]}
    cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    seen = set()

    def dfs(n_pos):
        if n_pos in seen:
            return math.inf
        seen.add(n_pos)
        rd = {v: k for k, v in n_pos}
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

        def can_reach(grid, hp, cell):
            if any((i, cell[1]) in grid for i in range(2, cell[0])):
                return -1
            if any((1, i) in grid for i in range(min(hp[1], cell[1]) + 1, max(hp[1], cell[1]))):
                return -1
            return cell[0] - 1 + abs(cell[1] - hp[1])

        ans = math.inf
        for letter, p in n_pos:
            if letter not in unplaced:
                continue
            bottom = tuple(goals[letter][1])
            up = tuple(goals[letter][0])
            ts = set()
            if p == bottom:
                continue
            if p in hallways:
                if bottom in rd and rd[bottom] != letter:
                    continue
                if bottom not in rd:
                    goal = bottom
                else:
                    if up in rd and rd[up] != letter:
                        continue
                    goal = up
                ts.add((p, goal))
            else:
                for h_p in sorted(hallways):
                    if h_p[1] in non_stop:
                        continue
                    ts.add((h_p, p))
            for src, dst in ts:
                path_len = can_reach(rd, src, dst)
                if path_len != -1:
                    nrd = rd.copy()
                    del nrd[p]
                    moved = src if p != src else dst
                    nrd[moved] = letter
                    nn_pos = frozenset((v, k) for k, v in nrd.items())
                    path_weight = path_len * cost[letter]
                    total_cost = path_weight + dfs(nn_pos)
                    if ans > total_cost:
                        print(f'move {letter} from {p} to {moved} cost {path_weight} total_cost {total_cost}')
                        ans = total_cost
        return ans

    return dfs(frozenset(pos))


# assert 8 == p1("""#############
# #.........A.#
# ###.#B#C#D###
#   #A#B#C#D#
#   #########""")

# assert 7008 == p1("""#############
# #.....D.D.A.#
# ###.#B#C#.###
#   #A#B#C#.#
#   #########""")

assert 9011 == p1("""#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########""")


# assert 9041 == p1("""#############
# #.....D.....#
# ###B#.#C#D###
#   #A#B#C#A#
#   #########""")

# print(p1("""#############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########"""))
