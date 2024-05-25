from util import ints


def p1(data: str):
    ans = 1
    for t, d in zip(*map(ints, data.splitlines())):
        ans *= sum((t - j) * j > d for j in range(t))
    return ans


def p2(data: str):
    return p1(data.replace(' ', ''))
