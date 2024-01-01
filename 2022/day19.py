from collections import defaultdict
from functools import cache

from helper import *

data = """
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
"""
data = raw_data(2022, 19)
blueprints = []

for line in lines(data):
    _, ore, clay, obs0, obs1, geo0, geo1 = nums(line)
    blueprints.append([(ore, 0, 0, 0), (clay, 0, 0, 0), (obs0, obs1, 0, 0), (0, geo0, geo1, 0)])

name_idx = {'ore': 0, 'clay': 1, 'obsidian': 2, 'geode': 3}


def p1():
    ans = 0
    for i, bp in enumerate(blueprints, start=1):
        state = set()
        state.add(((1, 0, 0, 0), (0, 0, 0, 0)))
        max_obs = 0
        for t in range(24):
            ns = set()
            for robots, gain in state:
                # print(robots, gain)
                term_gain = tuple([gain[i] + robots[i] for i in range(4)])
                for i in range(4):
                    if all(gain[n] >= bp[i][n] for n in range(4)):
                        ng = list(term_gain)
                        nr = list(robots)
                        nr[i] += 1
                        for j in range(4):
                            ng[j] -= bp[i][j]
                        ns.add((tuple(nr), tuple(ng)))
                max_obs = max(max_obs, term_gain[3])
                ns.add((robots, term_gain))
            state.clear()
            for robots, gain in ns:
                if gain[3] >= max_obs:
                    state.add((robots, gain))
            print(t, len(ns), len(state), max_obs)
        ans += i * max_obs
    print(ans)


def p2():
    ans = []
    for bp in blueprints[:3]:
        state = set()
        state.add(((1, 0, 0, 0), (0, 0, 0, 0)))
        max_obs = 0
        for t in range(32):
            ns = set()
            for robots, gain in state:
                # print(robots, gain)
                term_gain = tuple([gain[i] + robots[i] for i in range(4)])
                for i in range(4):
                    if all(gain[n] >= bp[i][n] for n in range(4)):
                        ng = list(term_gain)
                        nr = list(robots)
                        nr[i] += 1
                        for j in range(4):
                            ng[j] -= bp[i][j]
                        ns.add((tuple(nr), tuple(ng)))
                max_obs = max(max_obs, term_gain[3])
                ns.add((robots, term_gain))
            print(t, len(ns), len(state), max_obs)
            state = ns
            # state.clear()
            # for robots, gain in ns:
            #     if gain[3] >= max_obs:
            #         state.add((robots, gain))
        print(max_obs)
        ans.append(max_obs)
    print(ans[0] * ans[1] * ans[2])


# p1()
p2()
