import functools
from collections import defaultdict

from helper import *

data = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
data = raw_data(2022, 16)
lines = lines(data)
lines = [line.split() for line in lines]
D = {}
for i, line in enumerate(lines):
    c, r, ov = [line[1], int(next(re.finditer(r'\d+', line[4])).group()), line[9:]]
    ov = [x.replace(',', '') for x in ov]
    D[c] = (r, ov)
    # print(c, r, ov)


@functools.cache
def dfs(current, state: str, time_left) -> int:
    # print(current, state, time_left)
    if time_left <= 1:
        return 0
    if current in state:
        return max(dfs(c, state, time_left - 1) for c in D[current][1])
    else:
        if D[current][0] == 0:
            return max(dfs(c, state, time_left - 1) for c in D[current][1])
        b = max(dfs(c, state + ',' + current, time_left - 2) for c in D[current][1])
        b += (time_left - 1) * D[current][0]
        return b


ret = dfs('AA', '', 30)
print(ret)
