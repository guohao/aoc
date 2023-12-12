from typing import List

import helper

data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
data = io_utils.get_data(2023, 9)
lines = io_utils.raw_str_to_lines(data)


def gen_all_his(line: str) -> List[List[int]]:
    g = [[int(x) for x in line.split()]]
    while sum(g[-1]) != 0:
        d = []
        for i in range(len(g[-1]) - 1):
            d.append(g[-1][i + 1] - g[-1][i])
        g.append(d)
    return g


def p1():
    ans = []
    for line in lines:
        g = gen_all_his(line)
        g[-1].append(0)
        for i in range(len(g) - 2, -1, -1):
            g[i].append(g[i][-1] + g[i + 1][-1])
        ans.append(g[0][-1])
    print(sum(ans))


def p2():
    ans = []
    for line in lines:
        g = gen_all_his(line)
        g[-1].insert(0, 0)
        for i in range(len(g) - 2, -1, -1):
            g[i].insert(0, g[i][0] - g[i + 1][0])
        ans.append(g[0][0])
    print(sum(ans))


p1()
p2()
