import math
import re


def solve(data: str, limit_calories=False):
    ings = []
    for line in data.splitlines():
        ings.append(list(map(int, re.findall(r'-?\d+', line))))

    def dfs(remain, idx) -> list[list[int]]:
        if idx == len(ings) - 1:
            return [[remain]]
        return [[i] + nl for i in range(remain + 1) for nl in dfs(remain - i, idx + 1)]

    def score_of(comb):
        return math.prod(max(0, sum(comb[i] * ings[i][j] for i in range(len(ings)))) for j in range(4))

    ans = 0
    for comb in dfs(100, 0):
        if limit_calories and sum(comb[i] * ings[i][-1] for i in range(len(ings))) != 500:
            continue
        ans = max(ans, score_of(comb))
    return ans


def p1(data: str):
    return solve(data)


def p2(data: str):
    return solve(data, True)
