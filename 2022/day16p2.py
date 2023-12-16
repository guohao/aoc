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

ov = ','.join(c[0] for c in D.items() if c[1][0] == 0)


@functools.cache
def dfs(ci: str, ce: str, vo: str, time_left: int) -> int:
    # print(f'{ci} {ce} {vo} {26 - time_left}')
    if time_left <= 1:
        return 0
    time_left -= 1
    ret = -1
    for i in D[ci][1]:
        for j in D[ce][1]:
            ret = max(ret, dfs(i, j, vo, time_left))
    if ci not in vo:
        ret = max(ret, time_left * D[ci][0] + max(dfs(ci, ne, vo + ',' + ci, time_left) for ne in D[ce][1]))
    if ce not in vo:
        ret = max(ret, time_left * D[ce][0] + max(dfs(ni, ce, vo + ',' + ce, time_left) for ni in D[ci][1]))
    if ce not in vo and ci not in vo:
        if ce != ci:
            ret = max(ret, time_left * D[ci][0] + time_left * D[ce][0] + dfs(ci, ce, vo + ',' + ci + ',' + ce, time_left))
        else:
            ret = max(ret, time_left * D[ce][0] + max(dfs(ni, ce, vo + ',' + ce, time_left) for ni in D[ci][1]))
    return ret


ret = dfs('AA', 'AA', ov, 26)
print(ret)
