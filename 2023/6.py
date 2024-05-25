from util import ints


def p1(data: str):
    lines = data.splitlines()
    t = ints(lines[0])
    d = ints(lines[1])
    ans = 1
    for i in range(len(t)):
        ans *= sum((t[i] - j) * j > d[i] for j in range(t[i]))
    return ans


def p2(data: str):
    lines = data.replace(' ', '').splitlines()
    t = ints(lines[0])[0]
    d = ints(lines[1])[0]
    return sum((t - j) * j > d for j in range(t))
