import math


def p1(data: str):
    dt = int(data.splitlines()[0])
    ans = dt, -1
    for line in data.splitlines()[1].split(','):
        if line == 'x':
            continue
        x = int(line)
        r = math.ceil(dt / x) * x - dt
        if r < ans[0]:
            ans = r, x
    return math.prod(ans)
