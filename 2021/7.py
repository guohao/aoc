import math


def p1(data: str):
    ns = list(map(int, data.split(',')))

    ans = math.inf
    for n in range(min(ns), max(ns) + 1):
        ans = min(ans, sum(abs(x - n) for x in ns))
    return ans


def p2(data: str):
    ns = list(map(int, data.split(',')))

    ans = math.inf
    for n in range(min(ns), max(ns) + 1):
        ans = min(ans, sum((1 + abs(x - n)) * (abs(x - n)) // 2 for x in ns))
    return ans
