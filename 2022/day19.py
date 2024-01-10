from helper import *

data = raw_data(2022, 19)
blueprints = []

for line in lines(data):
    _, ore, clay, obs0, obs1, geo0, geo1 = ints(line)
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


def p1():
    print(sum(i * obs for i, obs in enumerate(solve(len(blueprints), 24), start=1)))


def p2():
    print(math.prod(solve(3, 32)))


p1()
p2()
