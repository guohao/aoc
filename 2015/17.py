import itertools


def p1(data: str):
    cs = list(map(int, data.splitlines()))
    ans = 0
    for i in range(1, len(cs)):
        for c in itertools.combinations(cs, i):
            if sum(c) == 150:
                ans += 1
    return ans


def p1(data: str):
    cs = list(map(int, data.splitlines()))
    for i in range(1, len(cs)):
        ans = 0
        for c in itertools.combinations(cs, i):
            if sum(c) == 150:
                ans += 1
        if ans:
            return ans
