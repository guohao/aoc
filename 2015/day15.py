from helper import *

data = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""
data = raw_data(2015, 15)
lines = lines(data)
ings = []
for line in lines:
    name = line.split(':')[0]
    ings.append(ints(line))


def score(state):
    if any(x < 0 for x in state):
        return 0

    return math.prod(state)


def score_2(state):
    if any(x < 0 for x in state):
        return 0
    if state[4] != 500:
        return 0
    return math.prod(state[:4])


def p1():
    def dfs(i, state, remain):
        if remain == 0:
            return score(state)
        if i == len(ings):
            return 0
        cur = ings[i]
        max_ = 0
        for k in range(0, remain + 1):
            ns = [state[j] + cur[j] * k for j in range(len(state))]
            max_ = max(dfs(i + 1, ns, remain - k), max_)
        return max_

    print(dfs(0, [0] * 4, 100))


def p2():
    def dfs(i, state, remain):
        if remain == 0:
            return score_2(state)
        if i == len(ings):
            return 0
        cur = ings[i]
        max_ = 0
        for k in range(0, remain + 1):
            ns = [state[j] + cur[j] * k for j in range(len(state))]
            max_ = max(dfs(i + 1, ns, remain - k), max_)
        return max_

    print(dfs(0, [0] * 5, 100))

p1()
p2()