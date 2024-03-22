import itertools
import math


def solve(data: str, n):
    pkgs = list(map(int, data.splitlines()))
    weight = sum(pkgs) // n
    for i in range(1, len(pkgs) // n):
        ans = math.inf
        for j in itertools.combinations(pkgs, i):
            if sum(j) == weight:
                ans = min(ans, math.prod(j))
        if ans < math.inf:
            return ans


def p1(data: str):
    return solve(data, 3)


def p2(data: str):
    return solve(data, 4)
