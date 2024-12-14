import math
import sys
from functools import cache

data = sys.stdin.read().strip()

lines = data.splitlines()
lines.insert(3, "  #D#B#A#C#")
lines.insert(3, "  #D#C#B#A#")
data = '\n'.join(lines)

pos = []
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c.isalpha():
            pos.append((c, (i, j)))
hallways = set((1, x) for x in list(range(1, 12)) if x not in range(3, 11, 2))
goals = {}
for letter, j in zip('ABCD', range(3, 11, 2)):
    goals[letter] = [(i, j) for i in range(2, max(x for _, (x, y) in pos) + 1)]

cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


@cache
def dfs(n_pos):
    rd = {v: k for k, v in n_pos}
    unplaced = {}
    for letter, goal in goals.items():
        for x in reversed(goal):
            if x not in rd or rd[x] != letter:
                unplaced[letter] = x
                break
    if not unplaced:
        return 0

    def can_reach(grid, hp, cell):
        if cell in grid and hp in grid:
            return -1
        if any((i, cell[1]) in grid for i in range(2, cell[0])):
            return -1
        if any((1, i) in grid for i in range(min(hp[1], cell[1]) + 1, max(hp[1], cell[1]))):
            return -1
        return cell[0] - 1 + abs(cell[1] - hp[1])

    ans = math.inf
    for letter, p in n_pos:
        if letter not in unplaced:
            continue
        goal = unplaced[letter]
        if p[1] == goal[1] and p[0] > goal[0]:
            continue
        ts = set()
        if p in hallways:
            ts.add((p, goal))
        else:
            for h_p in hallways:
                ts.add((h_p, p))
        for src, dst in ts:
            path_len = can_reach(rd, src, dst)
            if path_len == -1:
                continue
            moved = src if p != src else dst
            nn_pos = n_pos - frozenset([(letter, p)]) | frozenset([(letter, moved)])
            path_weight = path_len * cost[letter]
            total_cost = path_weight + dfs(nn_pos)
            if ans > total_cost:
                ans = total_cost
    return ans


print(dfs(frozenset(pos)))
