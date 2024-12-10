import math
import re
import sys

lines = [l.strip() for l in sys.stdin.readlines()]

blueprints = []

for line in lines:
    _, ore, clay, obs0, obs1, geo0, geo1 = map(int, re.findall('-?\d+', line))
    blueprints.append([(ore, 0, 0, 0), (clay, 0, 0, 0), (obs0, obs1, 0, 0), (geo0, 0, geo1, 0)])

name_idx = {'ore': 0, 'clay': 1, 'obsidian': 2, 'geode': 3}


def solve(max_bps, max_minutes):
    ans = []
    for bp in blueprints[:max_bps]:
        state = set()
        state.add(((1, 0, 0, 0), (0, 0, 0, 0)))
        max_obs = 0
        for t in range(max_minutes):
            ns = set()
            for robots, gain in state:
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
        ans.append(max_obs)
    return ans


print(math.prod(solve(3, 32)))

