from functools import cache

from helper import *

data = raw_data(2015, 17)

containers = ints(data)
N = 150


def p1():
    @cache
    def dfs(i, remain):
        if remain == 0:
            return 1
        if i == len(containers):
            return 0
        return dfs(i + 1, remain - containers[i]) + dfs(i + 1, remain)

    print(dfs(0, N))


def p2():
    @cache
    def dfs(i, comb, remain):
        if remain == 0:
            return [comb]
        if i == len(containers):
            return []
        a = dfs(i + 1, comb + (containers[i],), remain - containers[i])
        b = dfs(i + 1, comb, remain)
        if a and b:
            min_len = min(len(x) for x in a + b)
            return [x for x in a + b if len(x) == min_len]
        else:
            return a if a else b

    print(len(dfs(0, (), N)))


p2()
